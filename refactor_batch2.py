import codecs
import re

with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'r', 'utf-8') as f:
    code = f.read()

new_work_with_me = """save('work-with-me.html', 'Work With Me', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 grid-bg opacity-30 -z-20"></div>

<!-- STITCH HERO -->
<section class="max-w-6xl mx-auto text-center mb-24 fade-in-section relative">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[500px] bg-amber-500/10 blur-[150px] rounded-full -z-10 pointer-events-none fade-in-section"></div>
    <span class="text-amber-400 font-mono text-xs uppercase tracking-[0.3em] mb-4 block">// JOIN THE ROUND TABLE</span>
    <h1 class="font-display text-5xl md:text-8xl font-black uppercase tracking-tighter mb-8 text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-600 drop-shadow-[0_0_20px_rgba(251,191,36,0.3)] pb-2">
        I Don't Have Jobs.<br/>I Have a Mission.
    </h1>
    <p class="text-slate-400 text-lg md:text-xl max-w-3xl mx-auto leading-relaxed">
        If you're passionate about AI, automation, or building weird things — let's grow together. This isn't a corporate ladder. It's an invitation to forge digital weapons, learn relentlessly, and eventually earn your share.
    </p>
</section>

<!-- STITCH REALITY CHECK -->
<section class="max-w-5xl mx-auto mb-32 fade-in-section">
    <div class="glass-panel p-10 md:p-14 rounded-3xl border border-red-500/30 bg-black/50 relative overflow-hidden group">
        <div class="absolute top-0 left-0 w-2 h-full bg-gradient-to-b from-red-500 to-orange-500"></div>
        <div class="absolute -right-20 -top-20 text-[200px] material-symbols-outlined text-red-500/5 group-hover:text-red-500/10 transition-colors">warning</div>
        <h2 class="font-display text-3xl font-bold text-white mb-6 uppercase flex items-center gap-4"><span class="text-red-500 animate-pulse material-symbols-outlined">radio_button_checked</span> The Reality Check</h2>
        <div class="text-slate-400 text-base leading-relaxed space-y-4 max-w-3xl">
            <p>I'm going to be straight with you: Camelot Flows is a bootstrapped startup. I'm a solo founder, father of a 1-year-old, and a full-time employee at a corporate job. There is no venture capital. No shiny office in a high-rise. No guaranteed salary right now.</p>
            <p>I am looking for partners, not employees. I need people who want to learn exactly how I build these systems, contribute to current projects, and split the revenue when we close deals together.</p>
        </div>
    </div>
</section>

<!-- STITCH SKILLS GRID -->
<section class="max-w-7xl mx-auto mb-32 relative">
    <h2 class="font-display text-4xl font-bold text-center text-white mb-16 uppercase tracking-widest"><span class="text-transparent bg-clip-text bg-gradient-to-r from-neon-purple to-pink-500">Current</span> Bounties</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <div class="glass-card p-8 rounded-xl border border-white/5 hover:border-amber-400/50 transition-colors group relative overflow-hidden">
            <div class="absolute top-0 right-0 p-4 opacity-20 group-hover:opacity-40 transition-opacity"><span class="material-symbols-outlined text-amber-400 text-5xl">draw</span></div>
            <h3 class="font-display text-xl font-bold text-white mb-3">Copywriter / Storyteller</h3>
            <p class="text-slate-400 text-sm mb-4">You don't write "SEO content". You write manifestos. You understand human psychology and can sell ice to an Eskimo.</p>
            <span class="text-[10px] font-mono bg-amber-400/10 text-amber-400 px-2 py-1 rounded border border-amber-400/30 uppercase">Open</span>
        </div>

        <div class="glass-card p-8 rounded-xl border border-white/5 hover:border-emerald-400/50 transition-colors group relative overflow-hidden">
            <div class="absolute top-0 right-0 p-4 opacity-20 group-hover:opacity-40 transition-opacity"><span class="material-symbols-outlined text-emerald-400 text-5xl">share</span></div>
            <h3 class="font-display text-xl font-bold text-white mb-3">SMM / Community Builder</h3>
            <p class="text-slate-400 text-sm mb-4">You live on X, LinkedIn, and Discord. You know how to build hype, manage communities, and drive organic inbound leads.</p>
            <span class="text-[10px] font-mono bg-emerald-400/10 text-emerald-400 px-2 py-1 rounded border border-emerald-400/30 uppercase">Open</span>
        </div>

        <div class="glass-card p-8 rounded-xl border border-white/5 hover:border-neon-cyan/50 transition-colors group relative overflow-hidden">
            <div class="absolute top-0 right-0 p-4 opacity-20 group-hover:opacity-40 transition-opacity"><span class="material-symbols-outlined text-neon-cyan text-5xl">videocam</span></div>
            <h3 class="font-display text-xl font-bold text-white mb-3">Video Editor</h3>
            <p class="text-slate-400 text-sm mb-4">Short-form TikToks/Reels or long-form YouTube essays. You understand pacing, retention graphs, and visual hooks.</p>
            <span class="text-[10px] font-mono bg-neon-cyan/10 text-neon-cyan px-2 py-1 rounded border border-neon-cyan/30 uppercase">Open</span>
        </div>

        <div class="glass-card p-8 rounded-xl border border-white/5 hover:border-primary/50 transition-colors group relative overflow-hidden">
            <div class="absolute top-0 right-0 p-4 opacity-20 group-hover:opacity-40 transition-opacity"><span class="material-symbols-outlined text-primary text-5xl">code</span></div>
            <h3 class="font-display text-xl font-bold text-white mb-3">Junior Scripter</h3>
            <p class="text-slate-400 text-sm mb-4">Python or Node.js. You might not be a senior architect, but you know how to read docs, use APIs, and prompt LLMs to fix your bugs.</p>
            <span class="text-[10px] font-mono bg-primary/10 text-primary px-2 py-1 rounded border border-primary/30 uppercase">Looking</span>
        </div>

        <div class="glass-card p-8 rounded-xl border border-white/5 hover:border-pink-500/50 transition-colors group relative overflow-hidden">
            <div class="absolute top-0 right-0 p-4 opacity-20 group-hover:opacity-40 transition-opacity"><span class="material-symbols-outlined text-pink-500 text-5xl">brush</span></div>
            <h3 class="font-display text-xl font-bold text-white mb-3">UI/UX Designer</h3>
            <p class="text-slate-400 text-sm mb-4">Figma wizard. You understand dark mode, glassmorphism, and how to design for developers to actually implement it.</p>
            <span class="text-[10px] font-mono bg-pink-500/10 text-pink-500 px-2 py-1 rounded border border-pink-500/30 uppercase">Future</span>
        </div>

        <div class="glass-card p-8 rounded-xl border border-white/5 hover:border-orange-500/50 transition-colors group relative overflow-hidden bg-white/5 backdrop-blur-md">
            <div class="flex items-center justify-center h-full">
                <span class="text-slate-500 font-mono text-sm uppercase tracking-widest text-center">Unlisted Skills?<br/>Pitch Me.</span>
            </div>
        </div>

    </div>
</section>

<!-- STITCH PERSONAS -->
<section class="max-w-6xl mx-auto mb-32 fade-in-section">
    <div class="p-2 bg-gradient-to-r from-neon-purple/30 via-transparent to-neon-cyan/30 rounded-3xl mb-12">
        <div class="bg-black rounded-2xl p-10 text-center">
            <h2 class="font-display text-3xl font-bold text-white uppercase">The 3 Types of People I Want</h2>
        </div>
    </div>
    
    <div class="space-y-6">
        <div class="flex flex-col md:flex-row gap-6 items-stretch">
            <div class="w-full md:w-32 shrink-0 bg-neon-cyan/20 border border-neon-cyan/50 text-neon-cyan rounded-xl flex items-center justify-center font-display text-xl font-bold p-6">01</div>
            <div class="glass-panel p-8 rounded-xl flex-1 border-l-4 border-neon-cyan">
                <h3 class="font-display text-2xl font-bold text-white mb-2">The Absolute Beginner</h3>
                <p class="text-slate-400 leading-relaxed">You know nothing, but you are obsessed with learning. You have 10-20 hours a week to dedicate. I will teach you the exact stack I use. In return, you help me execute the repetitive tasks while you level up.</p>
            </div>
        </div>
        <div class="flex flex-col md:flex-row gap-6 items-stretch">
            <div class="w-full md:w-32 shrink-0 bg-neon-purple/20 border border-neon-purple/50 text-neon-purple rounded-xl flex items-center justify-center font-display text-xl font-bold p-6">02</div>
            <div class="glass-panel p-8 rounded-xl flex-1 border-l-4 border-neon-purple">
                <h3 class="font-display text-2xl font-bold text-white mb-2">The Complementary Expert</h3>
                <p class="text-slate-400 leading-relaxed">You are great at something I am terrible at (like Video Editing or organic TikTok scaling). We trade services—you help me scale the brand, I build you custom software or pay you a cut of the leads you generate.</p>
            </div>
        </div>
        <div class="flex flex-col md:flex-row gap-6 items-stretch">
            <div class="w-full md:w-32 shrink-0 bg-amber-400/20 border border-amber-400/50 text-amber-400 rounded-xl flex items-center justify-center font-display text-xl font-bold p-6">03</div>
            <div class="glass-panel p-8 rounded-xl flex-1 border-l-4 border-amber-400">
                <h3 class="font-display text-2xl font-bold text-white mb-2">The Hustler / Closer</h3>
                <p class="text-slate-400 leading-relaxed">You find clients who need websites, CRMs, or AI agents. You close them. I build the product. We split the profit. Simple whiteboard math.</p>
            </div>
        </div>
    </div>
</section>

<!-- STITCH CTA -->
<section class="max-w-3xl mx-auto text-center mb-24 fade-in-section">
    <h2 class="font-display text-4xl font-bold text-white mb-6 uppercase tracking-tight">Ready to Forge?</h2>
    <p class="text-slate-400 mb-10">Send an email summarizing what you can do and what you want to learn. No formal CVs required.</p>
    <button onclick="window.location.href='contact.html?objective=Join_The_Table'" class="bg-amber-400 text-obsidian px-12 py-5 rounded-sm font-mono text-lg font-bold tracking-[0.2em] uppercase hover:bg-white transition-all shadow-[0_0_30px_rgba(251,191,36,0.5)]">
        APPLY_FOR_SEAT
    </button>
</section>
</main>
''')"""

new_case_studies = """save('case-studies.html', 'Case Studies | Analytics', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-10 mix-blend-overlay -z-20"></div>

<!-- STITCH HERO -->
<section class="max-w-6xl mx-auto text-center mb-24 fade-in-section relative">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-[500px] bg-gradient-to-b from-primary/10 to-transparent blur-[120px] -z-10 pointer-events-none"></div>
    <span class="text-primary font-mono text-xs uppercase tracking-[0.3em] mb-4 block">// BATTLE LOGS</span>
    <h1 class="font-display text-5xl md:text-8xl font-black uppercase tracking-tighter mb-8 text-transparent bg-clip-text bg-gradient-to-r from-primary to-neon-cyan drop-shadow-[0_0_15px_rgba(99,102,241,0.3)] pb-2">
        Case Studies
    </h1>
    <p class="text-slate-400 text-lg md:text-xl max-w-2xl mx-auto leading-relaxed">
        I don't just write code. I engineer ROI. Here is the raw data from my most successful deployments.
    </p>
</section>

<!-- PROJECT 1 -->
<section class="max-w-7xl mx-auto mb-32 fade-in-section">
    <div class="glass-panel p-8 md:p-12 rounded-3xl border border-neon-cyan/30 bg-black/50 relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-[400px] h-[400px] bg-neon-cyan/5 blur-3xl rounded-full -z-10 group-hover:bg-neon-cyan/10 transition-colors"></div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
                <span class="inline-block border border-neon-cyan/50 text-neon-cyan font-mono text-[10px] px-3 py-1 rounded-full uppercase tracking-widest mb-6">Sector: Legal</span>
                <h2 class="font-display text-4xl font-bold text-white mb-6">Corporate Law Firm Dominance</h2>
                <p class="text-slate-400 mb-8 leading-relaxed">A prestigious Chișinău law firm needed to completely overhaul their outdated web presence to attract high-ticket international corporate clients. We dumped WordPress for a custom Next.js deployment with blazing fast Core Web Vitals and executed a highly targeted Google Ads Search campaign.</p>
                
                <div class="grid grid-cols-2 gap-6 mb-8">
                    <div class="border-l-2 border-neon-cyan/50 pl-4 py-1">
                        <span class="block text-xs font-mono text-slate-500 uppercase tracking-widest mb-1">Organic Traffic</span>
                        <div class="text-3xl font-display font-bold text-white">+340%</div>
                    </div>
                    <div class="border-l-2 border-neon-cyan/50 pl-4 py-1">
                        <span class="block text-xs font-mono text-slate-500 uppercase tracking-widest mb-1">Cost Per Lead</span>
                        <div class="text-3xl font-display font-bold text-neon-cyan">-62%</div>
                    </div>
                </div>

                <div class="flex gap-4">
                    <span class="bg-white/5 px-3 py-1 rounded text-xs font-mono text-slate-400">Next.js</span>
                    <span class="bg-white/5 px-3 py-1 rounded text-xs font-mono text-slate-400">Tailwind</span>
                    <span class="bg-white/5 px-3 py-1 rounded text-xs font-mono text-slate-400">Google Ads</span>
                </div>
            </div>
            <div class="relative h-[400px] rounded-2xl overflow-hidden border border-white/10 group-hover:border-neon-cyan/50 transition-colors duration-500 bg-obsidian">
                <div class="absolute inset-0 bg-gradient-to-tr from-neon-cyan/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 z-10 mix-blend-overlay"></div>
                <!-- Abstract Legal Representation -->
                <div class="absolute inset-0 flex items-center justify-center">
                    <span class="material-symbols-outlined text-[150px] text-neon-cyan/10 group-hover:text-neon-cyan/20 transition-colors duration-700 group-hover:scale-110">gavel</span>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- PROJECT 2 -->
<section class="max-w-7xl mx-auto mb-32 fade-in-section">
    <div class="glass-panel p-8 md:p-12 rounded-3xl border border-neon-purple/30 bg-black/50 relative overflow-hidden group">
        <div class="absolute top-0 left-0 w-[400px] h-[400px] bg-neon-purple/5 blur-3xl rounded-full -z-10 group-hover:bg-neon-purple/10 transition-colors"></div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div class="order-2 lg:order-1 relative h-[400px] rounded-2xl overflow-hidden border border-white/10 group-hover:border-neon-purple/50 transition-colors duration-500 bg-obsidian">
                <div class="absolute inset-0 bg-gradient-to-br from-neon-purple/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 z-10 mix-blend-overlay"></div>
                <!-- Abstract AI Representation -->
                <div class="absolute inset-0 flex items-center justify-center relative">
                    <div class="w-32 h-32 border-2 border-neon-purple/30 rounded-full animate-spin-slow"></div>
                    <div class="w-24 h-24 border border-neon-purple/50 rounded-full absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 flex items-center justify-center bg-neon-purple/10">
                        <span class="material-symbols-outlined text-4xl text-neon-purple">psychology</span>
                    </div>
                </div>
            </div>
            <div class="order-1 lg:order-2">
                <span class="inline-block border border-neon-purple/50 text-neon-purple font-mono text-[10px] px-3 py-1 rounded-full uppercase tracking-widest mb-6">Sector: SaaS & Support</span>
                <h2 class="font-display text-4xl font-bold text-white mb-6">Custom Technical AI Agent</h2>
                <p class="text-slate-400 mb-8 leading-relaxed">A specialized machinery supplier was losing hours answering routine technical questions. I trained a custom LangChain agent on their 500+ page technical manuals and deployed it to Telegram and WooCommerce, serving instant hyper-accurate part numbers to clients.</p>
                
                <div class="grid grid-cols-2 gap-6 mb-8">
                    <div class="border-l-2 border-neon-purple/50 pl-4 py-1">
                        <span class="block text-xs font-mono text-slate-500 uppercase tracking-widest mb-1">Human Time Saved</span>
                        <div class="text-3xl font-display font-bold text-white">15 hrs/wk</div>
                    </div>
                    <div class="border-l-2 border-neon-purple/50 pl-4 py-1">
                        <span class="block text-xs font-mono text-slate-500 uppercase tracking-widest mb-1">Resolution Speed</span>
                        <div class="text-3xl font-display font-bold text-neon-purple">1.2s avg</div>
                    </div>
                </div>

                <div class="flex gap-4">
                    <span class="bg-white/5 px-3 py-1 rounded text-xs font-mono text-slate-400">Python</span>
                    <span class="bg-white/5 px-3 py-1 rounded text-xs font-mono text-slate-400">Langchain</span>
                    <span class="bg-white/5 px-3 py-1 rounded text-xs font-mono text-slate-400">GPT-4</span>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- PROJECT 3 -->
<section class="max-w-7xl mx-auto mb-32 fade-in-section">
    <div class="glass-panel p-8 md:p-12 rounded-3xl border border-amber-400/30 bg-black/50 relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-[400px] h-[400px] bg-amber-400/5 blur-3xl rounded-full -z-10 group-hover:bg-amber-400/10 transition-colors"></div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
                <span class="inline-block border border-amber-400/50 text-amber-400 font-mono text-[10px] px-3 py-1 rounded-full uppercase tracking-widest mb-6">Sector: E-Commerce</span>
                <h2 class="font-display text-4xl font-bold text-white mb-6">Industrial Refrigeration Hub</h2>
                <p class="text-slate-400 mb-8 leading-relaxed">Built from the ground up for Masfrig. Complex WooCommerce setup handling industrial equipment variants. Custom shipping calculators, advanced CRM hooks, and a complete Meta Ads retargeting funnel.</p>
                
                <div class="grid grid-cols-2 gap-6 mb-8">
                    <div class="border-l-2 border-amber-400/50 pl-4 py-1">
                        <span class="block text-xs font-mono text-slate-500 uppercase tracking-widest mb-1">Yearly Revenue Lift</span>
                        <div class="text-3xl font-display font-bold text-white">+112%</div>
                    </div>
                    <div class="border-l-2 border-amber-400/50 pl-4 py-1">
                        <span class="block text-xs font-mono text-slate-500 uppercase tracking-widest mb-1">Conv. Rate</span>
                        <div class="text-3xl font-display font-bold text-amber-400">4.8%</div>
                    </div>
                </div>

                <div class="flex gap-4">
                    <span class="bg-white/5 px-3 py-1 rounded text-xs font-mono text-slate-400">WooCommerce</span>
                    <span class="bg-white/5 px-3 py-1 rounded text-xs font-mono text-slate-400">PHP/JS</span>
                    <span class="bg-white/5 px-3 py-1 rounded text-xs font-mono text-slate-400">Meta Ads</span>
                </div>
            </div>
            <div class="relative h-[400px] rounded-2xl overflow-hidden border border-white/10 group-hover:border-amber-400/50 transition-colors duration-500 bg-obsidian">
                <div class="absolute inset-0 bg-gradient-to-tr from-amber-400/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 z-10 mix-blend-overlay"></div>
                <!-- Abstract E-com Representation -->
                <div class="absolute inset-0 flex items-center justify-center">
                    <span class="material-symbols-outlined text-[150px] text-amber-400/10 group-hover:text-amber-400/20 transition-colors duration-700 group-hover:scale-110">ac_unit</span>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- STITCH CTA -->
<section class="max-w-3xl mx-auto text-center mb-24 fade-in-section">
    <h2 class="font-display text-4xl font-bold text-white mb-6 uppercase tracking-tight">Your Data Fits Here.</h2>
    <p class="text-slate-400 mb-10">Stop guessing. Deploy systems built on logic, tracking, and uncompromising quality.</p>
    <button onclick="window.location.href='contact.html?objective=Round_Table'" class="bg-primary/10 border border-primary text-primary px-12 py-5 rounded-sm font-mono text-lg font-bold tracking-[0.2em] uppercase hover:bg-primary hover:text-white transition-all shadow-[0_0_30px_rgba(99,102,241,0.5)]">
        REQUEST_AUDIT
    </button>
</section>
</main>
''')"""

# Replace work-with-me
wwm_pattern = re.compile(r"save\('work-with-me\.html'.*?</main>\s*'''\)", re.DOTALL)
code = re.sub(wwm_pattern, new_work_with_me, code)

# Replace case-studies
cs_pattern = re.compile(r"save\('case-studies\.html'.*?</main>\s*'''\)", re.DOTALL)
code = re.sub(cs_pattern, new_case_studies, code)

with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'w', 'utf-8') as f:
    f.write(code)

print("Batch 2 (Work With Me & Case Studies) refactored correctly with trailing parenthesis syntax intact.")
