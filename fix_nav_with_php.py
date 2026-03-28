from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# Replace the entire nav with the rebuilt version
old_nav = '<a href="../index.html" class="nav-brand"><div class="nav-mark"><svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" width="16" height="16"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg></div><span class="nav-name">Communio</span></a><div class="nav-links"><a href="../index.html" class="nav-link">About</a><a href="../register.html" class="nav-link">Register your parish</a></div><a href="../dashboard/home.html" class="nav-pill"><div class="nav-av">SM</div><span class="nav-pname">St. Mary\'s</span></a><a href="../register.html" class="nav-btn">Join Communio</a>'

new_nav = '<a href="../index.html" class="nav-brand"><div class="nav-mark"><svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" width="16" height="16"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg></div><span class="nav-name">Communio</span></a><div class="nav-links"><a href="../index.html" class="nav-link">About</a><a href="../dashboard/network.html" class="nav-link">Browse Network</a><a href="../register.html" class="nav-link">Register your parish</a></div><!-- <?php if($logged_in): ?> --><a href="../dashboard/home.html" class="nav-pill"><div class="nav-av">SM</div><span class="nav-pname">St. Mary\'s</span></a><!-- <?php else: ?> --><a href="../register.html" class="nav-btn">Join Communio</a><!-- <?php endif ?> -->'

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    print("Nav replaced successfully")
else:
    print("NOT FOUND - need to check exact string")
    # Show what's actually in the nav area
    import re
    match = re.search(r'nav-brand.{0,100}', html)
    if match:
        print(repr(match.group()))

p.write_text(html, encoding='utf-8')