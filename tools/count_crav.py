import os
import re

for fn in ['raw_index.html', 'page_menu.html', 'page_spices.html', 'page_contact.html', 'manifest.webmanifest']:
    if not os.path.exists(fn): continue
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    crav_upper = len(re.findall(r'\bCRAV\b', txt))
    crav_title = len(re.findall(r'\bCrav\b', txt))
    crav_lower = len(re.findall(r'\bcrav\b', txt))
    print(f"{fn}: CRAV={crav_upper}, Crav={crav_title}, crav={crav_lower}")
