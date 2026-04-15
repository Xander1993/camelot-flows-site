<?php
/* Template Name: The Arsenal */
get_header(); ?>
<main class="relative pt-40 pb-20 px-6 min-h-screen bg-obsidian">
    <div class="absolute inset-0 grid-bg opacity-30"></div>
    <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-20">
            <span class="text-neon-cyan font-mono text-xs uppercase tracking-[0.3em] mb-4 block">// SHOWCASE</span>
            <h1 class="font-display text-5xl md:text-7xl font-black text-white uppercase tracking-tighter mb-6 text-glow">The <span class="text-neon-cyan text-glow-cyan">Arsenal</span></h1>
            <p class="text-slate-400 max-w-2xl mx-auto">Explore our collection of Awwwards-tier web designs, high-performance templates, and conversion-optimized digital experiences.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="glass-panel p-4 rounded-xl group hover:border-neon-cyan/50 transition-colors">
                <div class="aspect-video bg-black rounded-lg overflow-hidden mb-6 relative">
                    <div class="absolute w-full h-full bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <span class="absolute bottom-4 left-4 z-20 font-mono text-xs text-neon-cyan uppercase">E-Commerce</span>
                </div>
                <h3 class="font-display font-bold text-2xl text-white mb-2">NexStore Theme</h3>
                <p class="text-sm text-slate-400 font-body mb-4">Hyper-fast headless Shopify integration with WebGL 3D product previews.</p>
                <a href="#" class="text-xs font-mono text-white group-hover:text-neon-cyan transition-colors flex items-center gap-2">VIEW_PROJECT <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
            </div>
            <div class="glass-panel p-4 rounded-xl group hover:border-primary/50 transition-colors">
                <div class="aspect-video bg-black rounded-lg overflow-hidden mb-6 relative">
                    <div class="absolute w-full h-full bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <span class="absolute bottom-4 left-4 z-20 font-mono text-xs text-primary uppercase">SaaS Dashboard</span>
                </div>
                <h3 class="font-display font-bold text-2xl text-white mb-2">MetricFlow UI</h3>
                <p class="text-sm text-slate-400 font-body mb-4">A dark-mode obsessed dashboard layout featuring live GSAP data visualizations.</p>
                <a href="#" class="text-xs font-mono text-white group-hover:text-primary transition-colors flex items-center gap-2">VIEW_PROJECT <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
            </div>
            <div class="glass-panel p-4 rounded-xl group hover:border-emerald-400/50 transition-colors">
                <div class="aspect-video bg-black rounded-lg overflow-hidden mb-6 relative">
                    <div class="absolute w-full h-full bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                    <span class="absolute bottom-4 left-4 z-20 font-mono text-xs text-emerald-400 uppercase">Fintech</span>
                </div>
                <h3 class="font-display font-bold text-2xl text-white mb-2">Vault Pay</h3>
                <p class="text-sm text-slate-400 font-body mb-4">Secure, elegant, and blazing fast banking template with fluid micro-interactions.</p>
                <a href="#" class="text-xs font-mono text-white group-hover:text-emerald-400 transition-colors flex items-center gap-2">VIEW_PROJECT <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
            </div>
        </div>
    </div>
</main>
<?php get_footer(); ?>