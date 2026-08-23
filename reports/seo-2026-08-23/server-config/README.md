# Pre-SEO production server configuration evidence

- Inspected: 2026-08-23 (Europe/Chisinau)
- Public apex: Cloudflare Pages, deployed from GitHub repository `Xander1993/camelot-flows-site`, production branch `master`
- Legacy `www` and `blog` origin: DigitalOcean VPS `46.101.150.59`, SSH port `8080`
- Web server: Apache 2.4.58 (Ubuntu); nginx is not installed
- Document root: `/var/www/html`
- Enabled blog vhost: `/etc/apache2/sites-enabled/blog.camelotflows.dev.conf`
- WordPress rewrite file: `/var/www/html/.htaccess`
- Existing live old-blog mappings were verified separately as one `301` hop to the matching apex post, then `200`

The adjacent files are read-only pre-change copies retrieved before any production configuration mutation. No server configuration change is planned unless the public validation proves an existing redirect defective.
