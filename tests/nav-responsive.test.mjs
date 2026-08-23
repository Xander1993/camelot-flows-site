import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import vm from 'node:vm';

test('desktop nav CTA respects the Tailwind lg visibility breakpoint', async () => {
  const [html, sourceCss, minifiedCss] = await Promise.all([
    readFile(new URL('../index.html', import.meta.url), 'utf8'),
    readFile(new URL('../assets/site.css', import.meta.url), 'utf8'),
    readFile(new URL('../assets/site.min.css', import.meta.url), 'utf8'),
  ]);

  const cta = html.match(/class="([^"]*\bnav-cta\b[^"]*)"/);
  assert.ok(cta, 'expected the desktop nav CTA in index.html');
  assert.match(cta[1], /\bhidden\b/);
  assert.match(cta[1], /\blg:inline-flex\b/);

  for (const [name, css] of [
    ['source CSS', sourceCss],
    ['minified production CSS', minifiedCss],
  ]) {
    const globalRule = css.match(/(?:^|})\.nav-cta\s*\{([^}]*)\}/m);
    assert.ok(globalRule, `expected the shared .nav-cta styling rule in ${name}`);
    assert.doesNotMatch(
      globalRule[1],
      /\bdisplay\s*:/,
      `${name} must not override hidden below 1024px and make the nav overflow`,
    );
  }
});

test('adaptive nav keeps fewer links at the narrow notebook breakpoints', async () => {
  const scripts = await Promise.all([
    readFile(new URL('../assets/js/camelot-gsap.js', import.meta.url), 'utf8'),
  ]);
  const expected = new Map([
    [767, null],
    [768, 2],
    [839, 2],
    [840, 3],
    [919, 3],
    [920, 4],
    [1099, 4],
    [1100, 5],
    [1379, 5],
    [1380, null],
  ]);

  for (const source of scripts) {
    const match = source.match(/const getTier = (\(w\) => \{[\s\S]*?\n\s*\});/);
    assert.ok(match, 'expected the adaptive nav tier function');
    const getTier = vm.runInNewContext(match[1], {
      BREAKPOINT_MIN: 768,
      BREAKPOINT_MAX: 1380,
    });
    for (const [width, tier] of expected) {
      assert.equal(getTier(width), tier, `unexpected visible-link tier at ${width}px`);
    }
  }
});

test('mobile menu toggle has no fractional dead zone below the md breakpoint', async () => {
  const [sourceCss, minifiedCss] = await Promise.all([
    readFile(new URL('../assets/css/camelot.css', import.meta.url), 'utf8'),
    readFile(new URL('../assets/css/camelot.min.css', import.meta.url), 'utf8'),
  ]);

  assert.match(sourceCss, /#mobile-menu-toggle\s*\{\s*display:\s*flex;/);
  assert.match(
    sourceCss,
    /@media\s*\(min-width:\s*768px\)[\s\S]*?#mobile-menu-toggle\s*\{\s*display:\s*none;/,
  );
  assert.match(minifiedCss, /#mobile-menu-toggle\{display:flex\}/);
  assert.match(
    minifiedCss,
    /@media\s*\(min-width:768px\)\{#mobile-menu-toggle\{display:none\}/,
  );
});
