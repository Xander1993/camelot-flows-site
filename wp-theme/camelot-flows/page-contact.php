<?php
/* Template Name: Contact */
get_header(); ?>

<main class="page-shell" style="padding-top:88px">

  <!-- Hero -->
  <section style="padding:96px 0 56px;position:relative;">
    <div aria-hidden="true" style="position:absolute;inset:0;background:url('<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-hero-contact.webp'); ?>') center/cover no-repeat;opacity:0.11;mix-blend-mode:multiply;pointer-events:none;"></div>
    <div class="container" style="position:relative;z-index:1;">
      <div class="hero-copy">
        <p class="hero-eyebrow">Response within 24 hours · EET (UTC+2)</p>
        <h1 class="hero-title">Tell me about <em class="accent">the work.</em></h1>
        <p class="hero-lead">Describe what you're trying to build. I'll read it, think about it, and reply with either a clear next step or an honest "this isn't the right fit."</p>
      </div>
    </div>
  </section>

  <!-- Form + Sidebar -->
  <section class="section tight">
    <div class="container">
      <div class="form-layout">

        <!-- Form -->
        <div class="form-shell">
          <form name="contact" action="mailto:alex@camelotflows.dev" method="POST" data-progress-form>
            <input type="hidden" name="objective" value="">
            <div class="progress-bar"><div class="progress-fill" data-progress-fill style="width:0%"></div></div>

            <div class="form-grid">
              <div class="field">
                <label class="field-label" for="c-name">Your name</label>
                <input id="c-name" type="text" name="name" placeholder="Alex" required>
              </div>
              <div class="field">
                <label class="field-label" for="c-email">Your email</label>
                <input id="c-email" type="email" name="email" placeholder="alex@example.com" required>
              </div>
              <div class="field">
                <label class="field-label" for="c-service">What are you looking for?</label>
                <select id="c-service" name="service" required>
                  <option value="">Choose one…</option>
                  <option value="site">A new website (The Site)</option>
                  <option value="staff">AI automation + agents (The Staff)</option>
                  <option value="round-table">Both together (The Round Table)</option>
                  <option value="agency">Agency overflow / white-label work</option>
                  <option value="other">Something else — I'll explain below</option>
                </select>
              </div>
              <div class="field">
                <label class="field-label" for="c-budget">Rough budget</label>
                <select id="c-budget" name="budget">
                  <option value="">I'd rather discuss it</option>
                  <option value="under-2k">Under €2,000</option>
                  <option value="2k-5k">€2,000 – €5,000</option>
                  <option value="5k-10k">€5,000 – €10,000</option>
                  <option value="10k+">€10,000+</option>
                </select>
              </div>
              <div class="field full">
                <label class="field-label" for="c-goal">What are you trying to accomplish?</label>
                <textarea id="c-goal" name="project_goal" rows="5"
                  placeholder="Describe the problem or goal in plain language. No need to be formal — a few sentences is fine." required></textarea>
              </div>
            </div>

            <div style="margin-top:24px;display:flex;align-items:center;gap:16px;flex-wrap:wrap">
              <button type="submit" class="button primary">Send message</button>
              <p class="form-note" data-form-status style="margin:0">I read every message and reply within 24 hours.</p>
            </div>
          </form>
        </div>

        <!-- Sidebar -->
        <div class="contact-sidebar">
          <h3>Before you send.</h3>
          <div style="display:grid;gap:20px;margin-top:24px">
            <div class="stack-card">
              <strong>No agency, no team</strong>
              <p>You'll talk to me directly — Alexandru, the person who will build your project. No account managers, no handoffs.</p>
            </div>
            <div class="stack-card">
              <strong>24-hour replies</strong>
              <p>I respond to every message within one business day. I'm in EET (UTC+2), which overlaps fully with Western Europe and reaches US East Coast mornings.</p>
            </div>
            <div class="stack-card">
              <strong>Fixed scope, fixed price</strong>
              <p>I'll confirm whether the project fits one of my productized tiers or needs a custom scope. Either way, you'll have a clear price before any work starts.</p>
            </div>
          </div>

          <div style="margin-top:28px;padding-top:24px;border-top:1px solid var(--cf-line)">
            <p style="font-size:0.88rem;color:var(--cf-muted);line-height:1.65;margin:0">Prefer to book a call directly?</p>
            <a href="https://cal.com/camelotflows/intro" target="_blank" rel="noopener"
               class="button ghost" style="margin-top:12px">Book a 30-min intro call &rarr;</a>
            <p style="font-size:0.78rem;color:var(--cf-muted);margin:10px 0 0;line-height:1.5">
              Free, no obligation. I'll ask about your project and tell you whether I can help.
            </p>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- Testimonials -->
  <section class="py-20 px-6 relative" id="testimonials">
    <div class="absolute inset-0 grid-bg opacity-20" aria-hidden="true"></div>
    <div class="max-w-7xl mx-auto relative z-10">
      <div class="text-center mb-14">
        <span class="text-primary-glow font-mono text-xs uppercase tracking-widest mb-4 block">// CLIENT_VOICES</span>
        <h2 class="font-display text-3xl md:text-4xl font-black text-white uppercase tracking-tighter mb-3">
          In Their <span class="text-accent text-glow">Own Words</span>
        </h2>
        <p class="text-slate-400 text-sm max-w-lg mx-auto leading-relaxed">Every project is a working partnership — these clients describe what that actually felt like.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

        <!-- Vasile – Timberkids -->
        <div class="glass-card rounded-xl p-8 relative border border-primary/20 transition-all duration-300">
          <div class="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-primary/70 to-accent/50 rounded-l-xl" aria-hidden="true"></div>
          <div class="mb-5 pl-1" style="color:#f59e0b;font-size:1.05rem;letter-spacing:3px" aria-label="5 stars">★★★★★</div>
          <blockquote class="text-white/70 text-sm leading-relaxed mb-8 pl-1">
            "Working with Alexandru felt less like hiring a developer and more like gaining a creative partner. The site launched in under two weeks — buttery smooth, every animation pixel-perfect. Parents comment on it constantly."
          </blockquote>
          <div class="flex items-center gap-3 pl-1">
            <div class="w-10 h-10 rounded-full bg-gradient-to-br from-primary/60 to-accent/60 flex items-center justify-center text-white font-bold font-mono text-sm flex-shrink-0" aria-hidden="true">V</div>
            <div>
              <strong class="text-white text-sm font-semibold block leading-tight">Vasile Enache</strong>
              <span class="text-primary-glow text-xs font-mono">Timberkids</span>
            </div>
          </div>
        </div>

        <!-- Alex – First Line Garage Door -->
        <div class="glass-card rounded-xl p-8 relative border border-primary/20 transition-all duration-300">
          <div class="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-accent/70 to-primary/50 rounded-l-xl" aria-hidden="true"></div>
          <div class="mb-5 pl-1" style="color:#f59e0b;font-size:1.05rem;letter-spacing:3px" aria-label="5 stars">★★★★★</div>
          <blockquote class="text-white/70 text-sm leading-relaxed mb-8 pl-1">
            "I gave Alexandru a rough brief and a firm deadline. He came back with a design I hadn't imagined and the finished site three days early. Lead volume is noticeably up — our old site is embarrassing to look at now."
          </blockquote>
          <div class="flex items-center gap-3 pl-1">
            <div class="w-10 h-10 rounded-full bg-gradient-to-br from-accent/60 to-primary/60 flex items-center justify-center text-white font-bold font-mono text-sm flex-shrink-0" aria-hidden="true">A</div>
            <div>
              <strong class="text-white text-sm font-semibold block leading-tight">Alex Petrov</strong>
              <span class="text-primary-glow text-xs font-mono">First Line Garage Door</span>
            </div>
          </div>
        </div>

        <!-- Andrei – Legal Point -->
        <div class="glass-card rounded-xl p-8 relative border border-primary/20 transition-all duration-300">
          <div class="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-cobalt/70 to-primary/50 rounded-l-xl" aria-hidden="true"></div>
          <div class="mb-5 pl-1" style="color:#f59e0b;font-size:1.05rem;letter-spacing:3px" aria-label="5 stars">★★★★★</div>
          <blockquote class="text-white/70 text-sm leading-relaxed mb-8 pl-1">
            "We needed a site that reflected the seriousness of our firm without feeling cold. Alexandru understood immediately — clean, authoritative, and the Merlin AI contact flow saves our team hours every week."
          </blockquote>
          <div class="flex items-center gap-3 pl-1">
            <div class="w-10 h-10 rounded-full bg-gradient-to-br from-cobalt/60 to-primary/60 flex items-center justify-center text-white font-bold font-mono text-sm flex-shrink-0" aria-hidden="true">A</div>
            <div>
              <strong class="text-white text-sm font-semibold block leading-tight">Andrei Moraru</strong>
              <span class="text-primary-glow text-xs font-mono">Legal Point</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

</main>

<?php get_footer(); ?>
