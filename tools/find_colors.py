import re

with open('style1.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Search for color definitions or theme variables in style1.css
colors = re.findall(r'--(?:color-)?([a-zA-Z0-9_-]+):\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)|hsl\([^)]+\))', css)
print("Color variables in style1.css:")
for name, val in colors:
    print(f"  --{name}: {val}")

# Search for mustard, red, beige in css
for c in ['mustard', 'beige', 'red']:
    matches = re.findall(rf'({c}[^:{{;]+:[^;}}]+)', css)
    print(f"\nMatches for {c}:")
    for m in matches[:5]:
        print(" ", m)
