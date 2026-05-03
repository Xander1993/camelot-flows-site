import json, os, sys
sys.path.insert(0, r'c:\Users\user\Downloads\stitch_camelot_flows_homepage')

BASE = r'c:\Users\user\Downloads\stitch_camelot_flows_homepage'

with open(os.path.join(BASE, '_shell_parts.json'), 'r', encoding='utf-8') as f:
    shell = json.load(f)

HEAD = shell['head_html']
BODY = shell['body_shell']

def build(filename, title, content):
    head = HEAD.replace('<title>Camelot Flows | Digital Architect</title>', f'<title>Camelot Flows | {title}</title>')
    full = head + '\n' + BODY.replace('[PAGE_CONTENT]', content)
    with open(os.path.join(BASE, filename), 'w', encoding='utf-8') as f:
        f.write(full)
    print(f"  OK {filename}")

# ── ARSENAL ───────────────────────────────────────────────────────────────────
arsenal = '''
<main class="pt-36 pb-24 overflow-hidden">
  <section class="max-w-7xl mx-auto px-8">
    <div class="text-center mb-20">
      <h1 class="text-6xl md:text-[10vw] font-display font-black text-white uppercase tracking-tighter leading-none mb-6">THE ARSENAL</h1>
      <p class="text-white/40 font-mono text-[11px] uppercase tracking-[0.4em]">High-End Technology Armory for the Modern Digital Elite.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-24">
      <!-- Excalibur -->
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-accent/30 transition-all group relative overflow-hidden" data-gsap="fade-up">
        <div class="absolute top-4 right-4 px-2 py-1 bg-white/5 rounded text-[8px] font-mono text-white/30 uppercase tracking-widest">VONA</div>
        <div class="flex items-center gap-4 mb-6">
          <div class="w-12 h-12 rounded-xl bg-accent/10 border border-accent/20 flex items-center justify-center">
            <span class="material-symbols-outlined text-accent text-xl">bolt</span>
          </div>
          <div>
            <h3 class="text-2xl font-display font-black text-white uppercase">Excalibur</h3>
            <p class="text-[9px] font-mono text-white/30 uppercase tracking-widest">Protocol Automation</p>
          </div>
        </div>
        <div class="mb-6">
          <span class="text-5xl font-display font-black text-white">$499</span>
          <span class="text-white/30 font-mono text-[10px] ml-2 uppercase">/3.1250V</span>
        </div>
        <div class="flex gap-3 mb-8">
          <span class="px-2 py-1 bg-white/5 border border-white/10 rounded text-[8px] font-mono text-white/40 uppercase">FRAMEWRK: NEXT.JS 14</span>
          <span class="px-2 py-1 bg-white/5 border border-white/10 rounded text-[8px] font-mono text-white/40 uppercase">STYLING: TAILWIND CSS</span>
        </div>
        <ul class="space-y-3 mb-10 text-[11px] font-mono text-white/50">
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent text-sm">check_circle</span> Glass-Isoptic Design System</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent text-sm">check_circle</span> Custom Motion Library</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent text-sm">check_circle</span> SEO Optimized Components</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent text-sm">check_circle</span> Unlimited Sub-domains</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-4 rounded-xl border border-accent/30 text-accent font-mono font-black text-[10px] uppercase tracking-widest hover:bg-accent hover:text-black transition-all">WIELD EXCALIBUR</button>
      </div>
      <!-- Merlin (Featured) -->
      <div class="glass-card rounded-3xl p-10 border-primary/40 shadow-[0_0_60px_rgba(79,70,229,0.2)] scale-105 relative overflow-hidden" data-gsap="fade-up">
        <div class="absolute top-4 right-4 px-2 py-1 bg-primary/20 border border-primary/40 rounded text-[8px] font-mono text-primary uppercase tracking-widest">BEST POPULAR</div>
        <div class="flex items-center gap-4 mb-6">
          <div class="w-12 h-12 rounded-xl bg-primary/20 border border-primary/40 flex items-center justify-center">
            <span class="material-symbols-outlined text-primary-glow text-xl">psychology</span>
          </div>
          <div>
            <h3 class="text-2xl font-display font-black text-white uppercase">Merlin</h3>
            <p class="text-[9px] font-mono text-white/30 uppercase tracking-widest">IntelliCore Engine</p>
          </div>
        </div>
        <div class="mb-6">
          <span class="text-5xl font-display font-black text-white">$1,299</span>
          <span class="text-white/30 font-mono text-[10px] ml-2 uppercase">/instance</span>
        </div>
        <div class="flex gap-3 mb-8 flex-wrap">
          <span class="px-2 py-1 bg-white/5 border border-white/10 rounded text-[8px] font-mono text-white/40 uppercase">TIER: 1</span>
          <span class="px-2 py-1 bg-white/5 border border-white/10 rounded text-[8px] font-mono text-white/40 uppercase">RECUR +3</span>
          <span class="px-2 py-1 bg-white/5 border border-white/10 rounded text-[8px] font-mono text-white/40 uppercase">AI: 0.23 / TIER: 25</span>
        </div>
        <ul class="space-y-3 mb-10 text-[11px] font-mono text-white/50">
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-primary text-sm">check_circle</span> Real-time Predictive Analytics</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-primary text-sm">check_circle</span> Orbital UI Data Visuals</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-primary text-sm">check_circle</span> Neural-Node Architecture</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-primary text-sm">check_circle</span> Advanced Logic Data Builder</li>
        </ul>
        <button onclick="window.location.href='merlin.html'" class="w-full py-4 rounded-xl bg-white text-black font-mono font-black text-[10px] uppercase tracking-widest hover:scale-105 transition-all">SUMMON MERLIN</button>
      </div>
      <!-- Round Table -->
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-amber-500/30 transition-all group relative overflow-hidden" data-gsap="fade-up">
        <div class="absolute top-4 right-4 px-2 py-1 bg-amber-500/10 border border-amber-500/20 rounded text-[8px] font-mono text-amber-500 uppercase tracking-widest">ENTERPRISE</div>
        <div class="flex items-center gap-4 mb-6">
          <div class="w-12 h-12 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center">
            <span class="material-symbols-outlined text-amber-500 text-xl">hub</span>
          </div>
          <div>
            <h3 class="text-2xl font-display font-black text-white uppercase">Round Table</h3>
            <p class="text-[9px] font-mono text-white/30 uppercase tracking-widest">Neural Biometric</p>
          </div>
        </div>
        <div class="mb-6">
          <span class="text-5xl font-display font-black text-white">$2,499</span>
          <span class="text-white/30 font-mono text-[10px] ml-2 uppercase">/ecosystem</span>
        </div>
        <div class="flex gap-3 mb-8 flex-wrap">
          <span class="px-2 py-1 bg-white/5 border border-white/10 rounded text-[8px] font-mono text-white/40 uppercase">CHANNEL: MULTI</span>
          <span class="px-2 py-1 bg-white/5 border border-white/10 rounded text-[8px] font-mono text-white/40 uppercase">POST-QUANTUM</span>
        </div>
        <ul class="space-y-3 mb-10 text-[11px] font-mono text-white/50">
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-amber-500 text-sm">check_circle</span> Decentralized Edge Nodes</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-amber-500 text-sm">check_circle</span> Multi-tenant Architecture</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-amber-500 text-sm">check_circle</span> Global CDN Propagation</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-amber-500 text-sm">check_circle</span> Cyberpunk UI Component Kit</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-4 rounded-xl border border-amber-500/30 text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest hover:bg-amber-500 hover:text-black transition-all">JOIN THE TABLE</button>
      </div>
    </div>
    <!-- Stats row -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
      <div class="glass-card rounded-2xl p-6 text-center border-white/5">
        <span class="material-symbols-outlined text-accent text-2xl mb-3 block">deployed_code</span>
        <div class="text-2xl font-display font-black text-white mb-1">412+</div>
        <p class="text-[9px] font-mono text-white/30 uppercase tracking-widest">Operational Runs</p>
      </div>
      <div class="glass-card rounded-2xl p-6 text-center border-white/5">
        <span class="material-symbols-outlined text-primary text-2xl mb-3 block">hub</span>
        <div class="text-2xl font-display font-black text-white mb-1">916</div>
        <p class="text-[9px] font-mono text-white/30 uppercase tracking-widest">616 Neural Modules</p>
      </div>
      <div class="glass-card rounded-2xl p-6 text-center border-white/5">
        <span class="material-symbols-outlined text-violet-400 text-2xl mb-3 block">encrypted</span>
        <div class="text-2xl font-display font-black text-white mb-1">Ω</div>
        <p class="text-[9px] font-mono text-white/30 uppercase tracking-widest">RNG-256 Quantum</p>
      </div>
      <div class="glass-card rounded-2xl p-6 text-center border-white/5">
        <span class="material-symbols-outlined text-amber-500 text-2xl mb-3 block">speed</span>
        <div class="text-2xl font-display font-black text-white mb-1">125+</div>
        <p class="text-[9px] font-mono text-white/30 uppercase tracking-widest">100 TEGS/HIGH+</p>
      </div>
    </div>
  </section>
</main>
'''
build('arsenal.html', 'Arsenal', arsenal)
print("Part 2 done.")
