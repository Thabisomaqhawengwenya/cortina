with open('chunks/0194vlaaft120.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

import re
peel_matches = [m.start() for m in re.finditer('peel', c, re.I)]
print("Peel matches count in 0194vlaaft120.js:", len(peel_matches))
for idx in peel_matches[:4]:
    print(c[max(0, idx - 150): min(len(c), idx + 250)])
    print("="*40)
