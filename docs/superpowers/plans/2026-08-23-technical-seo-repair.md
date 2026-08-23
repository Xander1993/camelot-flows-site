# Camelot Flows Technical SEO Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Preserve every indexed English URL while shipping crawlable Romanian and Russian pages, direct internal links, clean indexing signals, and reproducible before/after production evidence.

**Architecture:** The tracked English HTML remains the single hand-authored source. A tested Python generator uses the existing `window.cfLocales` dictionaries plus existing `data-lang-content` translations to emit static `/ro/.../index.html` and `/ru/.../index.html` documents; it never invents missing article translations. A tested crawler validates raw initial HTML, redirects, canonicals, hreflang, resources, sitemap membership, and internal-link counts before and after deployment.

**Tech Stack:** Static HTML, Python 3.10 + BeautifulSoup 4, Node test runner, Cloudflare Pages clean URLs/functions, Apache 2.4 on the legacy WordPress VPS, Chrome DevTools/Lighthouse.

**Spec:** `E:/AI/Codex/attachments/e8ad6e20-0cf4-4cac-a012-3082a047e3bc/pasted-text.txt`

## Global Constraints

- Keep root English URLs canonical; do not move them under `/en/`.
- Keep legacy `.html` and migrated `blog.camelotflows.dev` permanent redirects.
- Do not auto-redirect by IP, browser language, or `Accept-Language`.
- Generate localized URLs only from real existing translations.
- Preserve visual design, forms, theme switching, consent, navigation, and animation behavior.
- Keep the Ambienti draft out of `sitemap.xml` and noindex until approval.
- Deploy only after local validations pass, then repeat them against public production.
- Roll back immediately if a significant live regression appears.

---

### Task 1: Baseline evidence and rollback checkpoint

**Files:**
- Create: `reports/seo-2026-08-23/before-crawl.json`
- Create: `reports/seo-2026-08-23/before-summary.json`
- Create: `reports/seo-2026-08-23/server-config/README.md`
- Test: `tests/seo-crawl.test.mjs`

**Interfaces:**
- Produces: public URL inventory and server/deployment facts used by every later gate.

- [ ] Write crawler fixture tests proving one-hop redirects, raw HTML metadata extraction, sitemap flags, and inbound-link counting.
- [ ] Run `node --test tests/seo-crawl.test.mjs` and confirm failure because `tools/seo-crawl.mjs` does not exist.
- [ ] Implement `tools/seo-crawl.mjs` with `crawlSite({ baseUrl, seeds, sitemapUrls })` and JSON output.
- [ ] Run the crawler against the public site and save the raw before inventory.
- [ ] Record verified production commit `534bffde6a6b009d6b9986f1d222ad1cc24cc88b`, branch, tracked dirty files, Cloudflare/Apache document roots, deployment methods, and redirect configuration.

### Task 2: Static multilingual generator

**Files:**
- Create: `tools/build_localized.py`
- Create: `tests/test_build_localized.py`
- Modify: `assets/js/i18n.js`
- Modify: `assets/js/camelot-gsap.js`
- Generate: `ro/**/index.html`
- Generate: `ru/**/index.html`

**Interfaces:**
- Consumes: tracked English HTML, `assets/js/locales.js`, and existing `data-lang-content` blocks.
- Produces: `build_localized(root: Path) -> BuildReport` and fixed-language documents with reciprocal hreflang.

- [ ] Write failing fixtures for fixed `<html lang>`, self-canonical, reciprocal EN/RO/RU/x-default, localized metadata/body, absolute asset paths, crawlable language anchors, localized internal links, and removal of non-selected language bodies.
- [ ] Run `python -m unittest tests.test_build_localized -v` and confirm the expected import/behavior failures.
- [ ] Implement locale loading, translation lookup, HTML rewriting, blog translation eligibility, and deterministic output.
- [ ] Change the language interaction so anchors navigate to URL variants and stored language never mutates the English root document.
- [ ] Generate localized documents and rerun unit tests plus a deterministic second build.

### Task 3: Canonical internal routes, metadata, schema, and commercial clarity

**Files:**
- Modify: public top-level `*.html`
- Modify: `blog/index.html` and `blog/*/index.html`
- Modify: `assets/js/locales.js`
- Modify: `assets/js/locales.min.js`
- Modify: `assets/js/camelot-gsap.js`
- Modify: `assets/js/camelot-gsap.min.js`
- Test: `tests/seo-site.test.mjs`

**Interfaces:**
- Produces: final canonical clean URLs, no redirecting first-party navigation/prefetches, localized metadata, and one consistent Organization entity.

- [ ] Write failing tests that scan the real public HTML and reject `.html` internal navigation/prefetch URLs, redirected canonical/schema URLs, missing metadata/H1, non-anchor language options, and unsupported localized variants.
- [ ] Run `node --test tests/seo-site.test.mjs` and retain the red failure counts.
- [ ] Apply the smallest link and metadata edits; keep legacy redirect handling intact.
- [ ] Normalize Organization `@id` to `https://camelotflows.dev/#organization` and canonical author/about URLs without adding unsupported schema types.
- [ ] Make the homepage plain-language offer cover web/WordPress/WooCommerce, redesign/migration, AI automation/integrations, and maintenance without ranking promises or unmeasured claims.
- [ ] Rebuild localized output and run the site tests green.

### Task 4: Sitemap, robots, draft case study, and resources

**Files:**
- Modify: `sitemap.xml`
- Modify: `robots.txt` only if validation finds a real defect
- Create: `work/ambienti/index.html`
- Test: `tests/seo-site.test.mjs`

**Interfaces:**
- Produces: sitemap containing only indexable 200 canonical EN/RO/RU URLs and a noindex Ambienti preview excluded from it.

- [ ] Add failing assertions for sitemap 200/canonical/indexable rules, `robots.txt` sitemap reference, Ambienti noindex/exclusion, and first-party resource existence.
- [ ] Build the Ambienti preview only from verified repository/project facts, with no metrics, endorsement, or testimonial.
- [ ] Generate `sitemap.xml` from the validated page manifest and keep legacy aliases crawlable.
- [ ] Remove obsolete redirecting prefetches and repair any critical first-party resource failures.
- [ ] Run all local SEO tests and resource checks green.

### Task 5: Local rendering and performance gate

**Files:**
- Create: `reports/seo-2026-08-23/local-validation.json`

**Interfaces:**
- Produces: deploy/no-deploy decision.

- [ ] Run `node --test tests/*.test.mjs` and `python -m unittest tests.test_build_localized -v`.
- [ ] Run `npm run build` and verify generated CSS does not change unexpectedly or regress the page.
- [ ] Serve the repository locally and crawl EN/RO/RU raw HTML.
- [ ] Inspect desktop and 390px mobile navigation, language links, theme switcher, contact form, WhatsApp, consent, animation, and representative blog layouts.
- [ ] Run Lighthouse/trace baseline comparisons and block deployment on meaningful regressions or new console errors.

### Task 6: Deployment and public verification

**Files:**
- Create: `reports/seo-2026-08-23/after-crawl.json`
- Create: `reports/seo-2026-08-23/final-report.md`

**Interfaces:**
- Produces: public evidence and exact rollback instructions.

- [ ] Commit only scoped SEO files and push the SEO branch only after every local gate passes.
- [ ] Merge/push to the Cloudflare Pages production branch only within the authorization in the task and wait for the deployment to become live.
- [ ] Do not change Apache unless live migrated-blog validation proves the existing rules are defective; back up and syntax-test any config before reload.
- [ ] Crawl public production again; verify aliases and migrated blog URLs are one permanent hop to 200.
- [ ] Inspect representative EN/RO/RU raw source and rendered desktop/mobile pages, sitemap, robots, resource requests, console, and Lighthouse.
- [ ] Write the requested 12-section final report and use `SEO TECHNICAL REPAIR READY: YES` only when every critical gate is evidenced as passing.

### Task 7: Project memory ingestion

**Files:**
- Create/update only in `E:/Camelot Flows/02 - Tech/` through the project ingest workflow.

**Interfaces:**
- Produces: durable vault record of architecture, rollback point, validation evidence, and follow-up actions.

- [ ] Ingest the substantive implementation decisions and verified production result after the live validation gate.
- [ ] Update the vault index and log through the required vault-ingest workflow without adding repo memory files.
