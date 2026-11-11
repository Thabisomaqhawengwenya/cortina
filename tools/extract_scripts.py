import re
import os

with open('raw_index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find all script tags
all_scripts = re.findall(r'<script(.*?)>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
print(f"Total script tags: {len(all_scripts)}")
for i, (attrs, body) in enumerate(all_scripts):
    body_clean = body.strip()
    if body_clean:
        print(f"\n--- INLINE SCRIPT {i} (len: {len(body_clean)}) ---")
        print(body_clean[:500])
        if len(body_clean) > 500:
            print("...[truncated]")
