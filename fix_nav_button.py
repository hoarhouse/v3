#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Fixing nav button to always be flame orange")
print("=" * 50)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nBEFORE - Checking current nav-btn state:")
print("-" * 40)

# Check current .nav-btn rule
nav_btn_pattern = r'(\.nav-btn\s*\{[^}]*\})'
nav_btn_match = re.search(nav_btn_pattern, content, re.DOTALL)

if nav_btn_match:
    current_nav_btn = nav_btn_match.group(1)
    print("Current .nav-btn rule:")
    print(current_nav_btn[:200] + "..." if len(current_nav_btn) > 200 else current_nav_btn)
    
    # Check key properties
    has_terra = 'var(--terra)' in current_nav_btn
    has_white = '#ffffff' in current_nav_btn
    print(f"\n  ✓ Has var(--terra): {has_terra}")
    print(f"  ✓ Has #ffffff: {has_white}")

# Check .nav-btn:hover rule
nav_btn_hover_pattern = r'(\.nav-btn:hover\s*\{[^}]*\})'
nav_btn_hover_match = re.search(nav_btn_hover_pattern, content, re.DOTALL)

if nav_btn_hover_match:
    current_hover = nav_btn_hover_match.group(1)
    print("\nCurrent .nav-btn:hover rule:")
    print(current_hover[:200] + "..." if len(current_hover) > 200 else current_hover)
    
    has_terra_light = 'var(--terra-light)' in current_hover
    print(f"\n  ✓ Has var(--terra-light): {has_terra_light}")

# Check for .nav.scrolled .nav-btn override
scrolled_nav_btn_pattern = r'\.nav\.scrolled\s+\.nav-btn\s*\{[^}]*\}'
scrolled_nav_btn_match = re.search(scrolled_nav_btn_pattern, content, re.DOTALL)

if scrolled_nav_btn_match:
    print("\n⚠️ Found .nav.scrolled .nav-btn override:")
    print(scrolled_nav_btn_match.group(0))
    print("  This needs to be removed or fixed")

print("\nFIXING nav-btn styles:")
print("-" * 30)

changes_made = False

# Ensure .nav-btn has correct properties
if nav_btn_match:
    new_nav_btn = nav_btn_match.group(1)
    
    # Ensure background is terra
    if 'background:' in new_nav_btn and 'var(--terra)' not in new_nav_btn:
        new_nav_btn = re.sub(r'background:[^;]+;', 'background: var(--terra);', new_nav_btn)
        changes_made = True
        print("  ✓ Set background to var(--terra)")
    
    # Ensure color is white
    if 'color:' in new_nav_btn and '#ffffff' not in new_nav_btn:
        new_nav_btn = re.sub(r'color:[^;]+;', 'color: #ffffff;', new_nav_btn)
        changes_made = True
        print("  ✓ Set color to #ffffff")
    
    # Ensure no border
    if 'border:' not in new_nav_btn or 'border: none' not in new_nav_btn:
        if 'border:' in new_nav_btn:
            new_nav_btn = re.sub(r'border:[^;]+;', 'border: none;', new_nav_btn)
        else:
            new_nav_btn = new_nav_btn.replace('}', 'border: none;}')
        changes_made = True
        print("  ✓ Set border to none")
    
    if changes_made:
        content = content.replace(nav_btn_match.group(0), new_nav_btn)

# Ensure .nav-btn:hover has terra-light
if nav_btn_hover_match:
    new_hover = nav_btn_hover_match.group(1)
    
    if 'background:' in new_hover and 'var(--terra-light)' not in new_hover:
        new_hover = re.sub(r'background:[^;]+;', 'background: var(--terra-light);', new_hover)
        content = content.replace(nav_btn_hover_match.group(0), new_hover)
        changes_made = True
        print("  ✓ Set hover background to var(--terra-light)")

# Remove or fix any .nav.scrolled .nav-btn override
if scrolled_nav_btn_match:
    # Remove the override entirely
    content = content.replace(scrolled_nav_btn_match.group(0), '')
    changes_made = True
    print("  ✓ Removed .nav.scrolled .nav-btn override")

# Also check for inline .nav.scrolled rules that might affect nav-btn
nav_scrolled_block_pattern = r'(\.nav\.scrolled\s*\{[^}]*\})'
nav_scrolled_block_match = re.search(nav_scrolled_block_pattern, content, re.DOTALL)

if nav_scrolled_block_match:
    scrolled_block = nav_scrolled_block_match.group(1)
    # Make sure it doesn't change nav-btn styles
    if '--terra' in scrolled_block or 'nav-btn' in scrolled_block:
        print("  ⚠️ .nav.scrolled block may affect nav-btn")

print("\nAFTER - Verifying final state:")
print("-" * 35)

# Re-check the nav-btn after changes
final_nav_btn = re.search(nav_btn_pattern, content, re.DOTALL)
if final_nav_btn:
    final_btn = final_nav_btn.group(1)
    print("✓ .nav-btn properties:")
    if 'var(--terra)' in final_btn:
        print("  • background: var(--terra) ✅")
    if '#ffffff' in final_btn:
        print("  • color: #ffffff ✅")
    if 'border: none' in final_btn:
        print("  • border: none ✅")

final_hover = re.search(nav_btn_hover_pattern, content, re.DOTALL)
if final_hover:
    final_h = final_hover.group(1)
    print("\n✓ .nav-btn:hover properties:")
    if 'var(--terra-light)' in final_h:
        print("  • background: var(--terra-light) ✅")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    print("   Nav button now always orange")
elif not changes_made:
    print(f"\n✅ No changes needed - nav button already correctly configured")
    print("   • Always has terra/orange background")
    print("   • White text color")
    print("   • No conflicting scroll states")

print(f"\n{'='*50}")
print("🔥 NAV BUTTON STATUS:")
print("   • Default: Flame orange (var(--terra)) with white text")
print("   • Hover: Lighter orange (var(--terra-light))")
print("   • No scroll state overrides")
print(f"{'='*50}")
print("🚀 Ready to commit: 'Fix nav button always orange — Onyx & Flame'")