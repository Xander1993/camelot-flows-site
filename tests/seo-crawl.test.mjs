import { after, before, test } from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';

let server;
let baseUrl;

before(async () => {
  server = http.createServer((req, res) => {
    if (req.url === '/sitemap.xml') {
      res.writeHead(200, { 'content-type': 'application/xml' });
      res.end(`<?xml version="1.0"?><urlset><url><loc>${baseUrl}/</loc></url><url><loc>${baseUrl}/about</loc></url></urlset>`);
      return;
    }
    if (req.url === '/') {
      res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
      res.end(`<!doctype html><html lang="en"><head><title>Home</title><meta name="description" content="Home description"><link rel="canonical" href="${baseUrl}/"></head><body><main><h1>Home heading</h1><p>${'Initial content '.repeat(10)}</p><a href="/about.html">About</a></main></body></html>`);
      return;
    }
    if (req.url === '/about.html') {
      res.writeHead(308, { location: '/about' });
      res.end();
      return;
    }
    if (req.url === '/about') {
      res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
      res.end(`<!doctype html><html lang="en"><head><title>About</title><meta name="description" content="About description"><meta name="robots" content="index,follow"><link rel="canonical" href="${baseUrl}/about"></head><body><div id="content"><h1>About heading</h1><p>${'About content '.repeat(10)}</p></div></body></html>`);
      return;
    }
    res.writeHead(404, { 'content-type': 'text/plain' });
    res.end('missing');
  });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  baseUrl = `http://127.0.0.1:${server.address().port}`;
});

after(async () => {
  await new Promise((resolve) => server.close(resolve));
});

test('crawlSite records raw redirect status, one hop, and final metadata from initial HTML', async () => {
  const { crawlSite } = await import('../tools/seo-crawl.mjs');
  const result = await crawlSite({ baseUrl });

  assert.equal(result.sitemap.status, 200);
  assert.equal(result.sitemap.urlCount, 2);

  const alias = result.records.find((record) => record.url === `${baseUrl}/about.html`);
  assert.equal(alias.status, 308);
  assert.equal(alias.redirectHops, 1);
  assert.equal(alias.redirectDestination, `${baseUrl}/about`);
  assert.equal(alias.finalStatus, 200);
  assert.equal(alias.finalUrl, `${baseUrl}/about`);
  assert.equal(alias.canonical, `${baseUrl}/about`);
  assert.deepEqual(alias.h1, ['About heading']);
  assert.equal(alias.language, 'en');
  assert.equal(alias.mainContentInInitialHtml, true);
});

test('crawlSite marks sitemap membership and counts raw internal links', async () => {
  const { crawlSite } = await import('../tools/seo-crawl.mjs');
  const result = await crawlSite({ baseUrl });

  const home = result.records.find((record) => record.url === `${baseUrl}/`);
  const canonicalAbout = result.records.find((record) => record.url === `${baseUrl}/about`);
  const alias = result.records.find((record) => record.url === `${baseUrl}/about.html`);

  assert.equal(home.inSitemap, true);
  assert.equal(canonicalAbout.inSitemap, true);
  assert.equal(alias.inSitemap, false);
  assert.equal(alias.internalLinksIn, 1);
  assert.deepEqual(home.internalHtmlAliasLinks, ['/about.html']);
});
