import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open('raw_index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find all section tags or main structure
sections = re.findall(r'<section(.*?)>(.*?)</section>', html, re.DOTALL | re.IGNORECASE)
print(f"Total sections on homepage: {len(sections)}")

for i, (attrs, sec) in enumerate(sections):
    # Find classes
    c_m = re.search(r'class=["\'](.*?)["\']', attrs)
    classes = c_m.group(1) if c_m else ""
    print(f"\n==========================================")
    print(f"--- SECTION {i+1} [classes: {classes[:80]}] ---")
    texts = [t.strip() for t in re.findall(r'>([^<]+)<', sec) if t.strip()]
    print("Texts preview:\n ", "\n  ".join(texts[:12]))
