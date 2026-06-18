/**
 * POST /api/audit  — free conversion-path website audit.
 *
 * Body: { "url": "https://example.com", "adminKey"?, "compare"? }
 * Returns: { ok, finalUrl, score, summary, summarySource, variant, findings[], passed[], speedPending }
 * Mobile speed is a separate phase-2 call — see functions/api/audit-speed.js.
 *
 * Server-side because: SSRF-guarded outbound fetch, response-size caps and
 * per-IP throttling must not run in the visitor's browser. No persistent
 * storage — nothing about the audited site is kept after the response.
 *
 * v2 — optional AI summary layer (degrades to the template without config):
 *   LLM_API_KEY      secret; enables AI summaries (Nous portal / OpenRouter key)
 *   LLM_BASE_URL     OpenAI-compatible base, default https://inference-api.nousresearch.com/v1
 *   LLM_MODELS       comma list, default "deepseek/deepseek-v4-flash,nousresearch/hermes-4-70b" — random A/B per audit
 *   LLM_MONTHLY_CAP  max AI calls per calendar month (default 3000; enforced when RATE_KV is bound)
 *   ADMIN_KEY        with body.adminKey + body.compare, runs ALL models side by side (QA mode)
 *   RATE_KV          optional KV binding for the monthly AI-call budget
 */
import { pickModel, buildLlmMessages, buildAiReadMessages, callLlm } from '../_lib/llm.mjs';
import { pickLang, localizeFindings, localizePassed, localizedSummary, errMsg } from '../_lib/audit-i18n.mjs';
import { normalizeUrl, ssrfBlocked } from '../_lib/audit-net.mjs';

const MAX_BODY_BYTES = 1_500_000;
const FETCH_TIMEOUT_MS = 10_000;
const MAX_REDIRECTS = 4;
const RATE_LIMIT = 5; // requests per IP per window
const RATE_WINDOW_MS = 60_000;

const ipHits = new Map(); // per-isolate best-effort limiter

export async function onRequestPost(context) {
  const ip = context.request.headers.get('cf-connecting-ip') || 'unknown';
  let lang = 'en';
  try { lang = pickLang(new URL(context.request.url).searchParams.get('lang')); } catch { /* default en */ }
  if (rateLimited(ip)) {
    return json({ ok: false, error: 'rate_limited', message: errMsg('rate_limited', lang, 'Too many audits from this connection. Try again in a minute.') }, 429);
  }

  let target;
  let body = {};
  try {
    body = await context.request.json();
    target = normalizeUrl(String(body.url || ''));
  } catch {
    return json({ ok: false, error: 'bad_request', message: errMsg('bad_request', lang, 'Send JSON: {"url": "https://example.com"}') }, 400);
  }
  if (!target) {
    return json({ ok: false, error: 'invalid_url', message: errMsg('invalid_url', lang, 'That does not look like a public website address.') }, 400);
  }
  const blocked = ssrfBlocked(target);
  if (blocked) {
    return json({ ok: false, error: 'blocked_url', message: blocked }, 400);
  }

  let page;
  try {
    page = await guardedFetch(target);
  } catch (e) {
    return json({ ok: false, error: 'fetch_failed', message: errMsg('fetch_prefix', lang, 'Could not load that site') + ' (' + (e && e.message ? e.message : 'network error') + '). ' + errMsg('fetch_suffix', lang, 'Is it online and public?') }, 502);
  }

  // Mobile speed (PageSpeed Insights) is measured in a separate phase-2 call
  // (/api/audit-speed) so this response is fast and never blocks on Google's
  // 15-30s API. The client streams the speed card in and adjusts the score.
  const { findings, passed } = runChecks(page);
  const meta = parseMeta(page);

  const findingsL = localizeFindings(findings, lang);
  const passedL = localizePassed(passed, lang);
  const { score, summary: enSummary } = scoreAndSummarize(findingsL, page);
  const templateSummary = lang === 'en' ? enSummary : (localizedSummary(findingsL, lang) || enSummary);

  // --- AI summary layer (A/B between configured models; template is the fallback) ---
  const env = context.env || {};
  const isAdmin = Boolean(env.ADMIN_KEY && body.adminKey === env.ADMIN_KEY);
  let summary = templateSummary;
  let summarySource = 'template';
  let variant = null;
  let modelUsed = null;
  let usage = null;
  let compare = null;
  let aiRead = null;
  let aiReadDbg = null;

  if (env.LLM_API_KEY && (await llmBudgetOk(env))) {
    const models = String(env.LLM_MODELS || 'deepseek/deepseek-v4-flash,nousresearch/hermes-4-70b')
      .split(',').map((s) => s.trim()).filter(Boolean);
    const messages = buildLlmMessages(findingsL, page.finalUrl, score, lang);
    if (isAdmin && body.compare) {
      compare = await Promise.all(models.map(async (m) => {
        const r = await callLlm(env, m, messages);
        return { model: m, summary: r.text || null, error: r.error || null, usage: r.usage || null };
      }));
      const first = compare.find((c) => c.summary);
      if (first) { summary = first.summary; summarySource = 'llm'; }
    } else {
      const idx = Math.floor(Math.random() * models.length);
      modelUsed = pickModel(models, idx / models.length);
      // Two LLM passes in parallel: the plain-language summary + the structured "AI read"
      // (5-second clarity + AI-search readiness). Parallel so phase 1 stays fast.
      const aiMsgs = buildAiReadMessages(visibleText(page.html), meta.host, lang, {
        hasSchema: passed.includes('schema'),
        hasBusinessSchema: passed.includes('business_schema'),
        hasContact: passed.includes('contact'),
      });
      // AI read always uses the first (fastest) model + a longer budget — structured
      // JSON generation is slower and was timing out on the larger A/B model. One
      // quick retry on an empty/errored response (transient provider hiccups).
      const [r, ar] = await Promise.all([
        callLlm(env, modelUsed, messages),
        (async () => {
          const ex = { max_tokens: 1200, temperature: 0.2 };
          let x = await callLlm(env, models[0], aiMsgs, 20_000, ex);
          if (!x.text) x = await callLlm(env, models[0], aiMsgs, 12_000, ex);
          return x;
        })(),
      ]);
      if (r.text) {
        summary = r.text;
        summarySource = 'llm';
        variant = String.fromCharCode(65 + idx); // 'A' | 'B' | ...
        usage = r.usage;
      }
      if (ar.text) aiRead = parseAiRead(ar.text);
      aiReadDbg = { hasText: Boolean(ar.text), err: ar.error || null, parsed: Boolean(aiRead), sample: (ar.text || '').slice(0, 500) };
    }
  }

  const payload = {
    ok: true,
    finalUrl: page.finalUrl,
    score,
    summary,
    summarySource,
    variant,
    findings: findingsL.sort((a, b) => sevRank(b.severity) - sevRank(a.severity)),
    passed: passedL,
    meta,
    aiRead,
    aiReadDebug: aiReadDbg,
    speedPending: true,
  };
  if (isAdmin) {
    payload.model = modelUsed;
    payload.usage = usage;
    if (compare) payload.compare = compare;
  }
  return json(payload);
}

// Monthly AI-call budget. Without a KV binding we allow (per-IP limiting +
// a provider-side key limit are the backstop); with KV the cap is global.
async function llmBudgetOk(env) {
  const kv = env.RATE_KV;
  if (!kv) return true;
  try {
    const monthKey = 'llm:' + new Date().toISOString().slice(0, 7);
    const used = Number((await kv.get(monthKey)) || 0);
    if (used >= Number(env.LLM_MONTHLY_CAP || 3000)) return false;
    await kv.put(monthKey, String(used + 1), { expirationTtl: 3_200_000 });
    return true;
  } catch {
    return true;
  }
}

/* ---------------- helpers ---------------- */

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
  });
}

function rateLimited(ip) {
  const now = Date.now();
  const rec = ipHits.get(ip) || [];
  const fresh = rec.filter((t) => now - t < RATE_WINDOW_MS);
  fresh.push(now);
  ipHits.set(ip, fresh);
  if (ipHits.size > 5000) ipHits.clear(); // memory guard
  return fresh.length > RATE_LIMIT;
}

async function guardedFetch(startUrl) {
  let url = startUrl;
  for (let hop = 0; hop <= MAX_REDIRECTS; hop++) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);
    let res;
    try {
      res = await fetch(url.toString(), {
        redirect: 'manual',
        signal: controller.signal,
        headers: {
          'user-agent': 'Mozilla/5.0 (compatible; CamelotFlowsAudit/1.0; +https://camelotflows.dev/audit)',
          'accept': 'text/html,application/xhtml+xml',
          'accept-language': 'en,ro;q=0.9,ru;q=0.8',
        },
      });
    } finally {
      clearTimeout(timer);
    }
    if (res.status >= 300 && res.status < 400) {
      const loc = res.headers.get('location');
      if (!loc) throw new Error('redirect without target');
      const next = new URL(loc, url);
      const blocked = ssrfBlocked(next);
      if (blocked) throw new Error('redirects to a blocked address');
      url = next;
      continue;
    }
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const reader = res.body.getReader();
    let received = 0;
    const chunks = [];
    while (received < MAX_BODY_BYTES) {
      const { done, value } = await reader.read();
      if (done) break;
      chunks.push(value);
      received += value.length;
    }
    try { await reader.cancel(); } catch { /* already done */ }
    const buf = new Uint8Array(received);
    let off = 0;
    for (const c of chunks) { buf.set(c.subarray(0, Math.min(c.length, received - off)), off); off += c.length; if (off >= received) break; }
    const html = new TextDecoder('utf-8', { fatal: false }).decode(buf);
    return { finalUrl: url.toString(), https: url.protocol === 'https:', status: res.status, html };
  }
  throw new Error('too many redirects');
}

function f(id, severity, title, detail, vars) {
  return { id, severity, title, detail, vars };
}
function sevRank(s) { return s === 'high' ? 3 : s === 'medium' ? 2 : 1; }

function decodeEntities(s) {
  if (!s) return '';
  return s
    .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"').replace(/&#0?39;|&apos;/g, "'").replace(/&nbsp;/g, ' ')
    .replace(/&#(\d+);/g, (m, n) => { try { return String.fromCharCode(+n); } catch { return m; } })
    .trim();
}

// Parse the visible-identity fields used for the SERP / social-share previews.
function parseMeta(page) {
  const html = page.html;
  const grab = (re) => { const x = html.match(re); return x ? x[1].trim() : ''; };
  const metaContent = (name, attr) =>
    grab(new RegExp('<meta[^>]+' + attr + '\\s*=\\s*["\']' + name + '["\'][^>]+content\\s*=\\s*["\']([^"\']*)["\']', 'i')) ||
    grab(new RegExp('<meta[^>]+content\\s*=\\s*["\']([^"\']*)["\'][^>]+' + attr + '\\s*=\\s*["\']' + name + '["\']', 'i'));
  const title = grab(/<title[^>]*>([\s\S]*?)<\/title>/i);
  let host = '';
  try { host = new URL(page.finalUrl).hostname.replace(/^www\./, ''); } catch { /* ignore */ }
  let ogImage = metaContent('og:image', 'property') || metaContent('twitter:image', 'name');
  if (ogImage) { try { ogImage = new URL(ogImage, page.finalUrl).toString(); } catch { /* keep as-is */ } }
  return {
    host,
    url: page.finalUrl,
    title: decodeEntities(title).slice(0, 180),
    description: decodeEntities(metaContent('description', 'name')).slice(0, 320),
    ogTitle: decodeEntities(metaContent('og:title', 'property')).slice(0, 180),
    ogDescription: decodeEntities(metaContent('og:description', 'property')).slice(0, 320),
    ogImage: /^https?:\/\//i.test(ogImage) ? ogImage.slice(0, 600) : '',
  };
}

// Strip tags/scripts to a plain-text snippet for the "AI read" prompt.
function visibleText(html) {
  return String(html || '')
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<noscript[\s\S]*?<\/noscript>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&[a-z#0-9]+;/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 2400);
}

// Tolerant parse of the AI-read JSON (model output is untrusted and often slightly
// off: markdown fences, trailing commas, ok as a string, clarity item as a string).
function parseAiRead(s) {
  try {
    let t = String(s).trim().replace(/^```[a-z]*\s*/i, '').replace(/```\s*$/i, '').trim();
    const a = t.indexOf('{'), b = t.lastIndexOf('}');
    if (a < 0 || b < 0) return null;
    const js = t.slice(a, b + 1).replace(/,(\s*[}\]])/g, '$1'); // strip trailing commas
    const o = JSON.parse(js);
    if (!o || typeof o !== 'object' || !o.clarity || !o.aeo) return null;
    const truthy = (v) => v === true || v === 1 || /^(true|yes|ok|pass|good)$/i.test(String(v || ''));
    const norm = (x) => {
      if (x == null) return null;
      if (typeof x === 'string') return { ok: true, note: x.slice(0, 220) };
      if (typeof x === 'object') return { ok: truthy(x.ok), note: String(x.note || x.text || x.reason || '').slice(0, 220) };
      return null;
    };
    const what = norm(o.clarity.what), who = norm(o.clarity.who), why = norm(o.clarity.why);
    if (!what || !who || !why) return null;
    let ready = String(o.aeo.ready || '').toLowerCase().trim();
    if (!['yes', 'partial', 'no'].includes(ready)) ready = /(^|[^a-z])(yes|ready)([^a-z]|$)/.test(ready) ? 'yes' : (/(^|[^a-z])no([^a-z]|$)/.test(ready) ? 'no' : 'partial');
    const reasons = Array.isArray(o.aeo.reasons) ? o.aeo.reasons.slice(0, 3).map((r) => String(r).slice(0, 160)).filter(Boolean) : [];
    return { clarity: { what, who, why }, aeo: { ready, note: String(o.aeo.note || '').slice(0, 260), reasons } };
  } catch {
    return null;
  }
}

function runChecks(page) {
  const html = page.html;
  const lower = html.toLowerCase();
  const findings = [];
  const passed = [];

  // -- HTTPS --
  if (!page.https) {
    findings.push(f('https', 'high', 'Site served over plain HTTP',
      'Browsers mark the site “Not secure” next to your business name. This alone turns visitors away.'));
  } else {
    passed.push('https');
  }

  // -- click-to-call --
  const telLinks = [...html.matchAll(/href\s*=\s*["']tel:([^"']*)["']/gi)].map((x) => x[1].trim());
  const phonePattern = /(?:\+?\d[\d\s().-]{7,}\d)/;
  const visiblePhone = phonePattern.test(html.replace(/<script[\s\S]*?<\/script>/gi, ''));
  const brokenTel = telLinks.filter((t) => !t || /[^\d+()\-. %]/.test(t) || t.replace(/\D/g, '').length < 6);
  if (telLinks.length === 0 && visiblePhone) {
    findings.push(f('tel_missing', 'high', 'Phone number is not tappable',
      'A phone number appears on the page but it is not a tel: link. On mobile — where most local customers are — they have to memorize and retype it. Calls are lost exactly there.'));
  }
  if (brokenTel.length > 0) {
    const bvals = brokenTel.slice(0, 3).map((t) => '“' + (t || 'empty') + '”').join(', ');
    findings.push(f('tel_broken', 'high', brokenTel.length + ' broken click-to-call link' + (brokenTel.length > 1 ? 's' : ''),
      'tel: links exist but their targets are malformed (' + bvals + '). Tapping them does nothing — the most expensive kind of silent defect for a service business.',
      { count: brokenTel.length, vals: bvals }));
  } else if (telLinks.length > 0) {
    passed.push('tappable_phone');
  }

  // -- contact path --
  const hasForm = /<form[\s>]/i.test(html);
  const hasMailto = /href\s*=\s*["']mailto:/i.test(html);
  const hasContactLink = /href\s*=\s*["'][^"']*(contact|kontakt|contacte|контакт)[^"']*["']/i.test(html);
  if (!hasForm && !hasMailto && telLinks.length === 0 && !hasContactLink) {
    findings.push(f('no_contact_path', 'high', 'No obvious way to contact you',
      'No form, no email link, no tappable phone, no contact page link found on this page. A visitor who is ready to buy has to work to reach you — most won’t.'));
  } else {
    passed.push('contact');
  }

  // -- structured data --
  const ldBlocks = [...html.matchAll(/<script[^>]*type\s*=\s*["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)];
  let hasLocalBusiness = false, hasOrg = false, hasSelfRating = false;
  for (const b of ldBlocks) {
    let txt = b[1];
    try {
      const data = JSON.parse(txt);
      const nodes = [].concat(data['@graph'] || data);
      for (const n of nodes) {
        if (!n || typeof n !== 'object') continue;
        const t = String(n['@type'] || '');
        if (/LocalBusiness|Store|HomeAndConstructionBusiness|ProfessionalService|Dentist|Attorney|Plumber|Electrician|AutoRepair/i.test(t)) hasLocalBusiness = true;
        if (/Organization/i.test(t)) hasOrg = true;
        if (n.aggregateRating && /LocalBusiness|Organization|Store|ProfessionalService/i.test(t)) hasSelfRating = true;
      }
    } catch { /* unparseable JSON-LD ignored */ }
  }
  if (ldBlocks.length === 0) {
    findings.push(f('no_schema', 'medium', 'No structured data at all',
      'Google and AI assistants read schema.org markup to understand who you are, where you operate and what you sell. Without it you are a plain wall of text to them.'));
  } else {
    passed.push('schema');
    if (!hasLocalBusiness && !hasOrg) {
      findings.push(f('no_business_schema', 'medium', 'No LocalBusiness / Organization schema',
        'Structured data exists but nothing identifies the business itself — name, area served, phone. That is the block local search and AI assistants actually use.'));
    } else {
      passed.push('business_schema');
    }
  }
  if (hasSelfRating) {
    findings.push(f('self_rating', 'medium', 'Self-serving star rating markup',
      'aggregateRating on your own business entity violates Google’s structured-data guidelines and can earn a manual action. Stars belong on third-party review platforms.'));
  }

  // -- title --
  const titleM = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  const title = titleM ? titleM[1].trim() : '';
  if (!title) {
    findings.push(f('no_title', 'high', 'Missing page title',
      'The <title> tag is the headline of your Google result. Without it, Google improvises one for you.'));
  } else if (title.length < 15) {
    findings.push(f('thin_title', 'low', 'Page title is very short (“' + title.slice(0, 40) + '”)',
      'Short generic titles waste the single most valuable SEO field on the page.',
      { title: title.slice(0, 40) }));
  } else {
    passed.push('title');
  }

  // -- meta description --
  if (!/<meta[^>]+name\s*=\s*["']description["'][^>]*content\s*=\s*["'][^"']{20,}/i.test(html)) {
    findings.push(f('no_meta_desc', 'medium', 'Missing meta description',
      'This is the sales copy under your Google listing. When absent, Google picks a random sentence — rarely the one that sells.'));
  } else {
    passed.push('meta_desc');
  }

  // -- Open Graph --
  if (!/<meta[^>]+property\s*=\s*["']og:title["']/i.test(html)) {
    findings.push(f('no_og', 'low', 'No social sharing tags (Open Graph)',
      'When someone shares your site in WhatsApp, Viber or Facebook, the preview is blank or random. Shares without previews get fewer clicks.'));
  } else {
    passed.push('og');
  }

  // -- mobile viewport --
  if (!/<meta[^>]+name\s*=\s*["']viewport["']/i.test(html)) {
    findings.push(f('no_viewport', 'high', 'Not mobile-ready (no viewport tag)',
      'Without a viewport meta tag, phones render the desktop layout zoomed out. Most local-business traffic is mobile.'));
  } else {
    passed.push('viewport');
  }

  // -- h1 --
  const h1Count = (lower.match(/<h1[\s>]/g) || []).length;
  if (h1Count === 0) {
    findings.push(f('no_h1', 'low', 'No H1 heading',
      'Search engines treat the H1 as the page’s topic statement. Missing it weakens an easy relevance signal.'));
  } else {
    passed.push('h1');
  }

  // -- hreflang sanity (multilingual markets) --
  const hreflangs = [...html.matchAll(/hreflang\s*=\s*["']([^"']+)["']/gi)].map((x) => x[1]);
  const langAttr = html.match(/<html[^>]+lang\s*=\s*["']([^"']+)["']/i);
  if (hreflangs.length === 1) {
    findings.push(f('hreflang_single', 'low', 'Incomplete hreflang set',
      'Only one hreflang alternate is declared. A set needs every language version plus x-default, otherwise it does nothing.'));
  }
  if (!langAttr) {
    findings.push(f('no_lang', 'low', 'Missing lang attribute on <html>',
      'Screen readers and search engines have to guess the page language.'));
  } else {
    passed.push('lang');
  }

  // -- favicon (small trust touch) --
  if (!/rel\s*=\s*["'](?:shortcut )?icon["']/i.test(html)) {
    findings.push(f('no_favicon', 'low', 'No favicon declared',
      'The browser-tab icon is a small thing — its absence reads as “unfinished” in a tab bar full of polished competitors.'));
  } else {
    passed.push('favicon');
  }

  return { findings, passed };
}

function scoreAndSummarize(findings, page) {
  let score = 100;
  for (const x of findings) {
    score -= x.severity === 'high' ? 18 : x.severity === 'medium' ? 9 : 4;
  }
  score = Math.max(5, Math.min(100, score));

  const highs = findings.filter((x) => x.severity === 'high').length;
  const meds = findings.filter((x) => x.severity === 'medium').length;
  let summary;
  if (findings.length === 0) {
    summary = 'Clean pass — none of the usual conversion-path defects showed up on this page. The remaining wins are in copy, offer and speed tuning rather than broken plumbing.';
  } else if (highs > 0) {
    summary = highs + ' issue' + (highs > 1 ? 's' : '') + ' found that actively lose' + (highs > 1 ? '' : 's') + ' you enquiries — plus ' + (meds + (findings.length - highs - meds)) + ' smaller one' + (findings.length - highs > 1 ? 's' : '') + '. The high-severity items are the kind a visitor hits, fails silently, and never tells you about.';
  } else {
    summary = 'No conversion-killers found, but ' + findings.length + ' improvement' + (findings.length > 1 ? 's' : '') + ' would tighten how search engines and visitors read the site.';
  }
  return { score, summary };
}
