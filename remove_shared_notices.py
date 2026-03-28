from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# Remove both visible "Shared from Settings" notices injected in Phase 3
html = html.replace(
    '<a href="/v3/communio/dashboard/settings.html" class="shared-notice">⚙ Shared from Settings — edit in Settings →</a',
    ''
)
html = html.replace(
    '<span class="shared-notice">⚙ Shared from Settings — edit in Settings →</span',
    ''
)

p.write_text(html, encoding='utf-8')
print("shared-notice occurrences remaining:", html.count('shared-notice'))