const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = 3000;
const REMOTE_ORIGIN = 'https://www.cravburgers.shop';

// Map known pages
const ROUTES = {
  '/': 'raw_index.html',
  '/menu': 'page_menu.html',
  '/spices': 'page_spices.html',
  '/contact': 'page_contact.html'
};

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2',
  '.ico': 'image/x-icon',
  '.webmanifest': 'application/manifest+json'
};

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const pathname = parsedUrl.pathname;

  // 1. Check if it's one of our main pages
  if (ROUTES[pathname]) {
    const filePath = path.join(__dirname, ROUTES[pathname]);
    if (fs.existsSync(filePath)) {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      return fs.createReadStream(filePath).pipe(res);
    }
  }

  // 2. Check local CSS files
  if (pathname === '/_next/static/chunks/0ovftnp3y9gzb.css' && fs.existsSync(path.join(__dirname, 'style1.css'))) {
    res.writeHead(200, { 'Content-Type': 'text/css' });
    return fs.createReadStream(path.join(__dirname, 'style1.css')).pipe(res);
  }
  if (pathname === '/_next/static/chunks/05n9.pfd~lr39.css' && fs.existsSync(path.join(__dirname, 'style2.css'))) {
    res.writeHead(200, { 'Content-Type': 'text/css' });
    return fs.createReadStream(path.join(__dirname, 'style2.css')).pipe(res);
  }

  // 3. Check local JS chunks
  if (pathname.startsWith('/_next/static/chunks/')) {
    const filename = path.basename(pathname);
    const chunkPath = path.join(__dirname, 'chunks', filename);
    if (fs.existsSync(chunkPath)) {
      res.writeHead(200, { 'Content-Type': 'application/javascript' });
      return fs.createReadStream(chunkPath).pipe(res);
    }
  }

  // 4. Check if Next.js image optimizer request (?url=...) matches local public files
  if (pathname === '/_next/image' && parsedUrl.query && parsedUrl.query.url) {
    const assetRelative = parsedUrl.query.url.replace(/^\//, '');
    const localPublicPath = path.join(__dirname, 'public', assetRelative);
    if (fs.existsSync(localPublicPath)) {
      const ext = path.extname(localPublicPath).toLowerCase();
      res.writeHead(200, { 'Content-Type': MIME_TYPES[ext] || 'image/webp', 'Cache-Control': 'public, max-age=31536000' });
      return fs.createReadStream(localPublicPath).pipe(res);
    }
  }

  // 5. Check direct public file requests (e.g. /burgers/1b.png, /img-webp/..., /img/...)
  const directPublicPath = path.join(__dirname, 'public', pathname.replace(/^\//, ''));
  if (fs.existsSync(directPublicPath) && fs.statSync(directPublicPath).isFile()) {
    const ext = path.extname(directPublicPath).toLowerCase();
    res.writeHead(200, { 'Content-Type': MIME_TYPES[ext] || 'application/octet-stream', 'Cache-Control': 'public, max-age=31536000' });
    return fs.createReadStream(directPublicPath).pipe(res);
  }

  // 6. Manifest
  if (pathname === '/manifest.webmanifest' && fs.existsSync(path.join(__dirname, 'manifest.webmanifest'))) {
    res.writeHead(200, { 'Content-Type': 'application/manifest+json' });
    return fs.createReadStream(path.join(__dirname, 'manifest.webmanifest')).pipe(res);
  }

  // 7. Proxy fallback for remaining remote assets (e.g. fonts, etc.)
  const remoteUrl = REMOTE_ORIGIN + req.url;
  const proxyReq = https.request(remoteUrl, {
    method: req.method,
    headers: {
      ...req.headers,
      host: 'www.cravburgers.shop',
      referer: 'https://www.cravburgers.shop/'
    }
  }, (proxyRes) => {
    res.writeHead(proxyRes.statusCode, proxyRes.headers);
    proxyRes.pipe(res);
  });

  proxyReq.on('error', (err) => {
    console.error(`Proxy error for ${req.url}:`, err.message);
    res.writeHead(502);
    res.end('Proxy Error');
  });

  req.pipe(proxyReq);
});

server.listen(PORT, () => {
  console.log(`Cortina Ice Cream server running at http://localhost:${PORT}`);
});
