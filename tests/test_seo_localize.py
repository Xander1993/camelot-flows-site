import json
import tempfile
import unittest
from pathlib import Path

from bs4 import BeautifulSoup


class SeoLocalizationBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "assets" / "js").mkdir(parents=True)
        (self.root / "blog" / "translated-post").mkdir(parents=True)
        (self.root / "blog" / "english-only").mkdir(parents=True)
        locales = {
            "en": {"pages": {"index": {"hero": "English home", "meta_title": "English title", "meta_description": "English description"}, "about": {"hero": "English about", "meta_title": "About", "meta_description": "About description"}}},
            "ro": {"pages": {"index": {"hero": "Acasă în română", "meta_title": "Titlu română", "meta_description": "Descriere română"}, "about": {"hero": "Despre în română", "meta_title": "Despre", "meta_description": "Descriere despre"}}},
            "ru": {"pages": {"index": {"hero": "Главная по-русски", "meta_title": "Русский заголовок", "meta_description": "Русское описание"}, "about": {"hero": "О нас по-русски", "meta_title": "О нас", "meta_description": "Описание"}}},
        }
        locale_js = "window.cfLocales = " + json.dumps(locales, ensure_ascii=False) + ";"
        (self.root / "assets" / "js" / "locales.js").write_text(locale_js, encoding="utf-8")
        switcher = '<ul class="lang-menu"><li role="option" data-lang="en">EN</li><li role="option" data-lang="ro">RO</li><li role="option" data-lang="ru">RU</li></ul>'
        (self.root / "index.html").write_text(
            f'<!doctype html><html lang="en" data-i18n-page="index"><head><title>Old</title><meta name="description" content="Old"><link rel="canonical" href="https://camelotflows.dev/"><link rel="stylesheet" href="assets/site.css"><script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","@id":"https://camelotflows.dev/#organization","url":"https://camelotflows.dev/","inLanguage":"en"}}</script></head><body>{switcher}<main><h1 data-i18n="pages.index.hero">English home</h1><a href="about.html">About</a></main></body></html>',
            encoding="utf-8",
        )
        (self.root / "about.html").write_text(
            f'<!doctype html><html lang="en" data-i18n-page="about"><head><title>About</title><meta name="description" content="About description"><link rel="canonical" href="https://camelotflows.dev/about"></head><body>{switcher}<main><h1 data-i18n="pages.about.hero">English about</h1><img src="assets/about.webp"></main></body></html>',
            encoding="utf-8",
        )
        translated = f'''<!doctype html><html lang="en"><head><title>Translated post</title><meta name="description" content="English post description"><link rel="canonical" href="https://camelotflows.dev/blog/translated-post/"></head><body>{switcher}<article><h1><span data-lang-content="en">English post</span><span data-lang-content="ro" hidden>Articol română</span><span data-lang-content="ru" hidden>Статья по-русски</span></h1><div data-lang-content="en"><p>{'English body ' * 20}</p></div><div data-lang-content="ro" hidden><p>{'Conținut română ' * 20}</p></div><div data-lang-content="ru" hidden><p>{'Русское содержание ' * 20}</p></div></article></body></html>'''
        (self.root / "blog" / "translated-post" / "index.html").write_text(translated, encoding="utf-8")
        english_only = f'''<!doctype html><html lang="en"><head><title>English only</title><meta name="description" content="Only English"><link rel="canonical" href="https://camelotflows.dev/blog/english-only/"></head><body>{switcher}<article><h1>English only</h1><p>{'Only English body ' * 20}</p></article></body></html>'''
        (self.root / "blog" / "english-only" / "index.html").write_text(english_only, encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_build_emits_fixed_language_pages_with_self_canonical_and_reciprocal_hreflang(self):
        from tools.seo_localize import build_site

        report = build_site(self.root)
        ro = BeautifulSoup((self.root / "ro" / "about.html").read_text(encoding="utf-8"), "html.parser")

        self.assertEqual(ro.html["lang"], "ro")
        self.assertEqual(ro.html["data-cf-static-lang"], "ro")
        self.assertEqual(ro.h1.get_text(" ", strip=True), "Despre în română")
        self.assertEqual(ro.title.string, "Despre")
        self.assertEqual(ro.select_one('link[rel="canonical"]')["href"], "https://camelotflows.dev/ro/about")
        alternates = {link["hreflang"]: link["href"] for link in ro.select('link[rel="alternate"][hreflang]')}
        self.assertEqual(alternates, {
            "en": "https://camelotflows.dev/about",
            "ro": "https://camelotflows.dev/ro/about",
            "ru": "https://camelotflows.dev/ru/about",
            "x-default": "https://camelotflows.dev/about",
        })
        self.assertEqual(ro.img["src"], "/assets/about.webp")
        self.assertIn("ro/about.html", report["generated"])
        self.assertTrue((self.root / "sitemap.xml").exists())

    def test_language_options_are_crawlable_links_and_internal_links_use_final_localized_routes(self):
        from tools.seo_localize import build_site

        build_site(self.root)
        english = BeautifulSoup((self.root / "index.html").read_text(encoding="utf-8"), "html.parser")
        ro = BeautifulSoup((self.root / "ro" / "index.html").read_text(encoding="utf-8"), "html.parser")

        english_options = {node["data-lang"]: node.a["href"] for node in english.select('.lang-menu [data-lang]')}
        self.assertEqual(english_options, {"en": "/", "ro": "/ro/", "ru": "/ru/"})
        self.assertEqual(english.select_one('main a')["href"], "/about")
        self.assertEqual(ro.select_one('main a')["href"], "/ro/about")
        self.assertNotIn("localStorage.getItem('cf_lang')", (self.root / "index.html").read_text(encoding="utf-8"))

    def test_blog_outputs_only_selected_language_and_skips_untranslated_articles(self):
        from tools.seo_localize import build_site

        build_site(self.root)
        english = BeautifulSoup((self.root / "blog" / "translated-post" / "index.html").read_text(encoding="utf-8"), "html.parser")
        ro_path = self.root / "ro" / "blog" / "translated-post" / "index.html"
        ro = BeautifulSoup(ro_path.read_text(encoding="utf-8"), "html.parser")

        self.assertIn("English body", english.get_text(" ", strip=True))
        self.assertNotIn("Conținut română", english.get_text(" ", strip=True))
        self.assertIn("Conținut română", ro.get_text(" ", strip=True))
        self.assertNotIn("English body", ro.get_text(" ", strip=True))
        self.assertFalse((self.root / "ro" / "blog" / "english-only" / "index.html").exists())
        self.assertFalse((self.root / "ru" / "blog" / "english-only" / "index.html").exists())
        english_only = BeautifulSoup((self.root / "blog" / "english-only" / "index.html").read_text(encoding="utf-8"), "html.parser")
        self.assertEqual({link["hreflang"] for link in english_only.select('link[hreflang]')}, {"en", "x-default"})

    def test_localized_json_ld_uses_the_localized_canonical(self):
        from tools.seo_localize import build_site

        build_site(self.root)
        ro = BeautifulSoup((self.root / "ro" / "index.html").read_text(encoding="utf-8"), "html.parser")
        payload = json.loads(ro.select_one('script[type="application/ld+json"]').string)
        self.assertEqual(payload["url"], "https://camelotflows.dev/ro/")
        self.assertEqual(payload["inLanguage"], "ro")
        self.assertEqual(payload["@id"], "https://camelotflows.dev/#organization")

    def test_running_the_generator_twice_is_byte_for_byte_deterministic(self):
        from tools.seo_localize import build_site

        build_site(self.root)
        tracked = [self.root / "sitemap.xml", *sorted((self.root / "ro").rglob("*.html")), *sorted((self.root / "ru").rglob("*.html"))]
        first = {path.relative_to(self.root).as_posix(): path.read_bytes() for path in tracked}

        build_site(self.root)
        second = {path.relative_to(self.root).as_posix(): path.read_bytes() for path in tracked}

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
