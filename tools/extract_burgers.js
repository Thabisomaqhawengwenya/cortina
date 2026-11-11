const fs = require('fs');

const code = fs.readFileSync('chunks/007kg070x-b~l.js', 'utf8');

// Find where burgers are defined
const idx = code.indexOf('Spicy Jalapeño Burger');
if (idx !== -1) {
    console.log(code.substring(idx - 300, idx + 1800));
}
