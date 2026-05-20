(function () {
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    const query = (selector, root) => (root || document).querySelector(selector);
    const queryAll = (selector, root) => Array.from((root || document).querySelectorAll(selector));

    function initNav() {
        const nav = query("[data-site-nav]");
        const toggle = query("[data-nav-toggle]");
        const menu = query("[data-mobile-menu]");

        if (!nav) return;

        const onScroll = function () {
            nav.classList.toggle("is-scrolled", window.scrollY > 24);
        };

        onScroll();
        window.addEventListener("scroll", onScroll, { passive: true });

        if (toggle && menu) {
            toggle.addEventListener("click", function () {
                const isOpen = menu.classList.toggle("open");
                document.body.classList.toggle("menu-open", isOpen);
                toggle.setAttribute("aria-expanded", String(isOpen));
            });

            queryAll("a", menu).forEach(function (link) {
                link.addEventListener("click", function () {
                    menu.classList.remove("open");
                    document.body.classList.remove("menu-open");
                    toggle.setAttribute("aria-expanded", "false");
                });
            });
        }
    }

    function initMagneticButtons() {
        if (!window.matchMedia("(pointer: fine)").matches) return;
        if (query(".cf-cursor") || window.lenis) return;

        queryAll(".button, .nav-cta").forEach(function (button) {
            button.addEventListener("mousemove", function (event) {
                if (!window.gsap) return;

                const rect = button.getBoundingClientRect();
                const x = event.clientX - rect.left - rect.width / 2;
                const y = event.clientY - rect.top - rect.height / 2;

                window.gsap.to(button, {
                    x: x * 0.15,
                    y: y * 0.15,
                    duration: 0.28,
                    ease: "power2.out",
                    overwrite: "auto"
                });
            });

            button.addEventListener("mouseleave", function () {
                if (!window.gsap) return;

                window.gsap.to(button, {
                    x: 0,
                    y: 0,
                    duration: 0.6,
                    ease: "elastic.out(1, 0.35)",
                    overwrite: "auto"
                });
            });
        });
    }

    function initMarquee() {
        const track = query("[data-marquee-track]");

        if (!track || !window.gsap || prefersReducedMotion) return;

        window.gsap.to(track, {
            xPercent: -50,
            duration: 18,
            ease: "none",
            repeat: -1
        });
    }

    function initRevealAnimations() {
        if (!window.gsap || !window.ScrollTrigger) {
            queryAll(".reveal").forEach(function (item) {
                item.style.opacity = "1";
                item.style.transform = "none";
            });
            return;
        }

        window.gsap.registerPlugin(window.ScrollTrigger);

        const lenisAvailable = window.Lenis && !prefersReducedMotion && !window.lenis;

        if (lenisAvailable) {
            const lenis = new window.Lenis({
                duration: 1.08,
                smoothWheel: true,
                easing: function (t) {
                    return Math.min(1, 1.001 - Math.pow(2, -10 * t));
                }
            });

            lenis.on("scroll", window.ScrollTrigger.update);
            window.gsap.ticker.add(function (time) {
                lenis.raf(time * 1000);
            });
            window.gsap.ticker.lagSmoothing(0);
        }

        queryAll(".reveal").forEach(function (item) {
            window.gsap.to(item, {
                opacity: 1,
                y: 0,
                duration: 0.9,
                ease: "power3.out",
                scrollTrigger: {
                    trigger: item,
                    start: "top 86%"
                }
            });
        });
    }

    function initCounters() {
        if (!window.gsap || !window.ScrollTrigger || prefersReducedMotion) return;

        queryAll(".metric-number[data-count]").forEach(function (node) {
            const count = Number(node.getAttribute("data-count"));
            const prefix = node.getAttribute("data-prefix") || "";
            const suffix = node.getAttribute("data-suffix") || "";
            const decimals = Number(node.getAttribute("data-decimals") || "0");
            const state = { value: 0 };

            window.gsap.to(state, {
                value: count,
                duration: 1.3,
                ease: "power2.out",
                scrollTrigger: {
                    trigger: node,
                    start: "top 88%"
                },
                onUpdate: function () {
                    const raw = decimals > 0 ? state.value.toFixed(decimals) : Math.round(state.value).toString();
                    node.textContent = prefix + raw + suffix;
                }
            });
        });
    }

    function initJourneyProgress() {
        if (!window.gsap || !window.ScrollTrigger || prefersReducedMotion) return;

        queryAll(".journey").forEach(function (journey) {
            const progress = query(".journey-progress", journey);
            if (!progress) return;

            window.gsap.to(progress, {
                height: "100%",
                ease: "none",
                scrollTrigger: {
                    trigger: journey,
                    start: "top 82%",
                    end: "bottom 28%",
                    scrub: true
                }
            });
        });
    }

    function initHomePin() {
        if (!window.gsap || !window.ScrollTrigger || prefersReducedMotion) return;
        if (window.innerWidth < 1120) return;

        const track = query("[data-home-pin]");
        const stage = query("[data-home-stage]");

        if (!track || !stage) return;

        window.ScrollTrigger.create({
            trigger: track,
            start: "top top+=120",
            end: "bottom bottom-=120",
            pin: stage,
            pinSpacing: false,
            anticipatePin: 1
        });
    }

    function initPipelineAnimation() {
        if (!window.gsap || !window.ScrollTrigger || prefersReducedMotion) return;

        queryAll("[data-pipeline]").forEach(function (pipeline) {
            const progress = query("[data-pipeline-progress]", pipeline);
            if (!progress) return;

            window.gsap.fromTo(progress, {
                scaleX: 0,
                transformOrigin: "left center"
            }, {
                scaleX: 1,
                ease: "none",
                scrollTrigger: {
                    trigger: pipeline,
                    start: "top 75%",
                    end: "bottom 55%",
                    scrub: true
                }
            });
        });
    }

    function initAgencyStrip() {
        if (!window.gsap || !window.ScrollTrigger || prefersReducedMotion) return;
        if (window.innerWidth < 1120) return;

        const strip = query("[data-agency-strip]");
        if (!strip) return;

        window.gsap.to(strip, {
            x: -72,
            ease: "none",
            scrollTrigger: {
                trigger: strip,
                start: "top bottom",
                end: "bottom top",
                scrub: true
            }
        });
    }

    function initArsenalFilters() {
        const buttons = queryAll("[data-filter-button]");
        const cards = queryAll("[data-filter-card]");

        if (!buttons.length || !cards.length) return;

        buttons.forEach(function (button) {
            button.addEventListener("click", function () {
                const value = button.getAttribute("data-filter-button");

                buttons.forEach(function (item) {
                    item.classList.toggle("is-active", item === button);
                });

                cards.forEach(function (card) {
                    const group = card.getAttribute("data-filter-card");
                    const show = value === "all" || group.split(" ").includes(value);
                    card.classList.toggle("is-hidden", !show);
                });
            });
        });
    }

    function normalizedValue(value) {
        return (value || "").trim().toLowerCase();
    }

    function initLeadForm() {
        const params = new URLSearchParams(window.location.search);
        const objectiveToService = {
            creation: "site",
            project: "site",
            site: "site",
            automation: "staff",
            staff: "staff",
            merlin: "staff",
            maintenance: "other",
            marketing: "other",
            retainer: "round-table",
            "round-table": "round-table",
            agency: "agency"
        };

        queryAll("[data-progress-form]").forEach(function (form) {
            const progressFill = query("[data-progress-fill]", form);
            const statusNode = query("[data-form-status]", form);
            const serviceField = query("select[name='service']", form);
            const objectiveField = query("input[name='objective']", form);
            const objective = normalizedValue(params.get("objective"));

            if (objectiveField && objective) {
                objectiveField.value = objective;
            }

            if (serviceField && (params.has("service") || objective)) {
                const requested = normalizedValue(params.get("service")) || objectiveToService[objective] || objective;
                const options = Array.from(serviceField.options);
                const exact = options.find(function (option) {
                    return normalizedValue(option.value || option.textContent) === requested;
                });
                if (exact) serviceField.value = exact.value;
            }

            const fields = queryAll("[required]", form);

            function updateProgress() {
                if (!progressFill || !fields.length) return;

                let complete = 0;
                fields.forEach(function (field) {
                    if (field.value && String(field.value).trim() !== "") complete += 1;
                });

                progressFill.style.width = String((complete / fields.length) * 100) + "%";
            }

            updateProgress();
            fields.forEach(function (field) {
                ["input", "change", "blur"].forEach(function (eventName) {
                    field.addEventListener(eventName, updateProgress);
                });
            });

            form.addEventListener("submit", function (event) {
                event.preventDefault();

                const data = new FormData(form);
                const pairs = [
                    ["Name", data.get("name")],
                    ["Email", data.get("email")],
                    ["Service", data.get("service")],
                    ["Budget", data.get("budget")],
                    ["Objective", data.get("objective")],
                    ["Timeline", data.get("timeline")],
                    ["Market", data.get("market")],
                    ["Project goal", data.get("project_goal")]
                ].filter(function (entry) {
                    return entry[1] && String(entry[1]).trim() !== "";
                });

                const subjectPrefix = (window.cfI18n && window.cfI18n.t('contact.email_subject_prefix')) || "Project inquiry - ";
                const subject = subjectPrefix + (data.get("service") || "Camelot Flows");
                const body = pairs.map(function (entry) {
                    return entry[0] + ": " + entry[1];
                }).join("\n");

                if (statusNode) {
                    statusNode.textContent = (window.cfI18n && window.cfI18n.t('contact.form_status_opening')) || "Opening your email app with a structured project brief.";
                }

                window.location.href = "mailto:hello@camelotflows.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
            });
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        initNav();
        initMagneticButtons();
        initMarquee();
        initRevealAnimations();
        initCounters();
        initJourneyProgress();
        initHomePin();
        initPipelineAnimation();
        initAgencyStrip();
        initArsenalFilters();
        initLeadForm();

        // Handle ?goto=pricing — navigating here without a hash so GSAP inits
        // normally at the top, then Lenis scrolls to pricing after animations start.
        // Uses absolute scroll target (section.offsetTop + crawl-reveal offset) so
        // the behaviour is identical regardless of where the user was on the page.
        function getPricingScrollTarget() {
            var section = document.getElementById('starwars-pricing');
            if (!section) return null;
            // ~20% of the 120vh pin range brings the first card into view on desktop.
            var intoSection = window.innerWidth >= 768
                ? Math.round(window.innerHeight * 0.20)
                : 0;
            return section.getBoundingClientRect().top + window.scrollY + intoSection;
        }

        var gotoParam = new URLSearchParams(window.location.search).get('goto');
        if (gotoParam === 'pricing') {
            history.replaceState(null, '', window.location.pathname);
            setTimeout(function () {
                var targetY = getPricingScrollTarget();
                if (targetY === null) return;
                if (window.lenis) {
                    window.lenis.scrollTo(targetY, { duration: 1.5 });
                } else {
                    window.scrollTo({ top: targetY, behavior: 'smooth' });
                }
            }, 900);
        }

        // Intercept same-page #pricing-cards nav clicks — use Lenis instead of
        // native browser scroll so GSAP ScrollTrigger animations fire correctly.
        document.querySelectorAll('a[href="#pricing-cards"]').forEach(function (link) {
            link.addEventListener('click', function (e) {
                var targetY = getPricingScrollTarget();
                if (targetY === null) return; // not on homepage, let browser navigate normally
                e.preventDefault();
                if (window.lenis) {
                    window.lenis.scrollTo(targetY, { duration: 1.5 });
                } else {
                    window.scrollTo({ top: targetY, behavior: 'smooth' });
                }
            });
        });
    });
})();
