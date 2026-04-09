#!/usr/bin/env node

/**
 * Vigil Site Crawler — rewrites website.json by crawling every linked page
 * Usage: node crawl-site.js
 * Run from: v3/rise/mkt/
 */

const https = require('https');
const http = require('http');

const BASE_URL = 'https://hoarhouse.github.io/v3/rise';
const OUTPUT_FILE = __dirname + '/website.json';
const DELAY_MS = 800;

function fetch(url) {
  return new Promise((resolve, reject) => {
    const mod = url.startsWith('https') ? https : http;
    mod.get(url, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

function extractLinks(html, currentPath) {
  const links = [];
  const regex = /href=["']([^"'#?]+\.html)["']/gi;
  let match;
  while ((match = regex.exec(html)) !== null) {
    let href = match[1];
    // Skip external links and mkt/ pages (those are Vigil itself)
    if (href.startsWith('http') || href.includes('mkt/')) continue;
    // Resolve relative to current path
    if (!href.startsWith('/')) {
      const dir = currentPath.substring(0, currentPath.lastIndexOf('/') + 1);
      href = dir + href;
    }
    // Normalise
    href = href.replace(/\/\.\//g, '/').replace(/[^/]+\/\.\.\//g, '');
    if (!href.startsWith('/v3/rise/')) href = '/v3/rise/' + href.replace(/^\//, '');
    links.push(href);
  }
  return [...new Set(links)];
}

function extractText(html) {
  // Remove script, style, nav, header blocks
  let text = html
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<style[\s\S]*?<\/style>/gi, '')
    .replace(/<nav[\s\S]*?<\/nav>/gi, '')
    .replace(/<header[\s\S]*?<\/header>/gi, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&nbsp;/g, ' ')
    .replace(/&#\d+;/g, ' ')
    .replace(/\s{2,}/g, ' ')
    .trim();
  return text.substring(0, 4000);
}

function extractTitle(html) {
  const m = html.match(/<title>([^<]+)<\/title>/i);
  return m ? m[1].trim() : '';
}

function extractMeta(html) {
  const products = [];
  const clients = [];
  const productPatterns = ['Rise', 'Essence', 'COIOS', 'FedX', 'MyD', 'CORPEX', 'ProofX', 'SpadaX', 'GENESIS', 'GraDPaLM', 'HeliX', 'DOME', 'KAU'];
  const clientPatterns = ['MAVIR', 'ESA', 'European Space Agency', 'Kellton', 'Hungarian Government', 'MVM', '4iG'];
  productPatterns.forEach(p => { if (html.includes(p)) products.push(p); });
  clientPatterns.forEach(c => { if (html.includes(c)) clients.push(c); });
  return { products, clients };
}

async function crawl() {
  console.log('Vigil Site Crawler starting...');
  const visited = new Set();
  const queue = ['/v3/rise/index.html'];
  const pages = [];

  while (queue.length > 0) {
    const path = queue.shift();
    if (visited.has(path)) continue;
    visited.add(path);

    const url = 'https://hoarhouse.github.io' + path;
    console.log('Crawling: ' + url);

    try {
      const html = await fetch(url);
      if (html.includes('404') && html.includes('not found')) {
        console.log('  -> 404 skipped');
        continue;
      }

      const title = extractTitle(html);
      const text = extractText(html);
      const meta = extractMeta(html);
      const links = extractLinks(html, path);

      // Derive filename relative to rise/
      const filename = path.replace('/v3/rise/', '');

      pages.push({
        id: filename.replace(/[^a-zA-Z0-9]/g, '-').replace(/-+/g, '-'),
        url: filename,
        title,
        purpose: '',
        currentContent: text,
        productsMentioned: meta.products,
        clientsMentioned: meta.clients,
        missing: []
      });

      console.log('  -> OK: "' + title + '" | products: ' + meta.products.join(', ') + ' | links found: ' + links.length);

      // Add new links to queue
      links.forEach(link => {
        if (!visited.has(link) && !queue.includes(link)) {
          queue.push(link);
        }
      });

      await sleep(DELAY_MS);
    } catch (e) {
      console.log('  -> Error: ' + e.message);
    }
  }

  const output = {
    lastAudited: new Date().toISOString().split('T')[0],
    url: BASE_URL,
    crawledPages: pages.length,
    pages,
    globalGaps: [],
    priorityUpdates: []
  };

  require('fs').writeFileSync(OUTPUT_FILE, JSON.stringify(output, null, 2));
  console.log('\nDone. Crawled ' + pages.length + ' pages -> website.json updated.');
  console.log('Pages found:');
  pages.forEach(p => console.log('  ' + p.url + ' — ' + p.title));
}

crawl().catch(console.error);