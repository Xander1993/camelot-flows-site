import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';

const root = path.resolve(import.meta.dirname, '..');
const matrixPath = path.join(root, 'docs', 'URL_CONTENT_MATRIX.csv');

function parseCsv(text) {
  const rows = [];
  let row = [], field = '', quoted = false;
  for (let i = 0; i < text.length; i++) {
    const char = text[i];
    if (quoted) {
      if (char === '"' && text[i + 1] === '"') { field += '"'; i++; }
      else if (char === '"') quoted = false;
      else field += char;
    } else if (char === '"') quoted = true;
    else if (char === ',') { row.push(field); field = ''; }
    else if (char === '\n') { row.push(field.replace(/\r$/, '')); rows.push(row); row = []; field = ''; }
    else field += char;
  }
  if (field || row.length) { row.push(field); rows.push(row); }
  const headers = rows.shift();
  return rows.filter((item) => item.length > 1).map((item) => Object.fromEntries(headers.map((header, index) => [header, item[index] ?? ''])));
}

function csv(value) {
  const string = String(value ?? '');
  return /[",\r\n]/.test(string) ? `"${string.replaceAll('"', '""')}"` : string;
}

function routeFile(rawUrl) {
  const pathname = new URL(rawUrl).pathname;
  if (pathname === '/') return 'index.html';
  const clean = pathname.replace(/^\//, '').replace(/\/$/, '');
  return pathname.endsWith('/') ? path.join(clean, 'index.html') : `${clean}.html`;
}

function basePath(rawUrl) {
  const pathname = new URL(rawUrl).pathname.replace(/^\/(ro|ru)(?=\/)/, '');
  return pathname !== '/' ? pathname.replace(/\/$/, '') : '/';
}

function categoryFor(route) {
  if (['/', '/about', '/contact', '/work-with-me', '/quote-to-order'].includes(route)) return 'CORE COMMERCIAL';
  if (route.startsWith('/industries/')) return 'INDUSTRY';
  if (route === '/case-studies') return 'CASE STUDY';
  if (['/audit', '/service-automation', '/merlin-automation'].includes(route)) return 'SUPPORTING SERVICE';
  if (route === '/blog/building-dreamscape-in-parallel') return 'FOUNDER NOTE';
  if (route.startsWith('/blog/')) return 'TOPICAL ARTICLE';
  if (['/blog', '/privacy', '/legal'].includes(route)) return 'TECHNICAL OR UTILITY';
  return 'LEGACY WITH ACTIVE VALUE';
}

const rows = parseCsv(await readFile(matrixPath, 'utf8'));
const fingerprints = new Map();
for (const row of rows) {
  const html = await readFile(path.join(root, routeFile(row['current URL'])), 'utf8');
  const main = html.match(/<main\b[^>]*>([\s\S]*?)<\/main>/i)?.[1] || html.match(/<body\b[^>]*>([\s\S]*?)<\/body>/i)?.[1] || '';
  const text = main.replace(/<script\b[\s\S]*?<\/script>/gi, ' ').replace(/<style\b[\s\S]*?<\/style>/gi, ' ').replace(/<[^>]+>/g, ' ')
    .replace(/&[a-z0-9#]+;/gi, ' ').replace(/\s+/g, ' ').trim().toLocaleLowerCase();
  const wordCount = (text.match(/[\p{L}\p{N}]+/gu) || []).length;
  const fingerprint = createHash('sha256').update(text).digest('hex').slice(0, 16);
  const route = basePath(row['current URL']);
  let category = categoryFor(route);
  let recommendation = '';
  const duplicate = fingerprints.get(`${new URL(row['current URL']).pathname.split('/')[1] || 'en'}:${fingerprint}`);
  if (duplicate) {
    category = 'THIN / DUPLICATE / UNCLEAR';
    recommendation = `merge — exact primary-content duplicate of ${duplicate}`;
  } else if (wordCount < 120 && category === 'LEGACY WITH ACTIVE VALUE') {
    category = 'THIN / DUPLICATE / UNCLEAR';
    recommendation = 'improve — legacy route has fewer than 120 visible main-content words';
  }
  fingerprints.set(`${new URL(row['current URL']).pathname.split('/')[1] || 'en'}:${fingerprint}`, row['current URL']);
  row['quality category'] = category;
  row['recommended action'] = recommendation;
  row['visible main-content words'] = wordCount;
  row['content fingerprint'] = fingerprint;
}

const originalHeaders = Object.keys(rows[0]).filter((header) => !['quality category', 'recommended action', 'visible main-content words', 'content fingerprint'].includes(header));
const headers = [...originalHeaders, 'quality category', 'recommended action', 'visible main-content words', 'content fingerprint'];
await writeFile(matrixPath, [headers.join(','), ...rows.map((row) => headers.map((header) => csv(row[header])).join(','))].join('\n') + '\n', 'utf8');
const counts = Object.fromEntries([...new Set(rows.map((row) => row['quality category']))].sort().map((category) => [category, rows.filter((row) => row['quality category'] === category).length]));
process.stdout.write(JSON.stringify({ classified: rows.length, counts, reviewActions: rows.filter((row) => row['quality category'] === 'THIN / DUPLICATE / UNCLEAR').map((row) => ({ url: row['current URL'], action: row['recommended action'] })) }, null, 2) + '\n');
