#!/usr/bin/env python3
import os
import sys
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
css_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(script_dir, 'design.css')

with open(css_path) as f:
    css = f.read()

# Find all var(--...) references
vars_used = set(re.findall(r'var\(--([^)]+)\)', css))

# Find custom properties defined inside :root { ... }
root_block = re.search(r':root\s*\{([^}]+)\}', css, re.DOTALL)
root_vars = set()
if root_block:
    root_vars = set(re.findall(r'--([\w-]+):', root_block.group(1)))

undefined = vars_used - root_vars

print('=== CSS var() Reference Check ===')
print(f'Variables used via var(): {len(vars_used)}')
print(f'  Defined set:  {sorted(root_vars)}')
print(f'  Used set:     {sorted(vars_used)}')

if undefined:
    print(f'\n❌ UNDEFINED VAR() REFERENCES: {sorted(undefined)}')
    sys.exit(1)
else:
    print(f'\n✅ All var() references resolve to defined custom properties.')

# Brace balance
opens = css.count('{')
closes = css.count('}')
print(f'\nBraces: {{ = {opens}, }} = {closes}')
print('✓ Balanced' if opens == closes else f'❌ MISMATCH (diff={opens-closes})')