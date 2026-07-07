// Tests for the durable audit-lead KV backstop:
// functions/_lib/audit-lead-store.mjs
// Run: node --test tests/lead-store.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { saveLead } from '../functions/_lib/audit-lead-store.mjs';

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

const validLead = () => ({
  email: 'jane@example.com',
  url: 'https://example.com/',
  score: 48,
  lang: 'en',
  ip: '203.0.113.7',
});

test('saveLead persists a valid lead under a time-sorted lead: key and returns true', async () => {
  const kv = makeKV();
  const ok = await saveLead({ RATE_KV: kv }, validLead());
  assert.equal(ok, true);
  assert.equal(kv.puts, 1);
  const [k] = [...kv.store.keys()];
  assert.match(k, /^lead:\d{4}-\d{2}-\d{2}T.*Z-[a-z0-9]{8}$/, 'key is lead:<ISO ts>-<suffix>');
  const rec = JSON.parse(kv.store.get(k).v);
  assert.equal(rec.email, 'jane@example.com');
  assert.equal(rec.url, 'https://example.com/');
  assert.equal(rec.score, '48');
  assert.equal(rec.lang, 'en');
  assert.equal(rec.ip, '203.0.113.7');
  assert.match(rec.ts, /^\d{4}-\d{2}-\d{2}T/);
  // No TTL: a business lead must persist until the owner clears it.
  assert.equal(kv.store.get(k).ttl, undefined, 'lead is stored without an expiry');
});

test('saveLead skips (returns false, no write) on an invalid or empty email', async () => {
  const kv = makeKV();
  assert.equal(await saveLead({ RATE_KV: kv }, { email: 'not-an-email', url: 'x' }), false);
  assert.equal(await saveLead({ RATE_KV: kv }, { email: '', url: 'x' }), false);
  assert.equal(await saveLead({ RATE_KV: kv }, { url: 'x' }), false); // no email at all
  assert.equal(kv.puts, 0, 'nothing written for invalid leads');
});

test('saveLead fails open (returns false, no crash) when RATE_KV is unbound', async () => {
  assert.equal(await saveLead({}, validLead()), false);
  assert.equal(await saveLead(undefined, validLead()), false);
  assert.equal(await saveLead(null, validLead()), false);
});

test('saveLead fails open (returns false) when the lead itself is missing', async () => {
  const kv = makeKV();
  assert.equal(await saveLead({ RATE_KV: kv }, null), false);
  assert.equal(await saveLead({ RATE_KV: kv }, undefined), false);
  assert.equal(kv.puts, 0);
});

test('saveLead fails open (returns false, no throw) when KV.put throws', async () => {
  const badKV = { async get() { throw new Error('kv down'); }, async put() { throw new Error('kv down'); } };
  assert.equal(await saveLead({ RATE_KV: badKV }, validLead()), false);
});

test('saveLead truncates oversized fields and tolerates missing optional fields', async () => {
  const kv = makeKV();
  const ok = await saveLead({ RATE_KV: kv }, { email: 'a@b.co' }); // only the required field
  assert.equal(ok, true);
  const [k] = [...kv.store.keys()];
  const rec = JSON.parse(kv.store.get(k).v);
  assert.equal(rec.email, 'a@b.co');
  assert.equal(rec.url, '');
  assert.equal(rec.score, '');
  assert.equal(rec.lang, '');
  assert.equal(rec.ip, '');

  const kv2 = makeKV();
  await saveLead({ RATE_KV: kv2 }, {
    email: 'a@b.co',
    url: 'https://x.example/' + 'p'.repeat(500),
    lang: 'englishtoolong',
  });
  const rec2 = JSON.parse([...kv2.store.values()][0].v);
  assert.ok(rec2.url.length <= 300, 'url clamped to 300');
  assert.ok(rec2.lang.length <= 5, 'lang clamped to 5');
});

test('two leads in quick succession get distinct keys (no overwrite)', async () => {
  const kv = makeKV();
  await saveLead({ RATE_KV: kv }, validLead());
  await saveLead({ RATE_KV: kv }, validLead());
  assert.equal(kv.puts, 2);
  assert.equal(kv.store.size, 2, 'random suffix keeps same-ms leads from colliding');
});
