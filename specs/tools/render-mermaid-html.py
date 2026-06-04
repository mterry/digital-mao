#!/usr/bin/env python3
"""
Render Mermaid diagram source files to interactive HTML.
This script creates standalone HTML files with embedded Mermaid diagrams.
"""

import sys
import os
from pathlib import Path

def create_html(mermaid_content, title="Mermaid Diagram"):
    """Create HTML with embedded Mermaid diagram."""
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true,
            theme: 'default',
            securityLevel: 'loose',
            flowchart: {{
                useMaxWidth: true,
                htmlLabels: true,
                curve: 'basis'
            }}
        }});
    </script>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            margin-top: 0;
        }}
        .mermaid {{
            text-align: center;
            margin: 20px 0;
        }}
        .footer {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #666;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <div class="mermaid">
{mermaid_content}
        </div>
        <div class="footer">
            <p>Generated from Mermaid source diagram</p>
            <p>Interactive diagram - you can zoom and pan</p>
        </div>
    </div>
</body>
</html>"""
    return html_template

def main():
    if len(sys.argv) != 3:
        print("Usage: python render-mermaid-html.py <input.mmd> <output.html>")
        print("Example: python render-mermaid-html.py diagrams/source/c4-context.mmd diagrams/rendered/c4-context.html")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])
    
    # Check if input file exists
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    # Read Mermaid source
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            mermaid_content = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Generate title from filename
    title = input_file.stem.replace('-', ' ').replace('_', ' ').title()
    
    # Create HTML
    html_content = create_html(mermaid_content, title)
    
    # Write output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ Successfully rendered: {output_file}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

# Made with Bob
