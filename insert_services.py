import codecs

services_html = """
# ========== SERVICE: SITE CREATION ==========
save('service-creation.html', 'Site Creation | Forging Digital Kingdoms', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 grid-bg opacity-20 -z-20"></div>

<section class="max-w-6xl mx-auto text-center mb-24 fade-in-section relative">
<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-neon-cyan/10 blur-[150px] rounded-full -z-10 pointer-events-none"></div>
<span class="text-neon-cyan font-mono text-xs uppercase tracking-[0.3em] mb-4 block">// SERVICE_01</span>
<h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-transparent bg-clip-text bg-gradient-to-r from-neon-cyan to-indigo-500 pb-2">Forging Digital<br/>Kingdoms</h1>
<p class="text-slate-400 text-lg max-w-2xl mx-auto leading-relaxed">End-to-end web development crafted with an award-winning High-Tech Arthurian aesthetic. From landing pages to full applications, built with unmatched precision.</p>
</section>

<section class="max-w-7xl mx-auto mb-24 fade-in-section">
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
    <!-- Tier 1 -->
    <div class="glass-card p-8 rounded-xl border-t border-neon-cyan/30 relative group overflow-hidden">
        <div class="absolute top-0 right-0 p-4 opacity-10"><span class="material-symbols-outlined text-6xl text-neon-cyan">web</span></div>
        <h3 class="font-display text-2xl font-bold text-white mb-2 uppercase">The Squire</h3>
        <p class="font-mono text-xs text-neon-cyan mb-6">Timeline: 2-4 Weeks</p>
        <div class="text-3xl font-mono font-bold text-white mb-6">$300</div>
        <ul class="space-y-4 text-sm text-slate-400 mb-8 border-t border-white/5 pt-6">
            <li class="flex items-center gap-3"><span class="text-neon-cyan material-symbols-outlined text-sm">check</span> Custom Landing Page</li>
            <li class="flex items-center gap-3"><span class="text-neon-cyan material-symbols-outlined text-sm">check</span> CMS Integration</li>
            <li class="flex items-center gap-3"><span class="text-neon-cyan material-symbols-outlined text-sm">check</span> Basic SEO Setup</li>
            <li class="flex items-center gap-3"><span class="text-neon-cyan material-symbols-outlined text-sm">check</span> Mobile Optimized</li>
        </ul>
        <button onclick="window.location.href='contact.html?objective=Round Table'" class="w-full py-4 rounded bg-neon-cyan/10 border border-neon-cyan/50 text-neon-cyan font-mono text-sm font-bold uppercase tracking-widest hover:bg-neon-cyan hover:text-obsidian transition-colors">Select Tier</button>
    </div>
    
    <!-- Tier 2 -->
    <div class="glass-card p-8 rounded-xl border-t-2 border-neon-purple scale-105 relative group overflow-hidden shadow-[0_0_30px_rgba(191,0,255,0.15)]">
        <div class="absolute -top-12 right-0 w-32 h-32 bg-neon-purple/20 blur-3xl rounded-full"></div>
        <div class="absolute top-0 right-0 p-4 opacity-10"><span class="material-symbols-outlined text-6xl text-neon-purple">code_blocks</span></div>
        <div class="bg-neon-purple text-obsidian text-[10px] font-mono font-bold px-3 py-1 inline-block rounded mb-4 tracking-widest uppercase">Recommended</div>
        <h3 class="font-display text-2xl font-bold text-white mb-2 uppercase">The Knight</h3>
        <p class="font-mono text-xs text-neon-purple mb-6">Timeline: 4-8 Weeks</p>
        <div class="text-3xl font-mono font-bold text-neon-purple mb-6">$800</div>
        <ul class="space-y-4 text-sm text-white/90 mb-8 border-t border-white/5 pt-6">
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-sm">check</span> Full Custom Website (Up to 10 Pages)</li>
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-sm">check</span> GSAP Advanced Animations</li>
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-sm">check</span> Custom CMS / E-Commerce</li>
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-sm">check</span> Technical &amp; On-Page SEO</li>
        </ul>
        <button onclick="window.location.href='contact.html?objective=Round Table'" class="w-full py-4 rounded bg-neon-purple text-obsidian font-mono text-sm font-bold uppercase tracking-widest hover:bg-white hover:text-obsidian transition-colors shadow-[0_0_15px_rgba(191,0,255,0.4)]">Select Tier</button>
    </div>

    <!-- Tier 3 -->
    <div class="glass-card p-8 rounded-xl border-t border-amber-400/30 relative group overflow-hidden">
        <div class="absolute top-0 right-0 p-4 opacity-10"><span class="material-symbols-outlined text-6xl text-amber-400">api</span></div>
        <h3 class="font-display text-2xl font-bold text-white mb-2 uppercase">The King</h3>
        <p class="font-mono text-xs text-amber-400 mb-6">Timeline: 8-12+ Weeks</p>
        <div class="text-3xl font-mono font-bold text-white mb-6">$2,000+</div>
        <ul class="space-y-4 text-sm text-slate-400 mb-8 border-t border-white/5 pt-6">
            <li class="flex items-center gap-3"><span class="text-amber-400 material-symbols-outlined text-sm">check</span> Full Web Application / SaaS UI</li>
            <li class="flex items-center gap-3"><span class="text-amber-400 material-symbols-outlined text-sm">check</span> Headless Architecture (Next.js / Vue)</li>
            <li class="flex items-center gap-3"><span class="text-amber-400 material-symbols-outlined text-sm">check</span> Complex Database Integrations</li>
            <li class="flex items-center gap-3"><span class="text-amber-400 material-symbols-outlined text-sm">check</span> Interactive 3D / WebGL Elements</li>
        </ul>
        <button onclick="window.location.href='contact.html?objective=Excalibur'" class="w-full py-4 rounded bg-amber-400/10 border border-amber-400/50 text-amber-400 font-mono text-sm font-bold uppercase tracking-widest hover:bg-amber-400 hover:text-obsidian transition-colors">Select Tier</button>
    </div>
</div>
</section>

<section class="max-w-4xl mx-auto text-center mb-24 fade-in-section">
<button onclick="window.location.href='contact.html?objective=Round Table'" class="bg-obsidian border-2 border-neon-cyan text-neon-cyan px-12 py-5 rounded-full font-mono text-lg font-bold tracking-[0.2em] uppercase hover:bg-neon-cyan hover:text-obsidian transition-colors shadow-[0_0_30px_rgba(0,242,255,0.4)] animate-pulse">
    Engage the Forge
</button>
</section>
</main>
''')

# ========== SERVICE: SITE MAINTENANCE ==========
save('service-maintenance.html', 'Site Maintenance | Vanguard Protection', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 grid-bg opacity-30 -z-20"></div>

<section class="max-w-6xl mx-auto mb-20 fade-in-section relative grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
    <div>
        <span class="text-emerald-400 font-mono text-xs uppercase tracking-[0.3em] mb-4 block">// SERVICE_02</span>
        <h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-600 pb-2">Vanguard<br/>Protection</h1>
        <p class="text-slate-400 text-lg leading-relaxed mb-8">Continuous monitoring, impenetrable security, and hyper-optimized performance. Guardian of your digital kingdom 24/7.</p>
        <button onclick="window.location.href='contact.html'" class="bg-emerald-500/10 border border-emerald-500/50 text-emerald-400 px-8 py-4 rounded font-mono text-sm font-bold tracking-[0.2em] uppercase hover:bg-emerald-500 hover:text-obsidian transition-colors shadow-[0_0_20px_rgba(16,185,129,0.3)] inset-shadow">
            Summon Support
        </button>
    </div>
    
    <div class="glass-panel p-6 rounded-2xl border border-emerald-500/30 relative overflow-hidden bg-black/60 shadow-[0_0_40px_rgba(16,185,129,0.1)]">
        <div class="flex justify-between items-center mb-6 border-b border-white/5 pb-4">
            <h3 class="font-mono text-xs text-emerald-400 tracking-widest uppercase flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> SYSTEM_UPTIME</h3>
            <span class="font-display text-2xl text-emerald-300 font-black">99.9%</span>
        </div>
        <div class="h-40 flex items-end gap-2 px-2">
            <div class="w-full bg-emerald-500/20 h-[60%] rounded-t border-t border-emerald-500 hover:bg-emerald-500/40 transition-all cursor-pointer relative group"><div class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 text-[10px] font-mono text-emerald-400 transition-opacity">Optimal</div></div>
            <div class="w-full bg-emerald-500/20 h-[70%] rounded-t border-t border-emerald-500 hover:bg-emerald-500/40 transition-all cursor-pointer"></div>
            <div class="w-full bg-emerald-500/20 h-[65%] rounded-t border-t border-emerald-500 hover:bg-emerald-500/40 transition-all cursor-pointer"></div>
            <div class="w-full bg-emerald-500/20 h-[80%] rounded-t border-t border-emerald-500 hover:bg-emerald-500/40 transition-all cursor-pointer"></div>
            <div class="w-full bg-emerald-500/20 h-[95%] rounded-t border-t border-emerald-500 hover:bg-emerald-500/40 transition-all cursor-pointer relative group"><div class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 text-[10px] font-mono text-emerald-400 transition-opacity">Max Load</div></div>
            <div class="w-full bg-emerald-500/20 h-[90%] rounded-t border-t border-emerald-500 hover:bg-emerald-500/40 transition-all cursor-pointer"></div>
            <div class="w-full bg-emerald-500/20 h-[100%] rounded-t border-t border-emerald-500 hover:bg-emerald-500/40 transition-all cursor-pointer"></div>
        </div>
        <div class="flex justify-between mt-4 text-[10px] font-mono text-slate-500">
            <span>T-7 DAYS</span>
            <span>CURRENT</span>
        </div>
    </div>
</section>

<section class="max-w-6xl mx-auto mb-24 fade-in-section">
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <div class="glass-card p-8 rounded-xl border-l-2 border-emerald-500">
        <h3 class="font-display text-2xl text-white mb-2">Essential Ward</h3>
        <p class="font-mono text-emerald-400 text-sm mb-4">$49 / month</p>
        <p class="text-slate-400 text-sm mb-6">Basic security and updates to keep your site running smoothly.</p>
        <ul class="space-y-3 text-sm text-slate-300">
            <li class="flex items-center gap-2"><span class="text-emerald-500">&gt;</span> Daily Backups</li>
            <li class="flex items-center gap-2"><span class="text-emerald-500">&gt;</span> Plugin/Theme Updates</li>
            <li class="flex items-center gap-2"><span class="text-emerald-500">&gt;</span> Malware Scanning</li>
        </ul>
    </div>
    <div class="glass-card p-8 rounded-xl border-l-2 border-neon-purple shadow-[0_0_20px_rgba(191,0,255,0.1)]">
        <h3 class="font-display text-2xl text-white mb-2">Vanguard Zenith</h3>
        <p class="font-mono text-neon-purple text-sm mb-4">$149 / month</p>
        <p class="text-slate-400 text-sm mb-6">Complete peace of mind with dedicated developer hours and priority support.</p>
        <ul class="space-y-3 text-sm text-slate-300">
            <li class="flex items-center gap-2"><span class="text-neon-purple">&gt;</span> Everything in Essential Ward</li>
            <li class="flex items-center gap-2"><span class="text-neon-purple">&gt;</span> 2 Hours Custom Development</li>
            <li class="flex items-center gap-2"><span class="text-neon-purple">&gt;</span> Speed &amp; Core Web Vitals Optimization</li>
            <li class="flex items-center gap-2"><span class="text-neon-purple">&gt;</span> 24/7 Priority Emergency Support</li>
        </ul>
    </div>
</div>
</section>
</main>
''')

# ========== SERVICE: BUSINESS AUTOMATION ==========
save('service-automation.html', 'Business Automations | Alchemist Scripts', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/circuit-board.png')] opacity-10 mix-blend-screen -z-20"></div>

<section class="max-w-6xl mx-auto text-center mb-20 fade-in-section relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full bg-gradient-to-b from-neon-purple/20 to-transparent blur-[100px] -z-10 pointer-events-none"></div>
<span class="text-neon-purple font-mono text-xs uppercase tracking-[0.3em] mb-4 block">// SERVICE_03</span>
<h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-transparent bg-clip-text bg-gradient-to-r from-neon-purple to-[#ff00ff] pb-2">Alchemist<br/>Scripts</h1>
<p class="text-slate-400 text-lg max-w-2xl mx-auto leading-relaxed mb-8">Turning Logic into Gold. We architect deep integrations using Python, Zapier, Make, and local LLMs to obliterate manual workflows.</p>

<div class="max-w-3xl mx-auto bg-black/80 rounded-xl border border-neon-purple/30 text-left p-4 shadow-[0_0_30px_rgba(191,0,255,0.2)] font-mono text-sm overflow-hidden relative">
    <div class="flex gap-2 mb-4 border-b border-white/10 pb-2">
        <div class="w-3 h-3 rounded-full bg-red-500/50"></div>
        <div class="w-3 h-3 rounded-full bg-amber-500/50"></div>
        <div class="w-3 h-3 rounded-full bg-emerald-500/50"></div>
        <span class="text-[10px] text-slate-500 ml-4 absolute left-12 top-4">merlin_agent.py - Execution Log</span>
    </div>
    <div class="text-green-400 space-y-1 h-[120px] overflow-hidden flex flex-col justify-end">
        <p class="opacity-50">&gt; Retrieving CRM lead data [OK]</p>
        <p class="opacity-70">&gt; Analyzing intent with Local LLM (Llama-3)...</p>
        <p class="opacity-90">&gt; Intent recognized: "High-Value Consultation"</p>
        <p class="text-white">&gt; Generating custom proposal drafting script... [SUCCESS]</p>
        <p class="text-neon-purple animate-pulse">&gt; Dispatching email to client &amp; pinging Slack // Pipeline Complete. Saved 45 mins.</p>
    </div>
</div>
</section>

<section class="max-w-7xl mx-auto mb-24 fade-in-section">
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
    <div class="glass-card p-8 rounded-xl border-t border-slate-600">
        <h3 class="font-display text-2xl text-white mb-2">Initiate</h3>
        <p class="font-mono text-slate-400 text-sm mb-6">From $150 / workflow</p>
        <ul class="space-y-4 text-sm text-slate-400 mb-8 border-t border-white/5 pt-6">
            <li class="flex items-center gap-3"><span class="text-slate-500 material-symbols-outlined text-sm">bolt</span> Basic Zapier/Make setup</li>
            <li class="flex items-center gap-3"><span class="text-slate-500 material-symbols-outlined text-sm">bolt</span> Lead generation routing</li>
            <li class="flex items-center gap-3"><span class="text-slate-500 material-symbols-outlined text-sm">bolt</span> Simple email sequences</li>
        </ul>
    </div>
    <div class="glass-card p-8 rounded-xl border-t-2 border-neon-purple scale-105 shadow-[0_0_20px_rgba(191,0,255,0.15)] relative">
        <div class="absolute top-0 right-0 py-1 px-3 bg-neon-purple/20 text-neon-purple font-mono text-[10px] rounded-bl">POPULAR</div>
        <h3 class="font-display text-2xl text-white mb-2">Adept</h3>
        <p class="font-mono text-neon-purple text-sm mb-6">From $400 / system</p>
        <ul class="space-y-4 text-sm text-white/90 mb-8 border-t border-white/5 pt-6">
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-sm">auto_fix_high</span> Custom Python Scripts</li>
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-sm">auto_fix_high</span> Basic AI integration (OpenAI API)</li>
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-sm">auto_fix_high</span> Dynamic Document Generation</li>
        </ul>
        <button onclick="window.location.href='contact.html?objective=Merlin'" class="w-full py-3 rounded bg-neon-purple text-obsidian font-mono text-sm font-bold tracking-widest uppercase shadow-[0_0_15px_rgba(191,0,255,0.4)] hover:bg-white transition-colors">Summon Automation</button>
    </div>
    <div class="glass-card p-8 rounded-xl border-t border-amber-400/50">
        <h3 class="font-display text-2xl text-white mb-2">Grandmaster</h3>
        <p class="font-mono text-amber-400 text-sm mb-6">From $800 / architecture</p>
        <ul class="space-y-4 text-sm text-slate-300 mb-8 border-t border-white/5 pt-6">
            <li class="flex items-center gap-3"><span class="text-amber-400 material-symbols-outlined text-sm">diamond</span> Autonomous Multi-Agent Workflows</li>
            <li class="flex items-center gap-3"><span class="text-amber-400 material-symbols-outlined text-sm">diamond</span> Custom Knowledge Base (RAG)</li>
            <li class="flex items-center gap-3"><span class="text-amber-400 material-symbols-outlined text-sm">diamond</span> VPS Setup &amp; Deployment</li>
        </ul>
    </div>
</div>
</section>
</main>
''')

# ========== SERVICE: MARKETING ==========
save('service-marketing.html', 'Marketing | Growth Protocol', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 grid-bg opacity-30 -z-20"></div>

<section class="max-w-6xl mx-auto text-center mb-24 fade-in-section relative">
<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[400px] bg-amber-500/10 blur-[120px] rounded-full -z-10 pointer-events-none"></div>
<span class="text-amber-400 font-mono text-xs uppercase tracking-[0.3em] mb-4 block">// SERVICE_04</span>
<h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-600 pb-2">Growth<br/>Protocol</h1>
<p class="text-slate-400 text-lg max-w-2xl mx-auto leading-relaxed mb-12">10x Acquisition Engine. Google Ads, Meta SMM, and hyper-targeted conversion rate optimization.</p>

<div class="flex flex-col md:flex-row justify-center gap-6 max-w-4xl mx-auto">
    <div class="glass-panel p-6 rounded-xl flex-1 border border-neon-cyan/30 bg-black/50 hover:bg-black/80 transition-all text-left group">
        <span class="font-mono text-xs text-slate-400 mb-2 block">PROJECTED ROI</span>
        <div class="text-5xl font-display font-black text-neon-cyan mb-2 group-hover:scale-110 transition-transform origin-left">340%</div>
        <div class="w-full h-1 bg-white/5 rounded"><div class="w-[75%] h-full bg-neon-cyan rounded shadow-[0_0_10px_rgba(0,242,255,0.8)]"></div></div>
    </div>
    <div class="glass-panel p-6 rounded-xl flex-1 border border-amber-400/30 bg-black/50 hover:bg-black/80 transition-all text-left group">
        <span class="font-mono text-xs text-slate-400 mb-2 block">CONVERSION LIFT</span>
        <div class="text-5xl font-display font-black text-amber-400 mb-2 group-hover:scale-110 transition-transform origin-left">2.8x</div>
        <div class="w-full h-1 bg-white/5 rounded"><div class="w-[85%] h-full bg-amber-400 rounded shadow-[0_0_10px_rgba(251,191,36,0.8)]"></div></div>
    </div>
</div>
</section>

<section class="max-w-5xl mx-auto mb-24 fade-in-section">
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <div class="glass-card p-10 rounded-xl border-t border-white/10 hover:border-amber-400/50 transition-colors cursor-default relative overflow-hidden">
        <div class="absolute -bottom-10 -right-10 text-amber-400/5 material-symbols-outlined text-[150px]">campaign</div>
        <h3 class="font-display text-3xl font-bold text-white mb-2">Google Ads Strategy</h3>
        <p class="text-slate-400 mb-6">Stop burning budget on broad match keywords. I structure hyper-specific Search and Performance Max campaigns that target buying intent, backed by custom tracking mechanisms.</p>
        <button onclick="window.location.href='contact.html?objective=Agency'" class="text-amber-400 font-mono text-sm tracking-widest uppercase hover:underline">Discuss Strategy &gt;</button>
    </div>
    <div class="glass-card p-10 rounded-xl border-t border-white/10 hover:border-neon-cyan/50 transition-colors cursor-default relative overflow-hidden">
        <div class="absolute -bottom-10 -right-10 text-neon-cyan/5 material-symbols-outlined text-[150px]">query_stats</div>
        <h3 class="font-display text-3xl font-bold text-white mb-2">SEO &amp; CRO</h3>
        <p class="text-slate-400 mb-6">Technical SEO combined with Conversion Rate Optimization. Getting traffic isn't enough—your landing pages need to convert. We test flows, heatmaps, and optimize continuously.</p>
        <button onclick="window.location.href='contact.html?objective=Agency'" class="text-neon-cyan font-mono text-sm tracking-widest uppercase hover:underline">Audits Available &gt;</button>
    </div>
</div>
</section>

<section class="max-w-3xl mx-auto text-center mb-24 fade-in-section">
<button onclick="window.location.href='contact.html?objective=Agency'" class="bg-amber-500/10 border-2 border-amber-500 text-amber-400 px-12 py-5 rounded font-mono text-lg font-bold tracking-[0.2em] uppercase hover:bg-amber-500 hover:text-obsidian transition-all shadow-[0_0_30px_rgba(245,158,11,0.4)] inset-shadow">
    Initiate Campaign
</button>
</section>
</main>
'''
"""

with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'r', 'utf-8') as f:
    code = f.read()

if "SERVICE_01" not in code:
    insertion_point = 'print("\\nAll pages created successfully!")'
    new_code = code.replace(insertion_point, services_html + '\n' + insertion_point)
    with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'w', 'utf-8') as f:
        f.write(new_code)
    print("Services injected successfully.")
else:
    print("Already inserted.")
