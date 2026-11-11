with open('chunks/0jg2m1sj81gv0.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

import re
btn_idx = c.find('Order Now')
if btn_idx != -1:
    print("Found 'Order Now' in 0jg2m1sj81gv0.js:")
    print(c[max(0, btn_idx - 300): min(len(c), btn_idx + 400)])
