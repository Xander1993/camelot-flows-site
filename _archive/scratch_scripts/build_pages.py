import codecs
import json
import shutil

base_file = 'code_v2.html'
with codecs.open(base_file, 'r', 'utf-8') as f:
    lines = f.readlines()

head_part = "".join(lines[:247])
tail_part = "".join(lines[940:])

def build_page(filename, title, content):
    h = head_part.replace('<title>Camelot Flows | Neon Knight Edition</title>', f'<title>Camelot Flows | {title}</title>')
    full = h + '\n' + content + '\n' + tail_part
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(full)
    print(f"Generated {filename}")

# arsenal
arsenal_content = '''<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="max-w-6xl mx-auto flex flex-col justify-center items-center text-center">
    <h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-white text-glow">The <span class="text-neon-cyan">Arsenal</span></h1>
    <p class="text-slate-400 text-lg leading-relaxed max-w-2xl mb-12">A curated showcase of our previous web engineering and automation deployments.</p>
    <div class="glass-card p-12 rounded-xl text-center border-neon-cyan/30 w-full">
        <span class="material-symbols-outlined text-6xl text-neon-cyan mb-4">construction</span>
        <h2 class="text-2xl font-bold text-white uppercase mb-4">Armory Under Maintenance</h2>
        <p class="text-slate-400">Our project showcase is currently being updated with our latest 2026 enterprise deployments.</p>
    </div>
</div>
</main>'''

merlin_content = '''<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
    <div>
        <h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-white text-glow">The <span class="text-neon-purple">Merlin</span> System</h1>
        <p class="text-slate-400 text-lg leading-relaxed mb-8">Deploy fully autonomous AI agents that handle lead generation, sales routing, and customer support.</p>
        <button onclick="window.location.href='contact.html'" class="bg-neon-purple/10 border border-neon-purple/50 text-neon-purple px-8 py-3 rounded font-mono text-sm tracking-widest uppercase hover:bg-neon-purple hover:text-white transition-colors">Integrate Now</button>
    </div>
    <div class="glass-card p-8 rounded-xl border-neon-purple/30">
        <ul class="space-y-4 text-sm text-slate-300">
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-xl">smart_toy</span> Specialized Custom LLMs</li>
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-xl">dataset</span> Deep Context Knowledge</li>
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-xl">bolt</span> Real-time Lead Scoring</li>
            <li class="flex items-center gap-3"><span class="text-neon-purple material-symbols-outlined text-xl">cable</span> CRM Synchronization</li>
        </ul>
    </div>
</div>
</main>'''

case_studies_content = '''<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="max-w-6xl mx-auto flex flex-col justify-center items-center text-center">
    <h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-white text-glow">Case <span class="text-emerald-400">Studies</span></h1>
    <p class="text-slate-400 text-lg leading-relaxed max-w-2xl mb-12">Detailed breakdowns of our high-impact engineering missions.</p>
    <div class="glass-card p-12 rounded-xl text-center border-emerald-400/30 w-full">
        <span class="material-symbols-outlined text-6xl text-emerald-400 mb-4">analytics</span>
        <h2 class="text-2xl font-bold text-white uppercase mb-4">Data Compilation in Progress</h2>
        <p class="text-slate-400">Detailed analytics and performance summaries of our recent projects are currently being compiled.</p>
    </div>
</div>
</main>'''

agencies_content = '''<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
    <div>
        <h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-white text-glow">Agency <span class="text-neon-blue">Partners</span></h1>
        <p class="text-slate-400 text-lg leading-relaxed mb-8">White-label web development and robust automation integration to scale your agency's delivery capabilities without overhead.</p>
        <button onclick="window.location.href='contact.html'" class="bg-neon-blue/10 border border-neon-blue/50 text-neon-blue px-8 py-3 rounded font-mono text-sm tracking-widest uppercase hover:bg-neon-blue hover:text-white transition-colors">Schedule Audit</button>
    </div>
    <div class="glass-card p-8 rounded-xl border-neon-blue/30">
        <ul class="space-y-4 text-sm text-slate-300">
            <li class="flex items-center gap-3"><span class="text-neon-blue material-symbols-outlined text-xl">shield</span> Complete White-label (NDA)</li>
            <li class="flex items-center gap-3"><span class="text-neon-blue material-symbols-outlined text-xl">speed</span> Overflow Capacity Scaling</li>
            <li class="flex items-center gap-3"><span class="text-neon-blue material-symbols-outlined text-xl">model_training</span> Specialized Engineering Team</li>
        </ul>
    </div>
</div>
</main>'''

about_content = '''<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="max-w-4xl mx-auto text-center">
    <h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-white text-glow">About <span class="text-primary-glow">Us</span></h1>
    <p class="text-slate-400 text-lg leading-relaxed mb-8">Camelot Flows operates as a specialized engineering and design workshop focusing on bringing high-end aesthetics and bleeding-edge automation to modern businesses. We combine the reliability of traditional development with the speed of AI integration.</p>
</div>
</main>'''

contact_content = '''<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="max-w-4xl mx-auto">
    <h1 class="font-display text-5xl md:text-7xl font-black uppercase tracking-tighter mb-6 text-white text-center text-glow">Establish <span class="text-primary-glow">Uplink</span></h1>
    <p class="text-slate-400 text-center mb-12">Submit your coordinates, and we will initiate communications.</p>
    
    <div class="glass-card p-8 md:p-12 rounded-xl border-primary/30">
        <form class="space-y-6" name="contact" method="POST" data-netlify="true">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <label class="block font-mono text-xs text-primary mb-2 uppercase">Subject Name</label>
                    <input type="text" name="name" class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-white focus:border-primary/50 focus:ring-1 focus:ring-primary/50 outline-none transition-colors" placeholder="John Doe" required>
                </div>
                <div>
                    <label class="block font-mono text-xs text-primary mb-2 uppercase">Target Coordinates (Email)</label>
                    <input type="email" name="email" class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-white focus:border-primary/50 focus:ring-1 focus:ring-primary/50 outline-none transition-colors" placeholder="john@example.com" required>
                </div>
            </div>
            <div>
                <label class="block font-mono text-xs text-primary mb-2 uppercase">Objective Type</label>
                <select name="objective" class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-white focus:border-primary/50 focus:ring-1 focus:ring-primary/50 outline-none transition-colors" required>
                    <option value="">Select Initiative...</option>
                    <option value="web">Web Architecture</option>
                    <option value="automation">Workflow Automation</option>
                    <option value="agency">Agency Partnership</option>
                    <option value="other">Other Inquiry</option>
                </select>
            </div>
            <div>
                <label class="block font-mono text-xs text-primary mb-2 uppercase">Mission Brief</label>
                <textarea rows="5" name="message" class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-white focus:border-primary/50 focus:ring-1 focus:ring-primary/50 outline-none transition-colors" placeholder="Describe the optimal outcome..." required></textarea>
            </div>
            <button type="submit" class="w-full bg-primary hover:bg-primary/90 text-white font-mono font-bold tracking-widest uppercase py-4 rounded text-sm transition-colors mt-4">Transmit Signal</button>
        </form>
    </div>
</div>

<script>
    window.addEventListener('DOMContentLoaded', () => {
        const urlParams = new URLSearchParams(window.location.search);
        const objective = urlParams.get('objective');
        if (objective) {
            const select = document.querySelector('select');
            if (select) {
                const options = Array.from(select.options);
                const match = options.find(opt => opt.value === objective || opt.text.toLowerCase().includes(objective.toLowerCase()));
                if (match) {
                    select.value = match.value;
                }
            }
        }
    });
</script>
</main>'''

legal_content = '''<main class="relative pt-32 pb-20 px-6 min-h-screen">
<div class="max-w-4xl mx-auto">
    <h1 class="font-display text-4xl md:text-5xl font-black uppercase tracking-tighter mb-8 text-white">Legal Information</h1>
    <div class="prose prose-invert prose-slate max-w-none">
        <p>This is a demonstration legal page for Camelot Flows.</p>
    </div>
</div></main>'''

build_page('arsenal.html', 'Arsenal', arsenal_content)
build_page('merlin.html', 'Merlin System', merlin_content)
build_page('case-studies.html', 'Case Studies', case_studies_content)
build_page('for-agencies.html', 'Agency Partners', agencies_content)
build_page('about.html', 'About Us', about_content)
build_page('work-with-me.html', 'Work With Me', about_content)
build_page('contact.html', 'Contact', contact_content)
build_page('legal.html', 'Legal', legal_content)
build_page('privacy.html', 'Privacy Policy', legal_content)
build_page('service-creation.html', 'Site Creation', '<main class="pt-32 min-h-screen"><div class="text-center text-white p-20 glass-card mx-auto max-w-2xl mt-20">Migrated. See Web Architecture.</div></main>')
build_page('service-maintenance.html', 'Maintenance', '<main class="pt-32 min-h-screen"><div class="text-center text-white p-20 glass-card mx-auto max-w-2xl mt-20">Migrated. See Web Architecture.</div></main>')
build_page('service-automation.html', 'Automations', '<main class="pt-32 min-h-screen"><div class="text-center text-white p-20 glass-card mx-auto max-w-2xl mt-20">Migrated. See Merlin System.</div></main>')
build_page('service-marketing.html', 'Marketing', '<main class="pt-32 min-h-screen"><div class="text-center text-white p-20 glass-card mx-auto max-w-2xl mt-20">Migrated. See Agency Partners.</div></main>')

shutil.copy('code_v2.html', 'index.html')
print("Generated index.html")
