import re

filepath = 'c:/Users/user/Downloads/stitch_camelot_flows_homepage/code_v2.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    (
        r'<h2 class="font-display text-4xl md:text-5xl font-bold tracking-tighter text-white mb-2 uppercase">The High-Tech <br/>Round Table</h2>',
        r'<h2 class="font-display text-4xl md:text-5xl font-bold tracking-tighter text-white mb-2 uppercase">Core <br/>Capabilities</h2>'
    ),
    (
        r'<p class="font-mono text-xs text-primary mb-2">// SYSTEM_MODULES</p>\n<p class="text-slate-400 text-sm leading-relaxed">Elite protocols engineered for the modern sovereign entity. Zero latency. Maximum impact.</p>',
        r'<p class="font-mono text-xs text-primary mb-2">// SERVICES</p>\n<p class="text-slate-400 text-sm leading-relaxed">Comprehensive web and automation solutions engineered for ambitious growth.</p>'
    ),
    (
        r'<h3 class="font-display text-2xl font-bold mb-2 text-white uppercase">The Merlin Protocol</h3>\n    <div class="text-\[10px\] font-mono text-primary mb-6 tracking-widest uppercase">AI_SALES_AGENT_v1</div>\n    <p class="text-slate-400 mb-8 text-sm leading-relaxed border-l border-white/5 pl-4">\n                        Autonomous 24/7 AI agents that learn your brand\'s voice and close deals while you sleep.\n                    </p>\n    <div class="mt-auto pt-6 border-t border-white/5">\n    <ul class="space-y-3 text-xs font-mono text-slate-300">\n    <li class="flex items-center gap-3">\n    <span class="text-primary">&gt;</span> NLP_Mastery\n                            </li>\n    <li class="flex items-center gap-3">\n    <span class="text-primary">&gt;</span> Omni_Channel_Sync\n                            </li>',
        r'<h3 class="font-display text-2xl font-bold mb-2 text-white uppercase">Automation &amp; AI</h3>\n    <div class="text-[10px] font-mono text-primary mb-6 tracking-widest uppercase">WORKFLOW_SYSTEMS</div>\n    <p class="text-slate-400 mb-8 text-sm leading-relaxed border-l border-white/5 pl-4">\n                        Custom workflows and AI integrations that eliminate manual tasks and scale operations.\n                    </p>\n    <div class="mt-auto pt-6 border-t border-white/5">\n    <ul class="space-y-3 text-xs font-mono text-slate-300">\n    <li class="flex items-center gap-3">\n    <span class="text-primary">&gt;</span> Process_Automation\n                            </li>\n    <li class="flex items-center gap-3">\n    <span class="text-primary">&gt;</span> Custom_LLM_Apps\n                            </li>'
    ),
    (
        r'<h3 class="font-display text-2xl font-bold mb-2 text-white uppercase">Excalibur Web</h3>\n    <div class="text-\[10px\] font-mono text-indigo-300 mb-6 tracking-widest uppercase">INFRASTRUCTURE_CORE</div>\n    <p class="text-slate-300 mb-8 text-sm leading-relaxed border-l border-indigo-500/30 pl-4">\n                        High-Performance VPS &amp; WordPress architectures designed for speed, security, and total dominance.\n                    </p>',
        r'<h3 class="font-display text-2xl font-bold mb-2 text-white uppercase">Award-Winning Web</h3>\n    <div class="text-[10px] font-mono text-indigo-300 mb-6 tracking-widest uppercase">SITE_ARCHITECTURE</div>\n    <p class="text-slate-300 mb-8 text-sm leading-relaxed border-l border-indigo-500/30 pl-4">\n                        High-performance websites and landing pages designed for premium brands and market leaders.\n                    </p>'
    ),
    (
        r'<li class="flex items-center gap-3">\n    <span class="text-indigo-400 text-lg material-symbols-outlined">bolt</span> 99.9% Uptime SLA\n                            </li>\n    <li class="flex items-center gap-3">\n    <span class="text-indigo-400 text-lg material-symbols-outlined">public</span> Global CDN Grid\n                            </li>',
        r'<li class="flex items-center gap-3">\n    <span class="text-indigo-400 text-lg material-symbols-outlined">bolt</span> Custom Design\n                            </li>\n    <li class="flex items-center gap-3">\n    <span class="text-indigo-400 text-lg material-symbols-outlined">public</span> Conversion Focused\n                            </li>'
    ),
    (
        r'<h3 class="font-display text-2xl font-bold mb-2 text-white uppercase">Percival Parser</h3>\n    <div class="text-\[10px\] font-mono text-purple-400 mb-6 tracking-widest uppercase">DATA_INTEL_UNIT</div>\n    <p class="text-slate-400 mb-8 text-sm leading-relaxed border-l border-white/5 pl-4">\n                        Data Intelligence systems that extract, analyze, and synthesize raw data into actionable wisdom.\n                    </p>\n    <div class="mt-auto pt-6 border-t border-white/5">\n    <ul class="space-y-3 text-xs font-mono text-slate-300">\n    <li class="flex items-center gap-3">\n    <span class="text-purple-400">&gt;</span> Predictive_Analytics\n                            </li>\n    <li class="flex items-center gap-3">\n    <span class="text-purple-400">&gt;</span> Live_Dashboards\n                            </li>',
        r'<h3 class="font-display text-2xl font-bold mb-2 text-white uppercase">Agency White-Label</h3>\n    <div class="text-[10px] font-mono text-purple-400 mb-6 tracking-widest uppercase">PARTNERSHIP_TIER</div>\n    <p class="text-slate-400 mb-8 text-sm leading-relaxed border-l border-white/5 pl-4">\n                        Reliable development and automation support designed to scale your agency\'s delivery capabilities.\n                    </p>\n    <div class="mt-auto pt-6 border-t border-white/5">\n    <ul class="space-y-3 text-xs font-mono text-slate-300">\n    <li class="flex items-center gap-3">\n    <span class="text-purple-400">&gt;</span> NDA_Protected\n                            </li>\n    <li class="flex items-center gap-3">\n    <span class="text-purple-400">&gt;</span> Seamless_Integration\n                            </li>'
    ),
    (
        r'<p class="terminal-step text-slate-400 mb-10 text-base font-light">Our flows aren\'t just code; they are magical circuits that turn customer interaction into business growth without human friction.</p>',
        r'<p class="terminal-step text-slate-400 mb-10 text-base font-light">Our workflows aren\'t just code; they are connected systems that turn customer interaction into business growth without manual bottlenecks.</p>'
    ),
    (
        r'<h4 class="font-mono font-bold text-sm text-green-400">01_WHATSAPP_INTAKE</h4>\n<p class="text-xs text-slate-500 mt-1">Capture leads via encrypted channels.</p>',
        r'<h4 class="font-mono font-bold text-sm text-green-400">01_LEAD_INTAKE</h4>\n<p class="text-xs text-slate-500 mt-1">Capture leads via your preferred channels.</p>'
    ),
    (
        r'<h4 class="font-mono font-bold text-sm text-indigo-400">02_MERLIN_CORE</h4>\n<p class="text-xs text-slate-500 mt-1">Contextual decision making engine.</p>',
        r'<h4 class="font-mono font-bold text-sm text-indigo-400">02_DECISION_ENGINE</h4>\n<p class="text-xs text-slate-500 mt-1">Contextual routing and task generation.</p>'
    ),
    (
        r'<h2 class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">The Grand<br/><span class="text-neon-cyan text-glow-cyan">Armory</span></h2>\n            <p class="text-white/50 text-base font-light leading-relaxed mb-8">\n                Equip your operation with Awwwards-tier professional site templates, bespoke software systems, and battle-tested digital infrastructures. Our forge burns bright to deliver code wrought with perfection and unbreakable architecture.\n            </p>',
        r'<h2 class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">Asset<br/><span class="text-neon-cyan text-glow-cyan">Showcase</span></h2>\n            <p class="text-white/50 text-base font-light leading-relaxed mb-8">\n                Showcase of past web and automation builds. Explore live projects, concepts, and internal tools built for ambitious companies.\n            </p>'
    ),
    (
        r'<h2 class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">Alchemist\'s<br/><span class="text-neon-purple text-glow-purple">Sanctum</span></h2>\n            <p class="text-white/50 text-base font-light leading-relaxed mb-8">\n                Transmute raw data into automated action. We provide complex AI automation scripts, deep learning agents, and intelligent workflow systems that operate relentlessly. Turn friction into limitless kinetic energy.\n            </p>',
        r'<h2 class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">Workflow<br/><span class="text-neon-purple text-glow-purple">Automations</span></h2>\n            <p class="text-white/50 text-base font-light leading-relaxed mb-8">\n                Turn manual data entry into automated action. We build robust automation scripts, connected systems, and custom workflows that operate relentlessly and save hundreds of hours.\n            </p>'
    ),
    (
        r'<h2 class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">Aesthetic<br/><span class="text-emerald-400 text-glow" style="text-shadow: 0 0 20px rgba\(16,185,129,0\.5\)">Excellence</span></h2>\n            <p class="text-white/50 text-base font-light leading-relaxed mb-8">\n                Elevate your brand with award-winning UI/UX interfaces and fluid GSAP animations. We architect visually stunning digital experiences that convert, guaranteeing absolute user engagement.\n            </p>',
        r'<h2 class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">Aesthetic<br/><span class="text-emerald-400 text-glow" style="text-shadow: 0 0 20px rgba(16,185,129,0.5)">Excellence</span></h2>\n            <p class="text-white/50 text-base font-light leading-relaxed mb-8">\n                Elevate your brand with premium UI/UX interfaces and fluid animations. We architect visually stunning digital experiences that convert.\n            </p>'
    ),
    (
        r'<h2 class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">Cybernetic<br/><span class="text-indigo-400 text-glow" style="text-shadow: 0 0 20px rgba\(99,102,241,0\.5\)">Augmentations</span></h2>\n            <p class="text-white/50 text-base font-light leading-relaxed mb-8">\n                Seamlessly graft Camelot Flows into your existing enterprise architecture. We fuse our bleeding-edge AI modules with your legacy CRM/ERP systems, transforming outdated workflows into highly reactive, hyper-cognizant data nervous systems.\n            </p>',
        r'<h2 class="font-display text-4xl md:text-6xl lg:text-7xl font-black text-white uppercase tracking-tighter mb-6">System<br/><span class="text-indigo-400 text-glow" style="text-shadow: 0 0 20px rgba(99,102,241,0.5)">Integrations</span></h2>\n            <p class="text-white/50 text-base font-light leading-relaxed mb-8">\n                Seamlessly integrate our modules into your existing architecture. We connect custom tools with your CRM/ERP systems, transforming disconnected workflows into a unified setup.\n            </p>'
    ),
    (
        r'<h1 class="text-neon-cyan tracking-\[0\.5em\] text-sm font-bold uppercase mb-6 neon-text-cyan">Protocol: Acquisition</h1>\n                <h2 class="text-white font-display text-5xl md:text-8xl font-black leading-\[1\.1\] tracking-tighter mb-6 uppercase">ESTABLISH<br/><span class="text-transparent bg-clip-text bg-gradient-to-r from-\[#bf00ff\] to-\[#0066ff\]">DOMINANCE</span></h2>\n                <div class="h-\[1px\] w-24 bg-gradient-to-r from-transparent via-\[#bf00ff\] to-transparent mx-auto mb-8"></div>\n                <p class="text-white/50 text-xl font-light leading-relaxed max-w-2xl mx-auto">\n                    Select your holographic interface tier to begin deep-sector market manipulation.\n                </p>',
        r'<h1 class="text-neon-cyan tracking-[0.5em] text-sm font-bold uppercase mb-6 neon-text-cyan">Engagement Models</h1>\n                <h2 class="text-white font-display text-5xl md:text-8xl font-black leading-[1.1] tracking-tighter mb-6 uppercase">CHOOSE YOUR<br/><span class="text-transparent bg-clip-text bg-gradient-to-r from-[#bf00ff] to-[#0066ff]">PATH</span></h2>\n                <div class="h-[1px] w-24 bg-gradient-to-r from-transparent via-[#bf00ff] to-transparent mx-auto mb-8"></div>\n                <p class="text-white/50 text-xl font-light leading-relaxed max-w-2xl mx-auto">\n                    Select how you want to work with us to accelerate your growth.\n                </p>'
    ),
    (
        r'<h3 class="text-white text-3xl font-display font-bold tracking-\[0\.05em\] uppercase">Merlin Core</h3>\n                        <span class="text-neon-cyan text-\[10px\] font-bold tracking-\[0\.3em\] uppercase bg-neon-cyan/10 border border-neon-cyan/30 px-3 py-1 rounded">Level 01</span>',
        r'<h3 class="text-white text-3xl font-display font-bold tracking-[0.05em] uppercase">Project Scope</h3>\n                        <span class="text-neon-cyan text-[10px] font-bold tracking-[0.3em] uppercase bg-neon-cyan/10 border border-neon-cyan/30 px-3 py-1 rounded">One-Off</span>'
    ),
    (
        r'<button onclick="window\.location\.href=\'contact\.html\?objective=merlin\'" class="bg-neon-cyan/10 border border-neon-cyan/50 text-neon-cyan w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-cyan hover:text-obsidian transition-all duration-300 text-center cursor-pointer">Initiate Core</button>',
        r'<button onclick="window.location.href=\'contact.html?objective=project\'" class="bg-neon-cyan/10 border border-neon-cyan/50 text-neon-cyan w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-cyan hover:text-obsidian transition-all duration-300 text-center cursor-pointer">Start Project</button>'
    ),
    (
        r'<h3 class="text-white text-3xl font-display font-bold tracking-\[0\.05em\] uppercase">Percival Data</h3>\n                        <span class="text-neon-purple text-\[10px\] font-bold tracking-\[0\.3em\] uppercase bg-neon-purple/10 border border-neon-purple/30 px-3 py-1 rounded neon-text-purple">Level 02 // Rec\.</span>',
        r'<h3 class="text-white text-3xl font-display font-bold tracking-[0.05em] uppercase">Vanguard Support</h3>\n                        <span class="text-neon-purple text-[10px] font-bold tracking-[0.3em] uppercase bg-neon-purple/10 border border-neon-purple/30 px-3 py-1 rounded neon-text-purple">Retainer</span>'
    ),
    (
        r'<button onclick="window\.location\.href=\'contact\.html\?objective=percival\'" class="bg-neon-purple text-obsidian w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-white hover:text-black transition-colors text-center shadow-\[0_0_20px_rgba\(191,0,255,0\.4\)\] cursor-pointer">Establish Uplink</button>',
        r'<button onclick="window.location.href=\'contact.html?objective=retainer\'" class="bg-neon-purple text-obsidian w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-white hover:text-black transition-colors text-center shadow-[0_0_20px_rgba(191,0,255,0.4)] cursor-pointer">Discuss Retainer</button>'
    ),
    (
        r'<h3 class="text-white text-3xl font-display font-bold tracking-\[0\.05em\] uppercase">Excalibur Env</h3>\n                        <span class="text-neon-blue text-\[10px\] font-bold tracking-\[0\.3em\] uppercase bg-neon-blue/10 border border-neon-blue/30 px-3 py-1 rounded">Level 03</span>',
        r'<h3 class="text-white text-3xl font-display font-bold tracking-[0.05em] uppercase">Agency Partner</h3>\n                        <span class="text-neon-blue text-[10px] font-bold tracking-[0.3em] uppercase bg-neon-blue/10 border border-neon-blue/30 px-3 py-1 rounded">White-Label</span>'
    ),
    (
        r'<button onclick="window\.location\.href=\'contact\.html\?objective=excalibur\'" class="bg-neon-blue/10 border border-neon-blue/50 text-neon-blue w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-blue hover:text-white transition-all duration-300 text-center cursor-pointer">Summon Env</button>',
        r'<button onclick="window.location.href=\'for-agencies.html\'" class="bg-neon-blue/10 border border-neon-blue/50 text-neon-blue w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-blue hover:text-white transition-all duration-300 text-center cursor-pointer">Learn More</button>'
    )
]

for src, dst in replacements:
    html, count = re.subn(src, dst, html)
    print(f"Replaced {count} times")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
