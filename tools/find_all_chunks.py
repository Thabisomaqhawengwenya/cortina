import re

all_chunks = set()
for fn in ['raw_index.html', 'page_menu.html', 'page_spices.html', 'page_contact.html']:
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        chunks = re.findall(r'/_next/static/chunks/[a-zA-Z0-9_\-\.~]+\.js', f.read())
        all_chunks.update(chunks)

print(f"Total unique chunks: {len(all_chunks)}")
for c in sorted(all_chunks):
    print(c)
