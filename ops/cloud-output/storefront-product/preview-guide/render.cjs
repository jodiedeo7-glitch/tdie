const { chromium } = require('playwright');
const path=require('path'), fs=require('fs');
(async()=>{
  const dir=process.argv[2]; const out=process.argv[3]; fs.mkdirSync(out,{recursive:true});
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'}).catch(()=>chromium.launch());
  const p=await b.newPage({viewport:{width:1080,height:1440},deviceScaleFactor:1});
  await p.goto('file://'+path.resolve(dir,'index.html')); await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(500);
  const qa=await p.evaluate(()=>{
    const res=[];
    const fonts=[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+f.weight);
    res.push('fonts loaded: '+fonts.join(','));
    document.querySelectorAll('.page').forEach(pg=>{
      const pr=pg.getBoundingClientRect(); const foot=pg.querySelector('.foot').getBoundingClientRect();
      if(Math.round(pr.width)!==1080||Math.round(pr.height)!==1440) res.push(pg.id+' size '+pr.width+'x'+pr.height);
      pg.querySelectorAll('*').forEach(el=>{
        if(el.closest('svg')&&el.tagName!=='svg') return;
        const r=el.getBoundingClientRect(); if(!r.width) return;
        if(el.scrollWidth>el.clientWidth+1 && getComputedStyle(el).overflow!=='hidden' && el.clientWidth>0 && !el.matches('svg')) res.push(pg.id+' hscroll '+el.tagName+'.'+el.className+' '+el.textContent.trim().slice(0,40));
        if(r.right>pr.right+1||r.bottom>pr.bottom+1||r.left<pr.left-1) res.push(pg.id+' outside '+el.tagName+'.'+el.className+' '+el.textContent.trim().slice(0,30));
        if(!el.closest('.foot') && el.children.length===0 && el.textContent.trim() && r.bottom>foot.top-4 && r.top<foot.bottom) res.push(pg.id+' overlaps footer: '+el.textContent.trim().slice(0,40));
        const fs=parseFloat(getComputedStyle(el).fontSize); if(el.children.length===0&&el.textContent.trim()&&fs<18) res.push(pg.id+' small font '+fs+' '+el.textContent.trim().slice(0,30));
      });
      pg.querySelectorAll('.main .card,.main .frame,.main .callout,.main p,.main .btn').forEach(el=>{const r=el.getBoundingClientRect();if(r.bottom>foot.top-12)res.push(pg.id+' BOX NEAR FOOTER: '+el.className+' '+el.textContent.trim().slice(0,30)+' gap='+Math.round(foot.top-r.bottom));});
      // headline widows
      pg.querySelectorAll('h1 span, h2 span').forEach(s=>{
        const rg=document.createRange(); rg.selectNodeContents(s);
        const tops=[...new Set([...rg.getClientRects()].map(r=>Math.round(r.top)))];
        if(tops.length>1) res.push(pg.id+' headline line wraps: "'+s.textContent+'" lines='+tops.length);
      });
      // words of body copy
      const words=[...pg.querySelectorAll('p,figcaption,.chip,.callout,.sticker')].filter(e=>!e.querySelector('p')).map(e=>e.textContent).join(' ').split(/\s+/).filter(Boolean).length;
      res.push(pg.id+' text words(non-headline)='+words);
      // text vs text overlap among leaf text blocks
      const leaves=[...pg.querySelectorAll('p,h1,h2,.kicker,figcaption,.chip')].filter(e=>!e.closest('.foot'));
      for(let i=0;i<leaves.length;i++)for(let j=i+1;j<leaves.length;j++){const a=leaves[i].getBoundingClientRect(),c=leaves[j].getBoundingClientRect();
        if(leaves[i].contains(leaves[j])||leaves[j].contains(leaves[i]))continue;
        if(a.left<c.right&&c.left<a.right&&a.top<c.bottom&&c.top<a.bottom) res.push(pg.id+' TEXT OVERLAP: "'+leaves[i].textContent.trim().slice(0,25)+'" x "'+leaves[j].textContent.trim().slice(0,25)+'"');}
    });
    const t=document.body.innerText; if(/[—–]/.test(t)) res.push('DASH FOUND'); if(/\$|\d+\s*spots|Warmly/i.test(t)) res.push('PRICE/SPOTS/WARMLY FOUND');
    return res;
  });
  console.log(qa.join('\n'));
  const pages=await p.$$('.page');
  for(let i=0;i<pages.length;i++){await pages[i].screenshot({path:path.join(out,`wys-preview-guide-p${String(i+1).padStart(2,'0')}.png`)});}
  await p.pdf({path:path.join(out,'WYS-Free-Preview-Guide.pdf'),width:'1080px',height:'1440px',printBackground:true,preferCSSPageSize:true});
  await b.close();
})();
