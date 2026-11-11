import os

print("Applying Cortina Brand Palette...")

# Color replacements
# Red -> Cortina Green (#007A3D)
# Mustard -> Cortina Yellow (#FFC72C)
# Mustard-Dark -> Deep Golden Yellow (#E5A200)
# Beige -> Vanilla Cream (#FBF6EA)
# Black -> Chocolate Brown (#2E1810)

palette_replacements = [
    # CSS definitions
    ('--red:#f91814', '--red:#007A3D'),
    ('--red: #f91814', '--red: #007A3D'),
    ('--mustard:#ffd750', '--mustard:#FFC72C'),
    ('--mustard: #ffd750', '--mustard: #FFC72C'),
    ('--mustard-dark:#f4a804', '--mustard-dark:#E5A200'),
    ('--mustard-dark: #f4a804', '--mustard-dark: #E5A200'),
    ('--beige:#f5e3cd', '--beige:#FBF6EA'),
    ('--beige: #f5e3cd', '--beige: #FBF6EA'),
    ('--black:#1b1b1b', '--black:#2E1810'),
    ('--black: #1b1b1b', '--black: #2E1810'),
    
    # Inline hexes
    ('#f91814', '#007A3D'),
    ('#F91814', '#007A3D'),
    ('#f91914', '#007A3D'),
    ('#F91914', '#007A3D'),
    ('#f4a804', '#E5A200'),
    ('#F4A804', '#E5A200'),
    ('#ffd750', '#FFC72C'),
    ('#FFD750', '#FFC72C'),
    ('#f5e3cd', '#FBF6EA'),
    ('#F5E3CD', '#FBF6EA')
]

target_files = [
    'style1.css',
    'style2.css',
    'raw_index.html',
    'page_menu.html',
    'page_spices.html',
    'page_contact.html',
    'manifest.webmanifest'
] + [os.path.join('chunks', f) for f in os.listdir('chunks') if f.endswith('.js')]

for path in target_files:
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content
    for src, dst in palette_replacements:
        content = content.replace(src, dst)
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated palette in {path}")

print("Palette updated!")
