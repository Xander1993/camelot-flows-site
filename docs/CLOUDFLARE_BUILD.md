# Cloudflare Pages build contract

## Pinned runtime

- Node.js: `22.16.0`
- npm: the npm version distributed with Node 22.16.0 (`10.9.2` in the verified local run)
- Repository selectors: `.nvmrc`, `.node-version`, and `package.json` `engines.node`

Cloudflare Pages Build System v3 uses Node 22.16.0 by default and supports `.nvmrc`, `.node-version`, or `NODE_VERSION` to override the runtime. Build System v2 also permits a pinned modern Node version even though its old default is Node 18. The repository files therefore make the intended runtime explicit independently of the project's current build-image generation.

## Pages settings

- Production branch: `master` (do not change for this preview)
- Preview branch: `seo-reposition-stabilization`
- Build command: `npm ci && npm run build && npm test`
- Build output directory: `.`
- Recommended environment variable: `NODE_VERSION=22.16.0` (redundant with the repository pins, useful as a dashboard-visible safeguard)

The build is expected to generate the Tailwind/custom CSS bundle and minified JavaScript before running all tests. The second-pass local acceptance run used exactly Node 22.16.0 and npm 10.9.2.

Official references:

- https://developers.cloudflare.com/pages/configuration/build-image/
- https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/
