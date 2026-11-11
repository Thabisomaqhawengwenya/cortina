import urllib.request
import os

os.makedirs('assets_icecream', exist_ok=True)

test_urls = {
    'vanilla.jpg': 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Ice_cream_with_whipped_cream%2C_chocolate_syrup%2C_and_a_wafer_%28cropped%29.jpg',
    'strawberry.jpg': 'https://upload.wikimedia.org/wikipedia/commons/3/31/Ice_Cream_dessert_02.jpg',
    'cones.jpg': 'https://upload.wikimedia.org/wikipedia/commons/d/da/Strawberry_ice_cream_cone_%285076899310%29.jpg'
}

for name, url in test_urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CortinaProject/1.0'})
        path = os.path.join('assets_icecream', name)
        with urllib.request.urlopen(req, timeout=15) as resp, open(path, 'wb') as out:
            data = resp.read()
            out.write(data)
            print(f"Downloaded {name} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {name}: {e}")
