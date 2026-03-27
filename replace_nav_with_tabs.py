#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Replacing navigation with universal tab bar")
print("=" * 60)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 - ADD UNIVERSAL TAB BAR HTML:")
print("-" * 40)

# Find the closing </nav> tag for top-nav and add tab bar after it
tab_bar_html = '''
<nav class="tab-bar" id="tab-bar">
  <div class="tab-bar-inner">
    <button class="tab-item" id="tab-setup" onclick="go('setup')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="2" y="2" width="12" height="12" rx="1.5" stroke="currentColor" stroke-width="1.4"/><path d="M5 8h6M5 5.5h4M5 10.5h3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <span>Setup</span>
    </button>
    <button class="tab-item" id="tab-home" onclick="go('app','home')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2 7l6-5 6 5v7H10V9H6v5H2V7z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>
      <span>Home</span>
    </button>
    <button class="tab-item" id="tab-messages" onclick="go('app','messages')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2 3h12a1 1 0 011 1v7a1 1 0 01-1 1H4l-3 2V4a1 1 0 011-1z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>
      <span>Messages</span>
      <span class="tab-badge">3</span>
    </button>
    <button class="tab-item" id="tab-network" onclick="go('app','network')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="1.4"/><path d="M2 8h12M8 2a10 10 0 000 12M8 2a10 10 0 010 12" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <span>Network</span>
    </button>
    <button class="tab-item" id="tab-projects" onclick="go('app','projects')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="1" y="3" width="14" height="3" rx="1" stroke="currentColor" stroke-width="1.4"/><rect x="1" y="8" width="8" height="5" rx="1" stroke="currentColor" stroke-width="1.4"/><rect x="11" y="8" width="4" height="5" rx="1" stroke="currentColor" stroke-width="1.4"/></svg>
      <span>Projects</span>
    </button>
    <button class="tab-item" id="tab-website" onclick="go('app','website')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="1" y="2" width="14" height="11" rx="1.5" stroke="currentColor" stroke-width="1.4"/><path d="M1 5.5h14" stroke="currentColor" stroke-width="1.4"/></svg>
      <span>Website</span>
    </button>
    <button class="tab-item" id="tab-donations" onclick="go('app','donations')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="1" y="4" width="14" height="9" rx="1.5" stroke="currentColor" stroke-width="1.4"/><path d="M1 7.5h14" stroke="currentColor" stroke-width="1.4"/></svg>
      <span>Donations</span>
    </button>
    <button class="tab-item" id="tab-settings" onclick="go('app','settings')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="2.5" stroke="currentColor" stroke-width="1.4"/><path d="M8 1v2M8 13v2M1 8h2M13 8h2M3.05 3.05l1.41 1.41M11.54 11.54l1.41 1.41M3.05 12.95l1.41-1.41M11.54 4.46l1.41-1.41" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <span>Settings</span>
    </button>
    <button class="tab-item" id="tab-public" onclick="go('public')">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="6" r="2.5" stroke="currentColor" stroke-width="1.4"/><path d="M2 14c0-3.31 2.69-6 6-6s6 2.69 6 6" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <span>Profile</span>
    </button>
  </div>
</nav>'''

# Find the closing </nav> tag and insert tab bar after it
nav_closing_pattern = r'(</nav>\s*\n)'
nav_match = re.search(nav_closing_pattern, content)

if nav_match:
    insert_pos = nav_match.end()
    content = content[:insert_pos] + tab_bar_html + content[insert_pos:]
    print("  ✓ Added universal tab bar HTML after top-nav")
else:
    print("  ⚠ Could not find </nav> closing tag")

print("\nSTEP 2 - ADD TAB BAR CSS:")
print("-" * 30)

tab_bar_css = '''
.tab-bar {
  position: fixed;
  top: 58px;
  left: 0;
  right: 0;
  z-index: 190;
  background: #000000;
  border-bottom: 2px solid #e8c040;
  overflow-x: auto;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}
.tab-bar::-webkit-scrollbar { display: none; }
.tab-bar.hidden { display: none; }
.tab-bar-inner {
  display: flex;
  min-width: max-content;
  padding: 0 12px;
}
.tab-item {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 11px 16px;
  font-family: var(--f-sans);
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,0.45);
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s ease;
  margin-bottom: -2px;
}
.tab-item:hover { color: rgba(255,255,255,0.8); }
.tab-item.active {
  color: #ffffff;
  border-bottom-color: #d85020;
}
.tab-item svg { flex-shrink: 0; }
.tab-badge {
  background: #d85020;
  color: #ffffff;
  font-size: 9px;
  font-weight: 800;
  border-radius: 100px;
  padding: 1px 6px;
  min-width: 16px;
  text-align: center;
}
'''

# Insert CSS after the top-nav rules
css_insert_pattern = r'(.notif-dot\{[^}]+\}\s*\n)'
css_match = re.search(css_insert_pattern, content, re.DOTALL)

if css_match:
    insert_pos = css_match.end()
    content = content[:insert_pos] + tab_bar_css + content[insert_pos:]
    print("  ✓ Added tab bar CSS after top-nav rules")
else:
    print("  ⚠ Could not find insertion point for CSS")

print("\nSTEP 3 - REMOVE OLD NAVIGATION SYSTEMS:")
print("-" * 40)

# Remove setup-strip div and contents
setup_strip_pattern = r'<div class="setup-strip">.*?</div>(?:\s*\n)?'
setup_matches = re.findall(setup_strip_pattern, content, re.DOTALL)
if setup_matches:
    content = re.sub(setup_strip_pattern, '', content, flags=re.DOTALL)
    print(f"  ✓ Removed setup-strip div ({len(setup_matches)} instances)")

# Remove sidebar div and all contents
sidebar_pattern = r'<div class="sidebar">.*?</div>(?:\s*\n)?'
sidebar_matches = re.findall(sidebar_pattern, content, re.DOTALL)
if sidebar_matches:
    content = re.sub(sidebar_pattern, '', content, flags=re.DOTALL)
    print(f"  ✓ Removed sidebar div ({len(sidebar_matches)} instances)")

# Remove sb-toggle button
sb_toggle_pattern = r'<button[^>]*class="sb-toggle"[^>]*>.*?</button>(?:\s*\n)?'
sb_toggle_matches = re.findall(sb_toggle_pattern, content, re.DOTALL)
if sb_toggle_matches:
    content = re.sub(sb_toggle_pattern, '', content, flags=re.DOTALL)
    print(f"  ✓ Removed sb-toggle button ({len(sb_toggle_matches)} instances)")

# Update .main-content CSS - change margin-left to 0
main_content_pattern = r'(\.main-content\{[^}]*?)margin-left:220px;([^}]*?\})'
main_content_match = re.search(main_content_pattern, content, re.DOTALL)

if main_content_match:
    new_main_content = main_content_match.group(1) + 'margin-left:0;' + main_content_match.group(2)
    content = content.replace(main_content_match.group(0), new_main_content)
    print("  ✓ Changed .main-content margin-left to 0")

# Change .main-content padding
main_content_padding_pattern = r'(\.main-content\{[^}]*?)padding:86px 24px 100px;([^}]*?\})'
main_content_padding_match = re.search(main_content_padding_pattern, content, re.DOTALL)

if main_content_padding_match:
    new_padding = main_content_padding_match.group(1) + 'padding:70px 24px 100px;' + main_content_padding_match.group(2)
    content = content.replace(main_content_padding_match.group(0), new_padding)
    print("  ✓ Changed .main-content padding-top to 70px")

print("\nSTEP 4 - ADD BODY PADDING FOR TAB BAR:")
print("-" * 40)

# Find and update .setup-body padding
setup_body_pattern = r'(\.setup-body\{[^}]*?)padding-top:[^;]+;([^}]*?\})'
setup_body_match = re.search(setup_body_pattern, content, re.DOTALL)

if setup_body_match:
    new_setup = setup_body_match.group(1) + 'padding-top:100px;' + setup_body_match.group(2)
    content = content.replace(setup_body_match.group(0), new_setup)
    print("  ✓ Changed .setup-body padding-top to 100px")
elif '.setup-body{' in content:
    # Add padding if doesn't exist
    setup_simple_pattern = r'(\.setup-body\{[^}]*?)(\})'
    setup_simple_match = re.search(setup_simple_pattern, content, re.DOTALL)
    if setup_simple_match:
        new_setup = setup_simple_match.group(1) + 'padding-top:100px;' + setup_simple_match.group(2)
        content = content.replace(setup_simple_match.group(0), new_setup)
        print("  ✓ Added padding-top:100px to .setup-body")

# Find and update .pub-hero padding
pub_hero_pattern = r'(\.pub-hero\{[^}]*?)padding:[^;]+;([^}]*?\})'
pub_hero_match = re.search(pub_hero_pattern, content, re.DOTALL)

if pub_hero_match:
    new_pub = pub_hero_match.group(1) + 'padding:74px 20px 0;' + pub_hero_match.group(2)
    content = content.replace(pub_hero_match.group(0), new_pub)
    print("  ✓ Changed .pub-hero padding to 74px 20px 0")

print("\nSTEP 5 - UPDATE JAVASCRIPT FUNCTIONS:")
print("-" * 40)

# Replace go() function
new_go_function = '''function go(viewName, appSection){
  document.querySelectorAll('.view, .app-view').forEach(function(v){
    v.classList.remove('on');
    v.style.display='none';
  });
  var tabBar = document.getElementById('tab-bar');
  var target;
  if(viewName==='app'){
    target=document.getElementById('v-app');
    target.style.display='flex';
    target.classList.add('on');
    if(appSection) navTo(appSection);
    tabBar.classList.remove('hidden');
  } else if(viewName==='welcome'){
    target=document.getElementById('v-welcome');
    target.style.display='block';
    target.classList.add('on');
    tabBar.classList.add('hidden');
  } else {
    target=document.getElementById('v-'+viewName);
    target.style.display='block';
    target.classList.add('on');
    tabBar.classList.remove('hidden');
  }
  updateTabBar(viewName, appSection);
  document.documentElement.scrollTop=0;
  document.body.scrollTop=0;
  var viewMap={welcome:0,setup:1,public:9};
  var appMap={home:2,messages:3,network:4,projects:5,website:6,donations:7,settings:8};
  var idx=(viewName==='app')?(appSection?appMap[appSection]:2):viewMap[viewName];
  document.querySelectorAll('.sw-btn').forEach(function(b,i){
    b.classList.toggle('on',i===idx);
  });
  if(viewName==='app'&&appSection==='home') setTimeout(buildMiniChart,50);
  if(viewName==='app'&&appSection==='donations') setTimeout(buildFullChart,50);
}

function updateTabBar(viewName, appSection){
  document.querySelectorAll('.tab-item').forEach(function(t){
    t.classList.remove('active');
  });
  if(viewName==='setup'){
    var t=document.getElementById('tab-setup');
    if(t) t.classList.add('active');
  } else if(viewName==='public'){
    var t=document.getElementById('tab-public');
    if(t) t.classList.add('active');
  } else if(viewName==='app' && appSection){
    var t=document.getElementById('tab-'+appSection);
    if(t) t.classList.add('active');
  }
}'''

# Find and replace the existing go() function
go_pattern = r'function go\([^}]+\{[^}]+\}'
old_go_match = re.search(go_pattern, content, re.DOTALL)

if old_go_match:
    # Find the complete function including nested braces
    start_pos = old_go_match.start()
    brace_count = 0
    pos = start_pos
    while pos < len(content):
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_pos = pos + 1
                break
        pos += 1
    
    if 'end_pos' in locals():
        content = content[:start_pos] + new_go_function + content[end_pos:]
        print("  ✓ Replaced go() function with tab bar management")
else:
    print("  ⚠ Could not find go() function to replace")

# Update navTo() function to include updateTabBar call
navto_pattern = r'(function navTo\([^}]+\{[^}]+\})'
navto_match = re.search(navto_pattern, content, re.DOTALL)

if navto_match:
    # Find the complete navTo function
    start_pos = navto_match.start()
    brace_count = 0
    pos = start_pos
    while pos < len(content):
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_pos = pos
                break
        pos += 1
    
    if 'end_pos' in locals():
        original_navto = content[start_pos:end_pos]
        # Add updateTabBar call before the closing brace
        new_navto = original_navto + "  updateTabBar('app', section);\n  if(section==='home') setTimeout(buildMiniChart,50);\n  if(section==='donations') setTimeout(buildFullChart,50);"
        content = content[:start_pos] + new_navto + content[end_pos:]
        print("  ✓ Updated navTo() function with updateTabBar call")

print("\nSTEP 6 - UPDATE DOMCONTENTLOADED:")
print("-" * 35)

# Replace DOMContentLoaded function
new_dom_function = '''document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.view,.app-view').forEach(function(v){
    v.style.display='none';
    v.classList.remove('on');
  });
  var welcome=document.getElementById('v-welcome');
  welcome.style.display='block';
  welcome.classList.add('on');
  document.getElementById('tab-bar').classList.add('hidden');
  document.querySelectorAll('.sw-btn')[0].classList.add('on');
});'''

dom_pattern = r'document\.addEventListener\(\'DOMContentLoaded\'[^}]+\}\);'
dom_match = re.search(dom_pattern, content, re.DOTALL)

if dom_match:
    # Find complete function with proper brace matching
    start_text = "document.addEventListener('DOMContentLoaded'"
    start_pos = content.find(start_text)
    if start_pos != -1:
        brace_count = 0
        pos = start_pos
        while pos < len(content):
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_pos = pos + 3  # Include '});'
                    break
            pos += 1
        
        if 'end_pos' in locals():
            content = content[:start_pos] + new_dom_function + content[end_pos:]
            print("  ✓ Updated DOMContentLoaded initialization")

print("\nSTEP 7 - REMOVE OLD SIDEBAR CSS:")
print("-" * 35)

# List of CSS classes to remove
css_classes_to_remove = [
    r'\.sidebar\s*\{[^}]+\}',
    r'\.sb-parish\s*\{[^}]+\}', 
    r'\.sb-nav\s*\{[^}]+\}',
    r'\.sb-section-lbl\s*\{[^}]+\}',
    r'\.sb-item\s*\{[^}]+\}',
    r'\.sb-item\.active\s*\{[^}]+\}',
    r'\.sb-badge\s*\{[^}]+\}',
    r'\.sb-bottom\s*\{[^}]+\}',
    r'\.sb-profile-link\s*\{[^}]+\}',
    r'\.sb-toggle\s*\{[^}]+\}',
    r'\.setup-strip\s*\{[^}]+\}',
    r'\.setup-inner\s*\{[^}]+\}',
    r'\.s-tab\s*\{[^}]+\}',
    r'\.s-num\s*\{[^}]+\}',
    r'\.s-name\s*\{[^}]+\}',
]

removed_count = 0
for pattern in css_classes_to_remove:
    matches = re.findall(pattern, content, re.DOTALL)
    if matches:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        removed_count += len(matches)

print(f"  ✓ Removed {removed_count} old CSS blocks")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Replaced navigation with universal tab bar")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🎯 NAVIGATION REPLACEMENT COMPLETE:")
print("   • Added universal tab bar for all views except welcome")
print("   • Removed sidebar and setup-strip navigation")
print("   • Updated CSS for proper tab bar positioning")
print("   • Updated JavaScript for tab management")
print(f"{'='*60}")
print("🚀 Ready to commit: 'Replace nav with universal tab bar'")