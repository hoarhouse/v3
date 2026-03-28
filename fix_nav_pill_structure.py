from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# Replace the broken pill with the correct structure matching the dashboard exactly
html = html.replace(
    '<a href="../dashboard/home.html" class="nav-pill"><span class="nav-av">SM</span>St. Mary\'s</a>',
    '<a href="../dashboard/home.html" class="nav-pill"><div class="nav-av">SM</div><span class="nav-pname">St. Mary\'s</span></a>'
)

p.write_text(html, encoding='utf-8')
print("Done:", html.count('nav-pname'))