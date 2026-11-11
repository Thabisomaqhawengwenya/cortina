with open('chunks/15b1_xl_2nu.v.js', 'r', encoding='utf-8', errors='ignore') as f:
    c1 = f.read()

with open('chunks/0jg2m1sj81gv0.js', 'r', encoding='utf-8', errors='ignore') as f:
    c2 = f.read()

import re
print("--- Lenis in 15b1_xl_2nu.v.js ---")
lenis_matches = [m.start() for m in re.finditer('lenis', c1, re.I)]
for idx in lenis_matches[:3]:
    print(c1[max(0, idx - 150): min(len(c1), idx + 250)])
    print("="*40)

print("--- Cursor in 15b1_xl_2nu.v.js ---")
cursor_matches = [m.start() for m in re.finditer('cursor', c1, re.I)]
for idx in cursor_matches[:3]:
    print(c1[max(0, idx - 150): min(len(c1), idx + 250)])
    print("="*40)
