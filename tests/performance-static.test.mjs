import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
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

test('all indexable routes keep content visible and defer non-critical code', async () => {
  assert.equal(urls.length, 100);
  for (const url of urls) {
    const html = await readFile(path.join(root, routeFile(url)), 'utf8');
    const language = new URL(url).pathname.startsWith('/ro/') ? 'RO' : new URL(url).pathname.startsWith('/ru/') ? 'RU' : 'EN';
    assert.match(html, /<h1\b/i, `${url}: static H1`);
    assert.match(html, /site\.bundle\.min\.css\?v=1/, `${url}: stable CSS bundle`);
    assert.match(html, /cf-runtime\.min\.js\?v=1/, `${url}: essential runtime`);
    assert.match(html, /cf-motion-loader\.min\.js\?v=1/, `${url}: deferred motion loader`);
    assert.doesNotMatch(html, /id="preloader"|locales\.min\.js|googletagmanager\.com\/gtag\/js|cdnjs\.cloudflare\.com\/ajax\/libs\/gsap/, `${url}: no blocking loader or non-critical chain`);
    assert.doesNotMatch(html, /data-lang-content\s*=/, `${url}: no embedded alternate full-page language`);
    assert.match(html, new RegExp(`<span class="lang-current" data-cf-lang-current="">${language}<\\/span>`), `${url}: current language label`);
  }
});

test('mobile consent copy does not inherit a 260px vertical flex basis', async () => {
  const source = await readFile(path.join(root, 'assets/js/cf-consent.js'), 'utf8');
  assert.match(source, /#cf-consent p\{flex:0 1 auto\}/);
});

test('preview contact forms disable file upload pending privacy review', async () => {
  for (const file of ['contact.html', 'ro/contact.html', 'ru/contact.html']) {
    const html = await readFile(path.join(root, file), 'utf8');
    assert.match(html, /<input aria-disabled="true" disabled="" id="c-file" type="file">/);
    assert.match(html, /confidential|confidențial|конфиденциальн/i);
  }
});
