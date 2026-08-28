# Legacy blog redirect configuration

The legacy source is outside this repository. Public verification on 2026-08-28 found:

- the old blog homepage and 11 known slash-terminated article URLs redirect once with 301 to their matching canonical apex URL, then return 200;
- no-slash old article variants take two hops because the apex adds the canonical slash;
- sampled category, feed, author, and pagination paths redirect once to an apex path that truthfully returns 404.

Keep the old hostname active as a redirect source for at least 12 months after the last migration change. Do not redirect unrelated paths to `/` or `/blog/`.

## Preferred Cloudflare configuration

Create Bulk Redirects for the known no-slash variants first. Each entry is a static 301 with query strings removed:

```text
https://blog.camelotflows.dev/ai-intake-assistant-small-service-business -> https://camelotflows.dev/blog/ai-intake-assistant-small-service-business/
https://blog.camelotflows.dev/automate-import-back-office-before-hiring -> https://camelotflows.dev/blog/automate-import-back-office-before-hiring/
https://blog.camelotflows.dev/building-dreamscape-in-parallel -> https://camelotflows.dev/blog/building-dreamscape-in-parallel/
https://blog.camelotflows.dev/do-i-own-my-website-checklist -> https://camelotflows.dev/blog/do-i-own-my-website-checklist/
https://blog.camelotflows.dev/how-chatgpt-decides-which-local-businesses-to-recommend -> https://camelotflows.dev/blog/how-chatgpt-decides-which-local-businesses-to-recommend/
https://blog.camelotflows.dev/how-i-build-sites-for-clients -> https://camelotflows.dev/blog/how-i-build-sites-for-clients/
https://blog.camelotflows.dev/how-i-build-websites-for-e390-the-starter-page-breakdown -> https://camelotflows.dev/blog/how-i-build-websites-for-e390-the-starter-page-breakdown/
https://blog.camelotflows.dev/how-to-leave-your-web-agency-without-losing-your-website -> https://camelotflows.dev/blog/how-to-leave-your-web-agency-without-losing-your-website/
https://blog.camelotflows.dev/why-is-my-new-website-not-showing-up-on-google -> https://camelotflows.dev/blog/why-is-my-new-website-not-showing-up-on-google/
https://blog.camelotflows.dev/why-wordpress-slow-on-mobile -> https://camelotflows.dev/blog/why-wordpress-slow-on-mobile/
```

Keep the current hostname rule after those exact entries:

```text
Expression:
  (http.host eq "blog.camelotflows.dev")

Dynamic destination:
  concat("https://camelotflows.dev/blog", http.request.uri.path)

Status: 301
Preserve query string: off
```

The hostname rule deliberately preserves unknown paths. It allows the final apex URL to return a truthful 404 instead of consolidating unrelated historical URLs into the homepage.

Before changing taxonomy/feed/attachment behavior, export historical URLs and backlinks from Search Console or another authenticated source. Map any valuable URL one-to-one; use 404/410 only when no close replacement or retained value exists.

