from pathlib import Path

css_path = Path('/Users/christopherhoar/Desktop/v3/communio/communio.css')
css = css_path.read_text(encoding='utf-8')

# Add nav pill styles — with two variants:
# .top-nav .nav-pill = dark dashboard version (already works)
# .nav .nav-pill = light profile page version
pill_styles = """
/* ── Nav Pill (shared across dashboard + profile) ── */
.nav-pill{display:flex;align-items:center;gap:8px;border-radius:20px;padding:4px 12px 4px 4px;text-decoration:none;transition:all .2s}
.nav-av{width:26px;height:26px;background:var(--terra);border-radius:50%;font-size:10px;font-weight:700;color:white;display:flex;align-items:center;justify-content:center;flex-shrink:0}
/* Dashboard version — dark nav */
.top-nav .nav-pill{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1)}
.top-nav .nav-pill:hover{background:rgba(255,255,255,.12)}
.top-nav .nav-pname{font-size:13px;font-weight:600;color:#fff}
/* Profile page version — light nav */
.nav .nav-pill{background:rgba(0,0,0,.05);border:1px solid rgba(0,0,0,.08)}
.nav .nav-pill:hover{background:rgba(0,0,0,.1)}
.nav .nav-pname{font-size:13px;font-weight:600;color:var(--ink)}
"""

css = css + pill_styles
css_path.write_text(css, encoding='utf-8')
print("Done. nav-pill rules added:", css.count('nav-pill'))