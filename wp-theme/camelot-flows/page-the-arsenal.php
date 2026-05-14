<?php
/* Template Name: The Arsenal */
get_header(); ?>

<main id="arsenal-main" class="relative pt-32 pb-20 px-0 min-h-screen arsenal-wrapper overflow-x-hidden bg-obsidian text-charcoal">
    <!-- Hero Arsenal -->
    <section class="max-w-7xl mx-auto px-6 mb-32 relative z-10 pt-16">
        <div class="text-center">
            <span class="arsenal-reveal block text-neon-cyan font-mono text-sm tracking-[0.3em] uppercase mb-4 decode-reveal" data-target="CAPABILITIES_MATRIX">Capabilities_Matrix</span>
            <h1 class="arsenal-title font-display text-5xl md:text-8xl font-black uppercase tracking-tighter mb-6 text-white text-glow leading-none">
                The <span class="text-neon-cyan decode-reveal" data-target="Arsenal">Arsenal</span>
            </h1>
            <p class="arsenal-sub text-slate-400 text-lg md:text-2xl leading-relaxed max-w-3xl mx-auto font-light">
                Premium digital infrastructure and autonomous business workforces engineered to scale operations and eliminate bottlenecks.
            </p>
        </div>
    </section>

    <!-- Capability 01: High-Performance Digital Infrastructure (Web Architecture) -->
    <section id="cap-web" class="relative w-full bg-black/50 border-y border-white/10 z-20">
        <div class="sticky top-0 w-full flex flex-col justify-center overflow-hidden" style="padding-top:5rem;padding-bottom:3.5rem;">
            <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(0,255,255,0.05),transparent_70%)] pointer-events-none"></div>
            
            <div class="px-6 md:px-12 mb-8 md:mb-16 max-w-7xl mx-auto w-full flex justify-between items-end">
                <div>
                    <h4 class="text-neon-cyan font-mono text-xs md:text-sm tracking-widest uppercase mb-2">01 // Digital Infrastructure</h4>
                    <h2 class="text-white font-display text-4xl md:text-6xl font-bold uppercase tracking-tight">System<br>Architecture</h2>
                </div>
                <div class="hidden md:block text-right max-w-sm">
                    <p class="text-sm text-slate-400">Award-winning, high-conversion visual frameworks. We don't just build sites; we engineer digital assets that dominate mindshare.</p>
                </div>
            </div>

            <!-- Horizontal Scroll Track -->
            <div id="cap-web-scroll" class="flex gap-8 px-6 md:px-12 w-max lg:overflow-visible overflow-x-auto" style="scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:none;">
                <!-- Item 1 -->
                <div class="glass-card snap-start cap-web-card w-[85vw] md:w-[60vw] lg:w-[45vw] flex-shrink-0 h-[50vh] md:h-[60vh] rounded-2xl relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <img src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-hero-arsenal.webp'); ?>" alt="Web development toolkit workspace" width="1536" height="1024" loading="lazy" decoding="async" class="mockup-image w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity duration-700">
                    <div class="absolute bottom-0 left-0 p-8 z-20">
                        <h3 class="text-2xl font-bold text-white mb-2 uppercase tracking-wide">Immersive Frontends</h3>
                        <p class="text-sm text-slate-300">Cinematic user experiences that turn passive viewers into active buyers via micro-interactions and psychology-driven layouts.</p>
                    </div>
                </div>
                
                <!-- Item 2 -->
                <div class="glass-card snap-start cap-web-card w-[85vw] md:w-[60vw] lg:w-[45vw] flex-shrink-0 h-[50vh] md:h-[60vh] rounded-2xl relative overflow-hidden group border-neon-cyan/20">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <img src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-case-site.webp'); ?>" alt="Website rebuild before and after workspace" width="1672" height="941" loading="lazy" decoding="async" class="mockup-image w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-700 mix-blend-multiply">
                    <div class="absolute bottom-0 left-0 p-8 z-20">
                        <h3 class="text-2xl font-bold text-white mb-2 uppercase tracking-wide">Conversion Engineering</h3>
                        <p class="text-sm text-slate-300">Every animation and layout shift is deployed to optimize funnel continuity and maximize strategic ROAS.</p>
                    </div>
                </div>

                <!-- Item 3 -->
                <div class="glass-card snap-start cap-web-card w-[85vw] md:w-[60vw] lg:w-[45vw] flex-shrink-0 h-[50vh] md:h-[60vh] rounded-2xl relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <img src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-case-automation.webp'); ?>" alt="Automation workflow workspace" width="1672" height="941" loading="lazy" decoding="async" class="mockup-image w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity duration-700">
                    <div class="absolute bottom-0 left-0 p-8 z-20 cursor-pointer">
                        <h3 class="text-2xl font-bold text-white mb-2 uppercase tracking-wide cursor-hover">Infinite Scalability</h3>
                        <p class="text-sm text-slate-300 cursor-hover">Headless architectures and edge-deployed networks guaranteeing zero latency regardless of global load volume.</p>
                    </div>
                </div>
            </div>
            
            <div class="absolute bottom-4 left-0 w-full overflow-hidden opacity-20 pointer-events-none">
                <div id="cap-web-marquee" class="whitespace-nowrap font-mono text-neon-cyan text-4xl font-black uppercase tracking-widest flex gap-8">
                    <span>FRAMEWORK // DEPLOYED</span>
                    <span>FRAMEWORK // DEPLOYED</span>
                    <span>FRAMEWORK // DEPLOYED</span>
                    <span>FRAMEWORK // DEPLOYED</span>
                    <span>FRAMEWORK // DEPLOYED</span>
                </div>
            </div>
        </div>
    </section>

    <!-- ── Impact Record ─────────────────────────────────────── -->
    <section id="impact-record" class="relative py-32 px-6 overflow-hidden bg-obsidian impact-bg-top" style="position:relative;z-index:2;border-top:1px solid rgba(99,102,241,0.25);border-bottom:1px solid rgba(99,102,241,0.12);">

        <!-- Animated circuit SVG -->
        <div class="absolute inset-0 pointer-events-none select-none" aria-hidden="true">
            <svg width="100%" height="100%" viewBox="0 0 1440 520" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <pattern id="cf-grid" width="60" height="60" patternUnits="userSpaceOnUse">
                        <path d="M 60 0 L 0 0 0 60" fill="none" stroke="rgba(99,102,241,0.10)" stroke-width="1"/>
                    </pattern>
                    <radialGradient id="cf-glow-l" cx="25%" cy="50%" r="50%">
                        <stop offset="0%" stop-color="rgba(79,70,229,0.22)"/>
                        <stop offset="100%" stop-color="transparent"/>
                    </radialGradient>
                    <radialGradient id="cf-glow-r" cx="75%" cy="50%" r="50%">
                        <stop offset="0%" stop-color="rgba(139,92,246,0.18)"/>
                        <stop offset="100%" stop-color="transparent"/>
                    </radialGradient>
                </defs>
                <rect width="100%" height="100%" fill="url(#cf-grid)"/>
                <rect width="100%" height="100%" fill="url(#cf-glow-l)"/>
                <rect width="100%" height="100%" fill="url(#cf-glow-r)"/>
                <!-- Primary circuit run -->
                <path class="circuit-line"
                      d="M -80,200 L 220,200 L 220,140 L 480,140 L 480,260 L 720,260 L 720,140 L 960,140 L 960,200 L 1220,200 L 1220,300 L 1520,300"
                      stroke="rgba(99,102,241,0.55)" stroke-width="1.5" fill="none"
                      stroke-dasharray="3000" stroke-dashoffset="3000"/>
                <!-- Secondary run -->
                <path class="circuit-line-2"
                      d="M -80,360 L 160,360 L 160,280 L 440,280 L 440,380 L 760,380 L 760,240 L 1040,240 L 1040,360 L 1300,360 L 1300,260 L 1520,260"
                      stroke="rgba(139,92,246,0.38)" stroke-width="1" fill="none"
                      stroke-dasharray="3200" stroke-dashoffset="3200"/>
                <!-- Accent vertical spine -->
                <path class="circuit-line-3"
                      d="M 720,-40 L 720,140 L 760,140 L 760,260 L 720,260 L 720,540"
                      stroke="rgba(0,242,255,0.35)" stroke-width="1" fill="none"
                      stroke-dasharray="1200" stroke-dashoffset="1200"/>
                <!-- Stat column dividers -->
                <line x1="480" y1="80" x2="480" y2="440" stroke="rgba(255,255,255,0.04)" stroke-width="1"/>
                <line x1="960" y1="80" x2="960" y2="440" stroke="rgba(255,255,255,0.04)" stroke-width="1"/>
                <!-- Pulse nodes -->
                <circle class="circuit-node d1" cx="220" cy="200" r="4" fill="rgba(99,102,241,0.7)"/>
                <circle class="circuit-node d2" cx="480" cy="140" r="3" fill="rgba(139,92,246,0.8)"/>
                <circle class="circuit-node d3" cx="720" cy="260" r="5" fill="rgba(0,242,255,0.6)"/>
                <circle class="circuit-node d4" cx="960" cy="140" r="3" fill="rgba(99,102,241,0.7)"/>
                <circle class="circuit-node d5" cx="1220" cy="200" r="4" fill="rgba(139,92,246,0.6)"/>
                <circle class="circuit-node d2" cx="440" cy="280" r="3" fill="rgba(99,102,241,0.5)"/>
                <circle class="circuit-node d4" cx="760" cy="240" r="4" fill="rgba(0,242,255,0.5)"/>
                <circle class="circuit-node d1" cx="1040" cy="360" r="3" fill="rgba(139,92,246,0.6)"/>
                <!-- Halo rings behind stat numbers -->
                <circle cx="240"  cy="260" r="80" fill="none" stroke="rgba(79,70,229,0.05)"  stroke-width="60"/>
                <circle cx="720"  cy="260" r="80" fill="none" stroke="rgba(139,92,246,0.04)" stroke-width="60"/>
                <circle cx="1200" cy="260" r="80" fill="none" stroke="rgba(0,242,255,0.04)"  stroke-width="60"/>
            </svg>
        </div>

        <!-- Floating particles -->
        <div class="absolute inset-0 pointer-events-none" aria-hidden="true">
            <div class="circuit-particle" style="left:12%;top:70%;animation-delay:0s;animation-duration:5s"></div>
            <div class="circuit-particle" style="left:33%;top:55%;animation-delay:1.8s;animation-duration:6s"></div>
            <div class="circuit-particle" style="left:55%;top:75%;animation-delay:0.9s;animation-duration:4.5s"></div>
            <div class="circuit-particle" style="left:72%;top:60%;animation-delay:2.5s;animation-duration:5.5s"></div>
            <div class="circuit-particle" style="left:88%;top:68%;animation-delay:1.2s;animation-duration:5s"></div>
        </div>

        <div class="max-w-7xl mx-auto relative z-10">

            <!-- Header -->
            <div class="text-center mb-24">
                <span class="text-primary-glow font-mono text-xs uppercase tracking-[0.4em] mb-5 block">// DEPLOYMENT_RECORD</span>
                <h2 class="font-display text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-5 leading-none">
                    Built to <span class="text-candle text-glow-cyan">deliver.</span>
                </h2>
                <p class="text-slate-500 text-sm max-w-sm mx-auto leading-relaxed font-mono">
                    Every engagement is scoped, priced, and shipped to a contractual standard.
                </p>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-1 md:grid-cols-3 impact-divider divide-y md:divide-y-0 md:divide-x divide-white/5 rounded-2xl overflow-hidden border border-white/5">

                <!-- Stat 1 — 14 days -->
                <div class="relative px-10 py-14 text-center group hover:bg-white/3 transition-colors duration-500">
                    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="font-display text-8xl md:text-9xl font-black leading-none mb-4 tabular-nums">
                        <span class="text-white">14</span><span class="impact-accent-1 text-primary-glow text-4xl align-super ml-1 font-mono">d</span>
                    </div>
                    <div class="impact-accent-1 text-primary-glow font-mono text-xs tracking-[0.3em] uppercase mb-4">Average Delivery</div>
                    <p class="text-slate-500 text-sm leading-relaxed max-w-xs mx-auto">
                        From signed contract to live site — not a soft estimate, a contractual commitment.
                    </p>
                </div>

                <!-- Stat 2 — 100% -->
                <div class="relative px-10 py-14 text-center group hover:bg-white/3 transition-colors duration-500">
                    <div class="absolute inset-0 bg-gradient-to-b from-accent/5 to-transparent pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="font-display text-8xl md:text-9xl font-black leading-none mb-4 tabular-nums">
                        <span class="text-white">100</span><span class="impact-accent-2 text-accent text-4xl align-super ml-0.5 font-mono">%</span>
                    </div>
                    <div class="impact-accent-2 text-accent font-mono text-xs tracking-[0.3em] uppercase mb-4">Fixed Scope</div>
                    <p class="text-slate-500 text-sm leading-relaxed max-w-xs mx-auto">
                        One price. No revision traps, no mid-build "out-of-scope" invoices, ever.
                    </p>
                </div>

                <!-- Stat 3 — 3× -->
                <div class="relative px-10 py-14 text-center group hover:bg-white/3 transition-colors duration-500">
                    <div class="absolute inset-0 bg-gradient-to-b from-candle/5 to-transparent pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="font-display text-8xl md:text-9xl font-black leading-none mb-4 tabular-nums">
                        <span class="text-white">3</span><span class="impact-accent-3 text-candle text-4xl align-super ml-1 font-mono">×</span>
                    </div>
                    <div class="impact-accent-3 text-candle font-mono text-xs tracking-[0.3em] uppercase mb-4">Avg. Conversion Lift</div>
                    <p class="text-slate-500 text-sm leading-relaxed max-w-xs mx-auto">
                        Median client conversion rate improvement measured 90 days after launch.
                    </p>
                </div>

            </div>

            <!-- CTA strip -->
            <div class="mt-16 flex justify-center">
                <a href="<?php echo esc_url(home_url('/contact/')); ?>"
                   class="inline-flex items-center gap-3 px-8 py-4 bg-primary/10 border border-primary/30 text-white font-mono text-xs tracking-widest uppercase rounded hover:bg-primary/20 hover:border-primary/60 transition-all duration-300 group">
                    <span class="material-symbols-outlined text-primary-glow text-base group-hover:rotate-45 transition-transform duration-300">arrow_outward</span>
                    Start your deployment
                </a>
            </div>

        </div>
    </section>

    <!-- Capability 02: Autonomous Support Workforces (AI Nodes) -->
    <section id="cap-ai" class="relative py-32 px-6 overflow-hidden">
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_right,rgba(168,85,247,0.08),transparent_50%)] pointer-events-none"></div>
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="ai-left z-10 text-center lg:text-left">
                <h4 class="text-neon-purple font-mono text-sm tracking-widest uppercase mb-4">02 // Business Instrument Automation</h4>
                <h2 class="text-white font-display text-5xl md:text-7xl font-bold uppercase tracking-tight mb-6">Autonomous<br>Workforces</h2>
                <p class="text-slate-400 text-lg mb-8 max-w-xl mx-auto lg:mx-0">
                    Stop scaling headcount linearly with revenue. We integrate advanced AI operational nodes that handle customer routing, internal data compilation, and repetitive logistics at machine speed.
                </p>
                <div class="space-y-4 font-mono text-sm uppercase tracking-wide">
                    <div class="ai-list-item flex items-center justify-center lg:justify-start gap-4 text-slate-200">
                        <span class="material-symbols-outlined text-neon-purple mt-[-2px]">memory</span>
                        <span>24/7 Lead Qualification</span>
                    </div>
                    <div class="ai-list-item flex items-center justify-center lg:justify-start gap-4 text-slate-200">
                        <span class="material-symbols-outlined text-neon-purple mt-[-2px]">hub</span>
                        <span>Multi-System Data Sync</span>
                    </div>
                    <div class="ai-list-item flex items-center justify-center lg:justify-start gap-4 text-slate-200">
                        <span class="material-symbols-outlined text-neon-purple mt-[-2px]">support_agent</span>
                        <span>Tier 1 Support Eradication</span>
                    </div>
                </div>
            </div>
            
            <div class="ai-right relative h-[500px] perspective-1000">
                <div class="absolute inset-0 glass-card rounded-xl border border-neon-purple/30 flex items-center justify-center transform-style-3d hover:-rotate-y-12 hover:rotate-x-12 transition-transform duration-700 overflow-hidden group">
                    <img src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-hero-merlin.webp'); ?>" alt="Cozy AI automation command center" width="1536" height="1024" loading="lazy" decoding="async" class="w-full h-[120%] object-cover opacity-70 group-hover:opacity-95 transition-opacity mix-blend-multiply scale-110 group-hover:scale-100 duration-[2s]">
                    <div class="absolute inset-0 bg-gradient-to-t from-obsidian to-transparent z-10"></div>
                    <div class="absolute inset-0 flex flex-col items-center justify-center z-20">
                        <span class="material-symbols-outlined text-6xl text-neon-purple mb-4 animate-pulse">all_inclusive</span>
                        <div class="text-white font-mono uppercase tracking-widest text-sm border border-neon-purple/50 px-4 py-2 rounded bg-black/50 backdrop-blur-sm cursor-hover">Node Online</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ROI & Technical Matrix -->
    <section id="roi-matrix" class="py-32 bg-black/40 border-y border-white/5 relative z-10 perspective-1000">
        <div class="max-w-7xl mx-auto px-6 text-center mb-16">
            <h2 class="font-display text-4xl font-bold uppercase tracking-widest text-white">Operational Metrics</h2>
            <div class="w-24 h-1 bg-neon-cyan mx-auto mt-6 rounded-full opacity-50"></div>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 max-w-6xl mx-auto gap-8 px-6 transform-style-3d">
            <div class="roi-cell glass-card p-10 rounded-xl text-center border-white/10 hover:border-primary/50 transition-colors bg-gradient-to-b from-white/5 to-transparent backdrop-blur-xl">
                <span class="material-symbols-outlined text-5xl text-primary mb-4 drop-shadow-[0_0_15px_rgba(99,102,241,0.5)]">speed</span>
                <h3 class="text-4xl font-black text-white mb-2 font-mono">0.4s</h3>
                <p class="text-sm text-slate-400 uppercase tracking-widest font-mono">Avg Load Time</p>
                <p class="text-xs text-slate-500 mt-4 leading-relaxed">Achieved via edge caching and aggressive payload optimization.</p>
            </div>
            <div class="roi-cell glass-card p-10 rounded-xl text-center border-white/10 hover:border-neon-purple/50 transition-colors bg-gradient-to-b from-white/5 to-transparent backdrop-blur-xl">
                <span class="material-symbols-outlined text-5xl text-neon-purple mb-4 drop-shadow-[0_0_15px_rgba(168,85,247,0.5)]">monitoring</span>
                <h3 class="text-4xl font-black text-white mb-2 font-mono">+140%</h3>
                <p class="text-sm text-slate-400 uppercase tracking-widest font-mono">Conversion Lift</p>
                <p class="text-xs text-slate-500 mt-4 leading-relaxed">Through trust-generating aesthetics and frictionless UX pathways.</p>
            </div>
            <div class="roi-cell glass-card p-10 rounded-xl text-center border-white/10 hover:border-neon-cyan/50 transition-colors bg-gradient-to-b from-white/5 to-transparent backdrop-blur-xl">
                <span class="material-symbols-outlined text-5xl text-neon-cyan mb-4 drop-shadow-[0_0_15px_rgba(0,255,255,0.5)]">timer_off</span>
                <h3 class="text-4xl font-black text-white mb-2 font-mono">-70%</h3>
                <p class="text-sm text-slate-400 uppercase tracking-widest font-mono">Manual Ops</p>
                <p class="text-xs text-slate-500 mt-4 leading-relaxed">Time reclaimed through automated connective tissue APIs.</p>
            </div>
        </div>
    </section>

    <!-- Final CTA -->
    <section id="final-cta" class="py-32 px-6 max-w-4xl mx-auto text-center relative z-20">
        <div class="glass-card p-12 md:p-16 rounded-2xl border-primary/40 relative overflow-hidden cursor-hover">
            <div class="absolute inset-0 bg-gradient-to-br from-primary/10 to-transparent"></div>
            <img id="cta-core-img" src="<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-hero-work.webp'); ?>" width="1536" height="1024" loading="lazy" decoding="async" class="absolute inset-0 w-full h-[150%] object-cover mix-blend-multiply opacity-15 blur-sm scale-110 pointer-events-none" alt="">
            <div class="relative z-10">
                <h2 class="text-4xl md:text-5xl font-display font-black uppercase text-white mb-6 tracking-tight">Deploy to your<br><span class="text-primary-glow">Enterprise</span></h2>
                <p class="text-slate-300 mb-10 text-lg">Stop relying on outdated infrastructure. Equip your business with the ultimate digital arsenal.</p>
                <a href="<?php echo esc_url(home_url('/contact/')); ?>" class="inline-block bg-primary hover:bg-white text-white hover:text-black hover:shadow-[0_0_30px_rgba(255,255,255,0.4)] px-10 py-4 font-mono font-bold uppercase tracking-widest transition-all duration-300 cursor-hover skew-x-[-10deg]">
                    <span class="skew-x-[10deg] inline-block">Initiate Audit Sequence</span>
                </a>
            </div>
        </div>
    </section>

    <style>
        .text-stroke-1 { -webkit-text-stroke-width: 1px; }
        .text-stroke-white\/20 { -webkit-text-stroke-color: rgba(255,255,255,0.2); }
        .text-stroke-primary\/50 { -webkit-text-stroke-color: rgba(99,102,241,0.5); }
        .transform-style-3d { transform-style: preserve-3d; }
    </style>
</main>

<script>
window.addEventListener("DOMContentLoaded", () => {
    if (typeof gsap === "undefined" || typeof ScrollTrigger === "undefined") return;
    
    // Safety matching
    const mm = gsap.matchMedia();

    mm.add("(min-width: 1024px)", () => {
        // Hero Entrance
        const hTl = gsap.timeline();
        hTl.from(".arsenal-reveal", { y: -30, opacity: 0, duration: 1, ease: "power4.out", delay: 1.0 })
           .from(".arsenal-title", { y: 60, opacity: 0, rotationX: 45, transformOrigin: "bottom", duration: 1.2, ease: "back.out(1.5)" }, "-=0.6")
           .from(".arsenal-sub", { y: 30, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.8");

        // WOW HORIZONTAL SCROLL — GSAP pin (page stops scrolling, track slides)
        const capWeb = document.getElementById("cap-web");
        const capWebScroll = document.getElementById("cap-web-scroll");

        if (capWeb && capWebScroll) {
            // Measure travel from last card's right edge, not scrollWidth (which includes extra space)
            const travelDist = () => {
                const cards = capWebScroll.children;
                if (!cards.length) return 0;
                const last = cards[cards.length - 1];
                const padR = parseFloat(getComputedStyle(capWebScroll).paddingRight) || 0;
                return Math.max(0, last.offsetLeft + last.offsetWidth + padR - window.innerWidth);
            };

            gsap.to(capWebScroll, {
                x: () => -travelDist(),
                ease: "none",
                scrollTrigger: {
                    trigger: capWeb,
                    pin: true,
                    anticipatePin: 1,
                    scrub: 1,
                    start: "top top",
                    end: () => "+=" + travelDist(),
                    invalidateOnRefresh: true
                }
            });

            // Image parallax
            gsap.fromTo(".cap-web-card .mockup-image",
                { scale: 0.88 },
                { scale: 1.04,
                  ease: "none",
                  scrollTrigger: {
                      trigger: capWeb,
                      start: "top top",
                      end: () => "+=" + travelDist(),
                      scrub: 1,
                      invalidateOnRefresh: true
                  }
                }
            );

            // Marquee counter-scroll
            gsap.to("#cap-web-marquee", {
                xPercent: -30,
                ease: "none",
                scrollTrigger: {
                    trigger: capWeb,
                    start: "top bottom",
                    end: "bottom top",
                    scrub: 1
                }
            });
        }

        // Capability 02 (AI nodes 3D reveal)
        const aiTl = gsap.timeline({
            scrollTrigger: {
                trigger: "#cap-ai",
                start: "top 70%",
                toggleActions: "play none none none"
            }
        });
        
        aiTl.from(".ai-left h4, .ai-left h2, .ai-left p", { y: 30, opacity: 0, stagger: 0.15, duration: 1, ease: "power3.out" })
            .from(".ai-list-item", { rotationX: -90, opacity: 0, stagger: 0.2, duration: 1, ease: "back.out(1.4)" }, "-=0.5")
            .from(".ai-right", { x: 100, rotationY: -20, opacity: 0, duration: 1.5, ease: "power4.out" }, "-=1");

        // ROI Matrix card reveal
        gsap.from(".roi-cell", {
            y: 60, opacity: 0,
            stagger: 0.15, duration: 1.2, ease: "power3.out",
            scrollTrigger: {
                trigger: "#roi-matrix",
                start: "top 85%",
                toggleActions: "play none none none",
                invalidateOnRefresh: true,
                once: true
            }
        });

        // CTA Explosive Entrance
        gsap.from("#final-cta .glass-card", {
            scale: 0.8, opacity: 0, y: 100, rotationX: 10, duration: 1.5, ease: "power4.out",
            scrollTrigger: {
                trigger: "#final-cta",
                start: "top 85%"
            }
        });
        
        // CTA Core Image Orbit
        gsap.to("#cta-core-img", {
            scale: 1, filter: "blur(0px)", rotation: 15,
            ease: "none",
            scrollTrigger: {
                trigger: "#final-cta",
                start: "top bottom",
                end: "bottom top",
                scrub: 1
            }
        });
    });
    
    // Mobile fallback (No horizontal pin)
    // CSS in camelot.css handles overflow-x:auto on sticky + overflow-x:visible on track.
    mm.add("(max-width: 1023px)", () => {
        // Reset GSAP transform so the track sits at x:0 (no desktop slide applied)
        gsap.set("#cap-web-scroll", { x: 0, clearProps: "transform" });
        gsap.set("#cap-web-scroll > div", { clearProps: "width,maxWidth,paddingBottom" });
        gsap.set("#cap-web", { minHeight: 0, height: "auto" });
        
        gsap.from(".arsenal-title", { y: 30, opacity: 0, duration: 1, ease: "power4.out", delay: 1 });
        
        const cards = gsap.utils.toArray(".mockup-image, .ai-list-item, .roi-cell, #final-cta .glass-card");
        cards.forEach(card => {
            gsap.from(card, {
                y: 30, opacity: 0, duration: 0.8, ease: "power3.out",
                scrollTrigger: { trigger: card, start: "top 85%" }
            });
        });
    });
});
</script>

<?php get_footer(); ?>
