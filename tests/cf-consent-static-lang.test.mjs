import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import vm from 'node:vm';

test('cookie banner follows the fixed route language and links to localized privacy', async () => {
  const source = await readFile(new URL('../assets/js/cf-consent.js', import.meta.url), 'utf8');
  let banner;
  const makeElement = tag => ({
    tag,
    style: {},
    setAttribute() {},
    addEventListener() {},
    querySelector() { return { addEventListener() {} }; },
  });
  const document = {
    readyState: 'complete',
    documentElement: { getAttribute: name => name === 'data-cf-static-lang' ? 'ro' : null },
    getElementById: () => null,
    createElement: makeElement,
    head: { appendChild() {} },
    body: { appendChild(node) { banner = node; } },
  };
  const context = {
    document,
    localStorage: { getItem: key => key === 'cf_lang' ? 'en' : null, setItem() {} },
    setTimeout,
    window: {},
  };
  vm.runInNewContext(source, context);

  assert.match(banner.innerHTML, /Politica de confidențialitate/);
  assert.match(banner.innerHTML, /href="\/ro\/privacy"/);
});
