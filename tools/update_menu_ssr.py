with open('page_menu.html', 'r', encoding='utf-8', errors='ignore') as f:
    t = f.read()

menu_ssr_replacements = [
    ("Madagascar Gold", "Vanilla"),
    ("Bourbon vanilla · honeycomb crunch · waffle crisp", "Classic creamy vanilla crafted from pure fresh dairy"),
    ("Wild Raspberry Ripple", "Strawberry"),
    ("Raspberry coulis · white chocolate stracciatella", "Sweet sun-ripened strawberry swirl in velvety smooth cream"),
    ("Pistachio Di Bronte", "Chocolate"),
    ("Sicilian pistachios · Maldon sea salt · praline butter", "Rich, decadent cocoa blended into smooth, creamy ice cream"),
    ("Midnight Dark Fudge", "Cherry Ripple"),
    ("72% Belgian dark chocolate · fudge lava swirl", "Pure vanilla ice cream swirled with sweet cherry sauce ribbons"),
    ("Salted Caramel Dulce", "Shamiso Original"),
    ("Torched butter caramel · smoked sea salt · pretzel crunch", "Zimbabwe's beloved dairy snack ice cream, rich & satisfying"),
    ("Alphonso Mango Sorbet", "Cool Dudes Lollies"),
    ("Alphonso mango nectar · passionfruit zest · dairy-free", "Refreshing fruit ice lollies in Berry Blast, Orange, Passion & Cream Soda"),
    
    # Prices
    ("$16", "Cortina Classic"),
    ("$18", "Cortina Classic"),
    ("$21", "Cortina Classic"),
    ("$15", "Cortina Classic"),
    ("$19", "Cortina Shamiso"),
    ("$20", "Cortina Cool Dudes"),
    
    # Quick info
    ("Brioche", "125ml"),
    ("Beef", "300ml"),
    ("Mild", "1L / 2L"),
    ("10–12 min", "5L Tub"),
    ("12–14 min", "Family Tub"),
    ("12–15 min", "Kids Size"),
    ("Hot", "Berry Blast"),
    ("Medium", "Orange"),
    ("Sesame", "Passion"),
    ("Veggie", "Cream Soda"),
    ("720", "Pure Dairy"),
    ("810", "Pure Dairy"),
    ("900", "Pure Dairy"),
    ("620", "Dairy Snack"),
    ("870", "Shamiso"),
    ("830", "Cool Dudes"),
    ("32g", "Kefalos"),
    ("34g", "Kefalos"),
    ("37g", "Kefalos"),
    ("17g", "Kefalos"),
    ("36g", "Kefalos"),
    ("33g", "Kefalos")
]

for src, dst in menu_ssr_replacements:
    t = t.replace(src, dst)

with open('page_menu.html', 'w', encoding='utf-8') as f:
    f.write(t)

print("Updated page_menu.html SSR content!")
