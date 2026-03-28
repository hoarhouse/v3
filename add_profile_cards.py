from pathlib import Path

base = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard')

# ── CHANGE 1: Add profile card to home.html dashboard ──
f = base / 'home.html'
h = f.read_text(encoding='utf-8')

profile_card = '''        <div class="qa-card" style="border-color:var(--terra);background:var(--terra-pale);">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <div style="width:40px;height:40px;border-radius:var(--r-lg);background:var(--terra);color:var(--white);font-size:14px;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0;">SM</div>
            <div>
              <div style="font-size:13px;font-weight:800;color:var(--ink);">St. Mary's Parish</div>
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

# Insert profile card as first item in qa-cards div
h = h.replace(
    '<div class="qa-cards">',
    '<div class="qa-cards">\n' + profile_card
)

f.write_text(h, encoding='utf-8')
print('home.html: profile card added')

# ── CHANGE 4: Add profile strip to network.html ──
f = base / 'network.html'
h = f.read_text(encoding='utf-8')

profile_strip = '''    <!-- Your profile strip -->
    <div style="background:var(--ink);border-radius:var(--r-xl);padding:16px 20px;margin-bottom:24px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
      <div style="display:flex;align-items:center;gap:10px;flex:1;min-width:200px;">
        <div style="width:42px;height:42px;border-radius:var(--r-lg);background:var(--terra);color:var(--white);font-size:14px;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0;">SM</div>
        <div>
          <div style="font-size:13px;font-weight:700;color:var(--white);margin-bottom:2px;">St. Mary's Parish — Your public profile</div>
          <div style="font-size:11px;color:rgba(255,255,255,0.4);">This is what other parishes see when they find you · 142 visitors this month</div>
        </div>
      </div>
      <a href="../parish/profile.html" class="btn btn-secondary btn-sm" style="background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.15);color:rgba(255,255,255,0.7);">View my profile →</a>
    </div>'''

# Insert after page-header div
h = h.replace(
    '    <!-- PHP: GET params',
    profile_strip + '\n    <!-- PHP: GET params'
)

f.write_text(h, encoding='utf-8')
print('network.html: profile strip added')

# Verify
for name in ['home.html', 'network.html']:
    content = (base / name).read_text(encoding='utf-8')
    print(f'{name}: profile card={("View my public profile" in content or "View my profile" in content)}')