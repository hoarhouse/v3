#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Final terracotta boost")
print("=" * 40)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nBEFORE:")
terra_count_before = content.count("var(--terra)")
print(f"  var(--terra): {terra_count_before}")

print("\nAdding final terra touches:")
print("-" * 30)

# Add a couple more strategic terra uses

# 1. Make the sage border on line 886 use terra instead for consistency
content = re.sub(
    r'border-color:\s*var\(--sage\);',
    'border-color: var(--terra);',
    content
)
print("  ✓ Border color → terracotta")

# 2. Add terra to any CTA or important links
# Find .cta-link or similar
content = re.sub(
    r'(\.cta[^{]*\{[^}]*?)color:[^;]+;',
    r'\1color: var(--terra);',
    content,
    flags=re.DOTALL
)

# 3. Add terra to focus outline for accessibility
if 'outline-color: var(--terra)' not in content:
    # Add focus styles with terra outline
    focus_style = """
    *:focus-visible {
      outline: 2px solid var(--terra);
      outline-offset: 2px;
    }"""
    # Insert after the :root block
    root_end = content.find(':root {')
    if root_end > 0:
        root_close = content.find('}', root_end)
        if root_close > 0:
            content = content[:root_close + 1] + focus_style + content[root_close + 1:]
            print("  ✓ Added terra focus outlines")

print("\nFINAL VERIFICATION:")
print("-" * 25)
terra_count_after = content.count("var(--terra)")
print(f"  var(--terra) before: {terra_count_before}")
print(f"  var(--terra) after: {terra_count_after}")
print(f"  Total increase: +{terra_count_after - terra_count_before}")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    
    if terra_count_after > 20:
        print(f"  ✅ Terra usage: {terra_count_after} (target: > 20) ✓")
    else:
        print(f"  ⚠ Terra usage: {terra_count_after} (target: > 20)")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*40}")
print("🔥 FINAL TERRA COUNT: " + str(terra_count_after))
print(f"{'='*40}")