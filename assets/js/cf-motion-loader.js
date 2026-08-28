/* Load decorative motion only after meaningful content is available. */
(function () {
  'use strict';
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var started = false;
  var sources = [
    '/assets/js/gsap.min.js',
    '/assets/js/ScrollTrigger.min.js',
    '/assets/js/TextPlugin.min.js',
    '/assets/js/lenis.min.js',
    '/assets/js/camelot-gsap.min.js?v=10'
  ];

  function loadNext(index) {
    if (index >= sources.length) return;
    var script = document.createElement('script');
    script.src = sources[index];
    script.defer = true;
    script.onload = function () { loadNext(index + 1); };
    document.head.appendChild(script);
  }

  function start() {
    if (started) return;
    started = true;
    loadNext(0);
  }

  ['pointerdown', 'keydown', 'touchstart', 'scroll'].forEach(function (type) {
    window.addEventListener(type, start, { once: true, passive: true });
  });
  window.setTimeout(start, window.innerWidth < 768 ? 10000 : 6000);
})();
