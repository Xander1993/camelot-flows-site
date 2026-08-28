import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const output = process.argv[2] || 'docs/audit/content-validation-final.json';
const sitemap = await readFile(path.join(root, 'sitemap.xml'), 'utf8');
const urls = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((match) => match[1]);
const coreRoutes = ['/', '/quote-to-order', '/industries/technical-distributors', '/industries/hvac-refrigeration', '/websites', '/case-studies', '/about', '/contact'];
const failures = [];
const records = [];

function attrs(tag) {
  return Object.fromEntries([...tag.matchAll(/([^\s=/>]+)\s*=\s*(?:"([^"]*)"|'([^']*)')/g)].map((match) => [match[1].toLowerCase(), match[2] ?? match[3] ?? '']));
}

function fileFor(url) {
  const pathname = new URL(url).pathname;
  if (pathname === '/') return 'index.html';
  if (pathname.endsWith('/')) return `${pathname.slice(1)}index.html`;
  return `${pathname.slice(1)}.html`;
}

for (const url of urls) {
  const rel = fileFor(url);
  let html;
  try { html = await readFile(path.join(root, rel), 'utf8'); }
  catch { failures.push({ url, issue: 'missing output file', rel }); continue; }
  const canonicals = (html.match(/<link\b[^>]*>/gi) || []).map(attrs).filter((item) => item.rel === 'canonical').map((item) => item.href);
  const h1Count = (html.match(/<h1\b/gi) || []).length;
  const lang = html.match(/<html\b[^>]*lang=["']([^"']+)["']/i)?.[1] || null;
  const schemas = [];
  for (const match of html.matchAll(/<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)) {
    try {
      const value = JSON.parse(match[1]);
      const entries = Array.isArray(value?.['@graph']) ? value['@graph'] : [value];
      for (const entry of entries) if (entry?.['@type']) schemas.push(entry['@type']);
    } catch (error) { failures.push({ url, issue: 'invalid JSON-LD', error: String(error) }); }
  }
  const expectedLang = new URL(url).pathname.startsWith('/ro/') || new URL(url).pathname === '/ro/' ? 'ro' : new URL(url).pathname.startsWith('/ru/') || new URL(url).pathname === '/ru/' ? 'ru' : 'en';
  if (canonicals.length !== 1 || canonicals[0] !== url) failures.push({ url, issue: 'canonical mismatch', canonicals });
  if (h1Count !== 1) failures.push({ url, issue: 'H1 count', h1Count });
  if (lang !== expectedLang) failures.push({ url, issue: 'language mismatch', lang, expectedLang });
  if (/commercial\.(?:css|js)/.test(html)) failures.push({ url, issue: 'discarded redesign asset referenced' });
  records.push({ url, rel, canonical: canonicals[0] || null, lang, h1Count, schemaTypes: schemas });
}

for (const route of coreRoutes) {
  for (const prefix of ['', '/ro', '/ru']) {
    const localized = route === '/' ? `${prefix}/` || '/' : `${prefix}${route}`;
    const url = `https://camelotflows.dev${localized}`;
    const rel = fileFor(url);
    const html = await readFile(path.join(root, rel), 'utf8');
    const alternates = Object.fromEntries((html.match(/<link\b[^>]*>/gi) || []).map(attrs).filter((item) => item.hreflang && item.href).map((item) => [item.hreflang, item.href]));
    for (const code of ['en', 'ro', 'ru', 'x-default']) if (!alternates[code]) failures.push({ url, issue: `missing hreflang ${code}` });
  }
}

const contact = await readFile(path.join(root, 'contact.html'), 'utf8');
for (const name of ['name','company','website','country','products_services','request_channels','current_process','current_tools','monthly_volume','time_consuming_step','human_approval','desired_result','attachment','preferred_contact']) {
  if (!new RegExp(`name=["']${name}["']`).test(contact)) failures.push({ url: 'https://camelotflows.dev/contact', issue: `missing form field ${name}` });
}
if (/07:00|09:30|nap schedule|Arthur's nap/i.test(await readFile(path.join(root, 'about.html'), 'utf8'))) failures.push({ url: 'https://camelotflows.dev/about', issue: 'detailed personal schedule remains' });

const result = {
  generatedAt: new Date().toISOString(),
  sitemapUrls: urls.length,
  filesValidated: records.length,
  coreLocalizedPagesChecked: coreRoutes.length * 3,
  jsonLdDocuments: records.reduce((sum, record) => sum + record.schemaTypes.length, 0),
  schemaTypes: [...new Set(records.flatMap((record) => record.schemaTypes).flat())].sort(),
  failures,
};
await mkdir(path.dirname(path.join(root, output)), { recursive: true });
await writeFile(path.join(root, output), `${JSON.stringify(result, null, 2)}\n`, 'utf8');
console.log(JSON.stringify(result, null, 2));
if (failures.length) process.exitCode = 1;
