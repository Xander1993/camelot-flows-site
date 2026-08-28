/* Essential, dependency-free UI for the static multilingual routes. */
(function () {
  'use strict';

  function init() {
    document.documentElement.removeAttribute('data-i18n-loading');

    document.querySelectorAll('[data-cf-theme-toggle], #theme-toggle').forEach(function (button) {
      button.addEventListener('click', function () {
        var current = document.documentElement.getAttribute('data-theme') || 'cozy';
        var next = current === 'night' ? 'cozy' : 'night';
        document.documentElement.setAttribute('data-theme', next);
        try { localStorage.setItem('cf_theme', next); } catch (_) {}
        document.cookie = 'cf_theme=' + next + '; path=/; domain=.camelotflows.dev; max-age=31536000; SameSite=Lax';
      });
    });

    document.querySelectorAll('[data-cf-lang-switcher]').forEach(function (switcher) {
      var trigger = switcher.querySelector('[data-cf-lang-trigger]');
      var menu = switcher.querySelector('[role="listbox"]');
      if (!trigger || !menu) return;
      var language = document.documentElement.lang || 'en';
      var current = switcher.querySelector('[data-cf-lang-current]');
      if (current) current.textContent = language.toUpperCase();
      menu.querySelectorAll('[data-lang]').forEach(function (option) {
        option.setAttribute('aria-selected', String(option.getAttribute('data-lang') === language));
      });
      var close = function () {
        switcher.classList.remove('is-open');
        trigger.setAttribute('aria-expanded', 'false');
      };
      trigger.addEventListener('click', function () {
        var open = !switcher.classList.contains('is-open');
        switcher.classList.toggle('is-open', open);
        trigger.setAttribute('aria-expanded', String(open));
      });
      document.addEventListener('click', function (event) {
        if (!switcher.contains(event.target)) close();
      });
      switcher.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') { close(); trigger.focus(); }
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
