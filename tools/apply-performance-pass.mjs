import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';

const root = path.resolve(import.meta.dirname, '..');
const sitemap = await readFile(path.join(root, 'sitemap.xml'), 'utf8');
const urls = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((match) => match[1]);

function routeFile(rawUrl) {
  const pathname = new URL(rawUrl).pathname;
  if (pathname === '/') return 'index.html';
  const clean = pathname.replace(/^\//, '').replace(/\/$/, '');
  if (pathname.endsWith('/')) return path.join(clean, 'index.html');
  return `${clean}.html`;
}

const files = [...new Set(urls.map(routeFile))];
const icons = new Set();
for (const file of files) {
  const html = await readFile(path.join(root, file), 'utf8');
  for (const match of html.matchAll(/<span[^>]*class="[^"]*material-symbols-outlined[^"]*"[^>]*>([^<]+)<\/span>/g)) {
    const name = match[1].trim();
    if (/^[a-z0-9_]+$/.test(name)) icons.add(name);
  }
}

const iconNames = [...icons].sort().join(',');
const iconCss = `https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined&icon_names=${iconNames}&display=block`
  .replaceAll('&', '&amp;');
const textFontCss = 'https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;0,700;1,300;1,400&amp;family=Inter:wght@300;400;500&amp;family=Space+Grotesk:wght@500;700&amp;family=JetBrains+Mono:wght@400;700&amp;display=optional';
const fontLinks = `<link as="style" href="${textFontCss}" rel="preload">\n<link href="${textFontCss}" media="print" onload="this.media='all'" rel="stylesheet">\n<noscript><link href="${textFontCss}" rel="stylesheet"></noscript>\n<link href="${iconCss}" media="print" onload="this.media='all'" rel="stylesheet">\n<noscript><link href="${iconCss}" rel="stylesheet"></noscript>`;
const perfCritical = '<style id="cf-performance-critical">.material-symbols-outlined{display:inline-block;width:1em;min-width:1em;height:1em;overflow:hidden;white-space:nowrap;word-wrap:normal;letter-spacing:normal;line-height:1;vertical-align:middle}#hero-badge,#hero-word-1,#hero-word-2,#hero-p,#hero-btns,#hero-stats,.hero-word,.hero-price,.hero-cta{opacity:1!important;visibility:visible!important;transform:none!important}</style>';

for (const file of files) {
  const absolute = path.join(root, file);
  let html = await readFile(absolute, 'utf8');

  html = html.replace(/\s*<link[^>]+(?:cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net)[^>]+rel="(?:preconnect|preload)"[^>]*>/g, '');
  html = html.replace(/\s*<link as="document"[^>]+rel="prefetch">/g, '');
  html = html.replace(/<noscript>\s*<link[^>]+href="[^"]*(?:assets\/site(?:\.min)?\.css|assets\/css\/(?:tailwind\.built|camelot(?:\.min)?|theme-night(?:\.min)?|lang-switcher)\.css)[^"]*"[^>]*>\s*<\/noscript>/gi, '');
  html = html.replace(/\s*<link[^>]+href="[^"]*(?:assets\/site(?:\.min)?\.css|assets\/css\/(?:tailwind\.built|camelot(?:\.min)?|theme-night(?:\.min)?|lang-switcher)\.css)[^"]*"[^>]*>/gi, '');
  html = html.replace(/\s*<link[^>]+href="\/assets\/css\/site\.bundle\.min\.css\?v=\d+"[^>]*>/gi, '');
  html = html.replace(/<noscript>\s*<link[^>]+href="https:\/\/fonts\.googleapis\.com\/css2\?[^>]+>\s*<\/noscript>/gi, '');
  html = html.replace(/\s*<link(?=[^>]+href="https:\/\/fonts\.googleapis\.com\/css2\?)[^>]+>/gi, '');
  html = html.replace(/\s*<script async="" src="https:\/\/www\.googletagmanager\.com\/gtag\/js\?id=G-T4ZPEG1KSR"><\/script>\s*<script>[\s\S]*?gtag\('config', 'G-T4ZPEG1KSR'\);\s*<\/script>/g, '');
  html = html.replace(/\s*if \(l !== 'en'\) html\.setAttribute\('data-i18n-loading', '1'\);/g, '');
  html = html.replace(/\s*try \{\s*if \(sessionStorage\.getItem\('cf_loaded'\) === '1'\) \{\s*html\.classList\.add\('cf-skip-preloader'\);\s*\}\s*\} catch \(e\) \{\}/g, '');
  html = html.replace(/\s*<script defer="" src="https:\/\/cdnjs\.cloudflare\.com\/ajax\/libs\/gsap\/3\.12\.5\/(?:gsap|ScrollTrigger|TextPlugin)\.min\.js"><\/script>/g, '');
  html = html.replace(/\s*<script defer="" src="https:\/\/cdn\.jsdelivr\.net\/npm\/@studio-freight\/lenis@1\.0\.42\/dist\/lenis\.min\.js"><\/script>/g, '');
  html = html.replace(/\s*<script[^>]+src="https:\/\/(?:cdnjs\.cloudflare\.com\/ajax\/libs\/gsap|cdn\.jsdelivr\.net\/npm\/@studio-freight\/lenis)[^"]*"[^>]*><\/script>/gi, '');
  html = html.replace(/\s*<script[^>]+src="[^"]*(?:assets\/js\/(?:camelot-gsap|locales|i18n|cf-runtime|cf-motion-loader)(?:\.min)?\.js|assets\/site(?:\.min)?\.js)[^"]*"[^>]*><\/script>/gi, '');
  html = html.replace(/<div[^>]*id="preloader"[^>]*>[\s\S]*?(?=<div class="grain-overlay")/i, '');

  if (html.includes('id="cf-performance-critical"')) html = html.replace(/<style id="cf-performance-critical">[\s\S]*?<\/style>/, perfCritical);
  else html = html.replace('</head>', `${perfCritical}\n</head>`);
  html = html.replace('</head>', `${fontLinks}\n<link href="/assets/css/site.bundle.min.css?v=1" rel="stylesheet">\n</head>`);
  html = html.replace('</body>', '<script defer="" src="/assets/js/cf-runtime.min.js?v=1"></script>\n<script defer="" src="/assets/site.min.js?v=1"></script>\n<script defer="" src="/assets/js/cf-motion-loader.min.js?v=1"></script>\n</body>');
  html = html.replace(/src="\/assets\/images\/cf-mark\.png\?v=3"/g, 'decoding="async" height="56" loading="lazy" src="/assets/images/cf-mark-112.webp?v=1" width="39"');

  if (file.endsWith('contact.html')) {
    const lang = /^ro[\\/]/.test(file) ? 'ro' : /^ru[\\/]/.test(file) ? 'ru' : 'en';
    const unavailable = {
      en: 'File upload unavailable pending privacy review',
      ro: 'Încărcarea fișierelor este indisponibilă până la evaluarea de confidențialitate',
      ru: 'Загрузка файлов недоступна до завершения проверки конфиденциальности'
    }[lang];
    html = html.replace(/(<label[^>]+for="c-file"[^>]*>)[\s\S]*?(<\/label>)/, `$1${unavailable}$2`);
    html = html.replace(/<input[^>]+id="c-file"[^>]*>/, '<input aria-disabled="true" disabled="" id="c-file" type="file">');
  }

  await writeFile(absolute, html, 'utf8');
}

await sharp(path.join(root, 'assets/images/cf-mark.png'))
  .resize({ width: 112, withoutEnlargement: true })
  .webp({ quality: 90, alphaQuality: 100 })
  .toFile(path.join(root, 'assets/images/cf-mark-112.webp'));

process.stdout.write(JSON.stringify({ sitemapUrls: urls.length, files: files.length, iconCount: icons.size, iconNames }, null, 2) + '\n');
