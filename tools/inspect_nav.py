with open('chunks/15b1_xl_2nu.v.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

import re
nav_idx = c.find('Burgers')
if nav_idx != -1:
    print("Found 'Burgers' in 15b1_xl_2nu.v.js:")
    print(c[max(0, nav_idx - 300): min(len(c), nav_idx + 800)])
else:
    # search other chunks
    import os
    for fn in os.listdir('chunks'):
        if not fn.endswith('.js'): continue
        with open(os.path.join('chunks', fn), 'r', encoding='utf-8', errors='ignore') as f2:
            txt = f2.read()
            if 'BurgersBurgers' in txt or 'Our Spices' in txt:
                print(f"Found navigation in {fn}:")
                idx = txt.find('Our Spices')
                print(txt[max(0, idx - 200): min(len(txt), idx + 600)])
                break
