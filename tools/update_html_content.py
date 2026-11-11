import os
import re

print("Updating HTML files with authentic Cortina & Kefalos content...")

html_replacements = [
    # Hero Title
    ("THE SCOOP", "A LITTLE SCOOP OF HAPPINESS"),
    ("THE\\nSCOOP", "A LITTLE\\nSCOOP OF HAPPINESS"),
    ("THE BURGER", "A LITTLE SCOOP OF HAPPINESS"),
    (">THE<", ">A LITTLE<"),
    (">BURGER<", ">HAPPINESS<"),
    (">SCOOP<", ">HAPPINESS<"),
    
    # Hero description
    (
        "Slow churned in small batches daily, our gelato locks in silky micro-textures under velvety ribbons of pure indulgence.",
        "From creamy classics to exciting flavours, discover the delicious world of Cortina. Every scoop brings a little more joy to your day."
    ),
    (
        "Smashed hot on the flat top, our prime patties lock in ultimate juiciness under a caramelized crust.",
        "From creamy classics to exciting flavours, discover the delicious world of Cortina. Every scoop brings a little more joy to your day."
    ),
    (
        "Infused with Bourbon vanilla, Bronte pistachios, and rich Belgian chocolate swirls crafted to satisfy your cravings since 1997.",
        "Crafted with love by Kefalos Foods in Harare, Zimbabwe. Bringing smiles and pure dairy happiness to families since 1997."
    ),
    (
        "Topped with melted cheddar and our signature chili honey glaze crafted to satisfy your cravings since 1997.",
        "Crafted with love by Kefalos Foods in Harare, Zimbabwe. Bringing smiles and pure dairy happiness to families since 1997."
    ),
    
    # Hero badges
    ("SLOW\\nCHURNED", "PURE\\nDAIRY"),
    ("PURE\\nCREAM", "KEFALOS\\nZIMBABWE"),
    ("SLOW CHURNED", "PURE DAIRY"),
    ("PURE CREAM", "KEFALOS ZIMBABWE"),
    
    # Section 2
    ("creamy velvety pure indulgence", "A Little Scoop of Happiness"),
    ("juicy cheesy fully Loaded", "A Little Scoop of Happiness"),
    (
        "Cortina brings authentic Italian gelato mastery to life. Honoring slow-churned heritage, we craft each scoop with pure mountain milk and toasted nuts.",
        "Cortina brings the pure joy of ice cream to life. From creamy classics to exciting flavours, discover the delicious world of Cortina by Kefalos."
    ),
    (
        "CRAV is back and bolder than ever. Honoring our rich roots, we bring you the ultimate smashed experience fully loaded, hot, and crafted fresh.",
        "Cortina brings the pure joy of ice cream to life. From creamy classics to exciting flavours, discover the delicious world of Cortina by Kefalos."
    ),
    
    # CTA button
    ("Order Now", "Explore Our Flavours"),
    
    # Section 3: Exploded Layer Section
    ("Every Layer", "Every Scoop"),
    ("Signature", "Delicious"),
    ("Flavor", "Flavour"),
    
    # Section 4: Travel / Cities
    ("take away", "KEFALOS DAIRIES"),
    ("QUALITY THAT TRAVELS WITH YOU", "FRESHNESS THAT TRAVELS WITH YOU"),
    (
        "Freshly packed artisan gelato pints, ready to go wherever you crave. Packed with insulated cold preservation to ensure every scoop stays chilled and velvety.",
        "Packed in convenient 125ml cups, 300ml tubs, and 1L, 2L, and 5L family tubs, Cortina ice cream travels from our Harare dairies to every corner of Zimbabwe. Always fresh, always creamy."
    ),
    (
        "Freshly packed smash burgers, ready to go wherever you crave. From our flat-top to any corner of the globe, we ensure every layer stays hot and juicy.",
        "Packed in convenient 125ml cups, 300ml tubs, and 1L, 2L, and 5L family tubs, Cortina ice cream travels from our Harare dairies to every corner of Zimbabwe. Always fresh, always creamy."
    ),
    ("BERLIN", "HARARE"),
    ("LONDON", "BULAWAYO"),
    ("NEW YORK", "MUTARE"),
    ("SYDNEY", "GWERU"),
    ("TOKYO", "VICTORIA FALLS"),
    (
        "Grilled to perfection juicy, smoky, unforgettable.",
        "Fresh from the dairy, rich and creamy scoops for the sunshine capital."
    ),
    (
        "Sun-ripened tomatoes that bring natural sweetness and balance.",
        "Classic family tubs and refreshing treats across the City of Kings."
    ),
    (
        "Rich, creamy cheese that melts into every bite.",
        "Cool Dudes fruit ice lollies and sweet strawberry scoops in the sunshine."
    ),
    (
        "Soft, toasted buns crafted to hold everything together.",
        "Refreshing ice creams and cones enjoyed beside the mighty falls."
    ),
    
    # Section 6: Footer Hero
    ("feel the Change", "feel the Happiness"),
    ("feel theChange", "feel theHappiness"),
    ("FEEL IT", "TASTE IT"),
    (
        "Crafted for the bold, churned for pure pleasure. Dive into a legendary gelato experience where every velvety ribbon and crunchy topping rules.",
        "From family celebrations to sunny afternoon treats, Cortina ice cream brings people together. Discover our complete range of tubs, cones, and lollies today."
    ),
    (
        "Smashed for the bold, built for the hungry. Dive into a legendary craft experience where every crispy edge and juicy layer rules.",
        "From family celebrations to sunny afternoon treats, Cortina ice cream brings people together. Discover our complete range of tubs, cones, and lollies today."
    ),
    
    # Heritage / Location in Footer
    ("Est. 1997 — Navarra, España", "Kefalos · Harare, Zimbabwe"),
    ("Est. 1997  Navarra, Espaa", "Kefalos · Harare, Zimbabwe"),
    ("Navarra, España", "Harare, Zimbabwe"),
    
    # Menu Page replacements
    ("Scoop like you mean it", "A Little Scoop of Happiness"),
    ("Eat like you mean it", "A Little Scoop of Happiness"),
    ("Our Finest Gelato Flavors", "Our Finest Cortina Flavours"),
    ("Our Finest Gelato Picks", "Our Finest Cortina Flavours"),
    ("Our Finest\\nBurger Picks", "Our Finest\\nCortina Flavours"),
    ("Our Finest Burger Picks", "Our Finest Cortina Flavours"),
    
    # Spices Page -> Our Dairy
    ("from farm to bite", "from dairy to scoop"),
    ("from\\nfarm\\nto\\nbite", "from\\ndairy\\nto\\nscoop"),
    (
        "We didn't just pick ingredients off a list. We thought about where they come from, why they matter, and what they bring to the burger.",
        "At Kefalos, we believe true ice cream begins with wholesome fresh milk. Produced locally in Zimbabwe, Cortina is crafted with care, slow-churned for signature smoothness, and balanced with pure ingredients."
    ),
    ("Freshly Greens", "Fresh Farm Milk"),
    ("Juicy Tomatoes", "Real Fruit & Berries"),
    
    # Contact Page
    ("GOT A CRAVING?\\nLET'S TALK", "WANT TO STOCK CORTINA?\\nLET'S TALK"),
    ("WANT A TASTE?\\nLET'S TALK", "WANT TO STOCK CORTINA?\\nLET'S TALK"),
    ("GOT A CRAVING?LET'S TALK", "WANT TO STOCK CORTINA?LET'S TALK"),
    ("TELL US YOUR CRAVING...", "TELL US YOUR INQUIRY..."),
    ("TELL US YOUR FAVORITE FLAVORS...", "TELL US YOUR INQUIRY..."),
    ("SEND CRAVING", "SEND INQUIRY"),
    
    # Nav
    ("BurgersBurgers", "FlavoursFlavours"),
    ("Burgers", "Flavours"),
    ("GelatoGelato", "FlavoursFlavours"),
    ("Gelato", "Flavours"),
    ("Our Spices", "Our Dairy"),
    ("SpicesSpices", "DairyDairy"),
    ("Spices", "Our Dairy")
]

files = ['raw_index.html', 'page_menu.html', 'page_spices.html', 'page_contact.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        t = f.read()
    orig = t
    for src, dst in html_replacements:
        t = t.replace(src, dst)
    if t != orig:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"Updated {fn}")

print("HTML files updated successfully!")
