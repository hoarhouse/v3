#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Adding 'View demo' link to navigation in communio.html")
print("=" * 55)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\n1. FINDING .nav-links DIV:")
print("-" * 30)

# Find the .nav-links div and its closing tag
nav_links_pattern = r'(<div class="nav-links">.*?</div>)'
nav_links_match = re.search(nav_links_pattern, content, re.DOTALL)

if nav_links_match:
    nav_links_block = nav_links_match.group(0)
    print("✓ Found .nav-links div:")
    print(nav_links_block[:200] + "..." if len(nav_links_block) > 200 else nav_links_block)
    
    print("\n2. ADDING VIEW DEMO LINK:")
    print("-" * 30)
    
    # The demo link to insert
    demo_link = '''
    <a href="communio-dashboard.html" class="nav-link" style="color:var(--terracotta);font-weight:700;">
      View demo →
    </a>'''
    
    # Insert the demo link right after the closing </div> of .nav-links
    # Find the position right after the .nav-links closing tag
    nav_links_end = nav_links_match.end()
    
    # Insert the demo link
    content = content[:nav_links_end] + demo_link + content[nav_links_end:]
    
    print("✓ Inserted View demo link after .nav-links div")
    print("   Link: communio-dashboard.html")
    print("   Style: terracotta color, bold weight")
    print("   Text: 'View demo →'")
    
else:
    print("❌ .nav-links div not found!")

print("\n3. WRITING CHANGES:")
print("-" * 20)

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"✅ Updated {communio_file.name}")
else:
    print(f"⚠ No changes were made to {communio_file.name}")

print("\n4. VERIFICATION:")
print("-" * 15)
print("Run this command to verify:")
print("  grep -c 'communio-dashboard.html' communio.html")

print(f"\n{'='*55}")
print("🚀 Ready to commit communio.html in GitHub Desktop")
print("🌐 Test at hoarhouse.github.io/v3/communio.html in 3-5 minutes")