import re

with open('page_contact.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

inputs = re.findall(r'<input[^>]*>', html)
for inp in inputs:
    print("INPUT:", inp)

textareas = re.findall(r'<textarea[^>]*>', html)
for ta in textareas:
    print("TEXTAREA:", ta)

forms = re.findall(r'<form[^>]*>', html)
for frm in forms:
    print("FORM:", frm)
