/**
 * Shareable audit-report persistence.
 *
 * Until now an audit report was computed fresh on every POST /api/audit and
 * lived ONLY in the visitor's browser memory — a refresh, a copied URL, or a
 * link handed to a colleague lost it entirely (the report has no address).
 * This stores the finished report JSON in Cloudflare KV under a short,
 * unguessable id so /audit?r=<id> can re-render it and a "copy link" button can
 * share it.
 *
 * Storage: the SAME KV namespace the rate limiter and the monthly LLM budget
 * already use (RATE_KV), under a "report:" key prefix — so the owner still only
 * has to bind ONE namespace. See functions/_lib/audit-ratelimit.mjs.
 *
 * Fail-open by design. If RATE_KV is unbound, or any KV op throws:
 *   - saveReport()  returns null  -> the front-end simply offers no share link
 *   - getReport()   returns null  -> the ?r= path shows a friendly "expired" note
 *   - mergeSpeed()  returns false -> the stored report keeps its phase-1 score
 * Nothing here ever 500s, blocks, or 429s a visitor. Consequence: until the
 * owner binds RATE_KV in the Pages dashboard, the share feature is inert (no
 * link shown) exactly the way the report used to vanish — a zero-regression add.
 */

const REPORT_TTL_SECONDS = 60 * 60 * 24 * 30; // 30 days — long enough to share, short enough to forget
const ID_LEN = 12;                              // 12 chars of a 36-symbol alphabet ~= 62 bits, unguessable
const ID_ALPHABET = 'abcdefghijklmnopqrstuvwxyz0123456789';
const MAX_STORED_BYTES = 60_000;                // a normal report is ~3-8 KB; guards KV's 25 MB value limit and abuse

function key(id) { return 'report:' + id; }

// URL-safe, unguessable id from the platform CSPRNG (crypto.getRandomValues is
// present in both Cloudflare Workers and Node 18+). Not for security tokens —
// just enough entropy that report ids can't be walked or guessed.
export function genReportId() {
  const bytes = new Uint8Array(ID_LEN);
  crypto.getRandomValues(bytes);
  let out = '';
  for (let i = 0; i < ID_LEN; i++) out += ID_ALPHABET[bytes[i] % ID_ALPHABET.length];
  return out;
}

// Accept only ids we could have minted (defends the KV read against junk input).
export function validId(id) {
  return typeof id === 'string' && /^[a-z0-9]{6,24}$/.test(id);
}

// Whitelist the fields a shared report may carry: never the admin QA payload
// (model/usage/compare) and never transient flags (speedPending, reportId).
function shareable(payload) {
  return {
    ok: true,
    shared: true,
    finalUrl: payload.finalUrl || '',
    score: payload.score,
    summary: payload.summary || '',
    summarySource: payload.summarySource || 'template',
    variant: payload.variant || null,
    findings: Array.isArray(payload.findings) ? payload.findings : [],
    passed: Array.isArray(payload.passed) ? payload.passed : [],
    meta: payload.meta || null,
    aiRead: payload.aiRead || null,
  };
}

// Persist a finished phase-1 report; return its id, or null on any failure.
export async function saveReport(env, payload) {
  const kv = env && env.RATE_KV;
  if (!kv || !payload || payload.ok !== true) return null;
  try {
    const body = JSON.stringify(shareable(payload));
    if (body.length > MAX_STORED_BYTES) return null;
    const id = genReportId();
    await kv.put(key(id), body, { expirationTtl: REPORT_TTL_SECONDS });
    return id;
  } catch {
    return null;
  }
}

// Read a stored report by id; return the object (ok/shared forced true) or null.
export async function getReport(env, id) {
  const kv = env && env.RATE_KV;
  if (!kv || !validId(id)) return null;
  try {
    const raw = await kv.get(key(id));
    if (!raw) return null;
    const o = JSON.parse(raw);
    if (!o || typeof o !== 'object') return null;
    o.ok = true;
    o.shared = true;
    return o;
  } catch {
    return null;
  }
}

// Fold the phase-2 mobile-speed result into an already-stored report so a shared
// /audit?r=<id> shows the SAME final score the runner saw (phase-1 alone omits
// the speed delta). Keyed by the unguessable id the runner holds, so there is no
// overwrite-by-guess vector. Fail-open: any problem leaves the phase-1 report as-is.
export async function mergeSpeed(env, id, speed) {
  const kv = env && env.RATE_KV;
  if (!kv || !validId(id) || !speed) return false;
  try {
    const raw = await kv.get(key(id));
    if (!raw) return false;
    const o = JSON.parse(raw);
    if (!o || typeof o !== 'object') return false;
    const addF = Array.isArray(speed.findings) ? speed.findings : [];
    const addP = Array.isArray(speed.passed) ? speed.passed : [];
    // Append (not sort) to match how the live page streams the speed card in
    // below the existing findings.
    o.findings = (Array.isArray(o.findings) ? o.findings : []).concat(addF);
    o.passed = (Array.isArray(o.passed) ? o.passed : []).concat(addP);
    if (typeof speed.scoreDelta === 'number' && speed.scoreDelta !== 0) {
      o.score = Math.max(5, Math.min(100, Math.round((Number(o.score) || 0) + speed.scoreDelta)));
    }
    const body = JSON.stringify(o);
    if (body.length > MAX_STORED_BYTES) return false;
    await kv.put(key(id), body, { expirationTtl: REPORT_TTL_SECONDS });
    return true;
  } catch {
    return false;
  }
}
