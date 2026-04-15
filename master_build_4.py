import json, os
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

# ── WORK WITH ME ──────────────────────────────────────────────────────────────
work = '''
<main class="pt-36 pb-24">
  <section class="max-w-7xl mx-auto px-8">
    <div class="mb-20">
      <h1 class="text-6xl md:text-9xl font-display font-black uppercase tracking-tighter leading-none mb-6">
        I DON'T HAVE JOBS.<br/><span class="text-transparent bg-clip-text bg-gradient-to-r from-accent to-violet-400">I HAVE A MISSION.</span>
      </h1>
      <p class="text-white/50 max-w-2xl font-mono text-[11px] uppercase tracking-widest leading-relaxed mb-10">
        Building the future of decentralised intelligence. I'm a late-night coding rat, no-expense politics, just lean innovation.
      </p>
      <div class="flex flex-wrap gap-3 mb-8">
        <span class="px-3 py-1 bg-accent/10 border border-accent/20 rounded text-[9px] font-mono text-accent uppercase tracking-widest">#Bootstrapped</span>
        <span class="px-3 py-1 bg-white/5 border border-white/10 rounded text-[9px] font-mono text-white/40 uppercase tracking-widest">#solo_flow</span>
        <span class="px-3 py-1 bg-white/5 border border-white/10 rounded text-[9px] font-mono text-white/40 uppercase tracking-widest">#no_bullshit</span>
      </div>
    </div>

    <!-- Reality Check -->
    <div class="glass-card rounded-2xl p-10 border-amber-500/20 mb-16">
      <div class="flex items-center gap-3 mb-6">
        <span class="material-symbols-outlined text-amber-500">warning</span>
        <span class="text-[9px] font-mono text-amber-500 uppercase tracking-widest font-bold">REALITY CHECK</span>
      </div>
      <h2 class="text-2xl font-display font-black text-white uppercase mb-4">This isn't your average 9-to-6.</h2>
      <p class="text-white/50 font-mono text-[11px] uppercase tracking-widest leading-relaxed mb-8 max-w-3xl">
        We are a bootstrapped startup focused on high-innovation. Expect high performing, late-night coding sessions and a mission-first culture. We don't do endless meetings. We ship code and solve hard problems.
      </p>
    </div>

    <!-- Tech Stack -->
    <div class="mb-20">
      <h2 class="text-3xl font-display font-black text-white uppercase mb-10">The Tech Stack</h2>
      <div class="grid grid-cols-2 md:grid-cols-3 gap-6">
        <div class="glass-card rounded-xl p-6 border-white/5 hover:border-accent/30 transition-all">
          <div class="flex items-center justify-between mb-4">
            <h4 class="font-display font-black text-white uppercase">Python</h4>
            <span class="px-2 py-1 bg-emerald-500/10 border border-emerald-500/20 rounded text-[7px] font-mono text-emerald-400 uppercase">Core</span>
          </div>
          <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest">Backend automation, heavy data streaming, and AI pipeline orchestration.</p>
        </div>
        <div class="glass-card rounded-xl p-6 border-white/5 hover:border-primary/30 transition-all">
          <div class="flex items-center justify-between mb-4">
            <h4 class="font-display font-black text-white uppercase">AI Agents</h4>
            <span class="px-2 py-1 bg-primary/10 border border-primary/20 rounded text-[7px] font-mono text-primary uppercase">Engine</span>
          </div>
          <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest">LLM automation, autonomous decision-making, contextual engineering.</p>
        </div>
        <div class="glass-card rounded-xl p-6 border-white/5 hover:border-violet-500/30 transition-all">
          <div class="flex items-center justify-between mb-4">
            <h4 class="font-display font-black text-white uppercase">WordPress</h4>
            <span class="px-2 py-1 bg-violet-500/10 border border-violet-500/20 rounded text-[7px] font-mono text-violet-400 uppercase">Scale</span>
          </div>
          <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest">Successful business integrations, and custom engineering.</p>
        </div>
        <div class="glass-card rounded-xl p-6 border-white/5 hover:border-accent/30 transition-all">
          <div class="flex items-center justify-between mb-4">
            <h4 class="font-display font-black text-white uppercase">Frontend</h4>
            <span class="px-2 py-1 bg-accent/10 border border-accent/20 rounded text-[7px] font-mono text-accent uppercase">Visual</span>
          </div>
          <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest">Tailwind, accounting-side audits, and infrastructure that feels like GSAP.</p>
        </div>
        <div class="glass-card rounded-xl p-6 border-white/5 hover:border-amber-500/30 transition-all">
          <div class="flex items-center justify-between mb-4">
            <h4 class="font-display font-black text-white uppercase">DevOps</h4>
            <span class="px-2 py-1 bg-amber-500/10 border border-amber-500/20 rounded text-[7px] font-mono text-amber-400 uppercase">Infra</span>
          </div>
          <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest">Automated CI/CD pipelines, cloud infrastructure, and performance ops.</p>
        </div>
        <div class="glass-card rounded-xl p-6 border-white/5 hover:border-emerald-500/30 transition-all">
          <div class="flex items-center justify-between mb-4">
            <h4 class="font-display font-black text-white uppercase">Game Dev</h4>
            <span class="px-2 py-1 bg-emerald-500/10 border border-emerald-500/20 rounded text-[7px] font-mono text-emerald-400 uppercase">XP</span>
          </div>
          <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest">High fidelity GSAP work. Platforms. Partner to hundreds of gaming interfaces.</p>
        </div>
      </div>
    </div>

    <!-- Who Are You -->
    <div class="mb-16">
      <h2 class="text-3xl font-display font-black text-white uppercase mb-4 text-center">WHO ARE YOU?</h2>
      <p class="text-center text-white/30 font-mono text-[10px] uppercase tracking-widest mb-12">Choose your path and tell me why you should join the mission.</p>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="glass-card rounded-2xl overflow-hidden border-accent/20 hover:border-accent/50 transition-all group">
          <div class="h-48 bg-gradient-to-br from-accent/20 to-primary/10 flex items-center justify-center">
            <span class="material-symbols-outlined text-accent/40 text-8xl group-hover:scale-110 transition-all">rocket_launch</span>
          </div>
          <div class="p-8">
            <h3 class="text-xl font-display font-black text-white uppercase mb-3">The Student</h3>
            <p class="text-white/40 text-[10px] font-mono uppercase tracking-widest leading-relaxed mb-6">You're a self-teaching developer. You're here because it's down-to-earth, and you want to build things on your own.</p>
            <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-accent/30 rounded-lg text-accent font-mono text-[9px] uppercase tracking-widest hover:bg-accent hover:text-black transition-all">SELECT_PATH</button>
          </div>
        </div>
        <div class="glass-card rounded-2xl overflow-hidden border-violet-500/20 hover:border-violet-500/50 transition-all group">
          <div class="h-48 bg-gradient-to-br from-violet-500/20 to-primary/10 flex items-center justify-center">
            <span class="material-symbols-outlined text-violet-400/40 text-8xl group-hover:scale-110 transition-all">swap_horiz</span>
          </div>
          <div class="p-8">
            <h3 class="text-xl font-display font-black text-white uppercase mb-3">The Switcher</h3>
            <p class="text-white/40 text-[10px] font-mono uppercase tracking-widest leading-relaxed mb-6">You're transitioning to something you love. You're bored of your six figure corporate desk and you want to build things.</p>
            <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-violet-500/30 rounded-lg text-violet-400 font-mono text-[9px] uppercase tracking-widest hover:bg-violet-500 hover:text-black transition-all">SELECT_PATH</button>
          </div>
        </div>
        <div class="glass-card rounded-2xl overflow-hidden border-amber-500/20 hover:border-amber-500/50 transition-all group">
          <div class="h-48 bg-gradient-to-br from-amber-500/20 to-orange-500/10 flex items-center justify-center">
            <span class="material-symbols-outlined text-amber-400/40 text-8xl group-hover:scale-110 transition-all">local_fire_department</span>
          </div>
          <div class="p-8">
            <h3 class="text-xl font-display font-black text-white uppercase mb-3">The Enthusiast</h3>
            <p class="text-white/40 text-[10px] font-mono uppercase tracking-widest leading-relaxed mb-6">Not a newcomer, just an enthusiast. You want to use game mechanics and tech to solve real-world problems.</p>
            <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-amber-500/30 rounded-lg text-amber-400 font-mono text-[9px] uppercase tracking-widest hover:bg-amber-500 hover:text-black transition-all">SELECT PATH</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
'''
build('work-with-me.html', 'Work With Me', work)
print("Part 4 done.")
