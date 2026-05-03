import os

base = 'c:/Users/user/Downloads/stitch_camelot_flows_homepage'

# Read existing page for shell
with open(os.path.join(base, 'about-us.html'), 'r', encoding='utf-8') as f:
    shell = f.read()

head_end = shell.find('</head>') + len('</head>')
head_html = shell[:head_end]
body_start = shell.find('<body')
nav_end = shell.find('</nav>') + len('</nav>')
body_shell = shell[body_start:nav_end]

# Update nav links
body_shell = body_shell.replace(
    'href="code_v2.html#round-table">[Round_Table]</a>',
    'href="code_v2.html">[Home]</a>'
)
# Add About and Agencies links after Merlin
body_shell = body_shell.replace(
    'href="merlin.html">[Merlin]</a>\n</div>',
    'href="merlin.html">[Merlin]</a>\n'
    '<a class="px-4 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider" href="about.html">[About]</a>\n'
    '<a class="px-4 py-2 text-xs font-mono text-slate-400 hover:text-white hover:bg-white/5 rounded transition-colors uppercase tracking-wider" href="for-agencies.html">[Agencies]</a>\n</div>'
)

NEW_FOOTER = '''<footer class="bg-obsidian pt-24 pb-12 px-6 border-t border-primary/20 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-1/2 h-[1px] bg-gradient-to-r from-transparent via-primary/50 to-transparent shadow-[0_0_15px_rgba(99,102,241,0.5)]"></div>
<div class="max-w-7xl mx-auto">
<div class="grid grid-cols-1 md:grid-cols-12 gap-12 md:gap-16 mb-20">
<div class="md:col-span-4">
<div class="flex items-center gap-3 mb-6">
<div class="w-8 h-8 rounded bg-primary flex items-center justify-center"><span class="material-symbols-outlined text-white text-lg">architecture</span></div>
<span class="font-display text-xl font-bold tracking-tighter uppercase text-white">Camelot Flows</span>
</div>
<p class="text-slate-500 mb-8 text-sm leading-relaxed font-mono">
<span class="text-primary">&gt;</span> Location: Chișinău, Moldova<br/>
<span class="text-primary">&gt;</span> Founded by Alex Buzi<br/>
<span class="text-primary">&gt;</span> Mission: Award-Winning Design &amp; AI Automation.
</p>
</div>
<div class="md:col-span-2">
<h5 class="font-mono font-bold mb-6 text-xs text-white uppercase tracking-widest border-b border-white/10 pb-2 w-max">Protocol</h5>
<ul class="space-y-3 text-slate-500 text-sm font-mono">
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="arsenal.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> The Arsenal</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="merlin.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Merlin Protocol</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="case-studies.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Case Studies</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="for-agencies.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> For Agencies</a></li>
</ul>
</div>
<div class="md:col-span-2">
<h5 class="font-mono font-bold mb-6 text-xs text-white uppercase tracking-widest border-b border-white/10 pb-2 w-max">Company</h5>
<ul class="space-y-3 text-slate-500 text-sm font-mono">
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="about.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> About</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="work-with-me.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Work With Me</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="legal.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Legal</a></li>
<li><a class="hover:text-primary transition-colors flex items-center gap-2 group" href="privacy.html"><span class="opacity-0 group-hover:opacity-100 text-primary transition-opacity">&gt;</span> Privacy</a></li>
</ul>
</div>
<div class="md:col-span-4">
<h5 class="font-mono font-bold mb-6 text-xs text-white uppercase tracking-widest border-b border-white/10 pb-2 w-max">Join the Vanguard</h5>
<p class="text-slate-500 text-sm mb-6 leading-relaxed">Weekly insights on AI automation sent directly to your terminal.</p>
<div class="flex gap-2 p-1 bg-white/5 rounded border border-white/10 focus-within:border-primary/50 transition-colors">
<input class="bg-transparent border-none focus:ring-0 text-sm flex-1 px-4 text-white font-mono placeholder:text-slate-600" placeholder="ENTER_EMAIL_ADDRESS" type="email"/>
<button class="bg-primary hover:bg-primary/90 text-white px-4 py-2 rounded text-xs font-bold transition-colors font-mono">[SUBMIT]</button>
</div>
</div>
</div>
<div class="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6">
<p class="text-xs text-slate-600 font-mono">&copy; 2026 Camelot Flows. Built by Alex Buzi.</p>
<div class="flex flex-wrap justify-center gap-4 md:gap-8">
<div class="flex items-center gap-2 text-xs text-slate-500 font-mono"><span class="material-symbols-outlined text-sm text-green-500">wifi</span><span>System Status: Optimal</span></div>
<div class="flex items-center gap-2 text-xs text-slate-500 font-mono"><span class="material-symbols-outlined text-sm text-blue-500">bolt</span><span>Lightning Fast Performance</span></div>
</div>
</div>
</div>
</footer>'''

SUBPAGE_JS = '''
<div id="custom-cursor"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/TextPlugin.min.js"></script>
<script src="https://unpkg.com/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
<script>
gsap.registerPlugin(ScrollTrigger, TextPlugin);
const lenis = new Lenis({ duration: 1.2, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), smoothWheel: true });
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => { lenis.raf(time * 1000); });
gsap.ticker.lagSmoothing(0);
window.addEventListener('load', () => { gsap.from('main', { opacity: 0, y: 40, duration: 1, ease: 'power4.out' }); });
(() => {
    if (!window.matchMedia('(pointer: fine)').matches) return;
    const cursor = document.getElementById('custom-cursor');
    let vis = false, lpt = 0;
    gsap.set(cursor, { xPercent: -50, yPercent: -50, zIndex: 9999 });
    window.addEventListener('mousemove', (e) => {
        if (!vis) { vis = true; gsap.to(cursor, { opacity: 1, duration: 0.3 }); }
        gsap.to(cursor, { x: e.clientX, y: e.clientY, duration: 0.15, ease: 'power2.out' });
        const now = Date.now();
        if (now - lpt > 12) { lpt = now; const p = document.createElement('div');
            p.className = 'fixed w-[6px] h-[6px] bg-neon-purple rounded-full pointer-events-none z-[9998] shadow-[0_0_20px_4px_rgba(191,0,255,0.9)] mix-blend-screen blur-[1px]';
            document.body.appendChild(p); gsap.set(p, { x: e.clientX, y: e.clientY, xPercent: -50, yPercent: -50 });
            gsap.to(p, { x: e.clientX+(Math.random()-0.5)*15, y: e.clientY+(Math.random()-0.5)*15, scale: 0, opacity: 0, duration: Math.random()*0.4+0.4, ease: 'power2.out', onComplete: () => p.remove() });
        }
    });
    document.addEventListener('mouseleave', () => { vis = false; gsap.to(cursor, { opacity: 0, duration: 0.3 }); });
    document.querySelectorAll('a, button, input').forEach(el => {
        el.addEventListener('mouseenter', () => gsap.to(cursor, { scale: 3.5, opacity: 0.3, backgroundColor: '#bf00ff', duration: 0.3 }));
        el.addEventListener('mouseleave', () => gsap.to(cursor, { scale: 1, opacity: 1, backgroundColor: '#8b5cf6', duration: 0.3 }));
    });
    document.querySelectorAll('button').forEach(m => {
        m.addEventListener('mousemove', (e) => { const r = m.getBoundingClientRect(); gsap.to(m, { x: (e.clientX-r.left-r.width/2)*0.25, y: (e.clientY-r.top-r.height/2)*0.25, duration: 0.4, ease: 'power2.out', overwrite: 'auto' }); });
        m.addEventListener('mouseleave', () => gsap.to(m, { x:0, y:0, duration:0.8, ease:'elastic.out(1,0.3)', overwrite:'auto' }));
    });
})();
gsap.utils.toArray('.fade-in-section').forEach((el, i) => {
    gsap.from(el, { scrollTrigger: { trigger: el, start: 'top 85%', toggleActions: 'play none none none' }, y: 60, opacity: 0, duration: 1, delay: i * 0.05, ease: 'power4.out' });
});
gsap.utils.toArray('.timeline-node').forEach((el, i) => {
    gsap.from(el, { scrollTrigger: { trigger: el, start: 'top 85%', toggleActions: 'play none none none' }, x: i % 2 === 0 ? -60 : 60, opacity: 0, duration: 0.8, ease: 'power3.out' });
});
let proxy = { skew: 0 }, skewSetter = gsap.quickSetter('.glass-panel, .glass-card', 'skewY', 'deg'), clamp = gsap.utils.clamp(-3, 3);
ScrollTrigger.create({ onUpdate: (self) => { let s = clamp(self.getVelocity() / -400); if (Math.abs(s) > Math.abs(proxy.skew)) { proxy.skew = s; gsap.to(proxy, { skew: 0, duration: 0.8, ease: 'power3', overwrite: true, onUpdate: () => skewSetter(proxy.skew) }); } } });
</script>
</body></html>'''

def build_page(title, main_html):
    h = head_html.replace('<title>Camelot Flows | Neon Knight Edition</title>', f'<title>Camelot Flows | {title}</title>')
    return h + '\n' + body_shell + '\n' + main_html + '\n' + NEW_FOOTER + '\n' + SUBPAGE_JS

# ===================== PAGE CONTENT =====================
# Store in separate file to keep this script manageable
# We'll call build_pages_content.py next
print("Shell builder ready. Head:", len(head_html), "Body shell:", len(body_shell))

# Save shell parts for next script
import json
with open(os.path.join(base, '_shell_parts.json'), 'w', encoding='utf-8') as f:
    json.dump({
        'head_html': head_html,
        'body_shell': body_shell,
        'new_footer': NEW_FOOTER,
        'subpage_js': SUBPAGE_JS
    }, f)
print("Shell parts saved.")
