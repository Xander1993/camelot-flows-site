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

test('adaptive nav keeps mobile navigation through 800px and fewer desktop links after it', async () => {
  const scripts = await Promise.all([
    readFile(new URL('../assets/js/camelot-gsap.js', import.meta.url), 'utf8'),
  ]);
  const expected = new Map([
    [800, null],
    [801, 2],
    [859, 2],
    [860, 3],
    [959, 3],
    [960, 4],
    [1099, 4],
    [1100, 5],
    [1379, 5],
    [1380, null],
  ]);

  for (const source of scripts) {
    assert.match(source, /const BREAKPOINT_MIN = 801;/);
    const match = source.match(/const getTier = (\(w\) => \{[\s\S]*?\n\s*\});/);
    assert.ok(match, 'expected the adaptive nav tier function');
    const getTier = vm.runInNewContext(match[1], {
      BREAKPOINT_MIN: 801,
      BREAKPOINT_MAX: 1380,
    });
    for (const [width, tier] of expected) {
      assert.equal(getTier(width), tier, `unexpected visible-link tier at ${width}px`);
    }
  }
});

test('mobile menu toggle stays available through 800px without a fractional dead zone', async () => {
  const [sourceCss, minifiedCss] = await Promise.all([
    readFile(new URL('../assets/css/camelot.css', import.meta.url), 'utf8'),
    readFile(new URL('../assets/css/camelot.min.css', import.meta.url), 'utf8'),
  ]);

  assert.match(sourceCss, /#mobile-menu-toggle\s*\{\s*display:\s*flex;/);
  assert.match(
    sourceCss,
    /@media\s*\(max-width:\s*800px\)[\s\S]*?nav\.fixed\s*>\s*\.glass-panel\s*>\s*div:nth-child\(2\)\s*\{\s*display:\s*none\s*!important;/,
  );
  assert.match(
    sourceCss,
    /@media\s*\(min-width:\s*801px\)[\s\S]*?#mobile-menu-toggle\s*\{\s*display:\s*none;/,
  );
  assert.match(minifiedCss, /#mobile-menu-toggle\{display:flex\}/);
  assert.match(
    minifiedCss,
    /@media\s*\(min-width:801px\)\{#mobile-menu-toggle\{display:none\}/,
  );
});

test('homepage variants bust cached navigation CSS and JS', async () => {
  const pages = await Promise.all([
    readFile(new URL('../index.html', import.meta.url), 'utf8'),
    readFile(new URL('../ro/index.html', import.meta.url), 'utf8'),
    readFile(new URL('../ru/index.html', import.meta.url), 'utf8'),
  ]);

  for (const html of pages) {
    const siteCssVersion = html.match(/site\.min\.css\?v=(\d+)/);
    const camelotCssVersion = html.match(/camelot\.min\.css\?v=(\d+)/);
    const navJsVersion = html.match(/camelot-gsap\.min\.js\?v=(\d+)/);
    assert.ok(siteCssVersion && Number(siteCssVersion[1]) > 1);
    assert.ok(camelotCssVersion && Number(camelotCssVersion[1]) > 19);
    assert.ok(navJsVersion && Number(navJsVersion[1]) > 8);
  }
});
