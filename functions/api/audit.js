/**
 * POST /api/audit  — free conversion-path website audit.
 *
 * Body: { "url": "https://example.com", "adminKey"?, "compare"? }
 * Returns: { ok, finalUrl, score, summary, summarySource, variant, findings[], psi|null }
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
import { pickModel, buildLlmMessages, callLlm } from '../_lib/llm.mjs';

const MAX_BODY_BYTES = 1_500_000;
const FETCH_TIMEOUT_MS = 10_000;
const PSI_TIMEOUT_MS = 12_000;
const MAX_REDIRECTS = 4;
const RATE_LIMIT = 5; // requests per IP per window
const RATE_WINDOW_MS = 60_000;

const ipHits = new Map(); // per-isolate best-effort limiter

export async function onRequestPost(context) {
  const ip = context.request.headers.get('cf-connecting-ip') || 'unknown';
  if (rateLimited(ip)) {
    return json({ ok: false, error: 'rate_limited', message: 'Too many audits from this connection. Try again in a minute.' }, 429);
  }

  let target;
  let body = {};
  try {
    body = await context.request.json();
    target = normalizeUrl(String(body.url || ''));
  } catch {
    return json({ ok: false, error: 'bad_request', message: 'Send JSON: {"url": "https://example.com"}' }, 400);
  }
  if (!target) {
    return json({ ok: false, error: 'invalid_url', message: 'That does not look like a public website address.' }, 400);
  }
  const blocked = ssrfBlocked(target);
  if (blocked) {
    return json({ ok: false, error: 'blocked_url', message: blocked }, 400);
  }

  let page;
  try {
    page = await guardedFetch(target);
  } catch (e) {
    return json({ ok: false, error: 'fetch_failed', message: 'Could not load that site (' + (e && e.message ? e.message : 'network error') + '). Is it online and public?' }, 502);
  }

  const findings = runChecks(page);

  // PageSpeed Insights (free API) — optional, never blocks the audit.
  let psi = null;
  try {
    psi = await fetchPsi(page.finalUrl);
    if (psi) {
      if (psi.performance !== null && psi.performance < 50) {
        findings.push(f('slow_mobile', 'high', 'Slow on mobile',
          'Google PageSpeed scores this page ' + psi.performance + '/100 on a mobile connection. Visitors on phones bounce before slow pages finish loading.'));
      } else if (psi.performance !== null && psi.performance < 80) {
        findings.push(f('mediocre_mobile', 'medium', 'Mobile speed has headroom',
          'Mobile performance score is ' + psi.performance + '/100. Not broken, but every second of load time costs conversions.'));
      }
      if (psi.lcp_ms !== null && psi.lcp_ms > 4000) {
        findings.push(f('lcp', 'high', 'Main content takes ' + (psi.lcp_ms / 1000).toFixed(1) + 's to appear (LCP)',
          'Largest Contentful Paint above 4 seconds is in Google’s “poor” band — it hurts both rankings and patience.'));
      }
    }
  } catch { /* PSI is best-effort */ }

  const { score, summary: templateSummary } = scoreAndSummarize(findings, page);

  // --- AI summary layer (A/B between configured models; template is the fallback) ---
  const env = context.env || {};
  const isAdmin = Boolean(env.ADMIN_KEY && body.adminKey === env.ADMIN_KEY);
  let summary = templateSummary;
  let summarySource = 'template';
  let variant = null;
  let modelUsed = null;
  let usage = null;
  let compare = null;

  if (env.LLM_API_KEY && (await llmBudgetOk(env))) {
    const models = String(env.LLM_MODELS || 'deepseek/deepseek-v4-flash,nousresearch/hermes-4-70b')
      .split(',').map((s) => s.trim()).filter(Boolean);
    const messages = buildLlmMessages(findings, page.finalUrl, score);
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
      const r = await callLlm(env, modelUsed, messages);
      if (r.text) {
        summary = r.text;
        summarySource = 'llm';
        variant = String.fromCharCode(65 + idx); // 'A' | 'B' | ...
        usage = r.usage;
      }
    }
  }

  const payload = {
    ok: true,
    finalUrl: page.finalUrl,
    score,
    summary,
    summarySource,
    variant,
    findings: findings.sort((a, b) => sevRank(b.severity) - sevRank(a.severity)),
    psi,
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

function normalizeUrl(raw) {
  let s = raw.trim();
  if (!s) return null;
  if (!/^https?:\/\//i.test(s)) s = 'https://' + s;
  let u;
  try { u = new URL(s); } catch { return null; }
  if (u.protocol !== 'http:' && u.protocol !== 'https:') return null;
  if (u.username || u.password) return null;
  return u;
}

function ssrfBlocked(u) {
  const host = u.hostname.toLowerCase();
  if (u.port && u.port !== '80' && u.port !== '443') return 'Only standard web ports are audited.';
  if (host === 'localhost' || host.endsWith('.localhost') || host.endsWith('.local') ||
      host.endsWith('.internal') || host.endsWith('.lan') || !host.includes('.')) {
    return 'Internal or local addresses cannot be audited.';
  }
  // IPv6 literal
  if (host.startsWith('[') || host.includes(':')) return 'IP-literal addresses cannot be audited — use the domain name.';
  // IPv4 literal
  const m = host.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/);
  if (m) {
    const a = +m[1], b = +m[2];
    if (a === 10 || a === 127 || a === 0 ||
        (a === 172 && b >= 16 && b <= 31) ||
        (a === 192 && b === 168) ||
        (a === 169 && b === 254) || a >= 224) {
      return 'Private or reserved network addresses cannot be audited.';
    }
    return 'IP addresses cannot be audited — use the domain name.';
  }
  return null;
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

function f(id, severity, title, detail) {
  return { id, severity, title, detail };
}
function sevRank(s) { return s === 'high' ? 3 : s === 'medium' ? 2 : 1; }

function runChecks(page) {
  const html = page.html;
  const lower = html.toLowerCase();
  const findings = [];

  // -- HTTPS --
  if (!page.https) {
    findings.push(f('https', 'high', 'Site served over plain HTTP',
      'Browsers mark the site “Not secure” next to your business name. This alone turns visitors away.'));
  }

  // -- click-to-call --
  const telLinks = [...html.matchAll(/href\s*=\s*["']tel:([^"']*)["']/gi)].map((x) => x[1].trim());
  const phonePattern = /(?:\+?\d[\d\s().-]{7,}\d)/;
  const visiblePhone = phonePattern.test(html.replace(/<script[\s\S]*?<\/script>/gi, ''));
  if (telLinks.length === 0 && visiblePhone) {
    findings.push(f('tel_missing', 'high', 'Phone number is not tappable',
      'A phone number appears on the page but it is not a tel: link. On mobile — where most local customers are — they have to memorize and retype it. Calls are lost exactly there.'));
  }
  const brokenTel = telLinks.filter((t) => !t || /[^\d+()\-. %]/.test(t) || t.replace(/\D/g, '').length < 6);
  if (brokenTel.length > 0) {
    findings.push(f('tel_broken', 'high', brokenTel.length + ' broken click-to-call link' + (brokenTel.length > 1 ? 's' : ''),
      'tel: links exist but their targets are malformed (' + brokenTel.slice(0, 3).map((t) => '“' + (t || 'empty') + '”').join(', ') + '). Tapping them does nothing — the most expensive kind of silent defect for a service business.'));
  }

  // -- contact path --
  const hasForm = /<form[\s>]/i.test(html);
  const hasMailto = /href\s*=\s*["']mailto:/i.test(html);
  const hasContactLink = /href\s*=\s*["'][^"']*(contact|kontakt|contacte|контакт)[^"']*["']/i.test(html);
  if (!hasForm && !hasMailto && telLinks.length === 0 && !hasContactLink) {
    findings.push(f('no_contact_path', 'high', 'No obvious way to contact you',
      'No form, no email link, no tappable phone, no contact page link found on this page. A visitor who is ready to buy has to work to reach you — most won’t.'));
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
  } else if (!hasLocalBusiness && !hasOrg) {
    findings.push(f('no_business_schema', 'medium', 'No LocalBusiness / Organization schema',
      'Structured data exists but nothing identifies the business itself — name, area served, phone. That is the block local search and AI assistants actually use.'));
  }
  if (hasSelfRating) {
    findings.push(f('self_rating', 'medium', 'Self-serving star rating markup',
      'aggregateRating on your own business entity violates Google’s structured-data guidelines and can earn a manual action. Stars belong on third-party review platforms.'));
  }

  // -- title / meta description / OG --
  const titleM = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  const title = titleM ? titleM[1].trim() : '';
  if (!title) {
    findings.push(f('no_title', 'high', 'Missing page title',
      'The <title> tag is the headline of your Google result. Without it, Google improvises one for you.'));
  } else if (title.length < 15) {
    findings.push(f('thin_title', 'low', 'Page title is very short (“' + title.slice(0, 40) + '”)',
      'Short generic titles waste the single most valuable SEO field on the page.'));
  }
  if (!/<meta[^>]+name\s*=\s*["']description["'][^>]*content\s*=\s*["'][^"']{20,}/i.test(html)) {
    findings.push(f('no_meta_desc', 'medium', 'Missing meta description',
      'This is the sales copy under your Google listing. When absent, Google picks a random sentence — rarely the one that sells.'));
  }
  if (!/<meta[^>]+property\s*=\s*["']og:title["']/i.test(html)) {
    findings.push(f('no_og', 'low', 'No social sharing tags (Open Graph)',
      'When someone shares your site in WhatsApp, Viber or Facebook, the preview is blank or random. Shares without previews get fewer clicks.'));
  }

  // -- mobile viewport --
  if (!/<meta[^>]+name\s*=\s*["']viewport["']/i.test(html)) {
    findings.push(f('no_viewport', 'high', 'Not mobile-ready (no viewport tag)',
      'Without a viewport meta tag, phones render the desktop layout zoomed out. Most local-business traffic is mobile.'));
  }

  // -- h1 --
  const h1Count = (lower.match(/<h1[\s>]/g) || []).length;
  if (h1Count === 0) {
    findings.push(f('no_h1', 'low', 'No H1 heading',
      'Search engines treat the H1 as the page’s topic statement. Missing it weakens an easy relevance signal.'));
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
  }

  // -- favicon (small trust touch) --
  if (!/rel\s*=\s*["'](?:shortcut )?icon["']/i.test(html)) {
    findings.push(f('no_favicon', 'low', 'No favicon declared',
      'The browser-tab icon is a small thing — its absence reads as “unfinished” in a tab bar full of polished competitors.'));
  }

  return findings;
}

async function fetchPsi(url) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), PSI_TIMEOUT_MS);
  try {
    const api = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?strategy=mobile&category=performance&url=' + encodeURIComponent(url);
    const res = await fetch(api, { signal: controller.signal });
    if (!res.ok) return null;
    const data = await res.json();
    const lh = data.lighthouseResult || {};
    const audits = lh.audits || {};
    return {
      performance: lh.categories && lh.categories.performance ? Math.round(lh.categories.performance.score * 100) : null,
      lcp_ms: audits['largest-contentful-paint'] ? Math.round(audits['largest-contentful-paint'].numericValue) : null,
      cls: audits['cumulative-layout-shift'] ? +audits['cumulative-layout-shift'].numericValue.toFixed(3) : null,
    };
  } finally {
    clearTimeout(timer);
  }
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
