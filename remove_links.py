#!/usr/bin/env python3
"""
Remove all links, hyperlinks, and cross-reference links from markdown files.
"""

import re
from pathlib import Path

# Define patterns to remove
LINK_PATTERNS = [
    # Markdown links: [text](url) or [text](url "title")
    (r'\[([^\]]+)\]\([^)]+\)', r'\1'),
    
    # Image links: ![alt](url) - remove entirely
    (r'!\[[^\]]*\]\([^)]+\)', r''),
    
    # Reference-style links: [text][ref] or [ref]
    (r'\[([^\]]+)\]\[[^\]]*\]', r'\1'),
    
    # HTML inline links: <a href="url">text</a> or <a href='url'>text</a>
    (r'<a[^>]*href="[^"]*"[^>]*>([^<]*)</a>', r'\1'),
    (r"<a[^>]*href='[^']*'[^>]*>([^<]*)</a>", r'\1'),
    
    # HTML anchor tags with just href: <a href="url"></a>
    (r'<a[^>]*href="[^"]*"[^>]*></a>', r''),
    (r"<a[^>]*href='[^']*'[^>]*></a>", r''),
    
    # Backtick links: `text` (single backtick)
    (r'`([^`]+)`', r'\1'),
    
    # Code blocks with double backticks: ``text``
    (r'``([^`]+)``', r'\1'),
    
    # Triple backtick code blocks: ```content```
    (r'```[^`]*```', r''),
    
    # URLs at start of line or in brackets: `http://...` or `https://...`
    (r'`https?://[^\s`]+`', r''),
    
    # Mailto links in markdown
    (r'\[([^\]]+)\]\(mailto:[^)]+\)', r'\1'),
]


def remove_links(text):
    """Remove all types of links from text."""
    result = text
    for pattern, replacement in LINK_PATTERNS:
        result = re.sub(pattern, replacement, result)
    return result


def process_file(file_path):
    """Process a single file and return success status."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Remove links
        content = remove_links(content)
        
        # Clean up any resulting whitespace issues
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)  # Multiple blank lines
        content = re.sub(r'\n{3,}', '\n\n\n', content)  # More than 3 newlines
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Process all markdown files in the docs directory."""
    docs_dir = Path("/home/geonu/workspace/projects/gurufin-gitbook/docs")
    
    # Find all markdown files
    md_files = list(docs_dir.rglob("*.md"))
    
    print(f"Found {len(md_files)} markdown files to process")
    print("-" * 60)
    
    success_count = 0
    for md_file in sorted(md_files):
        if process_file(md_file):
            print(f"✓ Removed links from: {md_file.relative_to(docs_dir.parent)}")
            success_count += 1
        else:
            print(f"  No changes needed: {md_file.relative_to(docs_dir.parent)}")
    
    print("-" * 60)
    print(f"Processed {success_count}/{len(md_files)} files successfully")


if __name__ == "__main__":
    main()
