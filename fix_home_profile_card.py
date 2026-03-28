from pathlib import Path

f = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/home.html')
h = f.read_text(encoding='utf-8')

# Check what's actually there
print('Has qa-cards:', '<div class="qa-cards">' in h)
print('Has View my public profile:', 'View my public profile' in h)

# The insert target
old = '<div class="qa-cards">'
new = '''<div class="qa-cards">
        <div class="qa-card" style="border-color:var(--terra);background:var(--terra-pale);">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <div style="width:40px;height:40px;border-radius:var(--r-lg);background:var(--terra);color:var(--white);font-size:14px;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0;">SM</div>
            <div>
              <div style="font-size:13px;font-weight:800;color:var(--ink);">St. Mary\'s Parish</div>
              <div style="font-size:11px;color:var(--light);">stmarysnyc.communio.org · 142 visitors this month</div>
            </div>
          </div>
          <div style="display:flex;gap:5px;flex-wrap:wrap;margin-bottom:12px;">
            <span class="tag tag-terra">Peace &amp; reconciliation</span>
            <span class="tag tag-terra">Ethical technology</span>
            <span class="tag tag-terra">Youth ministry</span>
          </div>
          <div style="font-size:12px;color:var(--mid);margin-bottom:12px;">6 sister parishes · 4 active projects · ✓ Verified by DCF</div>
          <a href="../parish/profile.html" class="btn btn-primary btn-sm">View my public profile →</a>
        </div>'''

if old in h:
    h = h.replace(old, new, 1)
    f.write_text(h, encoding='utf-8')
    print('Profile card inserted successfully')
else:
    print('Target not found - searching for alternatives...')
    # Find what's actually there
    idx = h.find('qa-card')
    print('qa-card context:', repr(h[max(0,idx-100):idx+50]))