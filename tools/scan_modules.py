import os
import re

chunk_dir = 'chunks'
source_paths = set()
packages = set()

for fn in os.listdir(chunk_dir):
    if not fn.endswith('.js'):
        continue
    filepath = os.path.join(chunk_dir, fn)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    # Turbopack module pattern: [project]/... or "[project]/..."
    matches = re.findall(r'\[project\]/[a-zA-Z0-9_\-/\.]+', text)
    source_paths.update(matches)
    
    # Check for node_modules
    nm_matches = re.findall(r'node_modules/([a-zA-Z0-9@_\-]+)', text)
    packages.update(nm_matches)

print(f"=== DISCOVERED PROJECT SOURCE PATHS ({len(source_paths)}) ===")
for p in sorted(source_paths):
    print(p)

print(f"\n=== DISCOVERED NODE MODULE PACKAGES ({len(packages)}) ===")
for pkg in sorted(packages):
    print(pkg)
