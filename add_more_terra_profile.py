#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
profile_file = Path("/Users/christopherhoar/Desktop/v3/parish-profile.html")

print("Adding more terra (#d85020) to parish-profile.html")
print("=" * 60)

# Read the file
content = profile_file.read_text(encoding='utf-8')
original_content = content

print("\nCURRENT STATE:")
print("-" * 20)
current_count = content.count('#d85020')
print(f"  Current #d85020 count: {current_count}")
print(f"  Target: > 8 occurrences")

print("\nADDING TERRA TO MORE ELEMENTS:")
print("-" * 35)

changes = []

# 1. Update .nav-mark background from var(--terra) to hardcoded
if '.nav-mark { width: 32px; height: 32px; background: var(--terra);' in content:
    content = content.replace(
        '.nav-mark { width: 32px; height: 32px; background: var(--terra);',
        '.nav-mark { width: 32px; height: 32px; background: #d85020;'
    )
    changes.append("  ✓ .nav-mark: var(--terra) → #d85020")

# 2. Update .np-av background from var(--terra) to hardcoded  
if '.np-av { width: 24px; height: 24px; border-radius: 50%; background: var(--terra);' in content:
    content = content.replace(
        'background: var(--terra);',
        'background: #d85020;',
        1  # Only replace first occurrence (in .np-av)
    )
    changes.append("  ✓ .np-av: var(--terra) → #d85020")

# 3. Update .ph-av background from var(--terra) to hardcoded
if '.ph-av { width: 68px; height: 68px; border-radius: 17px; flex-shrink: 0; background: var(--terra);' in content:
    content = content.replace(
        '.ph-av { width: 68px; height: 68px; border-radius: 17px; flex-shrink: 0; background: var(--terra);',
        '.ph-av { width: 68px; height: 68px; border-radius: 17px; flex-shrink: 0; background: #d85020;'
    )
    changes.append("  ✓ .ph-av: var(--terra) → #d85020")

# 4. Update .ph-tab.on border-bottom-color
if '.ph-tab.on { color: var(--white); border-bottom-color: var(--terra); }' in content:
    content = content.replace(
        '.ph-tab.on { color: var(--white); border-bottom-color: var(--terra); }',
        '.ph-tab.on { color: var(--white); border-bottom-color: #d85020; }'
    )
    changes.append("  ✓ .ph-tab.on: border-bottom-color → #d85020")

# 5. Update .step-tab.active border-bottom-color
if '.step-tab.active { border-bottom-color: var(--terra); }' in content:
    content = content.replace(
        '.step-tab.active { border-bottom-color: var(--terra); }',
        '.step-tab.active { border-bottom-color: #d85020; }'
    )
    changes.append("  ✓ .step-tab.active: border-bottom-color → #d85020")

# 6. Update .nav-wordmark span color
if '.nav-wordmark span { color: var(--terra); }' in content:
    content = content.replace(
        '.nav-wordmark span { color: var(--terra); }',
        '.nav-wordmark span { color: #d85020; }'
    )
    changes.append("  ✓ .nav-wordmark span: var(--terra) → #d85020")

# 7. Update .wl-h1 em color from var(--terra-light) to hardcoded terra-light
if '.wl-h1 em { font-style: italic; font-family: var(--f-serif); font-weight: 400; color: var(--terra-light); }' in content:
    content = content.replace(
        'color: var(--terra-light);',
        'color: #f07040;'
    )
    changes.append("  ✓ .wl-h1 em: var(--terra-light) → #f07040")

# 8. Update .wl-city.you color from var(--terra-light) to hardcoded
if '.wl-city.you { color: var(--terra-light); font-weight: 700; }' in content:
    content = content.replace(
        '.wl-city.you { color: var(--terra-light); font-weight: 700; }',
        '.wl-city.you { color: #f07040; font-weight: 700; }'
    )
    changes.append("  ✓ .wl-city.you: var(--terra-light) → #f07040")

# 9. Update step.active background
if '.step-tab.active .step-num { border-color: var(--terra); background: var(--terra); color: var(--white); }' in content:
    content = content.replace(
        'border-color: var(--terra); background: var(--terra);',
        'border-color: #d85020; background: #d85020;'
    )
    changes.append("  ✓ .step-tab.active .step-num: hardcoded #d85020")

# 10. Add more terra to badge hover states
badge_hover_pattern = r'(\.badge:hover\s*\{[^}]*?\})'
badge_hover_match = re.search(badge_hover_pattern, content, re.DOTALL)

if badge_hover_match:
    badge_block = badge_hover_match.group(1)
    if 'border-color:' in badge_block and '#d85020' not in badge_block:
        new_block = re.sub(r'border-color:[^;]+;', 'border-color: #d85020;', badge_block)
        content = content.replace(badge_block, new_block)
        changes.append("  ✓ .badge:hover: border-color → #d85020")

# Print changes
for change in changes:
    print(change)

print("\nFINAL VERIFICATION:")
print("-" * 25)

# Count final occurrences
final_count = content.count('#d85020')
f07040_count = content.count('#f07040')

print(f"  #d85020 (terra): {final_count} occurrences")
print(f"  #f07040 (terra-light): {f07040_count} occurrences")

if final_count > 8:
    print(f"  ✅ Terra usage > 8 (target met!)")
else:
    print(f"  ⚠️ Still {9 - final_count} short of target")

# Write the updated content back
if content != original_content:
    profile_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {profile_file.name}")
    print(f"   Increased terra from {current_count} to {final_count} occurrences")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🔥 TERRA BOOST COMPLETE:")
print(f"   • Replaced {len(changes)} var(--terra) with #d85020")
print("   • Nav marks, avatars, tabs, badges")
print("   • Active states and accent elements")
print(f"{'='*60}")
print("🚀 Ready to commit: 'Hardcode more terra — parish-profile.html'")