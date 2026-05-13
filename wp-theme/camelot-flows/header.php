<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php wp_head(); ?>
</head>
<body <?php body_class('theme-cozy font-body overflow-x-hidden selection:bg-primary selection:text-white'); ?>>
<?php wp_body_open(); ?>

    <div class="scroll-progress" aria-hidden="true"></div>

    <div id="preloader" class="fixed inset-0 z-[999999] bg-obsidian flex flex-col items-center justify-center">
        <div class="absolute inset-0 grid-bg opacity-30"></div>
        <div class="w-32 h-32 relative flex items-center justify-center mb-8 z-10">
            <div class="absolute inset-0 rounded-full border-t-2 border-primary animate-spin"></div>
            <div
                class="absolute inset-2 rounded-full border-b-2 border-accent animate-[spin_2s_linear_infinite_reverse]">
            </div>
            <span class="material-symbols-outlined text-4xl text-white animate-pulse">design_services</span>
        </div>
        <div class="text-primary-glow font-mono text-[10px] tracking-[0.4em] uppercase mb-4 z-10" id="loader-text">
            Initializing Protocols...</div>
        <div class="w-64 h-[2px] bg-white/10 rounded-full overflow-hidden z-10">
            <div id="loader-bar" class="w-0 h-full bg-gradient-to-r from-primary to-accent"></div>
        </div>
        <div id="loader-percent" class="mt-4 font-mono text-white text-sm tracking-widest z-10">0%</div>
    </div>

    <div class="grain-overlay"></div>
    <div id="bg-orbs" class="fixed top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div class="bg-orb absolute top-[-10%] left-[-10%] w-[50vw] h-[50vw] bg-cobalt/20 rounded-full blur-[120px]">
        </div>
        <div
            class="bg-orb absolute bottom-[-10%] right-[-10%] w-[40vw] h-[40vw] bg-accent/10 rounded-full blur-[100px]">
        </div>
        <div class="bg-orb absolute top-[40%] left-[30%] w-[30vw] h-[30vw] bg-primary/10 rounded-full blur-[150px]">
        </div>
        <div class="absolute inset-0 grid-bg"></div>
    </div>

    <!-- ИЗМЕНЕНИЕ: Zentry Orbital Badge (Вращающаяся печать в углу) -->
    <div
        class="fixed bottom-8 right-8 z-50 pointer-events-none mix-blend-screen opacity-60 hidden md:flex items-center justify-center w-32 h-32">
        <svg viewBox="0 0 100 100" width="100" height="100" class="animate-[spin_12s_linear_infinite] absolute inset-0">
            <defs>
                <path id="circle" d="M 50, 50 m -35, 0 a 35,35 0 1,1 70,0 a 35,35 0 1,1 -70,0" />
            </defs>
            <text font-size="10.5" fill="currentColor" class="text-primary-glow font-mono uppercase tracking-[0.15em]">
                <textPath href="#circle">Camelot Flows • Digital Kingdom •</textPath>
            </text>
        </svg>
        <span class="material-symbols-outlined text-primary text-2xl animate-pulse">change_history</span>
    </div>

    <nav class="fixed top-0 left-0 w-full z-50 px-4 py-4 md:px-6 md:py-6">
        <div
            class="max-w-7xl mx-auto flex items-center justify-between glass-panel rounded-lg px-6 py-3 border-l-4 border-l-primary/50" style="position:relative;z-index:201">
            <div class="flex items-center gap-4">
                <div
                    class="w-8 h-8 rounded bg-gradient-to-br from-primary to-accent flex items-center justify-center shadow-neon">
                    <span class="material-symbols-outlined text-white text-lg">shield</span>
                </div>
                <div class="flex flex-col">
                    <span
                        class="text-lg font-display font-bold tracking-tight uppercase leading-none text-white">Camelot</span>
                    <span
                        class="text-[0.6rem] font-mono text-primary-glow tracking-[0.2em] uppercase mt-1">Flows_v2.0</span>
                </div>
            </div>
            <div class="hidden md:flex items-center gap-1">
                <a class="px-3 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider"
                    href="<?php echo CF_MAIN_SITE; ?>" data-i18n="common.nav.home">[Home]</a>
                <a class="px-3 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider"
                    href="<?php echo CF_MAIN_SITE; ?>/#round-table" data-i18n="common.nav.services">[Services]</a>
                <a class="px-3 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider"
                    href="<?php echo CF_MAIN_SITE; ?>/arsenal.html" data-i18n="common.nav.arsenal">[Arsenal]</a>
                <a class="px-3 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider"
                    href="<?php echo CF_MAIN_SITE; ?>/merlin.html" data-i18n="common.nav.merlin">[Merlin]</a>
                <a class="px-3 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider hidden lg:block"
                    href="<?php echo CF_MAIN_SITE; ?>/case-studies.html" data-i18n="common.nav.cases">[Cases]</a>
                <a class="px-3 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider hidden xl:block"
                    href="<?php echo CF_MAIN_SITE; ?>/for-agencies.html" data-i18n="common.nav.agencies">[Agencies]</a>
                <a class="px-3 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider hidden xl:block"
                    href="<?php echo CF_MAIN_SITE; ?>/about.html" data-i18n="common.nav.about">[About]</a>
                <a class="px-3 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider hidden lg:block"
                    href="<?php echo CF_MAIN_SITE; ?>/#starwars-pricing" data-i18n="common.nav.pricing">[Pricing]</a>
                <a class="px-3 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider"
                    href="<?php echo CF_MAIN_SITE; ?>/contact.html" data-i18n="common.nav.contact">[Contact]</a>
            </div>
            <div class="flex items-center gap-2">
                <a href="tel:+37369555936" class="nav-phone-btn flex items-center justify-center w-11 h-11 rounded border border-white/10 hover:bg-white/5 hover:border-primary/50 hover:text-primary transition-all text-slate-400" aria-label="Call Camelot Flows" title="+373 69 555 936">
                    <span class="material-symbols-outlined cf-phone-icon" style="font-size:18px">call</span>
                </a>
                <div class="hidden lg:flex items-center gap-2 px-3 py-1 rounded bg-black/40 border border-white/5">
                    <div class="w-1.5 h-1.5 rounded-full bg-emerald-500 status-dot animate-pulse"></div>
                    <span class="text-[10px] font-mono text-emerald-500/80" data-i18n="common.nav.sys_online">SYS_ONLINE</span>
                </div>
                <div class="lang-switcher" data-cf-lang-switcher>
                    <button class="lang-trigger" type="button" aria-haspopup="listbox" aria-expanded="false" aria-label="Change language" data-i18n-attr="aria-label:common.lang_label">
                        <span class="lang-current" data-cf-lang-current>EN</span>
                        <span class="material-symbols-outlined lang-chevron" style="font-size:16px">expand_more</span>
                    </button>
                    <ul class="lang-menu" role="listbox" hidden>
                        <li role="option" data-lang="en" tabindex="-1">EN</li>
                        <li role="option" data-lang="ro" tabindex="-1">RO</li>
                        <li role="option" data-lang="ru" tabindex="-1">RU</li>
                    </ul>
                </div>
                <button id="theme-toggle" type="button" class="theme-toggle" aria-label="Toggle theme">
    <span class="material-symbols-outlined icon-cozy" style="font-size:20px">dark_mode</span>
    <span class="material-symbols-outlined icon-night" style="font-size:20px">light_mode</span>
</button>
                <a href="<?php echo CF_MAIN_SITE; ?>/contact.html?service=staff"
                    class="bg-indigo-600/20 hover:bg-indigo-600/40 border border-indigo-500/50 hover:border-indigo-400 text-indigo-100 px-4 py-1.5 rounded text-xs font-mono font-bold transition-all shadow-neon hover:shadow-neon-strong hidden lg:inline-flex items-center nav-cta" data-i18n="common.nav.summon_agent">[Hire_me]</a>
            </div>
        </div>
        </nav>
