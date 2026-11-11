with open('chunks/0194vlaaft120.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

import re
svg_idx = c.find('pointLight')
if svg_idx != -1:
    print(c[max(0, svg_idx - 200): min(len(c), svg_idx + 800)])
