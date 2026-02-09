// Dual landing page backend
// Run with: node server.js

const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;

// Store emails by campaign
const emailStore = {
    "workspace": [],    // G-Suite Audit
    "dental": []       // Dental Recall
};

// MIME types
const mimeTypes = {
    '.html': 'text/html',
    '.js': 'application/javascript',
    '.css': 'text/css',
    '.json': 'application/json',
    '.xml': 'application/rss+xml',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
};

// RSS Feed templates
const rssTemplates = {
    workspace: `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Gaudi.io Updates</title>
    <link>https://gaudit.io</link>
    <description>G-Suite Audit Tool Updates</description>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    <item>
      <title>G-Suite Audit Tool Launched</title>
      <link>https://gaudit.io</link>
      <description>Automated Google Workspace security audits.</description>
    </item>
  </channel>
</rss>`,
    dental: `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>DentalRecall.io Updates</title>
    <link>https://dentalrecall.io</link>
    <description>Dental Recall Automation Updates</description>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    <item>
      <title>Dental Recall Automation Launched</title>
      <link>https://dentalrecall.io</link>
      <description>Simple, affordable, HIPAA compliant recall automation.</description>
    </item>
  </channel>
</rss>`
};

const server = http.createServer((req, res) => {
    // CORS
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    if (req.method === 'OPTIONS') {
        res.writeHead(204);
        res.end();
        return;
    }

    // Parse URL
    const url = new URL(req.url, `http://localhost:${PORT}`);
    const pathname = url.pathname;

    // API: Handle signup (POST /api/signup?campaign=workspace|dental)
    if (req.method === 'POST' && pathname === '/api/signup') {
        const campaign = url.searchParams.get('campaign') || 'workspace';
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', () => {
            try {
                const { email } = JSON.parse(body);
                if (email && email.includes('@')) {
                    if (!emailStore[campaign]) emailStore[campaign] = [];
                    emailStore[campaign].push({ email, date: new Date().toISOString() });
                    console.log(`📧 New signup [${campaign}]: ${email}`);
                    res.writeHead(200, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify({ success: true, message: 'Thanks!' }));
                } else {
                    res.writeHead(400, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify({ error: 'Invalid email' }));
                }
            } catch (e) {
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Server error' }));
            }
        });
        return;
    }

    // API: Get all signups (GET /api/signups?campaign=workspace|dental)
    if (req.method === 'GET' && pathname === '/api/signups') {
        const campaign = url.searchParams.get('campaign');
        let result;
        if (campaign && emailStore[campaign]) {
            result = emailStore[campaign];
        } else {
            result = emailStore;
        }
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(result, null, 2));
        return;
    }

    // RSS Feeds (for IFTTT automation)
    if (req.method === 'GET' && pathname === '/feed.xml') {
        res.writeHead(200, { 'Content-Type': 'application/rss+xml' });
        res.end(rssTemplates.workspace);
        return;
    }
    if (req.method === 'GET' && pathname === '/dental/feed.xml') {
        res.writeHead(200, { 'Content-Type': 'application/rss+xml' });
        res.end(rssTemplates.dental);
        return;
    }

    // Serve landing pages - determine file path
    let filePath = pathname;
    
    if (filePath === '/' || filePath === '/index.html') {
        filePath = '/workspace-audit-landing.html';
    } else if (filePath === '/dental') {
        filePath = '/dental-recall-landing.html';
    }
    
    // Resolve to absolute path
    filePath = path.join(__dirname, filePath);
    const ext = path.extname(filePath);
    const contentType = mimeTypes[ext] || 'text/plain';

    fs.readFile(filePath, (err, content) => {
        if (err) {
            res.writeHead(404);
            res.end('Not found');
        } else {
            res.writeHead(200, { 'Content-Type': contentType });
            res.end(content);
        }
    });
});

server.listen(PORT, () => {
    console.log(`
🚀 CLAWD LANDING PAGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Server running at: http://localhost:${PORT}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Landing Pages:
  /             → G-Suite Audit
  /dental       → Dental Recall
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
API Endpoints:
  POST /api/signup?campaign=workspace|dental
  GET  /api/signups?campaign=workspace|dental
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    `);
});
