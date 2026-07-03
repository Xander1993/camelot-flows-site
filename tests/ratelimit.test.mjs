// Tests for the audit endpoints' KV-backed per-IP rate limiter:
// functions/_lib/audit-ratelimit.mjs
// Run: node --test tests/ratelimit.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { rateLimit } from '../functions/_lib/audit-ratelimit.mjs';

// Minimal stand-in for a Cloudflare KV namespace (get/put), with call counters.
function makeKV() {
  const store = new Map();
  return {
    store,
    gets: 0,
    puts: 0,
    async get(k) { this.gets++; return store.has(k) ? store.get(k) : null; },
    async put(k, v) { this.puts++; store.set(k, v); },
  };
}
const opts = (extra) => ({ limit: 5, windowMs: 60_000, prefix: 'audit', ...extra });

test('KV counter allows exactly `limit` requests, then blocks (same IP, same window)', async () => {
  const kv = makeKV();
  const env = { RATE_KV: kv };
  const now = 1_000_000; // fixed timestamp => single window bucket
  const results = [];
  for (let i = 0; i < 7; i++) results.push(await rateLimit(env, '1.2.3.4', opts({ now })));
  // limit 5 => first five allowed (false), sixth and seventh blocked (true)
  assert.deepEqual(results, [false, false, false, false, false, true, true]);
  // Only writes while under the cap => at most `limit` writes per IP per window.
  assert.equal(kv.puts, 5, 'writes are capped at `limit`, not one-per-request');
});

test('the window resets: a new bucket lets the same IP through again', async () => {
  const kv = makeKV();
  const env = { RATE_KV: kv };
  const ip = '9.9.9.9';
  for (let i = 0; i < 6; i++) await rateLimit(env, ip, opts({ now: 1_000_000 }));
  assert.equal(await rateLimit(env, ip, opts({ now: 1_000_000 })), true, 'still blocked in window 1');
  // Jump a full window forward => different bucket key => allowed again.
  assert.equal(await rateLimit(env, ip, opts({ now: 1_060_000 })), false, 'allowed in window 2');
});

test('different IPs have independent counters', async () => {
  const kv = makeKV();
  const env = { RATE_KV: kv };
  const now = 2_000_000;
  for (let i = 0; i < 6; i++) await rateLimit(env, 'a', opts({ now }));
  assert.equal(await rateLimit(env, 'a', opts({ now })), true, 'a is blocked');
  assert.equal(await rateLimit(env, 'b', opts({ now })), false, 'b is unaffected');
});

test('no RATE_KV binding fails open (a single request is never blocked, never throws)', async () => {
  // Unbound env, and entirely-absent env, must both resolve false without throwing.
  assert.equal(await rateLimit({}, 'unbound-ip-1', opts({ now: 3_000_000 })), false);
  assert.equal(await rateLimit(undefined, 'unbound-ip-2', opts({ now: 3_000_000 })), false);
});

test('a throwing KV fails open (no crash, no false 429 on the first hit)', async () => {
  const env = {
    RATE_KV: {
      async get() { throw new Error('kv down'); },
      async put() { throw new Error('kv down'); },
    },
  };
  assert.equal(await rateLimit(env, 'kv-error-ip', opts({ now: 4_000_000 })), false);
});
