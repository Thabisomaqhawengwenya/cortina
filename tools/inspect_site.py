import re
import json

with open('raw_index.html', 'r', encoding='utf-8') as f:
    content = f.read()

titles = re.findall(r'<title>(.*?)</title>', content, re.IGNORECASE)
print('--- TITLE ---')
print(titles)

print('\n--- SCRIPTS ---')
scripts = re.findall(r'<script[^>]*src=["\'](.*?)["\']', content, re.IGNORECASE)
for s in scripts:
    print(s)

print('\n--- STYLESHEETS ---')
styles = re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\'](.*?)["\']', content, re.IGNORECASE)
for st in styles:
    print(st)

print('\n--- META TAGS ---')
metas = re.findall(r'<meta[^>]*>', content, re.IGNORECASE)
for m in metas:
    if 'description' in m or 'og:' in m or 'twitter:' in m or 'theme-color' in m or 'viewport' in m:
        print(m)

# Find all __next_f segments
next_f_matches = re.findall(r'self\.__next_f\.push\(\[(.*?)\'\]\)', content, re.DOTALL)
print(f'\n--- NEXT_F MATCHES ({len(next_f_matches)}) ---')
