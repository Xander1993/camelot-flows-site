import codecs
import re

with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'r', 'utf-8') as f:
    code = f.read()

new_arsenal = """save('arsenal.html', 'The Arsenal | Core Offerings', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-20 mix-blend-overlay -z-20"></div>

<!-- STITCH HERO -->
<section class="max-w-6xl mx-auto text-center mb-24 fade-in-section relative">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[400px] bg-emerald-500/10 blur-[150px] rounded-full -z-10 pointer-events-none fade-in-section"></div>
    <span class="text-emerald-400 font-mono text-xs uppercase tracking-[0.3em] mb-4 block">// STRATEGIC ASSETS</span>
    <h1 class="font-display text-5xl md:text-8xl font-black uppercase tracking-tighter mb-8 text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-600 pb-2 drop-shadow-[0_0_20px_rgba(16,185,129,0.4)]">
        The Arsenal
    </h1>
    <p class="text-slate-400 text-lg md:text-xl max-w-3xl mx-auto leading-relaxed border-l-2 border-emerald-400/50 pl-6 text-left">
        These are not templates. These are functional weapons designed to automate your workflow, convert your traffic, and dominate your niche.
    </p>
</section>

<!-- STITCH WEAPONS GALLERY -->
<section class="max-w-7xl mx-auto mb-32 relative">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- EXCALIBUR -->
        <div class="glass-card p-0 rounded-2xl border-t-2 border-amber-400 bg-obsidian overflow-hidden group fade-in-section relative shadow-[0_0_30px_rgba(251,191,36,0.1)] hover:shadow-[0_0_50px_rgba(251,191,36,0.3)] transition-all">
            <div class="h-48 bg-gradient-to-tr from-amber-400/20 to-orange-600/20 relative flex items-center justify-center overflow-hidden border-b border-white/5">
                <div class="absolute inset-0 bg-black/40 backdrop-blur-sm z-10 group-hover:bg-transparent transition-colors duration-500"></div>
                <span class="material-symbols-outlined text-8xl text-amber-500/50 group-hover:text-amber-400 group-hover:scale-110 transition-all z-20 drop-shadow-[0_0_15px_rgba(251,191,36,0.8)]">swords</span>
            </div>
            <div class="p-8 relative">
                <div class="absolute top-0 right-8 -translate-y-1/2 bg-amber-400 text-obsidian text-xs font-mono font-bold px-3 py-1 rounded shadow-lg uppercase">Flagship</div>
                <h3 class="font-display text-2xl font-bold text-white mb-2 uppercase">Excalibur Templates</h3>
                <p class="text-slate-400 text-sm leading-relaxed mb-6">Fully coded React/Next.js and Astro templates tailored for high-ticket service businesses. Skip 300 hours of design labor.</p>
                <ul class="space-y-3 mb-8 text-xs text-slate-300 font-mono">
                    <li class="flex items-center gap-2"><span class="text-amber-400">&gt;</span> Built-in GSAP Scripts</li>
                    <li class="flex items-center gap-2"><span class="text-amber-400">&gt;</span> 100/100 Lighthouse</li>
                    <li class="flex items-center gap-2"><span class="text-amber-400">&gt;</span> MDX Blog Architecture</li>
                </ul>
                <button onclick="window.location.href='contact.html?objective=Excalibur'" class="w-full py-3 bg-amber-400/10 border border-amber-400/50 text-amber-400 font-mono text-sm tracking-widest uppercase hover:bg-amber-400 hover:text-obsidian transition-colors rounded">Inspect Weapon</button>
            </div>
        </div>

        <!-- MERLIN -->
        <div class="glass-card p-0 rounded-2xl border-t-2 border-neon-purple bg-obsidian overflow-hidden group fade-in-section delay-100 relative shadow-[0_0_30px_rgba(191,0,255,0.1)] hover:shadow-[0_0_50px_rgba(191,0,255,0.3)] transition-all">
            <div class="h-48 bg-gradient-to-tr from-neon-purple/20 to-pink-600/20 relative flex items-center justify-center overflow-hidden border-b border-white/5">
                <div class="absolute inset-0 bg-black/40 backdrop-blur-sm z-10 group-hover:bg-transparent transition-colors duration-500"></div>
                <span class="material-symbols-outlined text-8xl text-neon-purple/50 group-hover:text-neon-purple group-hover:scale-110 transition-all z-20 drop-shadow-[0_0_15px_rgba(191,0,255,0.8)]">psychology_alt</span>
            </div>
            <div class="p-8 relative">
                <h3 class="font-display text-2xl font-bold text-white mb-2 uppercase">Merlin Auto-Agents</h3>
                <p class="text-slate-400 text-sm leading-relaxed mb-6">Pre-trained LLM models wrapped in custom Python logic. These agents interface with your CRM, email, and Slack to handle frontline work.</p>
                <ul class="space-y-3 mb-8 text-xs text-slate-300 font-mono">
                    <li class="flex items-center gap-2"><span class="text-neon-purple">&gt;</span> Lead Qualification Bot</li>
                    <li class="flex items-center gap-2"><span class="text-neon-purple">&gt;</span> Notion Synced RAG</li>
                    <li class="flex items-center gap-2"><span class="text-neon-purple">&gt;</span> Automated Proposal Gen</li>
                </ul>
                <button onclick="window.location.href='contact.html?objective=Merlin'" class="w-full py-3 bg-neon-purple/10 border border-neon-purple/50 text-neon-purple font-mono text-sm tracking-widest uppercase hover:bg-neon-purple hover:text-obsidian transition-colors rounded">Inspect Weapon</button>
            </div>
        </div>

        <!-- ROUND TABLE -->
        <div class="glass-card p-0 rounded-2xl border-t-2 border-neon-cyan bg-obsidian overflow-hidden group fade-in-section delay-200 relative shadow-[0_0_30px_rgba(0,242,255,0.1)] hover:shadow-[0_0_50px_rgba(0,242,255,0.3)] transition-all">
            <div class="h-48 bg-gradient-to-tr from-neon-cyan/20 to-blue-600/20 relative flex items-center justify-center overflow-hidden border-b border-white/5">
                <div class="absolute inset-0 bg-black/40 backdrop-blur-sm z-10 group-hover:bg-transparent transition-colors duration-500"></div>
                <span class="material-symbols-outlined text-8xl text-neon-cyan/50 group-hover:text-neon-cyan group-hover:scale-110 transition-all z-20 drop-shadow-[0_0_15px_rgba(0,242,255,0.8)]">hub</span>
            </div>
            <div class="p-8 relative">
                <h3 class="font-display text-2xl font-bold text-white mb-2 uppercase">Round Table Infra</h3>
                <p class="text-slate-400 text-sm leading-relaxed mb-6">The definitive Docker-based deployment template for VPS ecosystems. Stop renting Heroku or Vercel; host 100 projects on a $20 server.</p>
                <ul class="space-y-3 mb-8 text-xs text-slate-300 font-mono">
                    <li class="flex items-center gap-2"><span class="text-neon-cyan">&gt;</span> Traefik Reverse Proxy</li>
                    <li class="flex items-center gap-2"><span class="text-neon-cyan">&gt;</span> Portainer Setup Dash</li>
                    <li class="flex items-center gap-2"><span class="text-neon-cyan">&gt;</span> Hardened UFW Logic</li>
                </ul>
                <button onclick="window.location.href='contact.html?objective=Round_Table'" class="w-full py-3 bg-neon-cyan/10 border border-neon-cyan/50 text-neon-cyan font-mono text-sm tracking-widest uppercase hover:bg-neon-cyan hover:text-obsidian transition-colors rounded">Inspect Weapon</button>
            </div>
        </div>

    </div>
</section>
</main>
''')"""

new_merlin = """save('merlin.html', 'Merlin AI Protocol', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>

<!-- MATRIX BACKGROUND EFFECT -->
<div class="absolute inset-0 overflow-hidden pointer-events-none -z-10 opacity-20">
    <div class="w-full h-full text-neon-purple/30 font-mono text-[8px] leading-tight select-none rotate-180" style="writing-mode: vertical-rl;">
        01001101 01000101 01010010 01001100 01001001 01001110 00100000 01000001 01001001 00100000 01010011 01011001 01010011 01010100 01000101 01001101 01010011
        01001101 01000101 01010010 01001100 01001001 01001110 00100000 01000001 01001001 00100000 01010011 01011001 01010011 01010100 01000101 01001101 01010011
    </div>
</div>

<!-- STITCH HERO -->
<section class="max-w-6xl mx-auto text-center mb-20 fade-in-section relative">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-neon-purple/15 blur-[150px] rounded-full -z-10 pointer-events-none fade-in-section"></div>
    <span class="text-neon-purple font-mono text-xs uppercase tracking-[0.3em] mb-4 block animate-glow">// ADVANCED INTELLIGENCE CONSTRUCT</span>
    <h1 class="font-display text-5xl md:text-8xl font-black uppercase tracking-tighter mb-8 text-transparent bg-clip-text bg-gradient-to-b from-white via-neon-purple to-pink-600 pb-2 drop-shadow-[0_0_30px_rgba(191,0,255,0.5)]">
        The Merlin<br/>Protocol
    </h1>
    <p class="text-slate-300 text-lg max-w-2xl mx-auto leading-relaxed font-mono">
        > SYSTEM BOOT: Successful.<br/>
        > NEURAL LINK: Established.<br/>
        Not a ChatGPT wrapper. A fully embedded, locally aware agentic architecture driving your business brain.
    </p>
</section>

<!-- STITCH INFRASTRUCTURE -->
<section class="max-w-7xl mx-auto mb-32 fade-in-section">
    <div class="glass-panel p-2 rounded-3xl border border-neon-purple/30 bg-black/60 relative overflow-hidden">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-0 border border-white/5 rounded-2xl overflow-hidden">
            
            <div class="lg:col-span-4 bg-obsidian border-r border-white/5 p-8 relative">
                <h3 class="font-mono text-xs text-neon-purple uppercase tracking-widest mb-6">Component Architecture</h3>
                <div class="space-y-4 font-mono text-sm text-slate-400">
                    <div class="flex justify-between items-center bg-white/5 p-3 rounded border border-white/5 hover:border-neon-purple/50 transition-colors cursor-default group">
                        <span class="text-white group-hover:text-neon-purple">Ingestion Module</span>
                        <span class="material-symbols-outlined text-xs">database</span>
                    </div>
                    <div class="flex justify-between items-center bg-white/5 p-3 rounded border border-white/5 hover:border-neon-purple/50 transition-colors cursor-default group">
                        <span class="text-white group-hover:text-neon-purple">Vector Store (Chroma)</span>
                        <span class="material-symbols-outlined text-xs">grid_view</span>
                    </div>
                    <div class="flex justify-between items-center bg-neon-purple/20 p-3 rounded border border-neon-purple group shadow-[0_0_15px_rgba(191,0,255,0.2)] inset-shadow">
                        <span class="text-neon-purple font-bold">Reasoning Core (Llama 3)</span>
                        <span class="material-symbols-outlined text-xs text-neon-purple animate-pulse">memory</span>
                    </div>
                    <div class="flex justify-between items-center bg-white/5 p-3 rounded border border-white/5 hover:border-neon-purple/50 transition-colors cursor-default group">
                        <span class="text-white group-hover:text-neon-purple">Action Hooks (Zapier/Make)</span>
                        <span class="material-symbols-outlined text-xs">webhook</span>
                    </div>
                </div>
            </div>

            <div class="lg:col-span-8 p-12 relative overflow-hidden bg-gradient-to-br from-black to-neon-purple/10">
                <div class="absolute top-0 right-0 p-4 opacity-5"><span class="material-symbols-outlined text-[200px] text-neon-purple">code_blocks</span></div>
                <h2 class="font-display text-3xl font-bold text-white mb-6 leading-tight relative z-10">How Merlin Processes Your Data</h2>
                <div class="prose prose-invert prose-p:text-slate-400 prose-p:leading-relaxed max-w-none relative z-10">
                    <p>Unlike off-the-shelf bots that hallucinate answers, the Merlin Protocol uses a precise <strong>Retrieval-Augmented Generation (RAG)</strong> loop.</p>
                    <p>It connects securely to your internal SOPs, product catalogs, and historical ticket data. When a query hits the system, Merlin isolates the exact vector chunk relevant to the context, feeds it to the reasoning core, and outputs a mathematically deterministic response.</p>
                    <p>If the user requests an action—like booking a meeting or generating a PDF—Merlin triggers external webhook scripts via Python.</p>
                </div>
                <div class="mt-8 pt-8 border-t border-white/10 flex items-center justify-between relative z-10">
                    <div class="flex items-center gap-3">
                        <div class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></div>
                        <span class="font-mono text-xs text-emerald-400 uppercase tracking-widest">SYSTEM ONLINE</span>
                    </div>
                    <button onclick="window.location.href='contact.html?objective=Merlin'" class="bg-neon-purple text-obsidian px-6 py-2 rounded-sm font-mono text-xs font-bold uppercase hover:bg-white transition-colors">Deploy Instance</button>
                </div>
            </div>

        </div>
    </div>
</section>
</main>
''')"""

new_contact = """save('contact.html', 'Contact Command', '''
<main class="relative pt-32 pb-20 px-6 min-h-screen flex items-center justify-center">
<div class="absolute inset-0 bg-[#0a0a0f] -z-20"></div>
<div class="absolute inset-0 grid-bg opacity-30 -z-20"></div>

<section class="w-full max-w-4xl mx-auto z-10 fade-in-section">
    <div class="grid grid-cols-1 md:grid-cols-2 bg-black/60 rounded-3xl border border-neon-cyan/30 overflow-hidden shadow-[0_0_50px_rgba(0,242,255,0.1)]">
        
        <!-- SIDE PANEL -->
        <div class="p-12 md:p-16 bg-gradient-to-br from-obsidian to-neon-cyan/10 border-r border-white/5 relative">
            <span class="text-neon-cyan font-mono text-[10px] uppercase tracking-[0.3em] mb-4 block">// TRANSMISSION SECURE</span>
            <h1 class="font-display text-4xl font-black text-white uppercase tracking-tighter mb-4">Command<br/>Center</h1>
            <p class="text-slate-400 text-sm leading-relaxed mb-12">
                All transmissions are encrypted. Select your objective, input your data, and await terminal response.
            </p>
            
            <div class="space-y-6 font-mono text-xs text-slate-500">
                <div class="flex items-center gap-4">
                    <span class="material-symbols-outlined text-neon-cyan">mail</span>
                    <a href="mailto:alex@camelotflows.dev" class="hover:text-neon-cyan transition-colors">alex@camelotflows.dev</a>
                </div>
                <div class="flex items-center gap-4">
                    <span class="material-symbols-outlined text-emerald-400">location_on</span>
                    <span>Chișinău, Moldova [GMT+2]</span>
                </div>
                <div class="flex items-center gap-4">
                    <span class="material-symbols-outlined text-amber-400">schedule</span>
                    <span>Systems Online 24/7</span>
                </div>
            </div>
            <div class="absolute bottom-0 right-0 opacity-10 blur-xl pointer-events-none">
                <div class="w-48 h-48 bg-neon-cyan/50 rounded-full"></div>
            </div>
        </div>

        <!-- FORM PANEL (Stitch Pixel-Perfect Form 7 structure) -->
        <div class="p-10 md:p-14 relative bg-obsidian/80 backdrop-blur-xl">
            <h3 class="font-mono text-sm text-white mb-8 border-b border-white/10 pb-4">INITIALIZE_CONNECTION</h3>
            
            <form action="#" method="post" class="space-y-6">
                <!-- Name -->
                <div class="relative">
                    <label class="block font-mono text-[10px] text-neon-cyan uppercase tracking-widest mb-2">Subject Name <span class="text-red-500">*</span></label>
                    <input type="text" placeholder="Enter Designation" class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-sm text-white focus:outline-none focus:border-neon-cyan focus:ring-1 focus:ring-neon-cyan/50 transition-all font-mono" required />
                </div>
                
                <!-- Email -->
                <div class="relative">
                    <label class="block font-mono text-[10px] text-neon-cyan uppercase tracking-widest mb-2">Comms Channel (Email) <span class="text-red-500">*</span></label>
                    <input type="email" placeholder="user@domain.com" class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-sm text-white focus:outline-none focus:border-neon-cyan focus:ring-1 focus:ring-neon-cyan/50 transition-all font-mono" required />
                </div>

                <!-- Objective -->
                <div class="relative">
                    <label class="block font-mono text-[10px] text-neon-cyan uppercase tracking-widest mb-2">Primary Objective <span class="text-red-500">*</span></label>
                    <div class="relative">
                        <select class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-sm text-white focus:outline-none focus:border-neon-cyan focus:ring-1 focus:ring-neon-cyan/50 transition-all font-mono appearance-none" required>
                            <option value="Merlin">Deploy Merlin AI Agent</option>
                            <option value="Round Table">Full Round Table Build</option>
                            <option value="Excalibur">Excalibur Architecture</option>
                            <option value="Agency">Agency Partnership</option>
                            <option value="Other">Other Query</option>
                        </select>
                        <span class="absolute right-4 top-1/2 -translate-y-1/2 material-symbols-outlined text-slate-500 pointer-events-none">expand_content</span>
                    </div>
                </div>

                <!-- Message -->
                <div class="relative">
                    <label class="block font-mono text-[10px] text-neon-cyan uppercase tracking-widest mb-2">Data Payload <span class="text-red-500">*</span></label>
                    <textarea rows="4" placeholder="Detail your parameters..." class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-sm text-white focus:outline-none focus:border-neon-cyan focus:ring-1 focus:ring-neon-cyan/50 transition-all font-mono resize-none" required></textarea>
                </div>

                <!-- Submit -->
                <button type="submit" class="w-full py-4 mt-4 bg-neon-cyan/10 border border-neon-cyan text-neon-cyan font-mono text-sm font-bold tracking-[0.2em] uppercase hover:bg-neon-cyan hover:text-obsidian transition-colors rounded shadow-[0_0_20px_rgba(0,242,255,0.3)] inset-shadow">
                    TRANSMIT_PAYLOAD
                </button>
            </form>
        </div>

    </div>
</section>
</main>
''')"""

# Replace
arsenal_pattern = re.compile(r"save\('arsenal\.html'.*?</main>\s*'''\)", re.DOTALL)
code = re.sub(arsenal_pattern, new_arsenal, code)

merlin_pattern = re.compile(r"save\('merlin\.html'.*?</main>\s*'''\)", re.DOTALL)
code = re.sub(merlin_pattern, new_merlin, code)

contact_pattern = re.compile(r"save\('contact\.html'.*?</main>\s*'''\)", re.DOTALL)
code = re.sub(contact_pattern, new_contact, code)

with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'w', 'utf-8') as f:
    f.write(code)

print("Batch 3 (Arsenal, Merlin, Contact) refactored with missing paren fixes intact.")
