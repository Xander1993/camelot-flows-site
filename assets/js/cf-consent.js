/* Camelot Flows — cookie consent banner + GA4 Consent Mode v2 updates.
   Default consent state (denied) is set inline in each page's head BEFORE gtag config.
   This script only renders the banner and records the visitor's choice. */
(function () {
  'use strict';

  var KEY = 'cf_consent';
  var stored = null;
  try { stored = localStorage.getItem(KEY); } catch (e) { /* storage blocked: show banner every visit */ }
  if (stored === 'granted' || stored === 'denied') return; // choice already made

  var lang = 'en';
  try { lang = document.documentElement.getAttribute('data-cf-lang') || localStorage.getItem('cf_lang') || 'en'; } catch (e) {}
  if (['en', 'ro', 'ru'].indexOf(lang) === -1) lang = 'en';

  var T = {
    en: {
      text: 'I use one analytics cookie (Google Analytics) to see which pages help visitors. No ads, no tracking across sites.',
      more: 'Privacy policy',
      accept: 'Accept',
      decline: 'Decline'
    },
    ro: {
      text: 'Folosesc un singur cookie de analiză (Google Analytics) ca să văd ce pagini îi ajută pe vizitatori. Fără reclame, fără urmărire pe alte site-uri.',
      more: 'Politica de confidențialitate',
      accept: 'Accept',
      decline: 'Refuz'
    },
    ru: {
      text: 'Я использую один аналитический cookie (Google Analytics), чтобы видеть, какие страницы полезны посетителям. Без рекламы и без слежки на других сайтах.',
      more: 'Политика конфиденциальности',
      accept: 'Принять',
      decline: 'Отклонить'
    }
  }[lang];

  function decide(granted) {
    try { localStorage.setItem(KEY, granted ? 'granted' : 'denied'); } catch (e) {}
    if (granted && typeof window.gtag === 'function') {
      window.gtag('consent', 'update', { analytics_storage: 'granted' });
    }
    var el = document.getElementById('cf-consent');
    if (el) {
      el.style.transition = 'opacity .25s ease, transform .25s ease';
      el.style.opacity = '0';
      el.style.transform = 'translateY(12px)';
      setTimeout(function () { el.remove(); }, 260);
    }
  }

  function render() {
    if (document.getElementById('cf-consent')) return;
    var css = document.createElement('style');
    css.textContent =
      '#cf-consent{position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;max-width:640px;margin:0 auto;' +
      'padding:16px 20px;border-radius:14px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;' +
      'font-family:Inter,system-ui,sans-serif;font-size:13px;line-height:1.5;' +
      'background:rgba(245,244,240,.96);color:#2d2a26;border:1px solid rgba(45,42,38,.14);' +
      'box-shadow:0 12px 40px rgba(0,0,0,.18);backdrop-filter:blur(12px)}' +
      '[data-theme="night"] #cf-consent{background:rgba(13,15,24,.92);color:#e2e4ef;border-color:rgba(99,102,241,.35);' +
      'box-shadow:0 12px 40px rgba(0,0,0,.55),0 0 24px rgba(99,102,241,.12)}' +
      '#cf-consent p{margin:0;flex:1 1 260px}' +
      '#cf-consent a{text-decoration:underline;color:inherit;opacity:.85}' +
      '#cf-consent .cf-consent-actions{display:flex;gap:8px;flex:0 0 auto}' +
      '#cf-consent button{cursor:pointer;border-radius:9px;padding:9px 18px;font-size:13px;font-weight:600;' +
      'font-family:inherit;border:1px solid transparent;transition:opacity .15s ease}' +
      '#cf-consent button:hover{opacity:.85}' +
      '#cf-consent .cf-accept{background:#c96f4a;color:#fff}' +
      '[data-theme="night"] #cf-consent .cf-accept{background:#6366f1}' +
      '#cf-consent .cf-decline{background:transparent;color:inherit;border-color:rgba(45,42,38,.25)}' +
      '[data-theme="night"] #cf-consent .cf-decline{border-color:rgba(226,228,239,.25)}' +
      '@media (max-width:480px){#cf-consent{flex-direction:column;align-items:stretch;text-align:center}' +
      '#cf-consent .cf-consent-actions{justify-content:center}}';
    document.head.appendChild(css);

    var box = document.createElement('div');
    box.id = 'cf-consent';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-live', 'polite');
    box.setAttribute('aria-label', 'Cookie consent');
    box.innerHTML =
      '<p>' + T.text + ' <a href="/privacy">' + T.more + '</a></p>' +
      '<div class="cf-consent-actions">' +
      '<button type="button" class="cf-decline">' + T.decline + '</button>' +
      '<button type="button" class="cf-accept">' + T.accept + '</button>' +
      '</div>';
    document.body.appendChild(box);
    box.querySelector('.cf-accept').addEventListener('click', function () { decide(true); });
    box.querySelector('.cf-decline').addEventListener('click', function () { decide(false); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', render);
  } else {
    render();
  }
})();
