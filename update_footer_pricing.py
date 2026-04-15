import json
import re

footer_html = """<footer class="bg-obsidian pt-24 pb-12 px-6 border-t border-primary/20 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-1/2 h-[1px] bg-gradient-to-r from-transparent via-primary/50 to-transparent shadow-[0_0_15px_rgba(99,102,241,0.5)]"></div>
<div class="max-w-7xl mx-auto">
<div class="grid grid-cols-1 md:grid-cols-12 gap-8 md:gap-12 mb-20">
<div class="md:col-span-3">
<div class="flex items-center gap-3 mb-6">
<div class="w-8 h-8 rounded bg-primary flex items-center justify-center">
<span class="material-symbols-outlined text-white text-lg">architecture</span>
</div>
<span class="font-display text-xl font-bold tracking-tighter uppercase text-white">Camelot Flows</span>
</div>
<p class="text-slate-500 mb-8 text-sm leading-relaxed font-mono">
<span class="text-primary">&gt;</span> Location: Chisinau, MD<br/>
<span class="text-primary">&gt;</span> Coordinates: 47.0105° N, 28.8638° E<br/>
<span class="text-primary">&gt;</span> Mission: Awwwards-Tier Design & AI Automation.
</p>
<div class="flex gap-4">
<a class="w-10 h-10 border border-white/10 rounded flex items-center justify-center hover:bg-white/5 hover:border-primary/50 hover:text-primary transition-all text-slate-400" href="contact.html">
<span class="material-symbols-outlined text-lg">mail</span>
</a>
<a class="w-10 h-10 border border-white/10 rounded flex items-center justify-center hover:bg-white/5 hover:border-primary/50 hover:text-primary transition-all text-slate-400" href="contact.html">
<span class="material-symbols-outlined text-lg">alternate_email</span>
</a>
</div>
</div>
<div class="md:col-span-2">
<h5 class="font-mono font-bold mb-6 text-xs text-white uppercase tracking-widest border-b border-white/10 pb-2 w-max">Protocol</h5>
<ul class="space-y-3 text-slate-500 text-sm font-mono">
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="arsenal.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> The Arsenal</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="merlin.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Merlin</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="case-studies.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Case Studies</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="for-agencies.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Agencies</a></li>
</ul>
</div>
<div class="md:col-span-2">
<h5 class="font-mono font-bold mb-6 text-xs text-white uppercase tracking-widest border-b border-white/10 pb-2 w-max">Services</h5>
<ul class="space-y-3 text-slate-500 text-sm font-mono">
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="service-creation.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Site Creation</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="service-maintenance.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Maintenance</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="service-automation.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Automations</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="service-marketing.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Marketing</a></li>
</ul>
</div>
<div class="md:col-span-2">
<h5 class="font-mono font-bold mb-6 text-xs text-white uppercase tracking-widest border-b border-white/10 pb-2 w-max">Company</h5>
<ul class="space-y-3 text-slate-500 text-sm font-mono">
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="about.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> About</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="work-with-me.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Work With</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="legal.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Legal</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="contact.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Contact</a></li>
</ul>
</div>
<div class="md:col-span-3">
<h5 class="font-mono font-bold mb-6 text-xs text-white uppercase tracking-widest border-b border-white/10 pb-2 w-max">Vanguard</h5>
<p class="text-slate-500 text-sm mb-6 leading-relaxed">Weekly insights on AI automation sent directly to your terminal.</p>
<div class="flex gap-2 p-1 bg-white/5 rounded border border-white/10 focus-within:border-primary/50 transition-colors">
<input class="bg-transparent border-none focus:ring-0 text-sm flex-1 px-4 text-white font-mono placeholder:text-slate-600" placeholder="ENTER_EMAIL" type="email"/>
<button class="bg-primary hover:bg-primary/90 text-white px-4 py-2 rounded text-xs font-bold transition-colors font-mono">[SUBMIT]</button>
</div>
</div>
</div>
<div class="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6">
<p class="text-xs text-slate-600 font-mono">&copy; 2026 Camelot Flows. Built by Alex Buzi.</p>
<div class="flex flex-wrap justify-center gap-4 md:gap-8">
<div class="flex items-center gap-2 text-xs text-slate-500 font-mono">
<span class="material-symbols-outlined text-sm text-green-500">wifi</span>
<span>System Status: Optimal</span>
</div>
<div class="flex items-center gap-2 text-xs text-slate-500 font-mono">
<span class="material-symbols-outlined text-sm text-blue-500">bolt</span>
<span>Lightning Fast Performance</span>
</div>
</div>
</div>
</div>
</footer>"""

header_nav_html = """            <nav class="hidden md:flex items-center gap-8 font-mono text-sm uppercase tracking-widest">
                <a href="arsenal.html" class="text-white hover:text-primary transition-colors relative group">
                    <span class="absolute -left-3 opacity-0 group-hover:opacity-100 group-hover:-translate-x-1 transition-all text-primary">&gt;</span>
                    [Arsenal]
                </a>
                <a href="merlin.html" class="text-white hover:text-primary transition-colors relative group">
                    <span class="absolute -left-3 opacity-0 group-hover:opacity-100 group-hover:-translate-x-1 transition-all text-primary">&gt;</span>
                    [Merlin]
                </a>
                <a href="about.html" class="text-white hover:text-primary transition-colors relative group">
                    <span class="absolute -left-3 opacity-0 group-hover:opacity-100 group-hover:-translate-x-1 transition-all text-primary">&gt;</span>
                    [About]
                </a>
                <a href="for-agencies.html" class="text-white hover:text-primary transition-colors relative group">
                    <span class="absolute -left-3 opacity-0 group-hover:opacity-100 group-hover:-translate-x-1 transition-all text-primary">&gt;</span>
                    [Agencies]
                </a>
                <a href="contact.html" class="text-white hover:text-neon-cyan transition-colors relative group" style="text-shadow: 0 0 10px rgba(0,242,255,0.5)">
                    <span class="absolute -left-3 opacity-0 group-hover:opacity-100 group-hover:-translate-x-1 transition-all text-neon-cyan">&gt;</span>
                    [Contact]
                </a>
            </nav>"""

# Update _shell_parts.json
with open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/_shell_parts.json', 'r', encoding='utf-8') as f:
    parts = json.load(f)

parts['new_footer'] = footer_html

# Update body_shell inside _shell_parts.json to use the exact correct header nav
body_shell = parts['body_shell']
body_shell = re.sub(r'<nav class="hidden md:flex.*?</nav>', header_nav_html, body_shell, flags=re.DOTALL)
parts['body_shell'] = body_shell

with open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/_shell_parts.json', 'w', encoding='utf-8') as f:
    json.dump(parts, f, indent=4)

# Update code_v2.html
with open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/code_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Footer
html = re.sub(r'<footer.*?</footer>', footer_html, html, flags=re.DOTALL)

# Replace Header Nav
html = re.sub(r'<nav class="hidden md:flex.*?</nav>', header_nav_html, html, flags=re.DOTALL)

# Update Mobile Menu in code_v2.html
mobile_menu = """            <div class="px-6 py-8 space-y-6 font-mono text-lg uppercase tracking-widest text-center">
                <a href="arsenal.html" class="block text-white hover:text-primary transition-colors py-2 border-b border-white/5">The Arsenal</a>
                <a href="merlin.html" class="block text-white hover:text-primary transition-colors py-2 border-b border-white/5">Merlin Protocol</a>
                <a href="about.html" class="block text-white hover:text-primary transition-colors py-2 border-b border-white/5">About</a>
                <a href="for-agencies.html" class="block text-white hover:text-primary transition-colors py-2 border-b border-white/5">For Agencies</a>
                <a href="contact.html" class="block text-neon-cyan py-2 border-b border-neon-cyan/20">Contact</a>
            </div>"""
html = re.sub(r'<div class="px-6 py-8 space-y-6 font-mono.*?</div>', mobile_menu, html, flags=re.DOTALL)

# Pricing updates
html = html.replace('$2,400</div>', '$150</div>')
html = html.replace('<button class="bg-neon-cyan/10 border border-neon-cyan/50 text-neon-cyan w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-cyan hover:text-obsidian transition-all duration-300 text-center">Initiate Core</button>', '<button onclick="window.location.href=\'contact.html?objective=merlin\'" class="bg-neon-cyan/10 border border-neon-cyan/50 text-neon-cyan w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-cyan hover:text-obsidian transition-all duration-300 text-center cursor-pointer">Initiate Core</button>')

html = html.replace('$3,800</div>', '$450</div>')
html = html.replace('<button class="bg-neon-purple text-obsidian w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-white hover:text-black transition-colors text-center shadow-[0_0_20px_rgba(191,0,255,0.4)]">Establish Uplink</button>', '<button onclick="window.location.href=\'contact.html?objective=percival\'" class="bg-neon-purple text-obsidian w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-white hover:text-black transition-colors text-center shadow-[0_0_20px_rgba(191,0,255,0.4)] cursor-pointer">Establish Uplink</button>')

html = html.replace('$8,500<span class="text-3xl">+</span></div>', '$900<span class="text-3xl">+</span></div>')
html = html.replace('<button class="bg-neon-blue/10 border border-neon-blue/50 text-neon-blue w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-blue hover:text-white transition-all duration-300 text-center">Summon Env</button>', '<button onclick="window.location.href=\'contact.html?objective=excalibur\'" class="bg-neon-blue/10 border border-neon-blue/50 text-neon-blue w-full py-4 rounded-xl text-sm font-black font-mono tracking-widest uppercase hover:bg-neon-blue hover:text-white transition-all duration-300 text-center cursor-pointer">Summon Env</button>')

# Mid section button replacement
html = html.replace('<button class="bg-indigo-600/20 hover:bg-indigo-600/40 border border-indigo-500/50 hover:border-indigo-400 text-indigo-100 px-5 py-2 rounded text-xs font-mono font-bold transition-all shadow-neon hover:shadow-neon-strong">\\n                // SUMMON_AGENT\\n            </button>', '<button onclick="window.location.href=\'contact.html\'" class="bg-indigo-600/20 hover:bg-indigo-600/40 border border-indigo-500/50 hover:border-indigo-400 text-indigo-100 px-5 py-2 rounded text-xs font-mono font-bold transition-all shadow-neon hover:shadow-neon-strong cursor-pointer">\n                // SUMMON_AGENT\n            </button>')

with open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/code_v2.html', 'w', encoding='utf-8') as f:
    f.write(html)
