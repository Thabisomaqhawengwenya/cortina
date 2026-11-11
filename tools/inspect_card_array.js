const fs = require('fs');

const code = fs.readFileSync('chunks/007kg070x-b~l.js', 'utf8');

// Find the product array
const startIdx = code.indexOf('let o=[');
if (startIdx !== -1) {
    const endIdx = code.indexOf('];function d', startIdx);
    console.log(code.substring(startIdx, endIdx + 2));
} else {
    console.log("Could not find 'let o=['");
}
