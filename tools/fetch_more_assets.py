import urllib.request
import os

images_map = {
    'chocolate.jpg': 'https://upload.wikimedia.org/wikipedia/commons/f/f2/Chocolate_Ice_Cream.jpg',
    'sundae.jpg': 'https://upload.wikimedia.org/wikipedia/commons/e/e5/Ice_Cream_Sundae.jpg',
    'lollies.jpg': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Ice_Pops.jpg',
    'strawberry_fruit.jpg': 'https://upload.wikimedia.org/wikipedia/commons/2/29/PerfectStrawberry.jpg',
    'cherry.jpg': 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Cherry_Stella444.jpg',
    'milk.jpg': 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Milk_glass.jpg',
    'mint.jpg': 'https://upload.wikimedia.org/wikipedia/commons/a/a2/Mentha_spicata_002.JPG'
}

for name, url in images_map.items():
    path = os.path.join('assets_icecream', name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CortinaKefalos/1.0'})
        with urllib.request.urlopen(req, timeout=15) as resp, open(path, 'wb') as out:
            data = resp.read()
            out.write(data)
            print(f"Downloaded {name} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {name}: {e}")
