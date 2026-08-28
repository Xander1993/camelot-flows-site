# Camelot Flows SEO Repositioning and Stabilisation

Date: 2026-08-28  
Branch: `seo-reposition-stabilization`  
Production deployment: **not performed**

## 1. Strategic summary

Camelot Flows now presents one primary category: **AI-assisted sales and operations systems for technical B2B companies**. The homepage leads with a supervised customer-request-to-quotation workflow for distributors, installers, and technical service companies in Moldova and Romania. Prices, commitments, technical exceptions, and safety-critical choices remain explicitly human-approved.

Website work remains available at `/websites` as a separate supporting offer. The narrow €390 page remains preserved at its existing URL, but it is no longer the homepage's dominant commercial anchor.

The existing Camelot design was preserved. The branch-base Tailwind CSS, consent component, GSAP behavior source, themes, typography, logo, page components, and responsive navigation behavior have no diff. Content, destinations, metadata, language output, form fields, and schema were changed inside the existing templates.

## 2. Current architecture

- Static HTML site with Tailwind/component CSS and existing JavaScript interaction layer.
- Git origin: `git@github.com:Xander1993/camelot-flows-site.git`.
- Cloudflare Pages serves the repository root; production branch is `master`.
- Server used for the isolated worktree: `72.62.45.144`.
- Isolated worktree: `/home/deployer/sites/camelot-flows-seo`.
- English remains the root language; Romanian uses `/ro/`; Russian uses `/ru/`.
- The sitemap contains 100 canonical, indexable URLs.

## 3. Confirmed baseline problems

- The former homepage mixed websites, WordPress, SEO, broad AI automation, agency work, and unrelated topics, leaving no stable commercial category.
- No dedicated routes existed for quote-to-order automation, technical distributors, HVAC/refrigeration, or websites as a supporting capability.
- Three RO and three RU legacy offer pages repeated English meta descriptions.
- Founder/game-development content was featured as the main blog item rather than a secondary founder note.
- The About page published a detailed personal timetable.
- The generic contact form did not collect enough process context for a workflow diagnostic.
- Previous resource-failure evidence could not be reproduced: the live baseline loaded all 89 discovered first-party resources successfully.

Detailed evidence is in `docs/SEO_BASELINE.md` and `docs/URL_CONTENT_MATRIX.csv`.

## 4. Core route map

| Intent | English | Romanian | Russian |
|---|---|---|---|
| Homepage | `/` | `/ro/` | `/ru/` |
| Quote-to-Order | `/quote-to-order` | `/ro/quote-to-order` | `/ru/quote-to-order` |
| Technical distributors | `/industries/technical-distributors` | `/ro/industries/technical-distributors` | `/ru/industries/technical-distributors` |
| HVAC and refrigeration | `/industries/hvac-refrigeration` | `/ro/industries/hvac-refrigeration` | `/ru/industries/hvac-refrigeration` |
| Websites and portals | `/websites` | `/ro/websites` | `/ru/websites` |
| Case studies | `/case-studies` | `/ro/case-studies` | `/ru/case-studies` |
| About | `/about` | `/ro/about` | `/ru/about` |
| Workflow diagnostic | `/contact` | `/ro/contact` | `/ru/contact` |

Every core page has a self-canonical, reciprocal EN/RO/RU hreflang, and x-default. Language links are crawlable anchors and there is no IP or browser-language redirect.

## 5. URL migration and redirects

- All 88 pre-existing sitemap URLs were retained and assigned an action in the URL matrix.
- Twelve localized commercial URLs were added; no existing useful route was renamed or deleted.
- No new internal redirect was needed for the core release.
- Live host behavior already sends HTTP and www variants to `https://camelotflows.dev` in one 301.
- `/about/` and `/about.html` currently reach `/about` through one 308.
- Eleven known legacy blog article URLs redirect one-to-one from `blog.camelotflows.dev/<slug>/` to `/blog/<slug>/` with one 301.
- Legacy no-slash article variants currently take two hops; exact Cloudflare configuration to remove that extra hop is documented in `docs/LEGACY_BLOG_REDIRECTS.md`.
- Unmatched legacy category, feed, author, and pagination samples truthfully resolve to 404 after the legacy-host redirect.
- Intentionally noindexed pages in this release: **none**.

## 6. Content and trust changes

- Rewrote EN/RO/RU homepage copy around customer requests, quotation preparation, source checks, approvals, CRM/ERP updates, and follow-up.
- Added unique operational content for quote-to-order, technical distribution, and HVAC/refrigeration.
- Clearly labelled NordTech Systems SRL as a fictional capability demonstration, not a client or performance claim.
- Preserved Timberkids and First Line Garage Door as real client work without inventing new metrics.
- Removed the detailed personal schedule from About and retained the solo-specialist identity.
- Relabelled Dreamscape as Founder Notes and made it secondary without deleting its URL.
- Expanded the contact form into a workflow diagnostic and added the non-confidential-upload warning.
- Added localized Service schema copy and stable organization references.
- Corrected localized metadata on the six affected legacy RO/RU offer pages.

## 7. Changed files

Main source groups:

- Core and supporting HTML in the repository root, `blog/`, `ro/`, and `ru/`.
- New `industries/` routes and localized equivalents.
- `assets/js/locales.js` and generated `assets/js/locales.min.js`.
- `sitemap.xml`.
- `tools/reposition-content.mjs`, `tools/seo_localize.py`, `tools/seo-crawl.mjs`, `tools/build-url-matrix.mjs`, and `tools/validate-repositioning.mjs`.
- Audit, migration, stability, external-profile, roadmap, QA, and screenshot artifacts under `docs/`.

The exact list is available from `git diff 74e010b..seo-reposition-stabilization --name-status`.

## 8. Validation results

### Build and automated tests

- `npm run build`: passed on the isolated server worktree.
- `npm run build:js`: passed on the final content.
- Local Node 22 test suite: **87/87 passed**.
- Server Node 18 test runner: 38/50 passed; 12 failures are pre-existing Node-runtime compatibility issues (ESM named imports and missing global Web Crypto), not content failures. The production build still passed.
- Production dependency audit: 0 vulnerabilities; development dependency audit reports 3 high-severity issues in the existing toolchain.

### Crawl and resources

- Sitemap URLs: **100**.
- Crawled: **100**.
- Non-200 pages: **0**.
- Missing canonical, H1, or description: **0**.
- Wrong fixed-route language: **0**.
- URLs missing from sitemap: **0**.
- Duplicate canonical groups: **0**.
- First-party resources checked: **88**; failures: **0**.

### Content and structured data

- Files validated: **100**.
- Localized core pages checked: **24**.
- Parsed JSON-LD documents: **94**.
- JSON-LD parse failures: **0**.
- Types found: BlogPosting, BreadcrumbList, FAQPage, Organization, Person, Service, WebApplication, and WebSite.
- Detailed-schedule remnants: **0**.
- Discarded redesign CSS/JS references: **0**.

### Lighthouse local-lab results

| Profile | Performance | Accessibility | Best Practices | SEO | LCP | CLS |
|---|---:|---:|---:|---:|---:|---:|
| EN desktop | 77 | 95 | 81 | 100 | 1.9 s | 0.25 |
| EN mobile | 37 | 96 | 82 | 100 | 8.4 s | 0.155 |
| RO mobile | 44 | 96 | 82 | 100 | 20.3 s | 0.226 |
| RU mobile | 42 | 96 | 82 | 100 | 9.0 s | 0.007 |

The performance target was not met. The user-requested design-preservation boundary leaves the existing image/animation/preloader stack intact. The local antivirus also injects Kaspersky requests into headless Chrome, lowering best-practices and contaminating timing. Treat these as review-lab measurements, then rerun against the Cloudflare preview URL without local injection before production approval.

## 9. Screenshots

- `docs/screenshots/home-en-desktop.png`
- `docs/screenshots/home-en-mobile.png`
- `docs/screenshots/home-ro-desktop.png`
- `docs/screenshots/home-ro-mobile.png`
- `docs/screenshots/home-ru-desktop.png`
- `docs/screenshots/home-ru-mobile.png`

## 10. Remaining external or hosting actions

1. Review the isolated branch and create a Cloudflare Pages preview deployment only.
2. Apply the legacy-subdomain no-slash redirect improvement from `docs/LEGACY_BLOG_REDIRECTS.md` if Cloudflare access is available.
3. Rerun Lighthouse on the HTTPS preview without antivirus injection; decide separately whether a later, design-approved performance pass may alter the loader or media strategy.
4. Review Web3Forms file-upload limits and privacy handling before enabling the optional attachment in production.
5. Update real external profiles using `docs/EXTERNAL_PROFILE_UPDATE.md`; no external account was accessed in this work.

## 11. Local preview

From the repository root:

```powershell
npm ci
npm run build
node tools/serve-site.mjs
```

Then open `http://127.0.0.1:8765/`. The server resolves extensionless routes and localized nested pages.

## 12. Git commits

- `cc49fe4` — `docs: record SEO and migration baseline`
- `bee5415` — `feat: reposition multilingual commercial content`
- `7f28956` — `test: add crawl and browser QA evidence`
- Final report commit follows these three commits.

The branch has not been merged into `master`, pushed to the production branch, or deployed to Cloudflare Pages.

## 13. Post-deployment checklist

1. Deploy the reviewed branch through the normal Cloudflare Pages workflow.
2. Confirm the production host, canonical, hreflang, sitemap, robots, form, theme, and language links.
3. Submit the existing sitemap in Search Console; inspect only `/`, `/ro/`, `/quote-to-order`, `/ro/quote-to-order`, and the two industry routes initially.
4. Update external profile descriptions and website links.
5. Monitor weekly: non-brand impressions, query families, landing pages, crawl errors, and qualified contacts.
6. At 30 days, check discovery and language targeting; at 60 days, publish or update one strong topical resource; at 90 days, evaluate qualified demand before changing positioning or core URLs.
