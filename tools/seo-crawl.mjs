import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const REDIRECT_STATUSES = new Set([301, 302, 303, 307, 308]);

function decodeEntities(value = '') {
  return value
    .replace(/&nbsp;/gi, ' ')
    .replace(/&amp;/gi, '&')
    .replace(/&quot;/gi, '"')
    .replace(/&#39;|&apos;/gi, "'")
    .replace(/&lt;/gi, '<')
    .replace(/&gt;/gi, '>')
    .replace(/&#(\d+);/g, (_, code) => String.fromCodePoint(Number(code)))
    .replace(/&#x([0-9a-f]+);/gi, (_, code) => String.fromCodePoint(Number.parseInt(code, 16)));
}

function textContent(fragment = '') {
  return decodeEntities(fragment.replace(/<script\b[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style\b[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim());
}

function attributes(tag = '') {
  const result = {};
  const pattern = /([^\s=/>]+)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))/g;
  let match;
  while ((match = pattern.exec(tag))) result[match[1].toLowerCase()] = match[2] ?? match[3] ?? match[4] ?? '';
  return result;
}

function firstTag(html, name) {
  return html.match(new RegExp(`<${name}\\b[^>]*>`, 'i'))?.[0] || '';
}

function findMeta(html, name) {
  for (const tag of html.match(/<meta\b[^>]*>/gi) || []) {
    const attrs = attributes(tag);
    if ((attrs.name || '').toLowerCase() === name.toLowerCase()) return attrs.content || null;
  }
  return null;
}

function findCanonical(html, finalUrl) {
  for (const tag of html.match(/<link\b[^>]*>/gi) || []) {
    const attrs = attributes(tag);
    if ((attrs.rel || '').toLowerCase().split(/\s+/).includes('canonical') && attrs.href) {
      return new URL(attrs.href, finalUrl).href;
    }
  }
  return null;
}

function findHreflang(html, finalUrl) {
  const rows = [];
  for (const tag of html.match(/<link\b[^>]*>/gi) || []) {
    const attrs = attributes(tag);
    if ((attrs.rel || '').toLowerCase().split(/\s+/).includes('alternate') && attrs.hreflang && attrs.href) {
      rows.push({ lang: attrs.hreflang.toLowerCase(), href: new URL(attrs.href, finalUrl).href });
    }
  }
  return rows;
}

function normalizeDocumentUrl(raw, baseUrl, allowedOrigins) {
  try {
    const url = new URL(raw, baseUrl);
    if (!allowedOrigins.has(url.origin) || !['http:', 'https:'].includes(url.protocol)) return null;
    url.hash = '';
    url.search = '';
    const last = url.pathname.split('/').pop();
    if (url.pathname.startsWith('/api/') || url.pathname.startsWith('/cdn-cgi/')) return null;
    if (last && last.includes('.') && !/\.html?$/i.test(last)) return null;
    return url.href;
  } catch {
    return null;
  }
}

function parseHtml(html, finalUrl, allowedOrigins) {
  const htmlAttrs = attributes(firstTag(html, 'html'));
  const title = textContent(html.match(/<title\b[^>]*>([\s\S]*?)<\/title>/i)?.[1] || '') || null;
  const h1 = [...html.matchAll(/<h1\b[^>]*>([\s\S]*?)<\/h1>/gi)].map((match) => textContent(match[1])).filter(Boolean);
  const mainFragment = html.match(/<(?:main|article)\b[^>]*>([\s\S]*?)<\/(?:main|article)>/i)?.[1]
    || html.match(/<[^>]+role=["']main["'][^>]*>([\s\S]*?)<\/[^>]+>/i)?.[1]
    || html.match(/<body\b[^>]*>([\s\S]*?)<\/body>/i)?.[1]
    || '';
  const initialMainTextLength = textContent(mainFragment).length;
  const links = [];
  const internalHtmlAliasLinks = [];
  for (const tag of html.match(/<a\b[^>]*>/gi) || []) {
    const href = attributes(tag).href;
    if (!href) continue;
    const target = normalizeDocumentUrl(href, finalUrl, allowedOrigins);
    if (!target) continue;
    links.push(target);
    if (/\.html(?:$|[?#])/i.test(href)) internalHtmlAliasLinks.push(href);
  }
  for (const tag of html.match(/<link\b[^>]*>/gi) || []) {
    const attrs = attributes(tag);
    const rels = (attrs.rel || '').toLowerCase().split(/\s+/);
    if (!(rels.includes('prefetch') || (rels.includes('preload') && attrs.as === 'document')) || !attrs.href) continue;
    const target = normalizeDocumentUrl(attrs.href, finalUrl, allowedOrigins);
    if (!target) continue;
    links.push(target);
    if (/\.html(?:$|[?#])/i.test(attrs.href)) internalHtmlAliasLinks.push(attrs.href);
  }
  return {
    canonical: findCanonical(html, finalUrl),
    metaRobots: findMeta(html, 'robots'),
    title,
    metaDescription: findMeta(html, 'description'),
    h1,
    language: htmlAttrs.lang || null,
    hreflang: findHreflang(html, finalUrl),
    initialHtmlBytes: Buffer.byteLength(html),
    initialMainTextLength,
    mainContentInInitialHtml: initialMainTextLength >= 100,
    internalLinks: links,
    internalHtmlAliasLinks: [...new Set(internalHtmlAliasLinks)],
  };
}

async function requestWithHops(startUrl, fetchImpl, maxRedirects = 10) {
  let currentUrl = startUrl;
  let firstStatus = null;
  const redirectChain = [];
  for (let index = 0; index <= maxRedirects; index += 1) {
    const response = await fetchImpl(currentUrl, { redirect: 'manual', cache: 'no-store' });
    if (firstStatus === null) firstStatus = response.status;
    if (!REDIRECT_STATUSES.has(response.status)) {
      return { response, status: firstStatus, finalUrl: currentUrl, redirectChain };
    }
    const location = response.headers.get('location');
    const destination = location ? new URL(location, currentUrl).href : null;
    redirectChain.push({ from: currentUrl, status: response.status, to: destination });
    if (!destination) return { response, status: firstStatus, finalUrl: currentUrl, redirectChain };
    currentUrl = destination;
  }
  throw new Error(`redirect limit exceeded for ${startUrl}`);
}

export async function crawlSite({ baseUrl, seeds = [], fetchImpl = fetch, maxUrls = 300 } = {}) {
  if (!baseUrl) throw new TypeError('baseUrl is required');
  const base = new URL(baseUrl);
  const homeUrl = new URL('/', base).href;
  const sitemapUrl = new URL('/sitemap.xml', base).href;
  const sitemapResponse = await fetchImpl(sitemapUrl, { redirect: 'manual', cache: 'no-store' });
  const sitemapBody = await sitemapResponse.text();
  const sitemapUrls = [...sitemapBody.matchAll(/<loc>\s*([^<]+?)\s*<\/loc>/gi)].map((match) => decodeEntities(match[1]));
  const allowedOrigins = new Set([base.origin, ...seeds.map((seed) => new URL(seed, base).origin)]);
  const normalize = (value, parent = homeUrl) => normalizeDocumentUrl(value, parent, allowedOrigins);
  const normalizedSitemapUrls = sitemapUrls.map((url) => {
    try {
      const listed = new URL(url, base);
      return normalize(new URL(`${listed.pathname}${listed.search}`, base).href);
    } catch {
      return null;
    }
  }).filter(Boolean);
  const sitemapSet = new Set(normalizedSitemapUrls);
  const queue = [...new Set([homeUrl, ...normalizedSitemapUrls, ...seeds.map((seed) => normalize(seed)).filter(Boolean)])];
  const queued = new Set(queue);
  const inbound = new Map();
  const discoveredFrom = new Map();
  const records = [];

  while (queue.length && records.length < maxUrls) {
    const requestedUrl = queue.shift();
    try {
      const result = await requestWithHops(requestedUrl, fetchImpl);
      const contentType = result.response.headers.get('content-type') || '';
      const xRobots = result.response.headers.get('x-robots-tag') || '';
      let parsed = {
        canonical: null, metaRobots: null, title: null, metaDescription: null, h1: [], language: null,
        hreflang: [], initialHtmlBytes: 0, initialMainTextLength: 0, mainContentInInitialHtml: false,
        internalLinks: [], internalHtmlAliasLinks: [],
      };
      if (result.response.status === 200 && contentType.includes('text/html')) {
        parsed = parseHtml(await result.response.text(), result.finalUrl, allowedOrigins);
        for (const target of parsed.internalLinks) {
          inbound.set(target, (inbound.get(target) || 0) + 1);
          if (!discoveredFrom.has(target)) discoveredFrom.set(target, result.finalUrl);
          if (!queued.has(target)) { queued.add(target); queue.push(target); }
        }
      }
      records.push({
        url: requestedUrl,
        status: result.status,
        redirectDestination: result.redirectChain[0]?.to || null,
        redirectHops: result.redirectChain.length,
        redirectChain: result.redirectChain,
        finalUrl: result.finalUrl,
        finalStatus: result.response.status,
        contentType,
        canonical: parsed.canonical,
        metaRobots: [xRobots, parsed.metaRobots].filter(Boolean).join(', ') || null,
        title: parsed.title,
        metaDescription: parsed.metaDescription,
        h1: parsed.h1,
        language: parsed.language,
        hreflang: parsed.hreflang,
        inSitemap: sitemapSet.has(requestedUrl),
        internalLinksOut: parsed.internalLinks.length,
        internalHtmlAliasLinks: parsed.internalHtmlAliasLinks,
        initialHtmlBytes: parsed.initialHtmlBytes,
        initialMainTextLength: parsed.initialMainTextLength,
        mainContentInInitialHtml: parsed.mainContentInInitialHtml,
        discoveredFrom: discoveredFrom.get(requestedUrl) || null,
      });
    } catch (error) {
      records.push({ url: requestedUrl, error: String(error), status: null, finalStatus: null, redirectHops: null });
    }
  }

  for (const record of records) record.internalLinksIn = inbound.get(record.url) || 0;
  const canonicalGroups = new Map();
  for (const record of records) {
    if (record.finalStatus !== 200 || !record.canonical) continue;
    const urls = canonicalGroups.get(record.canonical) || [];
    urls.push(record.url);
    canonicalGroups.set(record.canonical, urls);
  }

  return {
    generatedAt: new Date().toISOString(),
    baseUrl: base.href,
    sitemap: { url: sitemapUrl, status: sitemapResponse.status, urlCount: normalizedSitemapUrls.length },
    crawledUrlCount: records.length,
    records,
    duplicateCanonicalGroups: [...canonicalGroups.entries()]
      .filter(([, urls]) => urls.length > 1)
      .map(([canonical, urls]) => ({ canonical, urls })),
  };
}

async function main(argv) {
  const options = { seeds: [] };
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === '--base') options.baseUrl = argv[++index];
    else if (arg === '--seed') options.seeds.push(argv[++index]);
    else if (arg === '--output') options.output = argv[++index];
    else if (arg === '--max-urls') options.maxUrls = Number(argv[++index]);
  }
  if (!options.baseUrl || !options.output) throw new Error('Usage: node tools/seo-crawl.mjs --base URL --output FILE [--seed URL]');
  const result = await crawlSite(options);
  await fs.mkdir(path.dirname(options.output), { recursive: true });
  await fs.writeFile(options.output, `${JSON.stringify(result, null, 2)}\n`, 'utf8');
  process.stdout.write(`${JSON.stringify({ output: options.output, crawled: result.crawledUrlCount, sitemap: result.sitemap })}\n`);
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main(process.argv.slice(2)).catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
}
