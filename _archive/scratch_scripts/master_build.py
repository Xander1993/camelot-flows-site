import json, os, re

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
    print(f"  ✓ {filename}")

# ── HOME PAGE ─────────────────────────────────────────────────────────────────
# Extract body from code_v2.html (everything from </nav> to last </footer>)
with open(os.path.join(BASE, 'code_v2.html'), 'r', encoding='utf-8') as f:
    cv2 = f.read()

m = re.search(r'(<main[\s\S]*?</main>)', cv2)
home_main = m.group(1) if m else '<main><h1>Home</h1></main>'

# Also grab any additional sections after </main> before <footer
extra_m = re.search(r'</main>([\s\S]*?)<footer', cv2)
home_extra = extra_m.group(1).strip() if extra_m else ''

build('index.html', 'Digital Architect', home_main + '\n' + home_extra)

# ── ABOUT PAGE ────────────────────────────────────────────────────────────────
about = '''
<main class="pt-36 pb-24 overflow-hidden">
  <section class="max-w-7xl mx-auto px-8">
    <!-- Hero -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center mb-32">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 border border-primary/20 mb-8">
          <span class="w-1.5 h-1.5 rounded-full bg-primary animate-pulse"></span>
          <span class="text-[9px] font-mono text-primary font-bold tracking-[0.3em] uppercase">Initialize_Identity_Protocol</span>
        </div>
        <h1 class="text-6xl md:text-8xl font-display font-black text-white uppercase tracking-tighter leading-none mb-8">
          I Build<br/><span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-accent">Digital<br/>Kingdoms.</span>
        </h1>
        <p class="text-white/50 text-base leading-relaxed mb-10 max-w-lg font-mono text-[11px] uppercase tracking-widest">
          A tech visionary from Chisinau, Moldova — architecting the intersection of performance, AI, and user experience. Father of Arthur, builder of futures.
        </p>
        <div class="flex flex-wrap gap-4">
          <button onclick="window.location.href='work-with-me.html'" class="px-8 py-3 bg-accent text-black font-mono font-black text-[10px] uppercase tracking-widest rounded-lg hover:scale-105 transition-all">Work Manifest</button>
          <button onclick="window.location.href='merlin.html'" class="px-8 py-3 border border-white/10 text-white font-mono font-black text-[10px] uppercase tracking-widest rounded-lg hover:bg-white/5 transition-all">Read Log</button>
        </div>
      </div>
      <div class="relative">
        <div class="glass-card rounded-2xl overflow-hidden aspect-video flex items-center justify-center border-primary/20">
          <div class="text-center p-12">
            <span class="material-symbols-outlined text-primary text-6xl mb-4 block opacity-40">account_circle</span>
            <p class="text-white/20 font-mono text-[9px] uppercase tracking-widest">PROJECT_LEAD: ALEX B.</p>
            <p class="text-white/10 font-mono text-[8px] uppercase tracking-widest mt-1">INSERT VISUAL DATA BLOCK</p>
          </div>
        </div>
        <div class="absolute -bottom-6 -right-6 glass-card rounded-xl p-4 border-accent/20">
          <div class="flex items-center gap-3">
            <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
            <span class="font-mono text-[9px] text-white/60 uppercase tracking-widest">Status: Forging Infrastructure</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Timeline -->
    <div class="mb-32">
      <h2 class="text-4xl font-display font-black text-white uppercase text-center mb-4">The Chronology</h2>
      <div class="h-px w-24 bg-gradient-to-r from-primary to-accent mx-auto mb-20"></div>
      <div class="relative">
        <div class="absolute left-1/2 top-0 bottom-0 w-px bg-gradient-to-b from-primary/50 via-accent/30 to-transparent -translate-x-1/2 hidden md:block"></div>
        <div class="space-y-16">
          <!-- Item 1 -->
          <div class="relative flex flex-col md:flex-row items-center gap-8">
            <div class="md:w-[45%] text-right pr-12">
              <div class="glass-card rounded-xl p-6 border-primary/20 inline-block text-left">
                <span class="text-[9px] font-mono text-primary uppercase tracking-widest block mb-2">2018 — 2020</span>
                <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Foundation Period</h3>
                <p class="text-white/40 text-[10px] font-mono leading-relaxed uppercase">Mastering the architecture of full-stack development and cloud from blank canvas.</p>
                <div class="mt-3 flex gap-2"><span class="px-2 py-1 bg-primary/10 border border-primary/20 rounded text-[8px] font-mono text-primary uppercase">node.js / react</span></div>
              </div>
            </div>
            <div class="w-4 h-4 rounded-full bg-primary border-2 border-obsidian shadow-[0_0_15px_rgba(79,70,229,0.8)] z-10 shrink-0"></div>
            <div class="md:w-[45%] pl-12"></div>
          </div>
          <!-- Item 2 -->
          <div class="relative flex flex-col md:flex-row items-center gap-8">
            <div class="md:w-[45%] text-right pr-12"></div>
            <div class="w-4 h-4 rounded-full bg-violet-500 border-2 border-obsidian shadow-[0_0_15px_rgba(139,92,246,0.8)] z-10 shrink-0"></div>
            <div class="md:w-[45%] pl-12">
              <div class="glass-card rounded-xl p-6 border-violet-500/20 inline-block text-left">
                <span class="text-[9px] font-mono text-violet-400 uppercase tracking-widest block mb-2">2020 — 2022</span>
                <h3 class="text-lg font-display font-bold text-white uppercase mb-2">Scaling Frontiers</h3>
                <p class="text-white/40 text-[10px] font-mono leading-relaxed uppercase">Architecting systems sending millions while maintaining surgical precision.</p>
                <div class="mt-3 flex gap-2"><span class="px-2 py-1 bg-violet-500/10 border border-violet-500/20 rounded text-[8px] font-mono text-violet-400 uppercase">python / AI</span></div>
              </div>
            </div>
          </div>
          <!-- Item 3 -->
          <div class="relative flex flex-col md:flex-row items-center gap-8">
            <div class="md:w-[45%] text-right pr-12">
              <div class="glass-card rounded-xl p-6 border-accent/20 inline-block text-left">
                <span class="text-[9px] font-mono text-accent uppercase tracking-widest block mb-2">2023 — NOW</span>
                <h3 class="text-lg font-display font-bold text-white uppercase mb-2">AI Integration Era</h3>
                <p class="text-white/40 text-[10px] font-mono leading-relaxed uppercase">Fusing agentic AI with architectural decisions and real-time automation.</p>
                <div class="mt-3 flex gap-2"><span class="px-2 py-1 bg-accent/10 border border-accent/20 rounded text-[8px] font-mono text-accent uppercase">AI / Make / GSAP</span></div>
              </div>
            </div>
            <div class="w-4 h-4 rounded-full bg-accent border-2 border-obsidian shadow-[0_0_15px_rgba(0,255,255,0.8)] z-10 shrink-0"></div>
            <div class="md:w-[45%] pl-12"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Philosophy -->
    <div>
      <h2 class="text-4xl font-display font-black text-white uppercase text-center mb-4">The Philosophy</h2>
      <div class="h-px w-24 bg-gradient-to-r from-primary to-accent mx-auto mb-16"></div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="glass-card rounded-2xl p-10 border-primary/20 hover:border-primary/50 transition-all group">
          <span class="material-symbols-outlined text-primary text-3xl mb-6 block">verified</span>
          <h3 class="text-xl font-display font-bold text-white uppercase mb-4">I Tell the Truth</h3>
          <p class="text-white/40 text-[11px] font-mono leading-relaxed uppercase tracking-widest">Radical honesty in technical debt. I file deploy notes, not spin. The foundation is accountable before the first stone is laid.</p>
        </div>
        <div class="glass-card rounded-2xl p-10 border-violet-500/20 hover:border-violet-500/50 transition-all group">
          <span class="material-symbols-outlined text-violet-400 text-3xl mb-6 block">construction</span>
          <h3 class="text-xl font-display font-bold text-white uppercase mb-4">I Build, Not Rent</h3>
          <p class="text-white/40 text-[11px] font-mono leading-relaxed uppercase tracking-widest">True ownership is a philosophy. I use custom-built solutions; never cookie-cutter tech because the thinking of the team elevates the entirety of the deployment.</p>
        </div>
        <div class="glass-card rounded-2xl p-10 border-accent/20 hover:border-accent/50 transition-all group">
          <span class="material-symbols-outlined text-accent text-3xl mb-6 block">psychology</span>
          <h3 class="text-xl font-display font-bold text-white uppercase mb-4">AI Is My Daily Toolkit</h3>
          <p class="text-white/40 text-[11px] font-mono leading-relaxed uppercase tracking-widest">Humans as co-pilots. I leverage advanced neural patterns to accelerate my strategy. My AI workflow is the compass, positioning a human intelligence overhead.</p>
        </div>
      </div>
    </div>
  </section>
</main>
'''
build('about.html', 'About', about)

# ── CONTACT PAGE ──────────────────────────────────────────────────────────────
contact = '''
<main class="pt-36 pb-24 overflow-hidden">
  <div class="max-w-3xl mx-auto px-8">
    <div class="text-center mb-16">
      <h1 class="text-6xl md:text-8xl font-display font-black text-white uppercase tracking-tighter leading-none mb-4">
        CONTACT_<span class="text-accent">INMATE</span>
      </h1>
      <p class="text-white/30 font-mono text-[10px] uppercase tracking-[0.4em]">SECURE ENCRYPTED UPLINK ESTABLISHED</p>
    </div>
    <div class="glass-card rounded-2xl border-accent/20 p-10">
      <div class="grid grid-cols-2 gap-6 mb-6">
        <div>
          <label class="block text-[9px] font-mono text-accent uppercase tracking-widest mb-2">&#9632; IDENTITY_NAME</label>
          <input type="text" placeholder="ENTER_NAME..." class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 font-mono text-sm text-white placeholder:text-white/20 focus:outline-none focus:border-accent/50 transition-all"/>
        </div>
        <div>
          <label class="block text-[9px] font-mono text-accent uppercase tracking-widest mb-2">&#9632; COMMS_CHANNEL</label>
          <input type="email" placeholder="NAME@NETWORK.COM" class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 font-mono text-sm text-white placeholder:text-white/20 focus:outline-none focus:border-accent/50 transition-all"/>
        </div>
      </div>
      <div class="mb-6">
        <label class="block text-[9px] font-mono text-accent uppercase tracking-widest mb-2">&#9632; MISSION_OBJECTIVE</label>
        <select class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 font-mono text-sm text-white/60 focus:outline-none focus:border-accent/50 transition-all">
          <option value="">SELECT_MISSION_TYPE</option>
          <option>Web Architecture (The Forge)</option>
          <option>AI Automation (Alchemist Scripts)</option>
          <option>Growth Protocol (Marketing)</option>
          <option>Vanguard Protection (Maintenance)</option>
          <option>Full Stack Initiative</option>
        </select>
      </div>
      <div class="mb-8">
        <label class="block text-[9px] font-mono text-accent uppercase tracking-widest mb-2">&#9632; DETAILED_DIRECTIVE</label>
        <textarea rows="6" placeholder="ENCRYPT_YOUR_MESSAGE_HERE..." class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 font-mono text-sm text-white placeholder:text-white/20 focus:outline-none focus:border-accent/50 transition-all resize-none"></textarea>
      </div>
      <button class="w-full py-4 bg-accent text-black font-mono font-black text-sm uppercase tracking-widest rounded-lg hover:scale-[1.02] transition-all shadow-[0_0_30px_rgba(0,255,255,0.3)]">
        INITIATE_PROTOCOL
      </button>
      <div class="mt-6 flex justify-between text-[8px] font-mono text-white/20 uppercase tracking-widest">
        <span>ENCRYPTION: AES-256-GCM</span>
        <span>LOCATION: UNKNOWN_SECTOR_7</span>
        <span>PULSE: STABLE</span>
      </div>
    </div>
    <div class="grid grid-cols-3 gap-4 mt-8">
      <div class="glass-card rounded-xl p-4 text-center border-white/5">
        <span class="material-symbols-outlined text-accent text-lg mb-1 block">wifi</span>
        <p class="text-[8px] font-mono text-white/30 uppercase tracking-widest">REMOTE_ACCESS_ONLY</p>
      </div>
      <div class="glass-card rounded-xl p-4 text-center border-white/5">
        <span class="material-symbols-outlined text-violet-400 text-lg mb-1 block">schedule</span>
        <p class="text-[8px] font-mono text-white/30 uppercase tracking-widest">UPTIME 24/7/365</p>
      </div>
      <div class="glass-card rounded-xl p-4 text-center border-white/5">
        <span class="material-symbols-outlined text-emerald-400 text-lg mb-1 block">bolt</span>
        <p class="text-[8px] font-mono text-white/30 uppercase tracking-widest">RESPONSE &lt;2H</p>
      </div>
    </div>
  </div>
</main>
'''
build('contact.html', 'Contact', contact)

print("Part 1 done.")
