const fs = require('fs');

const code = fs.readFileSync('chunks/007kg070x-b~l.js', 'utf8');

// Find all burger details or data arrays in this file
const matches = code.match(/\{[^}]*name:[^}]*\}/g) || [];
console.log('Matches with "name:":', matches.length);
matches.forEach((m, i) => console.log(`[${i}] ${m.substring(0, 150)}`));

// Find all burger objects or menu definitions
const arrays = code.match(/\[\{[^{}\]]*name:[^{}\]]*\}\]/g) || [];
console.log('Arrays with name:', arrays.length);
