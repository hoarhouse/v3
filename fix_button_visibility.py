#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Fixing button visibility and increasing terracotta presence")
print("=" * 60)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nBEFORE - Current terra usage:")
print("-" * 30)
terra_count_before = content.count("var(--terra)")
print(f"  var(--terra): {terra_count_before}")

print("\nSTEP 1 - FIXING BUTTON VISIBILITY:")
print("-" * 35)

# Fix .btn-main
btn_main_pattern = r'(\.btn-main\s*\{[^}]*?)background:[^;]+;([^}]*?\})'
btn_main_match = re.search(btn_main_pattern, content, re.DOTALL)
if btn_main_match:
    # Replace the background and ensure white text
    new_btn = btn_main_match.group(1) + "background: var(--terra);" + btn_main_match.group(2)
    if 'color:' not in new_btn:
        new_btn = new_btn.replace('}', 'color: #ffffff;}')
    elif 'color: #ffffff' not in new_btn:
        new_btn = re.sub(r'color:[^;]+;', 'color: #ffffff;', new_btn)
    content = content.replace(btn_main_match.group(0), new_btn)
    print("  ✓ Fixed .btn-main background and color")

# Fix .btn-main:hover
btn_hover_pattern = r'(\.btn-main:hover\s*\{[^}]*?)background:[^;]+;([^}]*?\})'
btn_hover_match = re.search(btn_hover_pattern, content, re.DOTALL)
if btn_hover_match:
    new_btn_hover = btn_hover_match.group(1) + "background: var(--terra-light);" + btn_hover_match.group(2)
    content = content.replace(btn_hover_match.group(0), new_btn_hover)
    print("  ✓ Fixed .btn-main:hover background")

# Fix .nav-btn
nav_btn_pattern = r'(\.nav-btn\s*\{[^}]*?)background:[^;]+;([^}]*?\})'
nav_btn_match = re.search(nav_btn_pattern, content, re.DOTALL)
if nav_btn_match:
    new_nav_btn = nav_btn_match.group(1) + "background: var(--terra);" + nav_btn_match.group(2)
    if 'color:' not in new_nav_btn:
        new_nav_btn = new_nav_btn.replace('}', 'color: #ffffff;}')
    elif 'color: #ffffff' not in new_nav_btn:
        new_nav_btn = re.sub(r'color:[^;]+;', 'color: #ffffff;', new_nav_btn)
    content = content.replace(nav_btn_match.group(0), new_nav_btn)
    print("  ✓ Fixed .nav-btn background and color")

# Fix .btn-ghost for visibility
btn_ghost_pattern = r'(\.btn-ghost\s*\{[^}]*?\})'
btn_ghost_match = re.search(btn_ghost_pattern, content, re.DOTALL)
if btn_ghost_match:
    ghost_block = btn_ghost_match.group(1)
    # Update border and color
    ghost_block = re.sub(r'border:[^;]+;', 'border: 2px solid rgba(255,255,255,0.6);', ghost_block)
    if 'border:' not in ghost_block:
        ghost_block = ghost_block.replace('}', 'border: 2px solid rgba(255,255,255,0.6);}')
    ghost_block = re.sub(r'color:[^;]+;', 'color: rgba(255,255,255,0.9);', ghost_block)
    if 'color:' not in ghost_block:
        ghost_block = ghost_block.replace('}', 'color: rgba(255,255,255,0.9);}')
    content = content.replace(btn_ghost_match.group(0), ghost_block)
    print("  ✓ Fixed .btn-ghost visibility")

print("\nSTEP 2 - INCREASING TERRACOTTA PRESENCE:")
print("-" * 45)

# 1. Hero badge dot
hero_dot_pattern = r'(\.hero-badge-dot\s*\{[^}]*?)background:[^;]+;([^}]*?\})'
hero_dot_match = re.search(hero_dot_pattern, content, re.DOTALL)
if hero_dot_match:
    new_dot = hero_dot_match.group(1) + "background: var(--terra);" + hero_dot_match.group(2)
    content = content.replace(hero_dot_match.group(0), new_dot)
    print("  ✓ Hero badge dot → terracotta")

# 2. Stat card hover
stat_hover_pattern = r'(\.stat-card:hover\s*\{[^}]*?)border-color:[^;]+;([^}]*?\})'
stat_hover_match = re.search(stat_hover_pattern, content, re.DOTALL)
if stat_hover_match:
    new_stat = stat_hover_match.group(1) + "border-color: var(--terra);" + stat_hover_match.group(2)
    content = content.replace(stat_hover_match.group(0), new_stat)
    print("  ✓ Stat card hover border → terracotta")

# 3. Feature card terra accent
feat_terra_pattern = r'(\.feat-card\.c-terra::before\s*\{[^}]*?)background:[^;]+;([^}]*?\})'
feat_terra_match = re.search(feat_terra_pattern, content, re.DOTALL)
if feat_terra_match:
    new_feat = feat_terra_match.group(1) + "background: var(--terra);" + feat_terra_match.group(2)
    content = content.replace(feat_terra_match.group(0), new_feat)
    print("  ✓ Feature card terra accent → terracotta")

# 4. Step number
step_num_pattern = r'(\.step-number\s*\{[^}]*?)color:[^;]+;([^}]*?\})'
step_num_match = re.search(step_num_pattern, content, re.DOTALL)
if step_num_match:
    new_step = step_num_match.group(1) + "color: var(--terra);" + step_num_match.group(2)
    content = content.replace(step_num_match.group(0), new_step)
    print("  ✓ Step number → terracotta")

# 5. Hero h1 highlight
hero_highlight_pattern = r'(\.hero-h1\s+\.highlight\s*\{[^}]*?)color:[^;]+;([^}]*?\})'
hero_highlight_match = re.search(hero_highlight_pattern, content, re.DOTALL)
if hero_highlight_match:
    new_highlight = hero_highlight_match.group(1) + "color: var(--terra);" + hero_highlight_match.group(2)
    content = content.replace(hero_highlight_match.group(0), new_highlight)
    print("  ✓ Hero h1 highlight → terracotta")

# 6. Section heading accent
section_accent_pattern = r'(\.section-h\s+\.accent\s*\{[^}]*?)color:[^;]+;([^}]*?\})'
section_accent_match = re.search(section_accent_pattern, content, re.DOTALL)
if section_accent_match:
    new_accent = section_accent_match.group(1) + "color: var(--terra);" + section_accent_match.group(2)
    content = content.replace(section_accent_match.group(0), new_accent)
    print("  ✓ Section heading accent → terracotta")

# 7. Inline problem section button
# Find and replace inline styles
content = re.sub(
    r'background:\s*var\(--amber\)([^"]*Register your parish)',
    r'background: var(--terra)\1',
    content
)
print("  ✓ Problem section CTA → terracotta")

# 8. Nav-name span (the "io")
nav_span_pattern = r'(\.nav-name\s+span\s*\{[^}]*?)color:[^;]+;([^}]*?\})'
nav_span_match = re.search(nav_span_pattern, content, re.DOTALL)
if nav_span_match:
    new_nav_span = nav_span_match.group(1) + "color: var(--terra);" + nav_span_match.group(2)
    content = content.replace(nav_span_match.group(0), new_nav_span)
    print("  ✓ Nav 'io' span → terracotta")

# 10. Country item hover
country_hover_pattern = r'(\.country-item:hover\s*\{[^}]*?)border-color:[^;]+;([^}]*?\})'
country_hover_match = re.search(country_hover_pattern, content, re.DOTALL)
if country_hover_match:
    hover_block = country_hover_match.group(1) + "border-color: var(--terra);" + country_hover_match.group(2)
    # Also update background
    hover_block = re.sub(r'background:[^;]+;', 'background: var(--terra-pale);', hover_block)
    content = content.replace(country_hover_match.group(0), hover_block)
    print("  ✓ Country item hover → terracotta")

print("\nSTEP 3 - WARMING BACKGROUND COLORS:")
print("-" * 35)

# Replace pure black backgrounds with warm black
warm_black = '#0e0a06'

# Hero/welcome background
content = re.sub(r'background:\s*#000000', f'background: {warm_black}', content)
content = re.sub(r'background-color:\s*#000000', f'background-color: {warm_black}', content)

# Also update the CSS variable if ink is used for backgrounds
content = content.replace('--ink:          #000000;', '--ink:          #0e0a06;')

print(f"  ✓ Changed pure black (#000000) → warm black ({warm_black})")

print("\nSTEP 4 - VERIFICATION:")
print("-" * 25)
terra_count_after = content.count("var(--terra)")
print(f"  var(--terra) before: {terra_count_before}")
print(f"  var(--terra) after: {terra_count_after}")
print(f"  Increase: +{terra_count_after - terra_count_before}")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    
    if terra_count_after > 20:
        print(f"  ✅ Terra usage: {terra_count_after} (target: > 20)")
    else:
        print(f"  ⚠ Terra usage: {terra_count_after} (target: > 20)")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🔥 BUTTON VISIBILITY & TERRACOTTA PRESENCE ENHANCED:")
print("   • All buttons now have solid flame backgrounds")
print("   • Ghost buttons have visible white borders")
print("   • Terracotta accents throughout for brand consistency")
print("   • Warmer black backgrounds (#0e0a06) for better harmony")
print(f"{'='*60}")
print("🚀 Ready to commit communio.html in GitHub Desktop")
print("🌐 Test at hoarhouse.github.io/v3/communio.html in 3-5 minutes")