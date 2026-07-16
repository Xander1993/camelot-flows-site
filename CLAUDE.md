# Camelot Flows — Project Guide

Solo workshop website. Static HTML site **and** WordPress theme, built from the same hand-authored pages. Premium aesthetic, dual-mode (cozy light / neon-knight dark), GSAP + Lenis driven.

---

## Memory — CRITICAL

**The Obsidian vault at `E:\Camelot Flows` is the ONLY memory system for this project.**

- Save all notes, feedback, decisions, and learnings to the vault using the obsidian MCP or Write tool
- Do NOT use the auto-memory folder at `C:\Users\user\.claude\projects\...\memory\` — that folder is overridden by this rule
- Vault folder routing: strategy/business → `01 - Business\`, tech → `02 - Tech\`, clients → `03 - Clients\`, outreach → `04 - Outreach\`, content → `05 - Content\`, principles/frameworks/feedback → `06 - Knowledge\`

---

## Session Start — Always Do This

1. Read `E:\Camelot Flows\🗺 index.md` **first** — this is the vault map. It tells you what exists and where.
2. Read `E:\Camelot Flows\🏠 Home.md` — current week's focus, active leads, metrics
3. For any strategy/outreach/research task → use the obsidian MCP (`mcp__obsidian__read_notes`) to read the specific note before starting
4. When research results come in or decisions are made → run `/ingest` to file immediately, don't wait to be asked
5. When you encounter a `[[wiki link]]` in a vault note → follow it with the obsidian MCP
6. **Check `E:\Camelot Flows\_inbox\`** — the human drop-zone (Obsidian Web Clipper target + manual dumps, the "raw/" staging from Karpathy's Obsidian-RAG pattern). If it holds files, process them: spawn a vault-ingest subagent (classify → wiki-fy → cross-reference 10–15 notes → update `🗺 index.md` → append `📋 log.md`), then move originals to `_inbox\_processed\`. Don't leave raw files unprocessed.

**Summarizing a video/article for ingestion:** use the `ytx` helper in WSL — `wsl -e bash -lc "~/.local/bin/ytx '<youtube-url>' [pattern]"` (default pattern `extract_wisdom`). It pulls the transcript via `yt-dlp` and pipes it into fabric. Do **not** use `fabric -y` directly — it hangs (no `YOUTUBE_API_KEY`).

**Ingest pattern (Karpathy LLM Wiki) — fully automatic, no prompt needed:**
| Step | Action |
|------|--------|
| Raw research arrives | Spawn a vault-ingest subagent (Agent tool) — do NOT process inline |
| Subagent handles | Classify → file → cross-reference **10–15** related notes → update index.md → append log.md |
| Main session receives | One-line summary: what was filed, what was updated, what links were made |
| Complex answer given | If a strategic answer took synthesis (3+ sentences), file it as a wiki page too |
| `/lint` | Health check: structural + gap analysis |

**Subagent rule — ALWAYS spawn Agent for vault ingestion:**
When research, decisions, or new knowledge arrives in the conversation:
1. DO NOT process it inline — this pollutes main context with vault work
2. Spawn an Agent subagent using the prompt template in the `/ingest` skill
3. The subagent handles the full pipeline: classify → write → cross-reference → update index → log
4. Report back to the user in one sentence: "Filed X → updated Y, Z, W → linked to A, B"
5. Main conversation stays clean and fast

**Query compounding rule:**
When you give a strategic answer that involved real synthesis — comparing options, market analysis, tactical recommendation — file it as a wiki page via subagent. The question becomes the title, the answer becomes the page. This is how the vault compounds on queries, not just ingests.

**Vault folder routing:**
| Task type | Vault folder |
|-----------|-------------|
| Market research, competitive analysis, pricing, testimonials | `E:\Camelot Flows\01 - Business\` |
| Outreach channels, group lists, email templates, social strategy | `E:\Camelot Flows\04 - Outreach\` |
| Tech, servers, MCP, infrastructure | `E:\Camelot Flows\02 - Tech\` |
| Client notes | `E:\Camelot Flows\03 - Clients\` |
| Content ideas, YouTube, social posts | `E:\Camelot Flows\05 - Content\` |
| Frameworks, tactics, principles | `E:\Camelot Flows\06 - Knowledge\` |

---

## Working Directories

| Path | Purpose |
|------|---------|
| `D:\Download\stitch_camelot_flows_homepage` | **This repo** — static HTML site + WP theme. Edit here, `git push` → Cloudflare Pages auto-deploys. |
| `E:\Camelot Flows` | **Obsidian vault** — all strategy, outreach, client, and knowledge notes. Write Obsidian notes here ONLY, never in the repo. |

## Servers

| Server | IP | SSH port | SSH user | Key | Hosts |
|--------|----|----------|----------|-----|-------|
| DigitalOcean VPS | `46.101.150.59` | `8080` | `root` | `C:\Users\user\.ssh\id_ed25519` | www.camelotflows.dev, blog.camelotflows.dev |
| Hostinger VPS | `72.62.45.144` | `22` | `developer` | `C:\Users\user\.ssh\id_ed25519` | camelotflows + client sites |

**SSH rule:** Always use PowerShell tool for SSH/SCP — Bash mangles Windows key paths.
**DO Console:** broken (Bitnami disables password auth). Use SCP only.
**SCP to DO:** `scp -P 8080 -i "C:\Users\user\.ssh\id_ed25519" file root@46.101.150.59:/var/www/html/...`

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

**Cloudflare Pages serves everything.** There is one live deployment target.

| What | Where served | How to deploy |
|---|---|---|
| `camelotflows.dev` (root) | **Cloudflare Pages** (`camelot-flows-site-git.pages.dev`) | `git push origin master` — auto-deploys |
| `www.camelotflows.dev` | CF-proxied → **301 to `https://camelotflows.dev/`** | n/a — redirect only |
| `blog.camelotflows.dev` | CF-proxied → **301 to `https://camelotflows.dev/blog/`** | n/a — redirect only |

DNS proof (re-verified 2026-07-16): apex, `www` and `blog` all resolve to the **same Cloudflare anycast IPs** (`172.67.221.28` / `104.21.53.245`); the apex is a CNAME → `camelot-flows-site-git.pages.dev`, flattened to A records by Cloudflare. Pages serves the static HTML, `assets/`, **and** `/work-with-me`, `/contact`, `/blog/` — all from the `.html` files in this repo, *not* from WordPress page templates.

`_headers` (HSTS, X-Frame-Options, frame-ancestors, Permissions-Policy) is scoped `/*`, which covers **both static assets and `/api/*` Functions** — verified 4/4 headers on `/`, `/audit`, `/contact` and `/api/audit`.

**The DigitalOcean VPS (`46.101.150.59`) is GONE.** It no longer answers ICMP, `:80` or `:8080` (re-verified 2026-07-16). `wp-theme/` and `build_wp.py` are still in this repo but are **vestigial — they deploy nowhere.** Do not `scp` to it and do not edit WP templates expecting a live page to change; the page you want is the `.html` file at the repo root.

**The trap:** editing `assets/js/camelot-gsap.js` only takes effect after `git push`. Cloudflare Pages serves `index.html` for 404s (SPA fallback), so a missing asset URL returns HTML, not a 404.

## Build & deploy

- **Static site (CF Pages):** edit HTML + `assets/` directly, then `git push origin master`. Pages deploys in ~30–60s.
- **WordPress theme (`wp-theme/`): DEAD PATH — do not use.** `build_wp.py` / `fix_wp_buttons.py` rewrite the static pages into `wp-theme/camelot-flows/page-*.php`, but their only deploy target was the DigitalOcean VPS, which is gone (see *Deployment architecture*). Editing these changes nothing live.
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
