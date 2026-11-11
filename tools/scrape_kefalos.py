import urllib.request
import re
import os

urls = [
    'https://www.kefalosfood.com/',
    'https://www.kefalosfood.com/cortina-ice-cream/',
    'https://www.kefalosfood.com/cortina-shamiso-ice-cream/',
    'https://www.kefalosfood.com/cortina-ice-lollies/'
]

os.makedirs('kefalos_data', exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

for url in urls:
    print('Fetching:', url)
    slug = url.strip('/').split('/')[-1] or 'home'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            with open(f'kefalos_data/{slug}.html', 'w', encoding='utf-8') as f:
                f.write(html)
            
            title = re.findall(r'<title>(.*?)</title>', html, re.I)
            print(f'  Title: {title}')
            
            # Find images
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.I)
            print(f'  Images: {len(imgs)}')
            for img in imgs:
                if 'cortina' in img.lower() or 'kefalos' in img.lower() or 'ice-cream' in img.lower() or 'shamiso' in img.lower():
                    print('    ->', img)
    except Exception as e:
        print('  Error fetching:', e)
