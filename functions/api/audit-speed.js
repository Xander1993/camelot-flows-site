/**
 * POST /api/audit-speed  — phase 2 of the audit: mobile speed (PageSpeed Insights).
 *
 * Split out from /api/audit so the main report is fast and never blocks on
 * Google's 15-30s API. The client renders the report first, then calls this and
 * streams the speed card in, adjusting the score by `scoreDelta`.
 *
 * Body: { "url": "https://example.com", "lang"?: "en|ro|ru" }
 * Returns: { ok, measured, psi|null, findings[], passed[], scoreDelta }
 *
 * Optional env: PSI_KEY — a Google PageSpeed API key lifts the unkeyed rate limit.
 */
import { pickLang, localizeFindings, localizePassed, errMsg } from '../_lib/audit-i18n.mjs';
import { normalizeUrl, ssrfBlocked, fetchPsi } from '../_lib/audit-net.mjs';

const PSI_TIMEOUT_MS = 24_000;
const RATE_LIMIT = 10; // per IP per window (one per audit, plus slack)
const RATE_WINDOW_MS = 60_000;
const ipHits = new Map();

export async function onRequestPost(context) {
  const ip = context.request.headers.get('cf-connecting-ip') || 'unknown';
  let lang = 'en';
  try { lang = pickLang(new URL(context.request.url).searchParams.get('lang')); } catch { /* default en */ }

  if (rateLimited(ip)) {
    return json({ ok: false, error: 'rate_limited', message: errMsg('rate_limited', lang, 'Too many requests. Try again in a minute.') }, 429);
  }

  let target;
  try {
    const body = await context.request.json();
    target = normalizeUrl(String((body && body.url) || ''));
  } catch {
    return json({ ok: false, error: 'bad_request', message: errMsg('bad_request', lang, 'Send JSON: {"url": "https://example.com"}') }, 400);
  }
  if (!target) {
    return json({ ok: false, error: 'invalid_url', message: errMsg('invalid_url', lang, 'That does not look like a public website address.') }, 400);
  }
  if (ssrfBlocked(target)) {
    return json({ ok: false, error: 'blocked_url', message: 'That address cannot be audited.' }, 400);
  }

  const env = context.env || {};

  // Temporary diagnostic: /api/audit-speed?debug=1 reports the raw PSI status + error
  // snippet (never the key value) so we can see why a keyed call fails.
  if (new URL(context.request.url).searchParams.get('debug') === '1') {
    let api = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?strategy=mobile&category=performance&url=' + encodeURIComponent(target.toString());
    if (env.PSI_KEY) api += '&key=' + encodeURIComponent(env.PSI_KEY);
    let st = 0, snip = '';
    try { const r = await fetch(api); st = r.status; snip = (await r.text()).slice(0, 400); } catch (e) { snip = 'fetch err ' + (e && e.message); }
    return json({ debug: true, keyed: Boolean(env.PSI_KEY), psiStatus: st, snippet: snip });
  }

  const keyed = Boolean(env.PSI_KEY); // diagnostic only — never exposes the value
  let psi = null;
  try { psi = await fetchPsi(target.toString(), PSI_TIMEOUT_MS, env.PSI_KEY || ''); } catch { psi = null; }

  if (!psi) {
    // Couldn't measure (timeout / rate-limited / blocked). Report it honestly;
    // the rest of the audit already stands on its own.
    return json({ ok: true, measured: false, keyed, psi: null, findings: [], passed: [], scoreDelta: 0 });
  }

  const findings = [];
  const passed = [];

  if (psi.performance !== null && psi.performance < 50) {
    findings.push(f('slow_mobile', 'high', 'Slow on mobile',
      'Google PageSpeed scores this page ' + psi.performance + '/100 on a mobile connection. Visitors on phones bounce before slow pages finish loading.',
      { perf: psi.performance }));
  } else if (psi.performance !== null && psi.performance < 80) {
    findings.push(f('mediocre_mobile', 'medium', 'Mobile speed has headroom',
      'Mobile performance score is ' + psi.performance + '/100. Not broken, but every second of load time costs conversions.',
      { perf: psi.performance }));
  } else if (psi.performance !== null) {
    passed.push('fast_mobile');
  }

  if (psi.lcp_ms !== null && psi.lcp_ms > 4000) {
    findings.push(f('lcp', 'high', 'Main content takes ' + (psi.lcp_ms / 1000).toFixed(1) + 's to appear (LCP)',
      'Largest Contentful Paint above 4 seconds is in Google’s “poor” band — it hurts both rankings and patience.',
      { secs: (psi.lcp_ms / 1000).toFixed(1) }));
  }

  const findingsL = localizeFindings(findings, lang);
  const passedL = localizePassed(passed, lang);
  let scoreDelta = 0;
  for (const x of findingsL) scoreDelta -= (x.severity === 'high' ? 18 : x.severity === 'medium' ? 9 : 4);

  return json({ ok: true, measured: true, keyed, psi, findings: findingsL, passed: passedL, scoreDelta });
}

function f(id, severity, title, detail, vars) {
  return { id, severity, title, detail, vars };
}

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
  if (ipHits.size > 5000) ipHits.clear();
  return fresh.length > RATE_LIMIT;
}
