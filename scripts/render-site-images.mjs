// Renders the site's raster images into site/static/ with Playwright, from the drawings in site/:
// - og-pt.png, og-en.png: the link-preview cards (site/og-card.html), 1200x630;
// - favicon.ico (16, 32 and 48 px, what browsers ask for at /favicon.ico; Google wants a multiple
//   of 48 px), apple-touch-icon.png (180 px, iPhone home screen), icon-192.png and icon-512.png
//   (site.webmanifest, Android), all from site/static/icon.svg.
// Only needed when the mascot, the icon or the hero sentence changes.
// Usage: node scripts/render-site-images.mjs   (from the repo root; needs the playwright package)
import { createRequire } from 'node:module';
import { writeFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

// require, not import: it also finds a Playwright installed globally (NODE_PATH).
const { chromium } = createRequire(import.meta.url)('playwright');

const site = (p) => pathToFileURL(resolve('site', p)).href;
const out = (p) => `site/static/${p}`;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });

for (const lang of ['pt', 'en']) {
  await page.goto(site('og-card.html') + (lang === 'en' ? '?lang=en' : ''));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: out(`og-${lang}.png`) });
}

// The icon at a size, on a background (null = transparent) and filling a share of the square.
async function icon(size, background, share) {
  await page.setViewportSize({ width: size, height: size });
  const px = Math.round(size * share);
  await page.setContent(`<body style="margin:0;width:${size}px;height:${size}px;display:grid;place-items:center;background:${background ?? 'transparent'}">
    <img src="${site('static/icon.svg')}" style="width:${px}px;height:${px}px"></body>`);
  await page.waitForLoadState('load');
  return page.screenshot({ omitBackground: background === null });
}

// Home-screen icons get the page's background and room around the book: Android crops
// "maskable" icons to a circle, which keeps only the middle 80 %.
writeFileSync(out('apple-touch-icon.png'), await icon(180, '#fbfaf5', 0.76));
writeFileSync(out('icon-192.png'), await icon(192, '#fbfaf5', 0.62));
writeFileSync(out('icon-512.png'), await icon(512, '#fbfaf5', 0.62));

// favicon.ico: an ICO file holding PNGs (every browser since IE 11 reads them).
const sizes = [16, 32, 48];
const pngs = [];
for (const s of sizes) pngs.push(await icon(s, null, 1));
const header = Buffer.alloc(6 + 16 * sizes.length);
header.writeUInt16LE(0, 0); header.writeUInt16LE(1, 2); header.writeUInt16LE(sizes.length, 4);
let offset = header.length;
sizes.forEach((s, i) => {
  const e = 6 + 16 * i;
  header.writeUInt8(s, e); header.writeUInt8(s, e + 1); header.writeUInt8(0, e + 2); header.writeUInt8(0, e + 3);
  header.writeUInt16LE(1, e + 4); header.writeUInt16LE(32, e + 6);
  header.writeUInt32LE(pngs[i].length, e + 8); header.writeUInt32LE(offset, e + 12);
  offset += pngs[i].length;
});
writeFileSync(out('favicon.ico'), Buffer.concat([header, ...pngs]));

await browser.close();
console.log('wrote site/static/: og-pt.png, og-en.png, favicon.ico, apple-touch-icon.png, icon-192.png, icon-512.png');
