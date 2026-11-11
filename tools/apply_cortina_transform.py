import os
import re

print("Starting Cortina Ice Cream Transformation...")

# Transformation mappings
replacements = [
    # Brand Name
    ("CRAV | Artisan Smashed Burgers", "CORTINA | Artisan Gelato & Ice Cream"),
    ("CRAV Artisan Burgers", "CORTINA Artisan Gelato"),
    ("CRAV Burgers", "CORTINA Gelato"),
    ("CRAV", "CORTINA"),
    ("crav", "cortina"),
    
    # Hero & Headings
    ("THE BURGER", "THE SCOOP"),
    ("THE\\nBURGER", "THE\\nSCOOP"),
    ("juicy cheesy fully Loaded", "creamy velvety pure indulgence"),
    ("Eat like you mean it", "Scoop like you mean it"),
    ("Our Finest\\nBurger Picks", "Our Finest\\nGelato Flavors"),
    ("Our Finest Burger Picks", "Our Finest Gelato Flavors"),
    
    # Badges
    ("SMASHED\\nFRESH", "SLOW\\nCHURNED"),
    ("BOLD\\nFLAVOR", "PURE\\nCREAM"),
    ("SMASHED FRESH", "SLOW CHURNED"),
    ("BOLD FLAVOR", "PURE CREAM"),
    
    # Taglines & Copy
    (
        "Smashed hot on the flat top, our prime patties lock in ultimate juiciness under a caramelized crust.",
        "Slow churned in small batches daily, our gelato locks in silky micro-textures under velvety ribbons of pure indulgence."
    ),
    (
        "Topped with melted cheddar and our signature chili honey glaze crafted to satisfy your cravings since 1997.",
        "Infused with Bourbon vanilla, Bronte pistachios, and rich Belgian chocolate swirls crafted to satisfy your cravings since 1997."
    ),
    (
        "CRAV is back and bolder than ever. Honoring our rich roots, we bring you the ultimate smashed experience fully loaded, hot, and crafted fresh.",
        "Cortina brings authentic Italian gelato mastery to life. Honoring slow-churned heritage, we craft each scoop with pure mountain milk and toasted nuts."
    ),
    (
        "Smashed for the bold, built for the hungry. Dive into a legendary craft experience where every crispy edge and juicy layer rules.",
        "Crafted for the bold, churned for pure pleasure. Dive into a legendary gelato experience where every velvety ribbon and crunchy topping rules."
    ),
    (
        "Freshly packed smash burgers, ready to go wherever you crave. From our flat-top to any corner of the globe, we ensure every layer stays hot and juicy.",
        "Freshly packed artisan gelato pints, ready to go wherever you crave. Packed with insulated cold preservation to ensure every scoop stays chilled and velvety."
    ),
    (
        "Experience the ultimate artisan smashed burgers at CRAV. Fresh ingredients, bold flavors, and zero guilt. Est. 1997",
        "Experience the ultimate artisan slow-churned gelato at Cortina. Fresh mountain milk, bold flavors, and zero guilt. Est. 1997"
    ),
    (
        "Experience the ultimate artisan smashed burgers at CRAV. Fresh ingredients, bold flavors, and zero guilt.",
        "Experience the ultimate artisan slow-churned gelato at Cortina. Fresh mountain milk, bold flavors, and zero guilt."
    ),
    
    # Nav links
    ("BurgersBurgers", "GelatoGelato"),
    ("Burgers", "Gelato"),
    
    # Form
    ("GOT A CRAVING?\\nLET'S TALK", "WANT A TASTE?\\nLET'S TALK"),
    ("GOT A CRAVING?LET'S TALK", "WANT A TASTE?LET'S TALK"),
    ("TELL US YOUR CRAVING...", "TELL US YOUR FAVORITE FLAVORS..."),
    ("SEND CRAVING", "SEND INQUIRY"),
    
    # Menu Items
    ("Classic Burger", "Madagascar Gold"),
    ("Smashed beef · cheddar · house sauce", "Bourbon vanilla · honeycomb crunch · waffle crisp"),
    ("Spicy Jalapeño Burger", "Wild Raspberry Ripple"),
    ("Jalapeño · pepper jack · spicy mayo", "Raspberry coulis · white chocolate stracciatella"),
    ("Bacon Cheese Burger", "Pistachio Di Bronte"),
    ("Crispy bacon · cheddar · caramel onions", "Sicilian pistachios · Maldon sea salt · praline butter"),
    ("Veggie Delight Burger", "Midnight Dark Fudge"),
    ("Veggie patty · fresh crunch · house sauce", "72% Belgian dark chocolate · fudge lava swirl"),
    ("BBQ Ranch Burger", "Salted Caramel Dulce"),
    ("BBQ glaze · ranch · crispy onions", "Torched butter caramel · smoked sea salt · pretzel crunch"),
    ("Mushroom Swiss Burger", "Alphonso Mango Sorbet"),
    ("Sautéed mushrooms · swiss · garlic aioli", "Alphonso mango nectar · passionfruit zest · dairy-free")
]

# Apply to HTML files
target_files = [
    'raw_index.html',
    'page_menu.html',
    'page_spices.html',
    'page_contact.html',
    'manifest.webmanifest'
]

for tf in target_files:
    if not os.path.exists(tf):
        continue
    with open(tf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_len = len(content)
    for src, dst in replacements:
        content = content.replace(src, dst)
    
    with open(tf, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {tf} (len: {original_len} -> {len(content)})")

# Apply to key chunks
chunk_files = [
    '007kg070x-b~l.js',
    '014r2tef6u366.js',
    '0194vlaaft120.js',
    '0c-pxnn7_5v8q.js',
    '0c.pl-_.6beb_.js',
    '0jg2m1sj81gv0.js',
    '15b1_xl_2nu.v.js'
]

for cf in chunk_files:
    path = os.path.join('chunks', cf)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_len = len(content)
    for src, dst in replacements:
        content = content.replace(src, dst)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated chunks/{cf} (len: {original_len} -> {len(content)})")

print("Transformation complete!")
