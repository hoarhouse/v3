#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Moving demo switcher to top bar and fixing email apostrophes")
print("=" * 70)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nCHANGE 1 - MOVE SWITCHER TO SECOND TOP BAR:")
print("-" * 50)

# STEP A - Remove existing .switcher div
switcher_pattern = r'<div class="switcher">.*?</div>'
switcher_match = re.search(switcher_pattern, content, re.DOTALL)

if switcher_match:
    print("  ✓ Found existing switcher div")
    content = re.sub(switcher_pattern, '', content, flags=re.DOTALL)
    print("  ✓ Removed existing switcher div")
else:
    print("  ⚠ Existing switcher div not found")

# STEP B - Add demo bar after top-nav closing tag
demo_bar_html = '''
<div class="demo-bar">
  <a class="db-btn" onclick="go('welcome')">1 Welcome</a>
  <a class="db-btn" onclick="go('setup')">2 Setup</a>
  <a class="db-btn" onclick="go('app','home')">3 Home</a>
  <a class="db-btn" onclick="go('app','messages')">4 Messages</a>
  <a class="db-btn" onclick="go('app','network')">5 Network</a>
  <a class="db-btn" onclick="go('app','projects')">6 Projects</a>
  <a class="db-btn" onclick="go('app','website')">7 Website</a>
  <a class="db-btn" onclick="go('app','donations')">8 Donations</a>
  <a class="db-btn" onclick="go('app','settings')">9 Settings</a>
  <a class="db-btn" onclick="go('public')">10 Profile</a>
</div>'''

# Find closing </nav> tag and add demo bar after it
nav_closing_pattern = r'(</nav>)'
if re.search(nav_closing_pattern, content):
    content = re.sub(nav_closing_pattern, r'\1' + demo_bar_html, content, count=1)
    print("  ✓ Added demo bar after top-nav")
else:
    print("  ⚠ Could not find </nav> tag")

# STEP C - Add CSS rules before closing </style> tag
demo_bar_css = '''
.demo-bar{position:fixed;top:58px;left:0;right:0;z-index:190;background:#111;border-bottom:1px solid rgba(255,255,255,0.1);display:flex;overflow-x:auto;scrollbar-width:none;padding:0 8px;}
.demo-bar::-webkit-scrollbar{display:none;}
.db-btn{font-family:var(--f-sans);font-size:11px;font-weight:600;color:rgba(255,255,255,0.4);background:none;border:none;border-bottom:2px solid transparent;padding:8px 12px;cursor:pointer;white-space:nowrap;text-decoration:none;transition:all .2s ease;margin-bottom:-1px;flex-shrink:0;}
.db-btn:hover{color:rgba(255,255,255,0.8);}
.db-btn.on{color:#ffffff;border-bottom-color:#d85020;}'''

# Find closing </style> tag and add CSS before it
style_closing_pattern = r'(</style>)'
if re.search(style_closing_pattern, content):
    content = re.sub(style_closing_pattern, demo_bar_css + r'\n\1', content)
    print("  ✓ Added demo bar CSS")
else:
    print("  ⚠ Could not find </style> tag")

# STEP D - Update padding-top and top values
print("  Updating view offsets for double nav bar...")

# Replace padding-top values
content = content.replace('padding-top:58px', 'padding-top:94px')
content = content.replace('padding-top: 58px', 'padding-top: 94px')
print("    ✓ Updated padding-top values")

# Replace top values (but be careful not to replace z-index values)
content = re.sub(r'\btop:58px\b', 'top:94px', content)
content = re.sub(r'\btop: 58px\b', 'top: 94px', content)
print("    ✓ Updated top positioning values")

print("\nCHANGE 2 - FIX EMAIL APOSTROPHE ISSUE:")
print("-" * 45)

# Find and fix apostrophes in email content
apostrophe_fixes = [
    ("I'd like to invite", "I&#39;d like to invite"),
    ("you'll", "you&#39;ll"),
    ("parish's", "parish&#39;s"),
    ("Fr. James O'Brien", "Fr. James O&#39;Brien"),
    ("St. Mary's Parish", "St. Mary&#39;s Parish")
]

fixes_made = 0
for old_text, new_text in apostrophe_fixes:
    if old_text in content:
        content = content.replace(old_text, new_text)
        fixes_made += 1
        print(f"  ✓ Fixed: {old_text} → {new_text}")

if fixes_made > 0:
    print(f"  ✅ Fixed {fixes_made} apostrophe issues in email content")
else:
    print("  ⚠ No apostrophe patterns found to fix")

print("\nVERIFICATION:")
print("-" * 20)

# Count elements
demo_bar_count = content.count('class="demo-bar"')
switcher_count = content.count('class="switcher"')
db_btn_count = content.count('db-btn')

print(f"  demo-bar classes: {demo_bar_count} (should be 1)")
print(f"  switcher classes: {switcher_count} (should be 0)")
print(f"  db-btn occurrences: {db_btn_count} (should be > 10)")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Moved switcher to top demo bar")
    print("   Fixed email apostrophe issues")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*70}")
print("🎛️ DEMO BAR IMPLEMENTATION:")
print("   • Removed bottom switcher")
print("   • Added top demo navigation bar") 
print("   • Updated all view offsets for double nav")
print("   • Fixed email template apostrophes")
print(f"{'='*70}")
print("🚀 Ready to verify and commit: 'Move demo switcher to top bar — fix nav'")