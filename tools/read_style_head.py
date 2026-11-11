with open('style1.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(min(40, len(lines))):
    print(f"{i+1}: {lines[i][:120]}")
