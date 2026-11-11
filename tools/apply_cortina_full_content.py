import os
import re

print("Starting Full Cortina Content Replacement...")

# 1. Update chunks/007kg070x-b~l.js (Menu card data and modal)
with open('chunks/007kg070x-b~l.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the product array in 007kg070x-b~l.js
old_array_pattern = r'let o=\[\{name:.*?\}\];function d'

new_array = '''let o=[{name:"Vanilla",price:"Cortina Classic",image:"/burgers/1b.png",detail:"Classic creamy vanilla crafted from pure fresh dairy",quick:{bun:"125ml",patty:"300ml",spice:"1L / 2L",time:"5L Tub"},nutrition:{calories:"Pure Dairy",protein:"Kefalos"}},{name:"Strawberry",price:"Cortina Classic",image:"/burgers/2b.png",detail:"Sweet sun-ripened strawberry swirl in velvety smooth cream",quick:{bun:"125ml",patty:"300ml",spice:"1L / 2L",time:"5L Tub"},nutrition:{calories:"Pure Dairy",protein:"Kefalos"}},{name:"Chocolate",price:"Cortina Classic",image:"/burgers/3b.png",detail:"Rich, decadent cocoa blended into smooth, creamy ice cream",quick:{bun:"125ml",patty:"300ml",spice:"1L / 2L",time:"5L Tub"},nutrition:{calories:"Pure Dairy",protein:"Kefalos"}},{name:"Cherry Ripple",price:"Cortina Classic",image:"/burgers/4b.png",detail:"Pure vanilla ice cream swirled with sweet cherry sauce ribbons",quick:{bun:"125ml",patty:"300ml",spice:"1L / 2L",time:"5L Tub"},nutrition:{calories:"Pure Dairy",protein:"Kefalos"}},{name:"Shamiso Original",price:"Cortina Shamiso",image:"/burgers/5b.png",detail:"Zimbabwe's beloved dairy snack ice cream, rich & satisfying",quick:{bun:"125ml",patty:"300ml",spice:"5L Tub",time:"Dairy Snack"},nutrition:{calories:"Shamiso",protein:"Kefalos"}},{name:"Cool Dudes Lollies",price:"Cortina Cool Dudes",image:"/burgers/6b.png",detail:"Refreshing fruit ice lollies in Berry Blast, Orange, Passion & Cream Soda",quick:{bun:"70ml",patty:"110ml",spice:"Real Fruit",time:"Ice Lolly"},nutrition:{calories:"Cool Dudes",protein:"Kefalos"}}];function d'''

c = re.sub(old_array_pattern, new_array, c, flags=re.DOTALL)

# Update modal text in 007kg070x-b~l.js
modal_old = 'title:"Checkout",badge:"Concept",children:"This is a concept website created by Anyflow Agency. If you are looking for brand design and development like this, you can reach out to us at anyflowagency@gmail.com"'
modal_new = 'title:"Cortina Ice Cream",badge:"Kefalos Zimbabwe",children:"Cortina Ice Cream is proudly produced by Kefalos in Harare, Zimbabwe. Available in 125ml, 300ml, 1L, 2L, and 5L tubs, cones, and lollies across all leading supermarkets and vendors nationwide. For commercial and retail distribution, visit kefalosfood.com."'
c = c.replace(modal_old, modal_new)

# Update "Added to Cart" to "Flavour Selected"
c = c.replace('"Added to Cart"', '"Flavour Selected"')
c = c.replace('"Checkout"', '"Inquire"')

with open('chunks/007kg070x-b~l.js', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated chunks/007kg070x-b~l.js")

# 2. Update CTA button in chunks/014r2tef6u366.js, 0194vlaaft120.js, 0c.pl-_.6beb_.js
for fn in ['014r2tef6u366.js', '0194vlaaft120.js', '0c.pl-_.6beb_.js']:
    p = os.path.join('chunks', fn)
    if not os.path.exists(p): continue
    with open(p, 'r', encoding='utf-8') as f:
        txt = f.read()
    txt = txt.replace('"Order Now"', '"Explore Our Flavours"')
    txt = txt.replace('Order Now', 'Explore Our Flavours')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f"Updated CTA in {fn}")

# 3. Update Cities in chunks/0c-pxnn7_5v8q.js
with open('chunks/0c-pxnn7_5v8q.js', 'r', encoding='utf-8') as f:
    c_cities = f.read()

city_replacements = [
    ('"BERLIN"', '"HARARE"'),
    ('BERLIN', 'HARARE'),
    ('"LONDON"', '"BULAWAYO"'),
    ('LONDON', 'BULAWAYO'),
    ('"NEW YORK"', '"MUTARE"'),
    ('NEW YORK', 'MUTARE'),
    ('"SYDNEY"', '"GWERU"'),
    ('SYDNEY', 'GWERU'),
    ('"TOKYO"', '"VICTORIA FALLS"'),
    ('TOKYO', 'VICTORIA FALLS'),
    ('takeaway packaging in Berlin', 'Cortina Ice Cream in Harare'),
    ('takeaway packaging in London', 'Cortina Ice Cream in Bulawayo'),
    ('takeaway packaging in New York', 'Cortina Cool Dudes in Mutare'),
    ('takeaway packaging in Sydney', 'Cortina Shamiso in Gweru'),
    ('takeaway packaging in Tokyo', 'Cortina Ice Cream at Victoria Falls')
]
for src, dst in city_replacements:
    c_cities = c_cities.replace(src, dst)

with open('chunks/0c-pxnn7_5v8q.js', 'w', encoding='utf-8') as f:
    f.write(c_cities)
print("Updated chunks/0c-pxnn7_5v8q.js")

# 4. Update Preloader in chunks/15b1_xl_2nu.v.js
with open('chunks/15b1_xl_2nu.v.js', 'r', encoding='utf-8') as f:
    c_pre = f.read()
c_pre = c_pre.replace('PREPARING ARTISAN KITCHEN...', 'PREPARING CORTINA ICE CREAM...')
c_pre = c_pre.replace('Est. 1997 — Navarra, España', 'Kefalos · Harare, Zimbabwe')
c_pre = c_pre.replace('Est. 1997  Navarra, Espaa', 'Kefalos · Harare, Zimbabwe')
with open('chunks/15b1_xl_2nu.v.js', 'w', encoding='utf-8') as f:
    f.write(c_pre)
print("Updated chunks/15b1_xl_2nu.v.js")

# 5. Update Navigation & Links in chunks/0jg2m1sj81gv0.js
with open('chunks/0jg2m1sj81gv0.js', 'r', encoding='utf-8') as f:
    c_nav = f.read()
c_nav = c_nav.replace('Est. 1997 — Navarra, España', 'Kefalos · Harare, Zimbabwe')
c_nav = c_nav.replace('{label:"Our Spices",href:"/spices"}', '{label:"Our Dairy",href:"/spices"}')
c_nav = c_nav.replace('Our Spices', 'Our Dairy')
c_nav = c_nav.replace('{label:"Gelato",href:"/menu"}', '{label:"Flavours",href:"/menu"}')
c_nav = c_nav.replace('Gelato', 'Flavours')
with open('chunks/0jg2m1sj81gv0.js', 'w', encoding='utf-8') as f:
    f.write(c_nav)
print("Updated chunks/0jg2m1sj81gv0.js")

print("All chunks updated cleanly!")
