#!/usr/bin/env python3
from pathlib import Path

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing border-radius values in communio-dashboard.html")
print("=" * 60)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')

# Store original for comparison
original_content = content

# First, report circle avatars (50%) - DO NOT CHANGE
circle_count = content.count("border-radius:50%")
print(f"\n✓ Found {circle_count} border-radius:50% (circles/avatars) - keeping these")

# Define replacements in order
replacements = [
    # First handle the var() replacements
    ("border-radius:var(--r-xl) var(--r-xl) 0 0", "border-radius:var(--r-lg) var(--r-lg) 0 0"),
    
    # Without spaces after colon
    ("border-radius:20px", "border-radius:10px"),
    ("border-radius:18px", "border-radius:10px"),
    ("border-radius:17px", "border-radius:10px"),
    ("border-radius:16px", "border-radius:10px"),
    ("border-radius:14px", "border-radius:8px"),
    ("border-radius:13px", "border-radius:8px"),
    ("border-radius:12px", "border-radius:8px"),
    ("border-radius:11px", "border-radius:6px"),
    ("border-radius:10px", "border-radius:6px"),
    ("border-radius:9px", "border-radius:6px"),
    
    # With spaces after colon
    ("border-radius: 20px", "border-radius: 10px"),
    ("border-radius: 18px", "border-radius: 10px"),
    ("border-radius: 17px", "border-radius: 10px"),
    ("border-radius: 16px", "border-radius: 10px"),
    ("border-radius: 14px", "border-radius: 8px"),
    ("border-radius: 13px", "border-radius: 8px"),
    ("border-radius: 12px", "border-radius: 8px"),
    ("border-radius: 11px", "border-radius: 6px"),
    ("border-radius: 10px", "border-radius: 6px"),
    ("border-radius: 9px", "border-radius: 6px"),
]

print("\nApplying replacements:")
print("-" * 40)

total_replacements = 0
for old_val, new_val in replacements:
    count = content.count(old_val)
    if count > 0:
        content = content.replace(old_val, new_val)
        print(f"✓ Replaced '{old_val}' → '{new_val}' ({count} times)")
        total_replacements += count

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {total_replacements} border-radius values")
else:
    print("\n⚠ No changes were needed")

print("\n" + "=" * 60)
print("Verification: Checking all border-radius values")
print("-" * 40)

# Now grep for all border-radius to verify
import subprocess
result = subprocess.run(
    ['grep', '-n', 'border-radius', str(dashboard_file)],
    capture_output=True,
    text=True
)

# Parse and analyze the results
lines = result.stdout.strip().split('\n')
problematic = []

for line in lines:
    # Skip 50% (circles)
    if '50%' in line:
        continue
    # Skip CSS variables
    if 'var(--r-' in line:
        continue
    # Check for values larger than 10px
    import re
    matches = re.findall(r'border-radius:\s*(\d+)px', line)
    for match in matches:
        if int(match) > 10:
            problematic.append(line)
            break

if problematic:
    print("\n⚠️ FOUND PROBLEMATIC VALUES (> 10px):")
    for line in problematic[:10]:  # Show first 10
        print(line[:150])  # Truncate long lines
else:
    print("\n✅ All hardcoded border-radius values are ≤ 10px (or 50% for circles)")

print(f"\nTotal border-radius declarations: {len(lines)}")
print(f"Circle avatars (50%): {circle_count}")

# Count remaining px values
px_values = {}
for line in lines:
    matches = re.findall(r'border-radius:\s*(\d+)px', line)
    for match in matches:
        val = f"{match}px"
        px_values[val] = px_values.get(val, 0) + 1

if px_values:
    print("\nRemaining px values:")
    for val, count in sorted(px_values.items(), key=lambda x: int(x[0][:-2]), reverse=True):
        print(f"  {val}: {count} occurrences")

print("\nDone!")