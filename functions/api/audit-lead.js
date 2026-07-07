/**
 * POST /api/audit-lead — capture a visitor who requests a fix plan from the free
 * audit. Three layers, so a lead is never silently lost:
 *   1. durable KV backstop (saveLead) — persisted BEFORE any push, independent of it,
 *      so even if every push channel fails the lead survives on the server;
 *   2. instant operator Telegram push (best-effort, no-op unless configured);
 *   3. (client-side) a Web3Forms receipt email.
 * The privacy policy promises a manual fix-plan + price, so leads must be honoured.
 *
 * Returns { ok, stored, notified } so the client can show an HONEST result: a green
 * confirmation only when at least one channel actually accepted the lead.
 *
 * Optional env (all no-op cleanly if unset): RATE_KV (durable store; also gates the
 * rate limiter + LLM budget), TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID. The token is
 * never returned to the client.
 */
import { rateLimit } from '../_lib/audit-ratelimit.mjs';
import { saveLead } from '../_lib/audit-lead-store.mjs';

const RATE_LIMIT = 8; // per IP per window
const RATE_WINDOW_MS = 60_000;

export async function onRequestPost(context) {
  const env = context.env || {};
  const ip = context.request.headers.get('cf-connecting-ip') || 'unknown';
  if (await rateLimit(env, ip, { limit: RATE_LIMIT, windowMs: RATE_WINDOW_MS, prefix: 'lead' })) {
    return json({ ok: false, error: 'rate_limited' }, 429);
  }

  let body = {};
  try { body = await context.request.json(); } catch { return json({ ok: false, error: 'bad_request' }, 400); }

  const email = String(body.email || '').slice(0, 200).trim();
  const url = String(body.url || '').slice(0, 300).trim();
  const score = String(body.score == null ? '' : body.score).slice(0, 8);
  const lang = String(body.lang || '').slice(0, 5);
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return json({ ok: false, error: 'invalid_email' }, 400);

  // 1) Durable backstop FIRST, independent of any push channel: persist the lead to
  // KV so it survives even if Telegram is unconfigured and the client email fails.
  const stored = await saveLead(env, { email, url, score, lang, ip });

  const token = env.TELEGRAM_BOT_TOKEN;
  const chat = env.TELEGRAM_CHAT_ID;
  if (!token || !chat) return json({ ok: true, stored, notified: false }); // no push configured

  const text =
    '\u{1F514} New audit fix-plan lead\n' +
    'Site: ' + (url || '—') + '\n' +
    'Score: ' + (score || '—') + '/100\n' +
    'Email: ' + email +
    (lang ? '\nLang: ' + lang : '');

  let notified = false;
  try {
    const r = await fetch('https://api.telegram.org/bot' + token + '/sendMessage', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ chat_id: chat, text, disable_web_page_preview: true }),
    });
    notified = r.ok;
  } catch { notified = false; }

  return json({ ok: true, stored, notified });
}

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
  });
}
