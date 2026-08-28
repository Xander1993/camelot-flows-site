import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const inputs = [
  'assets/css/tailwind.built.css',
  'assets/site.min.css',
  'assets/css/camelot.min.css',
  'assets/css/theme-night.min.css',
  'assets/css/lang-switcher.css'
];
const chunks = await Promise.all(inputs.map((file) => readFile(path.join(root, file), 'utf8')));
await writeFile(path.join(root, 'assets/css/site.bundle.min.css'), chunks.join('\n'), 'utf8');
process.stdout.write(`Built assets/css/site.bundle.min.css from ${inputs.length} ordered inputs.\n`);
