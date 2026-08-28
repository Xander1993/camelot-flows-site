#!/usr/bin/env node

import { readFile, writeFile } from 'node:fs/promises';

const source = process.argv[2] || 'docs/audit/live-baseline.json';
const output = process.argv[3] || 'docs/URL_CONTENT_MATRIX.csv';
const report = JSON.parse(await readFile(source, 'utf8'));
const base = 'https://camelotflows.dev';

const core = new Set([
  '/', '/quote-to-order', '/industries/technical-distributors', '/industries/hvac-refrigeration',
  '/websites', '/case-studies', '/about', '/contact',
]);
const newRoutes = [
  '/quote-to-order', '/industries/technical-distributors', '/industries/hvac-refrigeration', '/websites',
];

function localePath(route, lang) {
  if (lang === 'en') return route;
  return route === '/' ? `/${lang}/` : `/${lang}${route}`;
}

function pageLanguage(pathname) {
  if (pathname === '/ro/' || pathname.startsWith('/ro/')) return 'ro';
  if (pathname === '/ru/' || pathname.startsWith('/ru/')) return 'ru';
  return 'en';
}

function baseRoute(pathname) {
  if (pathname === '/ro/' || pathname === '/ru/') return '/';
  return pathname.replace(/^\/(?:ro|ru)(?=\/)/, '');
}

function topic(pathname, title = '') {
  const route = baseRoute(pathname);
  if (route === '/') return 'AI-assisted sales and operations systems for technical B2B companies';
  if (route === '/quote-to-order') return 'Supervised request-to-quotation workflow automation';
  if (route === '/industries/technical-distributors') return 'Automation for technical equipment distributors and importers';
  if (route === '/industries/hvac-refrigeration') return 'Automation for HVAC and refrigeration sales and service';
  if (route === '/websites') return 'B2B websites, WooCommerce, client portals, and integrations';
  if (route === '/case-studies') return 'Verified client work and fictional workflow demonstrations';
  if (route === '/about') return 'Alexandru Buzi and the solo-specialist operating model';
  if (route === '/contact') return 'Workflow diagnostic and project contact';
  if (route.startsWith('/blog/')) return route.includes('building-dreamscape') ? 'Founder notes and game-development learning' : 'Article: ' + title.replace(/\s*[|\-–—]\s*Camelot Flows.*$/i, '');
  if (route === '/legal' || route === '/privacy') return 'Legal and privacy information';
  if (route === '/arsenal') return 'Supporting tools and technology stack';
  if (route === '/merlin' || route === '/merlin-automation') return 'Legacy AI assistant offer';
  if (route === '/for-agencies') return 'White-label agency support';
  if (route === '/audit') return 'Website audit lead tool';
  if (['/launch-site', '/custom-premium', '/ecommerce-wp', '/service-creation', '/service-maintenance', '/service-marketing', '/work-with-me'].includes(route)) return 'Legacy website service offer';
  if (route === '/service-automation') return 'Supporting automation service';
  return title || route;
}

function decision(pathname) {
  const route = baseRoute(pathname);
  if (core.has(route)) return ['REWRITE IN PLACE', pathname, 'none', 'Core commercial route in the focused EN/RO/RU architecture.'];
  if (route.startsWith('/blog/')) return ['KEEP', pathname, 'none', route.includes('building-dreamscape') ? 'Preserve search signals; classify as Founder Notes and keep secondary.' : 'Preserve the article URL and accumulated search signals.'];
  if (route === '/legal' || route === '/privacy') return ['KEEP', pathname, 'none', 'Required trust and legal route.'];
  return ['KEEP BUT REMOVE FROM PRIMARY NAVIGATION', pathname, 'none', 'Preserve the existing intent and search signals as a secondary or footer route.'];
}

function csv(value) {
  const text = value == null ? '' : String(value);
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

const headers = [
  'current URL', 'HTTP status', 'indexability', 'canonical', 'language', 'title', 'H1', 'main topic',
  'internal links', 'external backlinks if discoverable', 'old equivalent URL', 'proposed action',
  'target URL', 'redirect type', 'reason',
];
const rows = [];

for (const page of report.records) {
  if (page.finalStatus !== 200 || !(page.contentType || '').includes('text/html')) continue;
  const url = new URL(page.url);
  const lang = pageLanguage(url.pathname);
  const [action, target, redirect, reason] = decision(url.pathname);
  const oldEquivalent = lang === 'en' && url.pathname.startsWith('/blog/')
    ? `https://blog.camelotflows.dev/${url.pathname.slice('/blog/'.length)}`
    : '';
  rows.push([
    page.url,
    page.status,
    /noindex/i.test(page.metaRobots || '') ? 'noindex' : 'indexable',
    page.canonical,
    lang,
    page.title,
    (page.h1 || []).join(' | '),
    topic(url.pathname, page.title),
    `incoming ${page.internalLinksIn}; outgoing ${page.internalLinksOut}`,
    'Not discoverable from public crawl; verify with Search Console/backlink export',
    oldEquivalent,
    action,
    `${base}${target}`,
    redirect,
    reason,
  ]);
}

for (const route of newRoutes) {
  for (const lang of ['en', 'ro', 'ru']) {
    const path = localePath(route, lang);
    rows.push([
      `${base}${path}`,
      'planned',
      'planned indexable',
      `${base}${path}`,
      lang,
      'Planned localized metadata',
      'Planned localized H1',
      topic(path),
      'planned links from homepage, related industry/service pages, and footer',
      'Not applicable; new URL',
      '',
      'CREATE',
      `${base}${path}`,
      'none',
      'Required focused commercial route with complete localized content.',
    ]);
  }
}

rows.sort((a, b) => a[0].localeCompare(b[0]));
await writeFile(output, `${[headers, ...rows].map((row) => row.map(csv).join(',')).join('\n')}\n`, 'utf8');
process.stdout.write(`${output}: ${rows.length} URL decisions\n`);

