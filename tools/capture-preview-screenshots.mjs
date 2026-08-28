import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const port = Number(process.env.CDP_PORT || 9333);
const baseUrl = process.argv[2];
const outputDirectory = process.argv[3] || 'docs/screenshots';

if (!baseUrl) {
  throw new Error('Usage: node tools/capture-preview-screenshots.mjs <base-url> [output-directory]');
}

const targets = [
  ['en', '/', 1440, 1100, false],
  ['en', '/', 390, 844, true],
  ['ro', '/ro/', 1440, 1100, false],
  ['ro', '/ro/', 390, 844, true],
  ['ru', '/ru/', 1440, 1100, false],
  ['ru', '/ru/', 390, 844, true],
];

const delay = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));

async function capture([language, pathname, width, height, mobile]) {
  const createUrl = `http://127.0.0.1:${port}/json/new?${encodeURIComponent(new URL(pathname, baseUrl).href)}`;
  const page = await fetch(createUrl, { method: 'PUT' }).then((response) => {
    if (!response.ok) throw new Error(`Could not create browser page: ${response.status}`);
    return response.json();
  });

  const socket = new WebSocket(page.webSocketDebuggerUrl);
  const pending = new Map();
  let commandId = 0;

  const opened = new Promise((resolve, reject) => {
    socket.addEventListener('open', resolve, { once: true });
    socket.addEventListener('error', reject, { once: true });
  });

  socket.addEventListener('message', (event) => {
    const message = JSON.parse(event.data);
    if (!message.id || !pending.has(message.id)) return;
    const { resolve, reject } = pending.get(message.id);
    pending.delete(message.id);
    if (message.error) reject(new Error(message.error.message));
    else resolve(message.result);
  });

  await opened;

  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const id = ++commandId;
    pending.set(id, { resolve, reject });
    socket.send(JSON.stringify({ id, method, params }));
  });

  try {
    await send('Page.enable');
    await send('Emulation.setDeviceMetricsOverride', {
      width,
      height,
      deviceScaleFactor: 1,
      mobile,
      screenWidth: width,
      screenHeight: height,
    });
    if (mobile) {
      await send('Network.setUserAgentOverride', {
        userAgent: 'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
      });
    }
    await send('Page.navigate', { url: new URL(pathname, baseUrl).href });
    await delay(2500);
    const { data } = await send('Page.captureScreenshot', {
      format: 'png',
      fromSurface: true,
      captureBeyondViewport: false,
    });
    const viewport = mobile ? 'mobile' : 'desktop';
    const outputPath = path.join(outputDirectory, `preview-${language}-${viewport}.png`);
    await writeFile(outputPath, Buffer.from(data, 'base64'));
    console.log(`${outputPath}\t${width}x${height}`);
  } finally {
    socket.close();
    await fetch(`http://127.0.0.1:${port}/json/close/${page.id}`, { method: 'PUT' }).catch(() => {});
  }
}

await mkdir(outputDirectory, { recursive: true });
for (const target of targets) await capture(target);
