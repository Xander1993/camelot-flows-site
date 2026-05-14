<?php
/* Template Name: Merlin Protocol */
get_header(); ?>

<main class="page-shell" style="padding-top:88px">

  <!-- Hero -->
  <section style="padding:96px 0 56px;position:relative;">
    <div aria-hidden="true" style="position:absolute;inset:0;background:url('<?php echo esc_url(get_template_directory_uri() . '/assets/images/cozy-freelancer/cf-cozy-hero-merlin.webp'); ?>') center/cover no-repeat;opacity:0.11;mix-blend-mode:multiply;pointer-events:none;"></div>
    <div class="container" style="position:relative;z-index:1;">
      <div class="hero-copy">
        <p class="hero-eyebrow">AI Automation · The Merlin System</p>
        <h1 class="hero-title">An AI agent that runs your <em class="accent">front-of-house.</em></h1>
        <p class="hero-lead">Merlin is a custom-built AI agent trained on your business context. It handles lead qualification, tier-1 support, and CRM sync — 24/7, without growing your headcount.</p>
        <div class="button-row">
          <a href="<?php echo esc_url(home_url('/contact/?service=staff')); ?>" class="button primary">Book a demo</a>
          <a href="<?php echo esc_url(home_url('/work-with-me/')); ?>" class="button ghost">See pricing</a>
        </div>
      </div>
    </div>
  </section>

  <!-- What Merlin does -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div class="section-header">
        <p class="section-kicker">Capabilities</p>
        <h2 class="section-title">What it replaces.</h2>
        <p class="section-copy">Every item below is something a human was doing manually before Merlin arrived. After setup, it runs on its own.</p>
      </div>
      <div class="grid-3">
        <div class="card">
          <p class="card-meta"><span class="material-symbols-outlined" style="font-size:1.1rem;vertical-align:-3px;color:var(--cf-sage)">smart_toy</span> Lead qualification</p>
          <h3>Inbound triage</h3>
          <p>Merlin reads every inbound message, classifies intent, scores lead quality, and routes to the right action — book a call, send a resource, or flag for your review.</p>
        </div>
        <div class="card highlight">
          <p class="card-meta"><span class="material-symbols-outlined" style="font-size:1.1rem;vertical-align:-3px;color:var(--cf-terracotta)">support_agent</span> Tier-1 support</p>
          <h3>Always-on support</h3>
          <p>FAQs, pricing questions, status checks, booking links — Merlin handles the first layer of support responses with context from your knowledge base. No breaks, no delays.</p>
        </div>
        <div class="card">
          <p class="card-meta"><span class="material-symbols-outlined" style="font-size:1.1rem;vertical-align:-3px;color:var(--cf-cobalt)">cable</span> CRM sync</p>
          <h3>Data without the admin</h3>
          <p>Every conversation writes to your CRM automatically. Contact records, tags, notes, and calendar events created without you touching a spreadsheet.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- How it's built -->
  <section class="section">
    <div class="container">
      <div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:start;">
        <div>
          <p class="section-kicker">The build</p>
          <h2 class="section-title">How I set it up.</h2>
          <p style="color:var(--cf-muted);font-size:1.02rem;line-height:1.75;margin:24px 0 0">Every Merlin instance is custom-built for one business. I train it on your docs, your tone, your offers, and your edge cases. Setup takes 2–3 weeks. After that, the monthly fee covers hosting, model costs, and ongoing refinement.</p>
        </div>
        <div style="display:grid;gap:16px;margin-top:4px">
          <div class="stack-card">
            <strong>Week 1 — Knowledge build</strong>
            <p>I ingest your docs, FAQs, pricing, and past conversations to build the context base.</p>
          </div>
          <div class="stack-card">
            <strong>Week 2 — Workflow wiring</strong>
            <p>n8n flows connect Merlin to your CRM, calendar, inbox, and any tools it needs to act.</p>
          </div>
          <div class="stack-card">
            <strong>Week 3 — Testing and handoff</strong>
            <p>We run real scenarios together until you're confident it handles your edge cases correctly.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Pricing CTA -->
  <section class="section" style="background:rgba(255,255,255,0.32);">
    <div class="container">
      <div style="text-align:center;max-width:540px;margin:0 auto">
        <p class="section-kicker">Pricing</p>
        <h2 class="section-title">€2,400 setup · €600/mo</h2>
        <p style="color:var(--cf-muted);font-size:1.02rem;line-height:1.75;margin:20px 0 32px">Fixed setup, cancel anytime. The monthly fee covers Claude API costs, n8n hosting, and my time to keep the agent accurate as your business evolves.</p>
        <div class="button-row" style="justify-content:center">
          <a href="<?php echo esc_url(home_url('/contact/?service=staff')); ?>" class="button primary">Book a demo call</a>
          <a href="<?php echo esc_url(home_url('/work-with-me/')); ?>" class="button ghost">Full pricing breakdown</a>
        </div>
      </div>
    </div>
  </section>

</main>

<?php get_footer(); ?>
