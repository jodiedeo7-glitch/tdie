import { chromium } from '/tmp/claude-0/-home-user-tdie/3a1419de-0e28-595d-bfd1-8c080dec4ee8/scratchpad/pw/node_modules/playwright/index.mjs';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell'});
for (const [mode,file] of [['fb','WYS_Presale_Poster_Facebook.png'],['skool','WYS_Presale_Poster_Skool.png']]) {
  const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});
  await p.goto('file://./poster.html');
  await p.evaluate(m=>document.body.className=m, mode);
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(300);
  const info=await p.evaluate(()=>{
    const r=[];const P=document.querySelector('.poster');
    document.querySelectorAll('.poster *').forEach(e=>{ if(e.scrollWidth>e.clientWidth+1 && getComputedStyle(e).overflow!=='visible' && !e.classList.contains('shot')) r.push('hscroll '+e.className);});
    const bar=document.querySelector('.bar').getBoundingClientRect(), steps=document.querySelector('.steps').getBoundingClientRect(), body=document.querySelector('.body-grid').getBoundingClientRect(), phr=document.querySelector('.phrase').getBoundingClientRect();
    const fonts=[...document.fonts].map(f=>f.family+':'+f.status);
    return {h:P.scrollHeight, stepsBottom:steps.bottom, barTop:bar.top, bodyBottom:body.bottom, phraseTop:phr.top, fonts, r, docW:document.documentElement.scrollWidth};
  });
  console.log(mode, JSON.stringify(info));
  await p.screenshot({path:'./'+file, fullPage: mode==='skool', clip: mode==='fb'?{x:0,y:0,width:1080,height:1350}:undefined});
  await p.close();
}
await b.close();
