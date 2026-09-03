#!/usr/bin/env python3
"""Check CSS var() references resolve to defined custom properties.
   Accepts CSS and HTML paths as optional CLI args; scans repo by default."""
import os
import sys
import re
import glob

def find_css_files(base_dir=None):
    """Find all .css files in the repo."""
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    # Look in root and common subdirectories
    patterns = [
        os.path.join(base_dir, '**/*.css'),
        os.path.join(base_dir, '*.css'),
        os.path.join(base_dir, 'frontend/**/*.css'),
        os.path.join(base_dir, 'frontend/*.css'),
    ]
    files = set()
    for p in patterns:
        for f in glob.glob(p, recursive=True):
            if os.path.isfile(f):
                files.add(os.path.normpath(f))
    return sorted(files)

def check_css_file(css_path):
    """Check a single CSS file for undefined var() references."""
    with open(css_path) as f:
        css = f.read()

    # Find all var(--...) references
    vars_used = set(re.findall(r'var\(--([^)]+)\)', css))

    # Find custom properties defined inside :root { ... }
    root_blocks = re.findall(r':root\s*\{([^}]+)\}', css, re.DOTALL)
    root_vars = set()
    for block in root_blocks:
        root_vars.update(set(re.findall(r'--([\w-]+):', block)))

    # Also find top-level variable definitions outside :root
    remaining = re.sub(r':root\s*\{[^}]+\}', '', css, flags=re.DOTALL)
    remaining = re.sub(r'@media[^{]+\{[^}]*\}', '', remaining, flags=re.DOTALL)
    top_vars = set(re.findall(r'--([\w-]+):', remaining))
    all_defined = root_vars | top_vars

    undefined = vars_used - all_defined

    return vars_used, all_defined, undefined

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Determine which CSS files to check
    if len(sys.argv) > 1:
        # Explicit paths provided as CLI args
        css_files = [os.path.abspath(p) for p in sys.argv[1:] if p.endswith('.css')]
        if not css_files:
            print("No .css files in arguments, using defaults", file=sys.stderr)
            css_files = find_css_files(script_dir)
    else:
        css_files = find_css_files(script_dir)

    if not css_files:
        print("❌ No CSS files found to check")
        sys.exit(1)

    all_pass = True
    for css_path in css_files:
        if not os.path.exists(css_path):
            print(f"⚠️  Skipping (not found): {css_path}")
            continue

        print(f"\n=== Checking: {css_path} ===")
        vars_used, all_defined, undefined = check_css_file(css_path)

        print(f'Variables used via var(): {len(vars_used)}')
        print(f'  Defined set:  {sorted(all_defined)}')
        print(f'  Used set:     {sorted(vars_used)}')

        if undefined:
            print(f'\n❌ UNDEFINED VAR() REFERENCES: {sorted(undefined)}')
            all_pass = False
        else:
            print(f'\n✅ All var() references resolve to defined custom properties.')

        # Brace balance
        with open(css_path) as f:
            css = f.read()
        opens = css.count('{')
        closes = css.count('}')
        balanced = opens == closes
        print(f'\nBraces: {{ = {opens}, }} = {closes}')
        print('✓ Balanced' if balanced else f'❌ MISMATCH (diff={opens-closes})')
        if not balanced:
            all_pass = False

    if all_pass:
        print(f'\n✅ All {len(css_files)} CSS file(s) passed.')
        sys.exit(0)
    else:
        print(f'\n❌ Some checks failed.')
        sys.exit(1)