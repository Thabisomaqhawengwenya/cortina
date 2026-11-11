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

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url);
  const pathname = parsedUrl.pathname;

  // 1. Check if it's one of our main pages
  if (ROUTES[pathname]) {
    const filePath = path.join(__dirname, ROUTES[pathname]);
    if (fs.existsSync(filePath)) {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      return fs.createReadStream(filePath).pipe(res);
    }
  }

  // 2. Check local files in chunks or root
  if (pathname.startsWith('/_next/static/chunks/')) {
    const filename = path.basename(pathname);
    // Check if css or js is local
    if (filename === '0ovftnp3y9gzb.css' && fs.existsSync(path.join(__dirname, 'style1.css'))) {
      res.writeHead(200, { 'Content-Type': 'text/css' });
      return fs.createReadStream(path.join(__dirname, 'style1.css')).pipe(res);
    }
    if (filename === '05n9.pfd~lr39.css' && fs.existsSync(path.join(__dirname, 'style2.css'))) {
      res.writeHead(200, { 'Content-Type': 'text/css' });
      return fs.createReadStream(path.join(__dirname, 'style2.css')).pipe(res);
    }
    const chunkPath = path.join(__dirname, 'chunks', filename);
    if (fs.existsSync(chunkPath)) {
      res.writeHead(200, { 'Content-Type': 'application/javascript' });
      return fs.createReadStream(chunkPath).pipe(res);
    }
  }

  // 3. Proxy all other assets (images, fonts, api, remaining next assets) to live site
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
  console.log(`CRAV Burgers local server running at http://localhost:${PORT}`);
});
