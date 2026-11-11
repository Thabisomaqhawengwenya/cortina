import os
import re

for fn in sorted(os.listdir('chunks')):
    if not fn.endswith('.js'):
        continue
    with open(os.path.join('chunks', fn), 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    
    # Check for gsap.to, gsap.timeline, ScrollTrigger, lenis, cursor, sticker
    terms = ['timeline', 'ScrollTrigger', 'Lenis', 'cursor', 'peel', 'sticker', 'audio', 'sound', 'svg', 'filter']
    matches = [t for t in terms if re.search(r'\b' + t + r'\b', txt, re.IGNORECASE)]
    if matches:
        print(f"{fn} matches: {', '.join(matches)}")
