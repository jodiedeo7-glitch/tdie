#!/usr/bin/env node
/**
 * Create an exact-photo editorial promotional flyer from a JSON manifest.
 * Usage: node ops/visual-qa/flyer.mjs input.json output.html
 * Then: node ops/visual-qa/audit.mjs --flyer output.html
 * Input fields: title, headline, tagline, subtitle, steps[], metrics:[{value,label}], photos:[{path,label}], width,height,background,accent.
 * Images are embedded byte-for-byte as data URLs; no AI regeneration/cropping.
 */
import { readFile, writeFile } from 'node:fs/promises';
import { resolve, extname, dirname } from 'node:path';
import { pathToFileURL } from 'node:url';
const [input, output] = process.argv.slice(2);
if (!input || !output) { console.error('Usage: node ops/visual-qa/flyer.mjs input.json output.html'); process.exit(2); }
const manifest=JSON.parse(await readFile(resolve(input),'utf8'));
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const width=Number(manifest.width||1080), height=Number(manifest.height||1350);
if(width<300||height<400||width>4000||height>8000)throw Error('Invalid dimensions');
if(!manifest.title||!Array.isArray(manifest.photos)||!manifest.photos.length)throw Error('title and photos required');
const photos=[];
for(const p of manifest.photos){
 const f=resolve(dirname(resolve(input)),p.path);
 const ext=extname(f).toLowerCase();
 const mime={'.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.webp':'image/webp'}[ext];
 if(!mime)throw Error('Unsupported photo type: '+ext);
 const bytes=await readFile(f);
 photos.push({label:esc(p.label),data:'data:'+mime+';base64,'+bytes.toString('base64')});
}
const bg=/^#[0-9a-f]{6}$/i.test(manifest.background)?manifest.background:'#202426';
const accent=/^#[0-9a-f]{6}$/i.test(manifest.accent)?manifest.accent:'#C8B89A';
const steps=(manifest.steps||[]).map((s,i)=>'<div class="step"><span class="num">'+String(i+1).padStart(2,'0')+'</span><span>'+esc(s)+'</span></div>').join('');
const metrics=(manifest.metrics||[]).map(m=>'<div class="metric"><strong>'+esc(m.value)+'</strong><span>'+esc(m.label)+'</span></div>').join('');
const cards=photos.map(p=>'<figure><div class="photo"><img src="'+p.data+'" alt="'+p.label+'"></div><figcaption>'+p.label+'</figcaption></figure>').join('');
const html=`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(manifest.title)}</title><style>
*{box-sizing:border-box}html,body{margin:0}body{width:${width}px;height:${height}px;overflow:hidden;background:${bg};color:#f5f2ec;font-family:Arial,Helvetica,sans-serif}main{width:100%;height:100%;padding:5.2%;display:flex;flex-direction:column;gap:3.3%;}.eyebrow{font-size:17px;letter-spacing:.22em;text-transform:uppercase;color:${accent};font-weight:700}.title{font-family:Georgia,'Times New Roman',serif;font-weight:400;letter-spacing:-.035em;font-size:clamp(42px,5.5vw,70px);line-height:1.03;margin:0;max-width:100%}.headline{font-size:25px;line-height:1.35;margin:0;max-width:850px}.tagline{font-size:21px;letter-spacing:.02em;margin:0;color:#d8d5ce}.rule{height:1px;background:${accent};opacity:.6;flex:none}.steps{display:flex;justify-content:space-between;gap:24px}.step{flex:1;display:flex;align-items:center;gap:13px;font-size:20px;line-height:1.2}.num{font-size:24px;font-family:Georgia,serif;color:${accent}}.metrics{display:flex;justify-content:space-between;gap:18px}.metric{flex:1;display:flex;flex-direction:column;gap:7px}.metric strong{font:normal 52px Georgia,serif;color:${accent}}.metric span{font-size:17px;line-height:1.2}.photos{display:grid;grid-template-columns:repeat(${photos.length},minmax(0,1fr));gap:12px;min-height:0;flex:1;align-items:stretch}.photos figure{min-width:0;margin:0;display:flex;flex-direction:column;gap:12px}.photo{flex:1;min-height:0;border:1px solid #555;display:flex;align-items:center;justify-content:center;background:#16191a;padding:5px}.photo img{width:100%;height:100%;object-fit:contain;display:block}.photos figcaption{text-align:center;font-size:16px;letter-spacing:.08em;text-transform:uppercase;color:${accent}}.sectiontitle{font:normal 29px Georgia,serif;margin:0}.spacer{flex:0 0 0}
</style></head><body><main><div class="eyebrow">${esc(manifest.eyebrow||'THE DIGITAL INCOME EDIT™')}</div><h1 class="title">${esc(manifest.title)}</h1>${manifest.headline?'<p class="headline">'+esc(manifest.headline)+'</p>':''}${manifest.subtitle?'<p class="tagline">'+esc(manifest.subtitle)+'</p>':''}<div class="rule"></div>${steps?'<div class="steps">'+steps+'</div>':''}${metrics?'<div class="metrics">'+metrics+'</div>':''}<h2 class="sectiontitle">${esc(manifest.photoHeading||'A real look it created')}</h2><div class="photos">${cards}</div>${manifest.tagline?'<p class="tagline">'+esc(manifest.tagline)+'</p>':''}</main></body></html>`;
await writeFile(resolve(output),html,'utf8');
console.log(resolve(output));
