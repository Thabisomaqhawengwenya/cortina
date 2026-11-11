import urllib.request
import os

os.makedirs('assets_icecream', exist_ok=True)

unsplash_items = {
    'hero_icecream_cone.jpg': 'https://images.unsplash.com/photo-1501443762994-82bd5dace89a?w=1080&q=80',  # Ice cream cone
    'vanilla_tub.jpg': 'https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=800&q=80',  # Ice cream scoop
    'strawberry_scoop.jpg': 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800&q=80',  # Strawberry ice cream
    'chocolate_scoop.jpg': 'https://images.unsplash.com/photo-1579954115545-a95591f28bfc?w=800&q=80',  # Chocolate ice cream
    'cherry_ripple.jpg': 'https://images.unsplash.com/photo-1587314168485-3236d6710814?w=800&q=80',  # Sundae / Berry swirl
    'shamiso_treat.jpg': 'https://images.unsplash.com/photo-1516559828984-fb3b99548b21?w=800&q=80',  # Dairy ice cream
    'cool_dudes_lollies.jpg': 'https://images.unsplash.com/photo-1505394033641-40c6ad1178d7?w=800&q=80',  # Popsicles / lollies
    'waffle_cone.jpg': 'https://images.unsplash.com/photo-1549395156-e0c1fe6fc7a5?w=800&q=80',  # Ice cream cone waffle
    'family_enjoying.jpg': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=80', # Friends / family ice cream
    'harare_tub.jpg': 'https://images.unsplash.com/photo-1576506295286-5cda18df43e7?w=800&q=80',
    'dessert_bowl.jpg': 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800&q=80'
}

for name, url in unsplash_items.items():
    path = os.path.join('assets_icecream', name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CortinaKefalos/1.0'})
        with urllib.request.urlopen(req, timeout=15) as resp, open(path, 'wb') as out:
            data = resp.read()
            out.write(data)
            print(f"Downloaded {name} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {name}: {e}")
