<?php
/* Template Name: Merlin Protocol */
get_header(); ?>
<main class="relative pt-40 pb-20 px-6 min-h-screen bg-obsidian overflow-hidden">
    <div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-primary/10 blur-[150px] rounded-full pointer-events-none"></div>
    <div class="max-w-5xl mx-auto relative z-10 text-center">
        <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-primary/30 bg-primary/10 mb-8">
            <span class="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
            <span class="font-mono text-xs text-primary tracking-widest uppercase">AI_SALES_AGENT_v2.0</span>
        </div>
        <h1 class="font-display text-5xl md:text-8xl font-black text-white uppercase tracking-tighter mb-8 text-glow">The <span class="text-primary-glow">Merlin</span> Protocol</h1>
        <p class="text-lg text-slate-400 max-w-3xl mx-auto leading-relaxed mb-12">
            Imagine an employee who never sleeps, knows your entire product catalog by heart, and closes deals through WhatsApp and Web Chat simultaneously. Merlin is our flagship AI business automation engine.
        </p>
        <div class="glass-panel p-8 md:p-12 rounded-2xl border-t border-white/10 shadow-neon mb-16 text-left">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                <div>
                     <h3 class="font-mono font-bold text-primary mb-4 uppercase tracking-wider text-sm">// Capabilities</h3>
                     <ul class="space-y-4 text-slate-300">
                         <li class="flex items-start gap-3">
                             <span class="material-symbols-outlined text-primary">check_circle</span>
                             <span><strong>Natural Language Processing:</strong> Converses indistinguishably from a human agent.</span>
                         </li>
                         <li class="flex items-start gap-3">
                             <span class="material-symbols-outlined text-primary">check_circle</span>
                             <span><strong>Omni-Channel Sync:</strong> Deploys on WhatsApp, Telegram, Instagram, and Web.</span>
                         </li>
                         <li class="flex items-start gap-3">
                             <span class="material-symbols-outlined text-primary">check_circle</span>
                             <span><strong>CRM Auto-Population:</strong> Automatically logs leads and schedules directly into your calendar.</span>
                         </li>
                     </ul>
                </div>
                <div class="glass-panel p-6 rounded-lg bg-black/50 border border-primary/20 flex flex-col justify-center items-center text-center">
                    <span class="material-symbols-outlined text-5xl text-primary mb-4 animate-pulse">model_training</span>
                    <h4 class="font-display font-bold text-white text-xl mb-2">Ready to Deploy?</h4>
                    <p class="text-xs text-slate-500 font-mono mb-6">Integration takes less than 48 hours.</p>
                    <button class="bg-primary hover:bg-white text-white hover:text-black font-mono font-bold uppercase tracking-wider text-sm py-3 px-6 rounded transition-all">Summon Merlin</button>
                </div>
            </div>
        </div>
    </div>
</main>
<?php get_footer(); ?>