with open('chunks/007kg070x-b~l.js', 'r', encoding='utf-8', errors='ignore') as f:
    txt = f.read()

import re
print("File size:", len(txt))

# Find string literals in this chunk
strings = re.findall(r'"([^"\\]{4,100})"', txt)
filtered = [s for s in strings if not s.startswith('http') and not s.startswith('/') and not s.startswith('__')]
print("Sample unique strings in 007kg070x-b~l.js:")
for s in sorted(set(filtered))[:50]:
    print(" ", s)
