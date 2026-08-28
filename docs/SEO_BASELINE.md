# Camelot Flows SEO baseline

Baseline captured: 2026-08-28 (Europe/Bucharest)  
Production source reconciled to: `74e010b` (`master`)  
Production host: Cloudflare Pages, project endpoint `camelot-flows-site-git.pages.dev`  
Canonical origin: `https://camelotflows.dev`

This baseline was completed before the repositioning implementation. Machine-readable evidence is in `docs/audit/live-baseline.json` and `docs/audit/live-resources-baseline.json`.

## Current architecture

- Hand-authored static English HTML at the repository root.
- Generated, fixed-language Romanian and Russian HTML under `/ro/` and `/ru/`.
- Cloudflare Pages clean URLs: top-level `.html` files resolve without the extension and without a trailing slash; blog posts use directory URLs with a trailing slash.
- GitHub `master` is the Cloudflare Pages production branch. No server copy or WordPress theme participates in deployment.
- GA4 is consent-gated through `assets/js/cf-consent.js`.
- Contact submissions use the existing Web3Forms integration.
- The old `blog.camelotflows.dev` host remains an external redirect source.

## Crawl totals

| Measure | Current result |
|---|---:|
| Sitemap URLs | 88 |
| Public URLs crawled from the sitemap | 88 |
| 200 responses | 88 |
| Indexable 200 HTML pages | 88 |
| Redirects or errors inside the sitemap | 0 |
| English pages | 30 |
| Romanian pages | 29 |
| Russian pages | 29 |
| Missing canonicals | 0 |
| Non-self-referencing canonicals | 0 |
| Missing descriptions | 0 |
| Missing or multiple H1s | 0 |
| Pages without meaningful raw HTML | 0 |
| Orphaned sitemap pages | 0 |
| First-party resources checked | 89 |
| First-party resource failures | 0 |

## Confirmed problems

### High priority

1. The homepage presents Camelot Flows primarily as a website, WordPress, WooCommerce, SEO, and broad AI-automation provider. It does not give search engines or technical B2B buyers one stable commercial category.
2. Primary navigation exposes many unrelated offers (web builds, arsenal, Merlin, agencies, pricing) instead of a small quote-to-order and industry hierarchy.
3. The current commercial structure lacks dedicated pages for quote-to-order automation, technical distributors, HVAC/refrigeration, and websites as a supporting capability.

### Medium priority

1. `/custom-premium`, `/launch-site`, and `/merlin-automation` reuse their English meta descriptions on Romanian and Russian URLs. Titles and body copy are localized, but the descriptions are duplicated across languages.
2. The old blog host sends known article URLs with a trailing slash through one direct 301 to the matching 200 article, but no-slash article variants take two hops because the apex adds the final slash.
3. Old taxonomy, feed, author, and pagination samples redirect once to equivalent-looking apex paths that return 404. This is truthful, but historical high-value URLs should be checked against Search Console/backlink exports before any 410 decisions.
4. The sitemap gives all localized and most historical pages the same `2026-08-23` modification date. Future sitemap updates should use page-level content dates instead of a blanket build date.

### Low priority

1. The English-only article `/blog/ai-intake-assistant-small-service-business/` correctly has no fabricated translations, but its hreflang set is necessarily limited to English and `x-default`.
2. Legacy pages remain heavily linked from the global navigation, diluting the new topic hierarchy even though none are technically orphaned.

## Host and redirect checks

- `http://camelotflows.dev/*` → one 301 → canonical HTTPS apex.
- `http://www.camelotflows.dev/*` → one 301 → canonical HTTPS apex.
- `https://www.camelotflows.dev/*` → one 301 → canonical HTTPS apex.
- `/about/` → one 308 → `/about`.
- `/about.html` → one 308 → `/about`.
- Eleven known old blog article URLs with trailing slashes → one 301 → matching `/blog/<slug>/` 200 URL.
- Tested no-slash old article URLs → 301 to apex path, then 308 to the canonical trailing-slash article URL.

## Language architecture

The current production repair already avoids the former single-URL language problem:

- English uses root URLs.
- Romanian uses `/ro/` URLs.
- Russian uses `/ru/` URLs.
- Pages have language-matched raw HTML, titles, H1s, canonicals, reciprocal hreflang, and crawlable language links.
- There is no IP- or browser-language redirect.

The repositioning must preserve this implementation and add matching EN/RO/RU URLs only where complete human-readable content is supplied.

## Rendering and resources

- All 88 indexable pages contain meaningful main content in the initial HTML response.
- The hero and H1 are not dependent on analytics, consent, fonts, animation, or language-switch JavaScript.
- The tested first-party resource set produced zero HTTP or HTML-fallback failures.
- Current pages load an established visual and animation stack. The repositioning must preserve that design system and behavior; performance work is limited to safe optimizations that do not alter the interface.

## Evidence limits

- No Search Console export or authenticated backlink index was available in the repository, so external backlink columns in the URL matrix are marked as not publicly discoverable rather than guessed.
- Browser rendering, mobile layouts, Lighthouse, form behavior, and structured data are verified after implementation in the final validation phase.
- No forms were submitted during baseline QA.
