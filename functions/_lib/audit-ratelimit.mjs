/**
 * Per-IP rate limiting for the /api/audit* endpoints.
 *
 * Why this exists: the old limiter was a per-isolate in-memory Map. Cloudflare
 * spreads requests across many Worker isolates and edge locations, so a flood
 * lands on fresh isolates that each start their counter at zero — the Map never
 * sees the same IP twice and the limit is effectively decorative (proven live:
 * 8 rapid POSTs, zero 429s). Every audit costs money (LLM summary + PageSpeed),
 * so an unthrottled anonymous endpoint is a standing bill.
 *
 * The fix is a Cloudflare KV fixed-window counter keyed on the client IP. KV is
 * shared across every isolate and edge location, so it actually caps how many
 * times one IP can trigger a paid audit per window.
 *
 * Fail-open by design. If the RATE_KV binding is absent, or any KV read/write
 * throws, we fall back to the per-isolate in-memory limiter and NEVER hard-fail
 * or 429 a visitor on that account. Consequence: until the owner binds RATE_KV
 * in the Pages dashboard, behaviour is identical to the old in-memory limiter,
 * so deploying this is a zero-regression change.
 *
 * OWNER ACTION (required for this to actually bite): bind a KV namespace as
 * RATE_KV in the Cloudflare Pages project (Settings -> Functions -> KV
 * namespace bindings) — the same binding llmBudgetOk() already uses for the
 * monthly LLM cap. One namespace serves both.
 *
 * KV is eventually consistent (a read can lag a write by up to ~60s at the
 * edge), so a burst spread across many edge locations can slightly undercount.
 * For a hard, synchronous cap, add a Cloudflare WAF rate-limiting rule on
 * /api/audit* (Security -> WAF -> Rate limiting rules, e.g. 10 req / 1 min /
 * IP). This KV counter is the app-level backstop that works without the WAF.
 */

const localHits = new Map(); // "prefix:ip" -> number[] timestamps, per-isolate best-effort

function localLimited(prefix, ip, now, limit, windowMs) {
  const k = prefix + ':' + ip;
  const rec = localHits.get(k) || [];
  const fresh = rec.filter((t) => now - t < windowMs);
  fresh.push(now);
  localHits.set(k, fresh);
  if (localHits.size > 5000) localHits.clear(); // memory guard
  return fresh.length > limit;
}

/**
 * @param {object} env  Pages Function env (RATE_KV may or may not be bound).
 * @param {string} ip   client IP (cf-connecting-ip).
 * @param {object} opts { limit, windowMs, prefix, now? }
 * @returns {Promise<boolean>} true if the request should be rejected with 429.
 */
export async function rateLimit(env, ip, opts = {}) {
  const limit = opts.limit ?? 5;
  const windowMs = opts.windowMs ?? 60_000;
  const prefix = opts.prefix || 'audit';
  const now = opts.now ?? Date.now();

  const kv = env && env.RATE_KV;
  if (kv) {
    try {
      // Fixed-window counter: one KV key per (ip, window), auto-expiring.
      const bucket = Math.floor(now / windowMs);
      const key = 'rl:' + prefix + ':' + ip + ':' + bucket;
      const used = Number((await kv.get(key)) || 0);
      if (used >= limit) return true; // over cap — block, and skip the write
      // Only write while under the cap, so an IP triggers at most `limit` writes
      // per window (stays well inside KV's per-key write budget).
      const ttl = Math.max(60, Math.ceil(windowMs / 1000) * 2);
      await kv.put(key, String(used + 1), { expirationTtl: ttl });
      return false;
    } catch {
      // KV hiccup — fall through to the in-memory fallback, never punish the visitor.
    }
  }

  // No RATE_KV bound (or KV errored): per-isolate best-effort (fail-open across isolates).
  return localLimited(prefix, ip, now, limit, windowMs);
}
