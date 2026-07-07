/**
 * Durable lead persistence for POST /api/audit-lead.
 *
 * Why this exists: a visitor who leaves an email for a fix plan is a paying
 * prospect, and the privacy policy PROMISES a manual fix-plan + price in return.
 * Until now that promise rode on two best-effort, ephemeral channels only:
 *   - client-side Web3Forms email (fails silently on CORS/rate-limit/free-cap), and
 *   - a server Telegram push that is a NO-OP unless TELEGRAM_BOT_TOKEN/CHAT_ID are
 *     bound (they are unset in Pages today).
 * If both slip, the lead reaches NOBODY while the visitor sees a success screen —
 * lost money and a broken promise. This adds a durable server-side backstop: every
 * VALIDATED lead is written to Cloudflare KV so it survives even when both push
 * channels fail.
 *
 * Storage: the SAME KV namespace the rate limiter, the monthly LLM budget, and the
 * shareable report-store already use (RATE_KV), under a "lead:" key prefix — so the
 * owner still only has to bind ONE namespace. See audit-ratelimit.mjs /
 * audit-report-store.mjs. Keys are time-prefixed (ISO timestamp + random suffix)
 * so `wrangler kv key list` returns them in chronological order and two leads in the
 * same millisecond never collide.
 *
 * No TTL: a business lead must not silently expire — it persists until the owner
 * clears it.
 *
 * Fail-open by design. If RATE_KV is unbound, the email is invalid, or any KV op
 * throws, saveLead() returns false and NEVER blocks or 500s the request. Consequence:
 * until the owner binds RATE_KV in the Pages dashboard the durable backstop is inert
 * (exactly today's behaviour) — a zero-regression add. Full durability arrives once
 * RATE_KV is bound (OWNER-MANUAL-TASKS item 1).
 */

const LEAD_PREFIX = 'lead:';
const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
const ID_ALPHABET = 'abcdefghijklmnopqrstuvwxyz0123456789';

// Short random suffix (CSPRNG-backed; present in Workers and Node 18+). Just enough
// entropy to disambiguate two leads written in the same millisecond — not a secret.
function randSuffix(n = 8) {
  const bytes = new Uint8Array(n);
  crypto.getRandomValues(bytes);
  let out = '';
  for (let i = 0; i < n; i++) out += ID_ALPHABET[bytes[i] % ID_ALPHABET.length];
  return out;
}

/**
 * Durably persist one validated lead. Returns true iff it was written to KV.
 *
 * @param {object} env   Pages Function env (RATE_KV may or may not be bound).
 * @param {object} lead  { email, url?, score?, lang?, ip? } — email is required.
 * @returns {Promise<boolean>} true if stored, false if skipped/failed (fail-open).
 */
export async function saveLead(env, lead) {
  const kv = env && env.RATE_KV;
  if (!kv || !lead) return false;

  const email = String(lead.email || '').slice(0, 200).trim();
  if (!EMAIL_RE.test(email)) return false; // never store an invalid/empty lead

  try {
    const ts = new Date().toISOString();
    const record = {
      email,
      url: String(lead.url || '').slice(0, 300),
      score: lead.score == null ? '' : String(lead.score).slice(0, 8),
      lang: String(lead.lang || '').slice(0, 5),
      ip: String(lead.ip || '').slice(0, 64),
      ts,
    };
    // Key sorts chronologically; suffix guarantees uniqueness within a millisecond.
    const k = LEAD_PREFIX + ts + '-' + randSuffix();
    await kv.put(k, JSON.stringify(record)); // no expirationTtl -> persists until cleared
    return true;
  } catch {
    return false;
  }
}
