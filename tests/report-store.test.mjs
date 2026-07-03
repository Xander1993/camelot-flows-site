// Tests for the shareable audit-report KV store:
// functions/_lib/audit-report-store.mjs
// Run: node --test tests/report-store.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { genReportId, validId, saveReport, getReport, mergeSpeed } from '../functions/_lib/audit-report-store.mjs';

// Minimal stand-in for a Cloudflare KV namespace (get/put + TTL capture).
function makeKV() {
  const store = new Map();
  return {
    store,
    puts: 0,
    async get(k) { return store.has(k) ? store.get(k).v : null; },
    async put(k, v, opts) { this.puts++; store.set(k, { v, ttl: opts && opts.expirationTtl }); },
  };
}

const samplePayload = () => ({
  ok: true,
  finalUrl: 'https://example.com/',
  score: 82,
  summary: 'A clean-ish page.',
  summarySource: 'llm',
  variant: 'A',
  findings: [{ id: 'no_og', severity: 'low', title: 'No OG', detail: 'x' }],
  passed: [{ id: 'https', label: 'Secure' }],
  meta: { host: 'example.com', title: 'Example' },
  aiRead: { clarity: { what: { ok: true, note: 'clear' } } },
  speedPending: true,
  // admin-only fields that must NOT be persisted:
  model: 'secret-model',
  usage: { total_tokens: 999 },
  compare: [{ model: 'm', summary: 's' }],
});

test('genReportId returns a 12-char lowercase-alnum id that passes validId', () => {
  for (let i = 0; i < 50; i++) {
    const id = genReportId();
    assert.match(id, /^[a-z0-9]{12}$/, 'id shape');
    assert.equal(validId(id), true);
  }
  // uniqueness across a small sample (CSPRNG-backed)
  const ids = new Set(Array.from({ length: 200 }, genReportId));
  assert.ok(ids.size > 190, 'ids should be overwhelmingly unique');
});

test('validId rejects junk and out-of-range lengths', () => {
  assert.equal(validId('abc'), false);          // too short
  assert.equal(validId('a'.repeat(25)), false);  // too long
  assert.equal(validId('Has-Caps!'), false);     // illegal chars
  assert.equal(validId(''), false);
  assert.equal(validId(null), false);
  assert.equal(validId(123), false);
});

test('saveReport stores a whitelisted subset and returns an id; getReport round-trips it', async () => {
  const kv = makeKV();
  const env = { RATE_KV: kv };
  const id = await saveReport(env, samplePayload());
  assert.ok(validId(id), 'returns a valid id');
  assert.equal(kv.puts, 1);
  // TTL was set (30 days) and key is prefixed.
  assert.ok(kv.store.has('report:' + id));
  assert.equal(kv.store.get('report:' + id).ttl, 60 * 60 * 24 * 30);

  const got = await getReport(env, id);
  assert.equal(got.ok, true);
  assert.equal(got.shared, true);
  assert.equal(got.score, 82);
  assert.equal(got.finalUrl, 'https://example.com/');
  assert.equal(got.findings.length, 1);
  assert.equal(got.passed[0].id, 'https');
  // admin QA fields and transient flags must be stripped
  assert.equal('model' in got, false, 'admin model not persisted');
  assert.equal('usage' in got, false, 'admin usage not persisted');
  assert.equal('compare' in got, false, 'admin compare not persisted');
  assert.equal('speedPending' in got, false, 'transient flag not persisted');
});

test('saveReport / getReport / mergeSpeed all fail-open without a KV binding', async () => {
  assert.equal(await saveReport({}, samplePayload()), null);
  assert.equal(await saveReport(undefined, samplePayload()), null);
  assert.equal(await getReport({}, 'abcdef123456'), null);
  assert.equal(await mergeSpeed({}, 'abcdef123456', { findings: [], passed: [], scoreDelta: -9 }), false);
});

test('saveReport does not persist a failed (ok:false) payload', async () => {
  const kv = makeKV();
  const id = await saveReport({ RATE_KV: kv }, { ok: false, error: 'fetch_failed' });
  assert.equal(id, null);
  assert.equal(kv.puts, 0);
});

test('getReport returns null for unknown or invalid ids', async () => {
  const kv = makeKV();
  const env = { RATE_KV: kv };
  assert.equal(await getReport(env, 'neverstored12'), null); // valid shape, not present
  assert.equal(await getReport(env, 'BAD'), null);           // invalid shape (no KV read attempted)
});

test('mergeSpeed folds speed findings/passed in and adjusts the stored score', async () => {
  const kv = makeKV();
  const env = { RATE_KV: kv };
  const id = await saveReport(env, samplePayload()); // score 82, 1 finding, 1 passed
  const ok = await mergeSpeed(env, id, {
    findings: [{ id: 'slow_mobile', severity: 'high', title: 'Slow on mobile', detail: 'x' }],
    passed: [],
    scoreDelta: -18,
  });
  assert.equal(ok, true);
  const got = await getReport(env, id);
  assert.equal(got.score, 64, '82 - 18 = 64');
  assert.equal(got.findings.length, 2, 'speed finding appended');
  assert.equal(got.findings[1].id, 'slow_mobile', 'appended after phase-1 findings');
  assert.equal(got.passed.length, 1, 'no new passed added');
});

test('mergeSpeed clamps the adjusted score to the 5..100 floor', async () => {
  const kv = makeKV();
  const env = { RATE_KV: kv };
  const p = samplePayload();
  p.score = 10;
  const id = await saveReport(env, p);
  await mergeSpeed(env, id, { findings: [], passed: [], scoreDelta: -40 });
  const got = await getReport(env, id);
  assert.equal(got.score, 5, 'floors at 5, never below');
});

test('mergeSpeed on a missing/unknown id is a no-op that returns false', async () => {
  const kv = makeKV();
  const env = { RATE_KV: kv };
  assert.equal(await mergeSpeed(env, 'missingid1234', { findings: [], passed: [], scoreDelta: -9 }), false);
});

test('a throwing KV fails open everywhere (no crash)', async () => {
  const badKV = {
    async get() { throw new Error('kv down'); },
    async put() { throw new Error('kv down'); },
  };
  const env = { RATE_KV: badKV };
  assert.equal(await saveReport(env, samplePayload()), null);
  assert.equal(await getReport(env, 'abcdef123456'), null);
  assert.equal(await mergeSpeed(env, 'abcdef123456', { findings: [], passed: [], scoreDelta: -9 }), false);
});
