"""Build fixed-language Camelot Flows HTML without changing the English URL structure."""

from __future__ import annotations

import json
import re
import subprocess
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup


BASE_URL = "https://camelotflows.dev"
LANGUAGES = ("en", "ro", "ru")
HTML_VOID_ELEMENTS = "area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr"
PUBLIC_TOP_LEVEL = (
    "index.html",
    "audit.html",
    "about.html",
    "arsenal.html",
    "merlin.html",
    "case-studies.html",
    "for-agencies.html",
    "contact.html",
    "work-with-me.html",
    "service-creation.html",
    "service-maintenance.html",
    "service-automation.html",
    "service-marketing.html",
    "launch-site.html",
    "merlin-automation.html",
    "ecommerce-wp.html",
    "custom-premium.html",
    "legal.html",
    "privacy.html",
    "quote-to-order.html",
    "websites.html",
    "industries/technical-distributors.html",
    "industries/hvac-refrigeration.html",
)


def _route_for(root: Path, source: Path) -> str:
    rel = source.relative_to(root).as_posix()
    if rel == "index.html":
        return "/"
    if source.parent == root:
        return f"/{source.stem}"
    if rel.endswith(".html") and not rel.startswith("blog/"):
        return f"/{rel[:-5]}"
    if rel == "blog/index.html":
        return "/blog/"
    if rel.startswith("blog/") and rel.endswith("/index.html"):
        return f"/{PurePosixPath(rel).parent.as_posix()}/"
    raise ValueError(f"Unsupported public HTML source: {rel}")


def _output_for(root: Path, source: Path, lang: str) -> Path:
    rel = source.relative_to(root)
    if rel == Path("index.html"):
        return root / lang / "index.html"
    if source.parent == root:
        return root / lang / source.name
    return root / lang / rel


def _localized_route(route: str, lang: str) -> str:
    if lang == "en":
        return route
    if route == "/":
        return f"/{lang}/"
    return f"/{lang}{route}"


def _absolute(route: str) -> str:
    return f"{BASE_URL}{route}"


def _load_locales(root: Path) -> dict:
    script = (
        "const fs=require('fs'),vm=require('vm');"
        "const c={window:{}};vm.createContext(c);"
        "vm.runInContext(fs.readFileSync('assets/js/locales.js','utf8'),c);"
        "process.stdout.write(JSON.stringify(c.window.cfLocales));"
    )
    result = subprocess.run(
        ["node", "-e", script],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return json.loads(result.stdout)


def _lookup(dictionary: dict, dotted_key: str):
    node = dictionary
    for part in dotted_key.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node if isinstance(node, str) and node else None


def _public_sources(root: Path) -> list[Path]:
    top = [root / name for name in PUBLIC_TOP_LEVEL if (root / name).exists()]
    blog = list((root / "blog").glob("index.html")) + list((root / "blog").glob("*/index.html"))
    return sorted(set(top + blog))


def _read_sidecar(root: Path) -> dict:
    path = root / "tools" / "seo-content" / "blog-translations.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _write_sidecar(root: Path, sidecar: dict) -> None:
    path = root / "tools" / "seo-content" / "blog-translations.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(sidecar, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _serialize_html(soup: BeautifulSoup) -> str:
    """Use one stable HTML spelling for void elements across repeated parses."""
    html = re.sub(rf"<({HTML_VOID_ELEMENTS})(\b[^<>]*?)/>", r"<\1\2>", str(soup), flags=re.IGNORECASE)
    return re.sub(r"(?m)^[ \t]+$", "", html)


def _capture_and_strip_blog_translations(root: Path, source: Path, text: str, sidecar: dict) -> tuple[str, bool]:
    key = source.relative_to(root).as_posix()
    soup = BeautifulSoup(text, "html.parser")
    nodes = {lang: soup.find_all(attrs={"data-lang-content": lang}) for lang in LANGUAGES}
    has_live_translations = (
        bool(nodes["en"])
        and len(nodes["en"]) == len(nodes["ro"]) == len(nodes["ru"])
        and all(sum(len(node.get_text(" ", strip=True)) for node in nodes[lang]) >= 100 for lang in ("ro", "ru"))
    )
    if has_live_translations:
        sidecar[key] = [
            {lang: str(nodes[lang][index]) for lang in LANGUAGES}
            for index in range(len(nodes["en"]))
        ]
    groups = sidecar.get(key, [])
    if not groups:
        return text, False

    english_nodes = soup.find_all(attrs={"data-lang-content": "en"})
    for index, node in enumerate(english_nodes):
        node.attrs.pop("data-lang-content", None)
        node.attrs.pop("hidden", None)
        node["data-cf-translation-group"] = str(index)
    for lang in ("ro", "ru"):
        for node in soup.find_all(attrs={"data-lang-content": lang}):
            node.decompose()
    return _serialize_html(soup), True


def _rewrite_known_html_urls(text: str, filename_routes: dict[str, str]) -> str:
    for filename, route in sorted(filename_routes.items(), key=lambda item: len(item[0]), reverse=True):
        pattern = re.compile(rf"(?:(?:\.\./)+|/)?{re.escape(filename)}", re.IGNORECASE)
        text = pattern.sub(route, text)
    return text


def _set_fixed_html_language(text: str, lang: str) -> str:
    def replace(match: re.Match) -> str:
        tag = match.group(0)
        tag = re.sub(r'\blang=["\'][^"\']*["\']', f'lang="{lang}"', tag, count=1)
        if "data-cf-static-lang=" in tag:
            tag = re.sub(r'\bdata-cf-static-lang=["\'][^"\']*["\']', f'data-cf-static-lang="{lang}"', tag, count=1)
        else:
            tag = tag[:-1] + f' data-cf-static-lang="{lang}">'
        return tag

    text = re.sub(r"<html\b[^>]*>", replace, text, count=1, flags=re.IGNORECASE)
    text = text.replace("var l = localStorage.getItem('cf_lang') || 'en';", "var l = document.documentElement.lang || 'en';")
    return text


def _hreflang_markup(route: str, available: tuple[str, ...]) -> str:
    rows = [f'<link rel="alternate" hreflang="{lang}" href="{_absolute(_localized_route(route, lang))}">' for lang in available]
    rows.append(f'<link rel="alternate" hreflang="x-default" href="{_absolute(route)}">')
    return "\n    ".join(rows)


def _set_canonical_and_hreflang(text: str, route: str, lang: str, available: tuple[str, ...]) -> str:
    text = re.sub(r"\s*<link\b[^>]*\bhreflang=[\"'][^\"']+[\"'][^>]*>", "", text, flags=re.IGNORECASE)
    canonical = _absolute(_localized_route(route, lang))
    canonical_tag = f'<link rel="canonical" href="{canonical}">'
    if re.search(r"<link\b[^>]*\brel=[\"']canonical[\"'][^>]*>", text, flags=re.IGNORECASE):
        text = re.sub(r"<link\b[^>]*\brel=[\"']canonical[\"'][^>]*>", canonical_tag, text, count=1, flags=re.IGNORECASE)
    else:
        text = text.replace("</head>", f"    {canonical_tag}\n</head>", 1)
    return text.replace(canonical_tag, f"{canonical_tag}\n    {_hreflang_markup(route, available)}", 1)


def _set_language_links(text: str, route: str, available: tuple[str, ...]) -> str:
    for lang in LANGUAGES:
        pattern = re.compile(
            rf"<li(?P<attrs>[^>]*\bdata-lang=[\"']{lang}[\"'][^>]*)>(?P<body>[\s\S]*?)</li>",
            re.IGNORECASE,
        )
        if lang not in available:
            text = pattern.sub("", text)
            continue
        href = _localized_route(route, lang)

        def replace(match: re.Match) -> str:
            attrs = match.group("attrs")
            label = BeautifulSoup(match.group("body"), "html.parser").get_text(" ", strip=True) or lang.upper()
            return f'<li{attrs}><a href="{href}" hreflang="{lang}">{label}</a></li>'

        text = pattern.sub(replace, text)
    return text


def _normalize_english(text: str, route: str, available: tuple[str, ...], filename_routes: dict[str, str]) -> str:
    text = _rewrite_known_html_urls(text, filename_routes)
    text = _set_fixed_html_language(text, "en")
    text = _set_canonical_and_hreflang(text, route, "en", available)
    text = _set_language_links(text, route, available)
    return text


def _replace_translation_groups(soup: BeautifulSoup, groups: list[dict], lang: str) -> None:
    for node in soup.select("[data-cf-translation-group]"):
        index = int(node["data-cf-translation-group"])
        if index >= len(groups) or lang not in groups[index]:
            continue
        replacement = BeautifulSoup(groups[index][lang], "html.parser").find()
        if replacement:
            replacement.attrs.pop("data-lang-content", None)
            replacement.attrs.pop("hidden", None)
            node.replace_with(replacement)


def _set_node_value(node, value: str) -> None:
    if value.startswith("html:"):
        fragment = BeautifulSoup(value[5:], "html.parser")
        node.clear()
        for child in list(fragment.contents):
            node.append(child)
    else:
        node.string = value


def _apply_dictionary(soup: BeautifulSoup, dictionary: dict) -> None:
    for node in soup.select("[data-i18n]"):
        value = _lookup(dictionary, node.get("data-i18n", ""))
        if value is not None:
            _set_node_value(node, value)
    for node in soup.select("[data-i18n-attr]"):
        for pair in node.get("data-i18n-attr", "").split(";"):
            if ":" not in pair:
                continue
            attr, key = (part.strip() for part in pair.split(":", 1))
            value = _lookup(dictionary, key)
            if value is not None:
                node[attr] = value


PRIMARY_NAV = {
    "common.nav.home": "/quote-to-order",
    "common.nav.services": "/industries/technical-distributors",
    "common.nav.arsenal": "/case-studies",
    "common.nav.merlin": "/websites",
    "common.nav.cases": "/about",
    "common.nav.contact": "/contact",
    "common.nav.summon_agent": "/contact",
}


def _set_primary_nav(text: str, lang: str, dictionary: dict) -> str:
    """Change navigation destinations and labels without changing its classes or behavior."""
    soup = BeautifulSoup(text, "html.parser")
    for key, route in PRIMARY_NAV.items():
        value = _lookup(dictionary, key)
        for node in soup.select(f'[data-i18n="{key}"]'):
            anchor = node if node.name == "a" else node.find_parent("a")
            if anchor:
                anchor["href"] = _localized_route(route, lang)
            if value:
                _set_node_value(node, value)
    for key in ("common.nav.agencies", "common.nav.pricing"):
        for node in soup.select(f'[data-i18n="{key}"]'):
            anchor = node if node.name == "a" else node.find_parent("a")
            (anchor or node).decompose()
    return _serialize_html(soup)


def _is_static_resource(value: str) -> bool:
    path = urlsplit(value).path
    return path.startswith("/assets/") or path.startswith("assets/") or "/assets/" in path or path.endswith(("favicon.ico", "favicon.png", "apple-touch-icon.png"))


def _localize_links(soup: BeautifulSoup, lang: str, available_by_route: dict[str, tuple[str, ...]]) -> None:
    known_routes = sorted(available_by_route, key=len, reverse=True)
    html_aliases = {f"{route}.html": route for route in known_routes if route != "/" and not route.endswith("/")}
    html_aliases["/index.html"] = "/"
    for node in soup.find_all(True):
        for attr in ("href", "src", "poster", "action"):
            value = node.get(attr)
            if not value or value.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
                continue
            if attr == "href" and node.has_attr("hreflang"):
                continue
            if _is_static_resource(value):
                marker = value.find("assets/")
                node[attr] = "/" + value[marker:] if marker >= 0 else "/" + value.lstrip("/")
                continue
            parts = urlsplit(value)
            if parts.scheme and parts.netloc and parts.netloc != "camelotflows.dev":
                continue
            candidate = parts.path or "/"
            if not candidate.startswith("/"):
                candidate = f"/{candidate}"
            candidate = html_aliases.get(candidate, candidate)
            matched = next((route for route in known_routes if candidate == route), None)
            if matched and lang in available_by_route[matched]:
                node[attr] = urlunsplit(("", "", _localized_route(matched, lang), parts.query, parts.fragment))
        if node.has_attr("style"):
            node["style"] = re.sub(r"url\((['\"]?)assets/", r"url(\1/assets/", node["style"])
        if node.has_attr("srcset"):
            items = []
            for item in node["srcset"].split(","):
                parts = item.strip().split(maxsplit=1)
                value = parts[0]
                if _is_static_resource(value):
                    marker = value.find("assets/")
                    value = "/" + value[marker:] if marker >= 0 else "/" + value.lstrip("/")
                items.append(" ".join((value, parts[1])) if len(parts) == 2 else value)
            node["srcset"] = ", ".join(items)
    for style in soup.find_all("style"):
        if style.string:
            style.string.replace_with(re.sub(r"url\((['\"]?)assets/", r"url(\1/assets/", style.string))


def _set_localized_metadata(soup: BeautifulSoup, dictionary: dict, page_slug: str | None) -> None:
    title = _lookup(dictionary, f"pages.{page_slug}.meta_title") if page_slug else None
    description = _lookup(dictionary, f"pages.{page_slug}.meta_description") if page_slug else None
    if not title:
        heading = soup.find("h1")
        if heading:
            title = f"{heading.get_text(' ', strip=True)} | Camelot Flows"
    if not description:
        paragraph = soup.select_one("main p, article p, [role=main] p")
        if paragraph:
            description = paragraph.get_text(" ", strip=True)[:160].rstrip()
    if title:
        if soup.title:
            soup.title.string = title
        for selector in ('meta[property="og:title"]', 'meta[name="twitter:title"]'):
            node = soup.select_one(selector)
            if node:
                node["content"] = title
    if description:
        for selector in ('meta[name="description"]', 'meta[property="og:description"]', 'meta[name="twitter:description"]'):
            node = soup.select_one(selector)
            if node:
                node["content"] = description


def _localize_schema_url(value: str, lang: str, available_by_route: dict[str, tuple[str, ...]]) -> str:
    parts = urlsplit(value)
    if parts.netloc not in ("", "camelotflows.dev"):
        return value
    if parts.fragment in ("organization", "alexandru-buzi"):
        return value
    route = parts.path or "/"
    if route in available_by_route and lang in available_by_route[route]:
        return urlunsplit((parts.scheme, parts.netloc, _localized_route(route, lang), parts.query, parts.fragment))
    return value


def _localize_schema(
    soup: BeautifulSoup,
    lang: str,
    available_by_route: dict[str, tuple[str, ...]],
    dictionary: dict,
    page_slug: str | None,
    route: str,
) -> None:
    def rewrite(node, key: str | None = None):
        if isinstance(node, dict):
            for child_key, child in list(node.items()):
                node[child_key] = rewrite(child, child_key)
            return node
        if isinstance(node, list):
            return [rewrite(child, key) for child in node]
        if isinstance(node, str) and key in ("url", "@id", "item"):
            return _localize_schema_url(node, lang, available_by_route)
        return node

    for script in soup.select('script[type="application/ld+json"]'):
        try:
            payload = json.loads(script.string or script.get_text())
        except json.JSONDecodeError:
            continue
        payload = rewrite(payload)
        if isinstance(payload, dict):
            payload["inLanguage"] = lang
        localized_url = _absolute(_localized_route(route, lang))
        title = _lookup(dictionary, f"pages.{page_slug}.meta_title") if page_slug else None
        description = _lookup(dictionary, f"pages.{page_slug}.meta_description") if page_slug else None

        def update_service(node):
            if isinstance(node, dict):
                types = node.get("@type", [])
                types = types if isinstance(types, list) else [types]
                if "Service" in types:
                    node["@id"] = f"{localized_url}#service"
                    node["url"] = localized_url
                    if title:
                        node["name"] = re.sub(r"\s*\|\s*Camelot Flows$", "", title)
                    if description:
                        node["description"] = description
                    node["provider"] = {"@id": f"{BASE_URL}/#organization"}
                    node["areaServed"] = [
                        {"@type": "Country", "name": "Moldova"},
                        {"@type": "Country", "name": "Romania"},
                    ]
                for child in node.values():
                    update_service(child)
            elif isinstance(node, list):
                for child in node:
                    update_service(child)

        update_service(payload)
        script.string = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def _read_sitemap_lastmods(root: Path) -> dict[str, str]:
    path = root / "sitemap.xml"
    if not path.exists():
        return {}
    try:
        tree = ET.parse(path)
    except (ET.ParseError, OSError):
        return {}
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    values: dict[str, str] = {}
    for node in tree.findall("sm:url", namespace):
        loc = node.findtext("sm:loc", default="", namespaces=namespace).strip()
        lastmod = node.findtext("sm:lastmod", default="", namespaces=namespace).strip()
        if loc and lastmod:
            values[loc] = lastmod
    return values


def _write_sitemap(root: Path, available_by_route: dict[str, tuple[str, ...]], previous_lastmods: dict[str, str]) -> None:
    rows = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    created_lastmod = date.today().isoformat()
    for route in sorted(available_by_route, key=lambda item: (item != "/", item)):
        for lang in available_by_route[route]:
            localized = _localized_route(route, lang)
            absolute = _absolute(localized)
            lastmod = previous_lastmods.get(absolute, created_lastmod)
            rows.extend(("  <url>", f"    <loc>{absolute}</loc>", f"    <lastmod>{lastmod}</lastmod>", "  </url>"))
    rows.append("</urlset>")
    (root / "sitemap.xml").write_text("\n".join(rows) + "\n", encoding="utf-8")


def _render_localized(
    english_text: str,
    route: str,
    lang: str,
    available: tuple[str, ...],
    available_by_route: dict[str, tuple[str, ...]],
    dictionary: dict,
    translation_groups: list[dict],
) -> str:
    soup = BeautifulSoup(english_text, "html.parser")
    soup.html["lang"] = lang
    soup.html["data-cf-static-lang"] = lang
    _replace_translation_groups(soup, translation_groups, lang)
    _apply_dictionary(soup, dictionary)
    _set_localized_metadata(soup, dictionary, soup.html.get("data-i18n-page"))
    _localize_links(soup, lang, available_by_route)
    _localize_schema(soup, lang, available_by_route, dictionary, soup.html.get("data-i18n-page"), route)

    canonical = soup.select_one('link[rel="canonical"]')
    if canonical:
        canonical["href"] = _absolute(_localized_route(route, lang))
    for link in list(soup.select('link[rel="alternate"][hreflang]')):
        link.decompose()
    anchor = canonical or soup.head.find()
    for code in (*available, "x-default"):
        link = soup.new_tag("link")
        link["rel"] = "alternate"
        link["hreflang"] = code
        link["href"] = _absolute(route if code == "x-default" else _localized_route(route, code))
        anchor.insert_after(link)
        anchor = link
    return _serialize_html(soup)


def build_site(root: Path | str) -> dict:
    root = Path(root).resolve()
    previous_lastmods = _read_sitemap_lastmods(root)
    locales = _load_locales(root)
    sources = _public_sources(root)
    filename_routes = {source.name: _route_for(root, source) for source in sources if source.parent == root}
    sidecar = _read_sidecar(root)
    source_text: dict[Path, str] = {}
    available_by_route: dict[str, tuple[str, ...]] = {}

    for source in sources:
        text = source.read_text(encoding="utf-8")
        translated = False
        if source.relative_to(root).as_posix().startswith("blog/"):
            text, translated = _capture_and_strip_blog_translations(root, source, text, sidecar)
        route = _route_for(root, source)
        available = LANGUAGES if not source.relative_to(root).as_posix().startswith("blog/") or translated else ("en",)
        if source.relative_to(root).as_posix() == "blog/index.html" and translated:
            available = LANGUAGES
        available_by_route[route] = available
        source_text[source] = text

    _write_sidecar(root, sidecar)
    generated = []
    for source in sources:
        route = _route_for(root, source)
        available = available_by_route[route]
        english = _normalize_english(source_text[source], route, available, filename_routes)
        english = _set_primary_nav(english, "en", locales["en"])
        source.write_text(english, encoding="utf-8")
        groups = sidecar.get(source.relative_to(root).as_posix(), [])
        for lang in ("ro", "ru"):
            if lang not in available:
                continue
            output = _output_for(root, source, lang)
            output.parent.mkdir(parents=True, exist_ok=True)
            rendered = _render_localized(english, route, lang, available, available_by_route, locales[lang], groups)
            rendered = _set_primary_nav(rendered, lang, locales[lang])
            output.write_text(rendered, encoding="utf-8")
            generated.append(output.relative_to(root).as_posix())

    _write_sitemap(root, available_by_route, previous_lastmods)
    return {"generated": sorted(generated), "routes": len(available_by_route)}


if __name__ == "__main__":
    report = build_site(Path(__file__).resolve().parents[1])
    print(json.dumps(report, indent=2))
