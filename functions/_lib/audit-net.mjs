// Shared network helpers for the audit endpoints (main audit + phase-2 speed).
// Kept SSRF-guarded and timeout-bounded; no persistent storage.

export function normalizeUrl(raw) {
  let s = String(raw || '').trim();
  if (!s) return null;
  if (!/^https?:\/\//i.test(s)) s = 'https://' + s;
  let u;
  try { u = new URL(s); } catch { return null; }
  if (u.protocol !== 'http:' && u.protocol !== 'https:') return null;
  if (u.username || u.password) return null;
  return u;
}

export function ssrfBlocked(u) {
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

// Google PageSpeed Insights (mobile, performance). Best-effort; returns null on
// any failure or timeout. timeoutMs is generous when called as its own phase
// (PSI routinely takes 15-30s). apiKey lifts the unkeyed rate limit when set.
export async function fetchPsi(url, timeoutMs = 25_000, apiKey = '') {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    let api = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?strategy=mobile&category=performance&url=' + encodeURIComponent(url);
    if (apiKey) api += '&key=' + encodeURIComponent(apiKey);
    const res = await fetch(api, { signal: controller.signal });
    if (!res.ok) return null;
    const data = await res.json();
    const lh = data.lighthouseResult || {};
    const audits = lh.audits || {};
    const shot = audits['final-screenshot'] && audits['final-screenshot'].details ? audits['final-screenshot'].details.data : null;
    return {
      performance: lh.categories && lh.categories.performance ? Math.round(lh.categories.performance.score * 100) : null,
      lcp_ms: audits['largest-contentful-paint'] ? Math.round(audits['largest-contentful-paint'].numericValue) : null,
      cls: audits['cumulative-layout-shift'] ? +audits['cumulative-layout-shift'].numericValue.toFixed(3) : null,
      screenshot: typeof shot === 'string' && shot.startsWith('data:image/') ? shot : null,
    };
  } catch {
    return null;
  } finally {
    clearTimeout(timer);
  }
}
