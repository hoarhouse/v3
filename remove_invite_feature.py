#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Removing invite parish feature entirely")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 - REMOVE INVITE MODAL HTML:")
print("-" * 40)

# Find and remove the invite modal block
modal_start_marker = "<!-- INVITE MODAL -->"
modal_end_marker = "<!-- DEMO SWITCHER -->"

modal_start = content.find(modal_start_marker)
if modal_start != -1:
    modal_end = content.find(modal_end_marker)
    if modal_end != -1:
        # Find the closing </div> before the demo switcher comment
        search_area = content[modal_start:modal_end]
        # Count divs to find the proper closing
        pos = len(search_area) - 1
        div_count = 0
        while pos >= 0:
            if search_area[pos-6:pos] == "</div>":
                div_count += 1
                if div_count == 1:  # First closing div going backwards
                    modal_actual_end = modal_start + pos
                    break
            pos -= 1
        
        if 'modal_actual_end' in locals():
            removed_content = content[modal_start:modal_actual_end]
            content = content[:modal_start] + content[modal_actual_end:]
            print(f"  ✓ Removed invite modal ({len(removed_content)} chars)")
        else:
            print("  ⚠ Could not find modal closing div")
    else:
        print("  ⚠ Could not find modal end marker")
else:
    print("  ⚠ Could not find modal start marker")

print("\nSTEP 2 - REMOVE SIDEBAR INVITE BUTTON:")
print("-" * 42)

# Find and remove the sidebar invite button
sidebar_button_pattern = r'<div class="sb-item" onclick="openInvite\(\'sidebar\'\)".*?</div>'
sidebar_match = re.search(sidebar_button_pattern, content, re.DOTALL)

if sidebar_match:
    content = content.replace(sidebar_match.group(0), '')
    print(f"  ✓ Removed sidebar invite button ({len(sidebar_match.group(0))} chars)")
else:
    print("  ⚠ Sidebar invite button not found")

print("\nSTEP 3 - REMOVE HOME DASHBOARD INVITE CARD:")
print("-" * 45)

# Find and remove the invite card from home dashboard
card_pattern = r'<div class="qa-card" style="background:var\(--terra\).*?Know a parish that should join\?.*?</div>'
card_match = re.search(card_pattern, content, re.DOTALL)

if card_match:
    content = content.replace(card_match.group(0), '')
    print(f"  ✓ Removed home invite card ({len(card_match.group(0))} chars)")
else:
    # Try alternative pattern
    alt_pattern = r'<div class="qa-card"[^>]*>.*?Know a parish that should join\?.*?</div>'
    alt_match = re.search(alt_pattern, content, re.DOTALL)
    if alt_match:
        content = content.replace(alt_match.group(0), '')
        print(f"  ✓ Removed home invite card (alt pattern, {len(alt_match.group(0))} chars)")
    else:
        print("  ⚠ Home invite card not found")

print("\nSTEP 4 - REMOVE NETWORK PAGE INVITE BUTTON:")
print("-" * 45)

# Find and remove the network invite button
network_button_pattern = r'<button class="btn-primary btn-sm" onclick="openInvite\(\'network\'\)".*?</button>'
network_match = re.search(network_button_pattern, content, re.DOTALL)

if network_match:
    content = content.replace(network_match.group(0), '')
    print(f"  ✓ Removed network invite button ({len(network_match.group(0))} chars)")
else:
    print("  ⚠ Network invite button not found")

# Replace the network header with simple version
print("  Simplifying network header...")
complex_header_pattern = r'<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:16px;">.*?</div>\s*</div>'
simple_header = '''<div style="margin-bottom:16px;">
        <div style="font-size:clamp(18px,4vw,24px);font-weight:800;color:var(--ink);letter-spacing:-0.025em;margin-bottom:3px;">Network</div>
        <div style="font-size:13px;color:var(--light);">4,847 verified parishes across 221 countries</div>
      </div>'''

header_match = re.search(complex_header_pattern, content, re.DOTALL)
if header_match:
    content = content.replace(header_match.group(0), simple_header)
    print("  ✓ Simplified network header")
else:
    print("  ⚠ Complex network header not found")

print("\nSTEP 5 - REMOVE INVITE JS FUNCTIONS:")
print("-" * 38)

# Find and remove invite JS functions
js_start_marker = "/* ── INVITE A PARISH"
js_end_marker = "/* ── SETTINGS TABS"

js_start = content.find(js_start_marker)
if js_start != -1:
    js_end = content.find(js_end_marker, js_start)
    if js_end != -1:
        removed_js = content[js_start:js_end]
        content = content[:js_start] + content[js_end:]
        print(f"  ✓ Removed invite JS functions ({len(removed_js)} chars)")
    else:
        print("  ⚠ Could not find JS end marker")
else:
    print("  ⚠ Could not find JS start marker")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Removed entire invite parish feature")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🗑️ INVITE FEATURE REMOVAL:")
print("   • Removed invite modal HTML")
print("   • Removed sidebar invite button")
print("   • Removed home dashboard invite card")
print("   • Removed network page invite button")
print("   • Removed all invite JS functions")
print("   • Simplified network header")
print(f"{'='*50}")
print("🔍 Ready for verification with grep and balance check")