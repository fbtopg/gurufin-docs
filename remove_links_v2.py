#!/usr/bin/env python3
"""
Remove all links, hyperlinks, and cross-reference links from markdown files.
"""

import re
from pathlib import Path

def remove_links(text):
    """Remove all types of links from text."""
    result = text
    
    # Markdown links: [text](url) or [text](url "title")
    result = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', result)
    
    # Image links: ![alt](url) - remove entirely
    result = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', result)
    
    # Reference-style links: [text][ref] or [ref]
    result = re.sub(r'\[([^\]]+)\]\[[^\]]*\]', r'\1', result)
    
    # HTML inline links: <a href="url">text</a> or <a href='url'>text</a>
    result = re.sub(r'<a[^>]*href="[^"]*"[^>]*>([^<]*)</a>', r'\1', result)
    result = re.sub(r"<a[^>]*href='[^']*'[^>]*>([^<]*)</a>", r'\1', result)
    
    # HTML anchor tags with just href: <a href="url"></a>
    result = re.sub(r'<a[^>]*href="[^"]*"[^>]*></a>', '', result)
    result = re.sub(r"<a[^>]*href='[^']*'[^>]*></a>", '', result)
    
    # Backtick links: `text` (single backtick) - but not code blocks
    result = re.sub(r'`([^`\n]+)`', r'\1', result)
    
    # Code blocks with double backticks: ``text``
    result = re.sub(r'``([^`]+)``', r'\1', result)
    
    # Triple backtick code blocks: ```content``` - remove entire block
    result = re.sub(r'```[^`]*```', '', result)
    
    # Backtick-started code blocks: ` on one line, content, ` on another line
    result = re.sub(r'^`$\n', '', result, flags=re.MULTILINE)
    result = re.sub(r'\n^`$', '', result, flags=re.MULTILINE)
    
    # Backtick-prefixed URLs: `http://...` or `https://...`
    result = re.sub(r'`https?://[^\s`]+`', '', result)
    
    # Bare URLs with label before colon: `- URL: https://...` or `- RPC: https://...`
    result = re.sub(r'(-\s*\w+:\s*)https?://[^\s`]+', r'\1', result)
    
    # Reference-style link labels like `See: <link>` or `| <link> |`
    result = re.sub(r'(See:|Check:|Learn:|Read:)\s*[<`]\s*[^\s>`]+[\]>`]', r'\1', result)
    
    # Link labels in lists like `- Link Label: [text]`
    result = re.sub(r'(See:|Check:|Learn:|Read:)\s+\[[^\]]+\]', r'\1', result)
    
    # URLs with fragments like `text#section`
    result = re.sub(r'[<`]\s*https?://[^\s>`#]+#[^\s>`]+[\]>`]', r'', result)
    
    # Mailto links in markdown
    result = re.sub(r'\[([^\]]+)\]\(mailto:[^)]+\)', r'\1', result)
    
    # Cross-reference links at end of sentences like `See: <link>` or `| <link> |`
    result = re.sub(r'(See:|Check:|Learn:|Read:)\s*[<`]\s*[^\s>`]+[\]>`]', r'\1', result)
    
    # Remove standalone link references like `- Topic | Description |` patterns with links
    result = re.sub(r'\|\s*[<`]\s*[^\s>`]+[\]>`]\s*\|', ' | ', result)
    
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
