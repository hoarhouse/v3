#!/usr/bin/env python3
import os

# Define files and their configurations
files_config = [
    # rise/ directory files
    {'path': 'rise/index.html', 'data_page': 'home', 'script_src': 'nav-site.js', 'data_prefix': None},
    {'path': 'rise/intelligence.html', 'data_page': 'intelligence', 'script_src': 'nav-site.js', 'data_prefix': None},
    {'path': 'rise/rise.html', 'data_page': 'rise', 'script_src': 'nav-site.js', 'data_prefix': None},
    {'path': 'rise/thinking.html', 'data_page': 'thinking', 'script_src': 'nav-site.js', 'data_prefix': None},
    
    # rise/record/ directory files
    {'path': 'rise/record/index.html', 'data_page': 'record', 'script_src': '../nav-site.js', 'data_prefix': '../'},
    {'path': 'rise/record/ipcei-cis.html', 'data_page': 'record', 'script_src': '../nav-site.js', 'data_prefix': '../'},
    {'path': 'rise/record/kau.html', 'data_page': 'record', 'script_src': '../nav-site.js', 'data_prefix': '../'},
    {'path': 'rise/record/helix.html', 'data_page': 'record', 'script_src': '../nav-site.js', 'data_prefix': '../'},
    {'path': 'rise/record/eidas.html', 'data_page': 'record', 'script_src': '../nav-site.js', 'data_prefix': '../'},
    {'path': 'rise/record/medical-ai.html', 'data_page': 'record', 'script_src': '../nav-site.js', 'data_prefix': '../'},
    {'path': 'rise/record/peter-antal.html', 'data_page': 'record', 'script_src': '../nav-site.js', 'data_prefix': '../'},
    {'path': 'rise/record/press.html', 'data_page': 'record', 'script_src': '../nav-site.js', 'data_prefix': '../'},
]

# CSS to add before </style>
css_addition = '''nav:not(#site-nav) { display: none !important; }
.nav-mobile-menu:not(#site-nav-mobile) { display: none !important; }
</style>'''

for config in files_config:
    file_path = config['path']
    data_page = config['data_page']
    script_src = config['script_src']
    data_prefix = config['data_prefix']
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # CHANGE 1: Add data attributes to body tag
        if data_prefix:
            new_body = f'<body data-page="{data_page}" data-prefix="{data_prefix}">'
        else:
            new_body = f'<body data-page="{data_page}">'
        
        content = content.replace('<body>', new_body)
        
        # CHANGE 2: Add CSS hide rule before </style>
        # Find the last </style> in head (look for pattern that's likely in head section)
        # We'll look for the specific pattern with nav-has-dropdown styles
        if '.nav-has-dropdown .nav-dropdown li:first-child { border-bottom: 1px solid #1E1E1E; margin-bottom: 4px; }' in content:
            content = content.replace(
                '.nav-has-dropdown .nav-dropdown li:first-child { border-bottom: 1px solid #1E1E1E; margin-bottom: 4px; }\n</style>',
                '.nav-has-dropdown .nav-dropdown li:first-child { border-bottom: 1px solid #1E1E1E; margin-bottom: 4px; }\n' + css_addition
            )
        else:
            print(f"⚠ Could not find expected style pattern in {file_path}")
        
        # CHANGE 3: Add script tag before </body>
        content = content.replace('</body>', f'<script src="{script_src}"></script>\n</body>')
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {file_path}")
        
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")

print("\nAll files updated successfully!")