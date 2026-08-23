import assert from 'node:assert/strict';
import test from 'node:test';
import { auditResources, extractFirstPartyResources } from '../tools/seo-resource-audit.mjs';

test('extractFirstPartyResources resolves srcsets and excludes third-party assets', () => {
  const html = '<link rel="stylesheet" href="/site.css"><link rel="prefetch" as="document" href="/about"><img src="image.webp" srcset="small.webp 480w, /large.webp 900w"><script src="https://cdn.example/app.js"></script>';
  assert.deepEqual(extractFirstPartyResources(html, 'https://site.test/about', 'https://site.test').sort(), [
    'https://site.test/image.webp',
    'https://site.test/large.webp',
    'https://site.test/site.css',
    'https://site.test/small.webp',
  ]);
});

test('auditResources flags Cloudflare-style HTML fallbacks for missing assets', async () => {
  const responses = new Map([
    ['https://site.test/sitemap.xml', new Response('<urlset><url><loc>https://site.test/</loc></url></urlset>', { headers: { 'content-type': 'application/xml' } })],
    ['https://site.test/', new Response('<main><img src="/missing.webp"></main>', { headers: { 'content-type': 'text/html' } })],
    ['https://site.test/missing.webp', new Response('<html>fallback</html>', { headers: { 'content-type': 'text/html' } })],
  ]);
  const fetchImpl = async (input) => {
    const response = responses.get(String(input));
    Object.defineProperty(response, 'url', { value: String(input) });
    return response.clone();
  };
  const result = await auditResources({ baseUrl: 'https://site.test', fetchImpl });
  assert.equal(result.resourceFailures.length, 1);
  assert.equal(result.resourceFailures[0].htmlFallback, true);
});
