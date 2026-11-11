import os
import re

chunk_dir = 'chunks'
libs = [
    'gsap', 'ScrollTrigger', 'framer-motion', 'framer', 'motion', 'lenis',
    'lucide', 'react-icons', 'zustand', 'jotai', 'redux', 'canvas-confetti',
    'three', 'spline', 'lottie', 'tailwind', 'shadcn', 'radix', 'swiper',
    'embla', 'stripe', 'paypal', 'cart', 'checkout'
]

results = {lib: set() for lib in libs}

for fn in os.listdir(chunk_dir):
    if not fn.endswith('.js'):
        continue
    filepath = os.path.join(chunk_dir, fn)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    for lib in libs:
        if re.search(r'\b' + re.escape(lib) + r'\b', text, re.IGNORECASE):
            results[lib].add(fn)

for lib, files in sorted(results.items()):
    if files:
        print(f"[{lib.upper()}] found in: {', '.join(files)}")
