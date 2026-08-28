import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const sitemap = await readFile(path.join(root, 'sitemap.xml'), 'utf8');
const urls = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((match) => match[1]);

function routeFile(rawUrl) {
  const pathname = new URL(rawUrl).pathname;
  if (pathname === '/') return 'index.html';
  const clean = pathname.replace(/^\//, '').replace(/\/$/, '');
  return pathname.endsWith('/') ? path.join(clean, 'index.html') : `${clean}.html`;
}

function text(value = '') {
  return value.replace(/<[^>]+>/g, ' ').replace(/&amp;/gi, '&').replace(/&quot;/gi, '"')
    .replace(/&#39;|&apos;/gi, "'").replace(/&[a-z0-9#]+;/gi, ' ').replace(/\s+/g, ' ').trim();
}

function expectedLanguage(url) {
  const pathname = new URL(url).pathname;
  return pathname === '/ro' || pathname.startsWith('/ro/') ? 'ro' : pathname === '/ru' || pathname.startsWith('/ru/') ? 'ru' : 'en';
}

const localized = {
  en: { home: 'Home', offer: 'Scope and price are confirmed in the written proposal.' },
  ro: { home: 'Acasă', offer: 'Domeniul și prețul sunt confirmate în propunerea scrisă.' },
  ru: { home: 'Главная', offer: 'Объём и цена подтверждаются в письменном предложении.' }
};

let removedFaq = 0;
let normalized = 0;
for (const url of urls) {
  const file = path.join(root, routeFile(url));
  let html = await readFile(file, 'utf8');
  const lang = expectedLanguage(url);
  const title = text(html.match(/<title>([\s\S]*?)<\/title>/i)?.[1] || '');
  const h1 = text(html.match(/<h1\b[^>]*>([\s\S]*?)<\/h1>/i)?.[1] || title);
  const description = text(html.match(/<meta\b(?=[^>]*\bname="description")(?=[^>]*\bcontent="([^"]*)")[^>]*>/i)?.[1] || '');

  html = html.replace(/<script\b[^>]*type="application\/ld\+json"[^>]*>([\s\S]*?)<\/script>/gi, (whole, raw) => {
    let data;
    try { data = JSON.parse(raw); } catch { return whole; }
    const type = data['@type'];
    if (type === 'FAQPage') {
      removedFaq++;
      return '';
    }
    data.inLanguage = lang;
    if (['BlogPosting', 'Article', 'NewsArticle'].includes(type)) {
      data.headline = h1;
      data.description = description;
    }
    if (['Organization', 'WebSite'].includes(type)) data.description = description;
    if (type === 'Service') {
      data.name = h1;
      data.description = description;
    }
    if (type === 'BreadcrumbList' && Array.isArray(data.itemListElement)) {
      if (data.itemListElement[0]) data.itemListElement[0].name = localized[lang].home;
      if (data.itemListElement.at(-1)) data.itemListElement.at(-1).name = h1;
    }
    if (lang !== 'en' && data.offers && typeof data.offers === 'object' && data.offers.description) {
      data.offers.description = localized[lang].offer;
    }
    normalized++;
    return `<script type="application/ld+json">${JSON.stringify(data)}</script>`;
  });
  await writeFile(file, html, 'utf8');
}

process.stdout.write(JSON.stringify({ pages: urls.length, normalized, removedFaq }, null, 2) + '\n');
