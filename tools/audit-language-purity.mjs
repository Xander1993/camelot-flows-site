import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const sitemapText = await readFile(path.join(root, 'sitemap.xml'), 'utf8');
const urls = [...sitemapText.matchAll(/<loc>([^<]+)<\/loc>/g)].map((match) => match[1]);
const sitemap = new Set(urls.map(normalizeUrl));

function normalizeUrl(value) {
  const url = new URL(value);
  url.hash = '';
  if (url.pathname !== '/' && url.pathname.endsWith('/')) url.pathname = url.pathname.slice(0, -1);
  return url.href;
}

function routeFile(rawUrl) {
  const pathname = new URL(rawUrl).pathname;
  if (pathname === '/') return 'index.html';
  const clean = pathname.replace(/^\//, '').replace(/\/$/, '');
  return pathname.endsWith('/') ? path.join(clean, 'index.html') : `${clean}.html`;
}

function decode(value = '') {
  return value
    .replace(/&nbsp;|&#160;/gi, ' ')
    .replace(/&amp;/gi, '&').replace(/&quot;/gi, '"').replace(/&#39;|&apos;/gi, "'")
    .replace(/&lt;/gi, '<').replace(/&gt;/gi, '>')
    .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)))
    .replace(/\s+/g, ' ').trim();
}

function textOnly(value = '') {
  return decode(value.replace(/<script\b[\s\S]*?<\/script>/gi, ' ').replace(/<style\b[\s\S]*?<\/style>/gi, ' ')
    .replace(/<svg\b[\s\S]*?<\/svg>/gi, ' ').replace(/<[^>]+>/g, ' '));
}

const words = {
  en: new Set('the and for with your from this that you we our is are to of in on a an as by or not website business service services page process'.split(' ')),
  ro: new Set('și si este sunt pentru cu din la un o care în in ale al pe sau nu site afacere servicii serviciu pagină pagina proces'.split(' ')),
  ru: new Set('и в на с для это что вы мы ваш ваша ваши из по или не сайт бизнес услуга услуги страница процесс'.split(' '))
};

function scores(value) {
  const tokens = textOnly(value).toLocaleLowerCase().match(/[\p{L}]+/gu) || [];
  const result = { en: 0, ro: 0, ru: 0, tokens: tokens.length };
  for (const token of tokens) {
    if (/\p{Script=Cyrillic}/u.test(token)) result.ru += 3;
    if (/[ăâîșşțţ]/u.test(token)) result.ro += 3;
    for (const lang of ['en', 'ro', 'ru']) if (words[lang].has(token)) result[lang] += 1;
  }
  return result;
}

function detect(value, expected) {
  const result = scores(value);
  const plain = textOnly(value);
  if (expected === 'en' && !/[ăâîșşțţ]/iu.test(plain) && !/\p{Script=Cyrillic}/u.test(plain)) return 'en';
  const ordered = ['en', 'ro', 'ru'].sort((a, b) => result[b] - result[a]);
  if (!result.tokens || result[ordered[0]] < 2) return expected;
  return ordered[0];
}

function foreignConflict(value, expected) {
  const result = scores(value);
  const foreign = ['en', 'ro', 'ru'].filter((lang) => lang !== expected).sort((a, b) => result[b] - result[a])[0];
  return result[foreign] >= 8 && result[foreign] > result[expected] * 1.5 ? foreign : '';
}

function csv(value) {
  const string = String(value ?? '');
  return /[",\r\n]/.test(string) ? `"${string.replaceAll('"', '""')}"` : string;
}

const rows = [];
for (const url of urls) {
  const html = await readFile(path.join(root, routeFile(url)), 'utf8');
  const expected = new URL(url).pathname.startsWith('/ro/') || new URL(url).pathname === '/ro' ? 'ro'
    : new URL(url).pathname.startsWith('/ru/') || new URL(url).pathname === '/ru' ? 'ru' : 'en';
  const htmlLang = html.match(/<html\b[^>]*\blang="([^"]+)"/i)?.[1]?.toLowerCase() || '';
  const title = html.match(/<title>([\s\S]*?)<\/title>/i)?.[1] || '';
  const h1 = html.match(/<h1\b[^>]*>([\s\S]*?)<\/h1>/i)?.[1] || '';
  const canonical = decode(html.match(/<link\b(?=[^>]*\brel="canonical")(?=[^>]*\bhref="([^"]+)")[^>]*>/i)?.[1] || '');
  const alternates = [...html.matchAll(/<link\b(?=[^>]*\brel="alternate")(?=[^>]*\bhreflang="([^"]+)")(?=[^>]*\bhref="([^"]+)")[^>]*>/gi)]
    .map((match) => ({ lang: match[1], url: decode(match[2]) }));
  const hreflangSet = alternates.map((entry) => `${entry.lang}=${entry.url}`).join(' | ');
  const hiddenAlternate = /data-lang-content\s*=\s*["']/i.test(html);
  const body = html.match(/<body\b[^>]*>([\s\S]*?)<\/body>/i)?.[1] || '';
  const primary = body.replace(/<nav\b[\s\S]*?<\/nav>/gi, ' ').replace(/<footer\b[\s\S]*?<\/footer>/gi, ' ');
  const nav = html.match(/<nav\b[\s\S]*?<\/nav>/i)?.[0] || '';
  const schemas = [...html.matchAll(/<script\b[^>]*type="application\/ld\+json"[^>]*>([\s\S]*?)<\/script>/gi)].map((match) => match[1]).join(' ');
  const forms = [...html.matchAll(/<form\b[\s\S]*?<\/form>/gi)].map((match) => match[0]).join(' ');

  const problems = [];
  if (htmlLang !== expected) problems.push(`html lang is ${htmlLang || 'missing'}, expected ${expected}`);
  if (detect(title, expected) !== expected) problems.push(`title appears ${detect(title, expected)}`);
  if (detect(h1, expected) !== expected) problems.push(`H1 appears ${detect(h1, expected)}`);
  for (const [area, value] of [['navigation', nav], ['body', primary], ['schema', schemas], ['form', forms]]) {
    const conflict = foreignConflict(value, expected);
    if (conflict) problems.push(`${area} contains dominant ${conflict}`);
  }
  if (hiddenAlternate) problems.push('full alternate-language data block found');
  if (!canonical || normalizeUrl(canonical) !== normalizeUrl(url)) problems.push('canonical does not match current language URL');
  for (const alternate of alternates) {
    if (alternate.lang !== 'x-default' && !sitemap.has(normalizeUrl(alternate.url))) problems.push(`hreflang ${alternate.lang} target is not indexable`);
  }
  if (!alternates.some((entry) => entry.lang === expected && normalizeUrl(entry.url) === normalizeUrl(url))) problems.push('self hreflang missing');

  rows.push({
    URL: url,
    'detected language': detect(primary, expected),
    'html lang': htmlLang,
    'title language': detect(title, expected),
    'H1 language': detect(h1, expected),
    'hidden alternate-language content found': hiddenAlternate ? 'yes' : 'no',
    canonical,
    'hreflang set': hreflangSet,
    status: problems.length ? 'FAIL' : 'PASS',
    action: problems.join('; ')
  });
}

const headers = ['URL', 'detected language', 'html lang', 'title language', 'H1 language', 'hidden alternate-language content found', 'canonical', 'hreflang set', 'status', 'action'];
const output = [headers.join(','), ...rows.map((row) => headers.map((header) => csv(row[header])).join(','))].join('\n') + '\n';
await writeFile(path.join(root, 'docs', 'LANGUAGE_PURITY_AUDIT.csv'), output, 'utf8');
process.stdout.write(JSON.stringify({ audited: rows.length, pass: rows.filter((row) => row.status === 'PASS').length, fail: rows.filter((row) => row.status === 'FAIL').length, failures: rows.filter((row) => row.status === 'FAIL').map((row) => ({ url: row.URL, action: row.action })) }, null, 2) + '\n');
