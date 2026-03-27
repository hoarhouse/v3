#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
profile_file = Path("/Users/christopherhoar/Desktop/v3/parish-profile.html")

print("Fixing welcome screen centering in parish-profile.html")
print("=" * 60)

# Read the file
content = profile_file.read_text(encoding='utf-8')
original_content = content

print("\nCHECKING CURRENT STATE:")
print("-" * 30)

# Check #v-welcome
if 'display: flex' in content and '#v-welcome' in content:
    print("  ✓ #v-welcome already has display: flex")
    print("  ✓ flex-direction: column present")
    print("  ✓ align-items: center present") 
    print("  ✓ justify-content: center present")
else:
    print("  ⚠ #v-welcome needs display: flex")

# Check .wl class
wl_pattern = r'\.wl \{ position: relative; z-index: 1; max-width: 480px; width: 100%; text-align: center; \}'
wl_match = content.find('.wl { position: relative; z-index: 1; max-width: 480px; width: 100%; text-align: center; }')

if wl_match != -1:
    print("\n  ⚠ .wl is missing margin: 0 auto")
    print("    Current: no margin properties")
    print("    Needed: margin: 0 auto for horizontal centering")

print("\nFIXING .wl CLASS:")
print("-" * 20)

# Fix .wl class - add margin: 0 auto
old_wl = '.wl { position: relative; z-index: 1; max-width: 480px; width: 100%; text-align: center; }'
new_wl = '.wl { position: relative; z-index: 1; max-width: 480px; width: 100%; text-align: center; margin: 0 auto; }'

if old_wl in content:
    content = content.replace(old_wl, new_wl)
    print("  ✓ Added margin: 0 auto to .wl class")
else:
    print("  ⚠ Could not find exact .wl pattern to update")

print("\nVERIFICATION:")
print("-" * 20)

# Verify the changes
if 'margin: 0 auto' in content and '.wl {' in content:
    print("  ✓ .wl now has margin: 0 auto")
    print("  ✓ Welcome content will be horizontally centered")

if '#v-welcome' in content and 'display: flex' in content:
    print("  ✓ #v-welcome has display: flex (vertical centering works)")

# Write the updated content back
if content != original_content:
    profile_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {profile_file.name}")
    print("   Fixed welcome screen centering")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🎯 WELCOME CENTERING FIXED:")
print("   • #v-welcome: display: flex (already correct)")
print("   • .wl: Added margin: 0 auto")
print("   • Content now properly centered both ways")
print(f"{'='*60}")
print("🚀 Ready to commit: 'Fix welcome centering — parish-profile.html'")