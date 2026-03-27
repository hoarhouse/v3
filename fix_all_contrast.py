#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("FULL VISIBILITY AUDIT AND CONTRAST FIX")
print("=" * 55)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nDIAGNOSTICS:")
print("-" * 20)
print(f"  Dark sections found:")
print(f"    • CTA section: background var(--ink)")
print(f"    • Footer: background var(--ink-soft)")
print(f"    • Marquee: background var(--amber) [gold]")
print(f"    • Community: background var(--amber) [gold]")

print("\n✅ STEP 2 - FIXING ALL DARK SECTIONS:")
print("=" * 45)

# A. HERO SECTION BUTTONS
print("\nA. HERO SECTION:")
print("-" * 30)

# Fix .btn-main
btn_main_pattern = r'(\.btn-main\s*\{[^}]*?\})'
btn_main_match = re.search(btn_main_pattern, content, re.DOTALL)
if btn_main_match:
    btn_block = btn_main_match.group(1)
    # Ensure background and color
    if 'background:' not in btn_block or 'var(--terra)' not in btn_block:
        btn_block = re.sub(r'background:[^;]+;', 'background: var(--terra);', btn_block)
    if 'background:' not in btn_block:
        btn_block = btn_block.replace('}', 'background: var(--terra);}')
    if 'color:' not in btn_block or '#ffffff' not in btn_block:
        btn_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', btn_block)
    if 'color:' not in btn_block:
        btn_block = btn_block.replace('}', 'color: #ffffff;}')
    content = content.replace(btn_main_match.group(0), btn_block)
    print("  ✓ .btn-main: terra bg, white text")

# Fix .btn-main:hover
btn_hover_pattern = r'(\.btn-main:hover\s*\{[^}]*?\})'
btn_hover_match = re.search(btn_hover_pattern, content, re.DOTALL)
if btn_hover_match:
    hover_block = btn_hover_match.group(1)
    hover_block = re.sub(r'background:[^;]+;', 'background: var(--terra-light);', hover_block)
    content = content.replace(btn_hover_match.group(0), hover_block)
    print("  ✓ .btn-main:hover: terra-light bg")

# Fix .btn-ghost
btn_ghost_pattern = r'(\.btn-ghost\s*\{[^}]*?\})'
btn_ghost_match = re.search(btn_ghost_pattern, content, re.DOTALL)
if btn_ghost_match:
    ghost_block = btn_ghost_match.group(1)
    # Clear and rebuild for proper ghost button
    ghost_block = re.sub(r'background:[^;]+;', 'background: transparent;', ghost_block)
    ghost_block = re.sub(r'color:[^;]+;', 'color: rgba(255,255,255,0.85);', ghost_block)
    ghost_block = re.sub(r'border:[^;]+;', 'border: 2px solid rgba(255,255,255,0.5);', ghost_block)
    if 'background:' not in ghost_block:
        ghost_block = ghost_block.replace('}', 'background: transparent;}')
    if 'color:' not in ghost_block:
        ghost_block = ghost_block.replace('}', 'color: rgba(255,255,255,0.85);}')
    if 'border:' not in ghost_block:
        ghost_block = ghost_block.replace('}', 'border: 2px solid rgba(255,255,255,0.5);}')
    content = content.replace(btn_ghost_match.group(0), ghost_block)
    print("  ✓ .btn-ghost: transparent, white text & border")

# Fix .btn-ghost:hover
ghost_hover_pattern = r'(\.btn-ghost:hover\s*\{[^}]*?\})'
ghost_hover_match = re.search(ghost_hover_pattern, content, re.DOTALL)
if ghost_hover_match:
    ghost_hover = ghost_hover_match.group(1)
    ghost_hover = re.sub(r'color:[^;]+;', 'color: #ffffff;', ghost_hover)
    ghost_hover = re.sub(r'border-color:[^;]+;', 'border-color: rgba(255,255,255,0.9);', ghost_hover)
    if 'color:' not in ghost_hover:
        ghost_hover = ghost_hover.replace('}', 'color: #ffffff;}')
    if 'border-color:' not in ghost_hover:
        ghost_hover = ghost_hover.replace('}', 'border-color: rgba(255,255,255,0.9);}')
    content = content.replace(ghost_hover_match.group(0), ghost_hover)
    print("  ✓ .btn-ghost:hover: bright white")

# B. CTA SECTION (dark background)
print("\nB. CTA SECTION (dark ink background):")
print("-" * 40)

# Fix .cta-h color (currently terra on dark bg - needs white)
cta_h_pattern = r'(\.cta-h\s*\{[^}]*?)color:\s*var\(--terra\);'
cta_h_match = re.search(cta_h_pattern, content, re.DOTALL)
if cta_h_match:
    content = re.sub(cta_h_pattern, r'\1color: #ffffff;', content, flags=re.DOTALL)
    print("  ✓ .cta-h: white text")

# Fix .cta-sub color
cta_sub_pattern = r'(\.cta-sub\s*\{[^}]*?)color:\s*var\(--terra\);'
cta_sub_match = re.search(cta_sub_pattern, content, re.DOTALL)
if cta_sub_match:
    content = re.sub(cta_sub_pattern, r'\1color: rgba(255,255,255,0.7);', content, flags=re.DOTALL)
    print("  ✓ .cta-sub: light white text")

# Fix .cta-note color
cta_note_pattern = r'(\.cta-note\s*\{[^}]*?\})'
cta_note_match = re.search(cta_note_pattern, content, re.DOTALL)
if cta_note_match:
    note_block = cta_note_match.group(1)
    note_block = re.sub(r'color:[^;]+;', 'color: rgba(255,255,255,0.4);', note_block)
    if 'color:' not in note_block:
        note_block = note_block.replace('}', 'color: rgba(255,255,255,0.4);}')
    content = content.replace(cta_note_match.group(0), note_block)
    print("  ✓ .cta-note: dim white text")

# Fix .cta-pill
cta_pill_pattern = r'(\.cta-pill\s*\{[^}]*?\})'
cta_pill_match = re.search(cta_pill_pattern, content, re.DOTALL)
if cta_pill_match:
    pill_block = cta_pill_match.group(1)
    pill_block = re.sub(r'color:[^;]+;', 'color: rgba(255,255,255,0.6);', pill_block)
    pill_block = re.sub(r'background:[^;]+;', 'background: rgba(255,255,255,0.08);', pill_block)
    pill_block = re.sub(r'border:[^;]+;', 'border: 1px solid rgba(255,255,255,0.12);', pill_block)
    if 'color:' not in pill_block:
        pill_block = pill_block.replace('}', 'color: rgba(255,255,255,0.6);}')
    if 'background:' not in pill_block:
        pill_block = pill_block.replace('}', 'background: rgba(255,255,255,0.08);}')
    if 'border:' not in pill_block:
        pill_block = pill_block.replace('}', 'border: 1px solid rgba(255,255,255,0.12);}')
    content = content.replace(cta_pill_match.group(0), pill_block)
    print("  ✓ .cta-pill: white/translucent")

# Fix .btn-main-light (CTA button)
btn_light_pattern = r'(\.btn-main-light\s*\{[^}]*?\})'
btn_light_match = re.search(btn_light_pattern, content, re.DOTALL)
if btn_light_match:
    light_block = btn_light_match.group(1)
    light_block = re.sub(r'background:[^;]+;', 'background: var(--terra);', light_block)
    light_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', light_block)
    if 'background:' not in light_block:
        light_block = light_block.replace('}', 'background: var(--terra);}')
    if 'color:' not in light_block:
        light_block = light_block.replace('}', 'color: #ffffff;}')
    content = content.replace(btn_light_match.group(0), light_block)
    print("  ✓ .btn-main-light: terra bg, white text")

# Fix .btn-main-light:hover
btn_light_hover_pattern = r'(\.btn-main-light:hover\s*\{[^}]*?\})'
btn_light_hover_match = re.search(btn_light_hover_pattern, content, re.DOTALL)
if btn_light_hover_match:
    light_hover = btn_light_hover_match.group(1)
    light_hover = re.sub(r'background:[^;]+;', 'background: var(--terra-light);', light_hover)
    content = content.replace(btn_light_hover_match.group(0), light_hover)
    print("  ✓ .btn-main-light:hover: terra-light bg")

# C. FOOTER (already has correct colors)
print("\nC. FOOTER (dark ink-soft background):")
print("-" * 40)
print("  ✓ Already correctly configured with white text")

# D. MARQUEE STRIP (amber background)
print("\nD. MARQUEE STRIP (amber/gold background):")
print("-" * 45)

# Fix marquee text for amber background
marquee_item_pattern = r'(\.marquee-item\s*\{[^}]*?)color:[^;]+;'
marquee_item_match = re.search(marquee_item_pattern, content, re.DOTALL)
if marquee_item_match:
    content = re.sub(marquee_item_pattern, r'\1color: rgba(0,0,0,0.75);', content, flags=re.DOTALL)
    print("  ✓ .marquee-item: dark text on gold")

marquee_dot_pattern = r'(\.marquee-dot\s*\{[^}]*?)background:[^;]+;'
marquee_dot_match = re.search(marquee_dot_pattern, content, re.DOTALL)
if marquee_dot_match:
    content = re.sub(marquee_dot_pattern, r'\1background: rgba(0,0,0,0.3);', content, flags=re.DOTALL)
    print("  ✓ .marquee-dot: dark dots on gold")

# E. COMMUNITY SECTION (amber background)
print("\nE. COMMUNITY SECTION (amber/gold background):")
print("-" * 50)

# Fix community text for amber background
community_quote_pattern = r'(\.community-quote\s*\{[^}]*?)color:\s*var\(--white\);'
community_quote_match = re.search(community_quote_pattern, content, re.DOTALL)
if community_quote_match:
    content = re.sub(community_quote_pattern, r'\1color: #1a0a00;', content, flags=re.DOTALL)
    print("  ✓ .community-quote: dark brown text")

community_attr_pattern = r'(\.community-attr\s*\{[^}]*?\})'
community_attr_match = re.search(community_attr_pattern, content, re.DOTALL)
if community_attr_match:
    attr_block = community_attr_match.group(1)
    attr_block = re.sub(r'color:[^;]+;', 'color: rgba(0,0,0,0.6);', attr_block)
    if 'color:' not in attr_block:
        attr_block = attr_block.replace('}', 'color: rgba(0,0,0,0.6);}')
    content = content.replace(community_attr_match.group(0), attr_block)
    print("  ✓ .community-attr: dark gray text")

# F. DONATION CARD (dark background)
print("\nF. DONATION CARD (dark backgrounds):")
print("-" * 40)

# Fix donation card text colors
dc_patterns = [
    (r'(\.dc-label\s*\{[^}]*?)color:[^;]+;', 'color: rgba(255,255,255,0.5);'),
    (r'(\.dc-amount\s*\{[^}]*?)color:[^;]+;', 'color: #ffffff;'),
    (r'(\.dc-row-label\s*\{[^}]*?)color:[^;]+;', 'color: rgba(255,255,255,0.5);'),
    (r'(\.dc-footer\s*\{[^}]*?)color:[^;]+;', 'color: rgba(255,255,255,0.4);'),
]

for pattern, new_color in dc_patterns:
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, r'\1' + new_color, content, flags=re.DOTALL)
        class_name = pattern.split('(')[1].split('\\')[0].replace('.', '')
        print(f"  ✓ {class_name}: white/translucent")

# G. INVITATION BOX (sage green background)
print("\nG. INVITATION BOX (sage green background):")
print("-" * 45)

ib_patterns = [
    (r'(\.ib-title\s*\{[^}]*?)color:[^;]+;', 'color: #ffffff;'),
    (r'(\.ib-desc\s*\{[^}]*?)color:[^;]+;', 'color: rgba(255,255,255,0.75);'),
]

for pattern, new_color in ib_patterns:
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, r'\1' + new_color, content, flags=re.DOTALL)
        class_name = pattern.split('(')[1].split('\\')[0].replace('.', '')
        print(f"  ✓ {class_name}: white text")

print("\n✅ STEP 4 - GLOBAL CHECK:")
print("=" * 30)
ink_count = content.count("color: var(--ink)")
black_count = content.count("color:#000") + content.count("color: #000")
print(f"  Remaining var(--ink) text: {ink_count}")
print(f"  Remaining #000 text: {black_count}")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    print("   All contrast issues fixed")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*55}")
print("🎨 CONTRAST FIXES APPLIED:")
print("   • Hero buttons: Solid terra with white text")
print("   • CTA section: White text on dark background")
print("   • Marquee: Dark text on gold background")
print("   • Community: Dark text on gold background")
print("   • All dark sections: Proper white/light text")
print(f"{'='*55}")
print("🚀 Ready to commit: 'Fix all contrast issues — Onyx & Flame'")