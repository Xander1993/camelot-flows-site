import os, re

BASE = r'c:\Users\user\Downloads\stitch_camelot_flows_homepage'

new_gsap_script = """
<script>
(function() {
    gsap.registerPlugin(ScrollTrigger);

    // Modern Luxury Cursor
    const cursor = document.getElementById("custom-cursor");
    if (cursor) {
        window.addEventListener("mousemove", (e) => {
            gsap.to(cursor, { x: e.clientX, y: e.clientY, opacity: 1, duration: 0.15, ease: 'power2.out' });
        });
        document.querySelectorAll("a, button, input").forEach(el => {
            el.addEventListener("mouseenter", () => gsap.to(cursor, { scale: 3, opacity: 0.4, backgroundColor: '#00f5ff', duration: 0.3 }));
            el.addEventListener("mouseleave", () => gsap.to(cursor, { scale: 1, opacity: 1, backgroundColor: '#8b5cf6', duration: 0.3 }));
        });
    }

    // Cozy Stagger Fade-Up Cards
    const cardSelectors = ['.glass-card', '[data-gsap="fade-up"]', 'section > div > div[class*="grid"] > div'];
    cardSelectors.forEach(sel => {
        gsap.utils.toArray(sel).forEach((el, i) => {
            gsap.fromTo(el, { y: 60, opacity: 0 }, {
                y: 0, opacity: 1, duration: 1, ease: 'power4.out',
                scrollTrigger: { trigger: el, start: 'top 85%', toggleActions: 'play none none none' }
            });
        });
    });

    // Award-Winning Text Reveals (Split Words effect via span wrapping if not already spanning)
    gsap.utils.toArray('h1, h2, h3').forEach(heading => {
        if (!heading.classList.contains('no-split')) {
            gsap.fromTo(heading, { y: 40, opacity: 0, rotationX: -20 }, {
                y: 0, opacity: 1, rotationX: 0, duration: 1.2, ease: 'back.out(1.4)',
                scrollTrigger: { trigger: heading, start: 'top 90%', toggleActions: 'play none none none' }
            });
        }
    });

    // Gradient Divider Expansions
    gsap.utils.toArray('.h-px, hr').forEach(line => {
        gsap.fromTo(line, { scaleX: 0, transformOrigin: 'left' }, {
            scaleX: 1, duration: 1.5, ease: 'power3.inOut',
            scrollTrigger: { trigger: line, start: 'top 90%' }
        });
    });

    // Parallax Orbs
    gsap.utils.toArray('.bg-orb').forEach((orb, i) => {
        gsap.to(orb, {
            y: i % 2 === 0 ? -100 : 100,
            ease: 'none',
            scrollTrigger: { trigger: 'body', start: 'top top', end: 'bottom bottom', scrub: 1 }
        });
    });

    // Magnetic Buttons
    gsap.utils.toArray('button').forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            gsap.to(btn, { x: x * 0.2, y: y * 0.2, duration: 0.4, ease: 'power2.out' });
        });
        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, { x: 0, y: 0, duration: 0.8, ease: 'elastic.out(1, 0.3)' });
        });
    });
})();
</script>
"""

replacements = {
    "Protocol: Neon Knight": "Design System: Stitch",
    "Rule Your": "Crafting Elite",
    "Digital Kingdom": "Digital Sanctuaries",
    "Deploy <span class=\\"text-white font-medium\\">Awwwards-tier web design</span> and hyper-fast infrastructure to conquer the digital frontier. Automate your business with zero friction.": "Elevating your brand with Awwwards-tier design and seamless infrastructure. We build digital experiences that feel truly luxurious and perform flawlessly.",
    "A tech visionary from Chisinau, Moldova — architecting the intersection of performance, AI, and user experience. Father of Arthur, builder of futures.": "A digital artisan crafting bespoke, high-performance web experiences. Merging award-winning design with seamless AI capabilities.",
    "INITIALIZE_AGENT": "LET'S CONNECT",
    "VIEW_ARSENAL": "OUR CAPABILITIES",
    "System Override": "Begin Your Journey",
    "Enter<br/>The Matrix": "Step Into<br/>The Future",
    "Excalibur Online": "Digital Excellence",
    "Camelot Server Authorized": "Exclusive Access Granted",
    "I Build<br/><span class=\\"text-transparent bg-clip-text bg-gradient-to-r from-primary to-accent\\">Digital<br/>Kingdoms.</span>": "I Build<br/><span class=\\"text-transparent bg-clip-text bg-gradient-to-r from-primary to-accent\\">Digital<br/>Sanctuaries.</span>",
    "EXCALIBUR PROTOCOL AUTOMATION": "SEAMLESS INTEGRATION",
    "NEON KNIGHT ARCHITECTURE": "BOUTIQUE DESIGN ARCHITECTURE",
    "100% UPTIME SLA": "UNCOMPROMISING RELIABILITY",
    "ZERO HUMAN FRICTION": "EFFORTLESS EXPERIENCES",
    "AI AUTOPILOT": "INTELLIGENT SCALING",
    "HIRE ME": "LET'S BUILD",
    "Read Log": "Our Story",
    "Work Manifest": "Case Studies",
    "background: rgba(10, 10, 18, 0.6)": "background: rgba(10, 10, 14, 0.75)",
    "backdrop-filter: blur(20px)": "backdrop-filter: blur(24px)",
    "background-color: #050508": "background: radial-gradient(circle at 50% 0%, #111114, #0a0a0c) !important; background-attachment: fixed !important;",
    "rgba(15, 15, 25, 0.6)": "rgba(20, 20, 24, 0.7)",
    "rounded-xl": "rounded-3xl",
    "rounded-2xl": "rounded-3xl",
    "font-bold text-slate-400": "font-bold text-zinc-400",
    "text-slate-400": "text-zinc-400",
    "text-slate-500": "text-zinc-500",
    "text-white/50": "text-zinc-300",
    "text-white/40": "text-zinc-400"
}

def apply_cozy_redesign(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply text replacements
    for old, new in replacements.items():
        html = html.replace(old, new)
        
    # Inject new GSAP instead of old GSAP
    html = re.sub(r'<script>\s*\(function\(\) \{.*?gsap\.registerPlugin\(ScrollTrigger\).*?\}\)\(\);\s*</script>', '', html, flags=re.DOTALL)
    if new_gsap_script.strip() not in html:
        html = html.replace('</body>', new_gsap_script + '\\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  ✓ {os.path.basename(filepath)}')

html_files = [f for f in os.listdir(BASE) if f.endswith('.html')]
for file in html_files:
    path = os.path.join(BASE, file)
    if os.path.exists(path):
        apply_cozy_redesign(path)

print('\\nDone! All pages now have cozy design tweaks and updated GSAP scripts.')
