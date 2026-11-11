import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_page_sections(filename):
    print(f"\n==========================================")
    print(f"SECTIONS IN {filename}")
    print(f"==========================================")
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    sections = re.findall(r'<section(.*?)>(.*?)</section>', html, re.DOTALL | re.IGNORECASE)
    print(f"Total sections: {len(sections)}")

    for i, (attrs, sec) in enumerate(sections):
        c_m = re.search(r'class=["\'](.*?)["\']', attrs)
        classes = c_m.group(1) if c_m else ""
        print(f"\n--- SECTION {i+1} [classes: {classes[:80]}] ---")
        texts = [t.strip() for t in re.findall(r'>([^<]+)<', sec) if t.strip()]
        print("Texts preview:\n ", "\n  ".join(texts[:10]))

inspect_page_sections('page_spices.html')
inspect_page_sections('page_contact.html')
