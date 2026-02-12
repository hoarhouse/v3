#!/usr/bin/env python3
import os
from pathlib import Path

def fix_double_v3(file_path):
    """Replace /v3//v3/ with /v3/ in HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace all instances of /v3//v3/ with /v3/
        content = content.replace('/v3//v3/', '/v3/')
        
        # Also catch any ..//v3/ patterns that might exist
        content = content.replace('..//v3/', '/v3/')
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Count replacements for reporting
            count = original_content.count('/v3//v3/') + original_content.count('..//v3/')
            
            print(f"Updated {os.path.relpath(file_path, '/Users/christopherhoar/Desktop/v3/vatican-resources')}: {count} replacements")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error updating {os.path.basename(file_path)}: {e}")
        return None

def process_directory(directory_path):
    """Process all HTML files in a directory"""
    updated = 0
    skipped = 0
    errors = 0
    
    for file_path in Path(directory_path).glob('*.html'):
        result = fix_double_v3(file_path)
        if result is True:
            updated += 1
        elif result is False:
            skipped += 1
        else:
            errors += 1
    
    return updated, skipped, errors

def main():
    base_path = '/Users/christopherhoar/Desktop/v3/vatican-resources'
    
    print("Fixing double /v3/ paths in vatican-resources HTML files...")
    print("="*60)
    
    # Process main directory
    print("\nMain directory:")
    main_updated, main_skipped, main_errors = process_directory(base_path)
    
    # Process htmldocs subdirectory
    print("\nhtmldocs subdirectory:")
    htmldocs_path = os.path.join(base_path, 'htmldocs')
    htmldocs_updated, htmldocs_skipped, htmldocs_errors = process_directory(htmldocs_path)
    
    print("\n" + "="*60)
    print("Summary:")
    print(f"Main directory: {main_updated} updated, {main_skipped} unchanged, {main_errors} errors")
    print(f"htmldocs: {htmldocs_updated} updated, {htmldocs_skipped} unchanged, {htmldocs_errors} errors")
    print(f"Total: {main_updated + htmldocs_updated} files updated")

if __name__ == "__main__":
    main()