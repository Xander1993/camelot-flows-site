from pathlib import Path
import re
import shutil


ROOT = Path(__file__).resolve().parent
HTML_PATH = ROOT / "index.html"
THEME_DIR = ROOT / "wp-theme" / "camelot-flows"
ASSETS_DIR = THEME_DIR / "assets"
DIST_DIR = ROOT / "dist"
STAGE_DIR = DIST_DIR / "camelot-flows"
PACKAGE_PATH = ROOT / "camelot-flows-theme-cozy.zip"

STATIC_ROUTE_MAP = {
    "index.html": "/",
    "arsenal.html": "/the-arsenal/",
    "merlin.html": "/merlin-protocol/",
    "merlin-protocol.html": "/merlin-protocol/",
    "case-studies.html": "/case-studies/",
    "for-agencies.html": "/for-agencies/",
    "about.html": "/about/",
    "contact.html": "/contact/",
    "service-creation.html": "/service-creation/",
    "service-maintenance.html": "/service-maintenance/",
    "service-automation.html": "/service-automation/",
    "service-marketing.html": "/service-marketing/",
    "work-with-me.html": "/work-with-me/",
    "legal.html": "/legal/",
    "privacy.html": "/privacy/",
    "web-design.html": "/web-design/",
    "automation.html": "/automation/",
    "maintenance.html": "/maintenance/",
    "growth-marketing.html": "/growth-marketing/",
}

PAGE_TEMPLATE_MAP = {
    "arsenal.html": ("page-the-arsenal.php", "The Arsenal"),
    "merlin.html": ("page-merlin-protocol.php", "Merlin Protocol"),
    "case-studies.html": ("page-case-studies.php", "Case Studies"),
    "for-agencies.html": ("page-for-agencies.php", "For Agencies"),
    "about.html": ("page-about.php", "About"),
    "contact.html": ("page-contact.php", "Contact"),
    "work-with-me.html": ("page-work-with-me.php", "Work With Me"),
    "legal.html": ("page-legal.php", "Legal"),
    "privacy.html": ("page-privacy.php", "Privacy"),
    "web-design.html": ("page-web-design.php", "Web Design"),
    "automation.html": ("page-automation.php", "Automation"),
    "maintenance.html": ("page-maintenance.php", "Maintenance"),
    "growth-marketing.html": ("page-growth-marketing.php", "Growth Marketing"),
    "service-creation.html": ("page-service-creation.php", "Service Creation"),
    "service-maintenance.html": ("page-service-maintenance.php", "Service Maintenance"),
    "service-automation.html": ("page-service-automation.php", "Service Automation"),
    "service-marketing.html": ("page-service-marketing.php", "Service Marketing"),
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_if_exists(source: Path, target: Path) -> None:
    if not source.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_tree_if_exists(source: Path, target: Path) -> None:
    if not source.exists():
        return
    shutil.copytree(source, target, dirs_exist_ok=True)


def wp_asset_expression(asset_path: str) -> str:
    return f"<?php echo esc_url(get_template_directory_uri() . '/{asset_path}'); ?>"


def wp_home_expression(route: str) -> str:
    return f"<?php echo esc_url(home_url('{route}')); ?>"


def split_static_ref(ref: str) -> tuple[str, str]:
    for marker in ("#", "?"):
        if marker in ref:
            base, suffix = ref.split(marker, 1)
            return base, marker + suffix
    return ref, ""


def route_for_ref(ref: str) -> str | None:
    base, suffix = split_static_ref(ref)
    route = STATIC_ROUTE_MAP.get(base)
    if route is None:
        return None
    if suffix.startswith("#"):
        return route.rstrip("/") + "/" + suffix if route != "/" else "/" + suffix
    if suffix.startswith("?"):
        return route + suffix.lstrip("?") if route.endswith("?") else route + suffix
    return route


def rewrite_static_href(match: re.Match) -> str:
    quote = match.group(1)
    ref = match.group(2)
    route = route_for_ref(ref)
    if route is None:
        return match.group(0)
    return f'href={quote}{wp_home_expression(route)}{quote}'


def rewrite_onclick_location(match: re.Match) -> str:
    ref = match.group(2)
    route = route_for_ref(ref)
    if route is None:
        return match.group(0)
    return f"window.location.href='{wp_home_expression(route)}'"


def rewrite_asset_refs(content: str) -> str:
    content = re.sub(
        r'(src|href)=("|\')(assets/[^"\']+)(\2)',
        lambda m: f'{m.group(1)}={m.group(2)}{wp_asset_expression(m.group(3))}{m.group(2)}',
        content,
    )
    content = re.sub(
        r'url\((["\']?)(assets/[^)"\']+)\1\)',
        lambda m: f"url({m.group(1)}{wp_asset_expression(m.group(2))}{m.group(1)})",
        content,
    )
    return content


def rewrite_wp_routes(content: str) -> str:
    content = re.sub(
        r'href=(["\'])([^"\']+\.html(?:[?#][^"\']*)?)\1',
        rewrite_static_href,
        content,
    )
    content = re.sub(
        r"window\.location\.href=(\\?['\"])([^'\"]+\.html(?:[?#][^'\"]*)?)(\\?['\"])",
        rewrite_onclick_location,
        content,
    )
    return content


def strip_page_scripts(content: str) -> str:
    return re.sub(r"\s*<script\b[^>]*>.*?</script>\s*", "\n", content, flags=re.DOTALL | re.IGNORECASE)


def extract_content_between_nav_and_footer(html: str, source_name: str) -> str:
    nav_end = html.find("</nav>")
    if nav_end == -1:
        raise ValueError(f"Could not find </nav> in {source_name}")
    nav_end += len("</nav>")

    footer_start = html.find("<footer", nav_end)
    if footer_start == -1:
        raise ValueError(f"Could not find <footer> in {source_name}")
    return html[nav_end:footer_start]


def redirect_template(template_label: str, target_route: str) -> str:
    return f"""<?php
/* Template Name: {template_label} */
wp_safe_redirect(home_url('{target_route}'), 301);
exit;
"""


def redirect_route_from_html(html: str) -> str | None:
    match = re.search(r'http-equiv=["\']refresh["\'][^>]*content=["\'][^"\']*url=([^"\']+)', html, re.IGNORECASE)
    if not match:
        return None
    return route_for_ref(match.group(1).strip())


def prepare_theme_assets() -> None:
    (ASSETS_DIR / "images").mkdir(parents=True, exist_ok=True)
    (ASSETS_DIR / "js").mkdir(parents=True, exist_ok=True)
    (ASSETS_DIR / "css").mkdir(parents=True, exist_ok=True)

    copy_if_exists(ROOT / "assets" / "site.css", ASSETS_DIR / "site.css")
    copy_tree_if_exists(ROOT / "assets" / "css", ASSETS_DIR / "css")
    copy_if_exists(ROOT / "assets" / "site.js", ASSETS_DIR / "site.js")
    copy_if_exists(ROOT / "assets" / "js" / "camelot-gsap.js", ASSETS_DIR / "js" / "camelot-gsap.js")
    copy_tree_if_exists(ROOT / "assets" / "images" / "additional-campaign", ASSETS_DIR / "images" / "additional-campaign")
    copy_tree_if_exists(ROOT / "assets" / "images" / "cozy-freelancer", ASSETS_DIR / "images" / "cozy-freelancer")
    copy_tree_if_exists(ROOT / "assets" / "images" / "generated", ASSETS_DIR / "images" / "generated")


def package_theme() -> None:
    if STAGE_DIR.exists():
        shutil.rmtree(STAGE_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copytree(THEME_DIR, STAGE_DIR)

    images_dir = STAGE_DIR / "assets" / "images"
    if images_dir.exists():
        for image_path in images_dir.rglob("*"):
            if not image_path.is_file():
                continue
            rel = image_path.relative_to(images_dir).as_posix()
            keep = rel.startswith("additional-campaign/") or rel.startswith("cozy-freelancer/") or rel == "generated/cf-favicon.svg"
            if not keep:
                image_path.unlink()

        for directory in sorted((p for p in images_dir.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
            if not any(directory.iterdir()):
                directory.rmdir()

    if PACKAGE_PATH.exists():
        PACKAGE_PATH.unlink()
    shutil.make_archive(str(PACKAGE_PATH.with_suffix("")), "zip", root_dir=DIST_DIR, base_dir="camelot-flows")


def build_theme() -> None:
    prepare_theme_assets()

    content = read_text(HTML_PATH)
    body_match = re.search(r'<body class="(.*?)">(.*?)</body>', content, re.DOTALL)
    if not body_match:
        raise ValueError("Could not find <body> in code_v2.html")

    body_classes = body_match.group(1)
    body_content = body_match.group(2)

    nav_end = body_content.find("</nav>")
    if nav_end == -1:
        raise ValueError("Could not find </nav> in code_v2.html")
    nav_end += len("</nav>")

    footer_start = body_content.find("<footer")
    if footer_start == -1:
        raise ValueError("Could not find <footer> in code_v2.html")

    header_html = rewrite_wp_routes(rewrite_asset_refs(body_content[:nav_end]))
    main_content = rewrite_wp_routes(rewrite_asset_refs(body_content[nav_end:footer_start]))
    footer_html = strip_page_scripts(body_content[footer_start:])
    footer_html = rewrite_wp_routes(rewrite_asset_refs(footer_html))

    style_header = """/*
Theme Name: Camelot Flows
Description: WordPress conversion of Camelot Flows
Version: 1.1.0
Text Domain: camelot-flows
*/
"""
    write_text(THEME_DIR / "style.css", style_header)

    header_php = f"""<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php wp_head(); ?>
</head>
<body <?php body_class('{body_classes}'); ?>>
<?php wp_body_open(); ?>
{header_html}
"""
    write_text(THEME_DIR / "header.php", header_php)

    footer_php = f"""{footer_html}
<?php wp_footer(); ?>
</body>
</html>
"""
    write_text(THEME_DIR / "footer.php", footer_php)

    index_php = f"""<?php get_header(); ?>
{main_content}
<?php get_footer(); ?>
"""
    write_text(THEME_DIR / "index.php", index_php)

    functions_php = """<?php
define('CF_MAIN_SITE', 'https://camelotflows.dev');

function camelot_flows_scripts() {
    wp_enqueue_style('google-fonts', 'https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;0,700;1,300;1,400&family=Inter:wght@300;400;500&family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;700&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap', array(), null);
    wp_enqueue_style('camelot-flows-style', get_stylesheet_uri(), array(), '1.1.0');
    wp_enqueue_style('camelot-flows-tailwind', get_template_directory_uri() . '/assets/css/tailwind.built.css', array('camelot-flows-style'), '1.3.0');
    wp_enqueue_style('camelot-flows-site', get_template_directory_uri() . '/assets/site.css', array('camelot-flows-tailwind'), '1.2.0');
    wp_enqueue_style('camelot-flows-components', get_template_directory_uri() . '/assets/css/camelot.css', array('camelot-flows-site'), '1.5.0');
    wp_enqueue_style('camelot-flows-night', get_template_directory_uri() . '/assets/css/theme-night.css', array('camelot-flows-components'), '1.2.0');
    wp_enqueue_style('camelot-flows-lang', get_template_directory_uri() . '/assets/css/lang-switcher.css', array('camelot-flows-night'), '1.2.0');
    wp_enqueue_script('lenis', 'https://unpkg.com/@studio-freight/lenis@1.0.42/dist/lenis.min.js', array(), null, true);
    wp_enqueue_script('gsap', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js', array(), null, true);
    wp_enqueue_script('scrolltrigger', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js', array('gsap'), null, true);
    wp_enqueue_script('textplugin', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/TextPlugin.min.js', array('gsap'), null, true);
    wp_enqueue_script('camelot-flows-locales', get_template_directory_uri() . '/assets/js/locales.js', array(), '1.2.0', true);
    wp_enqueue_script('camelot-flows-i18n', get_template_directory_uri() . '/assets/js/i18n.js', array('camelot-flows-locales'), '1.1.0', true);
    wp_enqueue_script('camelot-flows-gsap', get_template_directory_uri() . '/assets/js/camelot-gsap.js', array('gsap', 'scrolltrigger', 'textplugin', 'lenis', 'camelot-flows-i18n'), '1.5.0', true);
    wp_enqueue_script('camelot-flows-site', get_template_directory_uri() . '/assets/site.js', array('camelot-flows-gsap'), '1.2.0', true);
}
add_action('wp_enqueue_scripts', 'camelot_flows_scripts');

function camelot_flows_head() {
    ?>
    <script id="camelot-theme-bootstrap">
      (function () {
        var html = document.documentElement;
        try {
          var c = document.cookie.match('(?:^|;) ?cf_theme=([^;]*)');
          var t = c ? c[1] : (localStorage.getItem('cf_theme') || 'cozy');
          html.setAttribute('data-theme', t);
        } catch (e) { html.setAttribute('data-theme', 'cozy'); }
        try {
          var cl = document.cookie.match('(?:^|;) ?cf_lang=([^;]*)');
          var l = cl ? cl[1] : (localStorage.getItem('cf_lang') || 'en');
          if (['en','ro','ru'].indexOf(l) === -1) l = 'en';
          html.setAttribute('lang', l);
          html.setAttribute('data-cf-lang', l);
          if (l !== 'en') html.setAttribute('data-i18n-loading', '1');
        } catch (e) {}
        try {
          if (sessionStorage.getItem('cf_loaded') === '1') {
            html.classList.add('cf-skip-preloader');
          }
        } catch (e) {}
        html.classList.add('js');
      })();
    </script>
    <?php
}
add_action('wp_head', 'camelot_flows_head', 0);

function camelot_flows_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('automatic-feed-links');
    add_theme_support('html5', ['comment-list', 'comment-form', 'search-form', 'gallery', 'caption']);
    add_image_size('blog-card', 800, 450, true);
    register_nav_menus([
        'primary' => 'Primary Navigation',
        'blog'    => 'Blog Navigation',
    ]);
}
add_action('after_setup_theme', 'camelot_flows_setup');
"""
    write_text(THEME_DIR / "functions.php", functions_php)

    for source_name, (template_name, template_label) in PAGE_TEMPLATE_MAP.items():
        source_path = ROOT / source_name
        if not source_path.exists():
            continue
        source_html = read_text(source_path)
        redirect_route = redirect_route_from_html(source_html)
        if redirect_route:
            write_text(THEME_DIR / template_name, redirect_template(template_label, redirect_route))
            continue

        page_content = extract_content_between_nav_and_footer(source_html, source_name)
        page_content = rewrite_wp_routes(rewrite_asset_refs(page_content))
        template_php = f"""<?php
/* Template Name: {template_label} */
get_header(); ?>
{page_content}
<?php get_footer(); ?>
"""
        write_text(THEME_DIR / template_name, template_php)


if __name__ == "__main__":
    build_theme()
    package_theme()
    print(f"Theme generation complete: {PACKAGE_PATH.name}")
