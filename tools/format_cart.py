import jsbeautifier
import sys

with open('chunks/007kg070x-b~l.js', 'r', encoding='utf-8') as f:
    code = f.read()

try:
    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    res = jsbeautifier.beautify(code, opts)
    with open('chunks/cart_beautified.js', 'w', encoding='utf-8') as f:
        f.write(res)
    print("Beautified with jsbeautifier")
except Exception as e:
    print("jsbeautifier not installed, writing basic formatting")
    import re
    # simple formatting
    formatted = code.replace('{', '{\n').replace('}', '\n}\n').replace(';', ';\n')
    with open('chunks/cart_beautified.js', 'w', encoding='utf-8') as f:
        f.write(formatted)
