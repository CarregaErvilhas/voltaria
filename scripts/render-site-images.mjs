// Renders the site's raster images into site/static/ with Playwright: the link-preview cards
// (og-pt.png, og-en.png, from site/og-card.html) and the iPhone home-screen icon (apple-touch-icon.png,
// from site/static/icon.svg). Only needed when the mascot or the hero sentence changes.
// Usage: node scripts/render-site-images.mjs   (from the repo root; needs the playwright package)
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

// require, not import: it also finds a Playwright installed globally (NODE_PATH).
const { chromium } = createRequire(import.meta.url)('playwright');

const site = (p) => pathToFileURL(resolve('site', p)).href;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
for (const lang of ['pt', 'en']) {
  await page.goto(site('og-card.html') + (lang === 'en' ? '?lang=en' : ''));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: `site/static/og-${lang}.png` });
}
await page.setViewportSize({ width: 180, height: 180 });
await page.setContent(`<body style="margin:0;background:#fbfaf5;display:grid;place-items:center;height:180px">
  <img src="${site('static/icon.svg')}" style="width:136px;height:136px"></body>`);
await page.waitForLoadState('load');
await page.screenshot({ path: 'site/static/apple-touch-icon.png' });
await browser.close();
console.log('wrote site/static/og-pt.png, og-en.png, apple-touch-icon.png');
