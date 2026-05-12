<?php get_header(); ?>


    <main id="hero"
        class="relative pt-44 pb-20 px-6 overflow-hidden min-h-screen flex flex-col justify-center perspective-1000">
        <div aria-hidden="true" class="absolute inset-0 z-0 pointer-events-none" style="background:url('<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-hero-home.webp'); ?>') center/cover no-repeat;opacity:0.12;mix-blend-mode:multiply;"></div>
        <div
            class="absolute top-[25%] left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-primary/20 to-transparent z-0 overflow-hidden">
            <div
                class="data-stream w-32 md:w-64 h-full bg-gradient-to-r from-transparent via-white to-transparent shadow-[0_0_15px_#fff]">
            </div>
        </div>
        <div
            class="absolute bottom-[35%] left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-accent/20 to-transparent z-0 overflow-hidden">
            <div
                class="data-stream w-40 md:w-80 h-full bg-gradient-to-r from-transparent via-white to-transparent shadow-[0_0_15px_#fff]">
            </div>
        </div>

        <div class="absolute top-[20%] right-[8%] w-20 h-20 md:w-28 md:h-28 glass-panel rounded-xl rotate-12 flex items-center justify-center opacity-80 parallax-float z-20 shadow-neon border-primary/40"
            data-depth="0.15">
            <span
                class="material-symbols-outlined text-primary text-4xl md:text-5xl drop-shadow-[0_0_15px_rgba(79,70,229,0.8)]">code_blocks</span>
        </div>
        <div class="absolute bottom-[25%] left-[5%] md:left-[10%] w-16 h-16 md:w-20 md:h-20 glass-panel rounded-full flex items-center justify-center opacity-60 parallax-float z-20 border-accent/40"
            data-depth="-0.12">
            <span class="material-symbols-outlined text-accent text-2xl md:text-3xl">memory</span>
        </div>
        <div class="absolute top-[40%] left-[45%] md:left-[50%] w-12 h-12 md:w-16 md:h-16 glass-panel rounded-lg flex items-center justify-center opacity-40 parallax-float z-20 border-white/10"
            data-depth="0.08" style="transform: rotate(-15deg);">
            <span class="material-symbols-outlined text-white text-xl md:text-2xl">api</span>
        </div>

        <div class="max-w-7xl mx-auto w-full grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
            <div class="lg:col-span-7 z-10 relative">
                <div id="hero-badge"
                    class="inline-flex items-center gap-3 px-4 py-2 rounded-none border-l-2 border-primary bg-gradient-to-r from-primary/10 to-transparent mb-8">
                    <span class="material-symbols-outlined text-primary text-sm">location_on</span>
                    <span class="text-primary-glow font-mono text-xs tracking-widest uppercase">Solo workshop · serving worldwide</span>
                </div>
                <h1 id="hero-h1"
                    class="font-display text-5xl md:text-7xl lg:text-8xl font-bold leading-[1.1] tracking-tighter mb-8 text-white uppercase perspective-1000"
                    style="transform-style: preserve-3d;">
                    <span id="hero-word-1" class="inline-block whitespace-nowrap">Award-Winning</span> <br />
                    <span class="inline-flex overflow-hidden pb-4 -mb-4">
                        <span id="hero-word-2"
                            class="inline-block text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-purple-400 to-indigo-400 animate-gradient-x text-glow whitespace-nowrap">Systems</span>
                    </span>
                </h1>
                <p id="hero-p"
                    class="text-lg md:text-xl text-slate-400 max-w-xl mb-10 leading-relaxed font-light border-l border-white/10 pl-6">
                    I build the site, then I build the <span class="text-white font-medium">staff that runs it.</span>
                    Sites in two weeks. AI staff in three.
                </p>
                <div id="hero-btns" class="flex flex-wrap gap-5">
                    <button onclick="window.location.href='<?php echo esc_url(home_url('/contact/')); ?>'"
                        class="group relative px-8 py-4 bg-primary text-white font-mono font-bold text-sm tracking-wide overflow-hidden rounded-sm hover:scale-[1.02] transition-transform">
                        <div
                            class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000">
                        </div>
                        <span class="relative flex items-center gap-3">
                            START A PROJECT
                            <span class="material-symbols-outlined text-sm">arrow_forward</span>
                        </span>
                    </button>
                    <button onclick="window.location.href='<?php echo esc_url(home_url('/the-arsenal/')); ?>'"
                        class="px-8 py-4 glass-panel text-slate-300 font-mono font-bold text-sm tracking-wide rounded-sm hover:bg-white/5 border border-white/10 hover:border-primary/50 transition-colors flex items-center gap-3">
                        VIEW ARSENAL
                        <span class="material-symbols-outlined text-sm opacity-50">grid_view</span>
                    </button>
                </div>
                <div id="hero-stats" class="mt-16 flex gap-8 md:gap-12 border-t border-white/5 pt-8">
                    <div>
                        <div class="font-display text-xl font-bold text-white mb-1 text-primary">Productized</div>
                        <div class="text-[10px] font-mono text-slate-500 uppercase tracking-widest">Fixed price</div>
                    </div>
                    <div>
                        <div class="font-display text-xl font-bold text-white mb-1">24h reply</div>
                        <div class="text-[10px] font-mono text-slate-500 uppercase tracking-widest">Always</div>
                    </div>
                    <div>
                        <div class="font-display text-xl font-bold text-white mb-1">Worldwide</div>
                        <div class="text-[10px] font-mono text-slate-500 uppercase tracking-widest">From Chișinău</div>
                    </div>
                </div>
            </div>
            <div class="lg:col-span-5 relative h-[400px] md:h-[600px] w-full flex items-center justify-center">
                <div class="absolute inset-0 opacity-20"
                    style="background-image: radial-gradient(circle, #4f46e5 1px, transparent 1px); background-size: 30px 30px;">
                </div>
                <div class="relative w-full aspect-square max-w-md">
                    <div
                        class="absolute inset-0 rounded-full border border-primary/20 animate-[spin_10s_linear_infinite]">
                    </div>
                    <div
                        class="absolute inset-4 rounded-full border border-dashed border-primary/30 animate-[spin_15s_linear_infinite_reverse]">
                    </div>
                    <div
                        class="absolute inset-0 m-auto w-48 h-64 md:w-64 md:h-80 glass-panel clip-path-shield flex flex-col items-center justify-center z-10 shadow-neon">
                        <style>
                            .clip-path-shield {
                                clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
                            }
                        </style>
                        <div
                            class="w-16 h-16 md:w-20 md:h-20 mb-4 rounded-full bg-gradient-to-b from-primary/20 to-transparent flex items-center justify-center border border-primary/40 relative">
                            <div class="absolute inset-0 rounded-full animate-ping bg-primary/20"></div>
                            <span
                                class="material-symbols-outlined text-3xl md:text-4xl text-primary drop-shadow-[0_0_10px_rgba(79,70,229,0.8)]">security</span>
                        </div>
                        <h3 class="text-white font-mono font-bold tracking-widest text-xs md:text-sm mb-1">
                            PERFORMANCE_MAX</h3>
                        <p class="text-[8px] md:text-[10px] text-indigo-300 uppercase">Speed & Design: Awwwards Level
                        </p>
                    </div>
                    <div class="absolute top-10 right-0 glass-panel p-3 rounded border-l-2 border-l-emerald-500 backdrop-blur-md animate-bounce hidden md:block"
                        style="animation-duration: 3s;">
                        <div class="flex items-center gap-2 mb-1">
                            <span class="w-2 h-2 bg-emerald-500 rounded-full status-dot"></span>
                            <span class="text-[10px] font-mono text-white">CPU_LOAD</span>
                        </div>
                        <div class="w-24 h-1 bg-white/10 rounded-full overflow-hidden">
                            <div class="w-[30%] h-full bg-emerald-500"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- ИЗМЕНЕНИЕ: Zentry Kinetic Angled Marquee -->
    <div
        class="relative w-full overflow-hidden bg-primary py-5 -rotate-2 scale-110 z-30 shadow-[0_0_40px_rgba(79,70,229,0.4)] border-y border-white/20">
        <div
            class="marquee-container flex whitespace-nowrap font-display font-bold text-4xl md:text-5xl uppercase tracking-tighter text-obsidian">
            <!-- Блок контента 1 -->
            <div class="flex items-center">
                <span class="mx-6">// AWP WEB DESIGN</span>
                <span class="material-symbols-outlined text-4xl mx-2">auto_awesome</span>
                <span class="mx-6">// CUSTOM AUTOMATION</span>
                <span class="material-symbols-outlined text-4xl mx-2">speed</span>
                <span class="mx-6">// AGENCY PARTNERSHIPS</span>
                <span class="material-symbols-outlined text-4xl mx-2">memory</span>
                <span class="mx-6">// SCALABLE SYSTEMS</span>
            </div>
            <!-- Блок контента 2 (копия для бесконечного цикла) -->
            <div class="flex items-center">
                <span class="mx-6">// AWP WEB DESIGN</span>
                <span class="material-symbols-outlined text-4xl mx-2">auto_awesome</span>
                <span class="mx-6">// CUSTOM AUTOMATION</span>
                <span class="material-symbols-outlined text-4xl mx-2">speed</span>
                <span class="mx-6">// AGENCY PARTNERSHIPS</span>
                <span class="material-symbols-outlined text-4xl mx-2">memory</span>
                <span class="mx-6">// SCALABLE SYSTEMS</span>
            </div>
        </div>
    </div>

    <!-- ИЗМЕНЕНИЕ: Исправлен баг "Черной дыры" (GSAP Pin Spacer Bug). Убраны ручные высоты и sticky -->
    <section id="portal-trigger" class="relative bg-obsidian z-20">
        <!-- Блок центровки без sticky, GSAP сам создаст pin -->
        <div class="relative h-screen w-full flex items-center justify-center p-4 md:p-12 overflow-hidden">

            <!-- Сам Портал (изначально сжат в ромб/щит через clip-path) -->
            <div id="zentry-portal"
                class="w-full h-full bg-obsidian border border-primary/40 relative flex items-center justify-center overflow-hidden shadow-neon-strong"
                style="clip-path: polygon(50% 5%, 96% 50%, 50% 95%, 4% 50%); border-radius: 40px;">

                <!-- Параллакс фон внутри портала -->
                <div id="portal-bg"
                    class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-20">
                </div>
                <div class="absolute inset-0 bg-gradient-radial from-primary/30 via-obsidian/80 to-obsidian"></div>

                <!-- Контент портала -->
                <div class="text-center z-10 relative">
                    <span id="portal-sub"
                        class="text-primary-glow font-mono text-xs md:text-sm uppercase tracking-[0.4em] mb-4 block drop-shadow-[0_0_10px_rgba(99,102,241,0.8)]">Select
                        Path</span>
                    <h2 id="portal-text"
                        class="font-display text-5xl md:text-9xl font-bold tracking-tighter text-white uppercase text-glow mix-blend-overlay">
                        Choose<br />Your Flow</h2>
                </div>

                <!-- ИЗМЕНЕНИЕ: Артурианское Откровение (Голограмма Экскалибура) -->
                <div id="portal-revelation"
                    class="absolute inset-0 flex flex-col items-center justify-center opacity-0 scale-75 pointer-events-none z-20">
                    <div class="relative w-64 h-64 md:w-80 md:h-80 flex items-center justify-center">
                        <!-- Магические кольца (Ормузд/Артур) -->
                        <div
                            class="absolute inset-0 rounded-full border border-primary/20 animate-[spin_10s_linear_infinite]">
                        </div>
                        <div
                            class="absolute inset-4 rounded-full border border-dashed border-accent/40 animate-[spin_15s_linear_infinite_reverse]">
                        </div>
                        <div
                            class="absolute inset-8 rounded-full border-t-2 border-l-2 border-white/10 animate-[spin_5s_ease-in-out_infinite_alternate]">
                        </div>

                        <!-- Голографический Меч Экскалибур -->
                        <div class="relative z-10 flex flex-col items-center">
                            <span
                                class="material-symbols-outlined text-[100px] md:text-[140px] text-white drop-shadow-[0_0_40px_rgba(99,102,241,0.8)]"
                                style="transform: rotate(180deg);">swords</span>
                        </div>

                        <!-- Энергетический пьедестал -->
                        <div class="absolute bottom-10 w-32 h-4 bg-primary/60 blur-[15px] rounded-full"></div>
                        <div class="absolute bottom-10 w-16 h-2 bg-white/80 blur-[5px] rounded-full"></div>
                    </div>

                    <h3
                        class="font-display text-3xl md:text-5xl font-bold mt-8 text-white uppercase tracking-widest text-glow">
                        How Do You <span class="text-primary-glow">Operate?</span></h3>
                    <div
                        class="mt-4 flex flex-wrap justify-center items-center gap-3 bg-black/50 px-4 py-2 rounded border border-primary/30 backdrop-blur-md">
                        <a href="#grand-armory"
                            class="font-mono text-xs text-emerald-400 tracking-[0.2em] uppercase hover:underline">1.
                            Business</a>
                        <span class="text-white/30">|</span>
                        <a href="#obsidian-vault"
                            class="font-mono text-xs text-purple-400 tracking-[0.2em] uppercase hover:underline">2.
                            Founder</a>
                        <span class="text-white/30">|</span>
                        <a href="<?php echo esc_url(home_url('/for-agencies/')); ?>"
                            class="font-mono text-xs text-blue-400 tracking-[0.2em] uppercase hover:underline">3.
                            Agency</a>
                    </div>
                </div>

                <!-- Декоративные уголки -->
                <div class="absolute top-8 left-8 w-8 h-8 border-t-2 border-l-2 border-primary/50"></div>
                <div class="absolute top-8 right-8 w-8 h-8 border-t-2 border-r-2 border-primary/50"></div>
                <div class="absolute bottom-8 left-8 w-8 h-8 border-b-2 border-l-2 border-primary/50"></div>
                <div class="absolute bottom-8 right-8 w-8 h-8 border-b-2 border-r-2 border-primary/50"></div>
            </div>

        </div>
    </section>

    <section id="round-table"
        class="py-24 px-6 relative border-t border-white/5 bg-obsidian overflow-hidden -mt-[1px] z-30">
        <div
            class="absolute top-[5%] right-[-40%] md:right-[-15%] w-[500px] h-[500px] md:w-[800px] md:h-[800px] opacity-25 pointer-events-none z-0">
            <div id="literal-round-table"
                class="relative w-full h-full border-[2px] border-dashed border-primary/30 rounded-full flex items-center justify-center">
                <div class="absolute w-[75%] h-[75%] border border-accent/20 rounded-full"></div>
                <div class="absolute w-[45%] h-[45%] border border-white/5 rounded-full"></div>

                <div class="absolute w-full h-full" style="transform: rotate(0deg);">
                    <div
                        class="absolute top-[-24px] md:top-[-32px] left-1/2 -translate-x-1/2 w-12 h-12 md:w-16 md:h-16 bg-obsidian border border-primary/50 rounded-full flex items-center justify-center shadow-neon">
                        <span class="rt-icon material-symbols-outlined text-white text-lg md:text-2xl">smart_toy</span>
                    </div>
                </div>
                <div class="absolute w-full h-full" style="transform: rotate(60deg);">
                    <div
                        class="absolute top-[-24px] md:top-[-32px] left-1/2 -translate-x-1/2 w-12 h-12 md:w-16 md:h-16 bg-obsidian border border-accent/50 rounded-full flex items-center justify-center shadow-[0_0_15px_rgba(139,92,246,0.5)]">
                        <span class="rt-icon material-symbols-outlined text-white text-lg md:text-2xl">webhook</span>
                    </div>
                </div>
                <div class="absolute w-full h-full" style="transform: rotate(120deg);">
                    <div
                        class="absolute top-[-24px] md:top-[-32px] left-1/2 -translate-x-1/2 w-12 h-12 md:w-16 md:h-16 bg-obsidian border border-indigo-500/50 rounded-full flex items-center justify-center shadow-[0_0_15px_rgba(99,102,241,0.5)]">
                        <span class="rt-icon material-symbols-outlined text-white text-lg md:text-2xl">database</span>
                    </div>
                </div>
                <div class="absolute w-full h-full" style="transform: rotate(180deg);">
                    <div
                        class="absolute top-[-24px] md:top-[-32px] left-1/2 -translate-x-1/2 w-12 h-12 md:w-16 md:h-16 bg-obsidian border border-emerald-500/50 rounded-full flex items-center justify-center shadow-[0_0_15px_rgba(16,185,129,0.4)]">
                        <span class="rt-icon material-symbols-outlined text-white text-lg md:text-2xl">sync</span>
                    </div>
                </div>
                <div class="absolute w-full h-full" style="transform: rotate(240deg);">
                    <div
                        class="absolute top-[-24px] md:top-[-32px] left-1/2 -translate-x-1/2 w-12 h-12 md:w-16 md:h-16 bg-obsidian border border-purple-500/50 rounded-full flex items-center justify-center shadow-[0_0_15px_rgba(168,85,247,0.4)]">
                        <span class="rt-icon material-symbols-outlined text-white text-lg md:text-2xl">terminal</span>
                    </div>
                </div>
                <div class="absolute w-full h-full" style="transform: rotate(300deg);">
                    <div
                        class="absolute top-[-24px] md:top-[-32px] left-1/2 -translate-x-1/2 w-12 h-12 md:w-16 md:h-16 bg-obsidian border border-blue-500/50 rounded-full flex items-center justify-center shadow-[0_0_15px_rgba(59,130,246,0.4)]">
                        <span class="rt-icon material-symbols-outlined text-white text-lg md:text-2xl">analytics</span>
                    </div>
                </div>
                <div class="absolute inset-0 bg-gradient-radial from-primary/10 to-transparent rounded-full"></div>
            </div>
        </div>

        <div class="max-w-7xl mx-auto relative z-10">
            <div class="mb-16 md:mb-20 flex flex-col md:flex-row md:items-end justify-between gap-6">
                <div>
                    <h2 class="font-display text-4xl md:text-5xl font-bold tracking-tighter text-white mb-2 uppercase">
                        Core <br />Capabilities</h2>
                    <div class="h-1 w-20 bg-gradient-to-r from-primary to-transparent"></div>
                </div>
                <div class="md:text-right max-w-sm">
                    <p class="font-mono text-xs text-primary mb-2">// SERVICES</p>
                    <p class="text-slate-400 text-sm leading-relaxed">Comprehensive web and automation solutions
                        engineered for ambitious growth.</p>
                </div>
            </div>

            <div id="card-scroll-wrapper" class="relative w-full overflow-hidden pb-12">
                <div id="card-stack" class="flex flex-col md:flex-row gap-6 md:gap-12 md:w-max md:pr-32">
                    <div class="stack-card glass-card p-8 rounded-xl flex flex-col md:h-[480px] md:w-[450px] flex-shrink-0 group relative overflow-hidden"
                        style="transform-style: preserve-3d;">
                        <div
                            class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-primary/50 to-transparent transform origin-left scale-x-0 group-hover:scale-x-100 transition-transform duration-500">
                        </div>
                        <div
                            class="mb-8 w-14 h-14 rounded bg-primary/10 flex items-center justify-center border border-primary/20 group-hover:bg-primary/20 group-hover:border-primary/50 transition-colors">
                            <span
                                class="material-symbols-outlined text-3xl text-primary group-hover:text-white transition-colors">auto_fix</span>
                        </div>
                        <h3 class="font-display text-2xl font-bold mb-2 text-white uppercase">Automation &amp; AI</h3>
                        <div class="text-[10px] font-mono text-primary mb-6 tracking-widest uppercase">WORKFLOW_SYSTEMS
                        </div>
                        <p class="text-slate-400 mb-8 text-sm leading-relaxed border-l border-white/5 pl-4">
                            Custom workflows and AI integrations that eliminate manual tasks and scale operations.
                        </p>
                        <div class="mt-auto pt-6 border-t border-white/5">
                            <ul class="space-y-3 text-xs font-mono text-slate-300">
                                <li class="flex items-center gap-3">
                                    <span class="text-primary">&gt;</span> Process_Automation
                                </li>
                                <li class="flex items-center gap-3">
                                    <span class="text-primary">&gt;</span> Custom_LLM_Apps
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="stack-card glass-card p-8 rounded-xl flex flex-col md:h-[480px] md:w-[450px] flex-shrink-0 relative overflow-hidden ring-1 ring-primary/30 shadow-neon"
                        style="transform-style: preserve-3d;">
                        <div
                            class="absolute -top-20 -right-20 w-60 h-60 bg-primary/10 rounded-full blur-3xl pointer-events-none">
                        </div>
                        <div
                            class="mb-8 w-14 h-14 rounded bg-indigo-500 flex items-center justify-center border border-indigo-400 shadow-[0_0_15px_rgba(99,102,241,0.5)]">
                            <span class="material-symbols-outlined text-3xl text-white">swords</span>
                        </div>
                        <h3 class="font-display text-2xl font-bold mb-2 text-white uppercase">Award-Winning Web</h3>
                        <div class="text-[10px] font-mono text-indigo-300 mb-6 tracking-widest uppercase">
                            SITE_ARCHITECTURE</div>
                        <p class="text-slate-300 mb-8 text-sm leading-relaxed border-l border-indigo-500/30 pl-4">
                            High-performance websites and landing pages designed for premium brands and market leaders.
                        </p>
                        <div class="mt-auto pt-6 border-t border-white/10">
                            <ul class="space-y-3 text-xs font-mono text-white">
                                <li class="flex items-center gap-3">
                                    <span class="text-indigo-400 text-lg material-symbols-outlined">bolt</span> Custom
                                    Design
                                </li>
                                <li class="flex items-center gap-3">
                                    <span class="text-indigo-400 text-lg material-symbols-outlined">public</span>
                                    Conversion Focused
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="stack-card glass-card p-8 rounded-xl flex flex-col md:h-[480px] md:w-[450px] flex-shrink-0 group relative overflow-hidden"
                        style="transform-style: preserve-3d;">
                        <div
                            class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-purple-500/50 to-transparent transform origin-left scale-x-0 group-hover:scale-x-100 transition-transform duration-500">
                        </div>
                        <div
                            class="mb-8 w-14 h-14 rounded bg-purple-500/10 flex items-center justify-center border border-purple-500/20 group-hover:bg-purple-500/20 group-hover:border-purple-500/50 transition-colors">
                            <span
                                class="material-symbols-outlined text-3xl text-purple-400 group-hover:text-white transition-colors">query_stats</span>
                        </div>
                        <h3 class="font-display text-2xl font-bold mb-2 text-white uppercase">Agency White-Label</h3>
                        <div class="text-[10px] font-mono text-purple-400 mb-6 tracking-widest uppercase">
                            PARTNERSHIP_TIER</div>
                        <p class="text-slate-400 mb-8 text-sm leading-relaxed border-l border-white/5 pl-4">
                            Reliable development and automation support designed to scale your agency\'s delivery
                            capabilities.
                        </p>
                        <div class="mt-auto pt-6 border-t border-white/5">
                            <ul class="space-y-3 text-xs font-mono text-slate-300">
                                <li class="flex items-center gap-3">
                                    <span class="text-purple-400">&gt;</span> NDA_Protected
                                </li>
                                <li class="flex items-center gap-3">
                                    <span class="text-purple-400">&gt;</span> Seamless_Integration
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="terminal-section" class="py-24 px-6 bg-black relative overflow-hidden">
        <div class="absolute inset-0 opacity-20"
            style="background-image: linear-gradient(#1e1e2e 1px, transparent 1px), linear-gradient(90deg, #1e1e2e 1px, transparent 1px); background-size: 40px 40px;">
        </div>
        <div class="max-w-7xl mx-auto glass-panel border border-white/10 rounded-2xl p-6 md:p-16 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <div>
                    <div
                        class="terminal-step inline-block px-3 py-1 bg-primary/10 rounded text-primary text-[10px] font-mono mb-6 uppercase tracking-widest border border-primary/20">
                        Process Visualization
                    </div>
                    <h2 class="terminal-step font-display text-4xl font-bold mb-6 text-white tracking-tight uppercase">
                        Transmuting Inputs <br />Into <span class="text-primary-glow">Revenue</span></h2>
                    <p class="terminal-step text-slate-400 mb-10 text-base font-light">Our workflows aren\'t just code;
                        they are connected systems that turn customer interaction into business growth without manual
                        bottlenecks.</p>
                    <div class="space-y-4">
                        <div
                            class="terminal-step group flex items-center gap-4 p-4 rounded-lg bg-white/5 hover:bg-white/10 border border-white/5 hover:border-primary/30 transition-all cursor-default">
                            <div
                                class="w-10 h-10 min-w-10 rounded bg-green-900/30 flex items-center justify-center text-green-400 border border-green-500/30 shadow-[0_0_10px_rgba(74,222,128,0.2)]">
                                <span class="material-symbols-outlined text-lg">forum</span>
                            </div>
                            <div>
                                <h4 class="font-mono font-bold text-sm text-green-400">01_LEAD_INTAKE</h4>
                                <p class="text-xs text-slate-500 mt-1">Capture leads via your preferred channels.</p>
                            </div>
                        </div>
                        <div
                            class="terminal-step group flex items-center gap-4 p-4 rounded-lg bg-white/5 hover:bg-white/10 border border-white/5 hover:border-primary/30 transition-all cursor-default">
                            <div
                                class="w-10 h-10 min-w-10 rounded bg-indigo-900/30 flex items-center justify-center text-indigo-400 border border-indigo-500/30 shadow-[0_0_10px_rgba(99,102,241,0.2)]">
                                <span class="material-symbols-outlined text-lg">psychology</span>
                            </div>
                            <div>
                                <h4 class="font-mono font-bold text-sm text-indigo-400">02_DECISION_ENGINE</h4>
                                <p class="text-xs text-slate-500 mt-1">Contextual routing and task generation.</p>
                            </div>
                        </div>
                        <div
                            class="terminal-step group flex items-center gap-4 p-4 rounded-lg bg-white/5 hover:bg-white/10 border border-white/5 hover:border-primary/30 transition-all cursor-default">
                            <div
                                class="w-10 h-10 min-w-10 rounded bg-blue-900/30 flex items-center justify-center text-blue-400 border border-blue-500/30 shadow-[0_0_10px_rgba(96,165,250,0.2)]">
                                <span class="material-symbols-outlined text-lg">database</span>
                            </div>
                            <div>
                                <h4 class="font-mono font-bold text-sm text-blue-400">03_CRM_SYNC</h4>
                                <p class="text-xs text-slate-500 mt-1">Auto-population &amp; schedule handling.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="terminal-hub" class="relative flex items-center justify-center min-h-[300px] md:min-h-[400px]">
                    <div
                        class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/circuit-board.png')] opacity-10">
                    </div>
                    <div
                        class="relative w-full aspect-square max-w-[400px] flex items-center justify-center scale-75 md:scale-100">
                        <div class="absolute w-full h-full border border-primary/10 rounded-full animate-ping"
                            style="animation-duration: 3s"></div>
                        <div class="absolute w-[80%] h-[80%] border border-primary/20 rounded-full animate-ping"
                            style="animation-duration: 3s; animation-delay: 1s"></div>
                        <div
                            class="relative z-20 w-32 h-32 rounded-full bg-black border border-primary/50 shadow-[0_0_30px_rgba(79,70,229,0.4)] flex items-center justify-center">
                            <span class="material-symbols-outlined text-5xl text-primary animate-pulse">hub</span>
                        </div>
                        <div class="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 z-20">
                            <div
                                class="glass-panel px-4 py-2 rounded text-[10px] font-mono text-green-400 border border-green-500/30 shadow-[0_0_15px_rgba(74,222,128,0.3)]">
                                INPUT_SIGNAL
                            </div>
                            <div class="h-16 w-[1px] bg-gradient-to-b from-green-500 to-primary mx-auto"></div>
                        </div>
                        <div class="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-1/2 z-20">
                            <div class="h-16 w-[1px] bg-gradient-to-b from-primary to-blue-500 mx-auto"></div>
                            <div
                                class="glass-panel px-4 py-2 rounded text-[10px] font-mono text-blue-400 border border-blue-500/30 shadow-[0_0_15px_rgba(96,165,250,0.3)]">
                                OUTPUT_DATA
                            </div>
                        </div>
                        <div class="absolute left-0 top-1/2 -translate-x-1/2 -translate-y-1/2 z-20 flex items-center">
                            <div
                                class="glass-panel p-2 rounded-full border border-purple-500/30 shadow-[0_0_15px_rgba(168,85,247,0.3)] bg-black">
                                <span class="material-symbols-outlined text-purple-400 text-sm">bolt</span>
                            </div>
                            <div class="w-12 h-[1px] bg-gradient-to-r from-purple-500 to-primary hidden md:block"></div>
                        </div>
                        <div class="absolute right-0 top-1/2 translate-x-1/2 -translate-y-1/2 z-20 flex items-center">
                            <div class="w-12 h-[1px] bg-gradient-to-r from-primary to-orange-500 hidden md:block"></div>
                            <div
                                class="glass-panel p-2 rounded-full border border-orange-500/30 shadow-[0_0_15px_rgba(249,115,22,0.3)] bg-black">
                                <span class="material-symbols-outlined text-orange-400 text-sm">storage</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION: THE GRAND ARMORY -->
    <section id="grand-armory" class="py-24 px-6 relative bg-obsidian overflow-hidden border-t border-white/5 z-20">
        <div
            class="absolute top-1/2 left-0 -translate-y-1/2 w-[500px] h-[500px] bg-neon-cyan/10 blur-[150px] rounded-full pointer-events-none">
        </div>
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div
                class="armory-visual cf-artifact-frame cf-artifact-frame--terracotta relative h-[400px] md:h-[600px] w-full overflow-hidden glass-panel border border-neon-cyan/20 p-2">
                <div class="cf-artifact-core absolute inset-2 overflow-hidden">
                    <img src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-hero-arsenal.webp'); ?>" alt="Web development toolkit workspace"
                        width="1536" height="1024" loading="lazy" decoding="async"
                        class="cf-artifact-img w-full h-full object-cover img-zoom" />
                </div>
                <!-- Decorative overlay box -->
                <div
                    class="cf-artifact-label absolute bottom-6 right-6 glass-panel px-4 py-2 border border-neon-cyan/50 rounded flex items-center gap-3 shadow-[0_0_20px_rgba(0,242,255,0.3)] bg-obsidian/80">
                    <span class="w-2 h-2 rounded-full bg-neon-cyan animate-pulse"></span>
                    <span class="text-[10px] font-mono text-neon-cyan tracking-widest uppercase">Forge Active</span>
                </div>
                <span class="cf-artifact-node node-a"></span>
                <span class="cf-artifact-node node-b"></span>
                <span class="cf-artifact-node node-c"></span>
            </div>
            <div class="armory-content relative z-10">
                <span class="text-neon-cyan font-mono text-xs uppercase tracking-[0.3em] mb-4 block">//
                    ASSET_REPOSITORY</span>
                <h2
                    class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">
                    Asset<br /><span class="text-neon-cyan text-glow-cyan">Showcase</span></h2>
                <p class="text-white/50 text-base font-light leading-relaxed mb-8">
                    Showcase of past web and automation builds. Explore live projects, concepts, and internal tools
                    built for ambitious companies.
                </p>
                <ul class="space-y-4 mb-10 font-mono text-sm">
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-neon-cyan material-symbols-outlined">folder_special</span> Enterprise-Grade
                        Web Templates
                    </li>
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-neon-cyan material-symbols-outlined">api</span> Headless CMS Architecture
                    </li>
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-neon-cyan material-symbols-outlined">dns</span> Pre-configured Deployment
                        Pipelines
                    </li>
                </ul>
                <button onclick="window.location.href='<?php echo esc_url(home_url('/the-arsenal/')); ?>'"
                    class="bg-obsidian border border-neon-cyan/50 text-neon-cyan px-8 py-4 rounded text-xs font-bold font-mono uppercase tracking-[0.2em] hover:bg-neon-cyan hover:text-obsidian transition-colors shadow-[0_0_15px_rgba(0,242,255,0.2)]">
                    ENTER THE FORGE
                </button>
            </div>
        </div>
    </section>

    <!-- SECTION: THE ALCHEMIST'S SANCTUM -->
    <section id="alchemy-sanctum" class="py-24 px-6 relative bg-obsidian overflow-hidden border-t border-white/5 z-20">
        <div
            class="absolute top-1/2 right-0 -translate-y-1/2 w-[500px] h-[500px] bg-neon-purple/10 blur-[150px] rounded-full pointer-events-none">
        </div>
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="alchemy-content relative z-10 order-2 lg:order-1">
                <span class="text-neon-purple font-mono text-xs uppercase tracking-[0.3em] mb-4 block">//
                    SYSTEM_AUTOMATION</span>
                <h2
                    class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">
                    Workflow<br /><span class="text-neon-purple text-glow-purple">Automations</span></h2>
                <p class="text-white/50 text-base font-light leading-relaxed mb-8">
                    Turn manual data entry into automated action. We build robust automation scripts, connected systems,
                    and custom workflows that operate relentlessly and save hundreds of hours.
                </p>
                <ul class="space-y-4 mb-10 font-mono text-sm">
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-neon-purple material-symbols-outlined">model_training</span> Bespoke AI Agent
                        Scripts
                    </li>
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-neon-purple material-symbols-outlined">neurology</span> LLM Workflow
                        Synthesizers
                    </li>
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-neon-purple material-symbols-outlined">smart_toy</span> 24/7 Autonomous
                        Execution
                    </li>
                </ul>
                <button onclick="window.location.href='<?php echo esc_url(home_url('/merlin-protocol/')); ?>'"
                    class="bg-obsidian border border-neon-purple/50 text-neon-purple px-8 py-4 rounded text-xs font-bold font-mono uppercase tracking-[0.2em] hover:bg-neon-purple hover:text-obsidian transition-colors shadow-[0_0_15px_rgba(191,0,255,0.2)]">
                    VIEW AUTOMATIONS
                </button>
            </div>
            <div
                class="alchemy-visual cf-artifact-frame cf-artifact-frame--sage relative h-[400px] md:h-[600px] w-full overflow-hidden glass-panel border border-neon-purple/20 p-2 order-1 lg:order-2">
                <div class="cf-artifact-core absolute inset-2 overflow-hidden">
                    <img src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-hero-merlin.webp'); ?>" alt="Cozy AI automation command center"
                        width="1536" height="1024" loading="lazy" decoding="async"
                        class="cf-artifact-img w-full h-full object-cover img-zoom" />
                </div>
                <!-- Decorative overlay box -->
                <div
                    class="cf-artifact-label absolute top-6 left-6 glass-panel px-4 py-2 border border-neon-purple/50 rounded flex items-center gap-3 shadow-[0_0_20px_rgba(191,0,255,0.3)] bg-obsidian/80">
                    <span class="w-2 h-2 rounded-full bg-neon-purple animate-pulse"></span>
                    <span class="text-[10px] font-mono text-neon-purple tracking-widest uppercase">Run Sequence</span>
                </div>
                <span class="cf-artifact-node node-a"></span>
                <span class="cf-artifact-node node-b"></span>
                <span class="cf-artifact-node node-c"></span>
            </div>
        </div>
    </section>

    <!-- SECTION: THE OBSIDIAN VAULT -->
    <section id="obsidian-vault" class="py-24 px-6 relative bg-obsidian overflow-hidden border-t border-white/5 z-20">
        <div
            class="absolute top-1/2 left-0 -translate-y-1/2 w-[500px] h-[500px] bg-emerald-500/10 blur-[150px] rounded-full pointer-events-none">
        </div>
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div
                class="vault-visual cf-artifact-frame cf-artifact-frame--terracotta relative h-[400px] md:h-[600px] w-full overflow-hidden glass-panel border border-emerald-500/20 p-2">
                <div class="cf-artifact-core absolute inset-2 overflow-hidden">
                    <img src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-case-site.webp'); ?>" alt="Website rebuild before and after workspace"
                        width="1672" height="941" loading="lazy" decoding="async"
                        class="cf-artifact-img w-full h-full object-cover img-zoom" />
                </div>
                <div
                    class="cf-artifact-label absolute bottom-6 left-6 glass-panel px-4 py-2 border border-emerald-500/50 rounded flex items-center gap-3 shadow-[0_0_20px_rgba(16,185,129,0.3)] bg-obsidian/80">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                    <span class="text-[10px] font-mono text-emerald-400 tracking-widest uppercase">Design
                        Perfected</span>
                </div>
                <span class="cf-artifact-node node-a"></span>
                <span class="cf-artifact-node node-b"></span>
                <span class="cf-artifact-node node-c"></span>
            </div>
            <div class="vault-content relative z-10">
                <span class="text-emerald-400 font-mono text-xs uppercase tracking-[0.3em] mb-4 block">//
                    SECURITY_CORE</span>
                <h2
                    class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">
                    Aesthetic<br /><span class="text-emerald-400 text-glow"
                        style="text-shadow: 0 0 20px rgba(16,185,129,0.5)">Excellence</span></h2>
                <p class="text-white/50 text-base font-light leading-relaxed mb-8">
                    Elevate your brand with premium UI/UX interfaces and fluid animations. We architect visually
                    stunning digital experiences that convert.
                </p>
                <ul class="space-y-4 mb-10 font-mono text-sm">
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-emerald-400 material-symbols-outlined">design_services</span> Pixel-Perfect
                        Layouts
                    </li>
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-emerald-400 material-symbols-outlined">animation</span> Fluid
                        Micro-Interactions
                    </li>
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-emerald-400 material-symbols-outlined">diamond</span> Premium Brand Identity
                    </li>
                </ul>
            </div>
        </div>
    </section>

    <!-- SECTION: CYBERNETIC AUGMENTATIONS -->
    <section id="cybernetic-augmentations"
        class="py-24 px-6 relative bg-obsidian overflow-hidden border-t border-white/5 z-20">
        <div
            class="absolute top-1/2 right-0 -translate-y-1/2 w-[500px] h-[500px] bg-indigo-500/10 blur-[150px] rounded-full pointer-events-none">
        </div>
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="aug-content relative z-10 order-2 lg:order-1">
                <span class="text-indigo-400 font-mono text-xs uppercase tracking-[0.3em] mb-4 block">//
                    INFRASTRUCTURE_SYNC</span>
                <h2
                    class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">
                    System<br /><span class="text-indigo-400 text-glow"
                        style="text-shadow: 0 0 20px rgba(99,102,241,0.5)">Integrations</span></h2>
                <p class="text-white/50 text-base font-light leading-relaxed mb-8">
                    Seamlessly integrate our modules into your existing architecture. We connect custom tools with your
                    CRM/ERP systems, transforming disconnected workflows into a unified setup.
                </p>
                <ul class="space-y-4 mb-10 font-mono text-sm">
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-indigo-400 material-symbols-outlined">hub</span> Legacy CRM Integration
                    </li>
                    <li class="flex items-center gap-4 text-white/70">
                        <span class="text-indigo-400 material-symbols-outlined">insights</span> Hyper-Cognizant
                        Analytics
                    </li>
                </ul>
            </div>
            <div
                class="aug-visual cf-artifact-frame cf-artifact-frame--cobalt relative h-[400px] md:h-[600px] w-full overflow-hidden glass-panel border border-indigo-500/20 p-2 order-1 lg:order-2">
                <div class="cf-artifact-core absolute inset-2 overflow-hidden">
                    <img src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-case-roundtable.webp'); ?>" alt="Connected website and automation planning system"
                        width="1672" height="941" loading="lazy" decoding="async"
                        class="cf-artifact-img w-full h-full object-cover img-zoom" />
                </div>
                <div
                    class="cf-artifact-label absolute top-6 right-6 glass-panel px-4 py-2 border border-indigo-500/50 rounded flex items-center gap-3 shadow-[0_0_20px_rgba(99,102,241,0.3)] bg-obsidian/80">
                    <span class="w-2 h-2 rounded-full bg-indigo-400 animate-pulse"></span>
                    <span class="text-[10px] font-mono text-indigo-400 tracking-widest uppercase">Sync Active</span>
                </div>
                <span class="cf-artifact-node node-a"></span>
                <span class="cf-artifact-node node-b"></span>
                <span class="cf-artifact-node node-c"></span>
            </div>
        </div>
    </section>

    <!-- Star Wars Scrolling Pricing from Stitch Generation (Neon Purple Cyberpunk Redesign) -->
    <section id="starwars-pricing" class="h-screen w-full relative flex flex-col z-30 border-t border-white/5">
        <div class="starfield-anim"></div>

        <!-- Violet Network Wires Background -->
        <div
            class="absolute inset-0 z-0 flex items-center justify-center pointer-events-none opacity-40 mix-blend-screen overflow-hidden">
            <svg class="h-[150%] w-[150%] network-wires rotate-90 md:rotate-0" viewBox="0 0 1000 1000"
                preserveAspectRatio="xMidYMid slice">
                <defs>
                    <linearGradient id="neon-cyan-purple" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="#00f2ff" />
                        <stop offset="100%" stop-color="#bf00ff" />
                    </linearGradient>
                    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
                        <feGaussianBlur stdDeviation="3" result="blur" />
                        <feComposite in="SourceGraphic" in2="blur" operator="over" />
                    </filter>
                </defs>
                <!-- Background grid lines -->
                <g stroke="#bf00ff" stroke-width="1" opacity="0.1">
                    <line x1="0" y1="200" x2="1000" y2="200" />
                    <line x1="0" y1="400" x2="1000" y2="400" />
                    <line x1="0" y1="600" x2="1000" y2="600" />
                    <line x1="0" y1="800" x2="1000" y2="800" />
                    <line x1="200" y1="0" x2="200" y2="1000" />
                    <line x1="400" y1="0" x2="400" y2="1000" />
                    <line x1="600" y1="0" x2="600" y2="1000" />
                    <line x1="800" y1="0" x2="800" y2="1000" />
                </g>
                <!-- Animated Circuit Wires -->
                <g stroke="url(#neon-cyan-purple)" stroke-linecap="round" stroke-linejoin="round" fill="none"
                    filter="url(#neon-glow)">
                    <path d="M 500 0 L 500 150 L 200 150 L 200 450 L 50 450" class="circuit-wire" stroke-width="3" />
                    <path d="M 500 0 L 500 250 L 300 250 L 300 700 L 100 700" class="circuit-wire" stroke-width="2" />
                    <path d="M 500 0 L 500 100 L 800 100 L 800 600 L 950 600" class="circuit-wire" stroke-width="2.5" />
                    <path d="M 500 0 L 500 350 L 650 350 L 650 850 L 900 850" class="circuit-wire" stroke-width="4" />
                    <path d="M 500 0 L 500 1000" class="circuit-wire" stroke-width="2.5" stroke="#bf00ff" />
                    <path d="M 450 0 L 450 400 L 400 400 L 400 1000" class="circuit-wire" stroke-width="1.5"
                        stroke="#00f2ff" />
                    <path d="M 550 0 L 550 500 L 600 500 L 600 1000" class="circuit-wire" stroke-width="1.5"
                        stroke="#bf00ff" />

                    <!-- Graphic Nodes -->
                    <circle cx="200" cy="150" r="6" fill="#00f2ff" stroke="none" class="circuit-node" />
                    <circle cx="200" cy="450" r="10" fill="#bf00ff" stroke="none" class="circuit-node" />
                    <circle cx="300" cy="250" r="4" fill="#00f2ff" stroke="none" class="circuit-node" />
                    <circle cx="300" cy="700" r="8" fill="#00f2ff" stroke="none" class="circuit-node" />
                    <circle cx="800" cy="100" r="8" fill="#bf00ff" stroke="none" class="circuit-node" />
                    <circle cx="800" cy="600" r="12" fill="#00f2ff" stroke="none" class="circuit-node" />
                    <circle cx="650" cy="350" r="5" fill="#bf00ff" stroke="none" class="circuit-node" />
                    <circle cx="650" cy="850" r="10" fill="#bf00ff" stroke="none" class="circuit-node" />
                </g>
            </svg>
        </div>

        <!-- Holographic Sword Centerpiece -->
        <div
            class="absolute inset-0 z-0 flex items-center justify-center opacity-40 mix-blend-screen pointer-events-none hologram-sword-img">
            <img src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-hero-work.webp'); ?>" alt="Productized service planning workspace"
                width="1536" height="1024" loading="lazy" decoding="async"
                class="max-w-[700px] w-full object-contain filter blur-[1px] opacity-60" />
        </div>

        <div class="pricing-blueprint-system" aria-hidden="true">
            <svg class="pricing-blueprint-lines" viewBox="0 0 1200 760" preserveAspectRatio="xMidYMid slice">
                <defs>
                    <linearGradient id="pricingBlueprintStroke" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="currentColor" stop-opacity="0.08" />
                        <stop offset="50%" stop-color="currentColor" stop-opacity="0.32" />
                        <stop offset="100%" stop-color="currentColor" stop-opacity="0.08" />
                    </linearGradient>
                </defs>
                <path class="pricing-blueprint-route" d="M 112 540 H 318 C 390 540 390 380 470 380 H 600" />
                <path class="pricing-blueprint-route" d="M 1088 202 H 858 C 780 202 790 380 680 380 H 600" />
                <path class="pricing-blueprint-route" d="M 254 188 H 420 C 510 188 500 318 600 318" />
                <path class="pricing-blueprint-route" d="M 946 594 H 748 C 682 594 676 442 604 442" />
                <circle cx="600" cy="380" r="172" class="pricing-blueprint-ring" />
                <circle cx="600" cy="380" r="92" class="pricing-blueprint-ring pricing-blueprint-ring--inner" />
            </svg>

            <div class="pricing-blueprint-core">
                <span class="pricing-core-kicker">Engagement Matrix</span>
                <strong>Fixed Scope</strong>
                <span>brief -> build -> handoff</span>
            </div>

            <div class="pricing-route-card route-project">
                <span>01</span>
                <strong>Project</strong>
                <em>launch sprint</em>
            </div>
            <div class="pricing-route-card route-retainer">
                <span>02</span>
                <strong>Retainer</strong>
                <em>monthly support</em>
            </div>
            <div class="pricing-route-card route-agency">
                <span>03</span>
                <strong>Agency</strong>
                <em>white-label flow</em>
            </div>
            <div class="pricing-route-card route-intake">
                <span>IN</span>
                <strong>Brief</strong>
                <em>clear constraints</em>
            </div>
            <div class="pricing-route-card route-handoff">
                <span>OUT</span>
                <strong>Delivery</strong>
                <em>ready to ship</em>
            </div>
        </div>

        <div class="crawl-container relative z-10">
            <div class="crawl-content flex flex-col items-center gap-12 px-6 text-center">

                <div class="max-w-3xl mb-16">
                    <h1 class="text-neon-cyan tracking-[0.5em] text-sm font-bold uppercase mb-6 neon-text-cyan">
                        Engagement Models</h1>
                    <h2
                        class="text-white font-display text-5xl md:text-8xl font-black leading-[1.1] tracking-tighter mb-6 uppercase">
                        CHOOSE YOUR<br /><span
                            class="text-transparent bg-clip-text bg-gradient-to-r from-[#bf00ff] to-[#0066ff]">PATH</span>
                    </h2>
                    <div
                        class="h-[1px] w-24 bg-gradient-to-r from-transparent via-[#bf00ff] to-transparent mx-auto mb-8">
                    </div>
                    <p class="text-white/50 text-xl font-light leading-relaxed max-w-2xl mx-auto">
                        Select how you want to work with us to accelerate your growth.
                    </p>
                </div>

                <!-- Tier 1: Merlin Core -->
                <div
                    class="pricing-card-sw border-cyan glow-cyan w-full flex flex-col md:flex-row gap-8 items-center text-left relative overflow-hidden group">
                    <div class="absolute top-0 right-0 p-4 opacity-10">
                        <span class="material-symbols-outlined text-6xl text-neon-cyan">security</span>
                    </div>
                    <div class="flex-1 flex flex-col gap-4 relative z-10">
                        <div class="flex items-center gap-4">
                            <h3 class="text-white text-3xl font-display font-bold tracking-[0.05em] uppercase">Project
                                Scope</h3>
                            <span
                                class="text-neon-cyan text-[10px] font-bold tracking-[0.3em] uppercase bg-neon-cyan/10 border border-neon-cyan/30 px-3 py-1 rounded">One-Off</span>
                        </div>
                        <div class="flex flex-col gap-3 font-mono mt-4 border-t border-white/5 pt-4">
                            <div class="flex items-center gap-3 text-white/70 text-sm"><span
                                    class="text-neon-cyan material-symbols-outlined text-base">terminal</span> Basic
                                Holo-Stream Access</div>
                            <div class="flex items-center gap-3 text-white/70 text-sm"><span
                                    class="text-neon-cyan material-symbols-outlined text-base">memory</span> Obsidian
                                Terminal Skin</div>
                            <div class="flex items-center gap-3 text-white/70 text-sm"><span
                                    class="text-neon-cyan material-symbols-outlined text-base">hub</span> 3-Node Uplink
                                Support</div>
                        </div>
                    </div>
                    <div
                        class="flex flex-col items-end gap-4 min-w-[200px] border-l border-white/10 pl-8 ml-4 relative z-10">
                        <div class="flex items-baseline gap-2">
                            <div
                                class="text-neon-cyan text-5xl md:text-6xl font-black font-mono tracking-tighter neon-text-cyan">
                                $150</div>
                        </div>
                        <div class="text-white/40 text-xs font-mono tracking-widest uppercase mb-4">/cycle</div>
                        <button onclick="window.location.href='<?php echo esc_url(home_url('/contact/?objective=project')); ?>'"
                            class="bg-neon-cyan/10 border border-neon-cyan/50 text-neon-cyan w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-cyan hover:text-obsidian transition-all duration-300 text-center cursor-pointer">Start
                            Project</button>
                    </div>
                </div>

                <!-- Tier 2: Percival Data -->
                <div
                    class="pricing-card-sw border-purple glow-purple w-full flex flex-col md:flex-row gap-8 items-center text-left relative overflow-hidden scale-105">
                    <div class="absolute -top-12 -right-12 w-32 h-32 bg-neon-purple/20 blur-3xl pointer-events-none">
                    </div>
                    <div class="absolute top-0 right-0 p-4 opacity-20">
                        <span
                            class="material-symbols-outlined text-6xl text-neon-purple neon-text-purple">rocket_launch</span>
                    </div>
                    <div class="flex-1 flex flex-col gap-4 relative z-10">
                        <div class="flex items-center gap-4">
                            <h3 class="text-white text-3xl font-display font-bold tracking-[0.05em] uppercase">Vanguard
                                Support</h3>
                            <span
                                class="text-neon-purple text-[10px] font-bold tracking-[0.3em] uppercase bg-neon-purple/10 border border-neon-purple/30 px-3 py-1 rounded neon-text-purple">Retainer</span>
                        </div>
                        <div class="flex flex-col gap-3 font-mono mt-4 border-t border-white/5 pt-4">
                            <div class="flex items-center gap-3 text-white/90 text-sm"><span
                                    class="text-neon-purple material-symbols-outlined text-base">dataset</span>
                                Hyper-Data Mining Matrix</div>
                            <div class="flex items-center gap-3 text-white/90 text-sm"><span
                                    class="text-neon-purple material-symbols-outlined text-base">blur_on</span> Purple
                                Glow UI Interface</div>
                            <div class="flex items-center gap-3 text-white/90 text-sm"><span
                                    class="text-neon-purple material-symbols-outlined text-base">bolt</span>
                                Zero-Latency Feed</div>
                        </div>
                    </div>
                    <div
                        class="flex flex-col items-end gap-4 min-w-[200px] border-l border-white/10 pl-8 ml-4 relative z-10">
                        <div class="flex items-baseline gap-2">
                            <div
                                class="text-neon-purple text-5xl md:text-6xl font-black font-mono tracking-tighter neon-text-purple">
                                $450</div>
                        </div>
                        <div class="text-white/40 text-xs font-mono tracking-widest uppercase mb-4">/cycle</div>
                        <button onclick="window.location.href='<?php echo esc_url(home_url('/contact/?objective=retainer')); ?>'"
                            class="bg-neon-purple text-obsidian w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-white hover:text-black transition-colors text-center shadow-[0_0_20px_rgba(191,0,255,0.4)] cursor-pointer">Discuss
                            Retainer</button>
                    </div>
                </div>

                <!-- Tier 3: Excalibur Env -->
                <div
                    class="pricing-card-sw border-blue glow-blue w-full flex flex-col md:flex-row gap-8 items-center text-left relative overflow-hidden group">
                    <div class="absolute top-0 right-0 p-4 opacity-10">
                        <span class="material-symbols-outlined text-6xl text-neon-blue">diamond</span>
                    </div>
                    <div class="flex-1 flex flex-col gap-4 relative z-10">
                        <div class="flex items-center gap-4">
                            <h3 class="text-white text-3xl font-display font-bold tracking-[0.05em] uppercase">Agency
                                Partner</h3>
                            <span
                                class="text-neon-blue text-[10px] font-bold tracking-[0.3em] uppercase bg-neon-blue/10 border border-neon-blue/30 px-3 py-1 rounded">White-Label</span>
                        </div>
                        <div class="flex flex-col gap-3 font-mono mt-4 border-t border-white/5 pt-4">
                            <div class="flex items-center gap-3 text-white/70 text-sm"><span
                                    class="text-neon-blue material-symbols-outlined text-base">public</span> Full
                                Galactic Environment</div>
                            <div class="flex items-center gap-3 text-white/70 text-sm"><span
                                    class="text-neon-blue material-symbols-outlined text-base">view_in_ar</span> 3D
                                Perspective Analytics</div>
                            <div class="flex items-center gap-3 text-white/70 text-sm"><span
                                    class="text-neon-blue material-symbols-outlined text-base">gavel</span> 24/7 Council
                                Governance</div>
                        </div>
                    </div>
                    <div
                        class="flex flex-col items-end gap-4 min-w-[200px] border-l border-white/10 pl-8 ml-4 relative z-10">
                        <div class="flex items-baseline gap-2">
                            <div
                                class="text-neon-blue text-5xl md:text-6xl font-black font-mono tracking-tighter neon-text-blue">
                                $900<span class="text-3xl">+</span></div>
                        </div>
                        <div class="text-white/40 text-xs font-mono tracking-widest uppercase mb-4">/cycle</div>
                        <button onclick="window.location.href='<?php echo esc_url(home_url('/for-agencies/')); ?>'"
                            class="bg-neon-blue/10 border border-neon-blue/50 text-neon-blue w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-blue hover:text-white transition-all duration-300 text-center cursor-pointer">Learn
                            More</button>
                    </div>
                </div>

                <div class="py-24 text-center space-y-4">
                    <p class="text-white/30 text-[10px] tracking-[0.4em] uppercase">Encryption: AES-256 Quantum</p>
                    <p class="text-white/20 text-[8px] tracking-[0.2em] uppercase">Sector: 7-G | Terminal: 0x82...F9</p>
                </div>

            </div>
        </div>
    </section>

    <section class="py-16 px-6 border-b border-white/5">
        <div class="max-w-7xl mx-auto text-center">
            <p class="text-[10px] font-mono uppercase tracking-[0.3em] text-slate-500 mb-12">
                [TRUSTED_BY_SOVEREIGNS]
            </p>
            <div class="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-60">
                <div class="flex items-center gap-2 group cursor-default">
                    <span
                        class="material-symbols-outlined text-3xl group-hover:text-white transition-colors">payments</span>
                    <span
                        class="font-display text-xl font-bold tracking-tighter group-hover:text-white transition-colors italic">PAYNET</span>
                </div>
                <div class="flex items-center gap-2 group cursor-default">
                    <span
                        class="material-symbols-outlined text-3xl group-hover:text-white transition-colors">account_balance</span>
                    <span
                        class="font-display text-xl font-bold tracking-tighter group-hover:text-white transition-colors italic">GLOBALBANK</span>
                </div>
                <div class="flex items-center gap-2 group cursor-default">
                    <span
                        class="material-symbols-outlined text-3xl group-hover:text-white transition-colors">security</span>
                    <span
                        class="font-display text-xl font-bold tracking-tighter group-hover:text-white transition-colors italic">SECUREFLOW</span>
                </div>
                <div class="flex items-center gap-2 group cursor-default">
                    <span
                        class="material-symbols-outlined text-3xl group-hover:text-white transition-colors">public</span>
                    <span
                        class="font-display text-xl font-bold tracking-tighter group-hover:text-white transition-colors italic">HYPERNODE</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials ─────────────────────────────────────────── -->
    <section class="py-24 px-6 relative" id="testimonials">
        <div class="absolute inset-0 grid-bg opacity-20" aria-hidden="true"></div>
        <div class="max-w-7xl mx-auto relative z-10">
            <div class="text-center mb-16">
                <span class="text-primary-glow font-mono text-xs uppercase tracking-widest mb-4 block">// CLIENT_VOICES</span>
                <h2 class="font-display text-4xl md:text-5xl font-black text-white uppercase tracking-tighter mb-4">
                    In Their <span class="text-accent text-glow">Own Words</span>
                </h2>
                <p class="text-slate-400 text-sm max-w-xl mx-auto leading-relaxed">Every project is a working partnership — these clients describe what that actually felt like.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

                <!-- Vasile – Timberkids -->
                <div class="glass-card rounded-xl p-8 relative border border-primary/20 transition-all duration-300">
                    <div class="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-primary/70 to-accent/50 rounded-l-xl" aria-hidden="true"></div>
                    <div class="mb-5 pl-1" style="color:#f59e0b;font-size:1.05rem;letter-spacing:3px" aria-label="5 stars">★★★★★</div>
                    <blockquote class="text-white/70 text-sm leading-relaxed mb-8 pl-1">
                        "Working with Alexandru felt less like hiring a developer and more like gaining a creative partner. The site launched in under two weeks — buttery smooth, every animation pixel-perfect. Parents comment on it constantly."
                    </blockquote>
                    <div class="flex items-center gap-3 pl-1">
                        <div class="w-10 h-10 rounded-full bg-gradient-to-br from-primary/60 to-accent/60 flex items-center justify-center text-white font-bold font-mono text-sm flex-shrink-0" aria-hidden="true">V</div>
                        <div>
                            <strong class="text-white text-sm font-semibold block leading-tight">Vasile Enache</strong>
                            <span class="text-primary-glow text-xs font-mono">Timberkids</span>
                        </div>
                    </div>
                </div>

                <!-- Alex – First Line Garage Door -->
                <div class="glass-card rounded-xl p-8 relative border border-primary/20 transition-all duration-300">
                    <div class="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-accent/70 to-primary/50 rounded-l-xl" aria-hidden="true"></div>
                    <div class="mb-5 pl-1" style="color:#f59e0b;font-size:1.05rem;letter-spacing:3px" aria-label="5 stars">★★★★★</div>
                    <blockquote class="text-white/70 text-sm leading-relaxed mb-8 pl-1">
                        "I gave Alexandru a rough brief and a firm deadline. He came back with a design I hadn't imagined and the finished site three days early. Lead volume is noticeably up — our old site is embarrassing to look at now."
                    </blockquote>
                    <div class="flex items-center gap-3 pl-1">
                        <div class="w-10 h-10 rounded-full bg-gradient-to-br from-accent/60 to-primary/60 flex items-center justify-center text-white font-bold font-mono text-sm flex-shrink-0" aria-hidden="true">A</div>
                        <div>
                            <strong class="text-white text-sm font-semibold block leading-tight">Alex Petrov</strong>
                            <span class="text-primary-glow text-xs font-mono">First Line Garage Door</span>
                        </div>
                    </div>
                </div>

                <!-- Andrei – Legal Point -->
                <div class="glass-card rounded-xl p-8 relative border border-primary/20 transition-all duration-300">
                    <div class="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-cobalt/70 to-primary/50 rounded-l-xl" aria-hidden="true"></div>
                    <div class="mb-5 pl-1" style="color:#f59e0b;font-size:1.05rem;letter-spacing:3px" aria-label="5 stars">★★★★★</div>
                    <blockquote class="text-white/70 text-sm leading-relaxed mb-8 pl-1">
                        "We needed a site that reflected the seriousness of our firm without feeling cold. Alexandru understood immediately — clean, authoritative, and the Merlin AI contact flow saves our team hours every week."
                    </blockquote>
                    <div class="flex items-center gap-3 pl-1">
                        <div class="w-10 h-10 rounded-full bg-gradient-to-br from-cobalt/60 to-primary/60 flex items-center justify-center text-white font-bold font-mono text-sm flex-shrink-0" aria-hidden="true">A</div>
                        <div>
                            <strong class="text-white text-sm font-semibold block leading-tight">Andrei Moraru</strong>
                            <span class="text-primary-glow text-xs font-mono">Legal Point</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    
<?php get_footer(); ?>
