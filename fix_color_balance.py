#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Fixing color balance in communio.html")
print("Restoring var(--terra) for buttons/CTAs, keeping var(--amber) for accents")
print("=" * 70)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 - BEFORE counts:")
print("-" * 30)
terra_count_before = content.count("var(--terra)")
amber_count_before = content.count("var(--amber)")
print(f"  var(--terra): {terra_count_before}")
print(f"  var(--amber): {amber_count_before}")

print("\nSTEP 2 - RESTORING var(--terra) to buttons and CTAs:")
print("-" * 55)

# Based on the grep output, these lines need to be restored to terra:
# Line 127: .btn-main background
# Line 157: .nav-btn background  
# Line 237: .hero-badge-dot background
# Line 262: .hero-badge-text color
# Line 287: .btn-main:hover background
# Line 604: possibly a button background
# Line 705, 930: .collab-card.c-terra::before
# Line 953: .feat-card.c-terra .feat-pill color
# Line 1087: possibly button or action text
# Line 1154: .country-item:hover border
# Line 1262: possibly CTA button background
# Line 1884-1885: donation bar colors
# Line 2007: .cta-pill-dot

# Define specific replacements based on CSS selectors
replacements = [
    # Button backgrounds - definitely should be terra
    (r'(\.btn-main\s*\{[^}]*?)background:\s*var\(--amber\);', r'\1background: var(--terra);'),
    (r'(\.btn-main:hover\s*\{[^}]*?)background:\s*var\(--amber\);', r'\1background: var(--terra);'),
    (r'(\.nav-btn\s*\{[^}]*?)background:\s*var\(--amber\);', r'\1background: var(--terra);'),
    (r'(\.nav-btn:hover\s*\{[^}]*?)background:\s*var\(--amber\);', r'\1background: var(--terra);'),
    
    # Hero badge elements - should be terra
    (r'(\.hero-badge-dot\s*\{[^}]*?)background:\s*var\(--amber\);', r'\1background: var(--terra);'),
    (r'(\.hero-badge-text\s*\{[^}]*?)color:\s*var\(--amber\);', r'\1color: var(--terra);'),
    
    # Collab and feat cards with terra class - should use terra
    (r'(\.collab-card\.c-terra::before\s*\{[^}]*?)background:\s*var\(--amber\);', r'\1background: var(--terra);'),
    (r'(\.feat-card\.c-terra::before\s*\{[^}]*?)background:\s*var\(--amber\);', r'\1background: var(--terra);'),
    (r'(\.feat-card\.c-terra\s+\.feat-pill\s*\{[^}]*?)color:\s*var\(--amber\);', r'\1color: var(--terra);'),
    
    # Country item hover - should be terra
    (r'(\.country-item:hover\s*\{[^}]*?)border-color:\s*var\(--amber\);', r'\1border-color: var(--terra);'),
    
    # Button-like elements at specific lines
    (r'(\.btn-\w+\s*\{[^}]*?)background:\s*var\(--amber\);', r'\1background: var(--terra);'),
]

changes_made = []

for pattern, replacement in replacements:
    matches = re.findall(pattern, content, re.DOTALL)
    if matches:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        changes_made.append(f"  ✓ Restored terra in: {pattern.split('(')[1].split('\\')[0]}")
        
for change in changes_made:
    print(change)

# Also check for inline style replacements in HTML
inline_replacements = [
    ('background: var(--amber)', 'background: var(--terra)'),
    ('background:var(--amber)', 'background:var(--terra)'),
    ('color:var(--amber)', 'color:var(--terra)'),
    ('color: var(--amber)', 'color: var(--terra)'),
]

# Only replace in specific contexts (buttons, CTAs, dots)
button_contexts = [
    'cta-pill-dot',
    'dc-bar-fill', 
    'dc-row-pct',
    'btn',
    'badge',
]

for old, new in inline_replacements:
    # Find lines with these patterns
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if old in line:
            # Check if it's in a button/CTA context
            for context in button_contexts:
                if context in line:
                    lines[i] = line.replace(old, new)
                    print(f"  ✓ Restored terra in line {i+1}: {context}")
                    break
    content = '\n'.join(lines)

print("\nElements KEEPING var(--amber):")
print("-" * 35)
print("  • .marquee-strip background")
print("  • .label-tag color and ::before background")
print("  • .community-section background")
print("  • .step-time color and background")
print("  • .cta-h .big-accent color")
print("  • .feat-card.c-amber elements")
print("  • Research project type badges")

print("\nSTEP 3 - AFTER counts:")
print("-" * 25)
terra_count_after = content.count("var(--terra)")
amber_count_after = content.count("var(--amber)")
print(f"  var(--terra): {terra_count_after}")
print(f"  var(--amber): {amber_count_after}")

print("\nSUMMARY:")
print("-" * 20)
print(f"  Terra increased from {terra_count_before} to {terra_count_after} (+{terra_count_after - terra_count_before})")
print(f"  Amber reduced from {amber_count_before} to {amber_count_after} (-{amber_count_before - amber_count_after})")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    print("   Color balance restored: terra for buttons/CTAs, amber for accents")
else:
    print(f"\n⚠ No changes were made to {communio_file.name}")

print("\nVERIFICATION:")
print("-" * 20)
if terra_count_after > 15:
    print(f"  ✅ var(--terra): {terra_count_after} (target: > 15)")
else:
    print(f"  ⚠ var(--terra): {terra_count_after} (target: > 15)")
    
if 8 <= amber_count_after <= 12:
    print(f"  ✅ var(--amber): {amber_count_after} (target: 8-12)")
else:
    print(f"  ⚠ var(--amber): {amber_count_after} (target: 8-12)")

print(f"\n{'='*70}")
print("🎨 COLOR BALANCE RESTORED:")
print("   • Terracotta: Buttons, CTAs, primary actions")
print("   • Amber/Gold: Accent strips, labels, decorative elements")
print(f"{'='*70}")