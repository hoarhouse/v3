#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Removing remaining invite button")
print("=" * 35)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

# Find and remove the remaining invite button
remaining_button_pattern = r'<button onclick="openInvite\(\'home\'\)".*?</button>'
remaining_match = re.search(remaining_button_pattern, content, re.DOTALL)

if remaining_match:
    content = content.replace(remaining_match.group(0), '')
    print(f"  ✓ Removed remaining invite button ({len(remaining_match.group(0))} chars)")
    print(f"  Button was: {remaining_match.group(0)[:60]}...")
else:
    print("  ⚠ Remaining invite button not found")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
else:
    print(f"\n⚠ No changes were made")

print("🗑️ Remaining invite button removed")