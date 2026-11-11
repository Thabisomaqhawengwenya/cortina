import os
import re

print("Scrubbing remaining burger text and metadata...")

meta_replacements = [
    ("Artisan Burger Menu | CORTINA Flavours", "Cortina Flavours | Kefalos Ice Cream Zimbabwe"),
    ("Artisan Burger Menu", "Cortina Flavours"),
    ("smashed burgers", "artisan ice cream"),
    ("Smashed burgers", "Artisan ice cream"),
    ("smashed burger", "artisan ice cream"),
    ("Smashed burger", "Artisan ice cream"),
    ("premium smashed burgers", "delicious Cortina ice cream tubs and cones"),
    ("cheeseburgers", "ice cream tubs"),
    ("artisan burgers,smashed burgers,fresh ingredients,organic burgers,CORTINA burgers", "cortina ice cream,kefalos ice cream,zimbabwe ice cream,shamiso ice cream,cool dudes lollies,vanilla ice cream,harare dairy"),
    ("https://www.cortinaburgers.shop", "https://www.kefalosfood.com"),
    ("cortinaburgers.shop", "kefalosfood.com"),
    ("Experience the ultimate artisan smashed burgers at CORTINA", "Discover the delicious world of Cortina Ice Cream by Kefalos"),
    ("Experience the ultimate artisan smashed burgers at CORTINA. Fresh ingredients, bold flavors, and zero guilt.", "From creamy classics to exciting flavours, discover the delicious world of Cortina. Every scoop brings a little more joy to your day."),
    ("Premium smashed burger on a wooden board", "Cortina artisan ice cream tub and dessert scoops"),
    ("CRAV Artisan Smashed Burger with fresh ingredients", "Cortina Artisan Ice Cream Cone with double scoop"),
    ("burgerH.webp", "burgerH.webp"),
    ("burger-boy.png", "burger-boy.png"),
    ("CORTINA Flavours", "Cortina Ice Cream")
]

files = ['raw_index.html', 'page_menu.html', 'page_spices.html', 'page_contact.html', 'manifest.webmanifest']

for fn in files:
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        t = f.read()
    orig = t
    for src, dst in meta_replacements:
        t = t.replace(src, dst)
    if t != orig:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"Scrubbed {fn}")

print("Metadata cleaned!")
