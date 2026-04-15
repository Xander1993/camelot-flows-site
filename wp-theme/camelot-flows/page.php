<?php get_header(); ?>
<main class="relative pt-40 pb-20 px-6 min-h-screen flex flex-col items-center">
    <div class="absolute inset-0 bg-obsidian -z-20"></div>
    <div class="absolute inset-0 grid-bg opacity-30 -z-20"></div>
    
    <div class="max-w-4xl mx-auto w-full relative z-10 glass-panel p-8 md:p-16 rounded-2xl border-t border-white/10 shadow-neon">
        <h1 class="font-display text-4xl md:text-5xl font-black text-white uppercase tracking-tighter mb-8 text-glow">
            <?php the_title(); ?>
        </h1>
        <div class="h-1 w-20 bg-gradient-to-r from-primary to-transparent mb-12"></div>
        
        <div class="prose prose-invert prose-lg max-w-none font-body text-slate-300">
            <?php
            if ( have_posts() ) :
                while ( have_posts() ) : the_post();
                    the_content();
                endwhile;
            endif;
            ?>
        </div>
    </div>
</main>
<?php get_footer(); ?>