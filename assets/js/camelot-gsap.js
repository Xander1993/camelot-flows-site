        // ============================================================
        // CAMELOT FLOWS — GSAP ANIMATION ENGINE (ZENTRY TIER)
        // ============================================================
        const cfFallbackHidePreloader = () => {
            const pre = document.getElementById('preloader');
            if (pre && pre.dataset.cfHidden !== '1') {
                pre.dataset.cfHidden = '1';
                pre.style.transition = 'opacity .25s ease';
                pre.style.opacity = '0';
                pre.style.pointerEvents = 'none';
                setTimeout(function () { pre.style.display = 'none'; }, 260);
            }
            // Only force-reveal hero elements when GSAP failed to load entirely.
            // When GSAP is present, playHeroAnimation() owns the reveal via fromTo.
            if (!window.gsap) {
                document.querySelectorAll("#hero-badge, #hero-word-1, #hero-word-2, #hero-p, #hero-btns, #hero-stats").forEach((node) => {
                    node.style.opacity = "1";
                    node.style.visibility = "visible";
                    node.style.transform = "none";
                });
            }
            try { window.lenis && window.lenis.start(); } catch (_) { }
        };

        setTimeout(cfFallbackHidePreloader, 1500);

        if (!window.gsap || !window.ScrollTrigger || !window.TextPlugin || !window.Lenis) {
            document.documentElement.classList.add('cf-motion-fallback');
            document.addEventListener('DOMContentLoaded', () => {
                cfFallbackHidePreloader();

                document.addEventListener('click', (e) => {
                    const btn = e.target.closest('#theme-toggle, [data-cf-theme-toggle]');
                    if (!btn) return;
                    e.preventDefault();
                    const cur = document.documentElement.getAttribute('data-theme') || 'cozy';
                    const next = cur === 'night' ? 'cozy' : 'night';
                    document.documentElement.setAttribute('data-theme', next);
                    try { localStorage.setItem('cf_theme', next); } catch (_) { }
                    document.cookie = 'cf_theme=' + next + '; path=/; domain=.camelotflows.dev; max-age=31536000; SameSite=Lax';
                });

                const page = (window.location.pathname.split('/').pop() || 'index.html').split('?')[0] || 'index.html';
                document.querySelectorAll('nav a[href]').forEach((link) => {
                    const href = (link.getAttribute('href') || '').split('#')[0].split('?')[0];
                    if (href === page) link.classList.add('nav-current');
                });
            });
        } else {
        gsap.registerPlugin(ScrollTrigger, TextPlugin);

        // FAILSAFE — pure DOM, registered FIRST so a thrown error below
        // can never permanently strand the preloader (1.5s ceiling).
        setTimeout(function () {
            var pre = document.getElementById('preloader');
            if (!pre || pre.dataset.cfHidden === '1') return;
            pre.dataset.cfHidden = '1';
            pre.style.transition = 'opacity .25s ease';
            pre.style.opacity = '0';
            pre.style.pointerEvents = 'none';
            setTimeout(function () { pre.style.display = 'none'; }, 260);
            try { window.lenis && window.lenis.start(); } catch (_) { }
        }, 1500);

        // SKIP-PRELOADER GATE — once-per-session: first load shows the
        // animated loader; every subsequent navigation in the same session
        // skips it instantly so internal nav feels snappy.
        const SKIP_PRELOADER = sessionStorage.getItem('cf_loaded') === '1';
        if (!SKIP_PRELOADER) sessionStorage.setItem('cf_loaded', '1');
        if (SKIP_PRELOADER) {
            document.documentElement.classList.add('cf-skip-preloader');
        }

        const wrapLetters = (element) => {
            if (!element) return;
            // textContent (not innerText) — innerText returns "" on visibility:hidden
            // elements, which gsap.set(autoAlpha:0) has already applied here.
            const text = element.textContent;
            element.innerHTML = '';
            // Chars are grouped per word inside a nowrap wrapper: bare
            // inline-block char spans let the browser break lines mid-word
            // ("A SITE AS GOOD A / S" on 390px). Real spaces between the
            // wrappers keep textContent idempotent for re-wraps on language
            // switch.
            text.split(/\s+/).filter(Boolean).forEach((word, i) => {
                if (i > 0) element.appendChild(document.createTextNode(' '));
                const wordSpan = document.createElement('span');
                wordSpan.className = 'inline-block whitespace-nowrap hero-word';
                wordSpan.style.transformStyle = 'preserve-3d';
                word.split('').forEach(char => {
                    const span = document.createElement('span');
                    span.className = 'inline-block hero-char';
                    span.textContent = char;
                    wordSpan.appendChild(span);
                });
                element.appendChild(wordSpan);
            });
        };

        // NOTE: wrapLetters() is called inside playHeroAnimation, AFTER i18n
        // has applied translations. Wrapping at script-load would create spans
        // that the i18n DOMContentLoaded pass then destroys via textContent=...,
        // leaving the .hero-char animation with no targets.

        // HERO PRE-HIDE — these are the targets playHeroAnimation animates
        // FROM. We set autoAlpha: 0 synchronously so the natural state
        // never paints during the gap between defer-script execution and
        // the preloader timeline completing. Pairs with .js CSS hide for
        // coverage during initial parse.
        const _heroTargets = ["#hero-badge", "#hero-word-1", "#hero-word-2", "#hero-p", "#hero-btns", "#hero-stats"]
            .filter(sel => document.querySelector(sel));
        if (_heroTargets.length) gsap.set(_heroTargets, { autoAlpha: 0 });

        // ------------------------------------------------------------
        // 1. LENIS SMOOTH SCROLL
        // ------------------------------------------------------------
        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            smoothWheel: true,
        });
        window.lenis = lenis;  // expose for the DOM failsafe above

        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time) => { lenis.raf(time * 1000); });
        gsap.ticker.lagSmoothing(0);

        lenis.stop();

        const hidePreloader = () => {
            if (window._preloaderRun) return;
            window._preloaderRun = true;
            // Mark as handled so cfFallbackHidePreloader skips the preloader entirely.
            const pre = document.getElementById('preloader');
            if (pre) pre.dataset.cfHidden = '1';

            // Skip path — no animated loader on internal nav or when preloader element is absent.
            if (SKIP_PRELOADER || !pre) {
                if (pre) pre.style.display = 'none';
                lenis.start();
                playHeroAnimation();
                return;
            }

            const preloaderTl = gsap.timeline({
                onComplete: () => {
                    lenis.start();
                    playHeroAnimation();
                }
            });

            preloaderTl
                .to("#loader-percent", { innerHTML: "100%", duration: 1.5, snap: { innerHTML: 1 }, ease: "power2.inOut" })
                .to("#loader-bar", { width: "100%", duration: 1.5, ease: "power2.inOut" }, "<")
                .to("#loader-text", { text: (window.cfI18n && window.cfI18n.t('common.preloader_ready')) || "SYSTEM_READY", duration: 0.2 }, "-=0.2")
                .to("#preloader", { yPercent: -100, duration: 1, ease: "power4.inOut", delay: 0.3 })
                .set("#preloader", { display: "none" });
        };

        if (SKIP_PRELOADER) {
            // Defer one animation frame so all const declarations in this script
            // (including playHeroAnimation at line ~297) are fully initialized
            // before hidePreloader calls them. Calling synchronously here would
            // hit the temporal dead zone and silently leave the hero hidden.
            requestAnimationFrame(hidePreloader);
        } else {
            window.addEventListener("load", hidePreloader);
            setTimeout(hidePreloader, 800); // Secondary failsafe (the 1.5s DOM one is above)
        }

        // 3. PORTAL — sync: pin+scrub needs synchronous setup
        (() => {
            if (!document.getElementById('portal-trigger')) return;
            if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
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

        // Defer non-critical scroll/animation setup to idle — eliminates forced reflows from TBT window
        ;(window.requestIdleCallback || function(fn,o){setTimeout(fn,(o&&o.timeout)||100);})(function(){

        // ------------------------------------------------------------
        // 2. KINETIC MARQUEE (ZENTRY STYLE)
        // ------------------------------------------------------------
        // ИЗМЕНЕНИЕ: Бесконечная бегущая строка, ломающая сетку
        (() => {
            if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
            if (!document.querySelector(".marquee-container")) return;
            gsap.to(".marquee-container", {
                xPercent: -50, // Двигаем ровно на 50% (так как у нас 2 одинаковых блока внутри)
                ease: "none",
                repeat: -1,
                duration: 15 // Скорость движения
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
            if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
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

        }, { timeout: 2000 });

        // ------------------------------------------------------------
        // 6. HERO PARALLAX & KINETIC TYPOGRAPHY REVEAL
        // ------------------------------------------------------------
        const playHeroAnimation = () => {
            window._heroAnimStarted = true;
            if (!document.getElementById('hero-badge')) return; // Non-home pages: no-op
            // Wrap the hero word AFTER i18n has run, so the per-char spans
            // contain the translated letters and aren't wiped by a later
            // textContent assignment. Idempotent — re-wrapping plain text
            // gives the same result.
            wrapLetters(document.getElementById('hero-word-1'));
            // Targets were pre-hidden (autoAlpha: 0) at script load to prevent
            // a flash. We use fromTo so the from-state is explicit and the
            // tweens animate to autoAlpha: 1 regardless of pre-set state.
            const heroTl = gsap.timeline();

            heroTl
                .fromTo("#hero-badge",
                    { y: 60, autoAlpha: 0 },
                    { y: 0, autoAlpha: 1, duration: 1, ease: "power4.out" })
                // Unhide the word-1 wrapper so the per-char animation is visible.
                .set("#hero-word-1", { autoAlpha: 1 }, "<")
                .from(".hero-char", {
                    z: 400,
                    rotationX: -90,
                    opacity: 0,
                    stagger: 0.04,
                    duration: 1.2,
                    ease: "back.out(1.5)",
                    transformOrigin: "50% 50% -50px"
                }, "-=0.8")
                .fromTo("#hero-word-2",
                    { yPercent: 100, autoAlpha: 0 },
                    { yPercent: 0, autoAlpha: 1, duration: 1.2, ease: "power4.out" }, "-=1.0")
                .fromTo("#hero-p",
                    { y: 50, autoAlpha: 0 },
                    { y: 0, autoAlpha: 1, duration: 1, ease: "power4.out" }, "-=0.8")
                .fromTo("#hero-btns",
                    { y: 40, autoAlpha: 0 },
                    { y: 0, autoAlpha: 1, duration: 1, ease: "power4.out" }, "-=0.7")
                .fromTo("#hero-stats",
                    { y: 30, autoAlpha: 0 },
                    { y: 0, autoAlpha: 1, duration: 1, ease: "power4.out" }, "-=0.6");
        };

        // SYNC: sections that set initial visibility state

        // ------------------------------------------------------------
        // 7. CARD STACK — AWWWARDS HORIZONTAL SCROLL EFFECT
        // ------------------------------------------------------------
        (() => {
            let mm = gsap.matchMedia();

            mm.add("(min-width: 768px)", () => {
                const stackWrapper = document.getElementById("card-scroll-wrapper");
                const stackContent = document.getElementById("card-stack");

                if (!stackWrapper || !stackContent) return;

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
            if (!document.getElementById('terminal-hub')) return;
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
            const pricingSection = document.getElementById("starwars-pricing");
            if (!pricingSection) return;

            // 3D Perspective Scroll for Pricing
            let mm = gsap.matchMedia();

            mm.add("(min-width: 768px)", () => {
                const crawlContent = document.querySelector('.crawl-content');
                if (!crawlContent) return;

                // Blueprint / background elements inside the section
                const blueprintEls = pricingSection.querySelectorAll(
                    '.pricing-blueprint-system, .pricing-route-card, .hologram-sword-img, .starfield-anim'
                );

                // Start section invisible so it doesn't flash blueprint before pin,
                // but fade it in while it enters the viewport — snapping it on only
                // at pin start left a full blank viewport during entry
                gsap.set(pricingSection, { opacity: 0 });
                gsap.to(pricingSection, {
                    opacity: 1,
                    ease: "none",
                    scrollTrigger: {
                        trigger: "#starwars-pricing",
                        start: "top 95%",
                        end: "top 40%",
                        scrub: true,
                    }
                });
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
                        end: "+=120%",
                        pin: true,
                        scrub: 1.5,
                    }
                });

                crawlTl
                    // Crawl fades in
                    .to(crawlContent, { opacity: 1, duration: 0.1 }, 0)
                    // Crawl scrolls up
                    .to(crawlContent, {
                        yPercent: -180,
                        z: -1200,
                        rotationX: 45,
                        ease: "power1.inOut",
                        duration: 1
                    }, 0)
                    // Everything fades out together at 78% — blueprint elements + crawl + section bg
                    .to(crawlContent, { opacity: 0, duration: 0.06 }, 0.78)
                    .to(blueprintEls, { opacity: 0, duration: 0.14, stagger: 0 }, 0.78)
                    .to(pricingSection, { opacity: 0, duration: 0.22 }, 0.78);

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

                gsap.to(".pricing-blueprint-lines", {
                    rotation: 1.6,
                    scale: 1.015,
                    transformOrigin: "50% 50%",
                    duration: 7,
                    repeat: -1,
                    yoyo: true,
                    ease: "sine.inOut"
                });

                gsap.to(".pricing-blueprint-core", {
                    y: -10,
                    scale: 1.015,
                    duration: 5,
                    repeat: -1,
                    yoyo: true,
                    ease: "sine.inOut"
                });

                gsap.to(".pricing-route-card", {
                    y: (i) => i % 2 === 0 ? -18 : 18,
                    rotation: (i) => i % 2 === 0 ? "-=1.5" : "+=1.5",
                    duration: 4,
                    repeat: -1,
                    yoyo: true,
                    stagger: 0.18,
                    ease: "sine.inOut"
                });

                gsap.to(".pricing-blueprint-route, .pricing-blueprint-ring", {
                    strokeDashoffset: -80,
                    duration: 8,
                    repeat: -1,
                    ease: "none"
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
            });

            mm.add("(max-width: 767px)", () => {
                if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

                const crawlContainer = pricingSection.querySelector(".crawl-container");
                const crawlContent = pricingSection.querySelector(".crawl-content");
                const pricingCards = gsap.utils.toArray(pricingSection.querySelectorAll(".pricing-card-sw"));
                if (!crawlContainer || !crawlContent || !pricingCards.length) return;

                pricingSection.classList.add("is-mobile-crawl");

                const getStartY = () => Math.max(window.innerHeight * 0.58, 340);
                const getEndY = () => {
                    const readableExit = window.innerHeight * 0.42;
                    return -(crawlContent.scrollHeight - readableExit);
                };
                const getScrollLength = () => {
                    const contentTravel = crawlContent.scrollHeight * 1.35;
                    return "+=" + Math.max(contentTravel, window.innerHeight * 3.2);
                };

                gsap.set(crawlContent, {
                    y: getStartY(),
                    z: 50,
                    rotationX: 10,
                    opacity: 1,
                    transformOrigin: "50% 100%",
                    force3D: true
                });

                gsap.set(pricingCards, {
                    transformPerspective: 1400,
                    force3D: true
                });

                const mobileCrawlTl = gsap.timeline({
                    scrollTrigger: {
                        trigger: pricingSection,
                        start: "top top",
                        end: getScrollLength,
                        pin: true,
                        pinSpacing: true,
                        scrub: 1.1,
                        anticipatePin: 1,
                        invalidateOnRefresh: true,
                        onRefresh: () => {
                            gsap.set(crawlContent, { y: getStartY() });
                        }
                    }
                });

                mobileCrawlTl
                    .to(crawlContent, {
                        y: getEndY,
                        z: -360,
                        rotationX: 24,
                        ease: "none",
                        duration: 1
                    }, 0)
                    .to(crawlContent, {
                        opacity: 0,
                        ease: "power1.in",
                        duration: 0.12
                    }, 0.9);

                ScrollTrigger.refresh();

                return () => {
                    pricingSection.classList.remove("is-mobile-crawl");
                    mobileCrawlTl.kill();
                    gsap.set(crawlContent, { clearProps: "transform,opacity,willChange" });
                    gsap.set(pricingCards, { clearProps: "transform,transformPerspective,willChange" });
                };
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

        })();


        // Animate the New Sections
        if (document.getElementById("grand-armory")) {
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

            if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
                gsap.utils.toArray(".cf-artifact-frame").forEach((frame) => {
                    const core = frame.querySelector(".cf-artifact-core");
                    const img = frame.querySelector(".cf-artifact-img");
                    const details = frame.querySelectorAll(".cf-artifact-node, .cf-artifact-label");

                    const revealTl = gsap.timeline({
                        scrollTrigger: {
                            trigger: frame,
                            start: "top 82%",
                            end: "bottom 45%",
                            scrub: 0.8
                        }
                    });

                    if (core) {
                        revealTl.fromTo(core,
                            { clipPath: "polygon(0% 0%, 14% 0%, 8% 100%, 0% 92%)" },
                            { clipPath: "polygon(5% 0%, 100% 0%, 94% 100%, 0% 91%)", duration: 1, ease: "power2.out" },
                            0
                        );
                    }

                    if (img) {
                        revealTl.fromTo(img,
                            { scale: 1.2, xPercent: -4, filter: "saturate(0.82) contrast(0.92)" },
                            { scale: 1.04, xPercent: 0, filter: "saturate(1) contrast(1)", duration: 1, ease: "power2.out" },
                            0
                        );
                    }

                    if (details.length) {
                        revealTl.fromTo(details,
                            { autoAlpha: 0, y: 18 },
                            { autoAlpha: 1, y: 0, stagger: 0.08, duration: 0.45, ease: "power3.out" },
                            0.28
                        );
                    }
                });
            }
        }

        // Defer scroll-driven animations to idle — eliminates forced reflows from TBT
        ;(window.requestIdleCallback || function(fn,o){setTimeout(fn,(o&&o.timeout)||100);})(function(){

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
            if (!document.getElementById('literal-round-table')) return;
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
        // 9.5 SKEW ON SCROLL (TRENDING FLUIDITY EFFECT)
        // ------------------------------------------------------------
        let proxy = { skew: 0 },
            skewSetter = gsap.quickSetter(".glass-panel:not(.cf-artifact-frame):not(.cf-rise), .stack-card", "skewY", "deg"),
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
        gsap.utils.toArray('.img-zoom:not(.cf-artifact-img)').forEach(img => {
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

        // One-shot flash zoom entrance: snaps in from 1.14 → 1 with fast ease-out
        gsap.utils.toArray('.img-flash-zoom').forEach(img => {
            gsap.fromTo(img,
                { scale: 1.55 },
                {
                    scale: 1,
                    duration: 0.16,
                    ease: 'expo.out',
                    scrollTrigger: {
                        trigger: img,
                        start: 'top 88%',
                        once: true
                    }
                }
            );
        });

        }, { timeout: 2000 });

        // ============================================================
        // 10. THEME TOGGLE (cozy ↔ night) with View Transitions
        // ============================================================
        (() => {
            const setThemeCookie = (v) => {
                document.cookie = 'cf_theme=' + v + '; path=/; domain=.camelotflows.dev; max-age=31536000; SameSite=Lax';
            };
            const setTheme = (next) => {
                document.documentElement.setAttribute('data-theme', next);
                try { localStorage.setItem('cf_theme', next); } catch (_) { }
                setThemeCookie(next);
            };

            const toggle = () => {
                const cur = document.documentElement.getAttribute('data-theme') || 'cozy';
                const next = cur === 'night' ? 'cozy' : 'night';
                if (document.startViewTransition) {
                    document.startViewTransition(() => setTheme(next));
                } else {
                    setTheme(next);
                }
            };

            document.addEventListener('click', (e) => {
                const btn = e.target.closest('#theme-toggle, [data-cf-theme-toggle]');
                if (!btn) return;
                e.preventDefault();
                toggle();
            });
        })();

        ;(window.requestIdleCallback || function(fn,o){setTimeout(fn,(o&&o.timeout)||100);})(function(){
        // ============================================================
        // 11. MAGNETIC CTAs + CUSTOM CURSOR (premium polish)
        // ============================================================
        (() => {
            // Skip on touch devices and reduced-motion users.
            if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
            if (window.matchMedia("(hover: none)").matches) return;

            // -- Custom cursor blob ----------------------------------
            const cursor = document.createElement('div');
            cursor.className = 'cf-cursor';
            cursor.setAttribute('aria-hidden', 'true');
            document.body.appendChild(cursor);

            const xTo = gsap.quickTo(cursor, "x", { duration: 0.4, ease: "power3" });
            const yTo = gsap.quickTo(cursor, "y", { duration: 0.4, ease: "power3" });

            window.addEventListener('mousemove', (e) => {
                xTo(e.clientX);
                yTo(e.clientY);
            });

            const interactiveSel = 'a, button, [role=button], input, textarea, select, .glass-card, .button, [data-cf-magnetic]';
            document.body.addEventListener('mouseover', (e) => {
                if (e.target.closest(interactiveSel)) cursor.classList.add('is-hover');
            });
            document.body.addEventListener('mouseout', (e) => {
                if (e.target.closest(interactiveSel)) cursor.classList.remove('is-hover');
            });

            // -- Magnetic pull on primary CTAs and nav items ----------
            const magnetTargets = document.querySelectorAll('.button.primary, [data-cf-magnetic], .nav-cta, .theme-toggle, .lang-trigger');
            magnetTargets.forEach((el) => {
                const strength = parseFloat(el.dataset.cfMagnetStrength || "0.25");
                el.addEventListener('mousemove', (e) => {
                    const r = el.getBoundingClientRect();
                    const dx = (e.clientX - (r.left + r.width / 2)) * strength;
                    const dy = (e.clientY - (r.top + r.height / 2)) * strength;
                    gsap.to(el, { x: dx, y: dy, duration: 0.4, ease: "power3" });
                });
                el.addEventListener('mouseleave', () => {
                    gsap.to(el, { x: 0, y: 0, duration: 0.5, ease: "elastic.out(1, 0.4)" });
                });
            });
        })();

        // ============================================================
        // 12. SCROLL PROGRESS BAR (long-page polish)
        // ============================================================
        (() => {
            const bar = document.querySelector('.scroll-progress');
            if (!bar) return;
            ScrollTrigger.create({
                start: 0,
                end: "max",
                onUpdate: (self) => { bar.style.transform = 'scaleX(' + self.progress + ')'; }
            });
        })();

        }, { timeout: 2000 });

        // ============================================================
        // 13. ACTIVE NAV ITEM — highlight the link that matches the current page
        // ============================================================
        (() => {
            const normalizeRoute = (value) => {
                const path = new URL(value, window.location.origin).pathname
                    .replace(/^\/(?:ro|ru)(?=\/|$)/, '')
                    .replace(/\.html$/, '')
                    .replace(/\/$/, '');
                return path || '/';
            };
            const page = normalizeRoute(window.location.href);
            document.querySelectorAll('nav a[href]').forEach((link) => {
                if (normalizeRoute(link.href) === page) {
                    link.classList.add('nav-current');
                }
            });
        })();

        // ============================================================
        // 14. LANGUAGE SWITCHER (vertical letter stack)
        //     Opens a stacked menu (EN / RO / RU). Each option contains a
        //     normal crawlable link to the corresponding language URL.
        // ============================================================
        (() => {
            const REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

            function reorderMenuItems(menu, lang) {
                const order = [lang, ...['en', 'ro', 'ru'].filter(x => x !== lang)];
                order.forEach((code) => {
                    const li = menu.querySelector('[data-lang="' + code + '"]');
                    if (li) menu.appendChild(li);
                });
                menu.querySelectorAll('li').forEach((li) => {
                    li.classList.toggle('is-current', li.dataset.lang === lang);
                });
            }

            function syncTriggerLabel(switcher, lang) {
                const cur = switcher.querySelector('[data-cf-lang-current]');
                if (cur) cur.textContent = lang.toUpperCase();
            }

            function closeSwitcher(switcher) {
                if (!switcher.classList.contains('is-open')) return;
                switcher.classList.remove('is-open');
                const trigger = switcher.querySelector('.lang-trigger');
                if (trigger) trigger.setAttribute('aria-expanded', 'false');
                const menu = switcher.querySelector('.lang-menu');
                if (menu) {
                    // Match the CSS transition (0.35s) before re-hiding from a11y tree
                    setTimeout(() => {
                        if (!switcher.classList.contains('is-open')) menu.setAttribute('hidden', '');
                    }, 360);
                }
            }

            function openSwitcher(switcher) {
                const lang = (window.cfI18n && window.cfI18n.current()) || 'en';
                const menu = switcher.querySelector('.lang-menu');
                if (menu) {
                    reorderMenuItems(menu, lang);
                    menu.removeAttribute('hidden');
                }
                switcher.classList.add('is-open');
                const trigger = switcher.querySelector('.lang-trigger');
                if (trigger) trigger.setAttribute('aria-expanded', 'true');
            }

            function selectLang(switcher, lang) {
                if (!window.cfI18n) return;
                const prev = window.cfI18n.current();
                if (lang === prev) { closeSwitcher(switcher); return; }

                const menu = switcher.querySelector('.lang-menu');
                const target = menu && menu.querySelector('[data-lang="' + lang + '"]');
                const targetLink = target && target.querySelector('a[href]');
                const trigger = switcher.querySelector('.lang-trigger');
                const triggerLabel = trigger && trigger.querySelector('[data-cf-lang-current]');

                const finish = () => {
                    if (!targetLink) { closeSwitcher(switcher); return; }
                    try { localStorage.setItem('cf_lang', lang); } catch (_) { }
                    try { document.cookie = 'cf_lang=' + lang + '; path=/; domain=.camelotflows.dev; max-age=31536000; SameSite=Lax'; } catch (_) { }
                    window.location.assign(targetLink.href);
                };

                if (REDUCED || !target || !triggerLabel || !window.gsap) {
                    finish();
                    return;
                }

                // FLIP: tween chosen <li> into the trigger label position.
                const tRect = triggerLabel.getBoundingClientRect();
                const lRect = target.getBoundingClientRect();
                const dx = (tRect.left + tRect.width / 2) - (lRect.left + lRect.width / 2);
                const dy = (tRect.top + tRect.height / 2) - (lRect.top + lRect.height / 2);

                target.classList.add('is-flying');

                const others = Array.from(menu.querySelectorAll('li')).filter(li => li !== target);
                gsap.to(others, { autoAlpha: 0, y: -6, duration: 0.18, ease: 'power2.in' });

                gsap.to(target, {
                    x: dx,
                    y: dy,
                    scale: 0.92,
                    duration: 0.42,
                    ease: 'power3.inOut',
                    onComplete: () => {
                        // Close BEFORE clearProps: removing .is-open sets CSS opacity:0
                        // on li items, so clearing GSAP's inline opacity:0 is a no-op —
                        // no CSS transition fires, no black flash between states.
                        closeSwitcher(switcher);
                        gsap.set(target, { clearProps: 'all' });
                        gsap.set(others, { clearProps: 'all' });
                        target.classList.remove('is-flying');
                        finish();
                    }
                });
            }

            // ---- Bind handlers ----
            document.addEventListener('click', (e) => {
                const trigger = e.target.closest('.lang-trigger');
                if (trigger) {
                    e.preventDefault();
                    const switcher = trigger.closest('[data-cf-lang-switcher]');
                    if (!switcher) return;
                    if (switcher.classList.contains('is-open')) closeSwitcher(switcher);
                    else openSwitcher(switcher);
                    return;
                }

                const opt = e.target.closest('.lang-menu [data-lang]');
                if (opt) {
                    e.preventDefault();
                    const switcher = opt.closest('[data-cf-lang-switcher]');
                    if (!switcher) return;
                    selectLang(switcher, opt.dataset.lang);
                    return;
                }

                // Outside click — close any open switchers
                document.querySelectorAll('[data-cf-lang-switcher].is-open').forEach((s) => {
                    if (!s.contains(e.target)) closeSwitcher(s);
                });
            });

            // Keyboard support
            document.addEventListener('keydown', (e) => {
                const open = document.querySelector('[data-cf-lang-switcher].is-open');
                if (!open) return;
                if (e.key === 'Escape') {
                    closeSwitcher(open);
                    const t = open.querySelector('.lang-trigger');
                    if (t) t.focus();
                    return;
                }
                if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
                    const items = Array.from(open.querySelectorAll('.lang-menu [data-lang]'));
                    if (!items.length) return;
                    const idx = items.indexOf(document.activeElement);
                    let next = e.key === 'ArrowDown' ? idx + 1 : idx - 1;
                    if (next < 0) next = items.length - 1;
                    if (next >= items.length) next = 0;
                    items[next].setAttribute('tabindex', '0');
                    items[next].focus();
                    e.preventDefault();
                }
                if ((e.key === 'Enter' || e.key === ' ') && document.activeElement.matches('.lang-menu [data-lang]')) {
                    e.preventDefault();
                    selectLang(open, document.activeElement.dataset.lang);
                }
            });

            // Initial sync — once cfI18n applies the dict, mirror to trigger + menu order
            document.addEventListener('cf:langchange', (e) => {
                document.querySelectorAll('[data-cf-lang-switcher]').forEach((s) => {
                    syncTriggerLabel(s, e.detail.lang);
                    const menu = s.querySelector('.lang-menu');
                    if (menu) reorderMenuItems(menu, e.detail.lang);
                });
            });

            // Sync immediately too (cfI18n may be ready before this binds)
            const initialLang = (window.cfI18n && window.cfI18n.current()) || 'en';
            document.querySelectorAll('[data-cf-lang-switcher]').forEach((s) => {
                syncTriggerLabel(s, initialLang);
                const menu = s.querySelector('.lang-menu');
                if (menu) reorderMenuItems(menu, initialLang);
            });
        })();

        // ------------------------------------------------------------
        // 12. NAV "MORE" SUBMENU — adaptive collapse (768 px – 1379 px)
        //     768-839 → 2 links; 840-919 → 3; 920-1099 → 4;
        //     1100-1379 → 5. Thresholds include the logo and controls widths.
        //     Container visibility is forced via inline style so Tailwind
        //     `hidden md:flex` ambiguity cannot create a dead zone.
        //     No HTML changes to 14 pages needed.
        // ------------------------------------------------------------
        (() => {
            const BREAKPOINT_MIN = 768;
            const BREAKPOINT_MAX = 1380;

            // How many links stay visible in the bar at each width
            const getTier = (w) => {
                if (w < BREAKPOINT_MIN || w >= BREAKPOINT_MAX) return null;
                if (w >= 1100) return 5;
                if (w >= 920)  return 4;
                if (w >= 840)  return 3;
                return 2;
            };

            // Anchor via agencies link (proven selector from original §12)
            const agenciesAnchor = document.querySelector('nav a[data-i18n="common.nav.agencies"]');
            if (!agenciesAnchor) return;
            const navLinks = agenciesAnchor.closest('div');
            if (!navLinks) return;

            // Collect ALL nav links in DOM order from the container
            const allLinks = Array.from(navLinks.querySelectorAll('a[data-i18n^="common.nav."]'))
                .filter(a => a.getAttribute('data-i18n') !== 'common.nav.summon_agent'
                          && a.getAttribute('data-i18n') !== 'common.nav.sys_online');
            if (allLinks.length < 3) return;

            // Build More wrapper
            const wrapper = document.createElement('div');
            wrapper.className = 'nav-more-wrapper';
            wrapper.style.display = 'none';

            const trigger = document.createElement('button');
            trigger.type = 'button';
            trigger.className = 'nav-more-trigger';
            trigger.setAttribute('aria-expanded', 'false');
            trigger.innerHTML =
                '<span class="nav-more-label" data-i18n="common.nav.more">[More]</span>' +
                '<span class="material-symbols-outlined nav-more-chevron" aria-hidden="true">expand_more</span>';

            const menu = document.createElement('div');
            menu.className = 'nav-more-menu';
            menu.setAttribute('hidden', '');
            menu.setAttribute('role', 'menu');

            wrapper.appendChild(trigger);
            wrapper.appendChild(menu);
            navLinks.appendChild(wrapper);

            // Translate helper
            const getLangDict = () => {
                const lang = (window.cfI18n && window.cfI18n.current())
                    || (function () { try { return localStorage.getItem('cf_lang'); } catch (_) { return null; } }())
                    || 'en';
                return window.cfLocales && window.cfLocales[lang];
            };

            const translateEl = (el, dict) => {
                const key = el.getAttribute('data-i18n');
                if (!key || !dict) return;
                const parts = key.split('.');
                let val = dict;
                for (const p of parts) { val = val && val[p]; }
                if (val) el.textContent = val;
            };

            // Apply initial More label
            (() => {
                const dict = getLangDict();
                const val = dict && dict.common && dict.common.nav && dict.common.nav.more;
                const label = wrapper.querySelector('.nav-more-label');
                if (label && val) label.textContent = val;
            })();

            // Toggle
            let moreOpen = false;
            const closeMenu = () => {
                moreOpen = false;
                menu.setAttribute('hidden', '');
                wrapper.classList.remove('is-open');
                trigger.setAttribute('aria-expanded', 'false');
            };
            trigger.addEventListener('click', e => {
                e.stopPropagation();
                moreOpen = !moreOpen;
                if (moreOpen) menu.removeAttribute('hidden');
                else menu.setAttribute('hidden', '');
                wrapper.classList.toggle('is-open', moreOpen);
                trigger.setAttribute('aria-expanded', String(moreOpen));
            });
            document.addEventListener('click', closeMenu);
            document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });

            // Rebuild More menu items for the active tier
            let lastTier = -1;
            const rebuildMenu = (tier) => {
                if (tier === lastTier) return;
                lastTier = tier;
                const dict = getLangDict();
                menu.innerHTML = '';
                allLinks.slice(tier).forEach(link => {
                    const clone = link.cloneNode(true);
                    clone.style.removeProperty('display');
                    clone.setAttribute('role', 'menuitem');
                    translateEl(clone, dict);
                    menu.appendChild(clone);
                });
            };

            // Keep menu in sync on language change
            document.addEventListener('cf:langchange', () => {
                lastTier = -1;
                const w = window.innerWidth;
                const tier = getTier(w);
                if (tier !== null) {
                    rebuildMenu(tier);
                } else {
                    allLinks.forEach(l => l.style.removeProperty('display'));
                }
                const label = wrapper.querySelector('.nav-more-label');
                if (label && window.cfI18n) {
                    label.textContent = window.cfI18n.t('common.nav.more') || '[More]';
                }
            });

            // Main layout update — forces container visible in adaptive range
            const updateNav = () => {
                const w = window.innerWidth;
                const tier = getTier(w);

                if (tier === null) {
                    // Full nav or mobile — hand back to CSS
                    navLinks.style.removeProperty('display');
                    allLinks.forEach(l => l.style.removeProperty('display'));
                    wrapper.style.display = 'none';
                    closeMenu();
                    return;
                }

                // Force the container visible — overrides `hidden` class ambiguity
                navLinks.style.display = 'flex';

                // Show first `tier` links explicitly, collapse the rest
                allLinks.forEach((l, i) => {
                    l.style.display = i < tier ? 'inline-block' : 'none';
                });
                rebuildMenu(tier);
                wrapper.style.display = 'inline-flex';
            };

            updateNav();
            window.addEventListener('resize', updateNav);
        })();

        // ------------------------------------------------------------
        // 13. MOBILE NAV — hamburger (< 768 px) + GSAP mega drawer
        //     Hamburger sits LEFT of // button (right side of nav bar).
        //     Drawer positions itself below the glass panel via JS rect.
        //     No HTML changes to 14 pages needed.
        // ------------------------------------------------------------
        (() => {
            const BREAKPOINT = 768;
            const gsap = window.gsap;

            const nav = document.querySelector('nav');
            if (!nav) return;
            const navBar = nav.querySelector('.max-w-7xl');
            if (!navBar) return;
            const linksDiv = navBar.querySelector('.hidden.md\\:flex');

            // Controls div = LAST .flex.items-center.gap-4 in navBar
            const allFlexDivs = navBar.querySelectorAll('.flex.items-center.gap-4');
            const controlsDiv = allFlexDivs[allFlexDivs.length - 1];
            if (!linksDiv || !controlsDiv) return;

            // ---- Build hamburger button ----
            const burger = document.createElement('button');
            burger.type = 'button';
            burger.className = 'cf-hamburger';
            burger.setAttribute('aria-label', 'Open navigation');
            burger.setAttribute('aria-expanded', 'false');

            const setIcon = (icon) => {
                burger.innerHTML = `<span class="material-symbols-outlined" style="font-size:22px;line-height:1">${icon}</span>`;
            };
            setIcon('menu');

            // Insert BEFORE the nav-cta (// SUMMON_AGENT) button
            const navCta = controlsDiv.querySelector('.nav-cta');
            controlsDiv.insertBefore(burger, navCta || null);

            // ---- Build mega drawer ----
            const drawer = document.createElement('div');
            drawer.className = 'cf-mobile-drawer';
            drawer.setAttribute('aria-hidden', 'true');
            drawer.style.display = 'none';

            // Clone all nav links
            linksDiv.querySelectorAll('a[data-i18n]').forEach(link => {
                drawer.appendChild(link.cloneNode(true));
            });

            // Separator + CTA clone
            if (navCta) {
                const sep = document.createElement('div');
                sep.className = 'cf-drawer-sep';
                drawer.appendChild(sep);
                drawer.appendChild(navCta.cloneNode(true));
            }

            nav.appendChild(drawer);

            // ---- Translation helpers ----
            const applyTranslation = (lang) => {
                const dict = window.cfLocales && window.cfLocales[lang];
                if (!dict) return;
                drawer.querySelectorAll('a[data-i18n]').forEach(el => {
                    const parts = el.getAttribute('data-i18n').split('.');
                    let val = dict;
                    for (const p of parts) { val = val && val[p]; }
                    if (val) el.textContent = val;
                });
            };

            const initLang = (window.cfI18n && window.cfI18n.current())
                || (function () { try { return localStorage.getItem('cf_lang'); } catch (_) { return 'en'; } }())
                || 'en';
            applyTranslation(initLang);
            document.addEventListener('cf:langchange', (e) => applyTranslation(e.detail.lang));

            // ---- GSAP open/close ----
            let isOpen = false;
            let anim = null;

            const positionDrawer = () => {
                const rect = navBar.getBoundingClientRect();
                drawer.style.top    = (rect.bottom + 8) + 'px';
                drawer.style.left   = rect.left + 'px';
                drawer.style.right  = (document.documentElement.clientWidth - rect.right) + 'px';
            };

            const drawerLinks = () => drawer.querySelectorAll('a');

            const openDrawer = () => {
                if (isOpen) return;
                isOpen = true;
                setIcon('close');
                burger.setAttribute('aria-expanded', 'true');
                drawer.setAttribute('aria-hidden', 'false');
                positionDrawer();
                drawer.style.display = 'flex';

                if (gsap) {
                    if (anim) anim.kill();
                    anim = gsap.timeline()
                        .fromTo(drawer,
                            { clipPath: 'inset(0 0 100% 0 round 12px)', opacity: 0 },
                            { clipPath: 'inset(0 0 0% 0 round 12px)', opacity: 1, duration: 0.45, ease: 'power3.out' }
                        )
                        .fromTo(drawerLinks(),
                            { yPercent: -18, opacity: 0 },
                            { yPercent: 0, opacity: 1, stagger: 0.045, duration: 0.35, ease: 'power2.out' },
                            '-=0.28'
                        );
                }
            };

            const closeDrawer = (instant) => {
                if (!isOpen) return;
                isOpen = false;
                setIcon('menu');
                burger.setAttribute('aria-expanded', 'false');
                drawer.setAttribute('aria-hidden', 'true');

                if (gsap && !instant) {
                    if (anim) anim.kill();
                    anim = gsap.timeline({ onComplete: () => { drawer.style.display = 'none'; gsap.set(drawer, { clearProps: 'clipPath,opacity' }); } })
                        .to(drawerLinks(), { yPercent: -10, opacity: 0, stagger: 0.025, duration: 0.18, ease: 'power2.in' })
                        .to(drawer,
                            { clipPath: 'inset(0 0 100% 0 round 12px)', opacity: 0, duration: 0.28, ease: 'power2.in' },
                            '-=0.08'
                        );
                } else {
                    if (anim) anim.kill();
                    drawer.style.display = 'none';
                    if (gsap) gsap.set(drawer, { clearProps: 'clipPath,opacity' });
                }
            };

            burger.addEventListener('click', (e) => {
                e.stopPropagation();
                isOpen ? closeDrawer() : openDrawer();
            });

            drawer.querySelectorAll('a').forEach(a => a.addEventListener('click', () => closeDrawer()));

            document.addEventListener('click', (e) => {
                if (isOpen && !nav.contains(e.target)) closeDrawer();
            });
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && isOpen) closeDrawer();
            });
            window.addEventListener('resize', () => {
                if (window.innerWidth >= BREAKPOINT && isOpen) closeDrawer(true);
            });
        })();

        // ── Phone button hover: GSAP scale pulse layered on CSS ring ─────────
        (() => {
            if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
            document.querySelectorAll('.nav-phone-btn').forEach(btn => {
                btn.addEventListener('mouseenter', () => {
                    gsap.to(btn, { scale: 1.1, duration: 0.18, ease: 'power2.out' });
                });
                btn.addEventListener('mouseleave', () => {
                    gsap.to(btn, { scale: 1, duration: 0.5, ease: 'elastic.out(1.4, 0.5)' });
                });
            });
        })();

        // ============================================================
        // 15. MOBILE NAV — ensure full link set on every page
        // ============================================================
        (() => {
            const mobileNav = document.getElementById('mobile-nav');
            if (!mobileNav) return;
            const container = mobileNav.querySelector('.flex.flex-col') || mobileNav.querySelector('div');
            if (!container) return;
            if (container.querySelector('a[href*="for-agencies"]')) return; // already present

            const casesLink = container.querySelector('a[href*="case-studies"]');
            if (!casesLink) return;

            const cls = casesLink.className;
            const fixedLang = document.documentElement.getAttribute('data-cf-static-lang') || 'en';
            const langPrefix = fixedLang === 'en' ? '' : `/${fixedLang}`;
            const toAdd = [
                [`${langPrefix}/for-agencies`,    '[Agencies]', 'common.nav.agencies'],
                [`${langPrefix}/about`,           '[About]',    'common.nav.about'   ],
                [`${langPrefix}/#pricing-cards`,  '[Pricing]',  'common.nav.pricing' ],
            ];
            let after = casesLink;
            toAdd.forEach(([href, label, i18n]) => {
                const a = document.createElement('a');
                a.href = href;
                a.className = cls;
                a.textContent = label;
                a.setAttribute('data-i18n', i18n);
                after.insertAdjacentElement('afterend', a);
                after = a;
            });
        })();

        // ============================================================
        // 16. SCROLL REVEAL — GSAP ScrollTrigger for .cf-reveal/.cf-wipe
        // ============================================================
        (() => {
            if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
                document.querySelectorAll('.cf-reveal, .cf-reveal-x, .cf-wipe').forEach(el => el.classList.add('is-visible'));
                return;
            }
            gsap.utils.toArray('.cf-reveal, .cf-reveal-x, .cf-wipe').forEach(el => {
                ScrollTrigger.create({
                    trigger: el,
                    start: 'top 92%',
                    onEnter: () => el.classList.add('is-visible'),
                    once: true
                });
            });
        })();
        }
