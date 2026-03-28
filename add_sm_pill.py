from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# Add the SM pill before the Join Communio button
html = html.replace(
    '<a href="../register.html" class="nav-btn">Join Communio</a></nav>',
    '<a href="../dashboard/home.html" class="nav-pill"><span class="nav-av">SM</span>St. Mary\'s</a><a href="../register.html" class="nav-btn">Join Communio</a></nav>'
)

p.write_text(html, encoding='utf-8')
print("Done:", html.count('nav-pill'))