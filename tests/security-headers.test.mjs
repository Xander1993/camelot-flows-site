// Tests for CAMELOT-API-HEADERS-NOT-ON-FUNCTIONS: Cloudflare Pages applies the
// root `_headers` file to static assets ONLY, never to a Pages Function's
// response — so /api/audit was served with 0/4 security headers while every
// static route served 4/4. The /api/* Functions now set them at their shared
// json() choke-point.
//
// The parity test below is the important one: `_headers` (static) and
// SECURITY_HEADERS (Functions) are two sources for one posture, and nothing but
// a test stops them drifting apart.
// Run: node --test tests/security-headers.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { json, SECURITY_HEADERS } from '../functions/_lib/http.mjs';
import { onRequestGet } from '../functions/api/audit.js';

const repoRoot = join(dirname(fileURLToPath(import.meta.url)), '..');

// Parse the `/*` block of the real _headers file into {name: value}, lowercased.
function parseHeadersFile() {
  const txt = readFileSync(join(repoRoot, '_headers'), 'utf8');
  const out = {};
  let inGlob = false;
  for (const raw of txt.split('\n')) {
    const line = raw.trimEnd();
    if (!line.trim() || line.trim().startsWith('#')) continue;
    if (!line.startsWith(' ') && !line.startsWith('\t')) { inGlob = line.trim() === '/*'; continue; }
    if (!inGlob) continue;
    const idx = line.indexOf(':');
    if (idx === -1) continue;
    out[line.slice(0, idx).trim().toLowerCase()] = line.slice(idx + 1).trim();
  }
  return out;
}

const SECURITY_KEYS = [
  'strict-transport-security',
  'x-frame-options',
  'content-security-policy',
  'permissions-policy',
];

test('SECURITY_HEADERS does not drift from the static _headers file', () => {
  const fromFile = parseHeadersFile();
  for (const k of SECURITY_KEYS) {
    assert.ok(fromFile[k], `_headers is missing ${k} — did the /* block change?`);
    assert.equal(
      SECURITY_HEADERS[k], fromFile[k],
      `${k} differs between _headers (static) and SECURITY_HEADERS (Functions)`,
    );
  }
  // No extra keys in the Function set that _headers does not also send.
  assert.deepEqual(Object.keys(SECURITY_HEADERS).sort(), [...SECURITY_KEYS].sort());
});

test('json() carries all 4 security headers on a 200', () => {
  const r = json({ ok: true });
  assert.equal(r.status, 200);
  for (const k of SECURITY_KEYS) assert.equal(r.headers.get(k), SECURITY_HEADERS[k], `missing ${k}`);
});

test('json() preserves content-type and cache-control', () => {
  const r = json({ ok: true });
  assert.equal(r.headers.get('content-type'), 'application/json; charset=utf-8');
  assert.equal(r.headers.get('cache-control'), 'no-store');
});

test('json() body and status still round-trip', async () => {
  const r = json({ ok: false, error: 'bad_request' }, 400);
  assert.equal(r.status, 400);
  assert.deepEqual(await r.json(), { ok: false, error: 'bad_request' });
});

// The regression that was live: GET /api/audit with no ?r= returns 400 and used
// to carry 0/4 headers. Drives the REAL exported handler, no mocks needed.
test('real GET /api/audit 400 error path carries the security headers', async () => {
  const res = await onRequestGet({ env: {}, request: { url: 'https://camelotflows.dev/api/audit' } });
  assert.equal(res.status, 400);
  for (const k of SECURITY_KEYS) {
    assert.equal(res.headers.get(k), SECURITY_HEADERS[k], `400 path missing ${k}`);
  }
  const body = await res.json();
  assert.equal(body.ok, false);
  assert.equal(body.error, 'bad_request');
});

// Error paths are the ones most likely to bypass a header helper, so cover a
// second, different one: an unknown report id -> 404.
test('real GET /api/audit 404 error path carries the security headers', async () => {
  const res = await onRequestGet({ env: {}, request: { url: 'https://camelotflows.dev/api/audit?r=nope' } });
  assert.equal(res.status, 404);
  for (const k of SECURITY_KEYS) {
    assert.equal(res.headers.get(k), SECURITY_HEADERS[k], `404 path missing ${k}`);
  }
});
