#!/usr/bin/env python3
"""
Remove all links from markdown files while preserving visible text.
Handles Markdown links, HTML links, autolinks, and image links.
"""

import os
import re
from pathlib import Path

def remove_links(content: str) -> str:
    """Remove all links from markdown content, keeping only visible text."""
    
    # Remove image links: ![alt](url) - remove entirely
    content = re.sub(r'!\[[^\]]*\]\([^\)]*\)', '', content)
    
    # Remove HTML image tags: <img ...>
    content = re.sub(r'<img[^>]*>', '', content)
    
    # Remove HTML links: <a href="url">text</a> → text
    content = re.sub(r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']*)["\']([^>]*?)>(.*?)</a>', r'\3', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Remove Markdown links: [text](url) → text
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    
    # Remove autolinks: <url> → url
    content = re.sub(r'<(https?://[^\s<>]+)>', r'\1', content)
    
    # Remove bare URLs that might be links: (http://...) or just http://...
    # Keep them as text but make them non-linky
    content = re.sub(r'\((https?://[^\s)]+)\)', r' \1 ', content)
    
    return content.strip()

def process_file(file_path: str) -> bool:
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        cleaned_content = remove_links(original_content)
        
        if cleaned_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            print(f"✓ Cleaned: {file_path}")
            return True
        else:
            print(f"  No links in: {file_path}")
            return False
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def main():
    project_dir = Path("/home/geonu/workspace/projects/gurufin-gitbook")
    cleaned_count = 0
    
    # Find all markdown files
    md_files = list(project_dir.rglob("*.md"))
    
    print(f"Found {len(md_files)} markdown files\n")
    
    for md_file in md_files:
        if process_file(str(md_file)):
            cleaned_count += 1
    
    print(f"\n{'='*60}")
    print(f"Total files cleaned: {cleaned_count}/{len(md_files)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
