// Tests for CAMELOT-AUDIT-LLM-BUDGET-UNDERCOUNT: the monthly AI budget must
// count ACTUAL provider calls, not audits. Each non-lite audit fires 2-3
// callLlm() passes (summary + AI-read [+ one retry]) or N in admin-compare, but
// the old accounting incremented the KV counter by exactly 1 per audit — so
// LLM_MONTHLY_CAP silently permitted 2-3x the paid calls it promises to cap.
//
// Part A unit-tests the budget primitives (functions/_lib/audit-llm-budget.mjs):
//   read-only check, fail-open with zero writes, charge-by-n, cap boundary.
// Part B drives the REAL handler (functions/api/audit.js) with a mocked global
//   fetch — including the LLM /chat/completions endpoint — and asserts the KV
//   monthly counter advances by the true number of calls each path issued.
// Run: node --test tests/llm-budget.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { llmBudgetOk, chargeLlmBudget } from '../functions/_lib/audit-llm-budget.mjs';
import { onRequestPost } from '../functions/api/audit.js';

const MONTH_KEY = 'llm:' + new Date().toISOString().slice(0, 7);

// --- Mock KV: Map-backed, counts reads/writes so we can prove "zero writes". ---
function makeKV(initial = {}) {
  const store = new Map(Object.entries(initial).map(([k, v]) => [k, String(v)]));
  let gets = 0, puts = 0;
  return {
    async get(k) { gets++; const v = store.get(k); return v === undefined ? null : v; },
    async put(k, v) { puts++; store.set(k, String(v)); },
    stats: () => ({ gets, puts }),
    used: () => { const v = store.get(MONTH_KEY); return v === undefined ? null : Number(v); },
  };
}

/* =========================== Part A — primitives =========================== */

test('llmBudgetOk fail-open: no RATE_KV binding => allowed, and ZERO writes', async () => {
  // No KV object at all — the unbound case. Must allow and never attempt a write.
  assert.equal(await llmBudgetOk({}), true);
  // chargeLlmBudget on an unbound env must be a silent no-op (nothing to write to).
  await assert.doesNotReject(chargeLlmBudget({}, 3));
  await assert.doesNotReject(chargeLlmBudget({ RATE_KV: null }, 3));
});

test('llmBudgetOk is READ-ONLY: it checks the cap without incrementing the counter', async () => {
  const kv = makeKV();
  assert.equal(await llmBudgetOk({ RATE_KV: kv }), true);
  assert.equal(await llmBudgetOk({ RATE_KV: kv }), true);
  const { puts } = kv.stats();
  assert.equal(puts, 0, 'the up-front check must never write — charging happens after the calls');
  assert.equal(kv.used(), null, 'counter untouched by the check');
});

test('chargeLlmBudget advances the monthly counter by exactly n (read-modify-write)', async () => {
  const kv = makeKV();
  await chargeLlmBudget({ RATE_KV: kv }, 2);   // normal path
  assert.equal(kv.used(), 2);
  await chargeLlmBudget({ RATE_KV: kv }, 3);   // + admin-compare with 3 models
  assert.equal(kv.used(), 5, 'accumulates on top of the existing count');
});

test('chargeLlmBudget is a no-op for n <= 0 (no audit fired no calls)', async () => {
  const kv = makeKV({ [MONTH_KEY]: 4 });
  await chargeLlmBudget({ RATE_KV: kv }, 0);
  await chargeLlmBudget({ RATE_KV: kv }, -1);
  assert.equal(kv.used(), 4, 'counter unchanged');
  assert.equal(kv.stats().puts, 0, 'no writes for a zero/negative charge');
});

test('llmBudgetOk enforces the cap boundary (default 3000, override honoured)', async () => {
  assert.equal(await llmBudgetOk({ RATE_KV: makeKV({ [MONTH_KEY]: 2 }), LLM_MONTHLY_CAP: 3 }), true, 'under cap');
  assert.equal(await llmBudgetOk({ RATE_KV: makeKV({ [MONTH_KEY]: 3 }), LLM_MONTHLY_CAP: 3 }), false, 'at cap => blocked');
  assert.equal(await llmBudgetOk({ RATE_KV: makeKV({ [MONTH_KEY]: 9 }), LLM_MONTHLY_CAP: 3 }), false, 'over cap => blocked');
  assert.equal(await llmBudgetOk({ RATE_KV: makeKV({ [MONTH_KEY]: 2999 }) }), true, 'default cap 3000: 2999 allowed');
  assert.equal(await llmBudgetOk({ RATE_KV: makeKV({ [MONTH_KEY]: 3000 }) }), false, 'default cap 3000: 3000 blocked');
});

test('both primitives fail-open on a KV that throws (never hard-fail an audit)', async () => {
  const boom = { get: async () => { throw new Error('kv down'); }, put: async () => { throw new Error('kv down'); } };
  assert.equal(await llmBudgetOk({ RATE_KV: boom }), true, 'check fail-opens to allowed');
  await assert.doesNotReject(chargeLlmBudget({ RATE_KV: boom }, 2), 'charge swallows the write error');
});

/* ===================== Part B — real handler, real counts ===================== */

// Response stand-ins. HTML responses expose getReader() (guardedFetch streams
// them); the LLM endpoint exposes json() (callLlm parses it).
function htmlResp(html, { status = 200, contentType = 'text/html' } = {}) {
  const bytes = new TextEncoder().encode(html || '');
  let sent = false;
  const reader = {
    async read() { if (sent) return { done: true, value: undefined }; sent = true; return { done: false, value: bytes }; },
    async cancel() {},
  };
  const h = new Map([['content-type', contentType]]);
  return {
    status, ok: status >= 200 && status < 300,
    headers: { get: (k) => { const v = h.get(String(k).toLowerCase()); return v === undefined ? null : v; } },
    body: { getReader: () => reader, async cancel() {} },
  };
}
function missingResp() {
  return { status: 404, ok: false, headers: { get: () => null }, body: { getReader: () => ({ async read() { return { done: true }; }, async cancel() {} }), async cancel() {} } };
}
function llmResp(content) {
  return {
    ok: true, status: 200, headers: { get: () => null },
    async json() { return { choices: [{ message: { content: content == null ? '' : String(content) } }], usage: { total_tokens: 10 } }; },
  };
}

const GOOD_HTML =
  '<!doctype html><html lang="en"><head><title>Real Web Page Title Here</title>' +
  '<meta name="viewport" content="width=device-width, initial-scale=1"></head>' +
  '<body><h1>Welcome</h1><a href="tel:+37312345678">Call us</a></body></html>';
const AIREAD_JSON =
  '{"clarity":{"what":{"ok":true,"note":"x"},"who":{"ok":true,"note":"y"},"why":{"ok":true,"note":"z"}},"aeo":{"ready":"yes","note":"n","reasons":["a"]}}';

// Route a mocked fetch. `onAiRead(callIndex)` returns the content string for the
// Nth AI-read call (1-based) so a test can simulate an empty first response.
function installFetch({ onAiRead } = {}) {
  const orig = globalThis.fetch;
  let summaryCalls = 0, aiReadCalls = 0;
  globalThis.fetch = async (url, init) => {
    const u = String(url);
    if (u.endsWith('/chat/completions')) {
      const sys = JSON.parse(init.body).messages[0].content;
      if (/pageText/.test(sys)) {         // the structured AI-read pass
        aiReadCalls++;
        return llmResp(onAiRead ? onAiRead(aiReadCalls) : AIREAD_JSON);
      }
      summaryCalls++;                     // the plain-language summary pass
      return llmResp('A concise plain-language summary of the audit findings.');
    }
    if (u.endsWith('/robots.txt') || u.endsWith('/sitemap.xml')) return missingResp();
    return htmlResp(GOOD_HTML);
  };
  return { restore: () => { globalThis.fetch = orig; }, counts: () => ({ summaryCalls, aiReadCalls }) };
}

let ipSeq = 0; // unique IP per audit so the in-memory rate limiter never trips
async function runAudit({ env = {}, body = { url: 'https://example.com' }, onAiRead } = {}) {
  const f = installFetch({ onAiRead });
  try {
    const ctx = {
      env,
      request: {
        url: 'https://camelotflows.dev/api/audit',
        headers: { get: (k) => (String(k).toLowerCase() === 'cf-connecting-ip' ? '10.7.0.' + (++ipSeq) : null) },
        json: async () => body,
      },
    };
    const res = await onRequestPost(ctx);
    return { status: res.status, data: await res.json(), counts: f.counts() };
  } finally {
    f.restore();
  }
}

test('normal path: summary + AI-read both succeed => 2 calls => counter += 2', async () => {
  const kv = makeKV();
  const { status, data, counts } = await runAudit({ env: { LLM_API_KEY: 'test', RATE_KV: kv } });
  assert.equal(status, 200);
  assert.equal(data.ok, true);
  assert.equal(data.summarySource, 'llm', 'LLM layer actually ran (fail-open check allowed it)');
  assert.equal(counts.summaryCalls + counts.aiReadCalls, 2, 'exactly two provider calls fired');
  assert.equal(kv.used(), 2, 'monthly counter charged for 2 calls, not 1 audit');
});

test('normal path with an empty first AI-read => retry => 3 calls => counter += 3', async () => {
  const kv = makeKV();
  // First AI-read returns empty content (callLlm => "empty LLM response"), forcing one retry.
  const { data, counts } = await runAudit({
    env: { LLM_API_KEY: 'test', RATE_KV: kv },
    onAiRead: (n) => (n === 1 ? '' : AIREAD_JSON),
  });
  assert.equal(data.ok, true);
  assert.equal(counts.aiReadCalls, 2, 'AI-read fired twice (initial + retry)');
  assert.equal(counts.summaryCalls, 1);
  assert.equal(kv.used(), 3, 'counter charged for all 3 provider calls incl. the retry');
});

test('admin-compare: one call per model (N=3) => counter += 3', async () => {
  const kv = makeKV();
  const env = { LLM_API_KEY: 'test', RATE_KV: kv, ADMIN_KEY: 'secret', LLM_MODELS: 'm1,m2,m3' };
  const { data, counts } = await runAudit({
    env,
    body: { url: 'https://example.com', adminKey: 'secret', compare: true },
  });
  assert.equal(data.ok, true);
  assert.equal(counts.summaryCalls, 3, 'admin-compare issues one summary call per configured model');
  assert.equal(counts.aiReadCalls, 0, 'compare mode runs no AI-read pass');
  assert.equal(kv.used(), 3, 'counter charged N=models.length, not 1');
});

test('fail-open integration: no RATE_KV => LLM layer still runs, no crash, no KV needed', async () => {
  const { status, data, counts } = await runAudit({ env: { LLM_API_KEY: 'test' } }); // RATE_KV unbound
  assert.equal(status, 200);
  assert.equal(data.summarySource, 'llm', 'unbound budget fails open — calls still fire');
  assert.equal(counts.summaryCalls + counts.aiReadCalls, 2, 'same call volume, simply uncounted');
});

test('lite mode charges nothing (skips the LLM layer entirely)', async () => {
  const kv = makeKV();
  const f = installFetch({});
  try {
    const ctx = {
      env: { LLM_API_KEY: 'test', RATE_KV: kv },
      request: {
        url: 'https://camelotflows.dev/api/audit?lite=1',
        headers: { get: (k) => (String(k).toLowerCase() === 'cf-connecting-ip' ? '10.7.9.' + (++ipSeq) : null) },
        json: async () => ({ url: 'https://example.com' }),
      },
    };
    const res = await onRequestPost(ctx);
    const data = await res.json();
    assert.equal(data.ok, true);
    assert.equal(f.counts().summaryCalls + f.counts().aiReadCalls, 0, 'lite mode fires no LLM calls');
    assert.equal(kv.used(), null, 'nothing charged in lite mode');
  } finally {
    f.restore();
  }
});
