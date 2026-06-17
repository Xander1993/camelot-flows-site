// LLM A/B helpers for the audit tool. Provider-agnostic: any OpenAI-compatible
// /chat/completions endpoint (Nous portal, OpenRouter) — switched via env, not code.

export function pickModel(models, rand) {
  return models[Math.floor(rand * models.length)];
}

const LANG_NAME = { en: 'English', ro: 'Romanian', ru: 'Russian' };

export function buildLlmMessages(findings, url, score, lang) {
  const language = LANG_NAME[lang] || 'English';
  const system = [
    'You write the results summary for a free website audit tool made by Camelot Flows, a web studio for local service businesses.',
    'You will receive a JSON list of technical findings for one page.',
    'Rewrite them as a short, plain-language summary for a non-technical business owner: what is wrong, why it costs them customers, what to fix first.',
    'Use ONLY the findings provided. Do not invent, assume, or add any issue, metric, or fact that is not in the list. Do not exaggerate severity.',
    'Tone: helpful expert, no hype, no scare tactics. 120-180 words. Plain prose, no markdown headers, no bullet lists.',
    'Write the entire summary in ' + language + '. Keep proper nouns and technical tag names (such as title, tel:, hreflang, Open Graph, LCP) as-is.',
  ].join(' ');
  const user = JSON.stringify({ url, score, findings }, null, 1);
  return [
    { role: 'system', content: system },
    { role: 'user', content: user },
  ];
}

const LLM_TIMEOUT_MS = 15_000;

export async function callLlm(env, model, messages) {
  const base = (env.LLM_BASE_URL || 'https://inference-api.nousresearch.com/v1').replace(/\/$/, '');
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), LLM_TIMEOUT_MS);
  try {
    const res = await fetch(`${base}/chat/completions`, {
      method: 'POST',
      signal: controller.signal,
      headers: {
        'content-type': 'application/json',
        authorization: `Bearer ${env.LLM_API_KEY}`,
      },
      body: JSON.stringify({ model, messages, max_tokens: 650, temperature: 0.4 }),
    });
    if (!res.ok) return { error: 'LLM HTTP ' + res.status };
    const data = await res.json();
    const text = data && data.choices && data.choices[0] && data.choices[0].message
      ? String(data.choices[0].message.content || '').trim()
      : '';
    if (!text) return { error: 'empty LLM response' };
    return { text, usage: data.usage || null };
  } catch (e) {
    return { error: e && e.name === 'AbortError' ? 'LLM timeout' : 'LLM call failed' };
  } finally {
    clearTimeout(timer);
  }
}
