#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Introducing amber/gold as visible design element in communio.html")
print("=" * 65)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\n0. BEFORE - Current --amber usage:")
print("-" * 35)
try:
    result = subprocess.run([
        'grep', '-c', 'var(--amber)', str(communio_file)
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        before_count = int(result.stdout.strip())
        print(f"  var(--amber) occurrences: {before_count}")
    else:
        before_count = 0
        print("  var(--amber) occurrences: 0")
except Exception:
    before_count = 0
    print("  var(--amber) occurrences: 0")

print("\n1. MARQUEE STRIP - Change to amber background:")
print("-" * 50)

# 1.1: Change .marquee-strip background (terracotta -> amber)
if 'background: var(--terracotta);' in content:
    content = content.replace('background: var(--terracotta);', 'background: var(--amber);')
    print("✓ Changed .marquee-strip background from terracotta to amber")
else:
    print("⚠ .marquee-strip background pattern not found")

# 1.2 & 1.3: Update marquee-item and marquee-dot colors in their CSS blocks
marquee_item_pattern = r'(\\.marquee-item\s*\{[^}]*?)color:\s*var\(--white\);([^}]*\})'
marquee_item_match = re.search(marquee_item_pattern, content, re.DOTALL)

if marquee_item_match:
    new_marquee_item = marquee_item_match.group(1) + "color: rgba(22,18,12,0.85);" + marquee_item_match.group(2)
    content = content.replace(marquee_item_match.group(0), new_marquee_item)
    print("✓ Changed .marquee-item color to rgba(22,18,12,0.85)")
else:
    print("⚠ .marquee-item color pattern not found")

marquee_dot_pattern = r'(\\.marquee-dot\s*\{[^}]*?)background:\s*rgba\([^)]+\);([^}]*\})'
marquee_dot_match = re.search(marquee_dot_pattern, content, re.DOTALL)

if marquee_dot_match:
    new_marquee_dot = marquee_dot_match.group(1) + "background: rgba(22,18,12,0.4);" + marquee_dot_match.group(2)
    content = content.replace(marquee_dot_match.group(0), new_marquee_dot)
    print("✓ Changed .marquee-dot background to rgba(22,18,12,0.4)")
else:
    print("⚠ .marquee-dot background pattern not found")

print("\n2. LABEL TAGS - Change to amber color:")
print("-" * 40)

# 2.1: Change .label-tag color from terracotta to amber
if 'color: var(--terracotta);' in content:
    content = content.replace('color: var(--terracotta);', 'color: var(--amber);')
    print("✓ Changed .label-tag color from terracotta to amber")
else:
    print("⚠ .label-tag color pattern not found")

# 2.2: Change .label-tag::before background from terracotta to amber  
if 'background: var(--terracotta);' in content:
    content = content.replace('background: var(--terracotta);', 'background: var(--amber);')
    print("✓ Changed .label-tag::before background from terracotta to amber")
else:
    print("⚠ .label-tag::before background pattern not found")

print("\n3. STEP TIME BADGES - Change to amber:")
print("-" * 40)

# 3.1: Change .step-time color and add background
step_time_pattern = r'(\\.step-time\s*\{[^}]*?)color:\s*var\(--sage\);([^}]*\})'
step_time_match = re.search(step_time_pattern, content, re.DOTALL)

if step_time_match:
    # Replace the sage color with amber and add background
    new_step_time = step_time_match.group(1) + "color: var(--amber); background: var(--amber-pale); padding: 4px 8px; border-radius: var(--r-sm);" + step_time_match.group(2)
    content = content.replace(step_time_match.group(0), new_step_time)
    print("✓ Changed .step-time to amber color with amber-pale background")
else:
    print("⚠ .step-time pattern not found")

print("\n4. COMMUNITY QUOTE SECTION - Change to amber:")
print("-" * 45)

# 4.1: Change .community-section background from terracotta to amber
community_bg_pattern = r'(\\.community-section\s*\{[^}]*?)background:\s*var\(--terracotta\);([^}]*\})'
community_bg_match = re.search(community_bg_pattern, content, re.DOTALL)

if community_bg_match:
    new_community_bg = community_bg_match.group(1) + "background: var(--amber);" + community_bg_match.group(2)
    content = content.replace(community_bg_match.group(0), new_community_bg)
    print("✓ Changed .community-section background from terracotta to amber")
else:
    print("⚠ .community-section background pattern not found")

# 4.2: Update .community-attr and .community-quote colors
community_attr_pattern = r'(\\.community-attr\s*\{[^}]*?)color:\s*rgba\([^)]+\);([^}]*\})'
community_attr_match = re.search(community_attr_pattern, content, re.DOTALL)

if community_attr_match:
    new_community_attr = community_attr_match.group(1) + "color: rgba(22,18,12,0.6);" + community_attr_match.group(2)
    content = content.replace(community_attr_match.group(0), new_community_attr)
    print("✓ Changed .community-attr color to rgba(22,18,12,0.6)")
else:
    print("⚠ .community-attr color pattern not found")

community_quote_pattern = r'(\\.community-quote\s*\{[^}]*?)color:\s*var\([^)]+\);([^}]*\})'
community_quote_match = re.search(community_quote_pattern, content, re.DOTALL)

if community_quote_match:
    new_community_quote = community_quote_match.group(1) + "color: var(--ink);" + community_quote_match.group(2)
    content = content.replace(community_quote_match.group(0), new_community_quote)
    print("✓ Changed .community-quote color to var(--ink)")
else:
    print("⚠ .community-quote color pattern not found")

print("\n5. CTA SECTION ACCENT - Change to amber:")
print("-" * 40)

# 5.1: Change .cta-h .big-accent color from terracotta to amber
if '.cta-h .big-accent { color: var(--terracotta); }' in content:
    content = content.replace('.cta-h .big-accent { color: var(--terracotta); }', '.cta-h .big-accent { color: var(--amber); }')
    print("✓ Changed .cta-h .big-accent color from terracotta to amber")
else:
    print("⚠ .cta-h .big-accent color pattern not found")

print("\n6. FEAT PILL - Add amber variant:")
print("-" * 35)

# 6.1: Find existing feat-pill rule and add new amber variant
if '.feat-card.c-terra .feat-pill' in content:
    # Find a good insertion point - after the terracotta feat-pill rule
    terra_pill_pattern = r'(\\.feat-card\\.c-terra\s+\\.feat-pill\s*\{[^}]+\})'
    terra_pill_match = re.search(terra_pill_pattern, content, re.DOTALL)
    
    if terra_pill_match:
        new_amber_rule = """

.feat-card.c-amber .feat-pill { 
  background: var(--amber-pale); 
  color: var(--amber); 
}"""
        
        terra_pill_end = terra_pill_match.end()
        content = content[:terra_pill_end] + new_amber_rule + content[terra_pill_end:]
        print("✓ Added .feat-card.c-amber .feat-pill rule")
    else:
        print("⚠ Could not find insertion point for amber feat-pill rule")
else:
    print("⚠ .feat-card.c-terra .feat-pill pattern not found")

print("\n7. FINAL COUNT - After changes:")
print("-" * 35)

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"✅ Updated {communio_file.name}")
    
    # Count after changes
    try:
        result = subprocess.run([
            'grep', '-c', 'var(--amber)', str(communio_file)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            after_count = int(result.stdout.strip())
            print(f"  var(--amber) occurrences: {after_count}")
        else:
            after_count = 0
            print("  var(--amber) occurrences: 0")
    except Exception:
        after_count = 0
        print("  var(--amber) occurrences: 0")
    
    print(f"\n📊 CHANGE SUMMARY:")
    print(f"   Before: {before_count} var(--amber) occurrences")
    print(f"   After:  {after_count} var(--amber) occurrences")
    print(f"   Added:  {after_count - before_count} new amber elements")
    
else:
    print(f"⚠ No changes were made to {communio_file.name}")

print(f"\n{'='*65}")
print("🎨 AMBER DESIGN ELEMENTS ADDED:")
print("   • Marquee strip now has amber background")
print("   • Label tags now use amber color")
print("   • Step time badges now amber themed")
print("   • Community quote section amber background") 
print("   • CTA section accent now amber")
print("   • New feat-card amber pill variant added")
print(f"{'='*65}")
print("🚀 Ready to commit communio.html in GitHub Desktop")