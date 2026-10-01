// Render committed guide HTML; never regenerate it from an older template.
import {mkdirSync} from 'node:fs';
import {dirname,join} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
let chromium;
try {({chromium}=await import('playwright'));}
catch(error){if(!process.env.WYS_NODE_MODULES)throw error;({chromium}=createRequire(join(process.env.WYS_NODE_MODULES,'package.json'))('playwright'));}
const here=dirname(fileURLToPath(import.meta.url));
const out=join(here,'pdf'), checks=join(here,'tests','guide-render');
mkdirSync(checks,{recursive:true});
const browser=await chromium.launch({headless:true,...(process.env.WYS_CHROMIUM_PATH?{executablePath:process.env.WYS_CHROMIUM_PATH}:{})});
try {
 const page=await browser.newPage({viewport:{width:816,height:1056}});
 await page.goto(pathToFileURL(join(out,'While-You-Sleep-Storefront-Setup-Guide.html')).href,{waitUntil:'load'});
 await page.evaluate(()=>document.fonts.ready);
 const broken=await page.locator('img').evaluateAll(images=>images.filter(i=>!i.complete||!i.naturalWidth).map(i=>i.getAttribute('src')));
 if(broken.length)throw Error('Missing guide images: '+broken.join(', '));
 const sections=page.locator('.pg'),count=await sections.count();
 for(let i=0;i<count;i++)await sections.nth(i).screenshot({path:join(checks,'page-'+String(i+1).padStart(2,'0')+'.png')});
 const overflow=await sections.evaluateAll(pages=>pages.flatMap((pg,i)=>{
 const foot=pg.querySelector('.foot');if(!foot)return [];
 const bottom=foot.getBoundingClientRect().top;
 return [...pg.querySelectorAll('p,h2,h3,li,td')].filter(el=>!el.closest('.foot')&&el.getBoundingClientRect().bottom>bottom-4).map(el=>({page:i+1,text:el.textContent.slice(0,90)}));
 }));
 if(overflow.length)throw Error('Guide content overlaps footer: '+JSON.stringify(overflow));
 await page.pdf({path:join(out,'While-You-Sleep-Storefront-Setup-Guide.pdf'),printBackground:true,preferCSSPageSize:true});
 console.log('Rendered '+count+' pages; no broken images or footer overlaps.');
}finally{await browser.close();}
