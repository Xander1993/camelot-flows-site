from pathlib import Path
from textwrap import dedent
import shutil


ROOT = Path(__file__).resolve().parent
ASSETS_DIR = ROOT / "assets"
IMAGES_DIR = ASSETS_DIR / "images"


NAV_ITEMS = [
    ("Home", "index.html"),
    ("Web Design", "web-design.html"),
    ("Automation", "automation.html"),
    ("For Agencies", "for-agencies.html"),
    ("Case Studies", "case-studies.html"),
    ("About", "about.html"),
    ("Contact", "contact.html"),
]

MOBILE_ITEMS = NAV_ITEMS + [
    ("Arsenal", "arsenal.html"),
    ("Work With Me", "work-with-me.html"),
]

COZY_IMAGE_DIR = "assets/images/cozy-freelancer"

# New cozy assets are generated in-place and referenced directly. Keep this
# empty so regenerating the legacy page set does not overwrite old mockups.
IMAGE_MAP = {}


def button(label: str, href: str, variant: str = "primary", extra: str = "") -> str:
    class_name = f"button {variant}"
    if extra:
        class_name += f" {extra}"
    return f'<a href="{href}" class="{class_name}">{label}</a>'


def nav_html(current: str) -> str:
    nav_links = "\n".join(
        f'<a href="{href}" class="nav-link{" is-current" if href == current else ""}">{label}</a>'
        for label, href in NAV_ITEMS
    )
    mobile_links = "\n".join(
        f'<a href="{href}" class="mobile-link">{label}<span>{href}</span></a>'
        for label, href in MOBILE_ITEMS
    )
    return dedent(
        f"""
        <header class="site-nav" data-site-nav>
            <div class="nav-inner">
                <a href="index.html" class="nav-brand" aria-label="Camelot Flows home">
                    <span class="nav-mark">CF</span>
                    <span class="nav-copy">
                        <strong>Camelot Flows</strong>
                        <span>Founder-led premium web systems</span>
                    </span>
                </a>
                <nav class="nav-links" aria-label="Primary">
                    {nav_links}
                </nav>
                <a href="contact.html" class="nav-cta desktop-only">Start a project</a>
                <button class="nav-toggle" type="button" aria-label="Open navigation" aria-expanded="false" data-nav-toggle>
                    <span class="font-display">+</span>
                </button>
            </div>
        </header>
        <div class="mobile-menu" data-mobile-menu>
            {mobile_links}
            <a href="contact.html" class="nav-cta">Start a project</a>
        </div>
        """
    ).strip()


def footer_html() -> str:
    return dedent(
        """
        <footer class="site-footer">
            <div class="container">
                <div class="footer-grid">
                    <div>
                        <div class="footer-brand">
                            <span class="nav-mark">CF</span>
                            <span>
                                <strong>Camelot Flows</strong>
                                <span>Hybrid premium web and automation studio</span>
                            </span>
                        </div>
                        <p class="footer-copy">
                            Websites that feel premium. Automation that removes drag. Founder-level involvement from strategy through launch.
                        </p>
                    </div>
                    <div>
                        <div class="footer-heading">Core Pages</div>
                        <div class="footer-links">
                            <a href="web-design.html">Web Design and Build</a>
                            <a href="automation.html">Automation</a>
                            <a href="for-agencies.html">For Agencies</a>
                            <a href="case-studies.html">Case Studies</a>
                        </div>
                    </div>
                    <div>
                        <div class="footer-heading">Company</div>
                        <div class="footer-links">
                            <a href="arsenal.html">Arsenal</a>
                            <a href="about.html">About</a>
                            <a href="work-with-me.html">Work With Me</a>
                            <a href="contact.html">Contact</a>
                        </div>
                    </div>
                    <div>
                        <div class="footer-heading">Secondary</div>
                        <div class="footer-links">
                            <a href="maintenance.html">Maintenance</a>
                            <a href="growth-marketing.html">Growth and Landing Pages</a>
                            <a href="merlin-protocol.html">Merlin Protocol</a>
                            <a href="privacy.html">Privacy</a>
                            <a href="legal.html">Legal</a>
                            <a href="mailto:hello@camelotflows.com">hello@camelotflows.com</a>
                        </div>
                    </div>
                </div>
                <div class="footer-bottom">
                    <span>EN master copy shipped. RU and RO localization can now be layered on top.</span>
                    <span class="footer-status">Founder-led, async-friendly, NDA-ready</span>
                </div>
            </div>
        </footer>
        """
    ).strip()


def page(title: str, description: str, current: str, body: str, page_id: str) -> str:
    return dedent(
        f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <meta name="description" content="{description}">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
            <link rel="stylesheet" href="assets/site.css">
            <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/bundled/lenis.min.js"></script>
            <script src="assets/site.js" defer></script>
        </head>
        <body data-page="{page_id}">
            <div class="noise"></div>
            <div class="orb orb-sage"></div>
            <div class="orb orb-terra"></div>
            <div class="page-shell">
                {nav_html(current)}
                <main>
                    {body}
                </main>
                {footer_html()}
            </div>
        </body>
        </html>
        """
    ).strip() + "\n"


def redirect_page(title: str, target: str, description: str) -> str:
    return dedent(
        f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <meta name="description" content="{description}">
            <meta http-equiv="refresh" content="0; url={target}">
            <link rel="stylesheet" href="assets/site.css">
        </head>
        <body>
            <div class="page-shell">
                <main class="section">
                    <div class="container">
                        <div class="card" style="max-width: 720px; margin: 120px auto;">
                            <div class="card-meta">Redirect</div>
                            <h3>This page moved.</h3>
                            <p>You are being redirected to the updated page. If it does not open automatically, use the link below.</p>
                            <div class="button-row">
                                <a href="{target}" class="button primary">Open updated page</a>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
        </body>
        </html>
        """
    ).strip() + "\n"


HOME_BODY = dedent(
    f"""
    <section class="page-hero" data-home-pin>
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">Founder-led studio for premium digital growth</div>
                <h1 class="hero-title">Award-winning websites and <span class="accent">automation systems</span> for businesses that need to look sharper and run smoother.</h1>
                <p class="hero-lead">
                    Camelot Flows helps premium service brands, consultants, agencies and operators launch high-trust websites, remove slow manual work, and keep strategy, design and implementation inside one focused partnership.
                </p>
                <div class="button-row">
                    {button("Start a project", "contact.html?service=Website%20Design%20and%20Build", "primary")}
                    {button("See the core offers", "#core-offers", "secondary")}
                </div>
            </div>
            <div class="hero-stage" data-home-stage>
                <div class="signal-panel dark reveal">
                    <div class="panel-top">
                        <span class="panel-pill">Live delivery view</span>
                        <span class="card-meta">Website + automation</span>
                    </div>
                    <div class="workflow-log">
                        <div class="log-line"><strong>01. Inquiry captured</strong><span>qualified in one intake flow</span></div>
                        <div class="log-line"><strong>02. Positioning locked</strong><span>copy and structure aligned before design</span></div>
                        <div class="log-line"><strong>03. Site built fast</strong><span>premium visuals without agency bloat</span></div>
                        <div class="log-line"><strong>04. Ops cleaned up</strong><span>manual follow-ups turned into systems</span></div>
                    </div>
                </div>
                <div class="stage-stack reveal">
                    <div class="stack-card">
                        <div class="card-meta">What makes the offer different</div>
                        <strong>Design quality and operational thinking in the same room.</strong>
                        <p>Not just a prettier website. Not just a disconnected automation audit. One founder-led build system that respects brand, speed, trust and workflow reality.</p>
                    </div>
                    <div class="stack-card">
                        <div class="card-meta">Best fit</div>
                        <strong>Premium service businesses, agencies, consultants and operators.</strong>
                        <p>If your site feels under-positioned or your operations feel too manual, this is where a sharper web system starts paying off.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="container proof-strip">
            <div class="proof-item reveal"><strong>Founder-led</strong><span>You work close to the person designing and building the system.</span></div>
            <div class="proof-item reveal"><strong>Premium-first</strong><span>Editorial clarity, selective motion and high-trust visual craft.</span></div>
            <div class="proof-item reveal"><strong>Automation-aware</strong><span>Web projects are planned with intake, follow-up and operations in mind.</span></div>
            <div class="proof-item reveal"><strong>International-ready</strong><span>English-first structure with a clean path to RU and RO localization.</span></div>
        </div>
    </section>

    <section class="marquee" aria-label="Capabilities strip">
        <div class="marquee-track" data-marquee-track>
            <span>Premium websites</span>
            <span>Founder-led execution</span>
            <span>Automation systems</span>
            <span>White-label agency support</span>
            <span>Performance-minded build</span>
            <span>Premium websites</span>
            <span>Founder-led execution</span>
            <span>Automation systems</span>
            <span>White-label agency support</span>
            <span>Performance-minded build</span>
        </div>
    </section>

    <section class="section" id="core-offers">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Core offers</div>
                <h2 class="section-title">Two revenue drivers, one <span class="accent">focused studio</span>.</h2>
                <p class="section-copy">The site now leads with the two things most likely to win qualified work: premium website design and build, plus automation and AI workflows. Agency support, maintenance and custom tools stay visible, but they support the main story instead of diluting it.</p>
            </div>
            <div class="grid-3">
                <div class="card highlight reveal">
                    <div class="card-meta">Primary offer</div>
                    <h3>Web Design and Build</h3>
                    <p>Strategy, messaging, visual direction, build quality and motion all stitched into one premium web layer.</p>
                    <ul class="feature-list">
                        <li>Brand-led landing pages and multi-page sites</li>
                        <li>High-trust layout systems and editorial pacing</li>
                        <li>GSAP motion used to support narrative and conversion</li>
                    </ul>
                    <div class="button-row">
                        {button("See web design", "web-design.html", "secondary")}
                    </div>
                </div>
                <div class="card highlight reveal">
                    <div class="card-meta">Primary offer</div>
                    <h3>Automation and AI Workflows</h3>
                    <p>Lead intake, qualification, follow-up, handoff and internal ops designed as systems instead of recurring manual work.</p>
                    <ul class="feature-list">
                        <li>Workflow architecture for sales and operations</li>
                        <li>AI-assisted flows with human handoff logic</li>
                        <li>Documentation, observability and sensible fallbacks</li>
                    </ul>
                    <div class="button-row">
                        {button("See automation", "automation.html", "secondary")}
                    </div>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Support layer</div>
                    <h3>Agency and Retainer Support</h3>
                    <p>White-label execution, maintenance, landing page iterations and custom internal tools where they strengthen the main build.</p>
                    <ul class="feature-list">
                        <li>Invisible partner delivery for agencies</li>
                        <li>Post-launch maintenance and iteration</li>
                        <li>Internal tools when off-the-shelf breaks down</li>
                    </ul>
                    <div class="button-row">
                        {button("See agency support", "for-agencies.html", "ghost")}
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Why it converts</div>
                <h2 class="section-title">The site now makes the value obvious in under <span class="accent">five seconds</span>.</h2>
                <p class="section-copy">This version removes the vague freelancer feel. The homepage frames Camelot Flows as a boutique premium partner: sharper positioning, more commercial clarity, and stronger internal page paths for business owners, agencies and founder-led brands.</p>
            </div>
            <div class="grid-4">
                <div class="card dark reveal">
                    <div class="card-meta">Signal 01</div>
                    <h3>Clarity first</h3>
                    <p>The hero sells websites and automation immediately instead of making visitors decode the offer.</p>
                </div>
                <div class="card dark reveal">
                    <div class="card-meta">Signal 02</div>
                    <h3>Premium without noise</h3>
                    <p>Editorial spacing, darker feature moments and motion restraint keep the work feeling intentional rather than gimmicky.</p>
                </div>
                <div class="card dark reveal">
                    <div class="card-meta">Signal 03</div>
                    <h3>Segmented paths</h3>
                    <p>Businesses, agencies and founders each get a clear way into the site instead of one generic funnel.</p>
                </div>
                <div class="card dark reveal">
                    <div class="card-meta">Signal 04</div>
                    <h3>Proof architecture</h3>
                    <p>Case study structure, placeholder proof notes and explicit asset requests make the next iteration easy to strengthen with real evidence.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container">
            <div class="section-header centered reveal">
                <div class="section-kicker">Choose your path</div>
                <h2 class="section-title">Built for the people who need premium craft and <span class="accent">less operational drag</span>.</h2>
            </div>
            <div class="grid-3">
                <div class="card reveal">
                    <div class="card-meta">For businesses</div>
                    <h3>Service brands that need trust fast</h3>
                    <p>Your website should feel worth the price you charge, and your follow-up should not depend on memory and inbox chaos.</p>
                    <div class="button-row">
                        {button("See web design", "web-design.html", "secondary")}
                    </div>
                </div>
                <div class="card reveal">
                    <div class="card-meta">For agencies</div>
                    <h3>Teams that need invisible execution</h3>
                    <p>Bring in a white-label build and automation partner for overflow, specialist interaction work or founder-level delivery support.</p>
                    <div class="button-row">
                        {button("See agency model", "for-agencies.html", "secondary")}
                    </div>
                </div>
                <div class="card reveal">
                    <div class="card-meta">For founders</div>
                    <h3>Consultants and operators building the next layer</h3>
                    <p>When your business has outgrown templates and manual follow-ups, this is where a sharper web system starts paying off.</p>
                    <div class="button-row">
                        {button("See automation", "automation.html", "secondary")}
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">How the work runs</div>
                <h2 class="section-title">Simple process, premium output, <span class="accent">no agency drag</span>.</h2>
            </div>
            <div class="process-grid">
                <div class="process-step reveal">
                    <div class="process-step-number">01 - Discovery</div>
                    <h3>Fit, goal and constraints</h3>
                    <p>We get clear on the commercial goal, what the audience needs to believe, and where friction exists today.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">02 - Positioning</div>
                    <h3>Structure before polish</h3>
                    <p>Offer hierarchy, page flow, messaging and conversion logic get defined before the design gets dramatic.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">03 - Build</div>
                    <h3>Design and systems in sync</h3>
                    <p>Visual craft, motion, performance and workflow architecture move together instead of in separate disconnected phases.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">04 - Launch</div>
                    <h3>Handover with momentum</h3>
                    <p>The end state is a better website, a cleaner process and a clearer next step for support, growth or automation.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container detail-grid">
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-hero-about.webp" alt="Founder-led studio presentation" loading="lazy" decoding="async" width="1536" height="1024">
                <div class="image-caption"><span>Founder-led studio</span><span>Chisinau to international clients</span></div>
            </div>
            <div class="card reveal">
                <div class="card-meta">Founder authority</div>
                <h3>Closer to a boutique studio than a generic freelancer profile.</h3>
                <p>This implementation shifts the entire site into a stronger founder-led studio position: more editorial confidence, more internal structure, more selective language, less vague positioning and less sci-fi noise.</p>
                <ul class="feature-list">
                    <li>English-first copy architecture ready for localization</li>
                    <li>Proof placeholders where real metrics still need verification</li>
                    <li>Clearer navigation, clearer CTAs and clearer service hierarchy</li>
                </ul>
                <div class="button-row">
                    {button("Read the founder story", "about.html", "secondary")}
                    {button("Open contact", "contact.html", "ghost")}
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container">
            <div class="section-header centered reveal">
                <div class="section-kicker">Next best step</div>
                <h2 class="section-title">If the site needs to sell harder and your workflow needs to <span class="accent">waste less time</span>, start here.</h2>
                <p class="section-copy">Use the contact page to send a structured project brief. The new form qualifies scope by service, budget, timeline, market and business goal, so the first conversation starts with more signal.</p>
            </div>
            <div class="button-row" style="justify-content:center;">
                {button("Start a structured inquiry", "contact.html?service=Website%20Design%20and%20Build", "primary")}
                {button("Browse the Arsenal", "arsenal.html", "secondary")}
            </div>
        </div>
    </section>
    """
).strip()


WEB_DESIGN_BODY = dedent(
    f"""
    <section class="page-hero">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">Web Design and Build</div>
                <h1 class="hero-title">Premium websites that make the business feel <span class="accent">worth the price</span>.</h1>
                <p class="hero-lead">
                    Strategy, page flow, copy hierarchy, design system, motion and build quality are treated as one system. The result feels more like a high-end digital studio outcome and less like a stitched-together freelancer handoff.
                </p>
                <div class="button-row">
                    {button("Discuss a website project", "contact.html?service=Website%20Design%20and%20Build", "primary")}
                    {button("See case study structure", "case-studies.html", "secondary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-case-site.webp" alt="Web design service concept" loading="lazy" decoding="async" width="1672" height="941">
                <div class="image-caption"><span>Hybrid premium direction</span><span>Design + build in one workflow</span></div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container detail-grid">
            <div class="card reveal">
                <div class="card-meta">What the offer covers</div>
                <h3>Not just screens. The commercial layer under the screens.</h3>
                <p>Website work starts with the business position: who it is for, what it needs to communicate quickly, what objections need handling, what should happen after the click, and what the page structure has to do to support trust.</p>
                <ul class="feature-list">
                    <li>Offer hierarchy and message clarity</li>
                    <li>Brand-aligned visual direction and layout system</li>
                    <li>Responsive build with performance in mind</li>
                    <li>Animation used to support narrative, not distract from it</li>
                </ul>
            </div>
            <div class="card reveal">
                <div class="card-meta">Best fit</div>
                <h3>Service businesses, consultants, boutique firms and founder-led brands.</h3>
                <p>The strongest matches are businesses that have already proven the offer, but whose current site looks weaker than the work they actually deliver.</p>
                <div class="tag-row">
                    <span class="tag">Premium positioning</span>
                    <span class="tag">Trust and conversion</span>
                    <span class="tag">Selective GSAP motion</span>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container detail-grid">
            <div class="section-header reveal">
                <div class="section-kicker">From strategy to launch</div>
                <h2 class="section-title">A scrollytelling build process that keeps the site <span class="accent">coherent</span>.</h2>
                <p class="section-copy">This page gets a signature scroll mechanic: a vertical journey rail that reveals how a premium site gets structured and why each stage matters to the client outcome.</p>
            </div>
            <div class="journey reveal">
                <div class="journey-track"><div class="journey-progress"></div></div>
                <div class="journey-step">
                    <h3>01. Positioning and page map</h3>
                    <p class="timeline-copy">Define the story the site has to tell, the proof it needs to surface, and the pages required to support the sale.</p>
                </div>
                <div class="journey-step">
                    <h3>02. Wireframe and content direction</h3>
                    <p class="timeline-copy">Shape the reading rhythm, priority messages and CTA logic before visual treatment starts doing the heavy lifting.</p>
                </div>
                <div class="journey-step">
                    <h3>03. Design system and motion rules</h3>
                    <p class="timeline-copy">Build a premium look with clear spacing, typography control, section contrast and motion principles that feel deliberate.</p>
                </div>
                <div class="journey-step">
                    <h3>04. Build, review and refine</h3>
                    <p class="timeline-copy">Translate the design into production-quality code, test the interactions and remove friction before launch.</p>
                </div>
                <div class="journey-step">
                    <h3>05. Launch with operational readiness</h3>
                    <p class="timeline-copy">A site launch should not introduce chaos. Handover, form routing, analytics and maintenance expectations are planned early.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">What premium actually means</div>
                <h2 class="section-title">Better than a template. Smarter than pure <span class="accent">surface polish</span>.</h2>
            </div>
            <div class="grid-3">
                <div class="card reveal">
                    <div class="card-meta">Narrative</div>
                    <h3>Page flow that earns trust</h3>
                    <p>Sections are sequenced to answer the right business questions in the right order, instead of just filling screen space.</p>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Performance</div>
                    <h3>Fast enough to feel expensive</h3>
                    <p>Performance is part of the brand experience. The site should feel immediate, stable and polished across devices.</p>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Editing</div>
                    <h3>Practical after launch</h3>
                    <p>Content changes, integrations, new sections and campaign pages should not require rebuilding the entire thing from scratch.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Engagement models</div>
                <h2 class="section-title">Three typical scopes for the website side of the <span class="accent">studio offer</span>.</h2>
                <p class="section-copy">No fake pricing, no false precision. Scope is aligned after discovery, but these tiers make the service shape obvious.</p>
            </div>
            <div class="tier-grid">
                <div class="tier-card reveal">
                    <div class="tier-label">Foundation</div>
                    <h3>Focused launch site</h3>
                    <p>Ideal when the offer is clear and the priority is a better first impression, stronger trust and a cleaner call to action.</p>
                    <ul class="feature-list">
                        <li>Core homepage or landing page system</li>
                        <li>Offer-led copy structure</li>
                        <li>Responsive premium build</li>
                    </ul>
                </div>
                <div class="tier-card highlight reveal">
                    <div class="tier-label">Signature</div>
                    <h3>Multi-page brand site</h3>
                    <p>The main sweet spot for premium service brands that need clearer positioning, better authority and stronger conversion paths.</p>
                    <ul class="feature-list">
                        <li>Multi-page information architecture</li>
                        <li>Motion system and editorial pacing</li>
                        <li>Service, proof and conversion pages</li>
                    </ul>
                </div>
                <div class="tier-card reveal">
                    <div class="tier-label">Growth-ready</div>
                    <h3>Website plus systems layer</h3>
                    <p>Used when the build also needs booking logic, CRM routing, lead qualification or connected operational workflows.</p>
                    <ul class="feature-list">
                        <li>Website and automation handoff planning</li>
                        <li>Campaign or service page expansion</li>
                        <li>Maintenance and iteration path</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container detail-grid">
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-hero-arsenal.webp" alt="Selected website showcase concepts" loading="lazy" decoding="async" width="1536" height="1024">
                <div class="image-caption"><span>Selected showcase direction</span><span>Portfolio, not template spam</span></div>
            </div>
            <div class="card reveal">
                <div class="card-meta">Natural next step</div>
                <h3>Need the visual layer and the conversion layer to tighten up at the same time?</h3>
                <p>Start with the website conversation. If the business also needs cleaner lead flow, follow-up or qualification logic, that gets mapped early so the site is built around the workflow instead of patched after launch.</p>
                <div class="button-row">
                    {button("Start a website brief", "contact.html?service=Website%20Design%20and%20Build", "primary")}
                    {button("Browse the Arsenal", "arsenal.html", "secondary")}
                </div>
            </div>
        </div>
    </section>
    """
).strip()


AUTOMATION_BODY = dedent(
    f"""
    <section class="page-hero">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">Automation and AI workflows</div>
                <h1 class="hero-title">Smarter systems for the work that should already be <span class="accent">running itself</span>.</h1>
                <p class="hero-lead">
                    Camelot Flows turns repetitive lead handling, internal handoffs and follow-up tasks into clear, observable workflows. The goal is not novelty. The goal is less drag, faster response and cleaner operations.
                </p>
                <div class="button-row">
                    {button("Discuss an automation project", "contact.html?service=Automation%20and%20AI%20Workflows", "primary")}
                    {button("See Merlin Protocol", "merlin-protocol.html", "secondary")}
                </div>
            </div>
            <div class="signal-panel dark reveal">
                <div class="panel-top">
                    <span class="panel-pill">Automation map</span>
                    <span class="card-meta">Lead to handoff</span>
                </div>
                <div class="workflow-log">
                    <div class="log-line"><strong>Capture</strong><span>forms, chat, booking, inbound messages</span></div>
                    <div class="log-line"><strong>Qualify</strong><span>route by service, budget, market and urgency</span></div>
                    <div class="log-line"><strong>Sync</strong><span>CRM, calendar, docs, task systems</span></div>
                    <div class="log-line"><strong>Follow up</strong><span>AI-assisted drafts with human override where needed</span></div>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Signature interaction</div>
                <h2 class="section-title">A pipeline story that reveals how the workflow gets <span class="accent">stitched together</span>.</h2>
                <p class="section-copy">This page uses a GSAP pipeline mechanic tied directly to the offer: lead source, qualification, routing, handoff and follow-up become a visible sequence instead of abstract tech jargon.</p>
            </div>
            <div class="card dark reveal" data-pipeline>
                <div class="card-top">
                    <span class="card-pill">Workflow spine</span>
                    <span class="card-meta">Built for actual operations</span>
                </div>
                <div style="height: 4px; margin: 22px 0 26px; background: rgba(255,255,255,0.08); overflow: hidden; border-radius: 999px;">
                    <div data-pipeline-progress style="height:100%; background: linear-gradient(90deg, rgba(117,141,108,1), rgba(196,120,92,1));"></div>
                </div>
                <div class="grid-4">
                    <div class="card dark">
                        <div class="card-meta">01</div>
                        <h3>Source</h3>
                        <p>Intake from forms, DMs, bookings, email or internal requests.</p>
                    </div>
                    <div class="card dark">
                        <div class="card-meta">02</div>
                        <h3>Decision</h3>
                        <p>Route by service, urgency, quality and required next action.</p>
                    </div>
                    <div class="card dark">
                        <div class="card-meta">03</div>
                        <h3>Sync</h3>
                        <p>Update the systems that should know what happened without manual copying.</p>
                    </div>
                    <div class="card dark">
                        <div class="card-meta">04</div>
                        <h3>Follow-through</h3>
                        <p>Prepare replies, schedule tasks or hand off to a human with enough context.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">What gets automated</div>
                <h2 class="section-title">The parts of the business that create the most <span class="accent">avoidable friction</span>.</h2>
            </div>
            <div class="grid-3">
                <div class="card reveal">
                    <div class="card-meta">Sales flow</div>
                    <h3>Lead handling</h3>
                    <p>Capture, qualification, CRM updates, follow-up prompts, meeting prep and proposal triggers.</p>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Operations</div>
                    <h3>Internal workflows</h3>
                    <p>Notifications, documentation, task creation, content movement and repetitive team handoffs.</p>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Client service</div>
                    <h3>AI-assisted response systems</h3>
                    <p>Useful when response speed matters, but the business still needs guardrails and human escalation points.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">How value gets measured</div>
                <h2 class="section-title">The right ROI story is built around <span class="accent">business signal</span>, not flashy dashboards.</h2>
                <p class="section-copy">Without verified client metrics, the strongest move is to define what will be measured after deployment. This version keeps the proof architecture honest.</p>
            </div>
            <div class="grid-4">
                <div class="card reveal">
                    <h3>Response speed</h3>
                    <p>How much faster can the business acknowledge, route or answer inbound demand?</p>
                </div>
                <div class="card reveal">
                    <h3>Manual effort removed</h3>
                    <p>Which repeated tasks disappear, and who gets time back as a result?</p>
                </div>
                <div class="card reveal">
                    <h3>Error reduction</h3>
                    <p>How many handoffs and duplicated entries stop breaking because the workflow now has a single path?</p>
                </div>
                <div class="card reveal">
                    <h3>Visibility gained</h3>
                    <p>Can the team see what happened, where it went and what needs human attention next?</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container detail-grid">
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-case-automation.webp" alt="Automation service concept" loading="lazy" decoding="async" width="1672" height="941">
                <div class="image-caption"><span>Flagship automation offer</span><span>AI where it is actually useful</span></div>
            </div>
            <div class="card reveal">
                <div class="card-meta">Flagship page</div>
                <h3>Merlin Protocol is now framed as a serious automation offer, not a fantasy product.</h3>
                <p>The role of Merlin is clearer in this implementation: AI-assisted workflows, knowledge-aware response layers and operational routing for businesses that need speed without chaos.</p>
                <ul class="feature-list">
                    <li>Positioned around useful use cases instead of vague mythology</li>
                    <li>Connected to the broader automation offer, not isolated from it</li>
                    <li>Built with explicit handoff and safety language</li>
                </ul>
                <div class="button-row">
                    {button("Open Merlin Protocol", "merlin-protocol.html", "secondary")}
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Safeguards</div>
                <h2 class="section-title">Automation is only premium if it stays <span class="accent">observable and controlled</span>.</h2>
            </div>
            <div class="grid-3">
                <div class="card dark reveal">
                    <h3>Documentation</h3>
                    <p>The workflow should be understandable after launch, not only by the person who built it.</p>
                </div>
                <div class="card dark reveal">
                    <h3>Fallback logic</h3>
                    <p>If a trigger breaks or the AI layer is not confident, the system needs a clear human path.</p>
                </div>
                <div class="card dark reveal">
                    <h3>Scope discipline</h3>
                    <p>The best automations solve a real bottleneck first and expand only when the baseline is already working.</p>
                </div>
            </div>
            <div class="button-row" style="margin-top: 28px;">
                {button("Start an automation brief", "contact.html?service=Automation%20and%20AI%20Workflows", "primary")}
                {button("See maintenance options", "maintenance.html", "secondary")}
            </div>
        </div>
    </section>
    """
).strip()


AGENCIES_BODY = dedent(
    f"""
    <section class="page-hero">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">For Agencies</div>
                <h1 class="hero-title">White-label execution that keeps your team looking <span class="accent">buttoned-up</span>.</h1>
                <p class="hero-lead">
                    Camelot Flows plugs into agencies as an invisible delivery layer for premium frontend builds, interaction-heavy pages and automation work that needs founder-level care without creating client-facing noise.
                </p>
                <div class="button-row">
                    {button("Discuss agency support", "contact.html?service=White-label%20Agency%20Support", "primary")}
                    {button("See Work With Me", "work-with-me.html", "secondary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-hero-agencies.webp" alt="Agency collaboration concept" loading="lazy" decoding="async" width="1536" height="1024">
                <div class="image-caption"><span>Invisible partner mode</span><span>Premium delivery under your brand</span></div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Where the partnership fits</div>
                <h2 class="section-title">Bring the studio in where the project needs extra <span class="accent">specialist weight</span>.</h2>
            </div>
            <div class="grid-3">
                <div class="card reveal">
                    <div class="card-meta">Mode 01</div>
                    <h3>Overflow build support</h3>
                    <p>Useful when internal capacity is tight but the project still needs careful frontend execution and polished launch handling.</p>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Mode 02</div>
                    <h3>Interaction and premium page craft</h3>
                    <p>Ideal for hero sections, service pages, conversion pages and animation-heavy layers that need restraint and quality.</p>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Mode 03</div>
                    <h3>Automation under agency delivery</h3>
                    <p>When the site work also needs CRM routing, intake logic or operational cleanup behind the scenes.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Signature strip</div>
                <h2 class="section-title">A moving delivery strip that shows how agency collaboration stays <span class="accent">clean and invisible</span>.</h2>
                <p class="section-copy">The animation here supports the pitch: collaboration modes slide with scroll, emphasizing that the work can slot into an existing agency machine without becoming the story.</p>
            </div>
            <div class="agency-strip" data-agency-strip>
                <div class="strip-card dark reveal">
                    <div class="card-meta">NDA-ready</div>
                    <h3>Quiet by default</h3>
                    <p>No unnecessary exposure, no loud self-branding and no confusion around who owns the client relationship.</p>
                </div>
                <div class="strip-card dark reveal">
                    <div class="card-meta">Async updates</div>
                    <h3>Easy to manage</h3>
                    <p>Clear progress notes, production-minded communication and less project management overhead for your team.</p>
                </div>
                <div class="strip-card dark reveal">
                    <div class="card-meta">Production output</div>
                    <h3>Ship-ready work</h3>
                    <p>Not just pretty mocks. Real pages, real interaction logic, real implementation support when needed.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">How the handoff works</div>
                <h2 class="section-title">A collaboration model that keeps the main agency team in <span class="accent">control</span>.</h2>
            </div>
            <div class="process-grid">
                <div class="process-step reveal">
                    <div class="process-step-number">01 - Brief</div>
                    <h3>Scope and constraints</h3>
                    <p>What needs to be built, which parts are sensitive and how communication should run.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">02 - Build</div>
                    <h3>Focused delivery</h3>
                    <p>Implementation is handled with the agency standard, file structure and quality bar in mind.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">03 - Review</div>
                    <h3>Clean revisions</h3>
                    <p>Feedback gets translated into practical refinements instead of defensive process churn.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">04 - Handoff</div>
                    <h3>Ready for your client layer</h3>
                    <p>The result should feel like a strong extension of your team, not an awkward external dependency.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Fit check</div>
                <h2 class="section-title">When the partnership is a strong fit, and when it probably <span class="accent">is not</span>.</h2>
            </div>
            <div class="fit-grid">
                <div class="card fit-card good reveal">
                    <div class="card-meta">Strong fit</div>
                    <h3>High standards, clear expectations, premium output required</h3>
                    <ul class="feature-list">
                        <li>Agencies selling premium web or strategy work</li>
                        <li>Teams that need a reliable specialist layer</li>
                        <li>Projects where brand trust and implementation quality both matter</li>
                    </ul>
                </div>
                <div class="card fit-card bad reveal">
                    <div class="card-meta">Probably not</div>
                    <h3>Projects that only optimize for speed at any cost</h3>
                    <ul class="feature-list">
                        <li>Volume-first low-attention landing page factories</li>
                        <li>Teams that need constant live-call dependency</li>
                        <li>Projects with unstable scope and no decision owner</li>
                    </ul>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Proof note</div>
                    <h3>Case study layer pending</h3>
                    <p>Real white-label case studies should be added once usage permissions and sanitized proof assets are available.</p>
                    <div class="placeholder-note">Add anonymized before and after examples, delivery scope, timeline, and the agency-side value created.</div>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container detail-grid">
            <div class="card reveal">
                <div class="card-meta">What agencies get</div>
                <h3>Less delivery pressure on your side without lowering the standard.</h3>
                <p>Use Camelot Flows when the project needs a founder-level build mindset, stronger page craft, cleaner motion or automation support behind the scenes.</p>
                <div class="button-row">
                    {button("Start an agency conversation", "contact.html?service=White-label%20Agency%20Support", "primary")}
                    {button("See the Arsenal", "arsenal.html", "secondary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-hero-work.webp" alt="Collaboration and delivery overview" loading="lazy" decoding="async" width="1536" height="1024">
                <div class="image-caption"><span>Agency support</span><span>Quiet execution, visible quality</span></div>
            </div>
        </div>
    </section>
    """
).strip()


CASE_STUDIES_BODY = dedent(
    f"""
    <section class="page-hero hero-compact">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">Case Studies</div>
                <h1 class="hero-title">Proof structure first, verified metrics <span class="accent">as they become available</span>.</h1>
                <p class="hero-lead">
                    This page is intentionally honest. The structure is built for serious case studies, but every metric and testimonial should only be filled with verified proof. Until then, placeholders stay explicit.
                </p>
                <div class="button-row">
                    {button("Start a similar project", "contact.html", "primary")}
                    {button("See the Arsenal", "arsenal.html", "secondary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-case-roundtable.webp" alt="Case study page concept" loading="lazy" decoding="async" width="1672" height="941">
                <div class="image-caption"><span>Proof architecture</span><span>Ready for real client evidence</span></div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container case-layout">
            <div class="card reveal">
                <div class="case-card__image"><img src="assets/images/cozy-freelancer/cf-cozy-case-site.webp" alt="Premium website case placeholder" loading="lazy" decoding="async" width="1672" height="941"></div>
                <div class="case-card__body">
                    <div class="card-meta">Website case placeholder</div>
                    <h3>Premium service website repositioning</h3>
                    <p>Challenge: the business had strong delivery but a weak digital first impression. Work: new IA, sharper messaging, premium visual system, stronger CTA flow. Outcome: <strong>[replace with verified lead quality or conversion signal]</strong>.</p>
                    <div class="case-meta">
                        <span class="tag">Positioning</span>
                        <span class="tag">Design system</span>
                        <span class="tag">Conversion path</span>
                    </div>
                </div>
            </div>
            <div class="card reveal">
                <div class="case-card__image"><img src="assets/images/cozy-freelancer/cf-cozy-case-automation.webp" alt="Automation case placeholder" loading="lazy" decoding="async" width="1672" height="941"></div>
                <div class="case-card__body">
                    <div class="card-meta">Automation case placeholder</div>
                    <h3>Lead handling and follow-up workflow</h3>
                    <p>Challenge: inbound demand was handled manually across too many channels. Work: intake logic, qualification, CRM sync, follow-up prompts and handoff rules. Outcome: <strong>[replace with verified time saved or response speed]</strong>.</p>
                    <div class="case-meta">
                        <span class="tag">Workflow design</span>
                        <span class="tag">CRM sync</span>
                        <span class="tag">Human handoff</span>
                    </div>
                </div>
            </div>
            <div class="card reveal">
                <div class="case-card__image"><img src="assets/images/cozy-freelancer/cf-cozy-hero-agencies.webp" alt="Agency partner case placeholder" loading="lazy" decoding="async" width="1536" height="1024"></div>
                <div class="case-card__body">
                    <div class="card-meta">Agency case placeholder</div>
                    <h3>White-label premium build support</h3>
                    <p>Challenge: the agency needed a specialist execution layer for a high-touch launch. Work: focused page craft, interaction implementation and cleaner handoff. Outcome: <strong>[replace with verified timeline or retention signal]</strong>.</p>
                    <div class="case-meta">
                        <span class="tag">White-label</span>
                        <span class="tag">Frontend</span>
                        <span class="tag">Launch support</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">What each real case should include</div>
                <h2 class="section-title">A case study should show the business problem, the work, the result and the <span class="accent">proof source</span>.</h2>
            </div>
            <div class="process-grid">
                <div class="process-step reveal">
                    <div class="process-step-number">Problem</div>
                    <h3>What was not working</h3>
                    <p>Weak positioning, slow follow-up, low trust, fragile workflows or missing clarity.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">Work</div>
                    <h3>What got built or changed</h3>
                    <p>Specific deliverables, pages, automations, integrations, launch support and iteration cycles.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">Result</div>
                    <h3>What changed after launch</h3>
                    <p>Only verified metrics or credible qualitative outcomes, never vanity language with no source.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">Proof</div>
                    <h3>Where the proof came from</h3>
                    <p>Analytics, CRM logs, client statements, recorded ops changes or approved testimonial snippets.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Proof assets to request</div>
                <h2 class="section-title">The next round of credibility comes from <span class="accent">real evidence</span>.</h2>
            </div>
            <div class="grid-4">
                <div class="card dark reveal">
                    <h3>Before and after screenshots</h3>
                    <p>Enough to show visual improvement and structural clarity.</p>
                </div>
                <div class="card dark reveal">
                    <h3>Verified metrics</h3>
                    <p>Leads, close rate, response speed, hours saved or any grounded operational indicator.</p>
                </div>
                <div class="card dark reveal">
                    <h3>Short testimonial lines</h3>
                    <p>Client language about trust, process or speed that can be quoted accurately.</p>
                </div>
                <div class="card dark reveal">
                    <h3>Scope summary</h3>
                    <p>Pages built, workflows created, integrations touched and timeline constraints handled.</p>
                </div>
            </div>
        </div>
    </section>
    """
).strip()


ARSENAL_BODY = dedent(
    f"""
    <section class="page-hero hero-compact">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">Arsenal</div>
                <h1 class="hero-title">Selected capability pieces, direction studies and <span class="accent">showcase work</span>.</h1>
                <p class="hero-lead">
                    The Arsenal is positioned as a portfolio and capability showcase, not as a fake product catalog. It gives prospects a faster read on visual range, system thinking and offer depth.
                </p>
                <div class="button-row">
                    {button("Start a project", "contact.html", "primary")}
                    {button("See case study structure", "case-studies.html", "secondary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-hero-arsenal.webp" alt="Arsenal showcase interface" loading="lazy" decoding="async" width="1536" height="1024">
                <div class="image-caption"><span>Portfolio layer</span><span>Curated, not crowded</span></div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="arsenal-filters reveal">
                <button class="filter-button is-active" type="button" data-filter-button="all">All</button>
                <button class="filter-button" type="button" data-filter-button="web">Web</button>
                <button class="filter-button" type="button" data-filter-button="automation">Automation</button>
                <button class="filter-button" type="button" data-filter-button="agency">Agency</button>
                <button class="filter-button" type="button" data-filter-button="systems">Systems</button>
            </div>
            <div class="grid-3">
                <div class="card arsenal-card reveal" data-filter-card="web systems">
                    <div class="case-card__image"><img src="assets/images/cozy-freelancer/cf-cozy-hero-arsenal.webp" alt="Premium web showcase" loading="lazy" decoding="async" width="1536" height="1024"></div>
                    <div class="case-card__body">
                        <div class="card-meta">Web showcase</div>
                        <h3>Premium service site direction</h3>
                        <p>Editorial pacing, strong typographic hierarchy and a more trustworthy first impression for premium service brands.</p>
                        <div class="tag-row"><span class="tag">Web</span><span class="tag">Positioning</span></div>
                    </div>
                </div>
                <div class="card arsenal-card reveal" data-filter-card="automation systems">
                    <div class="case-card__image"><img src="assets/images/cozy-freelancer/cf-cozy-case-automation.webp" alt="Automation showcase" loading="lazy" decoding="async" width="1672" height="941"></div>
                    <div class="case-card__body">
                        <div class="card-meta">Automation showcase</div>
                        <h3>Operational workflow interface</h3>
                        <p>Visual language for AI-assisted routing, internal ops visibility and workflow control layers.</p>
                        <div class="tag-row"><span class="tag">Automation</span><span class="tag">Workflow</span></div>
                    </div>
                </div>
                <div class="card arsenal-card reveal" data-filter-card="agency web">
                    <div class="case-card__image"><img src="assets/images/cozy-freelancer/cf-cozy-hero-agencies.webp" alt="Agency support showcase" loading="lazy" decoding="async" width="1536" height="1024"></div>
                    <div class="case-card__body">
                        <div class="card-meta">Agency support</div>
                        <h3>White-label premium build layer</h3>
                        <p>Delivery direction for agencies that need clean frontend craft without exposing an external partner.</p>
                        <div class="tag-row"><span class="tag">Agency</span><span class="tag">Frontend</span></div>
                    </div>
                </div>
                <div class="card arsenal-card reveal" data-filter-card="web">
                    <div class="case-card__image"><img src="assets/images/cozy-freelancer/cf-cozy-case-site.webp" alt="Landing page showcase" loading="lazy" decoding="async" width="1672" height="941"></div>
                    <div class="case-card__body">
                        <div class="card-meta">Landing page</div>
                        <h3>Focused launch experience</h3>
                        <p>A tighter, more commercial approach for founder-led offers that need a premium first impression fast.</p>
                        <div class="tag-row"><span class="tag">Web</span><span class="tag">Launch</span></div>
                    </div>
                </div>
                <div class="card arsenal-card reveal" data-filter-card="systems automation">
                    <div class="case-card__image"><img src="assets/images/cozy-freelancer/cf-cozy-case-roundtable.webp" alt="Internal system showcase" loading="lazy" decoding="async" width="1672" height="941"></div>
                    <div class="case-card__body">
                        <div class="card-meta">Systems</div>
                        <h3>Internal admin or reporting layer</h3>
                        <p>Useful when off-the-shelf tools stop matching how the business actually works.</p>
                        <div class="tag-row"><span class="tag">Systems</span><span class="tag">Internal tools</span></div>
                    </div>
                </div>
                <div class="card arsenal-card reveal" data-filter-card="automation agency">
                    <div class="case-card__image"><img src="assets/images/cozy-freelancer/cf-cozy-hero-merlin.webp" alt="Merlin protocol showcase" loading="lazy" decoding="async" width="1536" height="1024"></div>
                    <div class="case-card__body">
                        <div class="card-meta">Flagship offer</div>
                        <h3>Merlin Protocol</h3>
                        <p>AI-assisted workflow direction framed as a serious automation service with human handoff logic.</p>
                        <div class="tag-row"><span class="tag">Automation</span><span class="tag">AI</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
).strip()


ABOUT_BODY = dedent(
    f"""
    <section class="page-hero">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">About Camelot Flows</div>
                <h1 class="hero-title">Founder-led by design. Built for clients who want sharper <span class="accent">signal and less drag</span>.</h1>
                <p class="hero-lead">
                    Camelot Flows is positioned like a boutique studio: closer to the business problem, closer to the quality bar and closer to implementation than the usual handoff-heavy process.
                </p>
                <div class="button-row">
                    {button("Work with Camelot Flows", "contact.html", "primary")}
                    {button("See the work model", "work-with-me.html", "secondary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-hero-about.webp" alt="Founder page concept" loading="lazy" decoding="async" width="1536" height="1024">
                <div class="image-caption"><span>Founder-led studio</span><span>Premium, direct, international</span></div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container detail-grid">
            <div class="card reveal">
                <div class="card-meta">Founder profile</div>
                <h3>Alex Buzi, building across design clarity and operational systems.</h3>
                <p>The strongest version of the positioning is not "I can do everything." It is "I can improve how the business looks, how the site sells and how the workflow runs, inside one more disciplined process."</p>
                <ul class="feature-list">
                    <li>Founder-level involvement from discovery through build</li>
                    <li>English, Russian and Romanian context for international work</li>
                    <li>Better fit for businesses that value clarity, speed and craft</li>
                </ul>
            </div>
            <div class="card reveal">
                <div class="card-meta">What the studio cares about</div>
                <h3>Sharp communication, commercial relevance and the details that make a site feel expensive.</h3>
                <p>The philosophy is intentionally practical: less vague creative theatre, more work that helps the business look credible and operate with less friction.</p>
                <div class="tag-row">
                    <span class="tag">Positioning</span>
                    <span class="tag">Design systems</span>
                    <span class="tag">Automation</span>
                    <span class="tag">Selective motion</span>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Timeline</div>
                <h2 class="section-title">A clearer founder story with enough structure to feel <span class="accent">credible</span>.</h2>
            </div>
            <div class="timeline">
                <div class="timeline-item reveal">
                    <div class="card-meta">Foundation</div>
                    <h3>Design sensitivity meets implementation depth</h3>
                    <p class="timeline-copy">The studio position works because it does not separate aesthetics from build quality or build quality from business logic.</p>
                </div>
                <div class="timeline-item reveal">
                    <div class="card-meta">Expansion</div>
                    <h3>Web craft extends into systems thinking</h3>
                    <p class="timeline-copy">Automation becomes a natural second pillar once the business starts needing cleaner intake, routing and follow-up.</p>
                </div>
                <div class="timeline-item reveal">
                    <div class="card-meta">Current mode</div>
                    <h3>Hybrid premium, founder-led, internationally relevant</h3>
                    <p class="timeline-copy">The current positioning is built for premium service businesses, agencies and founders that want a smaller, sharper partner.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Principles</div>
                <h2 class="section-title">What the studio tries to protect on every engagement.</h2>
            </div>
            <div class="grid-3">
                <div class="card dark reveal">
                    <h3>Clarity before drama</h3>
                    <p>The site should sell the offer first. Motion and styling should amplify that, not replace it.</p>
                </div>
                <div class="card dark reveal">
                    <h3>Premium means restraint</h3>
                    <p>Not every page needs to shout. The strongest moments come from contrast, pacing and selective emphasis.</p>
                </div>
                <div class="card dark reveal">
                    <h3>Systems should remove noise</h3>
                    <p>Automation is useful when it reduces friction and gives the team better visibility, not when it adds complexity for its own sake.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container detail-grid">
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-hero-about.webp" alt="Additional founder page direction" loading="lazy" decoding="async" width="1536" height="1024">
                <div class="image-caption"><span>Founder perspective</span><span>Small studio, sharper involvement</span></div>
            </div>
            <div class="card reveal">
                <div class="card-meta">What happens next</div>
                <h3>If the fit is there, the next step is a better brief, not a longer sales process.</h3>
                <p>The new contact structure is designed to collect the business context early so the first conversation starts closer to real scope and real value.</p>
                <div class="button-row">
                    {button("Open contact", "contact.html", "primary")}
                    {button("See agency support", "for-agencies.html", "secondary")}
                </div>
            </div>
        </div>
    </section>
    """
).strip()


WORK_WITH_ME_BODY = dedent(
    f"""
    <section class="page-hero">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">Work With Me</div>
                <h1 class="hero-title">A working model built for direct decisions, premium craft and <span class="accent">less friction</span>.</h1>
                <p class="hero-lead">
                    This page clarifies how projects run, what makes a strong fit, what to expect before the first call and how Camelot Flows keeps the process practical for both founder-led brands and agency teams.
                </p>
                <div class="button-row">
                    {button("Start a structured inquiry", "contact.html", "primary")}
                    {button("See the founder story", "about.html", "secondary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-hero-work.webp" alt="Work with me page concept" loading="lazy" decoding="async" width="1536" height="1024">
                <div class="image-caption"><span>Working model</span><span>Fast signals, cleaner process</span></div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Fit</div>
                <h2 class="section-title">A strong fit usually looks like this.</h2>
            </div>
            <div class="fit-grid">
                <div class="card fit-card good reveal">
                    <div class="card-meta">Good fit</div>
                    <h3>You already know the business is real and the current digital layer is lagging behind.</h3>
                    <ul class="feature-list">
                        <li>The offer already has traction or clear intent</li>
                        <li>You care about trust, positioning and how the site feels</li>
                        <li>You want someone who can think in both design and systems</li>
                    </ul>
                </div>
                <div class="card fit-card good reveal">
                    <div class="card-meta">Also good</div>
                    <h3>You want a smaller partner with more direct execution and less sales theatre.</h3>
                    <ul class="feature-list">
                        <li>Founder or operator can make decisions quickly</li>
                        <li>Scope can be discussed honestly</li>
                        <li>Quality matters more than volume for volume's sake</li>
                    </ul>
                </div>
                <div class="card fit-card bad reveal">
                    <div class="card-meta">Probably not</div>
                    <h3>You need a giant agency structure more than you need sharper work.</h3>
                    <ul class="feature-list">
                        <li>Too many decision-makers and no project owner</li>
                        <li>No clarity on goals, audience or timeline pressure</li>
                        <li>Commodity pricing expectations for premium work</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">Typical engagement shapes</div>
                <h2 class="section-title">Most projects land in one of three practical lanes.</h2>
            </div>
            <div class="grid-3">
                <div class="card reveal">
                    <div class="card-meta">Lane 01</div>
                    <h3>Website-first</h3>
                    <p>Use this when the business needs clearer positioning, better authority and a stronger first impression.</p>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Lane 02</div>
                    <h3>Automation-first</h3>
                    <p>Use this when follow-up, intake, routing or internal ops are clearly slowing the business down.</p>
                </div>
                <div class="card reveal">
                    <div class="card-meta">Lane 03</div>
                    <h3>Combined scope</h3>
                    <p>Use this when the public-facing site and the operational flow need to be rebuilt as part of the same commercial system.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container detail-grid">
            <div class="card dark reveal">
                <div class="card-meta">Before the first call</div>
                <h3>The most useful things to send early</h3>
                <ul class="feature-list">
                    <li>What you sell and who buys it</li>
                    <li>What feels weak in the current site or workflow</li>
                    <li>What should happen after a user contacts you</li>
                    <li>Any hard launch dates or internal constraints</li>
                </ul>
            </div>
            <div class="card dark reveal">
                <div class="card-meta">Working rhythm</div>
                <h3>Async-friendly, direct and easy to keep moving</h3>
                <p>Projects work best when feedback stays focused, decision loops stay short and the brief gets stronger before polish starts.</p>
                <div class="button-row">
                    {button("Send the brief", "contact.html", "primary")}
                </div>
            </div>
        </div>
    </section>
    """
).strip()


CONTACT_BODY = dedent(
    f"""
    <section class="page-hero hero-compact">
        <div class="container">
            <div class="section-header centered reveal">
                <div class="section-kicker">Contact</div>
                <h1 class="hero-title">Send a project brief with more signal and less <span class="accent">back-and-forth</span>.</h1>
                <p class="hero-lead" style="margin-left:auto; margin-right:auto;">
                    The new inquiry flow qualifies by service, budget, timeline, market and business goal. That means the first reply can start closer to real scope.
                </p>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container form-layout">
            <div class="form-shell reveal">
                <div class="progress-bar"><div class="progress-fill" data-progress-fill></div></div>
                <h3>Project inquiry</h3>
                <p class="form-note">Submitting opens your email app with a structured brief. This keeps the static site functional without pretending there is a backend in place.</p>
                <form data-progress-form>
                    <div class="form-grid">
                        <label class="field"><span class="field-label">Name</span><input type="text" name="name" required placeholder="Your name"></label>
                        <label class="field"><span class="field-label">Email</span><input type="email" name="email" required placeholder="you@company.com"></label>
                        <label class="field">
                            <span class="field-label">Service</span>
                            <select name="service" required>
                                <option value="">Select a focus</option>
                                <option value="Website Design and Build">Website Design and Build</option>
                                <option value="Automation and AI Workflows">Automation and AI Workflows</option>
                                <option value="White-label Agency Support">White-label Agency Support</option>
                                <option value="Maintenance and Optimization">Maintenance and Optimization</option>
                                <option value="Growth and Landing Pages">Growth and Landing Pages</option>
                                <option value="Something else">Something else</option>
                            </select>
                        </label>
                        <label class="field">
                            <span class="field-label">Budget</span>
                            <select name="budget" required>
                                <option value="">Choose a budget range</option>
                                <option value="Under 2k">Under 2k</option>
                                <option value="2k to 5k">2k to 5k</option>
                                <option value="5k to 10k">5k to 10k</option>
                                <option value="10k plus">10k plus</option>
                                <option value="Need help scoping first">Need help scoping first</option>
                            </select>
                        </label>
                        <label class="field">
                            <span class="field-label">Timeline</span>
                            <select name="timeline" required>
                                <option value="">Choose a timeline</option>
                                <option value="ASAP">ASAP</option>
                                <option value="Within 2 to 4 weeks">Within 2 to 4 weeks</option>
                                <option value="Within 1 to 2 months">Within 1 to 2 months</option>
                                <option value="Flexible but soon">Flexible but soon</option>
                            </select>
                        </label>
                        <label class="field"><span class="field-label">Market</span><input type="text" name="market" required placeholder="Who you sell to and where"></label>
                        <label class="field full"><span class="field-label">Project goal</span><textarea name="project_goal" required placeholder="What are you trying to improve, launch or fix? Include the main business goal, what feels weak today, and what success would look like."></textarea></label>
                    </div>
                    <div class="button-row">
                        <button type="submit" class="button primary">Prepare the inquiry</button>
                        <a href="mailto:hello@camelotflows.com" class="button secondary">Email directly</a>
                    </div>
                    <p class="form-note" data-form-status></p>
                </form>
            </div>
            <div class="contact-sidebar reveal">
                <h3>Best-fit signals</h3>
                <div class="sidebar-block">
                    <div class="card-meta">Good starting point</div>
                    <p>You already have a real offer, but the site, workflow or follow-up layer is not doing it justice yet.</p>
                </div>
                <div class="sidebar-block">
                    <div class="card-meta">Helpful context</div>
                    <p>Share links to the current site, competitor references, live assets, automation pain points and any launch deadline.</p>
                </div>
                <div class="sidebar-block">
                    <div class="card-meta">Working region</div>
                    <p>English-first delivery with context for RU and RO markets. Founder-led, async-friendly and comfortable with international work.</p>
                </div>
                <div class="sidebar-block">
                    <img src="assets/images/cozy-freelancer/cf-cozy-hero-contact.webp" alt="Contact page mockup" loading="lazy" decoding="async" width="1672" height="941">
                </div>
            </div>
        </div>
    </section>

    <section class="section section-alt">
        <div class="container">
            <div class="section-header reveal">
                <div class="section-kicker">What happens after you send the brief</div>
                <h2 class="section-title">Clearer next steps, not an overcomplicated sales funnel.</h2>
            </div>
            <div class="process-grid">
                <div class="process-step reveal">
                    <div class="process-step-number">01</div>
                    <h3>Quick fit review</h3>
                    <p>The project is screened for fit, urgency and the most useful direction for the first conversation.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">02</div>
                    <h3>Reply with context</h3>
                    <p>You get a response anchored in scope, questions and likely next steps rather than a generic availability message.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">03</div>
                    <h3>Discovery conversation</h3>
                    <p>If the fit is there, the conversation moves toward real goals, constraints and delivery shape.</p>
                </div>
                <div class="process-step reveal">
                    <div class="process-step-number">04</div>
                    <h3>Scope direction</h3>
                    <p>The output is a clearer plan for a website build, automation system, agency support model or combined scope.</p>
                </div>
            </div>
        </div>
    </section>
    """
).strip()


MAINTENANCE_BODY = dedent(
    f"""
    <section class="page-hero hero-compact">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">Maintenance and Optimization</div>
                <h1 class="hero-title">Post-launch support for sites and systems that still need to feel <span class="accent">looked after</span>.</h1>
                <p class="hero-lead">Maintenance is positioned as a support layer, not the headline offer. It exists for clients that want stability, iteration and someone close enough to fix issues before they grow.</p>
                <div class="button-row">
                    {button("Ask about support", "contact.html?service=Maintenance%20and%20Optimization", "primary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-case-roundtable.webp" alt="Maintenance support concept" loading="lazy" decoding="async" width="1672" height="941">
                <div class="image-caption"><span>Support layer</span><span>Monitoring, fixes and iteration</span></div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container grid-3">
            <div class="card reveal">
                <div class="card-meta">Monitoring</div>
                <h3>Site and workflow health</h3>
                <p>Keep watch on forms, delivery routes, broken sections, content issues and basic operational reliability.</p>
            </div>
            <div class="card reveal">
                <div class="card-meta">Iteration</div>
                <h3>Small improvements that keep compounding</h3>
                <p>Post-launch pages, CTA refinements, content adjustments and experience tuning without turning every change into a new project.</p>
            </div>
            <div class="card reveal">
                <div class="card-meta">Stability</div>
                <h3>A cleaner long-term ownership layer</h3>
                <p>Good maintenance makes the digital system feel cared for instead of fragile.</p>
            </div>
        </div>
    </section>
    """
).strip()


GROWTH_BODY = dedent(
    f"""
    <section class="page-hero hero-compact">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">Growth and Landing Pages</div>
                <h1 class="hero-title">A support offer for the pages, flows and measurements that help the main site <span class="accent">work harder</span>.</h1>
                <p class="hero-lead">Growth support should not compete with the core offer. It sits underneath it: landing page refinement, message testing, analytics clarity and small conversion improvements after the main system exists.</p>
                <div class="button-row">
                    {button("Ask about growth support", "contact.html?service=Growth%20and%20Landing%20Pages", "primary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-case-site.webp" alt="Growth and landing pages concept" loading="lazy" decoding="async" width="1672" height="941">
                <div class="image-caption"><span>Support layer</span><span>Pages, CRO and measurement</span></div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container grid-3">
            <div class="card reveal">
                <div class="card-meta">Landing pages</div>
                <h3>Focused campaign and service pages</h3>
                <p>Designed to support traffic, launches or sharper offer segmentation without bloating the main site.</p>
            </div>
            <div class="card reveal">
                <div class="card-meta">CRO</div>
                <h3>Conversion-focused refinements</h3>
                <p>Message order, CTA placement, proof sequencing and friction reduction after the main structure is in place.</p>
            </div>
            <div class="card reveal">
                <div class="card-meta">Measurement</div>
                <h3>Better read on what matters</h3>
                <p>Analytics and form logic that help the business see whether the site is attracting better conversations.</p>
            </div>
        </div>
    </section>
    """
).strip()


MERLIN_BODY = dedent(
    f"""
    <section class="page-hero">
        <div class="container hero-layout">
            <div class="hero-copy reveal">
                <div class="hero-eyebrow">Merlin Protocol</div>
                <h1 class="hero-title">The flagship automation page for AI-assisted routing, response and <span class="accent">operational clarity</span>.</h1>
                <p class="hero-lead">Merlin is no longer treated like a fantasy product. In this implementation it reads as a serious service layer for businesses that need faster response and cleaner operational handling with human control intact.</p>
                <div class="button-row">
                    {button("Ask about Merlin", "contact.html?service=Automation%20and%20AI%20Workflows", "primary")}
                    {button("Back to automation", "automation.html", "secondary")}
                </div>
            </div>
            <div class="image-frame reveal">
                <img src="assets/images/cozy-freelancer/cf-cozy-hero-merlin.webp" alt="Merlin protocol showcase" loading="lazy" decoding="async" width="1536" height="1024">
                <div class="image-caption"><span>Flagship automation page</span><span>AI with human handoff rules</span></div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container grid-3">
            <div class="card dark reveal"><div class="card-meta">Use case</div><h3>Inbound qualification</h3><p>Understand what came in, how urgent it is and where it should go next.</p></div>
            <div class="card dark reveal"><div class="card-meta">Use case</div><h3>AI-assisted reply drafting</h3><p>Prepare faster responses based on business context and known offer language.</p></div>
            <div class="card dark reveal"><div class="card-meta">Use case</div><h3>Human handoff with context</h3><p>When confidence drops or nuance matters, the right person gets the right context quickly.</p></div>
        </div>
    </section>

    <section class="section">
        <div class="container detail-grid">
            <div class="card reveal"><div class="card-meta">Rollout logic</div><h3>Start narrow, then expand.</h3><p>The best Merlin deployments begin with one clear bottleneck, prove value there, and only then grow into wider operational coverage.</p></div>
            <div class="card reveal"><div class="card-meta">Proof note</div><h3>Case studies should be tied to verified ops signal.</h3><p>When Merlin proof is added later, it should focus on response speed, lead routing quality, time saved and visibility gained.</p></div>
        </div>
    </section>
    """
).strip()


LEGAL_BODY = dedent(
    """
    <section class="page-hero hero-compact">
        <div class="container">
            <div class="section-header centered reveal">
                <div class="section-kicker">Legal</div>
                <h1 class="hero-title">Structural legal page placeholder pending final business details and professional review.</h1>
                <p class="hero-lead" style="margin-left:auto; margin-right:auto;">This page provides the right structure for a legal page, but it should be reviewed and completed with jurisdiction-specific details before production use.</p>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container legal-doc">
            <div class="card reveal">
                <h3>Business details</h3>
                <ul class="legal-list">
                    <li>Add the legal entity or sole proprietor details.</li>
                    <li>Add registered address, contact email and operating jurisdiction.</li>
                    <li>Add invoicing and contract references used in production.</li>
                </ul>
            </div>
            <div class="card reveal">
                <h3>Terms structure</h3>
                <ul class="legal-list">
                    <li>Scope and deliverables are governed by project agreements.</li>
                    <li>Payment, revisions, timelines and intellectual property should be defined in signed project documents.</li>
                    <li>Any live legal language should be reviewed by qualified counsel.</li>
                </ul>
            </div>
        </div>
    </section>
    """
).strip()


PRIVACY_BODY = dedent(
    """
    <section class="page-hero hero-compact">
        <div class="container">
            <div class="section-header centered reveal">
                <div class="section-kicker">Privacy</div>
                <h1 class="hero-title">Privacy page structure for a lead-generation site, pending final review before launch.</h1>
                <p class="hero-lead" style="margin-left:auto; margin-right:auto;">This page intentionally avoids claiming legal compliance beyond what is actually configured. It should be finalized with accurate tracking, storage and jurisdiction details before production use.</p>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container legal-doc">
            <div class="card reveal">
                <h3>What the site currently collects</h3>
                <ul class="legal-list">
                    <li>Information entered into the contact form, such as name, email, service interest and project details.</li>
                    <li>Any analytics data only if analytics tooling is installed and disclosed before launch.</li>
                </ul>
            </div>
            <div class="card reveal">
                <h3>What should be confirmed before launch</h3>
                <ul class="legal-list">
                    <li>Where inquiries are stored or routed.</li>
                    <li>Which analytics, cookies or third-party embeds are active.</li>
                    <li>How deletion, access and retention requests will be handled in practice.</li>
                </ul>
            </div>
        </div>
    </section>
    """
).strip()


PAGES = {
    "index.html": page(
        "Camelot Flows - Premium Websites and Automation",
        "Founder-led premium studio for award-winning websites, automation systems and white-label agency support.",
        "index.html",
        HOME_BODY,
        "home",
    ),
    "web-design.html": page(
        "Camelot Flows - Web Design and Build",
        "Premium web design and build for service brands, consultants and founder-led businesses that need stronger positioning and trust.",
        "web-design.html",
        WEB_DESIGN_BODY,
        "web-design",
    ),
    "automation.html": page(
        "Camelot Flows - Automation and AI Workflows",
        "Business automation and AI workflow design for lead handling, follow-up and operational clarity.",
        "automation.html",
        AUTOMATION_BODY,
        "automation",
    ),
    "for-agencies.html": page(
        "Camelot Flows - For Agencies",
        "White-label premium web and automation support for agencies that need specialist execution without extra noise.",
        "for-agencies.html",
        AGENCIES_BODY,
        "agencies",
    ),
    "case-studies.html": page(
        "Camelot Flows - Case Studies",
        "Proof architecture and structured case study placeholders for verified website and automation outcomes.",
        "case-studies.html",
        CASE_STUDIES_BODY,
        "case-studies",
    ),
    "arsenal.html": page(
        "Camelot Flows - Arsenal",
        "Selected showcase work, capability pieces and premium digital direction studies from Camelot Flows.",
        "arsenal.html",
        ARSENAL_BODY,
        "arsenal",
    ),
    "about.html": page(
        "Camelot Flows - About",
        "About the founder-led studio behind Camelot Flows and the principles shaping its premium web and automation work.",
        "about.html",
        ABOUT_BODY,
        "about",
    ),
    "work-with-me.html": page(
        "Camelot Flows - Work With Me",
        "How Camelot Flows works with businesses and agencies on premium websites, automation systems and delivery support.",
        "work-with-me.html",
        WORK_WITH_ME_BODY,
        "work-with-me",
    ),
    "contact.html": page(
        "Camelot Flows - Contact",
        "Send a structured project brief for website, automation or agency support work.",
        "contact.html",
        CONTACT_BODY,
        "contact",
    ),
    "maintenance.html": page(
        "Camelot Flows - Maintenance and Optimization",
        "Post-launch support for website and automation clients who need maintenance, iteration and operational stability.",
        "maintenance.html",
        MAINTENANCE_BODY,
        "maintenance",
    ),
    "growth-marketing.html": page(
        "Camelot Flows - Growth and Landing Pages",
        "Landing page, CRO and measurement support that sits underneath the main website and automation offer.",
        "growth-marketing.html",
        GROWTH_BODY,
        "growth",
    ),
    "merlin-protocol.html": page(
        "Camelot Flows - Merlin Protocol",
        "Flagship AI-assisted automation service for routing, response and operational clarity.",
        "merlin-protocol.html",
        MERLIN_BODY,
        "merlin",
    ),
    "legal.html": page(
        "Camelot Flows - Legal",
        "Structural legal page placeholder for Camelot Flows pending final review.",
        "legal.html",
        LEGAL_BODY,
        "legal",
    ),
    "privacy.html": page(
        "Camelot Flows - Privacy",
        "Privacy page structure for Camelot Flows pending final launch review and data handling confirmation.",
        "privacy.html",
        PRIVACY_BODY,
        "privacy",
    ),
    "merlin.html": redirect_page(
        "Camelot Flows - Merlin Redirect",
        "merlin-protocol.html",
        "Legacy Merlin page redirecting to the updated Merlin Protocol page.",
    ),
    "service-creation.html": redirect_page(
        "Camelot Flows - Website Service Redirect",
        "web-design.html",
        "Legacy service page redirecting to the updated web design page.",
    ),
    "service-maintenance.html": redirect_page(
        "Camelot Flows - Maintenance Redirect",
        "maintenance.html",
        "Legacy maintenance page redirecting to the updated maintenance page.",
    ),
    "service-automation.html": redirect_page(
        "Camelot Flows - Automation Redirect",
        "automation.html",
        "Legacy automation page redirecting to the updated automation page.",
    ),
    "service-marketing.html": redirect_page(
        "Camelot Flows - Growth Redirect",
        "growth-marketing.html",
        "Legacy marketing page redirecting to the updated growth page.",
    ),
}


def copy_images() -> None:
    ASSETS_DIR.mkdir(exist_ok=True)
    IMAGES_DIR.mkdir(exist_ok=True)
    for target_name, source in IMAGE_MAP.items():
        if not source.exists():
            raise FileNotFoundError(f"Missing source image: {source}")
        shutil.copy2(source, IMAGES_DIR / target_name)


def write_pages() -> None:
    for name, html in PAGES.items():
        (ROOT / name).write_text(html, encoding="utf-8")


def main() -> None:
    copy_images()
    write_pages()
    print(f"Generated {len(PAGES)} HTML pages and copied {len(IMAGE_MAP)} images.")


if __name__ == "__main__":
    main()
