/**
 * POST /api/audit-lead — instant operator notification when a visitor requests a
 * fix plan from the free audit. The Web3Forms email (sent from the client) is the
 * visitor-facing receipt + a backup; this adds a Telegram push so leads aren't missed
 * (the privacy policy promises a manual fix-plan + price, so they must be honoured).
 *
 * Optional env (no-ops cleanly if unset): TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID.
 * No storage; best-effort; the token is never returned to the client.
 */
const RATE_LIMIT = 8; // per IP per window
const RATE_WINDOW_MS = 60_000;
const ipHits = new Map();

export async function onRequestPost(context) {
  const ip = context.request.headers.get('cf-connecting-ip') || 'unknown';
  if (rateLimited(ip)) return json({ ok: false, error: 'rate_limited' }, 429);

  let body = {};
  try { body = await context.request.json(); } catch { return json({ ok: false, error: 'bad_request' }, 400); }

  const email = String(body.email || '').slice(0, 200).trim();
  const url = String(body.url || '').slice(0, 300).trim();
  const score = String(body.score == null ? '' : body.score).slice(0, 8);
  const lang = String(body.lang || '').slice(0, 5);
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return json({ ok: false, error: 'invalid_email' }, 400);

  const env = context.env || {};
  const token = env.TELEGRAM_BOT_TOKEN;
  const chat = env.TELEGRAM_CHAT_ID;
  if (!token || !chat) return json({ ok: true, notified: false }); // not configured yet — no-op

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

  return json({ ok: true, notified });
}

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
  });
}

function rateLimited(ip) {
  const now = Date.now();
  const rec = ipHits.get(ip) || [];
  const fresh = rec.filter((t) => now - t < RATE_WINDOW_MS);
  fresh.push(now);
  ipHits.set(ip, fresh);
  if (ipHits.size > 5000) ipHits.clear();
  return fresh.length > RATE_LIMIT;
}
