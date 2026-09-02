#!/usr/bin/env python3
# Quick WCAG contrast check for k-sebe-yoga design.css
import sys

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

colors = {
    'primary':'#3D2F28','secondary':'#6B5B50','tertiary':'#C98153',
    'neutral':'#FFF8EF','surface':'#F7EDE1','on_tertiary':'#FFFFFF'
}

combos = [
    ('primary','neutral','body text on page bg'),
    ('primary','surface','body text on card bg'),
    ('secondary','neutral','.meta on page bg'),
    ('secondary','surface','.meta on card bg'),
    ('tertiary','on_tertiary','button bg vs white text (decorative, 3:1 threshold)'),
]

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