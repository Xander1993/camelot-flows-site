// Integration tests for CAMELOT-AUDIT-CONTENTTYPE-GUARD: guardedFetch must refuse
// to score non-HTML responses (PDF / image / JSON API / file download) instead of
// UTF-8-decoding the bytes and reporting them as a "broken site". Drives the REAL
// handler functions/api/audit.js with a mocked global fetch.
// Run: node --test tests/contenttype.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { onRequestPost } from '../functions/api/audit.js';

// --- Response stand-in with a settable content-type header ---
function bodyFrom(str) {
  const bytes = new TextEncoder().encode(str || '');
  let sent = false;
  const reader = {
    async read() { if (sent) return { done: true, value: undefined }; sent = true; return { done: false, value: bytes }; },
    async cancel() {},
  };
  return { getReader() { return reader; }, async cancel() {} };
}
function resp({ status = 200, location = null, body = '', contentType = null } = {}) {
  const h = new Map();
  if (location) h.set('location', location);
  if (contentType !== null) h.set('content-type', contentType);
  return {
    status,
    ok: status >= 200 && status < 300,
    headers: { get: (k) => { const v = h.get(String(k).toLowerCase()); return v === undefined ? null : v; } },
    body: bodyFrom(body),
  };
}
const R200ct = (ct, body = '') => resp({ status: 200, body, contentType: ct });

function installFetch(routes) {
  const orig = globalThis.fetch;
  globalThis.fetch = async (url) => {
    const u = String(url);
    if (u.endsWith('/robots.txt')) return (routes.robots || (() => resp({ status: 404 })))(u);
    if (u.endsWith('/sitemap.xml')) return (routes.sitemap || (() => resp({ status: 404 })))(u);
    return routes.home(u);
  };
  return () => { globalThis.fetch = orig; };
}

let ipSeq = 0; // unique IP per audit so the in-memory rate limiter never trips
async function runAuditRaw(routes, { lang = '', url = 'https://example.com' } = {}) {
  const restore = installFetch(routes);
  try {
    const ctx = {
      env: {},
      request: {
        url: 'https://camelotflows.dev/api/audit' + (lang ? '?lang=' + lang : ''),
        headers: { get: (k) => (String(k).toLowerCase() === 'cf-connecting-ip' ? '10.9.0.' + (++ipSeq) : null) },
        json: async () => ({ url }),
      },
    };
    const res = await onRequestPost(ctx);
    return { status: res.status, data: await res.json() };
  } finally {
    restore();
  }
}

// A real, well-formed HTML homepage — the control case that must still score.
const GOOD_HTML =
  '<!doctype html><html lang="en"><head><title>Real Web Page Title Here</title>' +
  '<meta name="viewport" content="width=device-width, initial-scale=1"></head>' +
  '<body><h1>Welcome</h1><a href="tel:+37312345678">Call us</a></body></html>';

// Bytes a PDF actually starts with — proof we would have decoded garbage.
const PDF_BYTES = '%PDF-1.7\n1 0 obj<< /Type /Catalog >>endobj';
const JSON_BODY = '{"ok":true,"items":[1,2,3],"note":"this is an API endpoint"}';

test('application/pdf -> honest 422 not_html error, NOT a scored report', async () => {
  const { status, data } = await runAuditRaw({ home: () => R200ct('application/pdf', PDF_BYTES) });
  assert.equal(status, 422, 'HTTP 422 (survives Cloudflare 502-body replacement)');
  assert.equal(data.ok, false, 'not ok');
  assert.equal(data.error, 'not_html', 'error code is not_html');
  assert.equal(data.score, undefined, 'no fabricated score for a PDF');
  assert.equal(data.findings, undefined, 'no findings scored against PDF bytes');
  assert.match(data.message, /application\/pdf/, 'message names the real content type');
  assert.match(data.message, /web page/i, 'message explains it is not a web page');
});

test('application/json -> honest 422 not_html error', async () => {
  const { status, data } = await runAuditRaw({ home: () => R200ct('application/json', JSON_BODY) });
  assert.equal(status, 422);
  assert.equal(data.error, 'not_html');
  assert.equal(data.score, undefined);
  assert.match(data.message, /application\/json/);
});

test('image/png -> honest 422 not_html error', async () => {
  const { status, data } = await runAuditRaw({ home: () => R200ct('image/png', '\x89PNG\r\n\x1a\n') });
  assert.equal(status, 422);
  assert.equal(data.error, 'not_html');
  assert.match(data.message, /image\/png/);
});

test('text/html (with charset) -> unchanged: a real scored report', async () => {
  const { status, data } = await runAuditRaw({ home: () => R200ct('text/html; charset=utf-8', GOOD_HTML) });
  assert.equal(status, 200, 'normal audit still returns 200');
  assert.equal(data.ok, true, 'ok');
  assert.equal(typeof data.score, 'number', 'a real score is computed');
  assert.ok(Array.isArray(data.findings), 'findings array present');
});

test('application/xhtml+xml -> allowed and scored (valid web-page type)', async () => {
  const { status, data } = await runAuditRaw({ home: () => R200ct('application/xhtml+xml', GOOD_HTML) });
  assert.equal(status, 200);
  assert.equal(data.ok, true);
  assert.equal(typeof data.score, 'number');
});

test('absent content-type -> still attempted (some servers omit it), scored as before', async () => {
  const { status, data } = await runAuditRaw({ home: () => R200ct(null, GOOD_HTML) });
  assert.equal(status, 200, 'no content-type header must not block a real page');
  assert.equal(data.ok, true);
  assert.equal(typeof data.score, 'number');
});

test('empty content-type -> still attempted', async () => {
  const { status, data } = await runAuditRaw({ home: () => R200ct('', GOOD_HTML) });
  assert.equal(status, 200);
  assert.equal(data.ok, true);
});

test('non-HTML error localizes (ru): message comes back in Russian', async () => {
  const { status, data } = await runAuditRaw({ home: () => R200ct('application/pdf', PDF_BYTES) }, { lang: 'ru' });
  assert.equal(status, 422);
  assert.equal(data.error, 'not_html');
  assert.match(data.message, /веб-страниц/, 'ru not_html message');
  assert.match(data.message, /application\/pdf/, 'ru message still names the type');
});

test('non-HTML error localizes (ro)', async () => {
  const { data } = await runAuditRaw({ home: () => R200ct('application/pdf', PDF_BYTES) }, { lang: 'ro' });
  assert.equal(data.error, 'not_html');
  assert.match(data.message, /pagină web/, 'ro not_html message');
});

test('a non-HTML type reached via redirect is also caught (guard runs on the final response)', async () => {
  const chain = { 'https://example.com/': 'https://example.com/report.pdf' };
  const { status, data } = await runAuditRaw({
    home: (u) => (chain[u] ? resp({ status: 301, location: chain[u] }) : R200ct('application/pdf', PDF_BYTES)),
  });
  assert.equal(status, 422);
  assert.equal(data.error, 'not_html');
});
