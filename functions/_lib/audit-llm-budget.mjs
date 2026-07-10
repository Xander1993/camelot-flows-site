// Monthly AI-call budget for the /api/audit tool. Two steps so the counter
// tracks ACTUAL provider calls, not audits: llmBudgetOk() checks the cap up
// front (read-only), the audit fires its 2-3 callLlm() passes, then
// chargeLlmBudget() records exactly how many fired. Counting audits instead of
// calls under-counted paid usage by 2-3x (summary + AI-read [+ one retry], and
// N in admin-compare), so LLM_MONTHLY_CAP silently permitted 2-3x the ceiling
// its own env doc promises ("max AI calls per calendar month").
//
// Without a KV binding both functions fail-open: llmBudgetOk() allows and
// chargeLlmBudget() writes nothing — so behaviour is unchanged until the owner
// binds RATE_KV (the same namespace the rate limiter uses). One namespace, two
// keyspaces: 'rl:*' for the rate limiter, 'llm:<YYYY-MM>' for this budget.

function monthKey() {
  return 'llm:' + new Date().toISOString().slice(0, 7);
}

// Read-only cap check. Fail-open (no KV / KV error => allowed). Writes NOTHING —
// the real call count is charged afterwards by chargeLlmBudget().
export async function llmBudgetOk(env) {
  const kv = env && env.RATE_KV;
  if (!kv) return true;
  try {
    const used = Number((await kv.get(monthKey())) || 0);
    return used < Number(env.LLM_MONTHLY_CAP || 3000);
  } catch {
    return true;
  }
}

// Charge `n` provider calls against the monthly counter after they fire.
// Non-atomic read-modify-write — the same eventual-consistency trade-off as the
// rate limiter: a concurrent audit can overshoot the cap slightly, acceptable
// for a spend ceiling. No-op when RATE_KV is unbound, on any KV error, or n<=0.
export async function chargeLlmBudget(env, n) {
  const kv = env && env.RATE_KV;
  if (!kv || !(n > 0)) return;
  try {
    const key = monthKey();
    const used = Number((await kv.get(key)) || 0);
    await kv.put(key, String(used + n), { expirationTtl: 3_200_000 });
  } catch {
    /* best-effort; the provider-side key limit backstops a lost write */
  }
}
