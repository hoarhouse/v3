#!/usr/bin/env python3
import os
import re

v3_dir = "/Users/christopherhoar/Desktop/v3"
parish_file = os.path.join(v3_dir, "parish-profile.html")

print("Adding switcher functionality to parish-profile.html")
print("-" * 50)

# Read the file
with open(parish_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add switcher bar HTML after <body> tag
switcher_html = '''
  <div class="switcher">
    <button class="sw-btn on" onclick="sw('welcome',0)">Welcome</button>
    <button class="sw-btn" onclick="sw('dash',1)">Dashboard</button>
    <button class="sw-btn" onclick="sw('profile',2)">Public profile</button>
  </div>
'''

# Insert switcher after <body>
content = content.replace('<body>\n', '<body>\n' + switcher_html)
print("✓ Added switcher bar HTML")

# 2. Add switcher CSS styles (find where other styles are and add after NAV section)
switcher_css = '''
    /* ── SWITCHER ── */
    .switcher {
      position: fixed; bottom: 20px; left: 50%;
      transform: translateX(-50%); z-index: 900;
      background: var(--ink); border-radius: var(--r-pill);
      padding: 5px; display: flex; gap: 3px;
      box-shadow: var(--sh-md);
    }
    .sw-btn {
      font-family: var(--f-sans); font-size: 12px; font-weight: 600;
      color: rgba(255,253,249,0.4); background: none;
      border: none; border-radius: var(--r-pill);
      padding: 8px 16px; cursor: pointer;
      transition: all var(--ease); white-space: nowrap;
    }
    .sw-btn:hover { color: rgba(255,253,249,0.75); }
    .sw-btn.on { background: var(--terra); color: var(--white); }

'''

# Find the NAV section end and insert switcher CSS after it
nav_section_end = "    .nav-lbtn:hover { color: var(--ink); border-color: var(--ink); }"
content = content.replace(nav_section_end, nav_section_end + "\n" + switcher_css)
print("✓ Added switcher CSS styles")

# 3. Change default view from v-profile to v-welcome
content = content.replace('<div class="view on" id="v-profile">', '<div class="view" id="v-profile">')
content = content.replace('<div class="view" id="v-welcome">', '<div class="view on" id="v-welcome">')
print("✓ Set v-welcome as default view")

# 4. Add navigation buttons back
# Add Preview button to dashboard nav
old_nav_dash = '''      </a>
      <div class="nav-right">
        <div class="nav-parish">
          <div class="np-av">SM</div>
          <span class="np-name">St. Mary's</span>
        </div>
      </div>'''

new_nav_dash = '''      </a>
      <div class="nav-right">
        <div class="nav-parish">
          <div class="np-av">SM</div>
          <span class="np-name">St. Mary's</span>
        </div>
        <button class="nav-lbtn" onclick="sw('profile',2)">Preview →</button>
      </div>'''

content = content.replace(old_nav_dash, new_nav_dash)
print("✓ Added Preview button to dashboard nav")

# Add Dashboard button to profile nav
old_nav_profile = '''      </a>
      <div class="nav-right">
        <a href="communio-register.html" class="nav-lbtn">Register</a>
      </div>'''

new_nav_profile = '''      </a>
      <div class="nav-right">
        <button class="nav-lbtn" onclick="sw('dash',1)">← Dashboard</button>
      </div>'''

content = content.replace(old_nav_profile, new_nav_profile)
print("✓ Added Dashboard button to profile nav")

# Add Preview button to profile card
old_prof_card = '''          </div>
        </div>
        <div class="pc-body">'''

new_prof_card = '''          </div>
          <button class="pc-prev" onclick="sw('profile',2)">Preview public profile →</button>
        </div>
        <div class="pc-body">'''

content = content.replace(old_prof_card, new_prof_card)
print("✓ Added Preview button to profile card")

# 5. Update the "Set up your parish" button
content = content.replace(
    '<button class="btn btn-terra wl-cta">',
    '<button class="btn btn-terra wl-cta" onclick="sw(\'dash\',1)">'
)
print("✓ Updated 'Set up your parish' button")

# 6. Add JavaScript functions before closing </script> tag
# First, find and remove the existing pickA function closing to add our new functions
old_script_end = '''      document.getElementById('dw-cta').innerHTML=`Donate ${val} <svg viewBox="0 0 16 16" fill="none" width="14" height="14"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
    }
  </script>'''

new_script_end = '''      document.getElementById('dw-cta').innerHTML=`Donate ${val} <svg viewBox="0 0 16 16" fill="none" width="14" height="14"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
    }
    
    function sw(name,idx){
      document.querySelectorAll('.view').forEach(function(v){
        v.classList.remove('on');
        v.style.display='none';
      });
      var target=document.getElementById('v-'+name);
      target.classList.add('on');
      target.style.display='block';
      document.querySelectorAll('.sw-btn').forEach(function(b,i){
        b.classList.toggle('on',i===idx);
      });
      document.documentElement.scrollTop=0;
      document.body.scrollTop=0;
    }
    
    document.addEventListener('DOMContentLoaded',function(){
      document.querySelectorAll('.view').forEach(function(v){
        v.style.display='none';
      });
      var w=document.getElementById('v-welcome');
      w.style.display='block';
      w.classList.add('on');
    });
  </script>'''

content = content.replace(old_script_end, new_script_end)
print("✓ Added sw() function and DOMContentLoaded initializer")

# Write the updated content back
with open(parish_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nUpdate complete!")
print("\nVerifying changes:")
print(f"- Switcher elements: {content.count('switcher')} occurrences")
print(f"- sw-btn elements: {content.count('sw-btn')} occurrences")
print(f"- sw() function calls: {content.count('onclick=\"sw(')} occurrences")
print(f"- DOMContentLoaded: {content.count('DOMContentLoaded')} occurrence")