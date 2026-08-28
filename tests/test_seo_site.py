import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://camelotflows.dev"
LANGS = ("en", "ro", "ru")
PUBLIC_TOP_LEVEL = (
    "index.html", "audit.html", "about.html", "arsenal.html", "merlin.html", "case-studies.html", "quote-to-order.html", "websites.html",
    "for-agencies.html", "contact.html", "work-with-me.html", "service-creation.html",
    "service-maintenance.html", "service-automation.html", "service-marketing.html", "launch-site.html",
    "merlin-automation.html", "ecommerce-wp.html", "custom-premium.html", "legal.html", "privacy.html",
)


def route_for(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if path.parent == ROOT:
        return f"/{path.stem}"
    if rel == "blog/index.html":
        return "/blog/"
    if rel in ("industries/technical-distributors.html", "industries/hvac-refrigeration.html"):
        return f"/{path.parent.name}/{path.stem}"
    return f"/{path.parent.relative_to(ROOT).as_posix()}/"


def localized_route(route: str, lang: str) -> str:
    if route == "/":
        return f"/{lang}/"
    return f"/{lang}{route}"


def english_sources():
    top = [ROOT / name for name in PUBLIC_TOP_LEVEL]
    blog = list((ROOT / "blog").glob("index.html")) + list((ROOT / "blog").glob("*/index.html"))
    industries = list((ROOT / "industries").glob("*.html"))
    return sorted(set(top + blog + industries))


def localized_path(source: Path, lang: str) -> Path:
    rel = source.relative_to(ROOT)
    if rel == Path("index.html"):
        return ROOT / lang / "index.html"
    if source.parent == ROOT:
        return ROOT / lang / source.name
    return ROOT / lang / rel


class SeoSiteContractTests(unittest.TestCase):
    def test_all_first_party_static_resources_exist_locally(self):
        failures = []
        pages = english_sources()
        pages.extend(localized_path(source, lang) for source in english_sources() for lang in ("ro", "ru") if localized_path(source, lang).exists())
        pages.append(ROOT / "work" / "ambienti" / "index.html")
        resource_suffixes = (".css", ".js", ".png", ".jpg", ".jpeg", ".webp", ".svg", ".ico", ".woff", ".woff2", ".webm", ".mp4")
        for page in pages:
            soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
            candidates = []
            for node in soup.select("[src], link[href]"):
                candidates.append(node.get("src") or node.get("href"))
            for node in soup.select("[srcset]"):
                candidates.extend(item.strip().split()[0] for item in node["srcset"].split(","))
            for value in candidates:
                parts = urlsplit(value)
                if parts.scheme or parts.netloc or not parts.path.lower().endswith(resource_suffixes):
                    continue
                target = ROOT / parts.path.lstrip("/") if parts.path.startswith("/") else page.parent / parts.path
                if not target.resolve().is_file():
                    failures.append(f"{page.relative_to(ROOT)} -> missing {value}")
        self.assertEqual(failures, [])

    def test_english_pages_have_direct_internal_links_and_crawlable_language_urls(self):
        failures = []
        for source in english_sources():
            soup = BeautifulSoup(source.read_text(encoding="utf-8"), "html.parser")
            route = route_for(source)
            supported = ("en",) if "ai-intake-assistant" in source.as_posix() else LANGS
            for node in soup.select("a[href], link[rel=\"prefetch\"][href], link[rel=\"preload\"][as=\"document\"][href]"):
                href = node.get("href", "")
                if ".html" in urlsplit(href).path and not urlsplit(href).netloc:
                    failures.append(f"{source.relative_to(ROOT)} -> redirecting internal href {href}")
            options = soup.select(".lang-menu [data-lang]")
            option_map = {node["data-lang"]: node.find("a", href=True)["href"] if node.find("a", href=True) else None for node in options}
            if not option_map:
                option_map = {node.get("hreflang"): node.get("href") for node in soup.select(".language-links a[hreflang]")}
            expected = {lang: localized_route(route, lang) if lang != "en" else route for lang in supported}
            if option_map != expected:
                failures.append(f"{source.relative_to(ROOT)} language links {option_map} != {expected}")
        self.assertEqual(failures, [])

    def test_localized_pages_are_fixed_language_self_canonical_and_reciprocal(self):
        failures = []
        for source in english_sources():
            route = route_for(source)
            supported = ("en",) if "ai-intake-assistant" in source.as_posix() else LANGS
            for lang in ("ro", "ru"):
                target = localized_path(source, lang)
                if lang not in supported:
                    if target.exists():
                        failures.append(f"unsupported translation exists: {target.relative_to(ROOT)}")
                    continue
                if not target.exists():
                    failures.append(f"missing {target.relative_to(ROOT)}")
                    continue
                soup = BeautifulSoup(target.read_text(encoding="utf-8"), "html.parser")
                canonical = soup.select('link[rel="canonical"]')
                expected_url = f"{BASE}{localized_route(route, lang)}"
                if soup.html.get("lang") != lang or soup.html.get("data-cf-static-lang") != lang:
                    failures.append(f"{target.relative_to(ROOT)} fixed lang")
                if len(canonical) != 1 or canonical[0].get("href") != expected_url:
                    failures.append(f"{target.relative_to(ROOT)} canonical")
                if not soup.title or not soup.select_one('meta[name="description"]') or len(soup.find_all("h1")) != 1:
                    failures.append(f"{target.relative_to(ROOT)} title/description/H1")
                alternates = {link.get("hreflang"): link.get("href") for link in soup.select('link[rel="alternate"][hreflang]')}
                expected_alternates = {code: f"{BASE}{route if code == 'x-default' else (route if code == 'en' else localized_route(route, code))}" for code in (*supported, "x-default")}
                if alternates != expected_alternates:
                    failures.append(f"{target.relative_to(ROOT)} hreflang {alternates}")
                if soup.select("[data-lang-content]"):
                    failures.append(f"{target.relative_to(ROOT)} contains other language bodies")
                language_links = {link.get("hreflang"): link.get("href") for link in soup.select(".lang-menu a[hreflang], .language-links a[hreflang]")}
                expected_language_links = {code: (route if code == "en" else localized_route(route, code)) for code in supported}
                if language_links != expected_language_links:
                    failures.append(f"{target.relative_to(ROOT)} language links {language_links}")
                for node in soup.select("[src], link[href]"):
                    value = node.get("src") or node.get("href") or ""
                    if value.startswith("assets/") or value.startswith("../assets/"):
                        failures.append(f"{target.relative_to(ROOT)} relative asset {value}")
        self.assertEqual(failures, [])

    def test_json_ld_is_valid_and_uses_final_urls(self):
        failures = []
        for source in english_sources():
            soup = BeautifulSoup(source.read_text(encoding="utf-8"), "html.parser")
            for node in soup.select('script[type="application/ld+json"]'):
                try:
                    payload = json.loads(node.string or node.get_text())
                except json.JSONDecodeError as error:
                    failures.append(f"{source.relative_to(ROOT)} invalid JSON-LD: {error}")
                    continue
                if ".html" in json.dumps(payload):
                    failures.append(f"{source.relative_to(ROOT)} JSON-LD references redirecting .html URL")
        self.assertEqual(failures, [])

    def test_sitemap_contains_only_expected_canonical_language_pages(self):
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = [node.text for node in ET.parse(ROOT / "sitemap.xml").findall("sm:url/sm:loc", namespace)]
        expected = []
        for source in english_sources():
            route = route_for(source)
            expected.append(f"{BASE}{route}")
            if "ai-intake-assistant" not in source.as_posix():
                expected.extend(f"{BASE}{localized_route(route, lang)}" for lang in ("ro", "ru"))
        self.assertEqual(set(urls), set(expected))
        self.assertEqual(len(urls), len(set(urls)))
        self.assertNotIn(f"{BASE}/work/ambienti/", urls)

    def test_ambienti_preview_is_noindex_and_excluded_from_sitemap(self):
        preview = ROOT / "work" / "ambienti" / "index.html"
        self.assertTrue(preview.exists())
        soup = BeautifulSoup(preview.read_text(encoding="utf-8"), "html.parser")
        self.assertRegex(soup.select_one('meta[name="robots"]')["content"], r"\bnoindex\b")
        self.assertIn("WooCommerce", soup.get_text(" ", strip=True))


if __name__ == "__main__":
    unittest.main()
