import os
import re

html_path = 'c:/Users/user/Downloads/stitch_camelot_flows_homepage/code_v2.html'
base_dir = os.path.dirname(html_path)

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Text Replacements to shift focus from security to design
content = content.replace('href="#">[Round_Table]</a>', 'href="code_v2.html#round-table">[Round_Table]</a>')
content = content.replace('href="#">[Arsenal]</a>', 'href="arsenal.html">[Arsenal]</a>')
content = content.replace('href="#">[Merlin]</a>', 'href="merlin.html">[Merlin]</a>')
content = content.replace('href="#">', 'href="code_v2.html">') 

content = content.replace(
    'Deploy <span class="text-white font-medium">AI Autopilot</span> and high-performance web infrastructure to conquer the digital frontier. Orchestrate your business with mystic precision.',
    'Deploy <span class="text-white font-medium">Awwwards-tier web design</span> and hyper-fast infrastructure to conquer the digital frontier. Automate your business with zero friction.'
)
content = content.replace(
    'The Obsidian<br/><span class="text-emerald-400 text-glow" style="text-shadow: 0 0 20px rgba(16,185,129,0.5)">Vault</span>',
    'Aesthetic<br/><span class="text-emerald-400 text-glow" style="text-shadow: 0 0 20px rgba(16,185,129,0.5)">Excellence</span>'
)
content = content.replace(
    'Protect your digital sovereignty with Templar-grade encryption and immutable ledgers. We architect zero-trust networks and impenetrable data sanctuaries for the modern sovereign entity, guaranteeing absolute operational silence.',
    'Elevate your brand with award-winning UI/UX interfaces and fluid GSAP animations. We architect visually stunning digital experiences that convert, guaranteeing absolute user engagement.'
)

content = content.replace('Templar-Grade Encryption', 'Pixel-Perfect Layouts')
content = content.replace('Zero-Trust Architecture', 'Fluid Micro-Interactions')
content = content.replace('Immutable Audit Logs', 'Premium Brand Identity')
content = content.replace('>shield_locked<', '>design_services<')
content = content.replace('>fingerprint<', '>animation<')
content = content.replace('>verified_user<', '>diamond<')
content = content.replace('Vault Secure', 'Design Perfected')

content = content.replace('SHIELD_ACTIVE', 'PERFORMANCE_MAX')
content = content.replace('Protection Level: MAX', 'Speed & Design: Awwwards Level')
content = content.replace('Mission: Infrastructure for Sovereigns.', 'Mission: Awwwards-Tier Design & AI Automation.')
content = content.replace('256-bit Encrypted', 'Lightning Fast Performance')
content = content.replace('encrypted</span>', 'bolt</span>')
content = content.replace('shield_with_heart', 'architecture')

routes = {
    'The Arsenal': 'arsenal.html',
    'Merlin Protocol': 'merlin.html',
    'Case Studies': 'case-studies.html',
    'Documentation': 'documentation.html',
    'About Us': 'about-us.html',
    'Careers': 'careers.html',
    'Legal': 'legal.html',
    'Privacy': 'privacy.html'
}

for name, slug in routes.items():
    pattern = r'href="code_v2\.html"([^>]*?><span[^>]*?>&gt;</span>\s*' + name + ')'
    content = re.sub(pattern, f'href="{slug}"\\1', content)

content = content.replace('<button class="group relative px-8 py-4 bg-primary text-white font-mono font-bold text-sm tracking-wide overflow-hidden rounded-sm hover:scale-[1.02] transition-transform">', '<button onclick="window.location.href=\'merlin.html\'" class="group relative px-8 py-4 bg-primary text-white font-mono font-bold text-sm tracking-wide overflow-hidden rounded-sm hover:scale-[1.02] transition-transform">')
content = content.replace('<button class="px-8 py-4 glass-panel text-slate-300 font-mono font-bold text-sm tracking-wide rounded-sm hover:bg-white/5 border border-white/10 hover:border-primary/50 transition-colors flex items-center gap-3">', '<button onclick="window.location.href=\'arsenal.html\'" class="px-8 py-4 glass-panel text-slate-300 font-mono font-bold text-sm tracking-wide rounded-sm hover:bg-white/5 border border-white/10 hover:border-primary/50 transition-colors flex items-center gap-3">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Extract sections to build other pages
nav_end = content.find('</nav>') + 6
header_html = content[:nav_end]
# But we don't want the preloader on every page to prevent user annoyance.
header_html_no_preloader = re.sub(r'<div id="preloader".*?</div>\s*<div class="grain-overlay"', '<div class="grain-overlay"', header_html, flags=re.DOTALL)

footer_start = content.find('<footer')
footer_html = content[footer_start:]

# Arsenal Page
arsenal_content = f'''{header_html_no_preloader}
<main class="relative pt-40 pb-20 px-6 min-h-screen bg-obsidian">
    <div class="absolute inset-0 grid-bg opacity-30"></div>
    <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-20">
            <span class="text-neon-cyan font-mono text-xs uppercase tracking-[0.3em] mb-4 block">// SHOWCASE</span>
            <h1 class="font-display text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-6 text-glow">The <span class="text-neon-cyan text-glow-cyan">Arsenal</span></h1>
            <p class="text-slate-400 max-w-2xl mx-auto">Explore our collection of Awwwards-tier web designs, high-performance templates, and conversion-optimized digital experiences.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="glass-panel p-4 rounded-xl group hover:border-neon-cyan/50 transition-colors">
                <div class="aspect-video bg-black rounded-lg overflow-hidden mb-6 relative">
                    <div class="absolute w-full h-full bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <span class="absolute bottom-4 left-4 z-20 font-mono text-xs text-neon-cyan uppercase">E-Commerce</span>
                </div>
                <h3 class="font-display font-bold text-2xl text-white mb-2">NexStore Theme</h3>
                <p class="text-sm text-slate-400 font-body mb-4">Hyper-fast headless Shopify integration with WebGL 3D product previews.</p>
                <a href="#" class="text-xs font-mono text-white group-hover:text-neon-cyan transition-colors flex items-center gap-2">VIEW_PROJECT <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
            </div>
            <div class="glass-panel p-4 rounded-xl group hover:border-primary/50 transition-colors">
                <div class="aspect-video bg-black rounded-lg overflow-hidden mb-6 relative">
                    <div class="absolute w-full h-full bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <span class="absolute bottom-4 left-4 z-20 font-mono text-xs text-primary uppercase">SaaS Dashboard</span>
                </div>
                <h3 class="font-display font-bold text-2xl text-white mb-2">MetricFlow UI</h3>
                <p class="text-sm text-slate-400 font-body mb-4">A dark-mode obsessed dashboard layout featuring live GSAP data visualizations.</p>
                <a href="#" class="text-xs font-mono text-white group-hover:text-primary transition-colors flex items-center gap-2">VIEW_PROJECT <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
            </div>
            <div class="glass-panel p-4 rounded-xl group hover:border-emerald-400/50 transition-colors">
                <div class="aspect-video bg-black rounded-lg overflow-hidden mb-6 relative">
                    <div class="absolute w-full h-full bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <span class="absolute bottom-4 left-4 z-20 font-mono text-xs text-emerald-400 uppercase">Fintech</span>
                </div>
                <h3 class="font-display font-bold text-2xl text-white mb-2">Vault Pay</h3>
                <p class="text-sm text-slate-400 font-body mb-4">Secure, elegant, and blazing fast banking template with fluid micro-interactions.</p>
                <a href="#" class="text-xs font-mono text-white group-hover:text-emerald-400 transition-colors flex items-center gap-2">VIEW_PROJECT <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
            </div>
        </div>
    </div>
</main>
{footer_html}'''

with open(os.path.join(base_dir, 'arsenal.html'), 'w', encoding='utf-8') as f:
    f.write(arsenal_content)

# Merlin Page
merlin_content = f'''{header_html_no_preloader}
<main class="relative pt-40 pb-20 px-6 min-h-screen bg-obsidian overflow-hidden">
    <div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-primary/10 blur-[150px] rounded-full pointer-events-none"></div>
    <div class="max-w-5xl mx-auto relative z-10 text-center">
        <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-primary/30 bg-primary/10 mb-8">
            <span class="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
            <span class="font-mono text-xs text-primary tracking-widest uppercase">AI_SALES_AGENT_v2.0</span>
        </div>
        <h1 class="font-display text-5xl md:text-8xl font-black text-white uppercase tracking-tighter mb-8 text-glow">The <span class="text-primary-glow">Merlin</span> Protocol</h1>
        <p class="text-lg text-slate-400 max-w-3xl mx-auto leading-relaxed mb-12">
            Imagine an employee who never sleeps, knows your entire product catalog by heart, and closes deals through WhatsApp and Web Chat simultaneously. Merlin is our flagship AI business automation engine.
        </p>
        <div class="glass-panel p-8 md:p-12 rounded-2xl border-t border-white/10 shadow-neon mb-16 text-left">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                <div>
                     <h3 class="font-mono font-bold text-primary mb-4 uppercase tracking-wider text-sm">// Capabilities</h3>
                     <ul class="space-y-4 text-slate-300">
                         <li class="flex items-start gap-3">
                             <span class="material-symbols-outlined text-primary">check_circle</span>
                             <span><strong>Natural Language Processing:</strong> Converses indistinguishably from a human agent.</span>
                         </li>
                         <li class="flex items-start gap-3">
                             <span class="material-symbols-outlined text-primary">check_circle</span>
                             <span><strong>Omni-Channel Sync:</strong> Deploys on WhatsApp, Telegram, Instagram, and Web.</span>
                         </li>
                         <li class="flex items-start gap-3">
                             <span class="material-symbols-outlined text-primary">check_circle</span>
                             <span><strong>CRM Auto-Population:</strong> Automatically logs leads and schedules directly into your calendar.</span>
                         </li>
                     </ul>
                </div>
                <div class="glass-panel p-6 rounded-lg bg-black/50 border border-primary/20 flex flex-col justify-center items-center text-center">
                    <span class="material-symbols-outlined text-5xl text-primary mb-4 animate-pulse">model_training</span>
                    <h4 class="font-display font-bold text-white text-xl mb-2">Ready to Deploy?</h4>
                    <p class="text-xs text-slate-500 font-mono mb-6">Integration takes less than 48 hours.</p>
                    <button class="bg-primary hover:bg-white text-white hover:text-black font-mono font-bold uppercase tracking-wider text-sm py-3 px-6 rounded transition-all">Summon Merlin</button>
                </div>
            </div>
        </div>
    </div>
</main>
{footer_html}'''

for name, slug in routes.items():
    if slug not in ['arsenal.html', 'merlin.html']:
        page_title = name
        generic_content = f'''{header_html_no_preloader}
<main class="relative pt-40 pb-20 px-6 min-h-screen flex flex-col items-center">
    <div class="absolute inset-0 bg-obsidian -z-20"></div>
    <div class="absolute inset-0 grid-bg opacity-30 -z-20"></div>
    
    <div class="max-w-4xl mx-auto w-full relative z-10 glass-panel p-8 md:p-16 rounded-2xl border-t border-white/10 shadow-neon">
        <h1 class="font-display text-4xl md:text-5xl font-black text-white uppercase tracking-tighter mb-8 text-glow">
            {page_title}
        </h1>
        <div class="h-1 w-20 bg-gradient-to-r from-primary to-transparent mb-12"></div>
        
        <div class="prose prose-invert prose-lg max-w-none font-body text-slate-300 pointer-events-none">
            <p>Welcome to the {page_title} page.</p>
            <p>We believe in creating high-performance, visually stunning architectures to command user engagement.</p>
        </div>
    </div>
</main>
{footer_html}'''
        with open(os.path.join(base_dir, slug), 'w', encoding='utf-8') as f:
            f.write(generic_content)

with open(os.path.join(base_dir, 'merlin.html'), 'w', encoding='utf-8') as f:
    f.write(merlin_content)

print('Success: Replaced files')
