import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, join, normalize, resolve, sep } from 'node:path';

const root = resolve(process.cwd());
const port = Number(process.env.CF_SITE_PORT || 8765);
const types = {
  '.css': 'text/css; charset=utf-8', '.html': 'text/html; charset=utf-8', '.ico': 'image/x-icon',
  '.jpeg': 'image/jpeg', '.jpg': 'image/jpeg', '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.mp4': 'video/mp4', '.png': 'image/png',
  '.svg': 'image/svg+xml', '.webm': 'video/webm', '.webp': 'image/webp', '.xml': 'application/xml; charset=utf-8',
};

function candidates(pathname) {
  const clean = decodeURIComponent(pathname).replace(/\\/g, '/');
  if (clean === '/') return ['index.html'];
  const relative = normalize(clean.replace(/^\/+/, ''));
  if (extname(relative)) return [relative];
  if (clean.endsWith('/')) return [join(relative, 'index.html')];
  return [relative, `${relative}.html`, join(relative, 'index.html')];
}

async function resolveFile(pathname) {
  for (const candidate of candidates(pathname)) {
    const file = resolve(root, candidate);
    if (file !== root && !file.startsWith(root + sep)) continue;
    try {
      if ((await stat(file)).isFile()) return file;
    } catch {}
  }
  return null;
}

createServer(async (request, response) => {
  const pathname = new URL(request.url, 'http://localhost').pathname;
  const file = await resolveFile(pathname);
  if (!file) {
    response.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' });
    response.end('Not found');
    return;
  }
  const body = await readFile(file);
  response.writeHead(200, { 'content-type': types[extname(file).toLowerCase()] || 'application/octet-stream' });
  response.end(body);
}).listen(port, '127.0.0.1', () => {
  process.stdout.write(`Camelot Flows local server: http://127.0.0.1:${port}\n`);
});
