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

# ── SERVICE: MARKETING ────────────────────────────────────────────────────────
marketing = '''
<main class="pt-36 pb-24">
  <section class="max-w-7xl mx-auto px-8">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start mb-24">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/20 mb-6">
          <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
          <span class="text-[9px] font-mono text-amber-400 uppercase tracking-widest">STATUS: OPTIMAL EXECUTION</span>
        </div>
        <h1 class="text-5xl md:text-7xl font-display font-black text-white uppercase tracking-tighter leading-none mb-4">
          Growth<br/>Protocol:<br/><span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-500">10x Acquisition</span>
        </h1>
        <p class="text-white/50 font-mono text-[11px] uppercase tracking-widest leading-relaxed mb-10">Hyper-futuristic digital growth strategies for the next generation of tech. Precision-engineered acquisition systems optimised for scale and dominance.</p>
        <div class="flex gap-4">
          <button onclick="window.location.href='contact.html'" class="px-8 py-3 bg-amber-500 text-black font-mono font-black text-[10px] uppercase tracking-widest rounded-lg hover:scale-105 transition-all">INITIATE CAMPAIGN</button>
          <button class="px-8 py-3 border border-white/10 text-white font-mono font-black text-[10px] uppercase tracking-widest rounded-lg hover:bg-white/5 transition-all">Size Protocol</button>
        </div>
      </div>
      <div class="glass-card rounded-2xl p-8 border-amber-500/20">
        <div class="text-right font-mono text-[9px] text-amber-400 mb-4 uppercase tracking-widest">Analytics +420.69%</div>
        <div class="h-32 w-full relative overflow-hidden rounded-lg bg-amber-500/5 border border-amber-500/10 mb-4">
          <svg class="w-full h-full" viewBox="0 0 400 100" preserveAspectRatio="none">
            <path d="M0,90 C60,80 120,50 180,40 S280,10 400,5" fill="rgba(245,158,11,0.1)" stroke="#f59e0b" stroke-width="2"/>
          </svg>
        </div>
        <div class="grid grid-cols-3 gap-4 text-center">
          <div><div class="text-2xl font-display font-black text-amb-400 text-amber-400">10x</div><p class="text-[8px] font-mono text-white/30 uppercase">Growth Rate</p></div>
          <div><div class="text-2xl font-display font-black text-white">96%</div><p class="text-[8px] font-mono text-white/30 uppercase">Retention</p></div>
          <div><div class="text-2xl font-display font-black text-emerald-400">2.1M</div><p class="text-[8px] font-mono text-white/30 uppercase">Reach</p></div>
        </div>
      </div>
    </div>

    <!-- Retainer Tiers -->
    <h2 class="text-3xl font-display font-black text-white uppercase text-center mb-12">RETAINER TIERS</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-20">
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-amber-500/30 transition-all">
        <span class="text-[9px] font-mono text-white/30 uppercase mb-2 block">Scout</span>
        <p class="text-white/30 text-[10px] font-mono uppercase mb-4">Entry-level acquisition setup. Perfect for the early-stage mission.</p>
        <div class="text-5xl font-display font-black text-white mb-4">$199<span class="text-white/30 text-base font-mono">/mo</span></div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> 4 x Social Posts</li>
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> Weekly Insight Reports</li>
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> 1 Paid Ad Set</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-amber-500/30 rounded-xl text-amber-400 font-mono font-black text-[9px] uppercase tracking-widest hover:bg-amber-500/10 transition-all">SELECT_PHASE</button>
      </div>
      <div class="glass-card rounded-3xl p-10 border-amber-500/40 shadow-[0_0_40px_rgba(245,158,11,0.2)] scale-105 relative">
        <span class="absolute top-4 right-4 px-2 py-1 bg-amber-500/20 border border-amber-500/40 rounded text-[7px] font-mono text-amber-400 uppercase">KNIGHT-ERRANT</span>
        <span class="text-[9px] font-mono text-amber-400 uppercase mb-2 block">Knight-Errant</span>
        <p class="text-white/30 text-[10px] font-mono uppercase mb-4">Full-throttle marketing, full-blown customisation targeting.</p>
        <div class="text-5xl font-display font-black text-white mb-4">$599<span class="text-white/30 text-base font-mono">/mo</span></div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> 16 x Social Posts</li>
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> Weekly SEO Reports</li>
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> 3 Paid Ad Sets</li>
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> Email Series 4/mo</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 bg-amber-500 text-black rounded-xl font-mono font-black text-[9px] uppercase tracking-widest hover:scale-105 transition-all">INITIATE DEPLOYMENT</button>
      </div>
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-orange-500/30 transition-all">
        <span class="text-[9px] font-mono text-white/30 uppercase mb-2 block">Grandmaster</span>
        <p class="text-white/30 text-[10px] font-mono uppercase mb-4">Total market annihilation. For campaigns requiring custom-built pages.</p>
        <div class="text-5xl font-display font-black text-white mb-4">$1,499<span class="text-white/30 text-base font-mono">/mo</span></div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="text-orange-400">✓</span> Unlimited Content</li>
          <li class="flex items-center gap-2"><span class="text-orange-400">✓</span> Global Ad Networks</li>
          <li class="flex items-center gap-2"><span class="text-orange-400">✓</span> Personal CMO Access</li>
          <li class="flex items-center gap-2"><span class="text-orange-400">✓</span> Monthly OBR Sessions</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-orange-500/30 rounded-xl text-orange-400 font-mono font-black text-[9px] uppercase tracking-widest hover:bg-orange-500/10 transition-all">CONTACT_STRATEGIST</button>
      </div>
    </div>
    <!-- Final CTA -->
    <div class="glass-card rounded-3xl p-16 border-amber-500/20 text-center">
      <h2 class="text-4xl font-display font-black text-white uppercase mb-4">READY FOR SYSTEM OVERDRIVE?</h2>
      <p class="text-white/40 font-mono text-[11px] uppercase tracking-widest mb-8 max-w-xl mx-auto">The protocol is ready. We take tactical steps to ensure maximum acquisition power for every partner.</p>
      <button onclick="window.location.href='contact.html'" class="px-12 py-4 bg-amber-500 text-black font-mono font-black text-sm uppercase tracking-widest rounded-full hover:scale-105 transition-all shadow-[0_0_30px_rgba(245,158,11,0.4)] flex items-center gap-3 mx-auto">
        <span class="material-symbols-outlined">rocket_launch</span> INITIATE CAMPAIGN
      </button>
    </div>
  </section>
</main>
'''
build('service-marketing.html', 'Growth Protocol', marketing)

# ── SERVICE: MAINTENANCE ──────────────────────────────────────────────────────
maintenance = '''
<main class="pt-36 pb-24">
  <section class="max-w-7xl mx-auto px-8">
    <div class="text-center mb-20">
      <h1 class="text-5xl md:text-7xl font-display font-black text-white uppercase tracking-tighter leading-none mb-6">
        Vanguard Protection:<br/><span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-400">Guardian of Your Kingdom</span>
      </h1>
      <p class="text-white/50 font-mono text-[11px] uppercase tracking-widest max-w-2xl mx-auto">Premium fleet maintenance and cyber-sentinel support for elite technology portfolios. Your digital assets, under our absolute watch.</p>
    </div>
    <!-- Tiers -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-20">
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-emerald-500/30 transition-all">
        <div class="flex items-center justify-between mb-6">
          <span class="text-[9px] font-mono text-white/30 uppercase">Sentry</span>
          <span class="px-2 py-1 bg-emerald-500/10 border border-emerald-500/20 rounded text-[7px] font-mono text-emerald-400 uppercase">Active</span>
        </div>
        <div class="text-5xl font-display font-black text-white mb-4">$39<span class="text-white/30 text-base font-mono">/mo</span></div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Daily Integrity Backups</li>
          <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> 24hr Security Scan</li>
          <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> System Monitoring</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-emerald-500/30 rounded-xl text-emerald-400 font-mono font-black text-[9px] uppercase tracking-widest hover:bg-emerald-500/10 transition-all">DEPLOY SENTRY</button>
      </div>
      <div class="glass-card rounded-3xl p-10 border-emerald-400/40 shadow-[0_0_40px_rgba(52,211,153,0.2)] scale-105 relative">
        <span class="absolute top-4 right-4 px-2 py-1 bg-emerald-500/20 border border-emerald-500/40 rounded text-[7px] font-mono text-emerald-400 uppercase">COMMANDER</span>
        <div class="flex items-center justify-between mb-6">
          <span class="text-[9px] font-mono text-emerald-400 uppercase">Commander</span>
        </div>
        <div class="text-5xl font-display font-black text-white mb-4">$99<span class="text-white/30 text-base font-mono">/mo</span></div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> High-Priority Backups</li>
          <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Neural Bugfix Targeting</li>
          <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Deep Malware Purge</li>
          <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> 12hr Response SLA</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 bg-emerald-500 text-black rounded-xl font-mono font-black text-[9px] uppercase tracking-widest hover:scale-105 transition-all shadow-[0_0_20px_rgba(52,211,153,0.4)]">CLAIM PROTECTION</button>
      </div>
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-cyan-500/30 transition-all">
        <div class="flex items-center justify-between mb-6">
          <span class="text-[9px] font-mono text-white/30 uppercase">Overlord</span>
          <span class="px-2 py-1 bg-cyan-500/10 border border-cyan-500/20 rounded text-[7px] font-mono text-cyan-400 uppercase">Elite</span>
        </div>
        <div class="text-5xl font-display font-black text-white mb-4">$199<span class="text-white/30 text-base font-mono">/mo</span></div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="text-cyan-400">✓</span> 24/7 Comms Monitoring</li>
          <li class="flex items-center gap-2"><span class="text-cyan-400">✓</span> Quantum Firewall Shield</li>
          <li class="flex items-center gap-2"><span class="text-cyan-400">✓</span> Dedicated War Room</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-cyan-500/30 rounded-xl text-cyan-400 font-mono font-black text-[9px] uppercase tracking-widest hover:bg-cyan-500/10 transition-all">ASCEND NOW</button>
      </div>
    </div>
    <!-- Uptime -->
    <div class="glass-card rounded-2xl p-10 border-emerald-500/20 mb-12">
      <div class="flex justify-between items-center mb-8">
        <h3 class="text-2xl font-display font-black text-white uppercase">UPTIME ASSURANCE</h3>
        <div class="text-right">
          <span class="text-[9px] font-mono text-white/30 uppercase block">Global Availability</span>
          <span class="text-3xl font-display font-black text-emerald-400">99.9%</span>
        </div>
      </div>
      <div class="h-24 w-full relative overflow-hidden rounded-lg bg-emerald-500/5 border border-emerald-500/10 mb-8">
        <svg class="w-full h-full" viewBox="0 0 400 80" preserveAspectRatio="none">
          <path d="M0,60 C40,50 80,20 120,30 S200,10 260,20 S340,5 400,15" fill="rgba(52,211,153,0.1)" stroke="#34d399" stroke-width="2"/>
        </svg>
      </div>
      <div class="grid grid-cols-4 gap-6">
        <div class="text-center"><div class="text-2xl font-display font-black text-white">24/7s</div><p class="text-[8px] font-mono text-white/30 uppercase">Always On</p></div>
        <div class="text-center"><div class="text-2xl font-display font-black text-emerald-400">100%</div><p class="text-[8px] font-mono text-white/30 uppercase">Backup Rate</p></div>
        <div class="text-center"><div class="text-2xl font-display font-black text-white">0.00%</div><p class="text-[8px] font-mono text-white/30 uppercase">Breach Rate</p></div>
        <div class="text-center"><div class="text-2xl font-display font-black text-accent">AES-256</div><p class="text-[8px] font-mono text-white/30 uppercase">Encryption</p></div>
      </div>
    </div>
    <!-- CTA -->
    <div class="glass-card rounded-3xl p-16 border-emerald-500/20 text-center">
      <h2 class="text-4xl font-display font-black text-white uppercase mb-4">READY TO FORTIFY?</h2>
      <button onclick="window.location.href='contact.html'" class="mt-6 px-12 py-4 bg-emerald-500 text-black font-mono font-black text-sm uppercase tracking-widest rounded-full hover:scale-105 transition-all shadow-[0_0_30px_rgba(52,211,153,0.4)] flex items-center gap-3 mx-auto">
        <span class="material-symbols-outlined">security</span> SUMMON SUPPORT
      </button>
    </div>
  </section>
</main>
'''
build('service-maintenance.html', 'Vanguard Protection', maintenance)

# ── SERVICE: CREATION ─────────────────────────────────────────────────────────
creation = '''
<main class="pt-36 pb-24">
  <section class="max-w-7xl mx-auto px-8">
    <div class="text-center mb-20">
      <h1 class="text-5xl md:text-8xl font-display font-black text-white uppercase tracking-tighter leading-none mb-6">
        FORGING<br/><span class="text-transparent bg-clip-text bg-gradient-to-r from-accent to-primary">DIGITAL KINGDOMS</span>
      </h1>
      <p class="text-white/50 font-mono text-[11px] uppercase tracking-widest max-w-2xl mx-auto">High-tech Arthurian cyberpunk web development for your digital empire. Precision-engineered interfaces for modern monarchs.</p>
    </div>
    <h2 class="text-3xl font-display font-black text-white uppercase text-center mb-12">CHOOSE YOUR TIER</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-20">
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-accent/30 transition-all relative">
        <span class="absolute top-4 right-4 text-accent text-2xl">✕</span>
        <span class="text-[9px] font-mono text-white/30 uppercase mb-2 block">THE SQUIRE</span>
        <p class="text-white/30 text-[10px] font-mono uppercase mb-4">Single Page Interface — Entry-Level Construction</p>
        <div class="text-3xl font-display font-black text-white mb-2">2-4 WEEKS</div>
        <div class="text-accent font-mono text-sm mb-6">Starting configuration</div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="text-accent">✓</span> Single Page Interface</li>
          <li class="flex items-center gap-2"><span class="text-accent">✓</span> Essential SEO Core</li>
          <li class="flex items-center gap-2"><span class="text-accent">✓</span> Cyberpunk Visual Suite</li>
          <li class="flex items-center gap-2"><span class="text-accent">✓</span> Responsive Foundation</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-accent/30 rounded-xl text-accent font-mono font-black text-[9px] uppercase tracking-widest hover:bg-accent/10 transition-all">SELECT SQUIRE</button>
      </div>
      <div class="glass-card rounded-3xl p-10 border-primary/40 shadow-[0_0_40px_rgba(79,70,229,0.2)] scale-105 relative">
        <span class="absolute top-4 right-4 px-2 py-1 bg-primary/20 border border-primary/40 rounded text-[7px] font-mono text-primary uppercase">BEST POPULAR</span>
        <span class="text-[9px] font-mono text-primary uppercase mb-2 block">THE KNIGHT</span>
        <p class="text-white/30 text-[10px] font-mono uppercase mb-4">Multi-page Dominion — Full Production Stack</p>
        <div class="text-3xl font-display font-black text-white mb-2">4-8 WEEKS</div>
        <div class="text-primary font-mono text-sm mb-6">Suggested starting architecture</div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="text-primary">✓</span> Multi-page Domain</li>
          <li class="flex items-center gap-2"><span class="text-primary">✓</span> Advanced SEO Matrix</li>
          <li class="flex items-center gap-2"><span class="text-primary">✓</span> Custom Animations</li>
          <li class="flex items-center gap-2"><span class="text-primary">✓</span> CMS Integration</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 bg-white text-black rounded-xl font-mono font-black text-[9px] uppercase tracking-widest hover:scale-105 transition-all">SELECT KNIGHT</button>
      </div>
      <div class="glass-card rounded-3xl p-10 border-white/5 hover:border-amber-500/30 transition-all relative">
        <span class="absolute top-4 right-4 text-amber-500 text-2xl">♛</span>
        <span class="text-[9px] font-mono text-white/30 uppercase mb-2 block">THE KING</span>
        <p class="text-white/30 text-[10px] font-mono uppercase mb-4">Full-platform Sovereignty — Enterprise stack</p>
        <div class="text-3xl font-display font-black text-white mb-2">8-12+ WEEKS</div>
        <div class="text-amber-500 font-mono text-sm mb-6">Custom scoping required</div>
        <ul class="space-y-3 text-[10px] font-mono text-white/50 mb-10">
          <li class="flex items-center gap-2"><span class="text-amber-500">✓</span> Full E-Commerce Arsenal</li>
          <li class="flex items-center gap-2"><span class="text-amber-500">✓</span> Custom Web Architecture</li>
          <li class="flex items-center gap-2"><span class="text-amber-500">✓</span> Priority Round-Table</li>
          <li class="flex items-center gap-2"><span class="text-amber-500">✓</span> Complete Digital Sovereignty</li>
        </ul>
        <button onclick="window.location.href='contact.html'" class="w-full py-3 border border-amber-500/30 rounded-xl text-amber-500 font-mono font-black text-[9px] uppercase tracking-widest hover:bg-amber-500/10 transition-all">SELECT KING</button>
      </div>
    </div>
    <div class="glass-card rounded-3xl p-12 border-accent/20 text-center">
      <h2 class="text-3xl font-display font-black text-white uppercase mb-4">READY TO BUILD?</h2>
      <p class="text-white/40 font-mono text-[10px] uppercase tracking-widest mb-8">Step into the digital forge. Let's create something legendary. Your empire awaits its architect.</p>
      <button onclick="window.location.href='contact.html'" class="px-12 py-4 bg-accent text-black font-mono font-black text-sm uppercase tracking-widest rounded-full hover:scale-105 transition-all shadow-[0_0_30px_rgba(0,255,255,0.4)] flex items-center gap-3 mx-auto">
        <span class="material-symbols-outlined">construction</span> ENGAGE THE FORGE
      </button>
    </div>
  </section>
</main>
'''
build('service-creation.html', 'The Forge', creation)

# ── Legal pages ───────────────────────────────────────────────────────────────
legal_template = '''
<main class="pt-36 pb-24">
  <div class="max-w-4xl mx-auto px-8">
    <h1 class="text-4xl font-display font-black text-white uppercase mb-4">{title}</h1>
    <p class="text-white/30 font-mono text-[9px] uppercase tracking-widest mb-12">Last updated: March 2025</p>
    {body}
  </div>
</main>
'''
def legal_section(heading, paras):
    ps = ''.join(f'<p class="text-white/40 font-mono text-[11px] leading-relaxed mb-4 uppercase tracking-wider">{p}</p>' for p in paras)
    return f'<div class="mb-10"><h2 class="text-xl font-display font-black text-white uppercase mb-4">{heading}</h2>{ps}</div>'

legal_body = (
    legal_section("Acceptance of Terms", ["By accessing Camelot Flows, you agree to be bound by these Terms of Service.", "Use of this site constitutes your acceptance of these terms in full."]) +
    legal_section("Intellectual Property", ["All content, branding, and code are the intellectual property of Camelot Flows.", "Unauthorized reproduction or use of any materials is strictly prohibited."]) +
    legal_section("Services & Payment", ["All service engagements are governed by a signed Statement of Work.", "Pricing listed is indicative; final quotes are provided per project scope."]) +
    legal_section("Limitation of Liability", ["Camelot Flows shall not be liable for any indirect or consequential damages.", "Our maximum liability is limited to fees paid in the preceding 30 days."]) +
    legal_section("Contact", ["For legal inquiries, contact: legal@camelotflows.com"])
)
build('legal.html', 'Legal', legal_template.format(title='Terms of Service', body=legal_body))

privacy_body = (
    legal_section("Information Collection", ["We collect information you provide when contacting us (name, email, project details).", "We use analytics to improve our services — no personal data is sold."]) +
    legal_section("Data Use", ["Your data is used solely to provide and improve our services.", "We never share your data with third parties without your consent."]) +
    legal_section("Cookies", ["We use minimal, essential cookies for site functionality.", "You may disable cookies in your browser settings at any time."]) +
    legal_section("Your Rights", ["You have the right to access, correct, or delete your personal data.", "Contact us at privacy@camelotflows.com to exercise your rights."])
)
build('privacy.html', 'Privacy Policy', legal_template.format(title='Privacy Policy', body=privacy_body))

print("Part 6 done - all pages generated!")
