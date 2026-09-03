#!/usr/bin/env python3
# Quick WCAG contrast check for k-sebe-yoga design.css
# Reads CSS custom properties from design.css instead of hardcoded values
import sys
import os
import re

def lum(h):
    h = h.lstrip('#')
    r,g,b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    def srgb(v):
        v /= 255.0
        return v/12.92 if v <= 0.04045 else ((v+0.055)/1.055)**2.4
    return 0.2126*srgb(r) + 0.7152*srgb(g) + 0.0722*srgb(b)

def cr(fg,bg):
    l1,l2 = lum(fg), lum(bg)
    return round((max(l1,l2)+0.05)/(min(l1,l2)+0.05), 2)

def parse_css_vars(css_path):
    """Parse CSS custom properties from design.css file."""
    with open(css_path) as f:
        css = f.read()

    # Find all custom properties defined inside :root { ... }
    root_blocks = re.findall(r':root\s*\{([^}]+)\}', css, re.DOTALL)
    vars_map = {}
    for block in root_blocks:
        props = re.findall(r'--([\w-]+)\s*:\s*([^;]+);', block)
        for name, value in props:
            vars_map[name.strip()] = value.strip()

    # Also find properties in top-level CSS (not inside :root but at file level)
    # Remove :root blocks and media queries to find top-level vars
    remaining = re.sub(r':root\s*\{[^}]+\}', '', css, flags=re.DOTALL)
    remaining = re.sub(r'@media[^{]+\{[^}]*\}', '', remaining, flags=re.DOTALL)
    top_props = re.findall(r'--([\w-]+)\s*:\s*([^;]+);', remaining)
    for name, value in top_props:
        if name.strip() not in vars_map:
            vars_map[name.strip()] = value.strip()

    return vars_map

def resolve_color(vars_map, name):
    """Resolve a color name to its hex value, following var() references."""
    val = vars_map.get(name)
    if val is None:
        return None
    # Check if value references another var
    ref_match = re.match(r'var\(--([^)]+)\)', val)
    if ref_match:
        return resolve_color(vars_map, ref_match.group(1).strip())
    # Strip whitespace and return
    return val.strip()

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(script_dir, 'design.css')

    if not os.path.exists(css_path):
        print(f"❌ CSS file not found: {css_path}", file=sys.stderr)
        sys.exit(1)

    vars_map = parse_css_vars(css_path)

    # Define required color names for contrast checking
    required_colors = ['primary', 'secondary', 'tertiary', 'neutral', 'surface', 'on_tertiary']

    colors = {}
    missing = []
    for name in required_colors:
        val = resolve_color(vars_map, name)
        if val:
            colors[name] = val
        else:
            missing.append(name)

    if missing:
        print(f"❌ Missing required CSS variables: {missing}")
        print(f"   Available vars: {sorted(vars_map.keys())}")
        sys.exit(1)

    combos = [
        ('primary','neutral','body text on page bg'),
        ('primary','surface','body text on card bg'),
        ('secondary','neutral','.meta on page bg'),
        ('secondary','surface','.meta on card bg'),
        ('tertiary','on_tertiary','button bg vs white text (decorative, 3:1 threshold)'),
    ]

    print(f"Reading colors from: {css_path}")
    print(f"{'FG':<15} {'BG':<15} {'Ratio':<8} Result")
    print('-'*60)
    all_pass = True
    for f,b,u in combos:
        ratio = cr(colors[f], colors[b])
        req = 3.0 if 'decorative' in u else 4.5
        if ratio >= req:
            verb = f'PASS (AA {req}:1)'
        else:
            verb = f'FAIL (needs {req}:1)'
            all_pass = False
        print(f"{colors[f]:<15} {colors[b]:<15} {str(ratio):<8} {verb} — {u}")

    print()
    if all_pass:
        print('ALL TEXT-ON-BACKGROUND COMBOS PASS WCAG AA')
        sys.exit(0)
    else:
        print('SOME COMBOS FAIL WCAG AA — review above')
        sys.exit(1)

if __name__ == '__main__':
    main()
