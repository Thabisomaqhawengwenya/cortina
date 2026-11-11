import re

with open('style1.css', 'r', encoding='utf-8', errors='ignore') as f:
    s1 = f.read()

with open('style2.css', 'r', encoding='utf-8', errors='ignore') as f:
    s2 = f.read()

print("--- STYLE2 (len:", len(s2), ") ---")
print(s2)

print("\n--- STYLE1 ROOT VARIABLES ---")
root_vars = re.findall(r'--[a-zA-Z0-9_-]+:\s*[^;]+;', s1)
for rv in root_vars[:30]:
    print(rv)

print("\n--- FONT FACES ---")
fonts = re.findall(r'@font-face\s*\{[^}]+\}', s1, re.DOTALL)
for font in fonts:
    print(font)

print("\n--- KEYFRAMES ---")
keyframes = re.findall(r'@keyframes\s+([a-zA-Z0-9_-]+)', s1)
print(set(keyframes))
