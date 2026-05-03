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

# ── FOR AGENCIES ──────────────────────────────────────────────────────────────
agencies = '''
<main class="pt-36 pb-24">
  <section class="max-w-7xl mx-auto px-8">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center mb-24">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 border border-primary/20 mb-8">
          <span class="w-1.5 h-1.5 rounded-full bg-primary animate-pulse"></span>
          <span class="text-[9px] font-mono text-primary font-bold tracking-[0.3em] uppercase">Available for co-development</span>
        </div>
        <h1 class="text-5xl md:text-7xl font-display font-black text-white uppercase tracking-tighter leading-none mb-8">
          Your Clients<br/>Deserve Better.<br/><span class="text-accent">Let Me Help You<br/>Deliver.</span>
        </h1>
        <p class="text-white/50 text-sm leading-relaxed mb-10 font-mono">High-end development partnership for forward-thinking agencies. Specialised in Frontend Architecture and AI Implementation.</p>
        <div class="flex flex-wrap gap-4">
          <button onclick="window.location.href='contact.html'" class="px-8 py-3 bg-accent text-black font-mono font-black text-[10px] uppercase tracking-widest rounded-lg hover:scale-105 transition-all">Book a Discovery Call</button>
          <button onclick="window.location.href='case-studies.html'" class="px-8 py-3 border border-white/10 text-white font-mono font-black text-[10px] uppercase tracking-widest rounded-lg hover:bg-white/5 transition-all">View Work</button>
        </div>
      </div>
      <div class="glass-card rounded-2xl overflow-hidden border-accent/20">
        <div class="bg-black/60 rounded-2xl p-2">
          <div class="aspect-video bg-gradient-to-br from-primary/10 to-accent/5 rounded-xl flex items-center justify-center relative overflow-hidden">
            <span class="material-symbols-outlined text-accent/20 text-[120px]">display_settings</span>
            <div class="absolute bottom-6 right-6 font-mono text-[8px] text-white/20 uppercase space-y-1">
              <div>&#9632; NODE: 212.168.4.1</div>
              <div>&#9632; ITEM 2: NODE 28</div>
              <div>&#9632; ITEM 3: NOTE: WEB</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specialized services -->
    <h2 class="text-3xl font-display font-black text-white uppercase text-center mb-12">Specialized Services for Agencies</h2>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-24">
      <div class="glass-card rounded-2xl p-6 border-white/5 hover:border-accent/30 transition-all text-center group">
        <span class="material-symbols-outlined text-accent text-3xl mb-4 block">architecture</span>
        <h4 class="font-display font-black text-white uppercase text-sm mb-3">Frontend Architecture</h4>
        <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest leading-relaxed">Reconstruct a design system with a custom-built toolkit for seamless performance.</p>
        <button class="mt-4 text-accent font-mono text-[9px] uppercase tracking-widest hover:opacity-70 transition-all">More Info</button>
      </div>
      <div class="glass-card rounded-2xl p-6 border-white/5 hover:border-primary/30 transition-all text-center group">
        <span class="material-symbols-outlined text-primary text-3xl mb-4 block">psychology</span>
        <h4 class="font-display font-black text-white uppercase text-sm mb-3">AI Integration</h4>
        <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest leading-relaxed">LLM automation, autonomous workflows, and intelligent lead automation.</p>
        <button class="mt-4 text-primary font-mono text-[9px] uppercase tracking-widest hover:opacity-70 transition-all">More Info</button>
      </div>
      <div class="glass-card rounded-2xl p-6 border-white/5 hover:border-amber-500/30 transition-all text-center group">
        <span class="material-symbols-outlined text-amber-500 text-3xl mb-4 block">trending_up</span>
        <h4 class="font-display font-black text-white uppercase text-sm mb-3">SEO & Speed</h4>
        <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest leading-relaxed">Our service takes your clients to the top of search and keeps you there.</p>
        <button class="mt-4 text-amber-500 font-mono text-[9px] uppercase tracking-widest hover:opacity-70 transition-all">More Info</button>
      </div>
      <div class="glass-card rounded-2xl p-6 border-white/5 hover:border-violet-500/30 transition-all text-center group">
        <span class="material-symbols-outlined text-violet-400 text-3xl mb-4 block">build</span>
        <h4 class="font-display font-black text-white uppercase text-sm mb-3">DevOps</h4>
        <p class="text-white/30 text-[10px] font-mono uppercase tracking-widest leading-relaxed">Automated deployment pipelines so your team's productivity levels expand.</p>
        <button class="mt-4 text-violet-400 font-mono text-[9px] uppercase tracking-widest hover:opacity-70 transition-all">More Info</button>
      </div>
    </div>

    <!-- Why agencies choose me -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
      <div>
        <div class="text-[9px] font-mono text-accent uppercase tracking-widest mb-4">THE VALUE PROP</div>
        <h2 class="text-4xl font-display font-black text-white uppercase mb-8">Why Agencies Choose Me</h2>
        <p class="text-white/40 font-mono text-[11px] uppercase tracking-widest leading-relaxed mb-8">Act as an extension of your creative team, handling the complex technical weight so you can focus on strategy and design.</p>
        <ul class="space-y-6">
          <li class="flex items-start gap-4">
            <span class="material-symbols-outlined text-accent mt-1">check_circle</span>
            <div><h5 class="text-white font-mono font-bold text-sm uppercase mb-1">White-label output</h5><p class="text-white/30 text-[10px] font-mono uppercase tracking-widest">Professional communication directly with your clients or purely behind the scenes.</p></div>
          </li>
          <li class="flex items-start gap-4">
            <span class="material-symbols-outlined text-accent mt-1">check_circle</span>
            <div><h5 class="text-white font-mono font-bold text-sm uppercase mb-1">Rock-bottom delivery</h5><p class="text-white/30 text-[10px] font-mono uppercase tracking-widest">No scope creep, no excuses. Ship, iterate, no shortcuts.</p></div>
          </li>
          <li class="flex items-start gap-4">
            <span class="material-symbols-outlined text-accent mt-1">check_circle</span>
            <div><h5 class="text-white font-mono font-bold text-sm uppercase mb-1">Architectural excellence</h5><p class="text-white/30 text-[10px] font-mono uppercase tracking-widest">Even recommend code that your own developers won't love.</p></div>
          </li>
        </ul>
      </div>
      <div class="glass-card rounded-2xl p-8 border-white/5">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-10 h-10 rounded-full bg-primary/20 border border-primary/40 flex items-center justify-center font-display font-black text-sm text-primary">M</div>
          <div><p class="font-mono font-bold text-white text-sm">MirrorOne</p><p class="text-[9px] font-mono text-white/30 uppercase tracking-widest">Agency Director</p></div>
        </div>
        <p class="text-white/60 font-mono text-[11px] leading-relaxed italic">"Working with Camelot Flows elevated our technical delivery by orders of magnitude. Our clients are raving about the performance improvements and the AI-integrated workflows shipped on time."</p>
      </div>
    </div>
  </section>
</main>
'''
build('for-agencies.html', 'For Agencies', agencies)

# ── SERVICE: AUTOMATION ───────────────────────────────────────────────────────
automation = '''
<main class="pt-36 pb-24">
  <section class="max-w-7xl mx-auto px-8">
    <div class="mb-6">
      <span class="text-[9px] font-mono text-violet-400 uppercase tracking-widest">✦ A FOUNDATIONAL RITUAL</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-display font-black text-white uppercase tracking-tighter leading-none mb-6">
      Alchemist Scripts:<br/><span class="text-transparent bg-clip-text bg-gradient-to-r from-violet-400 to-fuchsia-500">Turning Logic Into Gold</span>
    </h1>
    <p class="text-white/50 max-w-2xl font-mono text-[11px] uppercase tracking-widest leading-relaxed mb-12">A sorcery-grade workflow optimization for your digital kingdom. We bridge the gap between complex tasks and seamless automation.</p>
    <div class="flex gap-4 mb-16">
      <span class="px-3 py-2 bg-violet-500/10 border border-violet-500/20 rounded text-[9px] font-mono text-violet-400 uppercase tracking-widest">Make.com</span>
      <span class="px-3 py-2 bg-white/5 border border-white/10 rounded text-[9px] font-mono text-white/40 uppercase tracking-widest">n8n</span>
      <span class="px-3 py-2 bg-white/5 border border-white/10 rounded text-[9px] font-mono text-white/40 uppercase tracking-widest">Airtable</span>
    </div>
    <!-- Terminal -->
    <div class="glass-card rounded-2xl p-2 mb-20 border-violet-500/20">
      <div class="bg-black rounded-xl p-8">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-3 h-3 rounded-full bg-red-500"></div><div class="w-3 h-3 rounded-full bg-yellow-500"></div><div class="w-3 h-3 rounded-full bg-green-500"></div>
          <span class="ml-4 text-[9px] font-mono text-white/20 uppercase tracking-widest">alchemist_scripts.run — trigger —input_path "event_schemas"</span>
        </div>
        <div class="space-y-2 font-mono text-[12px]">
          <p><span class="text-violet-400">[10:29:02]</span> <span class="text-white/60">artifact_collect_artifact —repo->{org}/{project} —sha</span></p>
          <p><span class="text-violet-400">[10:29:03]</span> <span class="text-emerald-400">Initializing Running Alchemist Run-Type...</span></p>
          <p><span class="text-violet-400">[10:29:04]</span> <span class="text-white/60">Loading Running framework 8.2.1 Iteration...</span></p>
          <p><span class="text-violet-400">[10:29:06]</span> <span class="text-white/60">PUSH: Splitting running complex tasks from —Alch...</span></p>
          <p><span class="text-violet-400">[10:29:07]</span> <span class="text-emerald-400">MISSION: Initializing camelot_flows_automation</span></p>
          <p><span class="text-white/20">Looking for target... <span class="animate-pulse">▌</span></span></p>
        </div>
      </div>
    </div>
    <!-- Tiers -->
    <h2 class="text-3xl font-display font-black text-white uppercase text-center mb-12">Choose Your Tier</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-20">
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-violet-500/30 transition-all">
        <span class="text-[9px] font-mono text-white/30 uppercase tracking-widest mb-4 block">Initiate</span>
        <p class="text-white/40 text-[10px] font-mono uppercase mb-6">Automate the repetitive, liberate your kingdom.</p>
        <div class="text-5xl font-display font-black text-white mb-8">$149<span class="text-white/30 text-base font-mono">/mo</span></div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-violet-400 text-sm">check</span> 5 Micro-Automations</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-violet-400 text-sm">check</span> Workflow Expressions</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-violet-400 text-sm">check</span> Support via Ritual</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-violet-500/30 rounded-xl text-violet-400 font-mono font-black text-[9px] uppercase tracking-widest hover:bg-violet-500/10 transition-all">BEGIN RITUAL</button>
      </div>
      <div class="glass-card rounded-3xl p-10 border-violet-500/40 shadow-[0_0_40px_rgba(139,92,246,0.2)] scale-105 relative">
        <span class="absolute top-4 right-4 px-2 py-1 bg-violet-500/20 border border-violet-500/40 rounded text-[7px] font-mono text-violet-400 uppercase">BEST VALUE</span>
        <span class="text-[9px] font-mono text-violet-400 uppercase tracking-widest mb-4 block">Adept</span>
        <p class="text-white/40 text-[10px] font-mono uppercase mb-6">Complex workflows serving digital kingdoms.</p>
        <div class="text-5xl font-display font-black text-white mb-8">$399<span class="text-white/30 text-base font-mono">/mo</span></div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-violet-400 text-sm">check</span> 15 Micro-Automations</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-violet-400 text-sm">check</span> Custom Algo Scripts</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-violet-400 text-sm">check</span> API Integrations</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-violet-400 text-sm">check</span> 48hr Response Time</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 bg-violet-500 text-white rounded-xl font-mono font-black text-[9px] uppercase tracking-widest hover:scale-105 transition-all shadow-[0_0_20px_rgba(139,92,246,0.4)]">SUMMON POWER</button>
      </div>
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-fuchsia-500/30 transition-all">
        <span class="text-[9px] font-mono text-white/30 uppercase tracking-widest mb-4 block">Master</span>
        <p class="text-white/40 text-[10px] font-mono uppercase mb-6">Unlimited automation management for large domains.</p>
        <div class="text-5xl font-display font-black text-white mb-8">$899<span class="text-white/30 text-base font-mono">/mo</span></div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-fuchsia-400 text-sm">check</span> Unlimited Automations</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-fuchsia-400 text-sm">check</span> Dedicated Automation</li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-fuchsia-400 text-sm">check</span> SLA Guarantee</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-fuchsia-500/30 rounded-xl text-fuchsia-400 font-mono font-black text-[9px] uppercase tracking-widest hover:bg-fuchsia-500/10 transition-all">FULL MASTERY</button>
      </div>
    </div>
    <!-- CTA -->
    <div class="text-center glass-card rounded-3xl p-16 border-violet-500/20">
      <h2 class="text-4xl font-display font-black text-white uppercase mb-4">Ready to transmute your workflow?</h2>
      <button onclick="window.location.href='contact.html'" class="mt-8 px-12 py-4 bg-violet-500 text-white font-mono font-black text-sm uppercase tracking-widest rounded-full hover:scale-105 transition-all shadow-[0_0_30px_rgba(139,92,246,0.5)] flex items-center gap-3 mx-auto">
        <span class="material-symbols-outlined">bolt</span> SUMMON AUTOMATIONS ✦
      </button>
      <p class="text-white/20 font-mono text-[9px] uppercase tracking-widest mt-6">*We want to talk first, but this is the easiest way to start.</p>
    </div>
  </section>
</main>
'''
build('service-automation.html', 'Alchemist Scripts', automation)
print("Part 5 done.")
