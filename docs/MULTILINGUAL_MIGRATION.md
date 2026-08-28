# Multilingual migration

## Preserved model

English remains the root language. Romanian uses `/ro/`; Russian uses `/ru/`. No request is redirected by IP, browser language, or `Accept-Language`.

Before the August 23 technical repair, EN/RO/RU content was switched inside the same canonical URL by JavaScript. Production already had that defect repaired before this repositioning branch: generated static RO and RU documents now contain localized raw HTML and self-canonicals.

This branch preserves the repaired architecture and adds the focused commercial equivalents below.

| Intent | English | Romanian | Russian |
|---|---|---|---|
| Homepage | `/` | `/ro/` | `/ru/` |
| Quote-to-order | `/quote-to-order` | `/ro/quote-to-order` | `/ru/quote-to-order` |
| Technical distributors | `/industries/technical-distributors` | `/ro/industries/technical-distributors` | `/ru/industries/technical-distributors` |
| HVAC and refrigeration | `/industries/hvac-refrigeration` | `/ro/industries/hvac-refrigeration` | `/ru/industries/hvac-refrigeration` |
| Websites and portals | `/websites` | `/ro/websites` | `/ru/websites` |
| Case studies | `/case-studies` | `/ro/case-studies` | `/ru/case-studies` |
| About | `/about` | `/ro/about` | `/ru/about` |
| Workflow diagnostic | `/contact` | `/ro/contact` | `/ru/contact` |

Every row has a reciprocal EN/RO/RU/x-default hreflang set. Each page uses a self-referencing absolute HTTPS canonical, language-matched title, description, H1, navigation, body, schema, and crawlable language links.

## Redirects and conventions

- Existing extensionless top-level URLs remain canonical; no core URL is renamed.
- Cloudflare Pages normalizes `.html` and trailing-slash aliases for top-level files to the existing extensionless canonical.
- The new pages follow that same extensionless convention.
- No locale redirect is added.

## Blog rule

Existing article URLs and their translations are preserved. The English-only AI intake article remains English-only; no low-quality automatic RO/RU page is generated. Dreamscape remains indexable in all existing languages but is labelled `Founder Notes` and removed from the featured full-width position.

Future article translations must be published only when the full article, metadata, navigation, and schema are reviewed in that language. Add the complete reciprocal hreflang set only after every declared equivalent returns canonical 200 HTML.

## Build ownership

The existing static templates and `assets/js/locales.js` remain authoritative. New commercial routes reuse the same Camelot page components, theme behavior, navigation, and motion as the existing site. `tools/seo_localize.py` continues to own localized legacy pages and articles.
