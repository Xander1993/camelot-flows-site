import json, os, sys
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

# ── MERLIN ────────────────────────────────────────────────────────────────────
merlin = '''
<main class="pt-36 pb-24">
  <section class="max-w-7xl mx-auto px-8">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 mb-32">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/10 border border-purple-500/20 mb-8">
          <span class="w-1.5 h-1.5 rounded-full bg-purple-500 animate-pulse"></span>
          <span class="text-[9px] font-mono text-purple-400 font-bold tracking-[0.3em] uppercase">Status // System Online</span>
        </div>
        <h1 class="text-6xl md:text-9xl font-display font-black text-white uppercase tracking-tighter leading-none mb-8">Automate<br/>Or <span class="text-purple-500">Stagnate.</span></h1>
        <p class="text-white/50 text-sm leading-relaxed mb-10 font-mono">High-end efficiency for technical professionals. Experience the next generation of protocol automation with real-time monitoring.</p>
        <div class="flex gap-4">
          <button onclick="window.location.href='contact.html?protocol=merlin'" class="px-8 py-3 bg-purple-500 text-white font-mono font-black text-[10px] uppercase tracking-widest rounded-lg hover:scale-105 transition-all shadow-[0_0_20px_rgba(139,92,246,0.4)] flex items-center gap-2">
            <span class="material-symbols-outlined text-sm">bolt</span> DEPLOY PROTOCOL
          </button>
          <button onclick="window.location.href='#docs'" class="px-8 py-3 border border-white/10 text-white font-mono font-black text-[10px] uppercase tracking-widest rounded-lg hover:bg-white/5 transition-all">DOCUMENTATION</button>
        </div>
      </div>
      <!-- Stats Panel -->
      <div class="glass-card rounded-2xl p-8 border-purple-500/20 relative">
        <div class="flex justify-between items-center mb-6">
          <div>
            <div class="text-[8px] font-mono text-white/30 uppercase tracking-widest mb-1">ACCELERATION_TIME</div>
            <div class="text-3xl font-display font-black text-white">12ms <span class="text-emerald-400 text-sm font-mono">2.4s</span></div>
          </div>
          <div>
            <div class="text-[8px] font-mono text-white/30 uppercase tracking-widest mb-1">AVT STATUS</div>
            <div class="text-3xl font-display font-black text-white">99.9% <span class="text-emerald-400 text-sm font-mono">FINAL</span></div>
          </div>
          <div class="text-right text-[8px] font-mono text-white/20 uppercase">MAKE: 32-MSF-1 / DL: AF24E</div>
        </div>
        <!-- Fake graph -->
        <div class="h-32 w-full mb-6 relative overflow-hidden rounded-lg bg-purple-500/5 border border-purple-500/10">
          <svg class="w-full h-full" viewBox="0 0 400 100" preserveAspectRatio="none">
            <path d="M0,80 C30,70 60,30 100,50 S170,20 220,40 S310,10 400,30" fill="none" stroke="#7c3aed" stroke-width="2" opacity="0.8"/>
            <path d="M0,90 C40,80 80,60 120,70 S200,40 260,60 S340,30 400,50" fill="none" stroke="#f59e0b" stroke-width="1.5" opacity="0.5" stroke-dasharray="4,4"/>
          </svg>
        </div>
        <div class="grid grid-cols-3 gap-4 mb-6">
          <div class="text-center"><div class="text-xl font-display font-black text-white">1,284</div><p class="text-[8px] font-mono text-white/30 uppercase">ACTIVE FLOWS</p></div>
          <div class="text-center"><div class="text-xl font-display font-black text-white">2.4M</div><p class="text-[8px] font-mono text-white/30 uppercase">OPS TODAY</p></div>
          <div class="text-center">
            <div class="text-[9px] font-mono text-emerald-400 font-bold uppercase tracking-widest mb-1">WORRY STATE</div>
            <div class="text-xl font-display font-black text-emerald-400">OPTIMAL</div>
          </div>
        </div>
        <div class="text-right">
          <div class="inline-flex items-center gap-2">
            <div class="w-2 h-2 rounded-full bg-purple-500 animate-pulse"></div>
            <span class="text-[9px] font-mono text-purple-400 uppercase tracking-widest">LIVE MONITORING</span>
          </div>
        </div>
      </div>
    </div>
    <!-- Feature Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8" data-gsap="fade-up">
      <div class="glass-card rounded-2xl p-8 border-white/5 hover:border-purple-500/30 transition-all">
        <span class="material-symbols-outlined text-purple-400 text-3xl mb-6 block">electric_bolt</span>
        <h3 class="text-xl font-display font-black text-white uppercase mb-4">Hyper-Speed Engine</h3>
        <p class="text-white/40 text-[11px] font-mono leading-relaxed uppercase tracking-widest">Execute complex protocol chains in sub-millisecond environments with optimised Rust backends.</p>
      </div>
      <div class="glass-card rounded-2xl p-8 border-white/5 hover:border-amber-500/30 transition-all">
        <span class="material-symbols-outlined text-amber-500 text-3xl mb-6 block">security</span>
        <h3 class="text-xl font-display font-black text-white uppercase mb-4">Military Encryption</h3>
        <p class="text-white/40 text-[11px] font-mono leading-relaxed uppercase tracking-widest">End-to-end encrypted logic flows that never touch a centralised database. Your keys, your rules.</p>
      </div>
      <div class="glass-card rounded-2xl p-8 border-white/5 hover:border-accent/30 transition-all">
        <span class="material-symbols-outlined text-accent text-3xl mb-6 block">hub</span>
        <h3 class="text-xl font-display font-black text-white uppercase mb-4">Universal Adapter</h3>
        <p class="text-white/40 text-[11px] font-mono leading-relaxed uppercase tracking-widest">Seamlessly connect any REST, GraphQL, or Webhook-based endpoint out of the box.</p>
      </div>
    </div>
  </section>
</main>
'''
build('merlin.html', 'Merlin Protocol', merlin)

# ── CASE STUDIES ──────────────────────────────────────────────────────────────
case_studies = '''
<main class="pt-36 pb-24">
  <section class="max-w-7xl mx-auto px-8">
    <div class="flex items-start justify-between mb-12">
      <div>
        <h1 class="text-5xl md:text-7xl font-display font-black uppercase tracking-tighter leading-none mb-4">
          <span class="text-accent">Case Studies:</span><br/><span class="text-white">Missions Completed</span>
        </h1>
        <p class="text-white/40 font-mono text-[11px] uppercase tracking-widest max-w-xl">High-impact results from technical engineering missions. Deploying scalable solutions across the full stack with surgical precision.</p>
      </div>
      <button class="hidden md:flex items-center gap-2 px-4 py-2 border border-white/10 rounded-lg text-white/40 font-mono text-[9px] uppercase tracking-widest hover:bg-white/5 transition-all">
        <span class="material-symbols-outlined text-sm">visibility</span> View GitHub
      </button>
    </div>
    <!-- Filter tabs -->
    <div class="flex gap-4 mb-12 border-b border-white/10 pb-px">
      <button class="pb-4 font-mono text-[10px] uppercase tracking-widest text-accent border-b-2 border-accent -mb-px transition-all">All Systems</button>
      <button class="pb-4 font-mono text-[10px] uppercase tracking-widest text-white/30 hover:text-white transition-all">Web Architectures</button>
      <button class="pb-4 font-mono text-[10px] uppercase tracking-widest text-white/30 hover:text-white transition-all">Backend Core</button>
      <button class="pb-4 font-mono text-[10px] uppercase tracking-widest text-white/30 hover:text-white transition-all">Automation Hooks</button>
    </div>
    <!-- Case cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-20">
      <div class="glass-card rounded-2xl overflow-hidden border-white/5 hover:border-accent/30 transition-all group">
        <div class="h-48 bg-gradient-to-br from-primary/20 to-accent/5 relative overflow-hidden flex items-center justify-center">
          <span class="material-symbols-outlined text-primary/40 text-8xl group-hover:scale-110 transition-all">network_node</span>
          <div class="absolute top-4 left-4 flex gap-2">
            <span class="px-2 py-1 bg-black/60 border border-primary/30 rounded text-[7px] font-mono text-primary uppercase">SCALE</span>
            <span class="px-2 py-1 bg-black/60 border border-white/10 rounded text-[7px] font-mono text-white/30 uppercase">FINTECH</span>
          </div>
        </div>
        <div class="p-8">
          <h3 class="text-xl font-display font-black text-white uppercase mb-3">Enterprise SEO Engine</h3>
          <p class="text-white/40 text-[10px] font-mono leading-relaxed uppercase mb-6">Engineered a global load-platform architecture focusing on dynamic rendering and multi-region deployment.</p>
          <div class="flex items-center justify-between mb-6">
            <div><span class="text-[8px] font-mono text-white/20">GROWTH</span><div class="text-emerald-400 font-display font-black text-sm">3x organic traffic</div></div>
          </div>
          <button class="w-full py-3 border border-white/10 rounded-lg text-white/50 font-mono text-[9px] uppercase tracking-widest hover:bg-white/5 transition-all">Mission Intel</button>
        </div>
      </div>
      <div class="glass-card rounded-2xl overflow-hidden border-white/5 hover:border-violet-500/30 transition-all group">
        <div class="h-48 bg-gradient-to-br from-violet-500/20 to-primary/5 relative overflow-hidden flex items-center justify-center">
          <span class="material-symbols-outlined text-violet-500/40 text-8xl group-hover:scale-110 transition-all">terminal</span>
          <div class="absolute top-4 left-4 flex gap-2">
            <span class="px-2 py-1 bg-black/60 border border-violet-500/30 rounded text-[7px] font-mono text-violet-400 uppercase">B2B</span>
            <span class="px-2 py-1 bg-black/60 border border-white/10 rounded text-[7px] font-mono text-white/30 uppercase">ERP</span>
          </div>
        </div>
        <div class="p-8">
          <h3 class="text-xl font-display font-black text-white uppercase mb-3">Workflow Automator</h3>
          <p class="text-white/40 text-[10px] font-mono leading-relaxed uppercase mb-6">Backend pipeline for high-scale operations, automating data synchronization across legacy ERP systems.</p>
          <div class="flex items-center justify-between mb-6">
            <div><span class="text-[8px] font-mono text-white/20">EFFICIENCY</span><div class="text-amber-400 font-display font-black text-sm">28hrs saved daily</div></div>
          </div>
          <button class="w-full py-3 border border-white/10 rounded-lg text-white/50 font-mono text-[9px] uppercase tracking-widest hover:bg-white/5 transition-all">Mission Intel</button>
        </div>
      </div>
      <div class="glass-card rounded-2xl overflow-hidden border-white/5 hover:border-amber-500/30 transition-all group">
        <div class="h-48 bg-gradient-to-br from-amber-500/20 to-orange-500/5 relative overflow-hidden flex items-center justify-center">
          <span class="material-symbols-outlined text-amber-500/40 text-8xl group-hover:scale-110 transition-all">language</span>
          <div class="absolute top-4 left-4 flex gap-2">
            <span class="px-2 py-1 bg-black/60 border border-amber-500/30 rounded text-[7px] font-mono text-amber-400 uppercase">CDN</span>
            <span class="px-2 py-1 bg-black/60 border border-white/10 rounded text-[7px] font-mono text-white/30 uppercase">E-COM</span>
          </div>
        </div>
        <div class="p-8">
          <h3 class="text-xl font-display font-black text-white uppercase mb-3">E-Commerce Core</h3>
          <p class="text-white/40 text-[10px] font-mono leading-relaxed uppercase mb-6">Headless commerce migration for a luxury brand, focusing on LCP optimization and global CDN strategy.</p>
          <div class="flex items-center justify-between mb-6">
            <div><span class="text-[8px] font-mono text-white/20">VELOCITY</span><div class="text-accent font-display font-black text-sm">60% faster load</div></div>
          </div>
          <button class="w-full py-3 border border-white/10 rounded-lg text-white/50 font-mono text-[9px] uppercase tracking-widest hover:bg-white/5 transition-all">Mission Intel</button>
        </div>
      </div>
    </div>
    <!-- Bottom stats -->
    <div class="grid grid-cols-3 gap-6 pt-12 border-t border-white/5">
      <div>
        <div class="text-[8px] font-mono text-white/30 uppercase tracking-widest mb-2">SYSTEM UPTIME</div>
        <div class="text-4xl font-display font-black text-white">99.9%</div>
        <div class="text-emerald-400 font-mono text-[10px] mt-1">+0.01% drift</div>
      </div>
      <div>
        <div class="text-[8px] font-mono text-white/30 uppercase tracking-widest mb-2">MISSIONS DONE</div>
        <div class="text-4xl font-display font-black text-white">42</div>
        <div class="text-accent font-mono text-[10px] mt-1">100% success+</div>
      </div>
      <div>
        <div class="text-[8px] font-mono text-white/30 uppercase tracking-widest mb-2">LINES DEPLOYED</div>
        <div class="text-4xl font-display font-black text-white">1.2M</div>
        <div class="text-violet-400 font-mono text-[10px] mt-1">Optimized code</div>
      </div>
    </div>
  </section>
</main>
'''
build('case-studies.html', 'Case Studies', case_studies)

print("Part 3 done.")
