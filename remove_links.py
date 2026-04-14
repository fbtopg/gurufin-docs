#!/usr/bin/env python3
"""
Script to remove all internal markdown links from all .md files in the docs directory.
Handles various link formats: [text](path), [text](path#anchor), [`code`](path)
"""

import re
import os
from pathlib import Path

def remove_links(content):
    """Remove all internal markdown links while preserving link text."""
    
    original_content = content
    
    # Pattern 1: Standard markdown links [text](path)
    content = re.sub(r'\[(.*?)\]\([^)]+\)', r'\1', content)
    
    # Pattern 2: Inline code links [`text`](path)
    content = re.sub(r'\[`(.*?)`\]\([^)]+\)', r'\1', content)
    
    # Pattern 3: Links in table rows | [text](path) |
    content = re.sub(r'\|\s*\[(.*?)\]\([^)]+\)\s*\|', r'| \1 |', content)
    
    # Pattern 4: Links with anchor [text](path#anchor)
    content = re.sub(r'\[(.*?)\]\([^)]+#[^)]*\)', r'\1', content)
    
    # Pattern 5: Multiple links in same text
    content = re.sub(r'\[(.*?)\]\([^)]+\)', r'\1', content)
    
    # Pattern 6: Links in quick links sections - **Name**: [Link](path)
    content = re.sub(r'\*\*(.*?)\*\*:\s*\[(.*?)\]\([^)]+\)', r'**\1**: \2', content)
    
    return content

def process_file(file_path):
    """Process a single markdown file and remove links."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = remove_links(content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    base_dir = Path('/home/geonu/workspace/projects/gurufin-gitbook')
    
    # Find all markdown files in the project
    md_files = list(base_dir.rglob('*.md'))
    
    # Filter out hidden directories and non-docs files
    filtered_files = [
        f for f in md_files 
        if '.git' not in str(f) and 'remove_links' not in str(f)
    ]
    
    print(f"Found {len(filtered_files)} markdown files")
    print("Processing files...")
    
    modified_count = 0
    for file_path in filtered_files:
        if process_file(file_path):
            modified_count += 1
            print(f"✓ Modified: {file_path}")
        else:
            print(f"  No changes: {file_path}")
    
    print(f"\nCompleted! Modified {modified_count} files.")

if __name__ == '__main__':
    main()
