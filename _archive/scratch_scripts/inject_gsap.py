"""
Inject rich GSAP scroll animations into all pages.
Does NOT alter any design/layout — only adds data attributes + a <script> block.
"""
import os, re

BASE = r'c:\Users\user\Downloads\stitch_camelot_flows_homepage'

# ------------------------------------------------------------------
# Shared GSAP animation script added to every subpage
# ------------------------------------------------------------------
GSAP_SCRIPT = """
<script>
(function() {
    gsap.registerPlugin(ScrollTrigger);

    // ── Stagger fade-up for cards ──────────────────────────────────
    const cardSelectors = [
        '.glass-card',
        '[data-gsap="fade-up"]',
        'section > div > div[class*="grid"] > div'
    ];
    cardSelectors.forEach(sel => {
        gsap.utils.toArray(sel).forEach((el, i) => {
            gsap.fromTo(el, {
                y: 40,
                opacity: 0
            }, {
                y: 0,
                opacity: 1,
                duration: 0.8,
                ease: 'power3.out',
                delay: (i % 4) * 0.12,
                scrollTrigger: {
                    trigger: el,
                    start: 'top 88%',
                    toggleActions: 'play none none none'
                }
            });
        });
    });

    // ── Hero headline split ────────────────────────────────────────
    gsap.utils.toArray('h1').forEach(h1 => {
        gsap.fromTo(h1, {
            y: 60,
            opacity: 0,
            skewY: 3
        }, {
            y: 0,
            opacity: 1,
            skewY: 0,
            duration: 1.2,
            ease: 'power4.out',
            scrollTrigger: {
                trigger: h1,
                start: 'top 90%',
                toggleActions: 'play none none none'
            }
        });
    });

    // ── Section headings h2 ────────────────────────────────────────
    gsap.utils.toArray('h2').forEach(h2 => {
        gsap.fromTo(h2, {
            x: -30,
            opacity: 0
        }, {
            x: 0,
            opacity: 1,
            duration: 0.9,
            ease: 'power3.out',
            scrollTrigger: {
                trigger: h2,
                start: 'top 88%',
                toggleActions: 'play none none none'
            }
        });
    });

    // ── Gradient divider lines ─────────────────────────────────────
    gsap.utils.toArray('.h-px, hr').forEach(line => {
        gsap.fromTo(line, { scaleX: 0, transformOrigin: 'left' }, {
            scaleX: 1,
            duration: 1,
            ease: 'power3.inOut',
            scrollTrigger: {
                trigger: line,
                start: 'top 90%'
            }
        });
    });

    // ── Stat counters ──────────────────────────────────────────────
    gsap.utils.toArray('[data-count]').forEach(el => {
        const target = parseFloat(el.getAttribute('data-count'));
        const suffix = el.getAttribute('data-suffix') || '';
        ScrollTrigger.create({
            trigger: el,
            start: 'top 85%',
            onEnter: () => {
                gsap.fromTo({ val: 0 }, { val: target }, {
                    duration: 1.8,
                    ease: 'power2.out',
                    onUpdate: function() {
                        el.textContent = Math.round(this.targets()[0].val).toLocaleString() + suffix;
                    }
                });
            }
        });
    });

    // ── Neon glow pulse on feature cards ──────────────────────────
    gsap.utils.toArray('.glass-card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            gsap.to(card, {
                boxShadow: '0 0 40px rgba(0,255,255,0.15)',
                borderColor: 'rgba(0,255,255,0.3)',
                duration: 0.4,
                ease: 'power2.out'
            });
        });
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                boxShadow: '0 0 0px rgba(0,255,255,0)',
                borderColor: 'rgba(255,255,255,0.08)',
                duration: 0.4,
                ease: 'power2.out'
            });
        });
    });

    // ── Parallax orbs ─────────────────────────────────────────────
    gsap.utils.toArray('.bg-orb').forEach((orb, i) => {
        gsap.to(orb, {
            y: i % 2 === 0 ? -60 : 60,
            ease: 'none',
            scrollTrigger: {
                trigger: 'body',
                start: 'top top',
                end: 'bottom bottom',
                scrub: 1.5
            }
        });
    });

    // ── Timeline items ─────────────────────────────────────────────
    gsap.utils.toArray('.space-y-16 > div').forEach((item, i) => {
        gsap.fromTo(item, {
            x: i % 2 === 0 ? -50 : 50,
            opacity: 0
        }, {
            x: 0,
            opacity: 1,
            duration: 0.9,
            ease: 'power3.out',
            scrollTrigger: {
                trigger: item,
                start: 'top 85%'
            }
        });
    });

    // ── Pricing card highlight ─────────────────────────────────────
    gsap.utils.toArray('.scale-105').forEach(card => {
        gsap.fromTo(card, {
            scale: 0.95,
            opacity: 0
        }, {
            scale: 1.05,
            opacity: 1,
            duration: 1,
            ease: 'back.out(1.7)',
            scrollTrigger: {
                trigger: card,
                start: 'top 85%'
            }
        });
    });

    // ── List items stagger ─────────────────────────────────────────
    gsap.utils.toArray('ul.space-y-3, ul.space-y-4, ul.space-y-6').forEach(ul => {
        const items = ul.querySelectorAll('li');
        gsap.fromTo(items, {
            x: -20,
            opacity: 0
        }, {
            x: 0,
            opacity: 1,
            duration: 0.5,
            stagger: 0.08,
            ease: 'power2.out',
            scrollTrigger: {
                trigger: ul,
                start: 'top 88%'
            }
        });
    });

    // ── CTA buttons pulse ──────────────────────────────────────────
    gsap.utils.toArray('button').forEach(btn => {
        if (btn.classList.contains('animate-pulse')) return;
        gsap.to(btn, {
            boxShadow: '0 0 25px rgba(0,255,255,0.5)',
            repeat: -1,
            yoyo: true,
            duration: 2,
            ease: 'sine.inOut',
            paused: true,
            onComplete: () => {}
        });

        btn.addEventListener('mouseenter', () => {
            gsap.to(btn, {
                scale: 1.04,
                duration: 0.3,
                ease: 'power2.out'
            });
        });
        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, {
                scale: 1,
                duration: 0.4,
                ease: 'elastic.out(1,0.5)'
            });
        });
    });

    // ── Floating badge ─────────────────────────────────────────────
    gsap.utils.toArray('.inline-flex.rounded-full').forEach(badge => {
        gsap.fromTo(badge, {
            y: -8,
            opacity: 0
        }, {
            y: 0,
            opacity: 1,
            duration: 0.7,
            ease: 'back.out(2)',
            scrollTrigger: {
                trigger: badge,
                start: 'top 90%'
            }
        });
    });

    // ── Terminal text typewriter simulation ────────────────────────
    const terminalLines = document.querySelectorAll('.space-y-2.font-mono p, .space-y-4.font-mono p');
    if (terminalLines.length) {
        gsap.fromTo(terminalLines, {
            opacity: 0,
            x: -10
        }, {
            opacity: 1,
            x: 0,
            duration: 0.4,
            stagger: 0.15,
            ease: 'power2.out',
            scrollTrigger: {
                trigger: terminalLines[0].closest('div') || terminalLines[0],
                start: 'top 85%'
            }
        });
    }
})();
</script>
"""

def inject_gsap(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove any previously injected animation script
    html = re.sub(r'<script>\s*\(function\(\) \{.*?gsap\.registerPlugin\(ScrollTrigger\).*?\}\)\(\);\s*</script>', '', html, flags=re.DOTALL)

    # Inject before </body>
    if GSAP_SCRIPT.strip() not in html:
        html = html.replace('</body>', GSAP_SCRIPT + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'  ✓ {os.path.basename(filepath)}')

pages = [
    'index.html',
    'about.html',
    'contact.html',
    'arsenal.html',
    'merlin.html',
    'case-studies.html',
    'work-with-me.html',
    'for-agencies.html',
    'for-businesses.html',
    'service-automation.html',
    'service-marketing.html',
    'service-maintenance.html',
    'service-creation.html',
    'legal.html',
    'privacy.html',
]

print('Injecting GSAP animations...')
for page in pages:
    path = os.path.join(BASE, page)
    if os.path.exists(path):
        inject_gsap(path)
    else:
        print(f'  MISSING: {page}')

print('\nDone! All pages now have rich GSAP scroll animations.')
