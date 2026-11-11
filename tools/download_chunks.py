import urllib.request
import os

os.makedirs('chunks', exist_ok=True)

with open('find_all_chunks.py', 'r') as f:
    pass

import re
all_chunks = set()
for fn in ['raw_index.html', 'page_menu.html', 'page_spices.html', 'page_contact.html']:
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        chunks = re.findall(r'/_next/static/chunks/[a-zA-Z0-9_\-\.~]+\.js', f.read())
        all_chunks.update(chunks)

print(f"Downloading {len(all_chunks)} chunks...")
has_maps = []
for c in sorted(all_chunks):
    base_name = os.path.basename(c)
    local_path = os.path.join('chunks', base_name)
    url = f"https://www.cravburgers.shop{c}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(local_path, 'wb') as out:
            out.write(resp.read())
        
        # Check source map
        map_url = url + '.map'
        try:
            map_req = urllib.request.Request(map_url, headers={'User-Agent': 'Mozilla/5.0'})
            map_path = local_path + '.map'
            with urllib.request.urlopen(map_req) as map_resp, open(map_path, 'wb') as map_out:
                data = map_resp.read()
                map_out.write(data)
                has_maps.append(base_name)
                print(f"  [MAP FOUND!] {base_name}.map ({len(data)} bytes)")
        except Exception:
            pass
    except Exception as e:
        print(f"  Error downloading {c}: {e}")

print(f"\nDone! Downloaded chunks. Source maps found: {len(has_maps)}")
