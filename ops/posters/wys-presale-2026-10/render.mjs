// Renders poster.html to the Facebook (1080x1350) and Skool (full height) PNGs at 2x.
// Usage: node render.mjs   (needs the `playwright` package; set CHROMIUM_PATH to use a preinstalled browser)
import { chromium } from 'playwright';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});

for (const [mode, file] of [['fb', 'WYS_Presale_Poster_Facebook.png'], ['skool', 'WYS_Presale_Poster_Skool.png']]) {
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await page.goto(pathToFileURL(path.join(dir, 'poster.html')).href);
  await page.evaluate((m) => { document.body.className = m; }, mode);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const info = await page.evaluate(() => {
    const poster = document.querySelector('.poster');
    const last = document.querySelector('.phrase').getBoundingClientRect();
    const bar = document.querySelector('.bar').getBoundingClientRect();
    const clipped = [];
    document.querySelectorAll('.poster *').forEach((e) => {
      if (e.closest('.shot') || e.closest('.phone')) return;
      if (e.scrollWidth > e.clientWidth + 1 && getComputedStyle(e).overflow !== 'visible') clipped.push(e.className);
    });
    return {
      height: poster.scrollHeight,
      contentBottom: Math.round(last.bottom),
      barTop: Math.round(bar.top),
      fonts: [...document.fonts].map((f) => `${f.family}:${f.status}`),
      clipped,
      docWidth: document.documentElement.scrollWidth,
    };
  });
  console.log(mode, JSON.stringify(info));
  await page.screenshot({
    path: path.join(dir, file),
    fullPage: mode === 'skool',
    clip: mode === 'fb' ? { x: 0, y: 0, width: 1080, height: 1350 } : undefined,
  });
  await page.close();
}
await browser.close();
