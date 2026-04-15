<?php
function camelot_flows_scripts() {
    wp_enqueue_script('tailwindcss', 'https://cdn.tailwindcss.com?plugins=forms,container-queries,typography', array(), null, false);
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
