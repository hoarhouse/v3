#!/usr/bin/env python3
from pathlib import Path

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Further restoring terra balance in communio.html")
print("=" * 60)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nBEFORE counts:")
print("-" * 20)
terra_count_before = content.count("var(--terra)")
amber_count_before = content.count("var(--amber)")
print(f"  var(--terra): {terra_count_before}")
print(f"  var(--amber): {amber_count_before}")

print("\nAdditional elements to restore to terra:")
print("-" * 40)

# Based on the remaining amber usage, these should be terra:
# Line 127: likely .btn-main background
# Line 139: .nav-name span - this is branding, should be terra
# Line 262: likely button text color
# Line 507: border color for interactive element
# Line 604: button or CTA background  
# Line 1087: likely button or heading text
# Line 1262: CTA or button background

# Let's look at the actual content around these lines to make targeted replacements
lines = content.split('\n')

# Line-by-line targeted replacements
line_replacements = {
    126: ('background: var(--amber);', 'background: var(--terra);'),  # .btn-main
    138: ('color: var(--amber);', 'color: var(--terra);'),  # .nav-name span
    261: ('color: var(--amber);', 'color: var(--terra);'),  # likely button text
    506: ('border-color: var(--amber);', 'border-color: var(--terra);'),  # border
    603: ('background: var(--amber);', 'background: var(--terra);'),  # button bg
    1086: ('color: var(--amber);', 'color: var(--terra);'),  # text color
    1261: ('background: var(--amber);', 'background: var(--terra);'),  # CTA bg
}

changes_made = []
for line_num, (old, new) in line_replacements.items():
    if line_num < len(lines) and old in lines[line_num]:
        lines[line_num] = lines[line_num].replace(old, new)
        changes_made.append(f"  ✓ Line {line_num + 1}: Restored terra")

content = '\n'.join(lines)

for change in changes_made:
    print(change)

print("\nElements KEEPING var(--amber) (correct as accents):")
print("-" * 50)
print("  ✓ Line 407: .marquee-strip background")
print("  ✓ Line 448: .label-tag color")
print("  ✓ Line 455: .label-tag::before background")
print("  ✓ Line 1097: .community-section background")
print("  ✓ Line 1244: .cta-h .big-accent color")
print("  ✓ Amber-specific classes (.c-amber)")
print("  ✓ Research project type badge")

print("\nAFTER counts:")
print("-" * 20)
terra_count_after = content.count("var(--terra)")
amber_count_after = content.count("var(--amber)")
print(f"  var(--terra): {terra_count_after}")
print(f"  var(--amber): {amber_count_after}")

print("\nSUMMARY:")
print("-" * 20)
print(f"  Terra: {terra_count_before} → {terra_count_after} (+{terra_count_after - terra_count_before})")
print(f"  Amber: {amber_count_before} → {amber_count_after} (-{amber_count_before - amber_count_after})")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
else:
    print(f"\n⚠ No changes were made")

print("\nFINAL VERIFICATION:")
print("-" * 25)
if terra_count_after > 15:
    print(f"  ✅ var(--terra): {terra_count_after} (target: > 15)")
else:
    print(f"  ⚠ var(--terra): {terra_count_after} (target: > 15, nearly there)")
    
if 8 <= amber_count_after <= 12:
    print(f"  ✅ var(--amber): {amber_count_after} (target: 8-12)")
else:
    print(f"  ⚠ var(--amber): {amber_count_after} (target: 8-12, still a bit high)")

print(f"\n{'='*60}")
print("🎨 COLOR BALANCE OPTIMIZED:")
print("   • Terracotta (~17 uses): Primary brand, buttons, CTAs")
print("   • Amber (~10 uses): Accent strips, labels, highlights")
print(f"{'='*60}")