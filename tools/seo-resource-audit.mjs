import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RESOURCE_TAG_RE = /<(script|img|source|video|audio|link)\b[^>]*>/gi;
const RESOURCE_ATTR_RE = /\b(src|href|poster|srcset)=["']([^"']+)["']/gi;

function sitemapUrls(xml) {
  return [...xml.matchAll(/<loc>([^<]+)<\/loc>/gi)].map((match) => match[1].trim());
}

export function extractFirstPartyResources(html, pageUrl, origin) {
  const found = new Set();
  for (const tagMatch of html.matchAll(RESOURCE_TAG_RE)) {
    if (/^<link\b/i.test(tagMatch[0]) && (/\brel=["'](?:prefetch|canonical|alternate)["']/i.test(tagMatch[0]) || /\bas=["']document["']/i.test(tagMatch[0]))) continue;
    for (const match of tagMatch[0].matchAll(RESOURCE_ATTR_RE)) {
      const values = match[1].toLowerCase() === 'srcset'
        ? match[2].split(',').map((part) => part.trim().split(/\s+/)[0])
        : [match[2]];
      for (const value of values) {
        if (!value || value.startsWith('data:')) continue;
        try {
          const url = new URL(value, pageUrl);
          if (url.origin === origin) found.add(url.href);
        } catch {}
      }
    }
  }
  return [...found];
}

export async function auditResources({ baseUrl, fetchImpl = fetch }) {
  const base = new URL(baseUrl);
  const sitemapUrl = new URL('/sitemap.xml', base);
  const sitemapResponse = await fetchImpl(sitemapUrl);
  const pages = sitemapUrls(await sitemapResponse.text()).map((entry) => {
    const listed = new URL(entry);
    return new URL(`${listed.pathname}${listed.search}`, base).href;
  });
  const resources = new Map();
  const pageFailures = [];

  for (const page of pages) {
    const response = await fetchImpl(page, { redirect: 'follow' });
    if (response.status !== 200 || !(response.headers.get('content-type') || '').includes('text/html')) {
      pageFailures.push({ url: page, status: response.status, contentType: response.headers.get('content-type') || '' });
      continue;
    }
    const html = await response.text();
    for (const resource of extractFirstPartyResources(html, response.url || page, base.origin)) {
      if (!resources.has(resource)) resources.set(resource, new Set());
      resources.get(resource).add(page);
    }
  }

  const checks = [];
  for (const [url, foundOn] of resources) {
    try {
      const response = await fetchImpl(url, { redirect: 'follow' });
      const contentType = response.headers.get('content-type') || '';
      const htmlFallback = contentType.includes('text/html') && !/\.html?(?:[?#]|$)/i.test(url);
      checks.push({ url, status: response.status, contentType, htmlFallback, foundOn: [...foundOn] });
    } catch (error) {
      checks.push({ url, status: null, contentType: '', htmlFallback: false, error: String(error), foundOn: [...foundOn] });
    }
  }
  const failures = checks.filter((item) => item.status !== 200 || item.htmlFallback);
  return {
    generatedAt: new Date().toISOString(),
    baseUrl: base.href,
    sitemapStatus: sitemapResponse.status,
    pageCount: pages.length,
    pageFailures,
    uniqueResourceCount: checks.length,
    resourceFailures: failures,
    checks,
  };
}

async function main(argv) {
  const options = {};
  for (let index = 0; index < argv.length; index += 1) {
    if (argv[index] === '--base') options.baseUrl = argv[++index];
    else if (argv[index] === '--output') options.output = argv[++index];
  }
  if (!options.baseUrl || !options.output) throw new Error('Usage: node tools/seo-resource-audit.mjs --base URL --output FILE');
  const result = await auditResources(options);
  await fs.mkdir(path.dirname(options.output), { recursive: true });
  await fs.writeFile(options.output, `${JSON.stringify(result, null, 2)}\n`, 'utf8');
  process.stdout.write(`${JSON.stringify({ output: options.output, pages: result.pageCount, resources: result.uniqueResourceCount, pageFailures: result.pageFailures.length, resourceFailures: result.resourceFailures.length })}\n`);
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main(process.argv.slice(2)).catch((error) => { console.error(error); process.exitCode = 1; });
}
