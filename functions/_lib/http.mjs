/**
 * Shared JSON response helper for the /api/* Pages Functions.
 *
 * Why this exists: Cloudflare Pages applies the root `_headers` file to STATIC
 * ASSETS ONLY — it does NOT touch a response returned by a Pages Function. That
 * gap is easy to miss from the outside, and we did miss it: a `/api/*` path with
 * no Function behind it (e.g. `/api/nonexistent-endpoint`) falls through to the
 * static `404.html` and DOES carry the `_headers` set, so spot-checking such a
 * path reports a false "4/4 headers on /api/*" and hides the real behaviour.
 *
 * Measured live 2026-07-17: `/api/audit` -> 400 with 0/4 security headers, while
 * `/`, `/audit`, `/contact`, `/blog/` and `/api/nonexistent-endpoint` all served
 * 4/4. This module closes that gap at the single choke-point every /api/*
 * response already flows through.
 *
 * Impact, stated honestly: LOW. `/api/*` returns JSON, which is not
 * clickjackable, so X-Frame-Options / frame-ancestors buy little here; and HSTS
 * is already pinned host-wide by every HTML response on this origin, so browsers
 * force HTTPS on /api/* regardless. The value is uniformity — posture should not
 * depend on whether a route happens to be a Function, a future Function that
 * returns HTML would otherwise ship bare, and the docs should describe something
 * that is actually true.
 *
 * KEEP IN SYNC with `_headers` at the repo root: that file governs static
 * assets, this object governs Function responses. They must not drift.
 * Deliberately mirrors `_headers` exactly, including the two decisions recorded
 * there — HSTS carries no `preload` (irreversible, needs owner sign-off) and the
 * CSP is scoped to `frame-ancestors` only (an unscoped policy would break the
 * inline scripts, GA4, Tailwind and Web3Forms the site depends on).
 */
export const SECURITY_HEADERS = {
  'strict-transport-security': 'max-age=31536000; includeSubDomains',
  'x-frame-options': 'DENY',
  'content-security-policy': "frame-ancestors 'none'",
  'permissions-policy': 'geolocation=(), microphone=(), camera=()',
};

/**
 * JSON response carrying the security headers. Every /api/* return — success,
 * 400, 404, 429 and 500 alike — goes through this one helper, so the error
 * paths are covered too, not just the happy path.
 */
export function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'cache-control': 'no-store',
      ...SECURITY_HEADERS,
    },
  });
}
