import os

path = 'c:/Users/user/Downloads/stitch_camelot_flows_homepage/wp-theme/camelot-flows/index.php'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<button class="bg-obsidian border border-neon-cyan/50 text-neon-cyan px-8 py-4 rounded text-xs font-bold font-mono uppercase tracking-[0.2em] hover:bg-neon-cyan hover:text-obsidian transition-colors shadow-[0_0_15px_rgba(0,242,255,0.2)]">',
    '<button onclick="window.location.href=\'<?php echo esc_url(site_url(\'/the-arsenal/\')); ?>\'" class="bg-obsidian border border-neon-cyan/50 text-neon-cyan px-8 py-4 rounded text-xs font-bold font-mono uppercase tracking-[0.2em] hover:bg-neon-cyan hover:text-obsidian transition-colors shadow-[0_0_15px_rgba(0,242,255,0.2)]">'
)

content = content.replace(
    '<button class="bg-obsidian border border-neon-purple/50 text-neon-purple px-8 py-4 rounded text-xs font-bold font-mono uppercase tracking-[0.2em] hover:bg-neon-purple hover:text-obsidian transition-colors shadow-[0_0_15px_rgba(191,0,255,0.2)]">',
    '<button onclick="window.location.href=\'<?php echo esc_url(site_url(\'/merlin-protocol/\')); ?>\'" class="bg-obsidian border border-neon-purple/50 text-neon-purple px-8 py-4 rounded text-xs font-bold font-mono uppercase tracking-[0.2em] hover:bg-neon-purple hover:text-obsidian transition-colors shadow-[0_0_15px_rgba(191,0,255,0.2)]">'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated theme index.php')
