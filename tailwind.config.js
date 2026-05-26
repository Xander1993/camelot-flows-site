/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./wp-theme/camelot-flows/**/*.php",
    "./assets/js/**/*.js",
    "./assets/site.js",
  ],
  // Safelist only classes added dynamically by JS at runtime (not in HTML source).
  safelist: [
    "cf-skip-preloader",
    "cf-cursor",
    "is-hover",
    "scroll-progress",
    "theme-toggle",
    "icon-cozy",
    "icon-night",
    // Custom token colors used via data-theme variants in JS/dynamic contexts
    {
      pattern: /(bg|text|border|from|to)-(primary|primary-glow|accent|cobalt|sage|terracotta|charcoal|candle|parchment|obsidian|obsidian-light)(\/.+)?/,
    },
    // Only the specific Tailwind color classes injected by locales.js
    "text-emerald-400",
    "text-indigo-400",
  ],
  theme: {
    extend: {
      colors: {
        // CSS-variable based colors — resolve via --cft-* tokens in camelot.css.
        // Night mode: :root defaults (neon). Cozy mode: [data-theme="cozy"] overrides.
        "primary":         "rgb(var(--cft-primary) / <alpha-value>)",
        "primary-glow":    "rgb(var(--cft-primary-glow) / <alpha-value>)",
        "accent":          "rgb(var(--cft-accent) / <alpha-value>)",
        "cobalt":          "rgb(var(--cft-cobalt) / <alpha-value>)",
        "obsidian":        "rgb(var(--cft-obsidian) / <alpha-value>)",
        "obsidian-light":  "rgb(var(--cft-obsidian-light) / <alpha-value>)",
        "parchment":       "rgb(var(--cft-parchment) / <alpha-value>)",
        "candle":          "rgb(var(--cft-candle) / <alpha-value>)",
        "sage":            "rgb(var(--cft-sage) / <alpha-value>)",
        "terracotta":      "rgb(var(--cft-terracotta) / <alpha-value>)",
        "charcoal":        "rgb(var(--cft-charcoal) / <alpha-value>)",
      },
      fontFamily: {
        "display": ["Fraunces", "Georgia", "serif"],
        "body":    ["Inter", "sans-serif"],
        "mono":    ["JetBrains Mono", "monospace"],
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
      },
      boxShadow: {
        'neon':        '0 4px 20px -4px rgba(196, 120, 92, 0.25), 0 2px 8px -2px rgba(196, 120, 92, 0.12)',
        'neon-strong': '0 6px 30px -6px rgba(196, 120, 92, 0.35)',
      },
    },
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/container-queries"),
  ],
};
