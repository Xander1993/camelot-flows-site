/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./assets/js/**/*.js",
    "./assets/site.js",
  ],
  // Safelist anything dynamically added by JS or generated arbitrary classes
  // that scanning might miss.
  safelist: [
    "cf-skip-preloader",
    "cf-cursor",
    "is-hover",
    "scroll-progress",
    "theme-toggle",
    "icon-cozy",
    "icon-night",
    {
      pattern: /(bg|text|border|from|to)-(primary|primary-glow|accent|cobalt|sage|terracotta|charcoal|candle|parchment|obsidian|obsidian-light)/,
    },
    {
      pattern: /(bg|text|border)-(slate|indigo|emerald|cyan|black|white)-(\d+)/,
    },
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
