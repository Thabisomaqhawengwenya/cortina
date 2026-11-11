import re

def analyze_html(filename):
    print(f"\n==================================================")
    print(f"ANALYSIS OF {filename}")
    print(f"==================================================")
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Extract all headings (h1, h2, h3, h4)
    headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html, re.DOTALL | re.IGNORECASE)
    print(f"\n--- HEADINGS ({len(headings)}) ---")
    for h in headings[:25]:
        clean_h = re.sub(r'<[^>]+>', '', h).strip()
        if clean_h:
            print(f"  • {clean_h}")

    # Extract all button texts
    buttons = re.findall(r'<button[^>]*>(.*?)</button>', html, re.DOTALL | re.IGNORECASE)
    print(f"\n--- BUTTONS ({len(buttons)}) ---")
    for b in set(re.sub(r'<[^>]+>', '', b).strip() for b in buttons if b.strip()):
        if b:
            print(f"  [BTN] {b}")

    # Extract all links (a href)
    links = re.findall(r'<a[^>]*href=["\'](.*?)["\'][^>]*>(.*?)</a>', html, re.DOTALL | re.IGNORECASE)
    print(f"\n--- NAV & LINKS ({len(links)}) ---")
    for href, text in links[:20]:
        clean_t = re.sub(r'<[^>]+>', '', text).strip()
        print(f"  -> {href} : '{clean_t}'")

    # Extract image sources
    images = re.findall(r'<img[^>]*src=["\'](.*?)["\']', html, re.IGNORECASE)
    print(f"\n--- IMAGES ({len(images)}) ---")
    for img in set(images):
        print(f"  [IMG] {img}")

analyze_html('raw_index.html')
analyze_html('page_menu.html')
analyze_html('page_spices.html')
analyze_html('page_contact.html')
