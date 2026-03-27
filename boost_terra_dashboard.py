#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Boosting terra (#d85020) in communio-dashboard.html")
print("=" * 60)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nCURRENT STATE:")
print("-" * 20)
current_count = content.count('#d85020')
print(f"  Current #d85020 count: {current_count}")
print(f"  Target: > 15 occurrences")
print(f"  Needed: {16 - current_count} more")

print("\nADDING MORE TERRA ELEMENTS:")
print("-" * 35)

changes = []

# Replace var(--terra) with hardcoded #d85020 throughout
var_terra_replacements = [
    ('background:var(--terra)', 'background:#d85020'),
    ('background: var(--terra)', 'background: #d85020'),
    ('border-color:var(--terra)', 'border-color:#d85020'),
    ('border-color: var(--terra)', 'border-color: #d85020'),
    ('color:var(--terra)', 'color:#d85020'),
    ('color: var(--terra)', 'color: #d85020'),
]

for old, new in var_terra_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        changes.append(f"  ✓ Replaced {count}x: {old} → {new}")

# Fix specific elements that should use terra
# 1. Profile avatars
if '.ph-av{' in content:
    pattern = r'(\.ph-av\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match and '#d85020' not in match.group(1):
        block = match.group(1)
        block = re.sub(r'background:[^;]+;', 'background:#d85020;', block)
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .ph-av: Set background to #d85020")

# 2. Tab active states
if '.ph-tab.on{' in content:
    pattern = r'(\.ph-tab\.on\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match and '#d85020' not in match.group(1):
        block = match.group(1)
        block = re.sub(r'border-bottom-color:[^;]+;', 'border-bottom-color:#d85020;', block)
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .ph-tab.on: Set border to #d85020")

# 3. Step indicators
if '.step-tab.active{' in content:
    pattern = r'(\.step-tab\.active\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match and '#d85020' not in match.group(1):
        block = match.group(1)
        block = re.sub(r'border-bottom-color:[^;]+;', 'border-bottom-color:#d85020;', block)
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .step-tab.active: Set border to #d85020")

# 4. Add terra to .btn-main if exists
if '.btn-main{' in content:
    pattern = r'(\.btn-main\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match and '#d85020' not in match.group(1):
        block = match.group(1)
        block = re.sub(r'background:[^;]+;', 'background:#d85020;', block)
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .btn-main: Set background to #d85020")

# 5. Navigation link button
if '.nav-lbtn{' in content:
    pattern = r'(\.nav-lbtn\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match and '#d85020' not in match.group(1):
        block = match.group(1)
        block = re.sub(r'background:[^;]+;', 'background:#d85020;', block)
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .nav-lbtn: Set background to #d85020")

# 6. Card accent borders/titles
if '.card-title{' in content:
    pattern = r'(\.card-title\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match and '#d85020' not in match.group(1):
        block = match.group(1)
        if 'color:' in block:
            block = re.sub(r'color:[^;]+;', 'color:#d85020;', block)
        else:
            block = block.replace('}', 'color:#d85020;}')
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .card-title: Set color to #d85020")

# 7. Stats numbers
if '.stat-num{' in content:
    pattern = r'(\.stat-num\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match and '#d85020' not in match.group(1):
        block = match.group(1)
        if 'color:' in block:
            block = re.sub(r'color:[^;]+;', 'color:#d85020;', block)
        else:
            block = block.replace('}', 'color:#d85020;}')
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .stat-num: Set color to #d85020")

# 8. Icon accents
if '.icon-terra{' in content:
    pattern = r'(\.icon-terra\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        block = match.group(1)
        block = re.sub(r'color:[^;]+;', 'color:#d85020;', block)
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .icon-terra: Set color to #d85020")

# 9. Progress bars
if '.progress-fill{' in content:
    pattern = r'(\.progress-fill\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match and '#d85020' not in match.group(1):
        block = match.group(1)
        block = re.sub(r'background:[^;]+;', 'background:#d85020;', block)
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .progress-fill: Set background to #d85020")

# 10. Active menu items
if '.menu-active{' in content:
    pattern = r'(\.menu-active\{[^}]*?\})'
    match = re.search(pattern, content, re.DOTALL)
    if match and '#d85020' not in match.group(1):
        block = match.group(1)
        block = re.sub(r'color:[^;]+;', 'color:#d85020;', block)
        content = content.replace(match.group(0), block)
        changes.append("  ✓ .menu-active: Set color to #d85020")

# Print changes
for change in changes:
    print(change)

print("\nFINAL VERIFICATION:")
print("-" * 25)

# Count final occurrences
final_count = content.count('#d85020')
e8c040_count = content.count('#e8c040')

print(f"  #d85020 (terra): {final_count} occurrences")
print(f"  #e8c040 (amber): {e8c040_count} occurrences")

if final_count > 15:
    print(f"  ✅ Terra usage > 15 (target met!)")
else:
    print(f"  ⚠️ Still {16 - final_count} short of target")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print(f"   Increased terra from {current_count} to {final_count} occurrences")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🔥 TERRA BOOST COMPLETE:")
print(f"   • Replaced {len(changes)} elements with #d85020")
print("   • Avatars, tabs, buttons, icons, progress bars")
print("   • All var(--terra) replaced with hardcoded hex")
print(f"{'='*60}")
print("🚀 Ready to commit: 'Apply Onyx & Flame — communio-dashboard.html'")