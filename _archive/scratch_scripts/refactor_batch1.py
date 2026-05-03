import codecs
import re

with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'r', 'utf-8') as f:
    code = f.read()

new_about_html = """save('about.html', 'About Alex Buzi', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 grid-bg opacity-30 -z-20"></div>

<!-- STITCH HERO -->
<section class="max-w-6xl mx-auto mb-24 relative fade-in-section">
    <div class="absolute top-1/2 left-0 -translate-y-1/2 w-[600px] h-[600px] bg-primary/10 blur-[150px] rounded-full -z-10 pointer-events-none fade-in-section"></div>
    <div class="grid grid-cols-1 md:grid-cols-12 gap-12 items-center">
        <div class="md:col-span-7 relative z-10">
            <span class="text-neon-cyan font-mono text-xs uppercase tracking-[0.3em] mb-4 block animate-glow">// ABOUT THE FOUNDER</span>
            <h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 leading-[0.9] text-transparent bg-clip-text bg-gradient-to-r from-neon-cyan to-indigo-500 pb-2 drop-shadow-[0_0_15px_rgba(0,242,255,0.4)]">
                I'm Alex Buzi.<br/>I build digital<br/>kingdoms.
            </h1>
            <p class="text-slate-400 text-lg leading-relaxed max-w-xl mb-8">
                Self-taught developer from Chișinău, Moldova. Father of Arthur — the reason this company is called Camelot. Full-time employee by day, builder of futures by night.
            </p>
            <div class="glass-panel p-4 inline-block rounded-lg border-l-2 border-neon-cyan/50 font-mono text-xs text-slate-300 space-y-2 relative overflow-hidden group">
                <div class="absolute inset-0 bg-neon-cyan/5 -translate-x-full group-hover:translate-x-0 transition-transform duration-500"></div>
                <p><span class="text-neon-cyan font-bold">&gt;</span> LOCATION: Chișinău, Moldova</p>
                <p><span class="text-emerald-400 font-bold">&gt;</span> STATUS: Forging Infrastructure</p>
                <p><span class="text-neon-purple font-bold">&gt;</span> STACK: Python / AI / GSAP / DevOps</p>
            </div>
        </div>
        <div class="md:col-span-5 flex justify-center relative">
            <div class="absolute -inset-4 bg-gradient-to-tr from-primary to-neon-cyan opacity-20 blur-2xl rounded-2xl -z-10 animate-pulse"></div>
            <div class="relative w-80 h-96 rounded-2xl border border-white/10 bg-black/40 backdrop-blur-sm overflow-hidden group flex flex-col items-center justify-center text-center shadow-[-20px_20px_60px_rgba(0,0,0,0.8)]">
                <div class="absolute inset-0 bg-gradient-to-b from-transparent to-black/80 z-10"></div>
                <!-- Assuming placeholder logic -->
                <span class="material-symbols-outlined text-6xl text-primary/30 mb-4 z-20 group-hover:text-primary transition-colors">person</span>
                <p class="font-mono text-xs text-white/50 uppercase tracking-widest z-20">PROJECT_LEAD: ALEX B.</p>
                <p class="text-[9px] text-neon-cyan/60 mt-2 font-mono z-20 uppercase">Insert visual data block</p>
            </div>
        </div>
    </div>
</section>

<!-- STITCH TIMELINE -->
<section class="max-w-4xl mx-auto mb-32 relative">
    <h2 class="font-display text-4xl font-black uppercase tracking-tighter mb-20 text-center text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-500 drop-shadow-[0_0_15px_rgba(251,191,36,0.3)] fade-in-section">The Origin Story</h2>
    <div class="relative">
        <div class="absolute left-[30px] md:left-1/2 top-0 bottom-0 w-px bg-gradient-to-b from-transparent via-primary/50 to-transparent"></div>
        <div class="space-y-16">
            
            <div class="timeline-node relative pl-20 md:pl-0 md:grid md:grid-cols-2 md:gap-12 group">
                <div class="md:text-right md:pr-12 fade-in-section">
                    <div class="inline-block px-3 py-1 bg-neon-cyan/10 border border-neon-cyan/30 rounded font-mono text-[10px] text-neon-cyan mb-2">2018–2019</div>
                    <h3 class="font-display text-2xl font-bold text-white mb-2 group-hover:text-neon-cyan transition-colors">The Spark</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">Started making WordPress sites as a hobby. First for friends, then for colleagues who needed a web presence. I was just curious.</p>
                </div><div class="hidden md:block"></div>
                <div class="absolute left-6 md:left-1/2 md:-translate-x-1/2 top-1 w-4 h-4 rounded-full bg-neon-cyan border-2 border-obsidian shadow-[0_0_15px_rgba(0,242,255,0.8)] group-hover:scale-150 transition-transform"></div>
            </div>

            <div class="timeline-node relative pl-20 md:pl-0 md:grid md:grid-cols-2 md:gap-12 group">
                <div class="hidden md:block"></div>
                <div class="md:pl-12 fade-in-section">
                    <div class="inline-block px-3 py-1 bg-primary/10 border border-primary/30 rounded font-mono text-[10px] text-primary mb-2">2019–2020</div>
                    <h3 class="font-display text-2xl font-bold text-white mb-2 group-hover:text-primary transition-colors">The Grind</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">Law firms, industrial companies, e-commerce stores. Learned the best templates, wrote my first custom PHP. All while working full-time.</p>
                </div>
                <div class="absolute left-6 md:left-1/2 md:-translate-x-1/2 top-1 w-4 h-4 rounded-full bg-primary border-2 border-obsidian shadow-[0_0_15px_rgba(99,102,241,0.8)] group-hover:scale-150 transition-transform"></div>
            </div>

            <div class="timeline-node relative pl-20 md:pl-0 md:grid md:grid-cols-2 md:gap-12 group">
                <div class="md:text-right md:pr-12 fade-in-section">
                    <div class="inline-block px-3 py-1 bg-neon-purple/10 border border-neon-purple/30 rounded font-mono text-[10px] text-neon-purple mb-2">2020–2021</div>
                    <h3 class="font-display text-2xl font-bold text-white mb-2 group-hover:text-neon-purple transition-colors">The Pivot</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">Chose Python. Fascinated by what scripts could accomplish at 3am while I slept. Learned SEO and Google Ads the hard way.</p>
                </div><div class="hidden md:block"></div>
                <div class="absolute left-6 md:left-1/2 md:-translate-x-1/2 top-1 w-4 h-4 rounded-full bg-neon-purple border-2 border-obsidian shadow-[0_0_15px_rgba(191,0,255,0.8)] group-hover:scale-150 transition-transform"></div>
            </div>

            <div class="timeline-node relative pl-20 md:pl-0 md:grid md:grid-cols-2 md:gap-12 group">
                <div class="hidden md:block"></div>
                <div class="md:pl-12 fade-in-section">
                    <div class="inline-block px-3 py-1 bg-[#ff0055]/10 border border-[#ff0055]/30 rounded font-mono text-[10px] text-[#ff0055] mb-2">2022</div>
                    <h3 class="font-display text-2xl font-bold text-white mb-2 group-hover:text-[#ff0055] transition-colors">The AI Dawn</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">When Moldova was just hearing about GPT-3.5, I was already deep. Building second brains, image generator pipelines, training LoRAs.</p>
                </div>
                <div class="absolute left-6 md:left-1/2 md:-translate-x-1/2 top-1 w-4 h-4 rounded-full bg-[#ff0055] border-2 border-obsidian shadow-[0_0_15px_rgba(255,0,85,0.8)] group-hover:scale-150 transition-transform"></div>
            </div>

            <div class="timeline-node relative pl-20 md:pl-0 md:grid md:grid-cols-2 md:gap-12 group">
                <div class="md:text-right md:pr-12 fade-in-section">
                    <div class="inline-block px-3 py-1 bg-emerald-400/10 border border-emerald-400/30 rounded font-mono text-[10px] text-emerald-400 mb-2">2023–2024</div>
                    <h3 class="font-display text-2xl font-bold text-white mb-2 group-hover:text-emerald-400 transition-colors">Architecture</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">AI agents on WhatsApp/Telegram. VPS infrastructure. Full-stack automation. Google's algorithms changed—I adapted while others complained.</p>
                </div><div class="hidden md:block"></div>
                <div class="absolute left-6 md:left-1/2 md:-translate-x-1/2 top-1 w-4 h-4 rounded-full bg-emerald-400 border-2 border-obsidian shadow-[0_0_15px_rgba(52,211,153,0.8)] group-hover:scale-150 transition-transform"></div>
            </div>

            <div class="timeline-node relative pl-20 md:pl-0 md:grid md:grid-cols-2 md:gap-12 group">
                <div class="hidden md:block"></div>
                <div class="md:pl-12 fade-in-section">
                    <div class="inline-block px-3 py-1 bg-amber-400/10 border border-amber-400/30 rounded font-mono text-[10px] text-amber-400 mb-2">2025 — Now</div>
                    <h3 class="font-display text-2xl font-bold text-white mb-2 group-hover:text-amber-400 transition-colors">Camelot Flows</h3>
                    <p class="text-slate-400 text-sm leading-relaxed">Named after my son Arthur. This isn't just a business—it's the castle I'm building for him, and for every business owner who deserves better.</p>
                </div>
                <div class="absolute left-6 md:left-1/2 md:-translate-x-1/2 top-1 w-4 h-4 rounded-full bg-amber-400 border-2 border-obsidian shadow-[0_0_15px_rgba(251,191,36,0.8)] group-hover:scale-150 transition-transform"></div>
            </div>

        </div>
    </div>
</section>

<!-- STITCH PHILOSOPHY -->
<section class="max-w-6xl mx-auto mb-32 relative">
    <div class="absolute top-1/2 right-0 -translate-y-1/2 w-[500px] h-[500px] bg-neon-purple/10 blur-[150px] rounded-full -z-10 pointer-events-none"></div>
    <h2 class="font-display text-3xl font-bold text-white uppercase tracking-tighter mb-12 text-center fade-in-section">Core <span class="text-transparent bg-clip-text bg-gradient-to-r from-neon-purple to-pink-500">Directives</span></h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="glass-card p-8 rounded-xl text-left border-t border-white/10 hover:border-amber-400/50 transition-colors fade-in-section">
            <span class="material-symbols-outlined text-5xl text-amber-400 mb-6 drop-shadow-[0_0_10px_rgba(251,191,36,0.6)]">balance</span>
            <h3 class="font-display text-2xl font-bold text-white mb-3">1. Tell the Truth</h3>
            <p class="text-slate-400 text-sm leading-relaxed">Sometimes I lose clients because of it. SEO can't guarantee anything. I never buy traffic. I never fake results. The honest path is the only path.</p>
        </div>
        <div class="glass-card p-8 rounded-xl text-left border-t border-white/10 hover:border-emerald-400/50 transition-colors fade-in-section delay-100">
            <span class="material-symbols-outlined text-5xl text-emerald-400 mb-6 drop-shadow-[0_0_10px_rgba(52,211,153,0.6)]">dns</span>
            <h3 class="font-display text-2xl font-bold text-white mb-3">2. Build, Not Rent</h3>
            <p class="text-slate-400 text-sm leading-relaxed">Your infrastructure should be yours. I deploy on dedicated VPS servers you control. You own your data, your agents, your entire system.</p>
        </div>
        <div class="glass-card p-8 rounded-xl text-left border-t border-white/10 hover:border-neon-cyan/50 transition-colors fade-in-section delay-200">
            <span class="material-symbols-outlined text-5xl text-neon-cyan mb-6 drop-shadow-[0_0_10px_rgba(0,242,255,0.6)]">model_training</span>
            <h3 class="font-display text-2xl font-bold text-white mb-3">3. AI as Standard</h3>
            <p class="text-slate-400 text-sm leading-relaxed">Every automation I sell, I've built and tested myself. No theoretical frameworks. Real pipelines, real agents powering massive efficiency.</p>
        </div>
    </div>
</section>

<!-- STITCH CTA -->
<section class="max-w-4xl mx-auto mb-24 fade-in-section relative">
    <div class="glass-panel text-center p-12 rounded-2xl border-2 border-primary/20 bg-gradient-to-b from-primary/5 to-black relative overflow-hidden group">
        <div class="absolute inset-0 bg-primary/10 -translate-y-full group-hover:translate-y-0 transition-transform duration-700"></div>
        <h2 class="font-display text-4xl font-bold text-white mb-6 relative z-10">Let's talk protocol.</h2>
        <p class="text-slate-400 mb-10 leading-relaxed max-w-xl mx-auto relative z-10">Whether you're a business owner drowning in routine, or an agency looking for a specialist weapon — I'm ready.</p>
        <button onclick="window.location.href='contact.html'" class="relative z-10 bg-primary/20 border-2 border-primary text-white font-mono font-bold uppercase tracking-[0.2em] text-sm py-4 px-10 rounded transition-all shadow-[0_0_20px_rgba(99,102,241,0.4)] hover:shadow-[0_0_40px_rgba(99,102,241,0.8)] hover:bg-primary">SUMMON_ALEX</button>
    </div>
</section>
</main>
'''"""

new_agencies_html = """save('for-agencies.html', 'For Agencies', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 grid-bg opacity-30 -z-20"></div>

<!-- STITCH HERO -->
<section class="max-w-6xl mx-auto text-center mb-24 fade-in-section relative">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-emerald-500/10 blur-[150px] rounded-full -z-10 pointer-events-none fade-in-section"></div>
    <span class="text-emerald-400 font-mono text-xs uppercase tracking-[0.3em] mb-4 block animate-pulse">// AGENCY PARTNERSHIP PROTOCOL</span>
    <h1 class="font-display text-5xl md:text-8xl font-black uppercase tracking-tighter mb-8 text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-600 drop-shadow-[0_0_20px_rgba(16,185,129,0.3)] pb-2">
        Your Clients<br/>Deserve Better.
    </h1>
    <p class="text-slate-400 text-lg md:text-xl max-w-3xl mx-auto leading-relaxed border-l-2 border-emerald-400/50 pl-6 text-left">
        I don't compete with agencies. I make them unstoppable. You own the brand strategy and client relationship. I deliver the award-winning code, AI automation, and infallible infrastructure.
    </p>
</section>

<!-- STITCH SERVICES GRID -->
<section class="max-w-7xl mx-auto mb-32 relative">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <div class="glass-card p-10 rounded-2xl border-t border-neon-cyan/30 hover:border-neon-cyan transition-all group fade-in-section relative overflow-hidden">
            <div class="absolute -right-10 -bottom-10 text-[180px] material-symbols-outlined text-neon-cyan/5 group-hover:text-neon-cyan/10 transition-all">design_services</div>
            <span class="material-symbols-outlined text-4xl text-neon-cyan mb-6">integration_instructions</span>
            <h3 class="font-display text-2xl font-bold text-white mb-4 uppercase">Frontend Architecture</h3>
            <p class="text-slate-400 text-sm leading-relaxed mb-6">Need an Awwwards submission? I build GSAP-powered, Tailwind-styled interfaces with smooth Lenis scroll, magnetic interactions, and cinematic parallax.</p>
            <div class="flex flex-wrap gap-2 text-[10px] font-mono font-bold text-neon-cyan uppercase">
                <span class="bg-neon-cyan/10 px-2 py-1 rounded border border-neon-cyan/30">GSAP</span>
                <span class="bg-neon-cyan/10 px-2 py-1 rounded border border-neon-cyan/30">Tailwind</span>
                <span class="bg-neon-cyan/10 px-2 py-1 rounded border border-neon-cyan/30">React/Next</span>
            </div>
        </div>

        <div class="glass-card p-10 rounded-2xl border-t border-neon-purple/30 hover:border-neon-purple transition-all group fade-in-section delay-100 relative overflow-hidden">
            <div class="absolute -right-10 -bottom-10 text-[180px] material-symbols-outlined text-neon-purple/5 group-hover:text-neon-purple/10 transition-all">smart_toy</div>
            <span class="material-symbols-outlined text-4xl text-neon-purple mb-6">memory</span>
            <h3 class="font-display text-2xl font-bold text-white mb-4 uppercase">AI Integration</h3>
            <p class="text-slate-400 text-sm leading-relaxed mb-6">Chatbots, AI sales agents, automated data pipelines. I deploy them on dedicated infrastructure your client owns. Real multi-agent systems with RAG workflow.</p>
            <div class="flex flex-wrap gap-2 text-[10px] font-mono font-bold text-neon-purple uppercase">
                <span class="bg-neon-purple/10 px-2 py-1 rounded border border-neon-purple/30">Python</span>
                <span class="bg-neon-purple/10 px-2 py-1 rounded border border-neon-purple/30">LangChain</span>
                <span class="bg-neon-purple/10 px-2 py-1 rounded border border-neon-purple/30">Ollama</span>
            </div>
        </div>

        <div class="glass-card p-10 rounded-2xl border-t border-primary/30 hover:border-primary transition-all group fade-in-section relative overflow-hidden">
            <div class="absolute -right-10 -bottom-10 text-[180px] material-symbols-outlined text-primary/5 group-hover:text-primary/10 transition-all">trending_up</div>
            <span class="material-symbols-outlined text-4xl text-primary mb-6">monitoring</span>
            <h3 class="font-display text-2xl font-bold text-white mb-4 uppercase">SEO & Performance</h3>
            <p class="text-slate-400 text-sm leading-relaxed mb-6">Core Web Vitals obsessed. Organic-only strategy. Google's algorithms have evolved—the old playbook is dead. I engineer sites to rank with clean, fast code.</p>
            <div class="flex flex-wrap gap-2 text-[10px] font-mono font-bold text-primary uppercase">
                <span class="bg-primary/10 px-2 py-1 rounded border border-primary/30">On-Page</span>
                <span class="bg-primary/10 px-2 py-1 rounded border border-primary/30">Technical</span>
                <span class="bg-primary/10 px-2 py-1 rounded border border-primary/30">Speed</span>
            </div>
        </div>

        <div class="glass-card p-10 rounded-2xl border-t border-amber-400/30 hover:border-amber-400 transition-all group fade-in-section delay-100 relative overflow-hidden">
            <div class="absolute -right-10 -bottom-10 text-[180px] material-symbols-outlined text-amber-400/5 group-hover:text-amber-400/10 transition-all">cloud_upload</div>
            <span class="material-symbols-outlined text-4xl text-amber-400 mb-6">terminal</span>
            <h3 class="font-display text-2xl font-bold text-white mb-4 uppercase">DevOps Setup</h3>
            <p class="text-slate-400 text-sm leading-relaxed mb-6">Your client runs on infrastructure they own—not SaaS subscriptions that bleed them dry. VPS routing, Docker, CI/CD pipelines, secured and handed over.</p>
            <div class="flex flex-wrap gap-2 text-[10px] font-mono font-bold text-amber-400 uppercase">
                <span class="bg-amber-400/10 px-2 py-1 rounded border border-amber-400/30">Docker</span>
                <span class="bg-amber-400/10 px-2 py-1 rounded border border-amber-400/30">Linux</span>
                <span class="bg-amber-400/10 px-2 py-1 rounded border border-amber-400/30">CI/CD</span>
            </div>
        </div>

    </div>
</section>

<!-- STITCH LIST -->
<section class="max-w-5xl mx-auto mb-32 fade-in-section">
    <div class="glass-panel p-10 md:p-16 rounded-3xl border-2 border-emerald-500/20 bg-gradient-to-tr from-emerald-500/5 to-black relative">
        <h2 class="font-display text-3xl font-bold text-white mb-10 text-center uppercase">Why Agencies <span class="text-emerald-400">Choose Me</span></h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8">
            <div class="flex items-start gap-4">
                <div class="w-8 h-8 rounded shrink-0 bg-emerald-500/20 border border-emerald-500/50 flex items-center justify-center text-emerald-400 material-symbols-outlined text-sm">done</div>
                <div>
                    <h4 class="font-display font-bold text-white text-lg">Zero Overhead</h4>
                    <p class="text-slate-400 text-sm mt-1">I operate as a one-man precision team. No bloat.</p>
                </div>
            </div>
            <div class="flex items-start gap-4">
                <div class="w-8 h-8 rounded shrink-0 bg-emerald-500/20 border border-emerald-500/50 flex items-center justify-center text-emerald-400 material-symbols-outlined text-sm">done</div>
                <div>
                    <h4 class="font-display font-bold text-white text-lg">White-Label Ready</h4>
                    <p class="text-slate-400 text-sm mt-1">Your brand, my build. Complete confidentiality.</p>
                </div>
            </div>
            <div class="flex items-start gap-4">
                <div class="w-8 h-8 rounded shrink-0 bg-emerald-500/20 border border-emerald-500/50 flex items-center justify-center text-emerald-400 material-symbols-outlined text-sm">done</div>
                <div>
                    <h4 class="font-display font-bold text-white text-lg">Global Arbitrage</h4>
                    <p class="text-slate-400 text-sm mt-1">Moldova pricing logic paired with EU/US-level quality output.</p>
                </div>
            </div>
            <div class="flex items-start gap-4">
                <div class="w-8 h-8 rounded shrink-0 bg-emerald-500/20 border border-emerald-500/50 flex items-center justify-center text-emerald-400 material-symbols-outlined text-sm">done</div>
                <div>
                    <h4 class="font-display font-bold text-white text-lg">Radical Honesty</h4>
                    <p class="text-slate-400 text-sm mt-1">I communicate directly. Even when the truth is uncomfortable.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- STITCH CTA -->
<section class="max-w-3xl mx-auto text-center mb-24 fade-in-section">
    <h2 class="font-display text-4xl font-bold text-white mb-6 uppercase tracking-tight">Make Your Next Project<br/>The One That <span class="text-emerald-400 border-b-2 border-emerald-400">Wins.</span></h2>
    <p class="text-slate-400 mb-10">Send the brief. I'll respond with strategic logic, cost feasibility, and deployment speed.</p>
    <button onclick="window.location.href='contact.html?objective=Agency'" class="bg-emerald-500 text-obsidian px-12 py-5 rounded-sm font-mono text-lg font-bold tracking-[0.2em] uppercase hover:bg-white transition-all shadow-[0_0_30px_rgba(16,185,129,0.5)]">
        INITIATE_PARTNERSHIP
    </button>
</section>
</main>
'''"""

# Replace ABOUT
about_pattern = re.compile(r"save\('about\.html'.*?</main>\s*'''\)", re.DOTALL)
code = re.sub(about_pattern, new_about_html, code)

# Replace AGENCIES
agencies_pattern = re.compile(r"save\('for-agencies\.html'.*?</main>\s*'''\)", re.DOTALL)
code = re.sub(agencies_pattern, new_agencies_html, code)

with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'w', 'utf-8') as f:
    f.write(code)

print("Batch 1 (About & Agencies) refactored with Pixel-Perfect ultra-premium UI arrays.")
