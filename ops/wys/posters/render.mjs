// Renders the WYS presale posters at 2x as JPG quality 93.
// Usage: node ops/wys/posters/render.mjs [outDir]
// (set PLAYWRIGHT_MODULE to a playwright index.mjs path if it isn't installed locally)
const {chromium} = await import(process.env.PLAYWRIGHT_MODULE || 'playwright');
import {fileURLToPath, pathToFileURL} from 'node:url';
import path from 'node:path';
const here = path.dirname(fileURLToPath(import.meta.url));
const out = process.argv[2] || here;
const page = pathToFileURL(path.join(here, 'poster.html')).href;
const browser = await chromium.launch();
for (const [size, w, h, name] of [['fb', 1080, 1350, 'wys-presale-facebook-1080x1350@2x.jpg'], ['skool', 1600, 900, 'wys-presale-skool-1600x900@2x.jpg']]) {
 const ctx = await browser.newContext({viewport: {width: w, height: h}, deviceScaleFactor: 2});
 const p = await ctx.newPage();
 await p.goto(`${page}?size=${size}`, {waitUntil: 'networkidle'});
 await p.evaluate(() => document.fonts.ready);
 await p.waitForTimeout(400);
 await p.screenshot({path: path.join(out, name), type: 'jpeg', quality: 93, clip: {x: 0, y: 0, width: w, height: h}});
 const over = await p.evaluate(() => [...document.querySelectorAll('.poster:not([hidden]) *')].filter((e) => {if (e.closest('.screen')) return false; const r = e.getBoundingClientRect(); return r.width && (r.right > innerWidth + 1 || r.bottom > innerHeight + 1);}).map((e) => e.className || e.tagName).slice(0, 5));
 console.log(name, over.length ? 'OVERFLOW: ' + over.join(',') : 'fits');
 await ctx.close();
}
await browser.close();
