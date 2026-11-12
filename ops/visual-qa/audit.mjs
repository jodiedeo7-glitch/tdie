#!/usr/bin/env node
/**
 * TDIE visual QA: website screenshots + promotional flyer rendering and objective checks.
 * Install: npm install --no-save playwright && npx playwright install chromium
 * Run: node ops/visual-qa/audit.mjs --site https://www.thedigitalincomeedit.com --out visual-qa-output
 * Flyer: node ops/visual-qa/audit.mjs --flyer ./flyer.html --out visual-qa-output
 * This is a deterministic QA foundation, NOT an autonomous aesthetic judge.
 */
import { chromium } from 'playwright';
import { mkdir, writeFile } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const arg = (name, fallback) => { const i = args.indexOf(name); return i < 0 ? fallback : args[i + 1]; };
const site = arg('--site', null), flyer = arg('--flyer', null);
const out = resolve(arg('--out', 'visual-qa-output'));
if (!site && !flyer) { console.error('Specify --site URL or --flyer HTML file'); process.exit(2); }
await mkdir(out, { recursive: true });
const browser = await chromium.launch({ headless: true });
const results = [];
const targets = site
  ? [{ label:'desktop',width:1440,height:900 },{label:'mobile390',width:390,height:844},{label:'mobile320',width:320,height:700}]
  : [{label:'flyer',width:1080,height:1350}];
try {
 for (const t of targets) {
  const page = await browser.newPage({viewport:{width:t.width,height:t.height},deviceScaleFactor:1});
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  const address = site || pathToFileURL(resolve(flyer)).href;
  await page.goto(address,{waitUntil:'networkidle',timeout:60000});
  await page.evaluate(()=>document.fonts.ready);
  const audit = await page.evaluate(() => {
   const visible = el => { const r=el.getBoundingClientRect(),s=getComputedStyle(el);return r.width>0&&r.height>0&&s.display!=='none'&&s.visibility!=='hidden'; };
   const elements = [...document.querySelectorAll('body *')].filter(visible);
   const overflow = document.documentElement.scrollWidth > innerWidth+1;
   const clipped = elements.filter(el=>{const r=el.getBoundingClientRect();return r.left < -2 || r.right > innerWidth+2;}).slice(0,30).map(el=>({tag:el.tagName,cls:String(el.className).slice(0,90),text:(el.textContent||'').trim().slice(0,70)}));
   const forbiddenPink = elements.filter(el=>{
    const c=getComputedStyle(el).backgroundColor;const m=c.match(/^rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)/);
    if(!m)return false;const [r,g,b]=m.slice(1).map(Number);
    return r>155 && r>g*1.35 && b>g*1.15 && (el.matches('button,a,[role=button],section,article,aside,header,footer,[class*=card],[class*=badge],[class*=pill],[class*=panel]'));
   }).slice(0,30).map(el=>({tag:el.tagName,cls:String(el.className).slice(0,90),background:getComputedStyle(el).backgroundColor}));
   const missingAlt=[...document.querySelectorAll('img')].filter(i=>!i.hasAttribute('alt')).map(i=>i.src).slice(0,30);
   const brokenImages=[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src).slice(0,30);
   const fonts=[...new Set(elements.filter(e=>e.matches('h1,h2,h3,p,button,a')).map(e=>getComputedStyle(e).fontFamily))].slice(0,20);
   const buttons=[...document.querySelectorAll('button,a,[role=button]')].filter(visible).filter(el=>el.getBoundingClientRect().height<44).slice(0,20).map(el=>(el.textContent||'').trim().slice(0,60));
   return {overflow,clipped,forbiddenPink,missingAlt,brokenImages,fonts,smallTargets:buttons,title:document.title};
  });
  const screenshot=resolve(out,t.label+'.png');
  await page.screenshot({path:screenshot,fullPage:true,animations:'disabled'});
  results.push({target:t.label,url:address,screenshot,audit,errors,pass:!audit.overflow&&!audit.clipped.length&&!audit.forbiddenPink.length&&!audit.brokenImages.length&&!errors.length});
  await page.close();
 }
} finally { await browser.close(); }
await writeFile(resolve(out,'report.json'),JSON.stringify({created:new Date().toISOString(),results},null,2));
console.log(JSON.stringify(results.map(({target,pass,audit,errors})=>({target,pass,overflow:audit.overflow,clipped:audit.clipped.length,pinkFills:audit.forbiddenPink.length,brokenImages:audit.brokenImages.length,errors})),null,2));
if(results.some(r=>!r.pass)) process.exitCode=1;
