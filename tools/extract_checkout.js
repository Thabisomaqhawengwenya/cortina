const fs = require('fs');

const code = fs.readFileSync('chunks/007kg070x-b~l.js', 'utf8');

// Search for modal, drawer, or checkout logic
const checkoutIdx = code.indexOf('Checkout');
if (checkoutIdx !== -1) {
    console.log(code.substring(checkoutIdx - 500, checkoutIdx + 1500));
}
