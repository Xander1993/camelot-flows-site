import os, json, re

base = 'c:/Users/user/Downloads/stitch_camelot_flows_homepage'
artifact_base = 'C:/Users/user/.gemini/antigravity/brain/36d123e7-2a56-4254-8fb7-c63809a4f3ad'

# Persona Images
startup_img = 'persona_startup_ceo_1773589126792.png'
scaleup_img = 'persona_scaleup_executive_1773589142392.png'
sovereign_img = 'persona_sovereign_visionary_1773589160104.png'

startup_path = f'file:///{artifact_base}/{startup_img}'
scaleup_path = f'file:///{artifact_base}/{scaleup_img}'
sovereign_path = f'file:///{artifact_base}/{sovereign_img}'

# Load shell
with open(os.path.join(base, '_shell_parts.json'), 'r', encoding='utf-8') as f:
    parts = json.load(f)

head_html = parts['head_html']
body_shell = parts['body_shell']

def build_page(title, content):
    h = head_html.replace('<title>Camelot Flows | Digital Architect</title>', f'<title>Camelot Flows | {title}</title>')
    # Ensure [PAGE_CONTENT] is in body_shell
    return h + '\n' + body_shell.replace('[PAGE_CONTENT]', content)

def save(name, title, content):
    with open(os.path.join(base, name), 'w', encoding='utf-8') as f:
        f.write(build_page(title, content))
    print(f"  Created {name}")

# --- 1. HOME PAGE CONTENT ---
with open(os.path.join(base, 'code_v2.html'), 'r', encoding='utf-8') as f:
    code_v2 = f.read()

# Extract EVERYTHING inside <div id="smooth-content"> except the footer
match = re.search(r'<div id="smooth-content">(.*?)<footer', code_v2, re.DOTALL)
if not match:
    # Fallback to everything after </nav>
    match = re.search(r'</nav>(.*?)<footer', code_v2, re.DOTALL)

home_content = match.group(1).strip() if match else "<!-- Home Content Missing -->"

# --- 2. ABOUT PAGE CONTENT (Restored Timeline) ---
about_content = f'''
<main class="relative pt-40 pb-24 overflow-hidden">
    <section class="max-w-7xl mx-auto px-8 relative z-10">
        <div class="mb-32">
            <h1 class="text-8xl font-display font-black text-white uppercase tracking-tighter mb-8 text-glow">Origin Story</h1>
            <p class="text-white/40 font-mono text-xs uppercase tracking-[0.5em]">The evolution of Camelot Flows.</p>
        </div>

        <!-- The Timeline -->
        <div class="relative">
            <div class="absolute left-1/2 top-0 bottom-0 w-[1px] bg-gradient-to-b from-primary via-white/20 to-transparent -translate-x-1/2 hidden md:block"></div>
            
            <div class="space-y-40">
                <!-- 2018: Spark -->
                <div class="relative flex flex-col md:flex-row items-center justify-between group">
                    <div class="md:w-[45%] text-right pr-12 hidden md:block">
                        <div class="text-6xl font-display font-black text-white/10 group-hover:text-primary transition-colors">2018</div>
                    </div>
                    <div class="w-8 h-8 rounded-full bg-obsidian border-4 border-primary z-10 shadow-neon"></div>
                    <div class="md:w-[45%] text-left pl-12">
                        <div class="glass-card p-10 rounded-3xl border-white/5">
                            <span class="text-primary font-mono text-xs uppercase tracking-widest mb-4 block">// THE_SPARK</span>
                            <h3 class="text-2xl font-display font-bold text-white uppercase mb-4">Initial Convergence</h3>
                            <p class="text-white/50 font-mono text-[11px] leading-relaxed uppercase tracking-widest">
                                The first encounter with high-stakes digital architecture. The foundation of aesthetics and logic was poured into my DNA.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- 2020: Grind -->
                <div class="relative flex flex-col md:flex-row-reverse items-center justify-between group">
                    <div class="md:w-[45%] text-left pl-12 hidden md:block">
                        <div class="text-6xl font-display font-black text-white/10 group-hover:text-primary transition-colors">2020</div>
                    </div>
                    <div class="w-8 h-8 rounded-full bg-obsidian border-4 border-primary z-10 shadow-neon"></div>
                    <div class="md:w-[45%] text-right pr-12">
                        <div class="glass-card p-10 rounded-3xl border-white/5">
                            <span class="text-primary font-mono text-xs uppercase tracking-widest mb-4 block">// THE_GRIND</span>
                            <h3 class="text-2xl font-display font-bold text-white uppercase mb-4">Code & Steel</h3>
                            <p class="text-white/50 font-mono text-[11px] leading-relaxed uppercase tracking-widest">
                                Thousands of hours in the terminal. Mastering the art of Python, GSAP, and performance-first web development.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- 2022: Pivot -->
                <div class="relative flex flex-col md:flex-row items-center justify-between group">
                    <div class="md:w-[45%] text-right pr-12 hidden md:block">
                        <div class="text-6xl font-display font-black text-white/10 group-hover:text-primary transition-colors">2022</div>
                    </div>
                    <div class="w-8 h-8 rounded-full bg-obsidian border-4 border-primary z-10 shadow-neon"></div>
                    <div class="md:w-[45%] text-left pl-12">
                        <div class="glass-card p-10 rounded-3xl border-white/5">
                            <span class="text-primary font-mono text-xs uppercase tracking-widest mb-4 block">// THE_PIVOT</span>
                            <h3 class="text-2xl font-display font-bold text-white uppercase mb-4">Strategic Evolution</h3>
                            <p class="text-white/50 font-mono text-[11px] leading-relaxed uppercase tracking-widest">
                                Shifting from "just building" to "building to win". Realizing that business logic is the true Excalibur.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- 2024: Camelot -->
                <div class="relative flex flex-col md:flex-row-reverse items-center justify-between group">
                    <div class="md:w-[45%] text-left pl-12 hidden md:block">
                        <div class="text-6xl font-display font-black text-white/10 group-hover:text-primary transition-colors">2024</div>
                    </div>
                    <div class="w-8 h-8 rounded-full bg-obsidian border-4 border-primary z-10 shadow-neon"></div>
                    <div class="md:w-[45%] text-right pr-12">
                        <div class="glass-card p-10 rounded-3xl border-primary/20 shadow-neon">
                            <span class="text-accent font-mono text-xs uppercase tracking-widest mb-4 block">// CAMELOT_FLOWS</span>
                            <h3 class="text-2xl font-display font-bold text-white uppercase mb-4">Sovereign Architecture</h3>
                            <p class="text-white/50 font-mono text-[11px] leading-relaxed uppercase tracking-widest">
                                The birth of the Digital Kingdom. Camelot Flows is now the beacon for businesses seeking 100% performance and zero fiction.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>
'''

# --- 3. BUSINESS HUB CONTENT ---
persona_section = f'''
<section class="py-32 px-8 relative overflow-hidden border-b border-white/5 bg-obsidian-light">
    <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-24">
            <h2 class="text-4xl md:text-6xl font-display font-black text-white uppercase tracking-tighter mb-4">Who Are You?</h2>
            <p class="text-white/40 font-mono text-[10px] uppercase tracking-[0.5em]">Choose your path and tell me why you should join the mission.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="glass-card rounded-3xl overflow-hidden group hover:border-accent/40 transition-all border-white/5">
                <div class="aspect-video relative overflow-hidden">
                    <img src="{startup_path}" alt="The Startup" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 opacity-80" />
                    <div class="absolute inset-0 bg-gradient-to-t from-obsidian to-transparent"></div>
                </div>
                <div class="p-10">
                    <h3 class="text-2xl font-display font-bold text-white uppercase mb-4">The Startup</h3>
                    <p class="text-white/50 text-[11px] font-mono leading-relaxed uppercase tracking-widest mb-8 font-light">
                        Hungry for real-world impact. You're tired of theoretical enigmas and want to build things that people actually use.
                    </p>
                    <button class="w-full py-3 rounded-xl border border-accent/20 text-accent font-mono font-black text-[10px] uppercase tracking-widest hover:bg-accent hover:text-black transition-all">SELECT_PATH</button>
                </div>
            </div>
            <div class="glass-card rounded-3xl overflow-hidden group hover:border-violet-500/40 transition-all border-white/5">
                <div class="aspect-video relative overflow-hidden">
                    <img src="{scaleup_path}" alt="The Scaleup" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 opacity-80" />
                    <div class="absolute inset-0 bg-gradient-to-t from-obsidian to-transparent"></div>
                </div>
                <div class="p-10">
                    <h3 class="text-2xl font-display font-bold text-white uppercase mb-4">The Scale-up</h3>
                    <p class="text-white/50 text-[11px] font-mono leading-relaxed uppercase tracking-widest mb-8 font-light">
                        You've seen the corporate world and you're bored with it. You're ready to pivot your skills into something meaningful and lean.
                    </p>
                    <button class="w-full py-3 rounded-xl border border-violet-500/20 text-violet-400 font-mono font-black text-[10px] uppercase tracking-widest hover:bg-violet-500 hover:text-white transition-all">SELECT_PATH</button>
                </div>
            </div>
            <div class="glass-card rounded-3xl overflow-hidden group hover:border-amber-500/40 transition-all border-white/5">
                <div class="aspect-video relative overflow-hidden">
                    <img src="{sovereign_path}" alt="The Sovereign" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 opacity-80" />
                    <div class="absolute inset-0 bg-gradient-to-t from-obsidian to-transparent"></div>
                </div>
                <div class="p-10">
                    <h3 class="text-2xl font-display font-bold text-white uppercase mb-4">The Sovereign</h3>
                    <p class="text-white/50 text-[11px] font-mono leading-relaxed uppercase tracking-widest mb-8 font-light">
                        Dominance isn't the beginning; it's the goal. You want to use game mechanics and multi-modal tech to solve real-world problems.
                    </p>
                    <button class="w-full py-3 rounded-xl border border-amber-500/20 text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest hover:bg-amber-500 hover:text-black transition-all">SELECT_PATH</button>
                </div>
            </div>
        </div>
    </div>
</section>
'''

def create_service_section(id, title, subtitle, color, tiers):
    tier_html = ""
    for t in tiers:
        benefits = "".join([f'<li class="flex items-center gap-2 mb-2"><span class="material-symbols-outlined text-[14px] text-{color}-400">check_circle</span> {b}</li>' for b in t['benefits']])
        tier_html += f'''
            <div class="glass-card p-10 rounded-[2rem] border-white/5 hover:border-{color}-500/30 transition-all group relative overflow-hidden">
                <div class="relative z-10">
                    <h3 class="text-2xl font-display font-black text-white uppercase mb-1">{t['name']}</h3>
                    <p class="text-[9px] font-mono text-white/30 uppercase tracking-[0.2em] mb-8">{t['desc']}</p>
                    <div class="text-6xl font-display font-black text-white mb-2 leading-none">{t['price']}</div>
                    <div class="text-[10px] font-mono text-{color}-400 uppercase tracking-widest mb-10">{t['period']}</div>
                    <ul class="text-[11px] font-mono text-white/50 uppercase tracking-widest mb-12 space-y-4">
                        {benefits}
                    </ul>
                    <button class="w-full py-5 rounded-2xl border border-white/10 text-white font-mono font-black text-[10px] tracking-[0.3em] uppercase group-hover:bg-white group-hover:text-black transition-all">{t['cta']}</button>
                </div>
            </div>
        '''
    return f'''
<section id="{id}" class="py-40 relative overflow-hidden skew-section">
    <div class="max-w-7xl mx-auto px-8 relative z-10">
        <div class="mb-32">
            <h2 class="text-[10vw] md:text-[8vw] font-display font-black leading-[0.8] mb-8 text-transparent bg-clip-text bg-gradient-to-r from-white via-white to-{color}-500/50 uppercase tracking-[-0.05em]">{title}</h2>
            <p class="text-lg text-white/40 max-w-xl font-sans leading-relaxed">{subtitle}</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">{tier_html}</div>
    </div>
</section>
'''

forge_section = create_service_section("forge", "THE FORGE", "Elite digital architecture for the new market. We build the machines that build your wealth.", "cyan", [
    {"name": "Squire", "desc": "Landing Protocol", "price": "$299", "period": "Fixed Bounty", "benefits": ["High-Fidelity Interface", "Responsive Grid", "SEO Shell"], "cta": "SELECT_SQUIRE"},
    {"name": "Knight", "desc": "Fleet Domain", "price": "$799", "period": "Fixed Bounty", "benefits": ["Multi-Page System", "GSAP Kinematics", "Conversion Logic"], "cta": "ENLIST_KNIGHT"},
    {"name": "King", "desc": "Empire Architecture", "price": "$1,999", "period": "Fixed Bounty", "benefits": ["E-Commerce Vault", "Custom Backends", "Royal Support"], "cta": "CHOOSE_KING"}
])
alchemist_section = create_service_section("automation", "ALCHEMIST", "Turning complex logic into gold workflows. Automation is the heartbeat of efficiency.", "violet", [
    {"name": "Initiate", "desc": "Basic Alchmemy", "price": "$149", "period": "Monthly Ritual", "benefits": ["Simple Workflows", "Daily Reports", "API Sync"], "cta": "START_RITUAL"},
    {"name": "Adept", "desc": "Advanced Transmutation", "price": "$399", "period": "Monthly Ritual", "benefits": ["Autonomous Agents", "Make.com Uplink", "Custom Logic"], "cta": "SUMMON_POWER"},
    {"name": "Master", "desc": "Sovereign Logic", "price": "$899", "period": "Monthly Ritual", "benefits": ["Enterprise Scaling", "Neural Integration", "24/7 Watch"], "cta": "RULE_ALL"}
])

gsap_logic = '''
<script>
    document.addEventListener('DOMContentLoaded', () => {
        let proxy = { skew: 0 }, skewSetter = gsap.quickSetter(".skew-section", "skewY", "deg"), clamp = gsap.utils.clamp(-5, 5);
        ScrollTrigger.create({
            onUpdate: (self) => {
                let skew = clamp(self.getVelocity() / -300);
                if (Math.abs(skew) > Math.abs(proxy.skew)) {
                    proxy.skew = skew;
                    gsap.to(proxy, {skew: 0, duration: 0.8, ease: "power3", overwrite: true, onUpdate: () => skewSetter(proxy.skew)});
                }
            }
        });
        document.querySelectorAll('.glass-card').forEach(card => {
            card.addEventListener('mouseenter', () => gsap.to(card, { y: -10, scale: 1.02, duration: 0.4, ease: "power2.out" }));
            card.addEventListener('mouseleave', () => gsap.to(card, { y: 0, scale: 1, duration: 0.6, ease: "elastic.out(1, 0.3)" }));
        });
    });
</script>
'''

# --- SAVE PAGES ---
save('index.html', 'Home', home_content)
save('about.html', 'About', about_content)
save('for-businesses.html', 'Businesses', persona_section + forge_section + alchemist_section + gsap_logic)
save('service-automation.html', 'Automation', alchemist_section + gsap_logic)

print("\nPages restabilized and refreshed.")
