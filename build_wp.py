import os
import re

html_path = 'c:/Users/user/Downloads/stitch_camelot_flows_homepage/code_v2.html'
theme_dir = 'c:/Users/user/Downloads/stitch_camelot_flows_homepage/wp-theme/camelot-flows'

os.makedirs(os.path.join(theme_dir, 'assets/images'), exist_ok=True)
os.makedirs(os.path.join(theme_dir, 'assets/js'), exist_ok=True)

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
css_content = style_match.group(1) if style_match else ''

with open(os.path.join(theme_dir, 'style.css'), 'w', encoding='utf-8') as f:
    f.write('/*\nTheme Name: Camelot Flows\nDescription: WP conversion of Camelot Flows\nVersion: 1.0\nText Domain: camelot-flows\n*/\n' + css_content)

# Extract body
body_match = re.search(r'<body class="(.*?)">(.*?)</body>', content, re.DOTALL)
body_classes = body_match.group(1) if body_match else 'font-body overflow-x-hidden selection:bg-primary selection:text-white'
body_content = body_match.group(2) if body_match else ''

# Extract JS
all_scripts = re.findall(r'<script>(.*?)</script>', body_content, re.DOTALL)
js_content = ''
for s in all_scripts:
    if 'gsap.registerPlugin' in s:
        js_content = s.strip()
        body_content = body_content.replace(f'<script>{s}</script>', '')

with open(os.path.join(theme_dir, 'assets/js/main.js'), 'w', encoding='utf-8') as f:
    f.write(js_content)

# Split body into header, index, footer
nav_end = body_content.find('</nav>') + 6
header_html = body_content[:nav_end]

footer_start = body_content.find('<footer')
main_content = body_content[nav_end:footer_start]
footer_html = body_content[footer_start:]

# Remove <script src=...> tags from footer_html since they are in functions.php
footer_html = re.sub(r'<script src=".*?"></script>\s*', '', footer_html)

# Adjust image paths in main
main_content = re.sub(r'src="([^http].*?\.png)"', r'src="<?php echo get_template_directory_uri(); ?>/assets/images/\1"', main_content)

header_php = f'''<!DOCTYPE html>
<html <?php language_attributes(); ?> class="dark">
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php wp_head(); ?>
</head>
<body <?php body_class('{body_classes}'); ?>>
<?php wp_body_open(); ?>
{header_html}
'''

with open(os.path.join(theme_dir, 'header.php'), 'w', encoding='utf-8') as f:
    f.write(header_php)

footer_php = f'''{footer_html}
<?php wp_footer(); ?>
</body>
</html>
'''

with open(os.path.join(theme_dir, 'footer.php'), 'w', encoding='utf-8') as f:
    f.write(footer_php)

index_php = f'''<?php get_header(); ?>
{main_content}
<?php get_footer(); ?>
'''

with open(os.path.join(theme_dir, 'index.php'), 'w', encoding='utf-8') as f:
    f.write(index_php)

functions_php = '''<?php
function camelot_flows_scripts() {
    wp_enqueue_script('tailwindcss', 'https://cdn.tailwindcss.com?plugins=forms,container-queries', array(), null, false);
    wp_enqueue_style('google-fonts', 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;700&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap', array(), null);
    wp_enqueue_style('camelot-flows-style', get_stylesheet_uri());
    wp_enqueue_script('lenis', 'https://unpkg.com/@studio-freight/lenis@1.0.42/dist/lenis.min.js', array(), null, true);
    wp_enqueue_script('gsap', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js', array(), null, true);
    wp_enqueue_script('scrolltrigger', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js', array('gsap'), null, true);
    wp_enqueue_script('textplugin', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/TextPlugin.min.js', array('gsap'), null, true);
    wp_enqueue_script('camelot-flows-main', get_template_directory_uri() . '/assets/js/main.js', array('gsap', 'scrolltrigger', 'textplugin', 'lenis'), '1.0', true);
}
add_action('wp_enqueue_scripts', 'camelot_flows_scripts');

function camelot_flows_head() {
    ?>
    <script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "primary": "#4f46e5","primary-glow": "#6366f1","accent": "#8b5cf6","cobalt": "#1e3a8a","obsidian": "#050508","obsidian-light": "#0a0a12",
                    },
                    fontFamily: {
                        "display": ["Space Grotesk", "sans-serif"],
                        "body": ["Inter", "sans-serif"],
                        "mono": ["JetBrains Mono", "monospace"],
                    },
                    backgroundImage: {
                        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
                    },
                    boxShadow: {
                        'neon': '0 0 15px -3px rgba(99, 102, 241, 0.4), 0 4px 6px -4px rgba(99, 102, 241, 0.2)',
                        'neon-strong': '0 0 25px -5px rgba(99, 102, 241, 0.6)',
                    }
                },
            },
        }
    </script>
    <?php
}
add_action('wp_head', 'camelot_flows_head', 10);

function camelot_flows_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
}
add_action('after_setup_theme', 'camelot_flows_setup');
'''

with open(os.path.join(theme_dir, 'functions.php'), 'w', encoding='utf-8') as f:
    f.write(functions_php)

print("Theme generation complete.")
