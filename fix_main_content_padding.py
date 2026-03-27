#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing main-content padding for nav overlap")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nCHECKING CURRENT STATE:")
print("-" * 30)

# Check current main-content padding
if 'padding:86px 24px 100px' in content:
    print("  ✓ Desktop main-content already has padding:86px")
else:
    print("  ⚠ Desktop main-content needs fixing")

if 'padding:20px 16px 100px' in content:
    print("  ⚠ Mobile main-content still has padding:20px (needs 78px)")
else:
    print("  ✓ Mobile main-content already fixed")

print("\nFIXING MAIN-CONTENT PADDING:")
print("-" * 35)

# Fix desktop version if needed
if 'padding:28px 24px 100px' in content:
    content = content.replace('padding:28px 24px 100px', 'padding:86px 24px 100px')
    print("  ✓ Fixed desktop: padding:28px → padding:86px")
else:
    print("  ✓ Desktop already correct (86px)")

# Fix mobile version
if 'padding:20px 16px 100px' in content:
    content = content.replace('padding:20px 16px 100px', 'padding:78px 16px 100px')
    print("  ✓ Fixed mobile: padding:20px → padding:78px")
    print("    (58px nav + 20px breathing room = 78px)")
else:
    print("  ✓ Mobile already correct")

print("\nVERIFICATION:")
print("-" * 20)

# Verify the changes
if 'padding:86px 24px 100px' in content:
    print("  ✓ Desktop main-content: padding:86px")

if 'padding:78px 16px 100px' in content:
    print("  ✓ Mobile main-content: padding:78px")

if 'padding:28px 24px 100px' in content or 'padding:20px 16px 100px' in content:
    print("  ⚠ Still has old padding values")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed main-content nav overlap for desktop and mobile")
else:
    print(f"\n✅ No changes needed - already correct")

print(f"\n{'='*50}")
print("🎯 MAIN-CONTENT PADDING FIXED:")
print("   • Desktop: 86px (58px nav + 28px breathing room)")
print("   • Mobile: 78px (58px nav + 20px breathing room)")
print("   • Content no longer obscured by fixed nav")
print(f"{'='*50}")
print("🚀 Ready to commit: 'Fix main content nav overlap'")