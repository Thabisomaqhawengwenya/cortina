import re

with open('page_menu.html', 'r', encoding='utf-8', errors='ignore') as f:
    menu_html = f.read()

# Let's search for currency symbols $, €, £ or numbers in page_menu.html
prices = re.findall(r'[\$€£]\s*\d+(?:\.\d{2})?', menu_html)
print(f"Prices found: {set(prices)}")

# Let's search for burger names or text patterns
items = re.findall(r'font-modak[^>]*>(.*?)<', menu_html)
print("Modak items:", set([i for i in items if i.strip()]))

# Let's search for chunks
chunks = re.findall(r'/_next/static/chunks/[a-zA-Z0-9_\-\.~]+\.js', menu_html)
print("Chunks in page_menu count:", len(set(chunks)))
for c in set(chunks):
    print(" ", c)
