import re

assets = set()
for fn in ['raw_index.html', 'page_menu.html', 'page_spices.html', 'page_contact.html', 'style1.css', 'style2.css']:
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # img src
    imgs = re.findall(r'src=["\']([^"\']+\.(?:png|webp|jpg|jpeg|svg|ico|woff2))["\']', content)
    assets.update(imgs)
    
    # url(...) in css or html
    urls = re.findall(r'url\(["\']?([^"\'\)]+\.(?:png|webp|jpg|jpeg|svg|ico|woff2))["\']?\)', content)
    assets.update(urls)
    
    # next/image url query parameter
    next_imgs = re.findall(r'url=([^&"\'\s]+\.(?:png|webp|jpg|jpeg|svg|ico))', content)
    for ni in next_imgs:
        import urllib.parse
        assets.add(urllib.parse.unquote(ni))

print(f"Total discovered media assets: {len(assets)}")
for a in sorted(assets):
    print(" ", a)
