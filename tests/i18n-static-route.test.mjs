import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

function loadI18n({ documentLang, storedLang }) {
  const listeners = new Map();
  const documentElement = {
    getAttribute(name) {
      if (name === 'data-cf-static-lang') return documentLang;
      if (name === 'data-i18n-page') return 'index';
      return null;
    },
    setAttribute() {},
    removeAttribute() {},
  };
  const document = {
    cookie: '',
    documentElement,
    readyState: 'loading',
    addEventListener(name, callback) { listeners.set(name, callback); },
    querySelectorAll() { return []; },
    querySelector() { return null; },
    dispatchEvent() {},
  };
  const window = {
    cfLocales: { en: { pages: {} }, ro: { pages: {} }, ru: { pages: {} } },
  };
  const context = {
    window,
    document,
    localStorage: { getItem: () => storedLang, setItem() {} },
    CustomEvent: class {},
    Promise,
    console,
  };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync('assets/js/i18n.js', 'utf8'), context);
  return window.cfI18n;
}

test('fixed English URL stays English even when localStorage previously selected Russian', () => {
  const i18n = loadI18n({ documentLang: 'en', storedLang: 'ru' });
  assert.equal(i18n.current(), 'en');
});

test('fixed Romanian URL uses Romanian independently of stored language', () => {
  const i18n = loadI18n({ documentLang: 'ro', storedLang: 'en' });
  assert.equal(i18n.current(), 'ro');
});

test('runtime mobile navigation injects clean routes with the fixed language prefix', () => {
  const source = fs.readFileSync('assets/js/camelot-gsap.js', 'utf8');
  assert.doesNotMatch(source, /\['for-agencies\.html'/);
  assert.doesNotMatch(source, /\['about\.html'/);
  assert.doesNotMatch(source, /\['index\.html#pricing-cards'/);
  assert.match(source, /const langPrefix = fixedLang === 'en' \? '' : `\/\$\{fixedLang\}`/);
});
