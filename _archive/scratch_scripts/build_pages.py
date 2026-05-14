import codecs
import json
import shutil
import re

base_file = 'code_v2.html'
with codecs.open(base_file, 'r', 'utf-8') as f:
    content = f.read()

# Dynamically slice the file to ensure stability even if formatted
nav_end = content.find('</nav>')
if nav_end != -1:
    nav_end += len('</nav>')
else:
    raise ValueError("Could not find </nav> tag in code_v2.html")

footer_start = content.find('<footer')
if footer_start == -1:
    raise ValueError("Could not find <footer tag in code_v2.html")

head_part = content[:nav_end]
tail_part = content[footer_start:]

SITE_URL = "https://camelotflows.com"
SITE_NAME = "Camelot Flows"
COZY_IMAGE_BASE = "assets/images/cozy-freelancer"
OG_IMAGE_DEFAULT = f"{COZY_IMAGE_BASE}/cf-cozy-og-default.webp"

def build_page(filename, title, content_html,
               description="", og_image=OG_IMAGE_DEFAULT):
    meta_block = (
        f'    <meta name="description" content="{description}">\n'
        f'    <link rel="canonical" href="{SITE_URL}/{filename}">\n'
        f'    <link rel="icon" href="assets/images/generated/cf-favicon.svg" type="image/svg+xml">\n'
        f'    <!-- Open Graph -->\n'
        f'    <meta property="og:type" content="website">\n'
        f'    <meta property="og:title" content="{SITE_NAME} | {title}">\n'
        f'    <meta property="og:description" content="{description}">\n'
        f'    <meta property="og:image" content="{SITE_URL}/{og_image}">\n'
        f'    <meta property="og:url" content="{SITE_URL}/{filename}">\n'
        f'    <meta property="og:site_name" content="{SITE_NAME}">\n'
        f'    <!-- Twitter Card -->\n'
        f'    <meta name="twitter:card" content="summary_large_image">\n'
        f'    <meta name="twitter:title" content="{SITE_NAME} | {title}">\n'
        f'    <meta name="twitter:description" content="{description}">\n'
        f'    <meta name="twitter:image" content="{SITE_URL}/{og_image}">\n'
    )
    h = head_part.replace(
        '<title>Camelot Flows | Neon Knight Edition</title>',
        f'<title>{SITE_NAME} | {title}</title>\n{meta_block}'
    )
    full = h + '\n' + content_html + '\n' + tail_part
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(full)
    print(f"Generated {filename}")

# ==========================================
# Awwwards-Tier Arsenal Content
# ==========================================
arsenal_content = '''<main id="arsenal-main" class="relative pt-32 pb-20 px-0 min-h-screen arsenal-wrapper overflow-x-hidden bg-obsidian text-charcoal">
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
    <section id="cap-web" class="relative min-h-[200vh] w-full bg-black/50 border-y border-white/10 z-20">
        <div class="sticky top-0 h-screen w-full flex flex-col justify-center overflow-hidden">
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
            <div id="cap-web-scroll" class="flex gap-8 px-6 md:px-12 w-[300vw] lg:w-[250vw]">
                <!-- Item 1 -->
                <div class="glass-card w-[85vw] md:w-[60vw] lg:w-[45vw] flex-shrink-0 h-[50vh] md:h-[60vh] rounded-2xl relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <img src="assets/images/cozy-freelancer/cf-cozy-hero-arsenal.webp" alt="Web development toolkit workspace" width="1536" height="1024" loading="lazy" decoding="async" class="mockup-image w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity duration-700">
                    <div class="absolute bottom-0 left-0 p-8 z-20">
                        <h3 class="text-2xl font-bold text-white mb-2 uppercase tracking-wide">Immersive Frontends</h3>
                        <p class="text-sm text-slate-300">Cinematic user experiences that turn passive viewers into active buyers via micro-interactions and psychology-driven layouts.</p>
                    </div>
                </div>
                
                <!-- Item 2 -->
                <div class="glass-card w-[85vw] md:w-[60vw] lg:w-[45vw] flex-shrink-0 h-[50vh] md:h-[60vh] rounded-2xl relative overflow-hidden group border-neon-cyan/20">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <img src="assets/images/cozy-freelancer/cf-cozy-case-site.webp" alt="Website rebuild before and after workspace" width="1672" height="941" loading="lazy" decoding="async" class="mockup-image w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-700 mix-blend-multiply">
                    <div class="absolute bottom-0 left-0 p-8 z-20">
                        <h3 class="text-2xl font-bold text-white mb-2 uppercase tracking-wide">Conversion Engineering</h3>
                        <p class="text-sm text-slate-300">Every animation and layout shift is deployed to optimize funnel continuity and maximize strategic ROAS.</p>
                    </div>
                </div>

                <!-- Item 3 -->
                <div class="glass-card w-[85vw] md:w-[60vw] lg:w-[45vw] flex-shrink-0 h-[50vh] md:h-[60vh] rounded-2xl relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <img src="assets/images/cozy-freelancer/cf-cozy-case-automation.webp" alt="Automation workflow workspace" width="1672" height="941" loading="lazy" decoding="async" class="mockup-image w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity duration-700">
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
                    <img src="assets/images/cozy-freelancer/cf-cozy-hero-merlin.webp" alt="Cozy AI automation command center" width="1536" height="1024" loading="lazy" decoding="async" class="w-full h-[120%] object-cover opacity-70 group-hover:opacity-95 transition-opacity mix-blend-multiply scale-110 group-hover:scale-100 duration-[2s]">
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
            <img id="cta-core-img" src="assets/images/cozy-freelancer/cf-cozy-hero-work.webp" width="1536" height="1024" loading="lazy" decoding="async" class="absolute inset-0 w-full h-[150%] object-cover mix-blend-multiply opacity-15 blur-sm scale-110 pointer-events-none" alt="">
            <div class="relative z-10">
                <h2 class="text-4xl md:text-5xl font-display font-black uppercase text-white mb-6 tracking-tight">Deploy to your<br><span class="text-primary-glow">Enterprise</span></h2>
                <p class="text-slate-300 mb-10 text-lg">Stop relying on outdated infrastructure. Equip your business with the ultimate digital arsenal.</p>
                <a href="contact.html" class="inline-block bg-primary hover:bg-white text-white hover:text-black hover:shadow-[0_0_30px_rgba(255,255,255,0.4)] px-10 py-4 font-mono font-bold uppercase tracking-widest transition-all duration-300 cursor-hover skew-x-[-10deg]">
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

        // WOW HORIZONTAL SCROLL
        const capWeb = document.getElementById("cap-web");
        const capWebScroll = document.getElementById("cap-web-scroll");
        
        if (capWeb && capWebScroll) {
            gsap.to(capWebScroll, {
                x: () => -(capWebScroll.scrollWidth - window.innerWidth),
                ease: "none",
                scrollTrigger: {
                    trigger: capWeb,
                    pin: true,
                    scrub: 1,
                    start: "top top",
                    end: () => "+=" + capWebScroll.scrollWidth
                }
            });
            
            // Image parallax inside horizontal scroll
            gsap.fromTo(".mockup-image", 
                { scale: 0.8, rotationY: -15 }, 
                { scale: 1.05, rotationY: 0, 
                  ease: "none",
                  scrollTrigger: {
                      trigger: capWeb,
                      start: "top top",
                      end: () => "+=" + capWebScroll.scrollWidth,
                      scrub: 1
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

        // ROI Matrix 3D Magnetic Pop Extreme Base Depth
        gsap.from(".roi-cell", {
            z: -800, rotationX: 45, rotationY: -45, opacity: 0,
            stagger: 0.2, duration: 1.5, ease: "power4.out",
            scrollTrigger: {
                trigger: "#roi-matrix",
                start: "top 70%",
                toggleActions: "play none none none"
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
    mm.add("(max-width: 1023px)", () => {
        gsap.set("#cap-web-scroll", { width: "100%", flexDirection: "column" });
        gsap.set("#cap-web-scroll > div", { width: "100%", paddingBottom: "3rem" });
        gsap.set("#cap-web", { height: "auto" });
        
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
</script>'''

merlin_content = '''<main class="page-shell" style="padding-top:88px">

  <!-- Hero -->
  <section style="padding:96px 0 56px;position:relative;">
    <div aria-hidden="true" style="position:absolute;inset:0;background:url('assets/images/cozy-freelancer/cf-cozy-hero-merlin.webp') center/cover no-repeat;opacity:0.11;mix-blend-mode:multiply;pointer-events:none;"></div>
    <div class="container" style="position:relative;z-index:1;">
      <div class="hero-copy">
        <p class="hero-eyebrow">AI Automation · The Merlin System</p>
        <h1 class="hero-title">An AI agent that runs your <em class="accent">front-of-house.</em></h1>
        <p class="hero-lead">Merlin is a custom-built AI agent trained on your business context. It handles lead qualification, tier-1 support, and CRM sync — 24/7, without growing your headcount.</p>
        <div class="button-row">
          <a href="contact.html?service=staff" class="button primary">Book a demo</a>
          <a href="work-with-me.html" class="button ghost">See pricing</a>
        </div>
      </div>
    </div>
  </section>

  <!-- What Merlin does -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div class="section-header">
        <p class="section-kicker">Capabilities</p>
        <h2 class="section-title">What it replaces.</h2>
        <p class="section-copy">Every item below is something a human was doing manually before Merlin arrived. After setup, it runs on its own.</p>
      </div>
      <div class="grid-3">
        <div class="card">
          <p class="card-meta"><span class="material-symbols-outlined" style="font-size:1.1rem;vertical-align:-3px;color:var(--cf-sage)">smart_toy</span> Lead qualification</p>
          <h3>Inbound triage</h3>
          <p>Merlin reads every inbound message, classifies intent, scores lead quality, and routes to the right action — book a call, send a resource, or flag for your review.</p>
        </div>
        <div class="card highlight">
          <p class="card-meta"><span class="material-symbols-outlined" style="font-size:1.1rem;vertical-align:-3px;color:var(--cf-terracotta)">support_agent</span> Tier-1 support</p>
          <h3>Always-on support</h3>
          <p>FAQs, pricing questions, status checks, booking links — Merlin handles the first layer of support responses with context from your knowledge base. No breaks, no delays.</p>
        </div>
        <div class="card">
          <p class="card-meta"><span class="material-symbols-outlined" style="font-size:1.1rem;vertical-align:-3px;color:var(--cf-cobalt)">cable</span> CRM sync</p>
          <h3>Data without the admin</h3>
          <p>Every conversation writes to your CRM automatically. Contact records, tags, notes, and calendar events created without you touching a spreadsheet.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- How it\'s built -->
  <section class="section">
    <div class="container">
      <div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:start;">
        <div>
          <p class="section-kicker">The build</p>
          <h2 class="section-title">How I set it up.</h2>
          <p style="color:var(--cf-muted);font-size:1.02rem;line-height:1.75;margin:24px 0 0">Every Merlin instance is custom-built for one business. I train it on your docs, your tone, your offers, and your edge cases. Setup takes 2–3 weeks. After that, the monthly fee covers hosting, model costs, and ongoing refinement.</p>
        </div>
        <div style="display:grid;gap:16px;margin-top:4px">
          <div class="stack-card">
            <strong>Week 1 — Knowledge build</strong>
            <p>I ingest your docs, FAQs, pricing, and past conversations to build the context base.</p>
          </div>
          <div class="stack-card">
            <strong>Week 2 — Workflow wiring</strong>
            <p>n8n flows connect Merlin to your CRM, calendar, inbox, and any tools it needs to act.</p>
          </div>
          <div class="stack-card">
            <strong>Week 3 — Testing and handoff</strong>
            <p>We run real scenarios together until you\'re confident it handles your edge cases correctly.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Pricing CTA -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div style="text-align:center;max-width:540px;margin:0 auto">
        <p class="section-kicker">Pricing</p>
        <h2 class="section-title">€2,400 setup · €600/mo</h2>
        <p style="color:var(--cf-muted);font-size:1.02rem;line-height:1.75;margin:20px 0 32px">Fixed setup, cancel anytime. The monthly fee covers Claude API costs, n8n hosting, and my time to keep the agent accurate as your business evolves.</p>
        <div class="button-row" style="justify-content:center">
          <a href="contact.html?service=staff" class="button primary">Book a demo call</a>
          <a href="work-with-me.html" class="button ghost">Full pricing breakdown</a>
        </div>
      </div>
    </div>
  </section>

</main>'''

case_studies_content = '''<main class="page-shell" style="padding-top:88px">

  <!-- Hero -->
  <section style="padding:96px 0 56px;position:relative;">
    <div class="container">
      <div class="hero-copy">
        <p class="hero-eyebrow">Labworks · demonstration projects</p>
        <h1 class="hero-title">Work I take. <em class="accent">Results I deliver.</em></h1>
        <p class="hero-lead">These are composite examples of the kind of project I build — same tools, same process, same scope discipline. Real client case studies will replace these as engagements complete.</p>
      </div>
    </div>
  </section>

  <!-- Case study cards -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div class="grid-3">

        <!-- Case 01 -->
        <div class="card">
          <div style="border-radius:16px;overflow:hidden;margin-bottom:20px;aspect-ratio:16/10;">
            <img src="assets/images/cozy-freelancer/cf-cozy-case-site.webp" alt="Website redesign project" width="1672" height="941" loading="lazy" decoding="async"
                 style="width:100%;height:100%;object-fit:cover;display:block;">
          </div>
          <p class="card-meta">The Site &nbsp;·&nbsp; labwork</p>
          <h3>E-commerce redesign, 12 days</h3>
          <p>A small retailer needed a site that could convert. Existing site was a 2012 WordPress install — no mobile layout, 7-second load time, no CTA structure.</p>
          <ul class="feature-list" style="margin-top:16px">
            <li>Astro + GSAP, rebuilt from scratch</li>
            <li>Product catalogue with Sanity CMS</li>
            <li>AI form-handler for quote requests</li>
          </ul>
          <p style="margin-top:16px;font-family:\'Fraunces\',Georgia,serif;font-size:1.05rem;color:var(--cf-terracotta);margin-bottom:12px">Load time: 7s &rarr; 0.4s</p>
          <div class="tag-row">
            <span class="tag">Astro</span><span class="tag">GSAP</span><span class="tag">Sanity</span><span class="tag">Netlify</span>
          </div>
        </div>

        <!-- Case 02 -->
        <div class="card highlight">
          <div style="border-radius:16px;overflow:hidden;margin-bottom:20px;aspect-ratio:16/10;">
            <img src="assets/images/cozy-freelancer/cf-cozy-case-automation.webp" alt="Automation workflow project" width="1672" height="941" loading="lazy" decoding="async"
                 style="width:100%;height:100%;object-fit:cover;display:block;">
          </div>
          <p class="card-meta">The Staff &nbsp;·&nbsp; labwork</p>
          <h3>Lead routing + support agent, 3 weeks</h3>
          <p>A SaaS founder was answering 40–60 inbound messages a week manually. Each needed a personalised reply. The bottleneck was killing response time and his evenings.</p>
          <ul class="feature-list" style="margin-top:16px">
            <li>n8n: inbound &rarr; classify &rarr; route</li>
            <li>Merlin agent for tier-1 support</li>
            <li>Weekly digest to founder\'s inbox</li>
          </ul>
          <p style="margin-top:16px;font-family:\'Fraunces\',Georgia,serif;font-size:1.05rem;color:var(--cf-terracotta);margin-bottom:12px">Manual replies: 60/week &rarr; 4/week</p>
          <div class="tag-row">
            <span class="tag">n8n</span><span class="tag">Claude API</span><span class="tag">Make</span><span class="tag">Cal.com</span>
          </div>
        </div>

        <!-- Case 03 -->
        <div class="card">
          <div style="border-radius:16px;overflow:hidden;margin-bottom:20px;aspect-ratio:16/10;">
            <img src="assets/images/cozy-freelancer/cf-cozy-case-roundtable.webp" alt="Full workshop project" width="1672" height="941" loading="lazy" decoding="async"
                 style="width:100%;height:100%;object-fit:cover;display:block;">
          </div>
          <p class="card-meta">The Round Table &nbsp;·&nbsp; labwork</p>
          <h3>Site + staff rebuild, 28 days</h3>
          <p>A one-person consultancy running on a 5-year-old Squarespace site, handling sales calls manually. They needed the front-end and the engine behind it, built to work together.</p>
          <ul class="feature-list" style="margin-top:16px">
            <li>New site: Next.js, conversion-focused</li>
            <li>Intake: form &rarr; CRM &rarr; calendar &rarr; email</li>
            <li>Merlin handling discovery call pre-qualification</li>
          </ul>
          <p style="margin-top:16px;font-family:\'Fraunces\',Georgia,serif;font-size:1.05rem;color:var(--cf-terracotta);margin-bottom:12px">Sales cycle: 2 weeks &rarr; 3 days</p>
          <div class="tag-row">
            <span class="tag">Next.js</span><span class="tag">n8n</span><span class="tag">Claude API</span><span class="tag">Cal.com</span>
          </div>
        </div>

      </div>

      <div style="margin-top:48px;text-align:center;padding:28px 32px;border-radius:20px;background:rgba(255,255,255,0.5);border:1px solid var(--cf-line)">
        <p style="color:var(--cf-muted);font-size:0.9rem;line-height:1.7;margin:0">
          These are labworks — honest demonstrations of process and capability, not client case studies.
          Real engagements will replace them as they complete.
        </p>
        <a href="contact.html" class="button ghost" style="margin-top:16px;display:inline-block">Start a project</a>
      </div>
    </div>
  </section>

</main>'''

agencies_content = '''<main class="page-shell" style="padding-top:88px">

  <!-- Hero -->
  <section style="padding:96px 0 56px;position:relative;">
    <div aria-hidden="true" style="position:absolute;inset:0;background:url('assets/images/cozy-freelancer/cf-cozy-hero-agencies.webp') center/cover no-repeat;opacity:0.11;mix-blend-mode:multiply;pointer-events:none;"></div>
    <div class="container" style="position:relative;z-index:1;">
      <div class="hero-copy">
        <p class="hero-eyebrow">White-label · NDA by default</p>
        <h1 class="hero-title">Overflow capacity for agencies who landed <em class="accent">more than they staffed.</em></h1>
        <p class="hero-lead">I work directly with your project manager under your brand. Clean code, on-time delivery, no direct client contact unless you want it. You take the credit.</p>
        <div class="button-row">
          <a href="contact.html?service=agency" class="button primary">Let\'s talk overflow</a>
          <a href="work-with-me.html" class="button ghost">See the rate card</a>
        </div>
      </div>
    </div>
  </section>

  <!-- How it works -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div class="section-header">
        <p class="section-kicker">The arrangement</p>
        <h2 class="section-title">How I work with agencies.</h2>
      </div>
      <div class="grid-3">
        <div class="card">
          <p class="card-meta"><span class="material-symbols-outlined" style="font-size:1rem;vertical-align:-2px;color:var(--cf-sage)">shield</span> NDA by default</p>
          <h3>Your brand. My work.</h3>
          <p>I sign an NDA before seeing any client details. All deliverables are handed to you — no watermarks, no signatures, no portfolio requests unless you approve.</p>
        </div>
        <div class="card highlight">
          <p class="card-meta"><span class="material-symbols-outlined" style="font-size:1rem;vertical-align:-2px;color:var(--cf-terracotta)">speed</span> Overflow capacity</p>
          <h3>Plug in when you need it.</h3>
          <p>I\'m available for sprint-based overflow. You brief me via Slack or Notion, I deliver on the timeline we agree, and we close the loop cleanly. No retainer required.</p>
        </div>
        <div class="card">
          <p class="card-meta"><span class="material-symbols-outlined" style="font-size:1rem;vertical-align:-2px;color:var(--cf-cobalt)">build</span> What I can deliver</p>
          <h3>Web + automation.</h3>
          <p>Astro, Next.js, GSAP animation, n8n workflows, Claude-based agents. If your agency lands a project needing any of these, I can execute it under your umbrella.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Rate card -->
  <section class="section">
    <div class="container">
      <div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:start;">
        <div>
          <p class="section-kicker">Rate card</p>
          <h2 class="section-title">Transparent agency pricing.</h2>
          <p style="color:var(--cf-muted);font-size:1.02rem;line-height:1.75;margin:24px 0 0">Agency rates are lower than direct-client rates because the relationship is simpler — no discovery, no async client questions, no scope ambiguity. You handle the client layer; I handle execution.</p>
          <a href="contact.html?service=agency" class="button primary" style="margin-top:28px;display:inline-block">Start the conversation</a>
        </div>
        <div style="display:grid;gap:16px;margin-top:4px">
          <div class="stack-card">
            <strong>Sprint rate &nbsp;&mdash;&nbsp; €1,500 / sprint</strong>
            <p>One week of focused delivery. Defined scope agreed before start. Ideal for single features, landing pages, or automation builds.</p>
          </div>
          <div class="stack-card">
            <strong>Hourly &nbsp;&mdash;&nbsp; €90 / hour</strong>
            <p>For scope that\'s genuinely hard to bound upfront. Tracked and invoiced weekly with a summary of work done.</p>
          </div>
          <div class="stack-card">
            <strong>Slack Connect onboarding included</strong>
            <p>I join your agency Slack as a guest. You can brief me, share assets, and review work without leaving your own tools.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>'''

about_content = '''<main class="page-shell" style="padding-top:88px">

  <!-- Hero -->
  <section style="padding:96px 0 56px;position:relative;">
    <div aria-hidden="true" style="position:absolute;inset:0;background:url('assets/images/cozy-freelancer/cf-cozy-hero-about.webp') center/cover no-repeat;opacity:0.11;mix-blend-mode:multiply;pointer-events:none;"></div>
    <div class="container" style="position:relative;z-index:1;">
      <div class="hero-copy">
        <p class="hero-eyebrow">Alexandru Buzi · Camelot Flows</p>
        <h1 class="hero-title">An Avalon for makers, run from Moldova while my son <em class="accent">Arthur</em> naps.</h1>
        <p class="hero-lead">I build the site, then I build the staff that runs it. One workshop, no middlemen, fixed prices.</p>
        <div class="button-row">
          <a href="work-with-me.html" class="button primary">See the services</a>
          <a href="contact.html" class="button ghost">Start a conversation</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Why Camelot? -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:start;">
        <div>
          <p class="section-kicker">The Name</p>
          <h2 class="section-title">Why <em class="accent">Camelot?</em></h2>
        </div>
        <div>
          <p style="color:var(--muted);font-size:1.02rem;line-height:1.75;margin:0">Avalon, in Arthurian legend, is where Excalibur was forged and kept between uses. Not a battlefield — a forge. A vault. The place where the work that makes the work possible gets done quietly, out of sight.</p>
          <p style="color:var(--muted);font-size:1.02rem;line-height:1.75;margin:18px 0 0">That\'s what this is: a one-person workshop where strategy, design, and automation are made to order, then dispatched. I named it after my son Arthur, because the day he arrived was the day I decided to build the thing I actually wanted to build.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- The Workshop -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <p class="section-kicker">The Workshop</p>
        <h2 class="section-title">What I build with.</h2>
        <p class="section-copy">Two co-equal services. The site is the storefront. The staff is the engine behind it. I do both, so neither gets compromised to fit the other.</p>
      </div>
      <div class="grid-3">
        <div class="card">
          <p class="card-meta">Web &amp; Interaction</p>
          <h3>Astro, Next.js, GSAP</h3>
          <p>Performance-first sites with premium animation. Designed to convert, built to load fast.</p>
          <div class="tag-row">
            <span class="tag">Astro</span><span class="tag">Next.js</span><span class="tag">GSAP</span><span class="tag">Tailwind</span>
          </div>
        </div>
        <div class="card highlight">
          <p class="card-meta">Automation &amp; AI</p>
          <h3>n8n, Make, Python, Claude API</h3>
          <p>Workflows that run while you sleep. Lead routing, support agents, data pipelines — built to hold under real load.</p>
          <div class="tag-row">
            <span class="tag">n8n</span><span class="tag">Make</span><span class="tag">Python</span><span class="tag">Claude API</span>
          </div>
        </div>
        <div class="card">
          <p class="card-meta">Infrastructure</p>
          <h3>Cursor, Netlify, Supabase, Git</h3>
          <p>Every project ships with clean handoff documentation. You own the codebase. I move fast without cutting corners.</p>
          <div class="tag-row">
            <span class="tag">Cursor</span><span class="tag">Netlify</span><span class="tag">Supabase</span><span class="tag">Git</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Arthur -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div style="display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,0.9fr);gap:64px;align-items:start;">
        <div>
          <p class="section-kicker">The Calendar</p>
          <h2 class="section-title">Arthur\'s nap schedule is my <em class="accent">deep-work calendar.</em></h2>
          <p style="color:var(--muted);font-size:1.02rem;line-height:1.75;margin:24px 0 0">Arthur is two. His nap schedule is non-negotiable, which means mine is too. Ninety minutes, twice a day — that\'s when the serious work happens. The architecture decisions, the animation code, the n8n flows that need actual thinking.</p>
          <p style="color:var(--muted);font-size:1.02rem;line-height:1.75;margin:16px 0 0">The rest of the day is communication, review, and the kind of light work that survives interruption. It sounds like a constraint. It\'s actually a filter: I only take work that fits, which means the work I do take gets done properly.</p>
        </div>
        <div class="stack-card" style="margin-top:4px">
          <strong>A typical day &mdash; Chișinău time</strong>
          <div style="display:grid;gap:20px;margin-top:24px;padding-left:20px;border-left:2px solid rgba(123,145,113,0.3)">
            <div>
              <p style="font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--sage);margin:0">7:00 &ndash; 9:00</p>
              <p style="color:var(--muted);margin:4px 0 0;font-size:0.95rem">Client replies, async reviews, quick fixes.</p>
            </div>
            <div>
              <p style="font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--sage);margin:0">9:30 &ndash; 11:00</p>
              <p style="color:var(--muted);margin:4px 0 0;font-size:0.95rem">First deep block. Architecture, heavy code, system design.</p>
            </div>
            <div>
              <p style="font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--sage);margin:0">14:00 &ndash; 16:00</p>
              <p style="color:var(--muted);margin:4px 0 0;font-size:0.95rem">Second deep block. Design, automation builds, testing.</p>
            </div>
            <div>
              <p style="font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--terracotta);margin:0">20:00 &ndash; 22:00</p>
              <p style="color:var(--muted);margin:4px 0 0;font-size:0.95rem">Side projects. The game. Writing. Experiments nobody asked for.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Game dev -->
  <section class="section">
    <div class="container">
      <div style="display:grid;grid-template-columns:minmax(0,0.95fr) minmax(0,1.05fr);gap:64px;align-items:center;">
        <div>
          <p class="section-kicker">Side Project</p>
          <h2 class="section-title">I\'m also building a <em class="accent">game.</em></h2>
          <p style="color:var(--muted);font-size:1.02rem;line-height:1.75;margin:24px 0 0">Not because it pays. Because it\'s the most effective way I\'ve found to stay sharp on animation, interaction design, and systems thinking. Game dev forces constraints that client work doesn\'t — and the techniques leak back into everything else.</p>
          <p style="color:var(--muted);font-size:1.02rem;line-height:1.75;margin:16px 0 0">The parallax on this site started as a game camera experiment. Merlin\'s dialogue routing started as an NPC state machine. The side project feeds the main work without the main work subsidising it.</p>
        </div>
        <div class="card highlight" style="padding:32px">
          <p class="card-meta">What this means for your project</p>
          <ul class="feature-list" style="margin-top:20px">
            <li>Animation skills maintained at game-dev level, applied to your site</li>
            <li>Systems thinking from game architecture carried into automation design</li>
            <li>A developer who ships creative side work stays technically curious — and that shows in the client work</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Moldova -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div class="section-header centered" style="text-align:center">
        <p class="section-kicker">Location</p>
        <h2 class="section-title">Moldova is an <em class="accent">asset.</em></h2>
        <p class="section-copy" style="max-width:600px;margin:16px auto 0">Lower cost of living means lower overhead, which means I can take fewer clients and do better work for each one. I don\'t race to fill a calendar. I pick work carefully and treat it accordingly. The timezone (EET, UTC+2) overlaps fully with Western Europe and reaches US East Coast mornings with an early start.</p>
      </div>
      <div class="proof-strip" style="margin-top:40px;grid-template-columns:repeat(3,minmax(0,1fr))">
        <div class="proof-item">
          <strong>24-hour replies</strong>
          <span>Every client message answered within one business day, without exception.</span>
        </div>
        <div class="proof-item">
          <strong>UTC+2 &nbsp;·&nbsp; EET</strong>
          <span>Full overlap with Western Europe. US East Coast reached by 8&nbsp;am local time.</span>
        </div>
        <div class="proof-item">
          <strong>Worldwide delivery</strong>
          <span>All handoffs in English. Contracts, invoices, and communication fully in writing.</span>
        </div>
      </div>
    </div>
  </section>

  <!-- The Promise -->
  <section class="section">
    <div class="container">
      <div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:start;">
        <div>
          <p class="section-kicker">How I work</p>
          <h2 class="section-title">The <em class="accent">promise.</em></h2>
          <p style="color:var(--muted);font-size:1.02rem;line-height:1.75;margin:24px 0 0">Every engagement is scoped before it starts. Fixed scope, fixed price, fixed timeline — no retainer creep, no invoice surprises. If scope changes, we agree on it in writing before I touch it.</p>
          <div class="button-row" style="margin-top:32px">
            <a href="work-with-me.html" class="button primary">See available services</a>
          </div>
        </div>
        <div style="display:grid;gap:16px;margin-top:4px">
          <div class="stack-card">
            <strong>24-hour reply, always</strong>
            <p>Every message answered within one business day. If something is blocking you, I unblock it that day.</p>
          </div>
          <div class="stack-card">
            <strong>Fixed scope, fixed price</strong>
            <p>You know the cost before we start. Scope changes are discussed, agreed, and repriced openly.</p>
          </div>
          <div class="stack-card">
            <strong>Clean handoff included</strong>
            <p>Every project ends with documentation. You own the codebase and can have any developer continue the work.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>'''

work_with_me_content = '''<main class="page-shell" style="padding-top:88px">

  <!-- Hero -->
  <section style="padding:96px 0 56px;position:relative;">
    <div aria-hidden="true" style="position:absolute;inset:0;background:url('assets/images/cozy-freelancer/cf-cozy-hero-work.webp') center/cover no-repeat;opacity:0.11;mix-blend-mode:multiply;pointer-events:none;"></div>
    <div class="container" style="position:relative;z-index:1;">
      <div class="hero-copy">
        <p class="hero-eyebrow">Fixed scope · fixed price · 24h reply</p>
        <h1 class="hero-title">Two services. One workshop. <em class="accent">Clear prices.</em></h1>
        <p class="hero-lead">I build the site, then I build the staff that runs it. Every engagement is scoped before it starts — no retainer creep, no invoice surprises.</p>
      </div>
    </div>
  </section>

  <!-- Tiers -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div class="tier-grid">

        <!-- Tier 1: The Site -->
        <div class="tier-card">
          <p class="tier-label">Web &amp; Interaction</p>
          <h3>The Site</h3>
          <p>A performance-first site with premium animation. Designed to convert, built to load fast. One AI form-handler included so leads go somewhere useful from day one.</p>
          <div class="tag-row" style="margin-top:20px">
            <span class="tag">Astro</span><span class="tag">GSAP</span><span class="tag">Tailwind</span><span class="tag">Netlify</span>
          </div>
          <ul class="feature-list" style="margin-top:24px">
            <li>Up to 8 pages, mobile-first responsive</li>
            <li>Scroll animations and micro-interactions</li>
            <li>Contact form wired to your inbox</li>
            <li>1 AI form-handler (lead qualification or routing)</li>
            <li>Performance-optimised images and fonts</li>
            <li>Clean handoff with documentation</li>
          </ul>
          <div style="margin-top:28px;padding-top:24px;border-top:1px solid var(--line)">
            <p style="font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--muted);margin:0">Starting from</p>
            <p style="font-family:\'Fraunces\',Georgia,serif;font-size:2.8rem;font-weight:700;letter-spacing:-0.04em;color:var(--text);margin:4px 0 0">€1,800</p>
            <p style="font-size:0.85rem;color:var(--muted);margin:4px 0 0">14-day delivery · fixed scope</p>
          </div>
          <a href="contact.html?service=site" class="button secondary" style="margin-top:20px;display:inline-block">Talk about your site</a>
        </div>

        <!-- Tier 2: The Staff (highlight) -->
        <div class="tier-card highlight">
          <p class="tier-label">Automation &amp; AI</p>
          <h3>The Staff</h3>
          <p>A Merlin AI agent and n8n workflow system that handles lead routing, tier-1 support, and data sync — running 24/7 without growing your headcount.</p>
          <div class="tag-row" style="margin-top:20px">
            <span class="tag">n8n</span><span class="tag">Merlin agent</span><span class="tag">Claude API</span><span class="tag">Make</span>
          </div>
          <ul class="feature-list" style="margin-top:24px">
            <li>Custom Merlin AI agent trained on your context</li>
            <li>Lead qualification and routing workflows</li>
            <li>Tier-1 support handling (FAQs, booking, status)</li>
            <li>CRM and calendar synchronisation</li>
            <li>Weekly digest report to your inbox</li>
            <li>30-day onboarding support included</li>
          </ul>
          <div style="margin-top:28px;padding-top:24px;border-top:1px solid rgba(123,145,113,0.2)">
            <p style="font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--muted);margin:0">Setup</p>
            <p style="font-family:\'Fraunces\',Georgia,serif;font-size:2.8rem;font-weight:700;letter-spacing:-0.04em;color:var(--text);margin:4px 0 0">€2,400</p>
            <p style="font-size:0.85rem;color:var(--muted);margin:4px 0 0">then €600/mo · cancel anytime</p>
          </div>
          <a href="contact.html?service=staff" class="button primary" style="margin-top:20px;display:inline-block">Talk about your staff</a>
        </div>

        <!-- Tier 3: The Round Table -->
        <div class="tier-card">
          <p class="tier-label">Full Workshop</p>
          <h3>The Round Table</h3>
          <p>Both services, built together so they talk to each other from the start. The site feeds the staff, the staff reports back to the site. 30 days, one engagement.</p>
          <div class="tag-row" style="margin-top:20px">
            <span class="tag">Everything in both tiers</span>
          </div>
          <ul class="feature-list" style="margin-top:24px">
            <li>Full site (up to 10 pages)</li>
            <li>Full Merlin agent + n8n stack</li>
            <li>Site and automation built to integrate natively</li>
            <li>Priority access during build</li>
            <li>60-day post-launch support window</li>
            <li>Clean handoff for both systems</li>
          </ul>
          <div style="margin-top:28px;padding-top:24px;border-top:1px solid var(--line)">
            <p style="font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--muted);margin:0">Fixed price</p>
            <p style="font-family:\'Fraunces\',Georgia,serif;font-size:2.8rem;font-weight:700;letter-spacing:-0.04em;color:var(--text);margin:4px 0 0">€4,800</p>
            <p style="font-size:0.85rem;color:var(--muted);margin:4px 0 0">30-day delivery · everything included</p>
          </div>
          <a href="contact.html?service=round-table" class="button secondary" style="margin-top:20px;display:inline-block">Book the Round Table</a>
        </div>

      </div>
    </div>
  </section>

  <!-- What\'s not included -->
  <section class="section">
    <div class="container">
      <div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);gap:56px;align-items:start;">
        <div>
          <p class="section-kicker">Honesty section</p>
          <h2 class="section-title">What\'s <em class="accent">not</em> included.</h2>
          <p style="color:var(--muted);font-size:1.02rem;line-height:1.75;margin:24px 0 0">I\'d rather tell you this upfront than negotiate it out of a scope document later. If your project needs any of these, I\'ll say so before we agree on anything — and we can scope it separately.</p>
        </div>
        <div style="display:grid;gap:16px;margin-top:4px">
          <div class="stack-card">
            <strong>Copywriting</strong>
            <p>I can refine your copy, but I don\'t write from scratch. You bring the words; I shape them into something that works on screen.</p>
          </div>
          <div class="stack-card">
            <strong>Brand identity</strong>
            <p>Logo design, typeface selection, and visual identity work are outside my scope. If you have a brand guide, I follow it exactly. If you don\'t, you\'ll need one before we start.</p>
          </div>
          <div class="stack-card">
            <strong>Paid ads or SEO campaigns</strong>
            <p>I build the technical SEO foundation into every site (meta, schema, speed). Running campaigns and managing ad spend is a different discipline — I don\'t do it.</p>
          </div>
          <div class="stack-card">
            <strong>Ongoing retainer (unless agreed)</strong>
            <p>The Staff tier includes a monthly fee for the running infrastructure. Everything else is a fixed engagement. I\'m not the right fit if you need someone available on-demand every week.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Good fit / Bad fit -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div class="section-header centered" style="text-align:center">
        <p class="section-kicker">Is this right for you?</p>
        <h2 class="section-title">Good fit. Bad fit.</h2>
        <p class="section-copy" style="max-width:560px;margin:12px auto 0">I take a small number of projects at a time. These criteria help both of us decide quickly.</p>
      </div>
      <div class="fit-grid" style="margin-top:40px">
        <div class="card fit-card good">
          <p class="card-meta" style="color:var(--sage)">Good fit</p>
          <ul class="feature-list" style="margin-top:16px">
            <li>You have a clear goal for the site or the automation</li>
            <li>You want to own the codebase when we\'re done</li>
            <li>You\'re comfortable with fixed scope and fixed price</li>
            <li>You have (or can write) the copy for your own business</li>
            <li>You communicate async and respond within a day</li>
            <li>You want senior-quality work at a solo workshop price</li>
          </ul>
        </div>
        <div class="card fit-card bad">
          <p class="card-meta" style="color:var(--terracotta)">Bad fit</p>
          <ul class="feature-list" style="margin-top:16px">
            <li>You need a team of five to manage the project</li>
            <li>Scope is still undefined and likely to shift weekly</li>
            <li>You\'re looking for the cheapest option available</li>
            <li>You need something live in under a week</li>
            <li>You want someone to run your ads or write your brand strategy</li>
            <li>You\'d rather pay by the hour than agree a scope upfront</li>
          </ul>
        </div>
        <div class="card">
          <p class="card-meta">Still unsure?</p>
          <h3 style="margin-top:16px">Send me a message.</h3>
          <p>Describe what you\'re trying to build. I\'ll tell you honestly whether it fits, and if it doesn\'t, I\'ll point you somewhere that might.</p>
          <a href="contact.html" class="button ghost" style="margin-top:24px;display:inline-block">Get in touch</a>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section">
    <div class="container">
      <div style="text-align:center;max-width:560px;margin:0 auto">
        <p class="section-kicker">Ready to start?</p>
        <h2 class="section-title">Tell me about <em class="accent">the work.</em></h2>
        <p style="color:var(--muted);font-size:1.02rem;line-height:1.75;margin:20px 0 32px">I read every message and reply within 24 hours. If the project is a good fit, we agree scope in writing before anything else happens.</p>
        <div class="button-row" style="justify-content:center">
          <a href="contact.html" class="button primary">Start a conversation</a>
          <a href="about.html" class="button ghost">Learn about the workshop</a>
        </div>
      </div>
    </div>
  </section>

</main>'''

contact_content = '''<main class="page-shell" style="padding-top:88px">

  <!-- Hero -->
  <section style="padding:96px 0 56px;position:relative;">
    <div aria-hidden="true" style="position:absolute;inset:0;background:url('assets/images/cozy-freelancer/cf-cozy-hero-contact.webp') center/cover no-repeat;opacity:0.11;mix-blend-mode:multiply;pointer-events:none;"></div>
    <div class="container" style="position:relative;z-index:1;">
      <div class="hero-copy">
        <p class="hero-eyebrow">Response within 24 hours · EET (UTC+2)</p>
        <h1 class="hero-title">Tell me about <em class="accent">the work.</em></h1>
        <p class="hero-lead">Describe what you\'re trying to build. I\'ll read it, think about it, and reply with either a clear next step or an honest "this isn\'t the right fit."</p>
      </div>
    </div>
  </section>

  <!-- Form + Sidebar -->
  <section class="section tight">
    <div class="container">
      <div class="form-layout">

        <!-- Form -->
        <div class="form-shell">
          <form name="contact" action="YOUR_N8N_WEBHOOK_URL_HERE" method="POST" data-progress-form>
            <div class="progress-bar"><div class="progress-fill" data-progress-fill style="width:0%"></div></div>

            <div class="form-grid">
              <div class="field">
                <label class="field-label" for="c-name">Your name</label>
                <input id="c-name" type="text" name="name" placeholder="Alex" required>
              </div>
              <div class="field">
                <label class="field-label" for="c-email">Your email</label>
                <input id="c-email" type="email" name="email" placeholder="alex@example.com" required>
              </div>
              <div class="field">
                <label class="field-label" for="c-service">What are you looking for?</label>
                <select id="c-service" name="service" required>
                  <option value="">Choose one…</option>
                  <option value="site">A new website (The Site)</option>
                  <option value="staff">AI automation + agents (The Staff)</option>
                  <option value="round-table">Both together (The Round Table)</option>
                  <option value="agency">Agency overflow / white-label work</option>
                  <option value="other">Something else — I\'ll explain below</option>
                </select>
              </div>
              <div class="field">
                <label class="field-label" for="c-budget">Rough budget</label>
                <select id="c-budget" name="budget">
                  <option value="">I\'d rather discuss it</option>
                  <option value="under-2k">Under €2,000</option>
                  <option value="2k-5k">€2,000 – €5,000</option>
                  <option value="5k-10k">€5,000 – €10,000</option>
                  <option value="10k+">€10,000+</option>
                </select>
              </div>
              <div class="field full">
                <label class="field-label" for="c-goal">What are you trying to accomplish?</label>
                <textarea id="c-goal" name="project_goal" rows="5"
                  placeholder="Describe the problem or goal in plain language. No need to be formal — a few sentences is fine." required></textarea>
              </div>
            </div>

            <div style="margin-top:24px;display:flex;align-items:center;gap:16px;flex-wrap:wrap">
              <button type="submit" class="button primary">Send message</button>
              <p class="form-note" data-form-status style="margin:0">I read every message and reply within 24 hours.</p>
            </div>
          </form>
        </div>

        <!-- Sidebar -->
        <div class="contact-sidebar">
          <h3>Before you send.</h3>
          <div style="display:grid;gap:20px;margin-top:24px">
            <div class="stack-card">
              <strong>No agency, no team</strong>
              <p>You\'ll talk to me directly — Alexandru, the person who will build your project. No account managers, no handoffs.</p>
            </div>
            <div class="stack-card">
              <strong>24-hour replies</strong>
              <p>I respond to every message within one business day. I\'m in EET (UTC+2), which overlaps fully with Western Europe and reaches US East Coast mornings.</p>
            </div>
            <div class="stack-card">
              <strong>Fixed scope, fixed price</strong>
              <p>I\'ll confirm whether the project fits one of my productized tiers or needs a custom scope. Either way, you\'ll have a clear price before any work starts.</p>
            </div>
          </div>

          <div style="margin-top:28px;padding-top:24px;border-top:1px solid var(--cf-line)">
            <p style="font-size:0.88rem;color:var(--cf-muted);line-height:1.65;margin:0">Prefer to book a call directly?</p>
            <a href="https://cal.com/camelotflows/intro" target="_blank" rel="noopener"
               class="button ghost" style="margin-top:12px;display:inline-block">Book a 30-min intro call &rarr;</a>
            <p style="font-size:0.78rem;color:var(--cf-muted);margin:10px 0 0;line-height:1.5">
              Free, no obligation. I\'ll ask about your project and tell you whether I can help.
            </p>
          </div>
        </div>

      </div>
    </div>
  </section>

</main>'''

legal_content = '''<main class="page-shell" style="padding-top:88px">
  <section style="padding:80px 0 48px">
    <div class="container" style="max-width:760px">
      <p class="section-kicker">Legal</p>
      <h1 class="section-title" style="margin-bottom:40px">Terms &amp; Conditions</h1>
      <div class="legal-doc">
        <p><strong>Last updated: April 2026</strong></p>
        <p>This website is operated by Alexandru Buzi, trading as Camelot Flows, based in Chișinău, Republic of Moldova.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Services</h2>
        <p>Camelot Flows provides web development, business automation, and AI integration services. All engagements are agreed in writing with a defined scope, fixed price, and clear deliverables before any work begins. No work commences without a signed scope document or written confirmation of terms.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Payment</h2>
        <p>Payment terms are specified in the project agreement for each engagement. Standard terms: 50% deposit before work begins, 50% on delivery. Deposits are non-refundable if the client cancels after work has commenced. Refunds for incomplete work are assessed on a case-by-case basis proportional to work delivered.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Intellectual Property</h2>
        <p>On full payment, the client receives ownership of all custom code and design assets created for their project. Third-party libraries, frameworks, and tools retain their respective open-source or commercial licences. Alexandru Buzi retains the right to display completed work in a portfolio unless the client requests otherwise in writing before the project begins.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Limitation of Liability</h2>
        <p>Camelot Flows is not liable for indirect, incidental, or consequential damages arising from the use of delivered work. Total liability in any dispute is limited to the amount paid for the specific engagement in question.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Governing Law</h2>
        <p>These terms are governed by the laws of the Republic of Moldova. Disputes will be resolved by mutual agreement wherever possible. If formal proceedings are necessary, they will be conducted in Chișinău, Moldova.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Contact</h2>
        <p>For any legal enquiries: <a href="mailto:hello@camelotflows.com" style="color:var(--cf-terracotta)">hello@camelotflows.com</a></p>
      </div>
    </div>
  </section>
</main>'''

privacy_content = '''<main class="page-shell" style="padding-top:88px">
  <section style="padding:80px 0 48px">
    <div class="container" style="max-width:760px">
      <p class="section-kicker">Privacy</p>
      <h1 class="section-title" style="margin-bottom:40px">Privacy Policy</h1>
      <div class="legal-doc">
        <p><strong>Last updated: April 2026</strong></p>
        <p>This policy describes how Camelot Flows (operated by Alexandru Buzi, Chișinău, Republic of Moldova) handles personal data collected through this website.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">What I collect</h2>
        <p>When you submit the contact form, I collect your name, email address, and the details you include in your message. I do not collect data passively — there are no tracking pixels, advertising cookies, or cross-site trackers on this website.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">How I use it</h2>
        <p>Contact form submissions are used solely to respond to your enquiry and, if we enter an engagement, to manage that project relationship. I do not sell, share, or rent your data to third parties.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Storage</h2>
        <p>Form submissions are stored by Netlify Forms on Netlify\'s servers (US-based). Email correspondence is stored in my personal email client. I retain project correspondence for up to three years after project completion for record-keeping purposes.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Analytics</h2>
        <p>This website does not currently use any analytics service. If analytics are added in the future, this policy will be updated before any data collection begins.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Your rights</h2>
        <p>You have the right to request a copy of any personal data I hold about you, to request its deletion, and to object to its processing. To exercise any of these rights, email <a href="mailto:hello@camelotflows.com" style="color:var(--cf-terracotta)">hello@camelotflows.com</a>.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Cookies</h2>
        <p>This website does not set cookies. The only third-party script loaded is Tailwind CSS via CDN and Google Fonts, which may set their own cookies under their respective privacy policies.</p>
        <h2 style="font-family:\'Fraunces\',Georgia,serif;font-size:1.35rem;margin:8px 0 0">Contact</h2>
        <p>Privacy questions: <a href="mailto:hello@camelotflows.com" style="color:var(--cf-terracotta)">hello@camelotflows.com</a></p>
      </div>
    </div>
  </section>
</main>'''

build_page('arsenal.html',      'The Arsenal',
    arsenal_content,
    description="The full capabilities of Camelot Flows: award-quality websites, autonomous AI workforces, and automation infrastructure — productized and fixed-price.",
    og_image="assets/images/cozy-freelancer/cf-cozy-og-arsenal.webp")

build_page('merlin.html',       'The Merlin System',
    merlin_content,
    description="Deploy Merlin — a custom AI agent that handles lead qualification, tier-1 support, and CRM sync 24/7 without growing your headcount.")

build_page('case-studies.html', 'Case Studies',
    case_studies_content,
    description="Real projects, real results. Detailed breakdowns of web and automation engagements delivered by Camelot Flows.")

build_page('for-agencies.html', 'For Agencies',
    agencies_content,
    description="Overflow capacity for agencies who landed more than they staffed. White-label web dev and automation from a solo workshop. NDA by default.")

build_page('about.html',        'About',
    about_content,
    description="Camelot Flows is a one-person workshop run by Alexandru Buzi in Chișinău, Moldova. Named after his son Arthur. Fixed prices, direct communication, senior-quality work.")

build_page('work-with-me.html', 'Work With Me',
    work_with_me_content,
    description="Three productized services: The Site (€1,800, 14 days), The Staff (€2,400 + €600/mo), The Round Table (€4,800, 30 days). Fixed scope, fixed price.")

build_page('contact.html',      'Contact',
    contact_content,
    description="Tell me about the work. I read every message and reply within 24 hours. No agency, no team — you'll talk to me directly.")

build_page('legal.html',        'Terms & Conditions',
    legal_content,
    description="Terms and conditions for Camelot Flows, operated by Alexandru Buzi in Chișinău, Republic of Moldova.")

build_page('privacy.html',      'Privacy Policy',
    privacy_content,
    description="Privacy policy for Camelot Flows. No tracking pixels, no ad cookies. Contact form data used only to respond to your enquiry.")
def write_redirect(filename, destination):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={destination}">
<title>Redirecting — Camelot Flows</title>
</head>
<body style="font-family:sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh;background:#F5F4F0;color:#6D6A64;">
<p>Redirecting to <a href="{destination}" style="color:#C4785C">{destination}</a>…</p>
</body>
</html>'''
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(html)
    print(f"Generated {filename} (redirect to {destination})")

write_redirect('service-creation.html', 'arsenal.html')
write_redirect('service-maintenance.html', 'arsenal.html')
write_redirect('service-automation.html', 'merlin.html')
write_redirect('service-marketing.html', 'for-agencies.html')

shutil.copy('code_v2.html', 'index.html')
print("Generated index.html")
