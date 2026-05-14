<?php
define('CF_MAIN_SITE', 'https://camelotflows.dev');

function camelot_flows_scripts() {
    wp_enqueue_style('google-fonts', 'https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;0,700;1,300;1,400&family=Inter:wght@300;400;500&family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;700&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap', array(), null);
    wp_enqueue_style('camelot-flows-style', get_stylesheet_uri(), array(), '1.1.0');
    wp_enqueue_style('camelot-flows-tailwind', get_template_directory_uri() . '/assets/css/tailwind.built.css', array('camelot-flows-style'), '1.3.0');
    wp_enqueue_style('camelot-flows-site', get_template_directory_uri() . '/assets/site.css', array('camelot-flows-tailwind'), '1.2.0');
    wp_enqueue_style('camelot-flows-components', get_template_directory_uri() . '/assets/css/camelot.css', array('camelot-flows-site'), '1.6.0');
    wp_enqueue_style('camelot-flows-night', get_template_directory_uri() . '/assets/css/theme-night.css', array('camelot-flows-components'), '1.2.0');
    wp_enqueue_style('camelot-flows-lang', get_template_directory_uri() . '/assets/css/lang-switcher.css', array('camelot-flows-night'), '1.2.0');
    wp_enqueue_script('lenis', 'https://unpkg.com/@studio-freight/lenis@1.0.42/dist/lenis.min.js', array(), null, true);
    wp_enqueue_script('gsap', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js', array(), null, true);
    wp_enqueue_script('scrolltrigger', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js', array('gsap'), null, true);
    wp_enqueue_script('textplugin', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/TextPlugin.min.js', array('gsap'), null, true);
    wp_enqueue_script('camelot-flows-locales', get_template_directory_uri() . '/assets/js/locales.js', array(), '1.2.0', true);
    wp_enqueue_script('camelot-flows-i18n', get_template_directory_uri() . '/assets/js/i18n.js', array('camelot-flows-locales'), '1.1.0', true);
    wp_enqueue_script('camelot-flows-gsap', get_template_directory_uri() . '/assets/js/camelot-gsap.v2.js', array('gsap', 'scrolltrigger', 'textplugin', 'lenis', 'camelot-flows-i18n'), '1.0.0', true);
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

