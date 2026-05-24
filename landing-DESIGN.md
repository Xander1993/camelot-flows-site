# Design System: Camelot Flows — Pricing Landing Pages

> Design bible for all 4 service landing pages: `launch-site.html`, `hermes-agent.html`,
> `ecommerce-wp.html`, `custom-premium.html`. Written per `stitch-design-taste` protocol.
> All sections reference this file. Override nothing without updating here first.

---

## 1. Visual Theme & Atmosphere

**Night mode (default):** Ethereal Glass — a deep, pressurised void punctuated by single-colour radial orbs.
The canvas feels like a high-end GPU render: obsidian black with precisely controlled ambient light leaking
in from one corner. Typography floats with apparent physical weight. Cards sit behind frosted panes of glass.
The atmosphere is deliberate, unhurried, premium — a film studio edit suite at 2 AM, not a SaaS dashboard.

**Cozy mode:** Editorial Luxury — warm cream parchment, terracotta ink, sage accents. The surface feels
like a beautifully typeset broadsheet, or a premium architectural studio's print portfolio. Shadows are
barely-there warm tints, not hard drops. The grain overlay hums at low opacity.

**Density:** 4 — Art Gallery. Massive white/dark space between sections. Content breathes.
**Variance:** 8 — Asymmetric. Hero is Editorial Split (60/40), never centred. Features use offset bento.
**Motion:** 7 — Cinematic. GSAP ScrollTrigger pins, spring-physics entrances, SVG draw animations.

Per-page accent colours (ONE accent per page, never mixed):

| Page              | Night accent (neon)      | Cozy accent (warm)       |
|-------------------|--------------------------|--------------------------|
| launch-site       | Neon Cyan   `#00f2ff`   | Terracotta   `#C4785C`  |
| hermes-agent      | Neon Purple `#bf00ff`   | Deep Violet  `#5B3A8C`  |
| ecommerce-wp      | Neon Amber  `#f59e0b`   | Amber        `#D97706`  |
| custom-premium    | Neon Cobalt `#0066ff`   | Cobalt       `#1D4ED8`  |

---

## 2. Color Palette & Roles

### Night Palette (data-theme="night")

- **Void Black** (`#050508`) — Body background. Never pure `#000`.
- **Obsidian Surface** (`#0A0A12`) — Section fill, card bases.
- **Glass Panel** (`rgba(255,255,255,0.04)`) — Card inner background (frosted glass feel).
- **Hairline Border** (`rgba(255,255,255,0.08)`) — All card outlines. Single-pixel structural lines only.
- **Slate Text** (`#e2e8f0`) — Primary body text. Not white — off-white with a hint of blue.
- **Muted Steel** (`rgba(226,232,240,0.45)`) — Secondary text, metadata, helper copy.
- **[Page Accent]** — Single accent per page (see table above). Used for: price display, eyebrow pills,
  SVG checkmark strokes, CTA button fill, active feature indicators. NOWHERE ELSE.
- **Accent Glow** (`rgba([accent], 0.18)`) — Used ONLY as a radial orb background. Never as text or border glow.

### Cozy Palette (data-theme="cozy")

- **Parchment** (`#F5F4F0`) — Body background.
- **Warm Surface** (`#EDEBE6`) — Card backgrounds, slightly darker than base.
- **Charcoal Ink** (`#1A1A18`) — Primary text. Not `#000`.
- **Stone** (`rgba(26,26,24,0.45)`) — Secondary text, captions.
- **[Page Accent]** — Warm variant (terracotta / violet / amber / cobalt). Same usage rules as night.
- **Accent Soft** (`rgba([accent], 0.10)`) — Eyebrow pill background. Never glow effect in cozy.

### Shared Rules
- Maximum 1 accent colour per page. Never use multiple accent colours in the same section.
- NO neon outer glows in cozy mode — accent used as solid fill or hairline border only.
- Night mode: accent MAY have a diffuse radial ambient glow (as background orb). NOT on text or button.
- Grain overlay: `opacity: 0.13` cozy, `opacity: 0.05` night — fixed pseudo-element only.

---

## 3. Typography Rules

### Font Stack (loaded via Google Fonts on each page)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Space+Grotesk:wght@300..700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

- **Fraunces** — Display font. All H1/H2 headings, eyebrow pills (small + all-caps), blockquotes,
  risk-reversal copy (italic), final CTA headline.
- **Space Grotesk** — Body text, feature descriptions, FAQ answers, nav links, form labels.
  `Inter` is **strictly banned**. No exceptions.
- **JetBrains Mono** — Price tags, timeline labels, step numbers, code snippets.
  Monospaced numerals. Always used for the `€` price.

### Scale Hierarchy

| Role | Spec |
|------|------|
| H1 Hero | `font-family: Fraunces; font-size: clamp(3.5rem, 5.5vw, 5.5rem); font-weight: 500; line-height: 1.05; letter-spacing: -0.02em; max-width: 44rem` |
| H2 Section | `font-family: Fraunces; font-size: clamp(2.5rem, 4vw, 3.75rem); font-weight: 400; line-height: 1.1` |
| Eyebrow Pill | `font-family: Fraunces; font-size: 0.6875rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.18em` |
| Price | `font-family: JetBrains Mono; font-size: clamp(4rem, 7vw, 6rem); font-weight: 400` |
| Body | `font-family: Space Grotesk; font-size: 1.0625rem; line-height: 1.7; max-width: 65ch` |
| Meta/label | `font-family: Space Grotesk; font-size: 0.8125rem; letter-spacing: 0.06em` |

### Typography Rules
- H1 must never exceed 3 lines at desktop viewport (1280px+). Use `max-w-3xl` + `clamp()` scale.
- Fraunces italic used ONLY for risk-reversal/guarantee copy and decorative pull-quotes. Not in nav, not in body.
- NO gradient text on headings (no `background-clip: text` fills on H1/H2). Accent used as solid colour.
- Track-tight (`letter-spacing: -0.02em`) on all display. Normal tracking on body (`0`).

---

## 4. Component Stylings

### Double-Bezel Card (all major cards — feature cards, risk-reversal, CTA zone)
```css
/* Outer shell */
.bezel-outer {
  border-radius: 2rem;
  padding: 6px;
  border: 1px solid rgba(255,255,255,0.08);   /* hairline ring */
  background: rgba(255,255,255,0.03);
}
/* Inner core */
.bezel-inner {
  border-radius: calc(2rem - 6px);
  background: rgba(255,255,255,0.04);         /* glass fill */
  box-shadow: inset 0 1px 1px rgba(255,255,255,0.10); /* top-edge refraction */
  padding: 2rem;
}
[data-theme="cozy"] .bezel-outer { border-color: rgba(26,26,24,0.09); background: rgba(26,26,24,0.03); }
[data-theme="cozy"] .bezel-inner { background: rgba(255,255,255,0.60); box-shadow: inset 0 1px 0 rgba(255,255,255,0.8); }
```

### Eyebrow Pill (before every H2 and H1)
```html
<span class="eyebrow-pill">Fixed Scope</span>
```
```css
.eyebrow-pill {
  display: inline-flex; align-items: center;
  padding: 0.25rem 0.875rem;
  border-radius: 999px;
  background: rgba([accent-rgb], 0.12);
  border: 1px solid rgba([accent-rgb], 0.25);
  color: [accent];
  font-family: Fraunces, serif;
  font-size: 0.6875rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-weight: 500;
}
```

### Button-in-Button CTA Pill
```html
<a href="..." class="cta-pill">
  <span>Book a Call</span>
  <span class="cta-arrow-circle">
    <svg><!-- right-arrow --></svg>
  </span>
</a>
```
```css
.cta-pill {
  display: inline-flex; align-items: center; gap: 0.75rem;
  padding: 0.875rem 0.875rem 0.875rem 1.75rem;
  border-radius: 999px;
  background: [accent];
  color: #fff (or #0A0A12 for light accents);
  font-family: Space Grotesk; font-size: 1rem; font-weight: 500;
  transition: transform 0.35s cubic-bezier(0.32,0.72,0,1),
              box-shadow 0.35s cubic-bezier(0.32,0.72,0,1);
}
.cta-pill:hover { transform: translateY(-2px); }
.cta-arrow-circle {
  width: 2.25rem; height: 2.25rem;
  border-radius: 999px;
  background: rgba(0,0,0,0.18);   /* or rgba(255,255,255,0.2) on dark btn */
  display: flex; align-items: center; justify-content: center;
  transition: transform 0.3s cubic-bezier(0.32,0.72,0,1);
}
.cta-pill:hover .cta-arrow-circle { transform: translate(3px, -2px) scale(1.1); }
```

### Ghost Secondary CTA Pill
```css
.cta-ghost {
  display: inline-flex; align-items: center; gap: 0.5rem;
  padding: 0.875rem 1.75rem;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.15);
  background: transparent;
  color: rgba(226,232,240,0.80);
  font-family: Space Grotesk; font-size: 1rem;
  transition: border-color 0.3s ease, background 0.3s ease;
}
.cta-ghost:hover { background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.3); }
[data-theme="cozy"] .cta-ghost { border-color: rgba(26,26,24,0.2); color: rgba(26,26,24,0.7); }
[data-theme="cozy"] .cta-ghost:hover { background: rgba(26,26,24,0.05); border-color: rgba(26,26,24,0.4); }
```

### FAQ Accordion
```css
.faq-item { border-bottom: 1px solid rgba(255,255,255,0.08); padding: 1.5rem 0; }
.faq-trigger { display: flex; justify-content: space-between; align-items: center; cursor: pointer; }
.faq-arrow { transition: transform 0.35s cubic-bezier(0.32,0.72,0,1); }
.faq-item.is-open .faq-arrow { transform: rotate(90deg); }
.faq-body { max-height: 0; overflow: hidden; opacity: 0;
  transition: max-height 0.45s cubic-bezier(0.4,0,0.2,1), opacity 0.3s ease 0.05s; }
.faq-item.is-open .faq-body { max-height: 300px; opacity: 1; }
[data-theme="cozy"] .faq-item { border-bottom-color: rgba(26,26,24,0.1); }
```

### Nav (floating glass pill — shared across all 4 pages)
```css
.lp-nav {
  position: fixed; top: 1.5rem; left: 50%; transform: translateX(-50%);
  z-index: 100;
  display: flex; align-items: center; gap: 2rem;
  padding: 0.75rem 1.75rem;
  border-radius: 999px;
  background: rgba(5,5,8,0.75);
  backdrop-filter: blur(20px) saturate(1.4);
  border: 1px solid rgba(255,255,255,0.08);
  white-space: nowrap;
}
[data-theme="cozy"] .lp-nav {
  background: rgba(245,244,240,0.80);
  border-color: rgba(26,26,24,0.10);
}
```

---

## 5. Layout Principles

- **Hero:** Editorial Split — 60% left (copy) / 40% right (price + abstract shape). NEVER centred.
  Below `md` (768px): single column, price block below copy.
- **Features (S3):** GSAP-pinned. Two-column split: 35% left (feature list) / 65% right (active detail).
  Below `md`: standard vertical accordion stack.
- **Deliverables (S4):** Single-column checklist, max-width 720px, centred with generous left padding on desktop.
- **Timeline (S5):** Full-width SVG drawn by scrub. Below `md`: vertical milestone list.
- **Risk Reversal (S6):** Double-bezel card, max-width 680px, centred.
- **FAQ (S7):** Single-column, max-width 720px, centred.
- **Final CTA (S8):** Full-viewport, centred for this section only (exception to split rule — CTA is isolation).
- **Max content width:** `max-w-7xl` (80rem) with `px-6 lg:px-12` padding.
- **Section gap:** `py-32 md:py-48` between all major sections.
- **CSS Grid** for all multi-column layouts. No flexbox percentage math.
- `min-h-[100dvh]` for full-viewport sections (S1 hero, S8 CTA). Never `h-screen`.

---

## 6. Motion & Interaction

All animations: `transform` + `opacity` ONLY. Never animate `top`, `left`, `width`, `height`.

### Hero Entrance (GSAP timeline, delay 0.2s after DOMContentLoaded)
```js
gsap.timeline({ delay: 0.2 })
  .from(".hero-word",  { y: 60, opacity: 0, stagger: 0.08, duration: 1,   ease: "power4.out" })
  .from(".hero-price", { x: 80, opacity: 0,                duration: 1,   ease: "back.out(1.7)" }, "-=0.6")
  .from(".hero-cta",   { y: 20, opacity: 0, stagger: 0.1,  duration: 0.7, ease: "power3.out"    }, "-=0.5");
```

### Mouse-Parallax Orbs (2 orbs behind hero)
```js
const orbs = document.querySelectorAll(".hero-orb");
window.addEventListener("mousemove", e => {
  const dx = e.clientX / window.innerWidth  - 0.5;
  const dy = e.clientY / window.innerHeight - 0.5;
  orbs.forEach((o, i) => gsap.to(o, { x: dx*(i+1)*40, y: dy*(i+1)*30, duration: 1.2, ease: "power1.out" }));
});
```

### Feature Spotlight Pin (S3) — Apple-style
```js
ScrollTrigger.create({
  trigger: "#feature-spotlight", pin: true, anticipatePin: 1, scrub: 0.6,
  start: "top top", end: () => "+=" + 4 * window.innerHeight * 0.75,
  onUpdate(self) {
    const idx = Math.min(Math.floor(self.progress * 4), 3);
    features.forEach((f, i) => gsap.to(f, { opacity: i===idx?1:0.2, scale: i===idx?1:0.95, duration: 0.35 }));
    details .forEach((d, i) => gsap.to(d, { opacity: i===idx?1:0,   y: i===idx?0:16,       duration: 0.35 }));
  }
});
```

### SVG Checkmark Draw (S4)
```js
document.querySelectorAll(".check-path").forEach((p, i) => {
  const len = p.getTotalLength();
  gsap.set(p, { strokeDasharray: len, strokeDashoffset: len });
  gsap.to(p, { strokeDashoffset: 0, duration: 0.55, ease: "power2.out",
    scrollTrigger: { trigger: p, start: "top 82%", toggleActions: "play none none reverse" },
    delay: i * 0.13 });
});
```

### Timeline SVG Scrub (S5)
```js
const tp = document.querySelector(".timeline-path");
if (tp) {
  const len = tp.getTotalLength();
  gsap.set(tp, { strokeDasharray: len, strokeDashoffset: len });
  gsap.to(tp, { strokeDashoffset: 0, ease: "none",
    scrollTrigger: { trigger: "#timeline-section", start: "top 70%", end: "bottom 30%", scrub: 1 } });
}
```

### Section Entry (scroll reveal, all sections except S1)
```js
gsap.utils.toArray(".section-reveal").forEach(el => {
  gsap.from(el, { y: 40, opacity: 0, duration: 0.9, ease: "power3.out",
    scrollTrigger: { trigger: el, start: "top 80%", toggleActions: "play none none reverse" } });
});
```

### Easing Reference (NO `linear` or `ease-in-out` anywhere)
| Use case | Easing |
|----------|--------|
| Hero text entrance | `power4.out` |
| Price bounce | `back.out(1.7)` |
| CTA / button hover | `cubic-bezier(0.32, 0.72, 0, 1)` |
| Scroll reveals | `power3.out` |
| Accordion open/close | `cubic-bezier(0.4, 0, 0.2, 1)` |
| SVG path draw | `power2.out` |
| Feature spotlight scrub | `none` (scrub handles it) |

### `invalidateOnRefresh: true`
All ScrollTrigger instances that compute height-dependent `end` values MUST use `invalidateOnRefresh: true`
so pinned sections recompute on window resize.

---

## 7. Anti-Patterns (Banned)

- **NO Inter font.** Space Grotesk for body. Fraunces for display. JetBrains Mono for numbers.
- **NO pure black** (`#000000`). Use `#050508` (night) or `#1A1A18` (cozy charcoal) for text.
- **NO neon outer glows in cozy mode.** Accent is solid fill only. No `box-shadow: 0 0 20px [accent]`.
- **NO neon glow on text** in either mode. `text-shadow` glows are banned entirely.
- **NO centered hero.** S1 is always Editorial Split. The only centered full-viewport section is S8 CTA.
- **NO meta-labels** ("SECTION 04", "STEP 01", "FEATURE A"). All headings are content-first.
- **NO gradient text on H1/H2.** Use solid accent colour or solid white/charcoal.
- **NO 3-column equal card grids.** Feature bento must be asymmetric or pinned-scroll.
- **NO `h-screen`** for full-height sections. Always `min-h-[100dvh]`.
- **NO animations on layout-triggering properties** (`top`, `left`, `width`, `height`).
- **NO `backdrop-blur` on scrolling containers.** Only on fixed/sticky nav and overlays.
- **NO grain/noise on scrolling containers.** Grain pseudo-element must be `position: fixed`.
- **NO emojis** anywhere in HTML, copy, or alt text.
- **NO broken image links.** Use `picsum.photos/seed/{keyword}/800/600` for any illustrative images.
- **NO AI copywriting clichés** ("Seamless", "Unleash", "Next-gen", "Game-changing", "Elevate").
- **NO fake round stats** (`99.99%`, `50%`). Use organic numbers (`47 projects`, `5–7 days`).
- **NO Inter, Roboto, Arial, Helvetica** — treated as CDN failure fallbacks, never intentional.
- **NO Lucide, FontAwesome, Material Icons** in thick-stroke form. Use inline SVG with `stroke-width="1.5"`.

---

## 8. Page-Specific Overrides

### launch-site.html
- S5 Timeline: Day 1 → Day 3 → Day 7. Milestones: "Kick-off call", "First draft", "Live"
- S4 Deliverables count: 6 items
- S3 Features: Speed · Scope Lock · Mobile-first · Analytics
- Promise headline (S8): "Your site, live before Monday."

### hermes-agent.html
- S5 Timeline: Week 1 → Week 2 → Ongoing. Milestones: "Agent config", "Integration", "Handoff + support"
- S4 Deliverables count: 5 items (configured agent, wrapper UI, CRM sync, email triage, docs)
- S3 Features: Lead Qualification · Email Triage · CRM Sync · Tier-1 Support
- Promise headline (S8): "Your first digital employee, deployed."
- Accent: Purple `#bf00ff` night / `#5B3A8C` cozy

### ecommerce-wp.html
- S5 Timeline: Week 1 → Week 2–3 → Week 4. Milestones: "Store scaffold", "Products + payments", "Hermes wired"
- S4 Deliverables count: 6 items
- S3 Features: WooCommerce · Payment Stack · Hermes Cart Recovery · Mobile Checkout
- Promise headline (S8): "A store that sells while you sleep."
- Accent: Amber `#f59e0b` night / `#D97706` cozy

### custom-premium.html
- S5 Timeline: Week 1 → Weeks 2–4 → Delivery. Milestones: "Deep-dive call", "Build sprint", "Handoff"
- S4 Deliverables count: 5 items (bespoke design, full Hermes integration, CMS, docs, 60-day support)
- S3 Features: No Templates · Full Hermes AI · Bespoke UX · 60-day Support
- Promise headline (S8): "Built for your brand. Runs on intelligence."
- Accent: Cobalt `#0066ff` night / `#1D4ED8` cozy
