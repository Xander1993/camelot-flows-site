const fs = require('fs');
global.window = {};
require('./assets/js/locales.js');
const en = window.cfLocales.en.pages['service-marketing'];
let html = fs.readFileSync('service-marketing.html', 'utf8');
const changed = [];
for (const [k, v] of Object.entries(en)) {
  if (typeof v !== 'string') continue;
  if (!/^s_(del|proc|out|cta)/.test(k)) continue;   // body sections only
  if (v.startsWith('html:')) continue;              // skip rich-markup values
  const esc = k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const re = new RegExp('(data-i18n="pages\\.service-marketing\\.' + esc + '">)([^<]*)(</)');
  html = html.replace(re, (m, p1, old, p3) => {
    if (old.trim() !== v.trim()) changed.push(k);
    return p1 + v + p3;
  });
}
fs.writeFileSync('service-marketing.html', html);
console.log('synced fallbacks:', [...new Set(changed)].join(', ') || '(none)');
