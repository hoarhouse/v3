from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/index.html')
html = p.read_text(encoding='utf-8')

# Replace the nav-links (The network, Collaborate, Tools, Pricing)
html = html.replace(
    '<a href="#network" class="nav-link">The network</a>',
    '<a href="#network" class="nav-link">About</a>'
)
html = html.replace(
    '<a href="#collaborate" class="nav-link">Collaborate</a>',
    '<a href="dashboard/network.html" class="nav-link">Browse Network</a>'
)
html = html.replace(
    '<a href="#tools" class="nav-link">Tools</a>',
    '<a href="register.html" class="nav-link">Register your parish</a>'
)
html = html.replace(
    '<a href="#pricing" class="nav-link">Pricing</a>',
    ''
)

# Replace "View demo →" with a proper link to the live profile demo
html = html.replace(
    'class="nav-link">View demo →</a>',
    'class="nav-link nav-demo">View demo →</a>'
)
html = html.replace(
    'href="dashboard/profile.html" class="nav-link nav-demo">View demo →</a>',
    'href="parish/profile.html" class="nav-link nav-demo">View demo →</a>'
)

p.write_text(html, encoding='utf-8')
print("Done")
print("About count:", html.count('>About<'))
print("Browse Network count:", html.count('>Browse Network<'))