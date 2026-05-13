# Camelot Flows — Project Guide

Solo workshop website. Static HTML site **and** WordPress theme, built from the same hand-authored pages. Premium aesthetic, dual-mode (cozy light / neon-knight dark), GSAP + Lenis driven.

---

## Quick orientation

- **Default theme:** `cozy` — warm cream surfaces, terracotta + sage accents, Fraunces serif display.
- **Dark theme:** `night` — deep obsidian background, indigo + cyan + magenta neon glows, glass-morphism panels.
- **Switch via:** the sun/moon button in the top nav. Persists to `localStorage['cf_theme']`. Driven by `<html data-theme="cozy|night">`.
- **Same HTML for both modes** — class names like `bg-obsidian`, `glass-panel`, `text-primary-glow` resolve to different values per `data-theme` via specificity overrides.

---

## Directory map

```
.
├── index.html, about.html, arsenal.html, merlin.html,        # Live pages (top nav)
│   case-studies.html, for-agencies.html, contact.html,
│   work-with-me.html, legal.html, privacy.html
├── service-creation.html, service-maintenance.html,          # Service detail pages
│   service-automation.html, service-marketing.html
├── assets/
│   ├── site.css            # Cozy palette, base utilities, .dark component variants
│   ├── site.js             # Small interaction helpers
│   ├── css/
│   │   ├── camelot.css     # Component styles (glass-panel, grid-bg, text-glow)
│   │   ├── theme-night.css # data-theme="night" overrides (the dark mode)
│   │   └── tokens.css      # Token reference (not yet imported)
│   ├── js/camelot-gsap.js  # GSAP/Lenis engine: preloader, hero, scroll triggers
│   └── images/             # Shared by both themes — kept as-is
├── wp-theme/camelot-flows/ # WordPress theme (parallel deploy)
├── build_wp.py             # HTML → WP page templates
├── fix_html_links.py       # Batch link repair
├── fix_wp_buttons.py       # WP CTA wrapper
├── _archive/               # Orphan HTML + scratch Python (do not deploy)
└── dist/                   # Generated build output (do not edit)
```

**Where NOT to look:**
- `../stitch_camelot_flows_homepage - Copy/` — deprecated reference variant. See its `DEPRECATED.md`. Do not develop there.
- `_archive/` — orphan pages and scratch scripts.
- `dist/` — generated build output.

---

## Live page inventory

| Page | Linked from | Role |
|---|---|---|
| `index.html` | (root) | Homepage / hero |
| `about.html` | nav, footer | About / team |
| `arsenal.html` | nav, footer | Product showcase |
| `merlin.html` | nav, footer | Merlin AI protocol |
| `case-studies.html` | nav | Portfolio |
| `for-agencies.html` | nav | Agency partnerships |
| `contact.html` | nav, footer | Contact form |
| `work-with-me.html` | footer | Engagement |
| `legal.html` | footer | Legal / terms |
| `privacy.html` | footer | Privacy policy |
| `service-creation.html` | footer (Services) | Web creation service |
| `service-maintenance.html` | footer (Services) | Maintenance service |
| `service-automation.html` | footer (Services) | AI automation service |
| `service-marketing.html` | footer (Services) | Growth marketing service |

---

## Theme system

**How it works**

1. **Bootstrap** (synchronous, runs before paint) at the top of every page's `<head>`:
   ```html
   <script>
     (function () {
       var t = localStorage.getItem('cf_theme') || 'cozy';
       document.documentElement.setAttribute('data-theme', t);
     })();
   </script>
   ```
2. **Stylesheets**, in order, after Tailwind:
   ```html
   <link rel="stylesheet" href="assets/site.css">
   <link rel="stylesheet" href="assets/css/camelot.css">
   <link rel="stylesheet" href="assets/css/theme-night.css">
   ```
3. **Toggle button** lives in the nav (`#theme-toggle`). The click handler in `camelot-gsap.js` flips `data-theme`, persists to `localStorage`, and wraps the swap in `document.startViewTransition` for a smooth cross-fade in Chromium.

**Why HTML uses dark-theme class names on the cozy site**

Originally the site was the dark Neon Knight design. The cozy variant kept the markup but **remapped Tailwind colors** in the inline `tailwind.config` (`obsidian → #F5F4F0`). When dark mode was added back, we kept this contract: HTML stays untouched, palettes swap via `[data-theme="night"] .bg-obsidian { … }` and friends.

**Specificity rule:** `[data-theme="night"] .x` is `0,2,0` and beats Tailwind's `.x` at `0,1,0` regardless of cascade order.

---

## Animation engine — `assets/js/camelot-gsap.js`

- **GSAP 3.12.5** + ScrollTrigger + TextPlugin (CDN)
- **Lenis 1.0.42** (CDN) — smooth scroll
- **Preloader**: shown on first session visit only. Subsequent navigations within the session are gated by `sessionStorage['cf_loaded']` and skip the loader entirely (`html.cf-skip-preloader { … }`).
- **Failsafe**: `setTimeout(hidePreloader, 800)` is the **first statement** in the file so a thrown error elsewhere can never permanently hang the preloader.
- **Hero flash fix**: `gsap.set([...], {autoAlpha:0, yPercent:100})` is called synchronously at script load — hero elements are never seen un-animated.
- **`prefers-reduced-motion: reduce`** disables the marquee, portal, magnetic cursor, and other long-running motion.

---

## Deployment architecture — CRITICAL

Two completely separate deployment targets. Changes to one do NOT affect the other.

| What | Where served | How to deploy |
|---|---|---|
| `camelotflows.dev` (root) | **Cloudflare Pages** (`camelot-flows-site-git.pages.dev`) | `git push origin master` — auto-deploys |
| `www.camelotflows.dev` | **DigitalOcean VPS** `46.101.150.59` port 8080 SSH | Manual `scp` to `/var/www/html/` |
| `blog.camelotflows.dev` | Same VPS | Same |

DNS proof: `camelotflows.dev` is a CNAME → `camelot-flows-site-git.pages.dev`. Static HTML + `assets/` are served by Pages. WordPress serves `/work-with-me/`, `/contact/` etc. via page templates.

**The trap:** editing `assets/js/camelot-gsap.js` only takes effect after `git push`. The VPS has `camelot-gsap.v2.js` as a parallel copy for WP theme use — keep both in sync. Cloudflare Pages serves `index.html` for 404s (SPA fallback), so a missing asset URL returns HTML, not a 404.

## Build & deploy

- **Static site (CF Pages):** edit HTML + `assets/` directly, then `git push origin master`. Pages deploys in ~30–60s.
- **WordPress theme (VPS):** `python build_wp.py` rewrites the static pages into `wp-theme/camelot-flows/page-*.php` template files. Run `python fix_wp_buttons.py` after to fix CTA wrappers. Then `scp` changed files to VPS.
- **Tailwind:** if `assets/css/tailwind.built.css` exists, it has been compiled locally — do not edit. Source: `src/tw.css`, `tailwind.config.js`. Rebuild with `npx tailwindcss -i src/tw.css -o assets/css/tailwind.built.css --minify`.

---

## Conventions

- **Don't add another `build_*.py`.** The pipeline is `build_wp.py`. Older variants are in `_archive/scratch_scripts/`.
- **Don't restore inline `<style>` blocks.** Component CSS lives in `assets/css/camelot.css`; theme overrides in `assets/css/theme-night.css`.
- **Don't edit `dist/` or the `- Copy` folder.**
- **Fonts:** Fraunces (display), Inter (body), JetBrains Mono (code), Material Symbols Outlined (icons). All from Google Fonts.
- **CTAs** point to `contact.html?objective=<slug>` so the contact form can pre-fill subject lines.
- **Image dimensions:** enforce via `aspect-ratio` CSS, never via fixed height — prevents layout shift.

---

## Known gotchas

- The Tailwind CDN script also injects styles at runtime — that's why the page can briefly show un-styled content if it loads slowly. Once locally compiled, this disappears.
- The cream/cozy noise overlay is opacity 0.13 — too loud on the dark theme. `theme-night.css` reduces it to 0.05.
- Hero word splits use `wrapLetters()` which replaces `innerText` with per-char `<span>`s. Don't translate the page before this runs (e.g. Google Translate) — it breaks character indexing.
- Lenis `lenis.stop()` is called at init and only re-`start()`ed when the preloader exits or when the skip-preloader path runs. If you add another long-running early-init step, make sure scroll still re-enables.
