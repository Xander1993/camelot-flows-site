// ============================================================
// CAMELOT FLOWS — GSAP ANIMATION ENGINE (ZENTRY TIER)
// ============================================================
gsap.registerPlugin(ScrollTrigger, TextPlugin);

const wrapLetters = (element) => {
    if (!element) return;
    const text = element.innerText;
    element.innerHTML = ''; 
    text.split('').forEach(char => {
        const span = document.createElement('span');
        span.className = 'inline-block hero-char';
        span.innerHTML = char === ' ' ? '&nbsp;' : char;
        element.appendChild(span);
    });
};

wrapLetters(document.getElementById('hero-word-1'));

// ------------------------------------------------------------
// 1. LENIS SMOOTH SCROLL
// ------------------------------------------------------------
const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
    smoothWheel: true,
});

lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => { lenis.raf(time * 1000); });
gsap.ticker.lagSmoothing(0);

lenis.stop();

window.addEventListener("load", () => {
    const preloaderTl = gsap.timeline({
        onComplete: () => {
            lenis.start();
            playHeroAnimation();
        }
    });

    preloaderTl
        .to("#loader-percent", { innerHTML: "100%", duration: 1.5, snap: { innerHTML: 1 }, ease: "power2.inOut" })
        .to("#loader-bar", { width: "100%", duration: 1.5, ease: "power2.inOut" }, "<")
        .to("#loader-text", { text: "SYSTEM_READY", duration: 0.2 }, "-=0.2")
        .to("#preloader", { yPercent: -100, duration: 1, ease: "power4.inOut", delay: 0.3 })
        .set("#preloader", { display: "none" });
});

// ------------------------------------------------------------
// 2. KINETIC MARQUEE (ZENTRY STYLE)
// ------------------------------------------------------------
// ИЗМЕНЕНИЕ: Бесконечная бегущая строка, ломающая сетку
(() => {
    gsap.to(".marquee-container", {
        xPercent: -50, // Двигаем ровно на 50% (так как у нас 2 одинаковых блока внутри)
        ease: "none",
        repeat: -1,
        duration: 15 // Скорость движения
    });
})();

// ------------------------------------------------------------
// 3. ZENTRY PORTAL (VIEWPORT TAKEOVER)
// ------------------------------------------------------------
// ИЗМЕНЕНИЕ: Разрывающий экран портал перед Round Table
(() => {
    let mm = gsap.matchMedia();
    
    mm.add("(min-width: 768px)", () => {
        const portalTl = gsap.timeline({
            scrollTrigger: {
                trigger: "#portal-trigger",
                start: "top top",
                end: "+=120%", 
                scrub: 0.5,
                pin: true,
            }
        });

        portalTl
            // Открываем ромб на весь экран
            .to("#zentry-portal", {
                clipPath: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)",
                borderRadius: "0px",
                duration: 1,
                ease: "power2.inOut"
            })
            // Параллакс фона внутри портала
            .fromTo("#portal-bg", 
                { scale: 1.5, rotation: 5 }, 
                { scale: 1, rotation: 0, duration: 1 }, 
            "<")
            // Текст внутри пропадает при расширении
            .to("#portal-text", { scale: 1.5, opacity: 0, duration: 0.5 }, "-=0.5")
            .to("#portal-sub", { opacity: 0, duration: 0.3 }, "-=0.5")
            // ИЗМЕНЕНИЕ: Появление Голограммы Экскалибура после исчезновения текста
            .to("#portal-revelation", { 
                opacity: 1, 
                scale: 1, 
                duration: 1, 
                ease: "back.out(1.5)" 
            }, "-=0.2"); // Запускаем чуть до того, как портал полностью откроется
    });
})();

// ------------------------------------------------------------
// 4. DATA STREAMS
// ------------------------------------------------------------
(() => {
    gsap.utils.toArray(".data-stream").forEach((stream, i) => {
        gsap.fromTo(stream, 
            { x: "-100vw" },
            { 
                x: "100vw", 
                duration: i === 0 ? 3 : 4, 
                repeat: -1, 
                ease: "none", 
                delay: i * 1.5 
            }
        );
    });
})();

// ------------------------------------------------------------
// 5. CUSTOM CURSOR
// ------------------------------------------------------------
(() => {
    if (window.matchMedia("(pointer: fine)").matches) {
        const cursor = document.getElementById("custom-cursor");
        let cursorVisible = false;
        let lastParticleTime = 0;

        gsap.set(cursor, { xPercent: -50, yPercent: -50, zIndex: 9999 });

        window.addEventListener("mousemove", (e) => {
            if (!cursorVisible) {
                cursorVisible = true;
                gsap.to(cursor, { opacity: 1, duration: 0.3 });
            }
            gsap.to(cursor, {
                x: e.clientX,
                y: e.clientY,
                duration: 0.15,
                ease: "power2.out",
            });

            // Comet Tail Particle System (Violet)
            const now = Date.now();
            if (now - lastParticleTime > 12) { // Increased density for smoother trail
                lastParticleTime = now;
                const particle = document.createElement("div");
                
                // Base particle styling (Neon Purple glowing dot with blur)
                particle.className = "fixed w-[6px] h-[6px] bg-neon-purple rounded-full pointer-events-none z-[9998] shadow-[0_0_20px_4px_rgba(191,0,255,0.9)] mix-blend-screen blur-[1px]";
                document.body.appendChild(particle);

                gsap.set(particle, {
                    x: e.clientX,
                    y: e.clientY,
                    xPercent: -50,
                    yPercent: -50,
                });

                // Animate tail dissipating and spreading
                gsap.to(particle, {
                    x: e.clientX + (Math.random() - 0.5) * 15, // Tighter spread for a clean line
                    y: e.clientY + (Math.random() - 0.5) * 15, 
                    scale: 0,
                    opacity: 0,
                    duration: Math.random() * 0.4 + 0.4,
                    ease: "power2.out",
                    onComplete: () => particle.remove()
                });
            }
        });

        document.addEventListener("mouseleave", () => {
            cursorVisible = false;
            gsap.to(cursor, { opacity: 0, duration: 0.3 });
        });

        // Interactive cursor scaling
        const interactiveEls = document.querySelectorAll("a, button, input, .circuit-node");
        interactiveEls.forEach((el) => {
            el.addEventListener("mouseenter", () => {
                gsap.to(cursor, { scale: 3.5, opacity: 0.3, backgroundColor: "#bf00ff", borderColor: "transparent", duration: 0.3, ease: "power2.out" });
            });
            el.addEventListener("mouseleave", () => {
                gsap.to(cursor, { scale: 1, opacity: 1, backgroundColor: "#8b5cf6", borderColor: "transparent", duration: 0.3, ease: "power2.out" });
            });
        });
    }
})();

// ------------------------------------------------------------
// 5.5. MAGNETIC ELEMENTS (TRENDING GSAP TRICK)
// ------------------------------------------------------------
(() => {
    if (window.matchMedia("(pointer: fine)").matches) {
        // Apply magnetic pull to all buttons
        const magnets = document.querySelectorAll("button");
        
        magnets.forEach((magnet) => {
            magnet.addEventListener("mousemove", (e) => {
                const rect = magnet.getBoundingClientRect();
                // Calculate distance from center of button
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                
                // Move button slightly towards mouse
                gsap.to(magnet, {
                    x: x * 0.25,
                    y: y * 0.25,
                    rotation: x * 0.05,
                    duration: 0.4,
                    ease: "power2.out",
                    overwrite: "auto"
                });
            });
            
            magnet.addEventListener("mouseleave", () => {
                // Bounce back using a highly kinetic elastic ease
                gsap.to(magnet, {
                    x: 0,
                    y: 0,
                    rotation: 0,
                    duration: 0.8,
                    ease: "elastic.out(1, 0.3)",
                    overwrite: "auto"
                });
            });
        });
    }
})();

// ------------------------------------------------------------
// 6. HERO PARALLAX & KINETIC TYPOGRAPHY REVEAL
// ------------------------------------------------------------
const playHeroAnimation = () => {
    const heroTl = gsap.timeline();

    heroTl
        .from("#hero-badge", { y: 60, opacity: 0, duration: 1, ease: "power4.out" })
        .from(".hero-char", { 
            z: 400, 
            rotationX: -90, 
            opacity: 0, 
            stagger: 0.04, 
            duration: 1.2,
            ease: "back.out(1.5)", 
            transformOrigin: "50% 50% -50px" 
        }, "-=0.8")
        .from("#hero-word-2", {
            yPercent: 100,
            duration: 1.2,
            ease: "power4.out"
        }, "-=1.0")
        .from("#hero-p",     { y: 50, opacity: 0, duration: 1, ease: "power4.out" }, "-=0.8")
        .from("#hero-btns",  { y: 40, opacity: 0, duration: 1, ease: "power4.out" }, "-=0.7")
        .from("#hero-stats", { y: 30, opacity: 0, duration: 1, ease: "power4.out" }, "-=0.6");
};

(() => {
    const orbs = document.querySelectorAll(".bg-orb");
    const multipliers = [0.03, -0.04, 0.025]; 

    if (window.matchMedia("(prefers-reduced-motion: no-preference)").matches) {
        window.addEventListener("mousemove", (e) => {
            const cx = window.innerWidth / 2;
            const cy = window.innerHeight / 2;
            const dx = (e.clientX - cx) / cx;
            const dy = (e.clientY - cy) / cy;

            orbs.forEach((orb, i) => {
                const m = multipliers[i] || 0.03;
                gsap.to(orb, {
                    x: -dx * m * window.innerWidth,
                    y: -dy * m * window.innerHeight,
                    duration: 1.2,
                    ease: "power1.out",
                });
            });

            gsap.utils.toArray(".parallax-float").forEach((el) => {
                const depth = parseFloat(el.getAttribute("data-depth")) || 0.1;
                gsap.to(el, {
                    x: dx * depth * 80,
                    y: dy * depth * 80,
                    duration: 1.5,
                    ease: "power2.out",
                });
            });
        });

        gsap.utils.toArray(".parallax-float").forEach((el) => {
            gsap.to(el, {
                y: "+=15",
                rotation: "+=10",
                duration: "random(3, 5)",
                repeat: -1,
                yoyo: true,
                ease: "sine.inOut"
            });
            
            const depth = parseFloat(el.getAttribute("data-depth")) || 0.1;
            gsap.to(el, {
                yPercent: depth * 300,
                rotation: depth * 100,
                ease: "none",
                scrollTrigger: {
                    trigger: "#hero",
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }
            });
        });
    }
})();

(() => {
    gsap.to("#literal-round-table", {
        rotation: 360,
        duration: 50,
        repeat: -1,
        ease: "none"
    });
    gsap.to(".rt-icon", {
        rotation: -360,
        duration: 50,
        repeat: -1,
        ease: "none"
    });
})();

// ------------------------------------------------------------
// 7. CARD STACK — AWWWARDS HORIZONTAL SCROLL EFFECT
// ------------------------------------------------------------
(() => {
    let mm = gsap.matchMedia();

    mm.add("(min-width: 768px)", () => {
        const stackWrapper = document.getElementById("card-scroll-wrapper");
        const stackContent = document.getElementById("card-stack");
        
        // Remove any old absolute positioning properties
        gsap.set(".stack-card", { clearProps: "all" });

        const getScrollAmount = () => {
            let offset = stackContent.scrollWidth - stackWrapper.offsetWidth;
            return offset > 0 ? -(offset + 24) : 0; // Add small padding so right edge is fully visible
        };

        const stackTl = gsap.timeline({
            scrollTrigger: {
                trigger: "#round-table",
                start: "top top",
                end: () => `+=${stackContent.scrollWidth}`, // Scroll dist matches width
                pin: true,
                scrub: 1, 
                invalidateOnRefresh: true
            },
        });

        stackTl.to(stackContent, {
            x: getScrollAmount,
            duration: 1,
            ease: "none"
        });

        return () => { gsap.set(".stack-card", { clearProps: "all" }); gsap.set(stackContent, { clearProps: "all" }); };
    });

    mm.add("(max-width: 767px)", () => {
        gsap.set(".stack-card", { clearProps: "all" });
        gsap.set("#card-stack", { clearProps: "all" });
    });
})();

// ------------------------------------------------------------
// 8. TERMINAL BOOT SEQUENCE
// ------------------------------------------------------------
(() => {
    const steps = gsap.utils.toArray(".terminal-step");

    steps.forEach((step, i) => {
        gsap.from(step, {
            scrollTrigger: {
                trigger: step,
                start: "top 88%",
                toggleActions: "play none none none",
            },
            y: 40,
            opacity: 0,
            duration: 0.8,
            delay: i * 0.1,
            ease: "power3.out",
        });
    });

    gsap.from("#terminal-hub", {
        scrollTrigger: {
            trigger: "#terminal-hub",
            start: "top 85%",
            toggleActions: "play none none none",
        },
        scale: 0.85,
        opacity: 0,
        duration: 1.2,
        ease: "power4.out",
    });
})();

// ------------------------------------------------------------
// 9. STAR WARS PRICING CRAWL ANIMATION
// ------------------------------------------------------------
(() => {
    // 3D Perspective Scroll for Pricing
    let mm = gsap.matchMedia();
    
    mm.add("(min-width: 768px)", () => {
        const crawlContent = document.querySelector('.crawl-content');
        
        // Initial setup
        gsap.set(crawlContent, { 
            rotationX: 25, 
            yPercent: 0, 
            z: 0,
            opacity: 0,
            transformOrigin: "50% 100%"
        });

        const crawlTl = gsap.timeline({
            scrollTrigger: {
                trigger: "#starwars-pricing",
                start: "top top",
                end: "+=250%", // Distance to scroll
                pin: true,
                scrub: 1.5,
            }
        });

        crawlTl
            .to(crawlContent, { opacity: 1, duration: 0.1 }, 0)
            .to(crawlContent, {
                yPercent: -180, // Scroll up past screen
                z: -1200,       // Move deep into Z space
                rotationX: 45,  // Lean back further
                ease: "power1.inOut",
                duration: 1
            }, 0)
            .to(crawlContent, { opacity: 0, duration: 0.2 }, 0.8); // Fade out at the end

        // Animate the hologram sword subtly
        gsap.to('.hologram-sword-img', {
            y: "+=30",
            rotation: 3,
            scale: 1.05,
            duration: 4,
            repeat: -1,
            yoyo: true,
            ease: "sine.inOut"
        });

        // Generate circuit wires drawing effect
        gsap.utils.toArray(".circuit-wire").forEach(wire => {
            const length = wire.getTotalLength();
            gsap.set(wire, { strokeDasharray: length, strokeDashoffset: length });
            
            gsap.to(wire, {
                strokeDashoffset: 0,
                scrollTrigger: {
                    trigger: "#starwars-pricing",
                    start: "top bottom", // Start when section enters screen
                    end: "bottom top", 
                    scrub: 1.5
                }
            });
        });

        // Pulse the circuit nodes
        gsap.utils.toArray(".circuit-node").forEach(node => {
            gsap.fromTo(node, 
                { scale: 0.5, opacity: 0 },
                {
                    scale: 1, 
                    opacity: 1,
                    scrollTrigger: {
                        trigger: "#starwars-pricing",
                        start: "top 80%",
                        toggleActions: "play none none reverse"
                    },
                    duration: 0.5,
                    ease: "back.out(2)"
                }
            );
        });

    });

    // Animate the New Sections
    gsap.from(".armory-visual", {
        scrollTrigger: { trigger: "#grand-armory", start: "top 85%" },
        x: -80, opacity: 0, duration: 1.2, ease: "power4.out"
    });
    gsap.from(".armory-content", {
        scrollTrigger: { trigger: "#grand-armory", start: "top 85%" },
        x: 80, opacity: 0, duration: 1.2, ease: "power4.out", delay: 0.2
    });

    gsap.from(".alchemy-visual", {
        scrollTrigger: { trigger: "#alchemy-sanctum", start: "top 85%" },
        x: 80, opacity: 0, duration: 1.2, ease: "power4.out"
    });
    gsap.from(".alchemy-content", {
        scrollTrigger: { trigger: "#alchemy-sanctum", start: "top 85%" },
        x: -80, opacity: 0, duration: 1.2, ease: "power4.out", delay: 0.2
    });

    gsap.from(".vault-visual", {
        scrollTrigger: { trigger: "#obsidian-vault", start: "top 85%" },
        x: -80, opacity: 0, duration: 1.2, ease: "power4.out"
    });
    gsap.from(".vault-content", {
        scrollTrigger: { trigger: "#obsidian-vault", start: "top 85%" },
        x: 80, opacity: 0, duration: 1.2, ease: "power4.out", delay: 0.2
    });

    gsap.from(".aug-visual", {
        scrollTrigger: { trigger: "#cybernetic-augmentations", start: "top 85%" },
        x: 80, opacity: 0, duration: 1.2, ease: "power4.out"
    });
    gsap.from(".aug-content", {
        scrollTrigger: { trigger: "#cybernetic-augmentations", start: "top 85%" },
        x: -80, opacity: 0, duration: 1.2, ease: "power4.out", delay: 0.2
    });

    // ------------------------------------------------------------
    // 9.5 SKEW ON SCROLL (TRENDING FLUIDITY EFFECT)
    // ------------------------------------------------------------
    let proxy = { skew: 0 },
        skewSetter = gsap.quickSetter(".glass-panel, .stack-card, .armory-visual, .vault-visual, .aug-visual", "skewY", "deg"),
        clamp = gsap.utils.clamp(-3, 3); // Limit skew to subtle degrees to avoid layout breaking

    ScrollTrigger.create({
        onUpdate: (self) => {
            let skew = clamp(self.getVelocity() / -400); // Inverse velocity tied to skew
            if (Math.abs(skew) > Math.abs(proxy.skew)) {
                proxy.skew = skew;
                gsap.to(proxy, {
                    skew: 0,
                    duration: 0.8,
                    ease: "power3",
                    overwrite: true,
                    onUpdate: () => skewSetter(proxy.skew)
                });
            }
        }
    });

    // Image slow zoom effect
    gsap.utils.toArray('.img-zoom').forEach(img => {
        gsap.to(img, {
            scale: 1.15,
            scrollTrigger: {
                trigger: img,
                start: "top bottom",
                end: "bottom top",
                scrub: true
            }
        });
    });

})();