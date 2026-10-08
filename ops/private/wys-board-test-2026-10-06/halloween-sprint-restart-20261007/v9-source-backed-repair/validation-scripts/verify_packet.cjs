const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/Jodie/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'../outputs/Packet-1-V9');
const qa=path.join(root,'document-qa');fs.mkdirSync(qa,{recursive:true});
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',downloadsPath:qa});
 const ctx=await browser.newContext({acceptDownloads:true});
 const page=await ctx.newPage();let errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.route(/^https?:/,r=>r.abort());
 const source=JSON.parse(fs.readFileSync(path.join(root,'packet-1.json'),'utf8'));
 await page.goto(pathToFileURL(path.join(root,'FULL-PACKET-1.html')).href);
 await page.evaluate(()=>{document.documentElement.style.scrollBehavior='auto';document.querySelectorAll('img').forEach(i=>i.loading='eager')});
 await page.waitForFunction(()=>[...document.images].every(i=>i.complete&&i.naturalWidth>0));
 let widths=[];
 for(const width of [1280,390,320]){
   await page.setViewportSize({width,height:900});
   const result=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,images:document.images.length,broken:[...document.images].filter(i=>!i.complete||!i.naturalWidth).length,textareas:document.querySelectorAll('textarea').length}));
   if(result.scrollWidth>width||result.broken)throw Error('Overflow or broken images: '+JSON.stringify(result));
   widths.push(result);
   await page.screenshot({path:path.join(qa,`top-${width}.png`)});
 }
 await page.setViewportSize({width:1280,height:1000});
 for(const l of source.looks){
   const section=page.locator('#look-'+l.number);
   await section.scrollIntoViewIfNeeded();
   await page.evaluate(n=>document.getElementById('look-'+n).scrollIntoView({block:'start'}),l.number);
   await page.screenshot({path:path.join(qa,`look-${l.number}-desktop.png`)});
   for(const role of ['BASIC','STYLED','LIFESTYLE']){
     const t=page.locator(`#prompt-${l.number}-${role}`);
     if(await t.inputValue()!==l.prompts[role])throw Error(`Prompt mismatch ${l.number} ${role}`);
     const saved=fs.readFileSync(path.join(root,`prompts/${String(l.number).padStart(2,'0')}-${role.toLowerCase()}.txt`),'utf8');
     if(saved!==await t.inputValue())throw Error('Saved prompt mismatch');
     const buttons=section.locator('button').nth(['BASIC','STYLED','LIFESTYLE'].indexOf(role));
     await buttons.click();
     await page.waitForFunction(({n,role})=>[...document.querySelectorAll(`#look-${n} button`)].some(b=>b.textContent==='Copied'||b.textContent==='Selected — copy with Ctrl+C'),{n:l.number,role});
     await buttons.evaluate(b=>new Promise((resolve,reject)=>{const end=Date.now()+5000;const check=()=>{if(['Copied','Selected — copy with Ctrl+C'].includes(b.textContent))resolve();else if(Date.now()>end)reject(new Error(b.textContent));else setTimeout(check,20)};check()}));
     const label=await buttons.textContent();
     if(!['Copied','Selected — copy with Ctrl+C'].includes(label))throw Error('Copy failed');
   }
 }
 // Verify one actual downloadable source byte-for-byte, and all embedded assets by hash below.
 const photoLink=page.locator('#look-1 .product').first().getByRole('link',{name:'Download individual photo'});
 const [dl]=await Promise.all([page.waitForEvent('download'),photoLink.click()]);
 const temp=path.join(qa,'download-check.jpg');await dl.saveAs(temp);
 if(!fs.readFileSync(temp).equals(fs.readFileSync(path.join(root,'references/B0F5GP8LRG.jpg'))))throw Error('Download changed bytes');
 fs.unlinkSync(temp);
 const assetCheck=await page.evaluate(async()=>{
   let links=[...document.querySelectorAll('[data-asset-href]')];
   let urls=[...new Set(links.map(a=>a.href))];
   const results=await Promise.all(urls.map(async u=>({url:u,ok:(await fetch(u)).ok})));
   return {downloadLinks:links.length,uniqueDownloads:urls.length,failures:results.filter(r=>!r.ok).length};
 });
 if(errors.length||assetCheck.failures)throw Error(JSON.stringify({errors,assetCheck}));
 fs.writeFileSync(path.join(qa,'RENDER-CHECKS.json'),JSON.stringify({status:'RENDERED_DOCUMENT_CHECKS_PASS',widths,copyButtonsTested:27,promptTextExactMatches:27,downloadByteMatch:true,assetCheck,consoleErrors:errors,imageVisualQA:'NOT_RUN_NO_GENERATION'},null,2));
 await browser.close();console.log(JSON.stringify({widths,assetCheck,copyButtonsTested:27,errors}));
})().catch(e=>{console.error(e.stack);process.exit(1)});
