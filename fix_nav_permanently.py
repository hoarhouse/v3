#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing navigation permanently - move to demo bar")
print("=" * 60)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 - REMOVE OLD SWITCHER DIV:")
print("-" * 40)

# Find and remove the switcher div
switcher_start = content.find('<div class="switcher">')
if switcher_start != -1:
    # Find the matching closing div by counting nested divs
    pos = switcher_start + len('<div class="switcher">')
    div_count = 1
    
    while pos < len(content) and div_count > 0:
        if content[pos:pos+4] == '<div':
            div_count += 1
        elif content[pos:pos+6] == '</div>':
            div_count -= 1
            if div_count == 0:
                switcher_end = pos + 6
                break
        pos += 1
    
    if 'switcher_end' in locals():
        switcher_content = content[switcher_start:switcher_end]
        content = content[:switcher_start] + content[switcher_end:]
        print(f"  ✓ Removed switcher div ({len(switcher_content)} chars)")
    else:
        print("  ⚠ Could not find switcher closing div")
else:
    print("  ⚠ Switcher div not found")

print("\nSTEP 2 - ADD DEMO BAR CSS:")
print("-" * 35)

demo_bar_css = '''.demo-bar{position:fixed;top:58px;left:0;right:0;z-index:190;background:#111;border-bottom:1px solid rgba(255,255,255,0.1);display:flex;overflow-x:auto;scrollbar-width:none;padding:0 8px;}
.demo-bar::-webkit-scrollbar{display:none;}
.db-btn{font-family:var(--f-sans);font-size:11px;font-weight:600;color:rgba(255,255,255,0.4);background:none;border:none;border-bottom:2px solid transparent;padding:8px 12px;cursor:pointer;white-space:nowrap;text-decoration:none;display:inline-block;transition:color .2s;flex-shrink:0;}
.db-btn:hover{color:rgba(255,255,255,0.8);}
.db-btn.on{color:#fff;border-bottom-color:#d85020;}
'''

# Find closing </style> tag and insert CSS before it
style_end = content.rfind('</style>')
if style_end != -1:
    content = content[:style_end] + demo_bar_css + content[style_end:]
    print("  ✓ Added demo bar CSS before </style>")
else:
    print("  ⚠ Could not find </style> tag")

print("\nSTEP 3 - ADD DEMO BAR HTML:")
print("-" * 35)

demo_bar_html = '''</nav>
<div class="demo-bar" id="demo-bar">
  <a class="db-btn on" onclick="go('welcome')">1 Welcome</a>
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

# Replace first occurrence of </nav>
first_nav_end = content.find('</nav>')
if first_nav_end != -1:
    content = content[:first_nav_end] + demo_bar_html + content[first_nav_end + 6:]
    print("  ✓ Added demo bar HTML after first </nav>")
else:
    print("  ⚠ Could not find </nav> tag")

print("\nSTEP 4 - FIX OFFSET FOR ALL VIEWS:")
print("-" * 40)

# Update padding-top and top values
replacements = [
    ("padding-top:58px", "padding-top:94px"),
    ("padding-top: 58px", "padding-top: 94px"),
    ("top:58px", "top:94px"),
    ("top: 58px", "top: 94px")
]

for old, new in replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✓ Replaced {old} → {new} ({count} times)")

print("\nSTEP 5 - FIX APOSTROPHES IN _buildPreview:")
print("-" * 45)

apostrophe_fixes = [
    ("I'd like", "I&#39;d like"),
    ("O'Brien", "O&#39;Brien"),
    ("St. Mary's", "St. Mary&#39;s"),
    ("you'll", "you&#39;ll"),
    ("You'll", "You&#39;ll"),
    ("they'll", "they&#39;ll"),
    ("parish's", "parish&#39;s")
]

for old, new in apostrophe_fixes:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✓ Fixed {old} → {new} ({count} times)")

print("\nSTEP 6 - UPDATE go() FUNCTION FOR DEMO BAR:")
print("-" * 45)

# Find the go() function and add demo bar update code
go_function_start = content.find('function go(')
if go_function_start != -1:
    # Find the end of the go function
    pos = go_function_start
    brace_count = 0
    found_first_brace = False
    
    while pos < len(content):
        if content[pos] == '{':
            brace_count += 1
            found_first_brace = True
        elif content[pos] == '}':
            brace_count -= 1
            if found_first_brace and brace_count == 0:
                go_function_end = pos
                break
        pos += 1
    
    if 'go_function_end' in locals():
        # Insert the demo bar update code before the closing brace
        demo_bar_update = '''  /* Update demo bar active state */
  var allBtns = document.querySelectorAll('.db-btn');
  var viewMap2 = {welcome:0,setup:1,public:9};
  var appMap2 = {home:2,messages:3,network:4,projects:5,website:6,donations:7,settings:8};
  var activeIdx = (viewName==='app')?(appSection?appMap2[appSection]:2):viewMap2[viewName];
  allBtns.forEach(function(b,i){ b.classList.toggle('on', i===activeIdx); });
'''
        
        content = content[:go_function_end] + demo_bar_update + content[go_function_end:]
        print("  ✓ Added demo bar update code to go() function")
    else:
        print("  ⚠ Could not find end of go() function")
else:
    print("  ⚠ Could not find go() function")

print("\nSTEP 7 - VERIFICATION:")
print("-" * 25)

# Count occurrences
demo_bar_count = content.count('demo-bar')
switcher_count = content.count('switcher')
apostrophe_count = content.count("I'd")

print(f"  demo-bar occurrences: {demo_bar_count} (should be > 3)")
print(f"  switcher occurrences: {switcher_count} (should be 0)")
print(f"  \"I'd\" occurrences: {apostrophe_count} (should be 0)")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Navigation permanently fixed with demo bar")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🎛️ NAVIGATION PERMANENTLY FIXED:")
print("   • Removed old switcher div")
print("   • Added demo bar with 10 buttons")
print("   • Updated all view offsets")
print("   • Fixed email apostrophes")
print("   • Enhanced go() function")
print(f"{'='*60}")
print("🚀 Ready to verify balance and commit: 'Move nav to demo bar - fix permanently'")