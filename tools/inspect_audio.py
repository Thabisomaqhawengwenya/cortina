with open('chunks/0wj8l4fwydekq.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

import re
audio_matches = [m.start() for m in re.finditer('audio', c, re.I)]
print("Audio matches in 0wj8l4fwydekq.js:", len(audio_matches))
for idx in audio_matches[:5]:
    print(c[max(0, idx - 100): min(len(c), idx + 200)])
    print("="*40)
