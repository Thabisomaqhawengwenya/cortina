import os
from PIL import Image, ImageOps

os.makedirs('public/burgers', exist_ok=True)
os.makedirs('public/img-webp', exist_ok=True)
os.makedirs('public/img', exist_ok=True)

src_dir = 'assets_icecream'

def save_webp_and_png(src_path, dest_webp, dest_png=None, size=(1000, 1000), make_circular_or_clean=False):
    try:
        im = Image.open(src_path).convert('RGBA')
        # Center crop to square
        w, h = im.size
        min_dim = min(w, h)
        left = (w - min_dim) // 2
        top = (h - min_dim) // 2
        im = im.crop((left, top, left + min_dim, top + min_dim))
        im = im.resize(size, Image.Resampling.LANCZOS)
        
        if dest_webp:
            im.save(dest_webp, 'WEBP', quality=85)
            print(f"Saved {dest_webp}")
        if dest_png:
            im.save(dest_png, 'PNG', optimize=True)
            print(f"Saved {dest_png}")
    except Exception as e:
        print(f"Error processing {src_path}: {e}")

# Process Menu Burgers -> Cortina Ice Cream
menu_map = {
    'vanilla_tub.jpg': ('public/burgers/1b.png', 'public/img-webp/cheese.webp'),
    'strawberry_scoop.jpg': ('public/burgers/2b.png', 'public/img-webp/tomatoimg.webp'),
    'chocolate_scoop.jpg': ('public/burgers/3b.png', 'public/img-webp/meat.webp'),
    'cherry_ripple.jpg': ('public/burgers/4b.png', 'public/img-webp/tomato.webp'),
    'shamiso_treat.jpg': ('public/burgers/5b.png', 'public/img-webp/sydney.webp'),
    'cool_dudes_lollies.jpg': ('public/burgers/6b.png', 'public/img-webp/newyork.webp'),
    'hero_icecream_cone.jpg': (None, 'public/img-webp/burgerH.webp'),
    'dessert_bowl.jpg': (None, 'public/img-webp/cta.webp'),
    'waffle_cone.jpg': (None, 'public/img-webp/bun.webp'),
    'family_enjoying.jpg': (None, 'public/img-webp/burgerwithhands.webp'),
    'harare_tub.jpg': (None, 'public/img-webp/berlin.webp'),
    'strawberry_fruit.jpg': (None, 'public/img-webp/cheesyBurger.webp'),
    'milk.jpg': (None, 'public/img-webp/lettuceimg.webp'),
    'cherry.jpg': (None, 'public/img-webp/spices.webp')
}

for src_name, (dest_png, dest_webp) in menu_map.items():
    src_file = os.path.join(src_dir, src_name)
    if os.path.exists(src_file):
        save_webp_and_png(src_file, dest_webp, dest_png)

# Duplicate for remaining webp slots
for duplicate, target in [
    ('public/img-webp/berlin.webp', 'public/img-webp/london.webp'),
    ('public/img-webp/cta.webp', 'public/img-webp/tokyo.webp'),
    ('public/img-webp/bun.webp', 'public/img-webp/fries.webp'),
    ('public/img-webp/cheese.webp', 'public/img-webp/cheeseimg.webp'),
    ('public/img-webp/tomato.webp', 'public/img-webp/lettuce.webp'),
    ('public/img-webp/cheesyBurger.webp', 'public/img-webp/smoky-burger.webp'),
    ('public/img-webp/cheese.webp', 'public/img-webp/cheese-logo.webp'),
    ('public/img-webp/hero_icecream_cone.webp' if os.path.exists('public/img-webp/hero_icecream_cone.webp') else 'public/img-webp/burgerH.webp', 'public/img/burger-boy.png')
]:
    if os.path.exists(duplicate):
        img = Image.open(duplicate)
        img.save(target)
        print(f"Copied {duplicate} -> {target}")

print("All ice cream assets processed and mapped successfully!")
