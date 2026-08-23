# Camelot Flows Technical SEO Repair

Production: `https://camelotflows.dev`

Completed: 2026-08-23

Rollback baseline: `534bffde6a6b009d6b9986f1d222ad1cc24cc88b`

Production commit: `f93ee839c1ce385521907637261ffac3f839423e`

## 1. Audit summary

The production site now exposes 88 indexable canonical URLs: 30 English, 29 Romanian, and 29 Russian. A 156-URL verification crawl covered every canonical, all 57 `.html` aliases, and all 11 legacy `blog.camelotflows.dev` aliases.

| Gate | Before | After |
|---|---:|---:|
| Sitemap canonical URLs | 30 | 88 |
| Canonical languages | EN only | EN, RO, RU |
| Canonical pages returning direct 200 | 30 | 88 |
| Internal pages containing `.html` aliases | 60 crawled records | 0 canonical pages |
| Explicit aliases verified in one hop | 30 discovered | 68/68 seeded |
| Redirect chains over one hop | 0 | 0 |
| Unexpected final 404/5xx | 0 | 0 |
| Missing canonical / description / H1 / initial main copy | 0 | 0 |
| First-party live resource failures | Not exhaustively measured | 0 across 89 resources |

The intentional unknown-route check returns `404` with `Page not found | Camelot Flows`. The Ambienti preview returns `200` but carries `noindex,follow,noarchive` and is absent from the sitemap.

## 2. Root causes

1. Language selection was a client-side state change, so crawlers had only English URLs and no indexable RO/RU documents.
2. Hand-authored pages and translated blog fragments retained `.html` aliases, producing unnecessary platform redirects.
3. A mobile-only runtime navigation helper injected three relative `.html` links after page load.
4. Canonicals and hreflang covered English only; the sitemap therefore represented only 30 URLs.
5. Several service/homepage blocks contained unsupported metric-style claims and one unverified testimonial.
6. Deployment topology was easy to confuse: the apex is Cloudflare Pages, while `www` and the old blog host use the DigitalOcean Apache/WordPress host.

## 3. Redirect and 404 map

| Source family | Count | Response | Destination | Result |
|---|---:|---|---|---|
| `/{route}.html` | 19 | 308 | Matching clean English route | 19/19 one hop to 200 |
| `/ro/{route}.html` | 19 | 308 | Matching clean Romanian route | 19/19 one hop to 200 |
| `/ru/{route}.html` | 19 | 308 | Matching clean Russian route | 19/19 one hop to 200 |
| `blog.camelotflows.dev` index + articles | 11 | 301 | Matching apex blog route | 11/11 one hop to 200 |
| Unknown route | 1 probe | 404 | Custom 404 document | Correct status and title |

No redirect exceeded one hop. The complete hop-by-hop evidence is in `after-crawl.json`. Apache configuration was inspected and backed up, but not changed because the existing old-blog redirects were already correct.

## 4. Canonical sitemap list

All route families below have EN, RO, and RU canonicals unless noted. Each localized document is server-rendered/static HTML with a self-canonical and reciprocal `en`, `ro`, `ru`, and `x-default` alternates.

- `/`
- `/about`
- `/arsenal`
- `/audit`
- `/case-studies`
- `/contact`
- `/custom-premium`
- `/ecommerce-wp`
- `/for-agencies`
- `/launch-site`
- `/legal`
- `/merlin-automation`
- `/merlin`
- `/privacy`
- `/service-automation`
- `/service-creation`
- `/service-maintenance`
- `/service-marketing`
- `/work-with-me`
- `/blog/`
- `/blog/ai-intake-assistant-small-service-business/` - English only; no fabricated translation
- `/blog/automate-import-back-office-before-hiring/`
- `/blog/building-dreamscape-in-parallel/`
- `/blog/do-i-own-my-website-checklist/`
- `/blog/how-chatgpt-decides-which-local-businesses-to-recommend/`
- `/blog/how-i-build-sites-for-clients/`
- `/blog/how-i-build-websites-for-e390-the-starter-page-breakdown/`
- `/blog/how-to-leave-your-web-agency-without-losing-your-website/`
- `/blog/why-is-my-new-website-not-showing-up-on-google/`
- `/blog/why-wordpress-slow-on-mobile/`

The sitemap contains exactly those 30 English URLs plus the 29 valid RO and 29 valid RU equivalents. There are no `.html` URLs, redirects, 404s, duplicate entries, or noindex pages in the sitemap.

## 5. Internationalization implementation

- Generated fixed `/ro/` and `/ru/` route trees from the English sources and existing human-written locale dictionaries/blog translations.
- Replaced client-only language switching with crawlable language anchors.
- Made route language authoritative over stale `localStorage` or cookies.
- Localized internal links, consent-policy links, schema URLs, canonicals, and navigation state.
- Added reciprocal hreflang to 87 route families; the one English-only article correctly advertises only `en` and `x-default`.
- Added deterministic generation coverage: a second generation pass changes zero of 59 generated/sitemap files.

## 6. Metadata and on-page changes

- Homepage title: `Web Development, WooCommerce & AI Automation | Camelot Flows`.
- Homepage copy now states the real offer and service area without invented rankings or conversion metrics.
- WooCommerce page now targets development, redesign, and migration intent in title, H1, description, and body copy.
- Replaced unsupported numeric claims with factual process/verification language across creation, maintenance, Merlin, launch, ecommerce, and arsenal content.
- Removed the unverified Legal Point testimonial.
- Preserved verified service prices and delivery ranges already defined by the business.
- Every canonical has one H1, a title, a meta description, a self-canonical, and meaningful initial HTML content.

## 7. Schema changes

- Kept one stable Organization identity at `https://camelotflows.dev/#organization`.
- Updated homepage Organization description and `knowsAbout` to the actual offer.
- Localized page/article URLs and `inLanguage` while preserving stable Organization and Person IDs.
- Parsed every JSON-LD block successfully; no schema URL contains `.html`.
- No AggregateRating, fake review schema, or unsupported claim schema was added.

## 8. Resource fixes

- Normalized localized asset paths, inline `url(...)`, `srcset`, scripts, styles, icons, and image references to root-safe URLs.
- Rebuilt Tailwind CSS and minified JavaScript.
- Fixed language routing in `i18n.js`, consent UI, the language picker, active navigation, and mobile runtime navigation.
- Live audit: 88 pages, 89 unique first-party resources, zero page failures, zero missing resources, and zero HTML fallbacks masquerading as assets.
- Fresh 390px browser check: zero broken images, zero overflow, zero console errors, and zero rendered `.html` links.

## 9. 3xx, 4xx, and 5xx before/after

| Signal | Before | After |
|---|---:|---:|
| Canonical direct 200s | 30 | 88 |
| Explicit permanent aliases verified | 30 discovered | 68/68 seeded |
| Internal `.html` references | 49 distinct across 60 crawl records | 0 |
| Redirect chains >1 hop | 0 | 0 |
| Unexpected final 404 | 0 | 0 |
| Unexpected final 5xx | 0 | 0 |
| Deliberate unknown route | Not part of baseline crawl | Correct 404 |

Duplicate-canonical groups in the expanded after-crawl are the 68 deliberate alias-to-canonical pairs, not duplicate sitemap entries.

## 10. Performance comparison

Chrome navigation traces used the same Fast 4G profiles before and after.

| Profile | Before | After | Assessment |
|---|---|---|---|
| Mobile 390x844, DPR 3, CPU 4x | LCP 718 ms, TTFB 34 ms, CLS 0.01 | Three runs: 749/763/785 ms; median 763 ms, TTFB 34 ms, median CLS 0.00 | No material regression; +45 ms median LCP |
| Desktop 1440x900, CPU 1x | LCP 368 ms, TTFB 34 ms, CLS 0.19 | LCP 377 ms, TTFB 33 ms, CLS 0.09 | LCP effectively flat; CLS improved |

Final production mobile Lighthouse: SEO 100, Best Practices 100, Accessibility 97. No CrUX field data was available for the query-parameter test URLs.

## 11. Cache and CDN actions

- Deployed commits `4bba1c8`, `9f73fc1`, and final `f93ee83` through the existing Git-to-Cloudflare Pages pipeline.
- Verified each deployment by a new sitemap/content/script fingerprint before crawling.
- No global cache purge was performed. A purge was unnecessary because Cloudflare Pages published the new asset/content versions successfully and fresh browser contexts received the final JavaScript.
- No VPS restart or Apache/WordPress cache mutation was performed.

## 12. Rollback information

The exact pre-change production commit is `534bffde6a6b009d6b9986f1d222ad1cc24cc88b`.

Safe rollback preserves history by reverting the three production commits newest-first:

```powershell
git revert f93ee839c1ce385521907637261ffac3f839423e
git revert 9f73fc1
git revert 4bba1c8
git push origin master
```

Before-state crawl, server configuration snapshots, and after-state evidence live beside this report. The WordPress/VPS configuration was not mutated, so no server-side rollback is needed.

## External indexing submission

`robots.txt` returns 200 and declares `https://camelotflows.dev/sitemap.xml`; the sitemap itself returns 200 with 88 valid canonicals. Direct Search Console resubmission was not completed because the available browser session reached the Google sign-in screen and no authenticated Search Console property/API credential was available. Manual action: sign in to Search Console for `sc-domain:camelotflows.dev`, open Sitemaps, and submit `sitemap.xml` once.

## Verification evidence

- `before-crawl.json` and `before-summary.json`
- `after-crawl.json` and `after-summary.json`
- `local-resource-audit.json` and `after-resource-audit.json`
- `performance-comparison.json`
- `server-config/` pre-change snapshots
- Automated gates: 83 JavaScript tests and 11 Python SEO/localization tests passed

READY FOR INDEXING: YES
