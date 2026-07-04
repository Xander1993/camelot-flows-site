// Integration tests for AUDIT-CHEAP-CHECKS: the extra signals lifted from the
// already-fetched HTML (image alt coverage, mixed content, redirect-chain length)
// plus the two same-origin existence probes (robots.txt / sitemap.xml).
// Drives the REAL handler functions/api/audit.js with a mocked global fetch, so
// guardedFetch, runChecks, addOriginProbes and localization all run for real.
// Run: node --test tests/cheapchecks.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { onRequestPost } from '../functions/api/audit.js';

// --- minimal Response stand-in (full control over redirects + streamed body) ---
function bodyFrom(str) {
  const bytes = new TextEncoder().encode(str || '');
  let sent = false;
  const reader = {
    async read() { if (sent) return { done: true, value: undefined }; sent = true; return { done: false, value: bytes }; },
    async cancel() {},
  };
  return { getReader() { return reader; }, async cancel() {} };
}
function resp({ status = 200, location = null, body = '' } = {}) {
  const h = new Map();
  if (location) h.set('location', location);
  return {
    status,
    ok: status >= 200 && status < 300,
    headers: { get: (k) => { const v = h.get(String(k).toLowerCase()); return v === undefined ? null : v; } },
    body: bodyFrom(body),
  };
}
const R404 = () => resp({ status: 404, body: 'not found' });
const R200 = (body = '') => resp({ status: 200, body });

function installFetch(routes) {
  const orig = globalThis.fetch;
  globalThis.fetch = async (url) => {
    const u = String(url);
    if (u.endsWith('/robots.txt')) return routes.robots(u);
    if (u.endsWith('/sitemap.xml')) return routes.sitemap(u);
    return routes.home(u);
  };
  return () => { globalThis.fetch = orig; };
}

let ipSeq = 0; // unique IP per audit so the in-memory rate limiter never trips
async function runAudit(routes, { lang = '', url = 'https://example.com' } = {}) {
  const restore = installFetch(routes);
  try {
    const ctx = {
      env: {}, // no LLM key, no RATE_KV -> template-only, fully offline
      request: {
        url: 'https://camelotflows.dev/api/audit' + (lang ? '?lang=' + lang : ''),
        headers: { get: (k) => (String(k).toLowerCase() === 'cf-connecting-ip' ? '10.0.0.' + (++ipSeq) : null) },
        json: async () => ({ url }),
      },
    };
    const res = await onRequestPost(ctx);
    return await res.json();
  } finally {
    restore();
  }
}

const fIds = (d) => (d.findings || []).map((x) => x.id);
const pIds = (d) => (d.passed || []).map((x) => x.id);
const find = (d, id) => (d.findings || []).find((x) => x.id === id);

// https page: 3 images (2 without alt), 2 http:// sub-resources => img_alt + mixed_content
const FINDINGS_HTML =
  '<!doctype html><html><head><title>Test Page Title Here</title></head><body>' +
  '<img src="http://cdn.test/a.jpg">' +
  '<img src="http://cdn.test/b.jpg">' +
  '<img src="/c.jpg" alt="c photo">' +
  '</body></html>';

// https page: every image has alt; the only http URL is in data-src (lazyload, not a
// loaded resource) => neither img_alt nor mixed_content should flag.
const PASS_HTML =
  '<!doctype html><html lang="en"><head><title>Good Page Title Here</title>' +
  '<meta name="viewport" content="width=device-width, initial-scale=1"></head><body>' +
  '<img src="https://cdn.test/a.jpg" alt="a">' +
  '<img data-src="http://lazy.test/b.jpg" src="https://cdn.test/b.jpg" alt="b">' +
  '</body></html>';

test('flags img_alt + mixed_content + missing robots/sitemap on a defective https page', async () => {
  const d = await runAudit({ home: () => R200(FINDINGS_HTML), robots: R404, sitemap: R404 });
  const ids = fIds(d);
  assert.ok(ids.includes('img_alt'), 'img_alt finding present');
  assert.ok(ids.includes('mixed_content'), 'mixed_content finding present');
  assert.ok(ids.includes('no_robots'), 'no_robots finding present');
  assert.ok(ids.includes('no_sitemap'), 'no_sitemap finding present');
  // severities
  assert.equal(find(d, 'img_alt').severity, 'low');
  assert.equal(find(d, 'mixed_content').severity, 'medium');
  // counts are surfaced honestly
  assert.match(find(d, 'img_alt').title, /2 of 3/);
  assert.match(find(d, 'mixed_content').title, /2 insecure resources/);
  // these must NOT also appear as passes
  const p = pIds(d);
  assert.ok(!p.includes('img_alt') && !p.includes('no_mixed_content') && !p.includes('robots') && !p.includes('sitemap'));
});

test('passes img_alt/no_mixed_content/robots/sitemap on a clean https page (data-src is not mixed content)', async () => {
  const d = await runAudit({
    home: () => R200(PASS_HTML),
    robots: () => R200('User-agent: *\nAllow: /'),
    sitemap: () => R200('<urlset></urlset>'),
  });
  const p = pIds(d);
  assert.ok(p.includes('img_alt'), 'img_alt passed');
  assert.ok(p.includes('no_mixed_content'), 'no_mixed_content passed (data-src ignored)');
  assert.ok(p.includes('robots'), 'robots passed');
  assert.ok(p.includes('sitemap'), 'sitemap passed');
  const ids = fIds(d);
  assert.ok(!ids.includes('img_alt') && !ids.includes('mixed_content') && !ids.includes('no_robots') && !ids.includes('no_sitemap'));
});

test('a Sitemap: directive in robots.txt counts as a sitemap even when /sitemap.xml is 404', async () => {
  const d = await runAudit({
    home: () => R200(PASS_HTML),
    robots: () => R200('User-agent: *\nSitemap: https://example.com/custom-sitemap.xml'),
    sitemap: R404,
  });
  assert.ok(pIds(d).includes('sitemap'), 'sitemap counted via robots.txt directive');
  assert.ok(!fIds(d).includes('no_sitemap'), 'no missing-sitemap finding when declared in robots');
  assert.ok(pIds(d).includes('robots'));
});

test('mixed_content is NOT evaluated on a plain-http page (https finding fires instead)', async () => {
  // http:// input -> guardedFetch reports https:false -> mixed-content block is skipped
  const d = await runAudit(
    { home: () => R200('<html><head><title>Plain HTTP Page Title</title></head><body><img src="http://x/y.jpg"></body></html>'), robots: R404, sitemap: R404 },
    { url: 'http://example.com' }
  );
  assert.ok(fIds(d).includes('https'), 'https finding present on an http page');
  assert.ok(!fIds(d).includes('mixed_content'), 'mixed_content not applicable on an http page');
  assert.ok(!pIds(d).includes('no_mixed_content'), 'no mixed-content pass on an http page');
});

test('flags redirect_chain when 3 redirects precede the final page', async () => {
  const chain = {
    'https://example.com/': 'https://example.com/a',
    'https://example.com/a': 'https://example.com/b',
    'https://example.com/b': 'https://example.com/final',
  };
  const d = await runAudit({
    home: (u) => (chain[u] ? resp({ status: 301, location: chain[u] }) : R200(PASS_HTML)),
    robots: () => R200('User-agent: *'),
    sitemap: () => R200('<urlset></urlset>'),
  });
  assert.ok(fIds(d).includes('redirect_chain'), 'redirect_chain finding present');
  assert.match(find(d, 'redirect_chain').title, /3 redirects/);
  assert.equal(d.finalUrl, 'https://example.com/final');
});

test('does NOT flag redirect_chain for a single normal redirect', async () => {
  const chain = { 'https://example.com/': 'https://example.com/home' };
  const d = await runAudit({
    home: (u) => (chain[u] ? resp({ status: 301, location: chain[u] }) : R200(PASS_HTML)),
    robots: () => R200('User-agent: *'),
    sitemap: () => R200('<urlset></urlset>'),
  });
  assert.ok(!fIds(d).includes('redirect_chain'), 'a single redirect is normal, not flagged');
});

test('probe failures are fail-safe: a network error yields neither finding nor pass', async () => {
  const boom = () => { throw new Error('econnreset'); };
  const d = await runAudit({ home: () => R200(PASS_HTML), robots: boom, sitemap: boom });
  const ids = fIds(d), p = pIds(d);
  assert.ok(!ids.includes('no_robots') && !ids.includes('no_sitemap'), 'no false "missing" on network error');
  assert.ok(!p.includes('robots') && !p.includes('sitemap'), 'no false "present" on network error');
  // the rest of the audit still completed
  assert.equal(d.ok, true);
});

test('a data-alt attribute does not count as real alt text', async () => {
  const html =
    '<!doctype html><html><head><title>Data Alt Test Page Here</title></head><body>' +
    '<img src="https://x/a.jpg" data-alt="a">' +
    '<img src="https://x/b.jpg" data-alt="b">' +
    '</body></html>';
  const d = await runAudit({ home: () => R200(html), robots: () => R200('User-agent: *'), sitemap: () => R200('<urlset></urlset>') });
  assert.ok(fIds(d).includes('img_alt'), 'both images counted as missing alt (data-alt ignored)');
  assert.match(find(d, 'img_alt').title, /2 of 2/);
});

test('new findings localize (ru): titles + fix come back in Russian', async () => {
  const d = await runAudit({ home: () => R200(FINDINGS_HTML), robots: R404, sitemap: R404 }, { lang: 'ru' });
  const img = find(d, 'img_alt');
  assert.match(img.title, /изображени/, 'ru img_alt title');
  assert.match(img.title, /2 из 3/, 'ru title interpolates the real counts');
  assert.ok(img.fix && /alt/i.test(img.fix), 'ru fix present');
  assert.ok(img.effort, 'effort label present');
  assert.match(find(d, 'no_robots').title, /robots\.txt/i);
});
