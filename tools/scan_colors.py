import re
import os

files = ['style1.css', 'style2.css', 'raw_index.html', 'page_menu.html', 'page_spices.html', 'page_contact.html'] + [os.path.join('chunks', f) for f in os.listdir('chunks') if f.endswith('.js')]

color_patterns = [
    r'#F91[89]1[45]',
    r'#ffd750',
    r'#f4a804',
    r'#f5e3cd',
    r'#1b1b1b'
]

for cp in color_patterns:
    matches_count = 0
    files_with_match = []
    for fn in files:
        if not os.path.exists(fn): continue
        with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
            t = f.read()
            m = re.findall(cp, t, re.I)
            if m:
                matches_count += len(m)
                files_with_match.append(os.path.basename(fn))
    print(f"Pattern {cp}: {matches_count} matches in {len(files_with_match)} files: {', '.join(files_with_match[:6])}")
