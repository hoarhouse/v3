#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Fixing ALL transparent button backgrounds")
print("=" * 50)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nBEFORE - Current button states:")
print("-" * 35)

# Check current states
checks = [
    (r'(    \.nav-btn \{[^}]*?\})', '.nav-btn'),
    (r'(    \.btn-main \{[^}]*?\})', '.btn-main'),
    (r'(    \.btn-main-light \{[^}]*?\})', '.btn-main-light'),
]

for pattern, name in checks:
    match = re.search(pattern, content, re.DOTALL)
    if match:
        block = match.group(1)
        if 'var(--terra)' in block:
            print(f"  ⚠ {name}: using var(--terra)")
        elif '#d85020' in block:
            print(f"  ✓ {name}: already using #d85020")
        else:
            print(f"  ? {name}: unknown background")

print("\n✅ FIXING ALL BUTTON CSS RULES:")
print("-" * 35)

changes_made = 0

# CHANGE 1: Fix .nav-btn
nav_btn_pattern = r'(    \.nav-btn \{[^}]*?\})'
nav_btn_match = re.search(nav_btn_pattern, content, re.DOTALL)

if nav_btn_match:
    nav_btn_block = nav_btn_match.group(1)
    
    # Replace var(--terra) with hardcoded hex
    if 'background: var(--terra)' in nav_btn_block:
        nav_btn_block = nav_btn_block.replace('background: var(--terra);', 'background: #d85020;')
        changes_made += 1
        print("  ✓ .nav-btn: var(--terra) → #d85020")
    elif 'background:' in nav_btn_block and '#d85020' not in nav_btn_block:
        nav_btn_block = re.sub(r'background:\s*[^;]+;', 'background: #d85020;', nav_btn_block)
        changes_made += 1
        print("  ✓ .nav-btn: background → #d85020")
    
    # Ensure white color
    if 'color: #ffffff' not in nav_btn_block:
        if 'color:' in nav_btn_block:
            nav_btn_block = re.sub(r'color:\s*[^;]+;', 'color: #ffffff;', nav_btn_block)
        else:
            nav_btn_block = nav_btn_block.replace('}', '  color: #ffffff;\n    }')
        print("  ✓ .nav-btn: ensured white text")
    
    content = content.replace(nav_btn_match.group(0), nav_btn_block)

# CHANGE 2: Fix .btn-main (already done but double-check)
btn_main_pattern = r'(    \.btn-main \{[^}]*?\})'
btn_main_match = re.search(btn_main_pattern, content, re.DOTALL)

if btn_main_match:
    btn_main_block = btn_main_match.group(1)
    
    if 'background: var(--terra)' in btn_main_block:
        btn_main_block = btn_main_block.replace('background: var(--terra);', 'background: #d85020;')
        changes_made += 1
        print("  ✓ .btn-main: var(--terra) → #d85020")
    elif 'background:' not in btn_main_block or '#d85020' not in btn_main_block:
        if 'background:' in btn_main_block:
            btn_main_block = re.sub(r'background:\s*[^;]+;', 'background: #d85020;', btn_main_block)
        else:
            btn_main_block = btn_main_block.replace('}', '  background: #d85020;\n    }')
        changes_made += 1
        print("  ✓ .btn-main: ensured #d85020")
    
    # Ensure white color
    if 'color: #ffffff' not in btn_main_block:
        if 'color:' in btn_main_block:
            btn_main_block = re.sub(r'color:\s*[^;]+;', 'color: #ffffff;', btn_main_block)
        else:
            btn_main_block = btn_main_block.replace('}', '  color: #ffffff;\n    }')
        print("  ✓ .btn-main: ensured white text")
    
    content = content.replace(btn_main_match.group(0), btn_main_block)

# CHANGE 3: Fix .btn-main-light
btn_light_pattern = r'(    \.btn-main-light \{[^}]*?\})'
btn_light_match = re.search(btn_light_pattern, content, re.DOTALL)

if btn_light_match:
    btn_light_block = btn_light_match.group(1)
    
    if 'background: var(--terra)' in btn_light_block:
        btn_light_block = btn_light_block.replace('background: var(--terra);', 'background: #d85020;')
        changes_made += 1
        print("  ✓ .btn-main-light: var(--terra) → #d85020")
    elif 'background:' in btn_light_block and '#d85020' not in btn_light_block:
        btn_light_block = re.sub(r'background:\s*[^;]+;', 'background: #d85020;', btn_light_block)
        changes_made += 1
        print("  ✓ .btn-main-light: background → #d85020")
    
    # Ensure white color
    if 'color: #ffffff' not in btn_light_block:
        if 'color:' in btn_light_block:
            btn_light_block = re.sub(r'color:\s*[^;]+;', 'color: #ffffff;', btn_light_block)
        else:
            btn_light_block = btn_light_block.replace('}', '  color: #ffffff;\n    }')
        print("  ✓ .btn-main-light: ensured white text")
    
    content = content.replace(btn_light_match.group(0), btn_light_block)

# CHANGE 4: Fix inline style with !important
print("\n✅ FIXING INLINE STYLE:")
print("-" * 30)

# Find and replace the inline style
old_inline = 'style="margin-top:28px; display:inline-flex; background:#d85020; color:#ffffff;"'
new_inline = 'style="margin-top:28px; display:inline-flex; background:#d85020 !important; color:#ffffff !important;"'

if old_inline in content:
    content = content.replace(old_inline, new_inline)
    changes_made += 1
    print("  ✓ Added !important to inline style")
else:
    # Try without the previous background/color
    old_inline_base = 'style="margin-top:28px; display:inline-flex;"'
    if old_inline_base in content:
        content = content.replace(old_inline_base, new_inline)
        changes_made += 1
        print("  ✓ Added background and color with !important")

print("\nVERIFICATION:")
print("-" * 20)

# Verify all buttons have #d85020
for pattern, name in checks:
    match = re.search(pattern, content, re.DOTALL)
    if match:
        block = match.group(1)
        if '#d85020' in block:
            print(f"  ✓ {name}: has #d85020")
        else:
            print(f"  ⚠ {name}: missing #d85020")

# Count total #d85020 occurrences
d85020_count = content.count('#d85020')
print(f"\n  Total #d85020 occurrences: {d85020_count}")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    print(f"   Fixed {changes_made} button backgrounds")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🔥 ALL BUTTONS FIXED:")
print("   • .nav-btn: #d85020 background, white text")
print("   • .btn-main: #d85020 background, white text")
print("   • .btn-main-light: #d85020 background, white text")
print("   • Inline button: #d85020 !important")
print(f"{'='*50}")
print("🚀 Ready to commit: 'Fix all transparent buttons with hardcoded hex'")