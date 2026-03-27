#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing communio-dashboard.html styling issues")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')

# Store original content for comparison
original_content = content

print("\nISSUE 1: Fixing welcome screen centering")
print("-" * 40)

# Find and update .wl class to ensure centering
# Look for .wl { pattern and add margin auto if not present
wl_pattern = r'\.wl\s*\{([^}]+)\}'
wl_match = re.search(wl_pattern, content)
if wl_match:
    wl_content = wl_match.group(1)
    if 'margin-left: auto' not in wl_content and 'margin-right: auto' not in wl_content:
        # Add margin auto properties
        new_wl_content = wl_content.rstrip() + '\n      margin-left: auto;\n      margin-right: auto;'
        content = content.replace(wl_match.group(0), f'.wl {{{new_wl_content}\n    }}')
        print("✓ Added margin-left: auto and margin-right: auto to .wl")
    else:
        print("- .wl already has margin auto")

# Find and update #v-welcome to ensure flex centering
vwelcome_pattern = r'#v-welcome\s*\{([^}]+)\}'
vwelcome_match = re.search(vwelcome_pattern, content)
if vwelcome_match:
    vw_content = vwelcome_match.group(1)
    needs_update = False
    
    if 'align-items: center' not in vw_content:
        vw_content = vw_content.rstrip() + '\n      align-items: center;'
        needs_update = True
        
    if 'justify-content: center' not in vw_content:
        vw_content = vw_content.rstrip() + '\n      justify-content: center;'
        needs_update = True
    
    if needs_update:
        content = content.replace(vwelcome_match.group(0), f'#v-welcome {{{vw_content}\n    }}')
        print("✓ Added flex centering to #v-welcome")
    else:
        print("- #v-welcome already has centering")

print("\nISSUE 2: Reducing border-radius values")
print("-" * 40)

# Replace CSS variable values
replacements = [
    ('--r-md: 12px', '--r-md: 8px'),
    ('--r-lg: 20px', '--r-lg: 12px'),
    ('--r-xl: 28px', '--r-xl: 16px'),
]

for old, new in replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"✓ Replaced {old} with {new} ({count} occurrence{'s' if count != 1 else ''})")

# Replace hardcoded border-radius values
# Using exact replacements to avoid unintended changes
border_replacements = [
    ('border-radius:var(--r-xl) var(--r-xl) 0 0', 'border-radius:var(--r-lg) var(--r-lg) 0 0'),
    ('border-radius:14px', 'border-radius:8px'),
    ('border-radius:10px', 'border-radius:6px'),
    ('border-radius:13px', 'border-radius:8px'),
    ('border-radius:17px', 'border-radius:10px'),
    ('border-radius:18px', 'border-radius:10px'),
    ('border-radius:16px', 'border-radius:10px'),
    ('border-radius:20px', 'border-radius:12px'),
]

# Also check for spaced versions
border_replacements_spaced = [
    ('border-radius: var(--r-xl) var(--r-xl) 0 0', 'border-radius: var(--r-lg) var(--r-lg) 0 0'),
    ('border-radius: 14px', 'border-radius: 8px'),
    ('border-radius: 10px', 'border-radius: 6px'),
    ('border-radius: 13px', 'border-radius: 8px'),
    ('border-radius: 17px', 'border-radius: 10px'),
    ('border-radius: 18px', 'border-radius: 10px'),
    ('border-radius: 16px', 'border-radius: 10px'),
    ('border-radius: 20px', 'border-radius: 12px'),
]

all_border_replacements = border_replacements + border_replacements_spaced

for old, new in all_border_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"✓ Replaced {old} with {new} ({count} occurrence{'s' if count != 1 else ''})")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print("\n✅ File updated successfully!")
    
    # Count total changes
    print("\nSummary of changes:")
    print(f"- File size: {len(content)} bytes")
    print(f"- Total replacements made")
else:
    print("\n⚠ No changes were needed")

print("\nDone!")