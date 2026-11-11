import os
import re

for fn in sorted(os.listdir('chunks')):
    if not fn.endswith('.js'): continue
    with open(os.path.join('chunks', fn), 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    crav_upper = len(re.findall(r'\bCRAV\b', txt))
    if crav_upper > 0 or 'cravburgers' in txt:
        print(f"chunks/{fn}: CRAV={crav_upper}, cravburgers={'cravburgers' in txt}")
