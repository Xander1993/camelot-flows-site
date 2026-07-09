// Tests for CAMELOT-AUDIT-METADESC-ATTR-ORDER: the meta-description check must be
// attribute-order-independent, so it agrees with the SERP preview (parseMeta) that
// displays the same description. A content-first tag — <meta content="…" name="description"> —
// must PASS, not be falsely flagged no_meta_desc while the preview shows the text.
// Drives the REAL handler functions/api/audit.js with a mocked global fetch.
// Run: node --test tests/metadesc.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { onRequestPost } from '../functions/api/audit.js';

function bodyFrom(str) {
  const bytes = new TextEncoder().encode(str || '');
  let sent = false;
  const reader = {
    async read() { if (sent) return { done: true, value: undefined }; sent = true; return { done: false, value: bytes }; },
    async cancel() {},
  };
  return { getReader() { return reader; }, async cancel() {} };
}
function resp({ status = 200, body = '', contentType = 'text/html' } = {}) {
  const h = new Map();
  if (contentType !== null) h.set('content-type', contentType);
  return {
    status,
    ok: status >= 200 && status < 300,
    headers: { get: (k) => { const v = h.get(String(k).toLowerCase()); return v === undefined ? null : v; } },
    body: bodyFrom(body),
  };
}
function installFetch(homeHtml) {
  const orig = globalThis.fetch;
  globalThis.fetch = async (url) => {
    const u = String(url);
    if (u.endsWith('/robots.txt') || u.endsWith('/sitemap.xml')) return resp({ status: 404, contentType: 'text/plain' });
    return resp({ status: 200, body: homeHtml, contentType: 'text/html' });
  };
  return () => { globalThis.fetch = orig; };
}

let ipSeq = 0; // unique IP per audit so the in-memory rate limiter never trips
async function audit(homeHtml) {
  const restore = installFetch(homeHtml);
  try {
    const ctx = {
      env: {},
      request: {
        url: 'https://camelotflows.dev/api/audit',
        headers: { get: (k) => (String(k).toLowerCase() === 'cf-connecting-ip' ? '10.11.0.' + (++ipSeq) : null) },
        json: async () => ({ url: 'https://example.com' }),
      },
    };
    const res = await onRequestPost(ctx);
    return await res.json();
  } finally {
    restore();
  }
}

const REAL_DESC = 'We install and repair garage doors across Chicagoland — same-day service.';
function page(metaTag) {
  return '<!doctype html><html lang="en"><head><title>Chicagoland Garage Door Pros</title>' +
    '<meta name="viewport" content="width=device-width, initial-scale=1">' +
    metaTag +
    '</head><body><h1>Welcome</h1><a href="tel:+13125550199">Call us</a></body></html>';
}
const hasFinding = (data, id) => data.findings.some((x) => x.id === id);
const hasPassed = (data, id) => data.passed.some((p) => p.id === id);

test('name-first meta description passes (regression)', async () => {
  const data = await audit(page('<meta name="description" content="' + REAL_DESC + '">'));
  assert.equal(hasFinding(data, 'no_meta_desc'), false, 'must NOT flag no_meta_desc');
  assert.equal(hasPassed(data, 'meta_desc'), true, 'must pass meta_desc');
});

test('content-first meta description passes (the bug: was falsely flagged)', async () => {
  const data = await audit(page('<meta content="' + REAL_DESC + '" name="description">'));
  assert.equal(hasFinding(data, 'no_meta_desc'), false, 'content-first order must NOT flag no_meta_desc');
  assert.equal(hasPassed(data, 'meta_desc'), true, 'content-first order must pass meta_desc');
});

test('content-first with extra attributes between still passes', async () => {
  const data = await audit(page('<meta charset="utf-8" content="' + REAL_DESC + '" data-x="y" name="description">'));
  assert.equal(hasFinding(data, 'no_meta_desc'), false);
  assert.equal(hasPassed(data, 'meta_desc'), true);
});

test('genuinely missing meta description is still flagged', async () => {
  const data = await audit(page('')); // no description tag at all
  assert.equal(hasFinding(data, 'no_meta_desc'), true, 'absent description must flag no_meta_desc');
  assert.equal(hasPassed(data, 'meta_desc'), false);
});

test('too-short description (<20 chars) is still flagged, either order', async () => {
  const nameFirst = await audit(page('<meta name="description" content="Too short">'));
  assert.equal(hasFinding(nameFirst, 'no_meta_desc'), true, 'short name-first must flag');
  const contentFirst = await audit(page('<meta content="Too short" name="description">'));
  assert.equal(hasFinding(contentFirst, 'no_meta_desc'), true, 'short content-first must flag');
});

test('whitespace-only description is flagged (agrees with preview which trims)', async () => {
  const data = await audit(page('<meta content="                          " name="description">'));
  assert.equal(hasFinding(data, 'no_meta_desc'), true, 'all-whitespace desc is effectively empty');
});
