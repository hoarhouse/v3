#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Fixing .btn-main transparent background issue")
print("=" * 50)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nBEFORE - Current .btn-main state:")
print("-" * 35)

# Find the exact .btn-main CSS rule (not hover, not variants)
btn_main_pattern = r'(    \.btn-main \{[^}]*?\})'
btn_main_match = re.search(btn_main_pattern, content, re.DOTALL)

if btn_main_match:
    current_btn = btn_main_match.group(1)
    print("Found .btn-main CSS rule:")
    
    # Check current background
    if 'background: var(--terra)' in current_btn:
        print("  ⚠ Currently using var(--terra) - needs hardcoded value")
    elif 'background:' in current_btn:
        bg_match = re.search(r'background:\s*([^;]+);', current_btn)
        if bg_match:
            print(f"  Current background: {bg_match.group(1)}")
    else:
        print("  ⚠ No background property found")

print("\n✅ FIXING .btn-main CSS:")
print("-" * 30)

changes_made = False

# Fix the .btn-main CSS rule
if btn_main_match:
    new_btn = btn_main_match.group(1)
    
    # Replace var(--terra) with hardcoded hex
    if 'background: var(--terra)' in new_btn:
        new_btn = new_btn.replace('background: var(--terra);', 'background: #d85020;')
        changes_made = True
        print("  ✓ Replaced var(--terra) → #d85020")
    elif 'background:' in new_btn:
        # Replace any existing background
        new_btn = re.sub(r'background:\s*[^;]+;', 'background: #d85020;', new_btn)
        changes_made = True
        print("  ✓ Set background to #d85020")
    else:
        # Add background if missing
        new_btn = new_btn.replace('}', '  background: #d85020;\n    }')
        changes_made = True
        print("  ✓ Added background: #d85020")
    
    # Ensure color is white
    if 'color: #ffffff' not in new_btn:
        if 'color:' in new_btn:
            new_btn = re.sub(r'color:\s*[^;]+;', 'color: #ffffff;', new_btn)
        else:
            new_btn = new_btn.replace('}', '  color: #ffffff;\n    }')
        changes_made = True
        print("  ✓ Ensured color: #ffffff")
    
    if changes_made:
        content = content.replace(btn_main_match.group(0), new_btn)

print("\n✅ FIXING inline style button:")
print("-" * 35)

# Fix the inline style button
inline_pattern = r'style="margin-top:28px; display:inline-flex;"'
if inline_pattern in content:
    new_inline = 'style="margin-top:28px; display:inline-flex; background:#d85020; color:#ffffff;"'
    content = content.replace(inline_pattern, new_inline)
    print("  ✓ Added background and color to inline style")
    changes_made = True
else:
    print("  ⚠ Inline style pattern not found")

print("\nVERIFICATION:")
print("-" * 20)

# Verify the changes
if changes_made:
    # Check .btn-main CSS
    new_btn_match = re.search(btn_main_pattern, content, re.DOTALL)
    if new_btn_match and '#d85020' in new_btn_match.group(1):
        print("  ✓ .btn-main has background: #d85020")
    
    # Check inline style
    if 'background:#d85020' in content and 'margin-top:28px' in content:
        print("  ✓ Inline button has background:#d85020")

# Count occurrences
d85020_count = content.count('#d85020')
print(f"\n  Total #d85020 occurrences: {d85020_count}")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    print("   Fixed transparent button backgrounds")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🔥 BUTTON FIX APPLIED:")
print("   • .btn-main: Hardcoded #d85020 background")
print("   • Inline button: Added background:#d85020")
print("   • Both have white text color")
print(f"{'='*50}")
print("🚀 Ready to commit: 'Fix btn-main transparent background'")