import os
import re

chunk_dir = 'chunks'
for fn in os.listdir(chunk_dir):
    if not fn.endswith('.js'):
        continue
    filepath = os.path.join(chunk_dir, fn)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    # Turbopack registration patterns:
    # e.g., (self.TURBOPACK=self.TURBOPACK||[]).push(...)
    # or (globalThis.TURBOPACK_CHUNK_LISTS=...)
    print(f"File: {fn} (size: {len(text)} bytes)")
    first_line = text[:200]
    print(f"  Start: {first_line}")
