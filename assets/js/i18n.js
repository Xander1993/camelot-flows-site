// ============================================================
// CAMELOT FLOWS — i18n LOADER
// ------------------------------------------------------------
// Reads dictionaries from window.cfLocales (loaded by locales.js
// as a blocking <script> before this file on every page, so it
// works on file:// AND http://). window.cfLocales is the SOLE
// source of truth. If it is absent, translation degrades to each
// element's built-in English text (no JSON fetch fallback).
//
// Public API on window.cfI18n:
//   .current()  -> 'en' | 'ro' | 'ru'
//   .set(lang)  -> Promise<void>     swap dict, walk DOM, persist
//   .t(key)     -> string            JS-side string lookup
//   .ready      -> Promise<void>     resolves once initial dict applied
// Dispatches on document:
//   new CustomEvent('cf:langchange', { detail: { lang, prev } })
// ============================================================
(function () {
    var SUPPORTED = ['en', 'ro', 'ru'];
    var DEFAULT_LANG = 'en';
    var STORAGE_KEY = 'cf_lang';
    var COOKIE_DOMAIN = '.camelotflows.dev';
    var dicts = {};   // local cache: { en: {...}, ro: {...} }
    var current = readStoredLang();
    var readyResolve;
    var readyPromise = new Promise(function (r) { readyResolve = r; });

    function readStoredLang() {
        try {
            var c = document.cookie.match('(?:^|;) ?cf_lang=([^;]*)');
            var v = c ? c[1] : localStorage.getItem(STORAGE_KEY);
            if (v && SUPPORTED.indexOf(v) !== -1) return v;
        } catch (_) { }
        return DEFAULT_LANG;
    }

    function writeStoredLang(lang) {
        try { localStorage.setItem(STORAGE_KEY, lang); } catch (_) { }
        try {
            document.cookie = 'cf_lang=' + lang + '; path=/; domain=' + COOKIE_DOMAIN + '; max-age=31536000; SameSite=Lax';
        } catch (_) { }
    }

    // Dotted-path lookup. Returns string if found AND non-empty, else undefined.
    function lookup(dict, key) {
        if (!dict || !key) return undefined;
        var parts = key.split('.');
        var node = dict;
        for (var i = 0; i < parts.length; i++) {
            if (node && typeof node === 'object' && parts[i] in node) {
                node = node[parts[i]];
            } else {
                return undefined;
            }
        }
        if (typeof node === 'string' && node.length > 0) return node;
        return undefined;
    }

    // Per-key fallback: lang dict first, then EN dict.
    function translate(lang, key) {
        var v = lookup(dicts[lang], key);
        if (v !== undefined) return v;
        if (lang !== DEFAULT_LANG) {
            var fb = lookup(dicts[DEFAULT_LANG], key);
            if (fb !== undefined) return fb;
        }
        return undefined;
    }

    // Source of truth: window.cfLocales (set by assets/js/locales.js, loaded as a
    // blocking <script> before this file on every page). Resolves synchronously.
    // If the global is somehow absent we degrade to an empty dict so applyDom
    // leaves each element's built-in English text in place — no network fallback,
    // no risk of serving a stale partial dictionary.
    function loadDict(lang) {
        if (dicts[lang]) return Promise.resolve(dicts[lang]);

        if (window.cfLocales && window.cfLocales[lang]) {
            dicts[lang] = window.cfLocales[lang];
            return Promise.resolve(dicts[lang]);
        }

        console.warn('[cfI18n] window.cfLocales["' + lang + '"] missing — did locales.js load before i18n.js? Falling back to built-in text.');
        dicts[lang] = {};
        return Promise.resolve(dicts[lang]);
    }

    // Dictionary values may opt into raw HTML via the "html:" prefix.
    function setNodeText(node, value) {
        if (typeof value !== 'string') return;
        if (value.indexOf('html:') === 0) {
            node.innerHTML = value.slice(5);
        } else {
            node.textContent = value;
        }
    }

    function applyDom(lang) {
        var textNodes = document.querySelectorAll('[data-i18n]');
        for (var i = 0; i < textNodes.length; i++) {
            var n = textNodes[i];
            var key = n.getAttribute('data-i18n');
            var v = translate(lang, key);
            if (v !== undefined) setNodeText(n, v);
        }

        var attrNodes = document.querySelectorAll('[data-i18n-attr]');
        for (var j = 0; j < attrNodes.length; j++) {
            var an = attrNodes[j];
            var spec = an.getAttribute('data-i18n-attr') || '';
            var pairs = spec.split(';');
            for (var k = 0; k < pairs.length; k++) {
                var pair = pairs[k].trim();
                if (!pair) continue;
                var idx = pair.indexOf(':');
                if (idx <= 0) continue;
                var attrName = pair.slice(0, idx).trim();
                var attrKey = pair.slice(idx + 1).trim();
                var attrVal = translate(lang, attrKey);
                if (attrVal !== undefined) an.setAttribute(attrName, attrVal);
            }
        }

        var pageSlug = document.documentElement.getAttribute('data-i18n-page');
        if (pageSlug) {
            // SEO: meta tags must remain as static HTML only
            var titleVal = translate(lang, 'pages.' + pageSlug + '.meta_title');
            // if (titleVal !== undefined) document.title = titleVal;

            var descVal = translate(lang, 'pages.' + pageSlug + '.meta_description');
            // if (descVal !== undefined) {
            //     ['meta[name="description"]', 'meta[property="og:description"]', 'meta[name="twitter:description"]']
            //         .forEach(function (sel) {
            //             var m = document.querySelector(sel);
            //             if (m) m.setAttribute('content', descVal);
            //         });
            // }
            // if (titleVal !== undefined) {
            //     ['meta[property="og:title"]', 'meta[name="twitter:title"]']
            //         .forEach(function (sel) {
            //             var m = document.querySelector(sel);
            //             if (m) m.setAttribute('content', titleVal);
            //         });
            // }
        }

        document.querySelectorAll('[data-lang-content]').forEach(function (el) {
            el.hidden = el.dataset.langContent !== lang;
        });

        document.documentElement.setAttribute('lang', lang);
        document.documentElement.setAttribute('data-cf-lang', lang);
        document.documentElement.removeAttribute('data-i18n-loading');

        var labelNode = document.querySelector('[data-cf-lang-current]');
        if (labelNode) labelNode.textContent = lang.toUpperCase();
    }

    function applyAndDispatch(lang, prev) {
        applyDom(lang);
        document.dispatchEvent(new CustomEvent('cf:langchange', {
            detail: { lang: lang, prev: prev }
        }));
    }

    function set(lang) {
        if (SUPPORTED.indexOf(lang) === -1) lang = DEFAULT_LANG;
        var prev = current;
        var loads = [loadDict(lang)];
        if (lang !== DEFAULT_LANG) loads.push(loadDict(DEFAULT_LANG));
        return Promise.all(loads).then(function () {
            current = lang;
            writeStoredLang(lang);
            if (document.startViewTransition && prev !== lang) {
                document.startViewTransition(function () { applyAndDispatch(lang, prev); });
            } else {
                applyAndDispatch(lang, prev);
            }
        });
    }

    window.cfI18n = {
        current: function () { return current; },
        set: set,
        t: function (key) {
            var v = translate(current, key);
            return v !== undefined ? v : key;
        },
        ready: readyPromise
    };

    function init() {
        var loads = [loadDict(current)];
        if (current !== DEFAULT_LANG) loads.push(loadDict(DEFAULT_LANG));
        Promise.all(loads).then(function () {
            applyDom(current);
            readyResolve();
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
