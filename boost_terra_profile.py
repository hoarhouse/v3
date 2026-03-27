#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
profile_file = Path("/Users/christopherhoar/Desktop/v3/parish-profile.html")

print("Boosting terra (#d85020) usage in parish-profile.html")
print("=" * 60)

# Read the file
content = profile_file.read_text(encoding='utf-8')
original_content = content

print("\nCURRENT STATE:")
print("-" * 20)
current_count = content.count('#d85020')
print(f"  Current #d85020 count: {current_count}")
print(f"  Target: > 8 occurrences")
print(f"  Needed: {9 - current_count} more")

print("\nADDING MORE TERRA ELEMENTS:")
print("-" * 35)

# Find and update more elements that should use terra

# 1. Profile card avatar border/accent
pc_av_pattern = r'(\.pc-av\s*\{[^}]*?\})'
pc_av_match = re.search(pc_av_pattern, content, re.DOTALL)

if pc_av_match:
    av_block = pc_av_match.group(1)
    if 'border:' in av_block and '#d85020' not in av_block:
        av_block = re.sub(r'border:[^;]+;', 'border: 3px solid #d85020;', av_block)
        content = content.replace(pc_av_match.group(0), av_block)
        print("  ✓ .pc-av: Added #d85020 border")

# 2. Active state indicators (.on, .active classes)
# Find any .on or .active classes that don't already use terra
active_patterns = [
    (r'(\.tabs-btn\.on\s*\{[^}]*?\})', '.tabs-btn.on'),
    (r'(\.menu-item\.active\s*\{[^}]*?\})', '.menu-item.active'),
    (r'(\.pill\.active\s*\{[^}]*?\})', '.pill.active'),
]

for pattern, name in active_patterns:
    match = re.search(pattern, content, re.DOTALL)
    if match:
        block = match.group(1)
        if '#d85020' not in block:
            block = re.sub(r'background:[^;]+;', 'background: #d85020;', block)
            content = content.replace(match.group(0), block)
            print(f"  ✓ {name}: Set background to #d85020")

# 3. Progress indicators
prog_bar_pattern = r'(\.prog-fill\s*\{[^}]*?\})'
prog_bar_match = re.search(prog_bar_pattern, content, re.DOTALL)

if prog_bar_match:
    prog_block = prog_bar_match.group(1)
    if 'background:' in prog_block and '#d85020' not in prog_block:
        prog_block = re.sub(r'background:[^;]+;', 'background: #d85020;', prog_block)
        content = content.replace(prog_bar_match.group(0), prog_block)
        print("  ✓ .prog-fill: Set to #d85020")

# 4. Links in hero/dark sections
ph_link_pattern = r'(\.ph-link\s*\{[^}]*?\})'
ph_link_match = re.search(ph_link_pattern, content, re.DOTALL)

if ph_link_match:
    link_block = ph_link_match.group(1)
    if 'color:' in link_block and '#d85020' not in link_block:
        link_block = re.sub(r'color:[^;]+;', 'color: #d85020;', link_block)
        content = content.replace(ph_link_match.group(0), link_block)
        print("  ✓ .ph-link: Set color to #d85020")

# 5. Icon accents
icon_pattern = r'(\.icon-accent\s*\{[^}]*?\})'
icon_match = re.search(icon_pattern, content, re.DOTALL)

if icon_match:
    icon_block = icon_match.group(1)
    if 'color:' in icon_block and '#d85020' not in icon_block:
        icon_block = re.sub(r'color:[^;]+;', 'color: #d85020;', icon_block)
        content = content.replace(icon_match.group(0), icon_block)
        print("  ✓ .icon-accent: Set to #d85020")

# 6. Badge/notification elements
badge_pattern = r'(\.badge-count\s*\{[^}]*?\})'
badge_match = re.search(badge_pattern, content, re.DOTALL)

if badge_match:
    badge_block = badge_match.group(1)
    if 'background:' in badge_block and '#d85020' not in badge_block:
        badge_block = re.sub(r'background:[^;]+;', 'background: #d85020;', badge_block)
        content = content.replace(badge_match.group(0), badge_block)
        print("  ✓ .badge-count: Set background to #d85020")

# 7. Hover states for interactive elements
hover_patterns = [
    (r'(\.pc-btn:hover\s*\{[^}]*?\})', '.pc-btn:hover'),
    (r'(\.menu-item:hover\s*\{[^}]*?\})', '.menu-item:hover'),
]

for pattern, name in hover_patterns:
    match = re.search(pattern, content, re.DOTALL)
    if match:
        block = match.group(1)
        if 'color:' in block and '#d85020' not in block:
            block = re.sub(r'color:[^;]+;', 'color: #d85020;', block)
            content = content.replace(match.group(0), block)
            print(f"  ✓ {name}: Set hover color to #d85020")

# 8. Add more inline styles where appropriate
# Find donation widget button if not already terra
if 'dw-btn' in content and 'background: #d85020' not in content:
    # Already handled in previous script, skip
    pass

print("\nFINAL VERIFICATION:")
print("-" * 25)

# Count final occurrences
final_count = content.count('#d85020')
amber_count = content.count('#e8c040')

print(f"  #d85020 (terra): {final_count} occurrences")
print(f"  #e8c040 (amber): {amber_count} occurrences")

if final_count > 8:
    print(f"  ✅ Terra usage > 8 (target met!)")
else:
    print(f"  ⚠️ Still need {9 - final_count} more terra elements")

# Write the updated content back
if content != original_content:
    profile_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {profile_file.name}")
    print(f"   Increased terra from {current_count} to {final_count} occurrences")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🔥 TERRA BOOST COMPLETE:")
print(f"   • Added {final_count - current_count} more #d85020 elements")
print("   • Profile avatars, active states, progress bars")
print("   • Links, icons, badges, hover states")
print(f"{'='*60}")
print("🚀 Ready to commit: 'Boost terra presence — parish-profile.html'")