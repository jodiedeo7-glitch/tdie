# WYS preview guide built from the home page's own components (thedigitalincomeedit.com/), scaled ~1.45x for a 1080x1440 page.
import sys
W=sys.argv[1]
GL=open(W+'/glitter.txt').read().strip()
G1=GL.split(';--glitter2:')[0].replace('--glitter:','')
G2=GL.split(';--glitter2:')[1].rstrip(';')
CSS='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1080"><title>WYS Free Preview Guide</title><style>
@font-face{font-family:"Newsreader";src:url("type/newsreader-latin-600-normal.woff2") format("woff2");font-weight:600}
@font-face{font-family:"Inter";src:url("type/inter-latin-400-normal.woff2") format("woff2");font-weight:400}
@font-face{font-family:"Inter";src:url("type/inter-latin-600-normal.woff2") format("woff2");font-weight:600}
@font-face{font-family:"Inter";src:url("type/inter-latin-700-normal.woff2") format("woff2");font-weight:700}
@font-face{font-family:"Inter";src:url("type/inter-latin-800-normal.woff2") format("woff2");font-weight:800}
:root{--cream:#FFFBF8;--ink:#1A1417;--hot:#D62E73;--rose:#B8245F;--line:#E891B6;--kickline:#EAA2C0;--blush:#FFF5FA;--frame:#FFD7E9;--halo:#FFE3F0;--lavbg:#FBF7FF;--lavline:#C4AFE4;--gold:#C8A96A;--paper:#FFFCFE;--dash:#F3A9C8}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#fff}
body{font-family:Inter,sans-serif;color:var(--ink)}
@page{size:1080px 1440px;margin:0}
.page{width:1080px;height:1440px;position:relative;overflow:hidden;background:var(--cream);display:flex;flex-direction:column;break-after:page;page-break-after:always}
.page:last-child{break-after:auto;page-break-after:auto}
/* header + masthead, as on the home page */
.hdr{flex:none;display:flex;justify-content:space-between;align-items:center;padding:30px 72px;background:var(--blush);border-bottom:4px solid #F2A8C8}
.logo{font:600 36px/1 Newsreader;letter-spacing:-.01em;color:var(--ink)}
.logo em{font-style:normal;color:var(--hot);margin-left:6px}
.hbtn{display:inline-flex;align-items:center;gap:12px;padding:16px 26px;border:1.5px solid var(--line);border-radius:999px;background:#fff;box-shadow:0 3px 0 #F6C9DD;font:700 18px/1 Inter;letter-spacing:.12em;text-transform:uppercase;color:var(--ink)}
.hbtn::before,.btn::before{content:"✦";color:var(--hot)}
.mast{flex:none;display:flex;align-items:center;gap:26px;padding:20px 72px;background:#fff;border-bottom:1px solid #EFE4DC}
.mast span{font:700 18px/1 Inter;letter-spacing:.16em;text-transform:uppercase;color:var(--rose);white-space:nowrap}
.mast span:last-child{color:#4A3F44}
.mast i{flex:1;height:1px;background:var(--gold);opacity:.7}
.main{flex:1;min-height:0;padding:54px 72px 0;display:flex;flex-direction:column;gap:34px}
.foot{flex:none;margin:0 72px;padding:20px 0 34px;border-top:1px solid #E8D9CC;display:flex;justify-content:space-between;font:700 18px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:#4A3F44}
.foot b{color:var(--rose)}
/* e-kick pill */
.kick{align-self:flex-start;display:inline-flex;align-items:center;gap:16px;padding:12px 24px;border:1.5px solid var(--kickline);border-radius:999px;background:var(--blush);font:700 18px/1.2 Inter;letter-spacing:.13em;text-transform:uppercase;color:var(--rose)}
.kick::before{content:"";width:40px;height:1.5px;background:var(--gold)}
h1,h2{font-family:Newsreader,serif;font-weight:600;letter-spacing:-.025em;line-height:1.1;color:var(--ink);text-wrap:balance}
h1{font-size:72px}h2{font-size:62px}
h1 em,h2 em{font-style:normal;color:var(--hot)}
.lede{font:400 25px/1.6 Inter;color:var(--ink)}
.lede strong{font-weight:700}
.head{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:44px;align-items:end}
.head>div{display:flex;flex-direction:column;gap:22px}
/* "How most people build it" side note */
.fw{border-left:1.5px solid var(--gold);padding-left:28px;font:400 23px/1.6 Inter;color:var(--ink)}
.fw .t{display:block;font:700 18px/1.2 Inter;letter-spacing:.15em;text-transform:uppercase;color:#4A3F44;margin-bottom:12px}
.fw strong{display:block;margin-top:12px;font-weight:600}
/* e-btn */
.btn{display:inline-flex;align-items:center;gap:18px;align-self:flex-start;padding:22px 36px;border:1.5px solid var(--line);border-radius:999px;background:#fff;box-shadow:0 3px 0 #F6C9DD;font:700 18px/1 Inter;letter-spacing:.12em;text-transform:uppercase;color:var(--ink);text-decoration:none}
.btn::after{content:"→";color:var(--ink)}
/* cover-photo frame, with fine glitter in the pink border */
.frame{margin:0;padding:20px;border-radius:40px;background-color:var(--frame);outline:1.5px solid var(--line);box-shadow:0 18px 42px rgba(184,36,95,.11);display:flex;flex-direction:column;position:relative}
.frame .ph{flex:1;min-height:0;border-radius:16px 16px 0 0;overflow:hidden;background:#F4EDE6}
.frame img{display:block;width:100%%;height:100%%;object-fit:cover}
.frame figcaption{flex:none;background:var(--paper);border-radius:0 0 16px 16px;padding:16px 20px;text-align:center;font:700 18px/1.3 Inter;letter-spacing:.14em;text-transform:uppercase;color:#4A3F44}
.frame figcaption b{color:var(--rose)}
/* showroom "room" cards */
.rooms{display:grid;gap:26px}
.room{background:#fff;border:2px solid var(--line);border-radius:30px 30px 30px 8px;overflow:hidden;box-shadow:0 24px 40px -34px rgba(184,36,95,.6);display:flex;flex-direction:column}
.room .rp{position:relative;border-bottom:1.5px solid var(--line)}
.room .rp img{display:block;width:100%%;aspect-ratio:4/5;object-fit:cover}
.room .badge{position:absolute;top:16px;right:16px;padding:10px 18px;border-radius:999px;background:var(--hot);color:#fff;font:700 20px/1 Inter;box-shadow:0 4px 10px rgba(184,36,95,.3)}
.room .rb{padding:22px 24px 26px;display:flex;flex-direction:column;gap:8px}
.ck{font:700 18px/1.2 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--rose)}
.room h3{font:600 32px/1.15 Newsreader;letter-spacing:-.01em;color:var(--ink)}
.room p{font:400 21px/1.5 Inter;color:var(--ink)}
/* method staircase cards */
.stair{display:grid;gap:30px;padding-top:46px;position:relative}
.step{position:relative;background:#fff;border:2px solid var(--line);border-radius:34px 12px;box-shadow:0 26px 50px -40px rgba(194,24,91,.55);padding:66px 26px 28px;text-align:center}
.step.lav{background:var(--lavbg);border-color:var(--lavline)}
.step .num{position:absolute;top:-46px;left:50%%;transform:translateX(-50%%);width:92px;height:92px;border-radius:50%%;display:grid;place-items:center;background:linear-gradient(135deg,#E8418A,#B8245F);color:#fff;font:600 42px/1 Newsreader;box-shadow:0 14px 28px -12px rgba(194,24,91,.7),0 0 0 9px var(--halo)}
.step .ord{font:700 18px/1.2 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--rose)}
.step h3{font:600 40px/1.12 Newsreader;letter-spacing:-.015em;color:var(--ink);margin-top:6px;text-wrap:balance}
.step p{font:400 21px/1.5 Inter;color:var(--ink);margin-top:12px;text-wrap:pretty}
.step b{display:block;margin-top:16px;padding-top:16px;border-top:1.5px dashed var(--dash);font:600 21px/1.4 Inter;color:var(--rose)}
/* refuse list boxes */
.refh{font:700 18px/1.2 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--rose)}
.refuse{display:grid;gap:18px}
.refuse>div{background:#fff;border:2px solid var(--line);border-radius:8px 8px 30px 8px;padding:24px 28px}
.refuse strong{display:block;font:600 30px/1.2 Newsreader;color:var(--ink);margin-bottom:8px}
.refuse.p9 span{font-size:24px}
.refuse.p9 strong{font-size:36px;margin-bottom:14px}
.refuse.p9>div{padding:32px}
.refuse span{font:400 21px/1.55 Inter;color:var(--ink)}
/* fam checklist */
.fam{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px 34px;list-style:none}
.fam li{display:flex;gap:16px;font:400 24px/1.45 Inter;color:var(--ink)}
.fam li::before{content:"✓";flex:none;width:32px;height:32px;margin-top:2px;border-radius:50%%;background:var(--hot);color:#fff;display:grid;place-items:center;font:700 18px/1 Inter}
.note{padding-top:24px;border-top:1.5px solid #F2A8C8;font:400 23px/1.6 Inter;color:var(--ink)}
.note strong{color:var(--rose);font-weight:700}
.mani{display:flex;align-items:baseline;justify-content:center;gap:24px;flex-wrap:wrap;text-align:center}
.mani span{font:700 18px/1.3 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--rose)}
.mani p{font:600 46px/1.15 Newsreader;letter-spacing:-.02em;color:var(--ink)}
.mani p em{font-style:normal;color:var(--hot)}
.meta{display:flex;border-top:1.5px solid #F2A8C8;padding-top:26px}
.meta div{flex:1;text-align:center;border-left:1px solid #E8D9CC}
.meta div:first-child{border-left:0}
.meta b{display:block;font:600 34px/1 Inter;color:var(--ink)}
.meta span{display:block;margin-top:10px;font:400 18px/1.35 Inter;color:#4A3F44}
.small{font:400 19px/1.5 Inter;color:#4A3F44}
.sp{flex:1}
</style></head><body>
''' % ()
def page(n,mast,body):
    return f'''<section class="page" id="p{n}">
<div class="hdr"><span class="logo">The Digital Income<em>Edit™</em></span><span class="hbtn">Free preview guide</span></div>
<div class="mast"><span>The While-You-Sleep Storefront™</span><i></i><span>{mast}</span></div>
<div class="main">{body}</div>
<div class="foot"><span>The While-You-Sleep Storefront™</span><b>{n:02d} / 10</b></div></section>
'''
def frame(src,alt,cap,h,pos=''):
    return f'<figure class="frame gl" style="height:{h}px"><div class="ph"><img src="img/{src}" alt="{alt}" style="object-position:{pos or "50% 50%"}"></div><figcaption>{cap}</figcaption></figure>'
def room(src,alt,badge,ck,h3,p):
    return f'<div class="room"><div class="rp"><img src="img/{src}" alt="{alt}"><span class="badge">{badge}</span></div><div class="rb"><span class="ck">{ck}</span><h3>{h3}</h3><p>{p}</p></div></div>'
def room2(*a):
    return room(*a).replace('alt=','style="aspect-ratio:3/5" alt=',1)
def step(i,ordl,h3,p='',b='',lav=False):
    return f'<div class="step{" lav" if lav else ""}"><span class="num">{i}</span><span class="ord">{ordl}</span><h3>{h3}</h3>{f"<p>{p}</p>" if p else ""}{f"<b>{b}</b>" if b else ""}</div>'
P=[]
P.append(page(1,'Planned. Pinned. Posted.',f'''
<span class="kick">Free preview</span>
<h1>Your taste.<br>A repeatable <em>system.</em></h1>
<p class="lede"><strong>Planned. Pinned. Posted. Blogged. You Slept.</strong></p>
<div class="rooms" style="grid-template-columns:repeat(3,minmax(0,1fr))">
{room("plaid-basic.jpg","Basic: pink plaid shacket outfit laid out on wood floorboards","Basic","01 · First","See the pieces","Every piece, laid out.")}
{room("plaid-styled.jpg","Styled: the plaid outfit hung by a farmhouse window with pumpkins and apples","Styled","02 · Second","Feel the style","Fully styled, never bare.")}
{room("plaid-lifestyle.jpg","Lifestyle: Tommy Kate laughing at the pumpkin patch in the plaid outfit","Lifestyle","03 · Last","Picture it","Tommy Kate wearing the look.")}
</div>
<div class="meta"><div><b>Customized</b><span>to your taste</span></div><div><b>Guided</b><span>setup</span></div><div><b>Automatic</b><span>after setup</span></div></div>'''))
P.append(page(2,'The problem',f'''
<div class="head"><div><span class="kick">The part nobody tells you</span><h2>You found the look.<br><em>Now what?</em></h2></div>
<p class="fw"><span class="t">Every single look</span>comes with four jobs. Tomorrow brings a new look and the same four jobs.</p></div>
{frame("kitchen-late.jpg","Late night at the kitchen island with a laptop","<b>Another late one</b> · the same four jobs",560,"60% 45%")}
<ul class="fam"><li>The photos</li><li>The words</li><li>Where people shop it</li><li>Doing it all again tomorrow</li></ul>
<p class="note"><strong>6 Pins a day. By hand?</strong> Passive income isn't passive when you are the one doing every job.</p>'''))
P.append(page(3,'The shift',f'''
<div style="display:grid;grid-template-columns:420px minmax(0,1fr);gap:46px;align-items:center;margin-top:10px">
{frame("nightstand.jpg","Nightstand at night with a phone, a book and a pink tumbler beside the bed","<b>Lights out</b>",1090,"70% 50%")}
<div style="display:flex;flex-direction:column;gap:26px"><span class="kick">Here's the shift</span><h2>What if the treadmill ran <em>without you?</em></h2>
<p class="lede">The While-You-Sleep Storefront™ does the jobs for you. Set it up once. Then no constantly making lists.</p>
<div style="margin-top:14px;padding-top:26px;border-top:1.5px solid #F2A8C8"><span class="ck">Jodie, on why she built it</span><p style="margin-top:10px;font:600 50px/1.05 Newsreader;color:var(--hot);letter-spacing:-.02em;white-space:nowrap">“NO THINKING.”</p></div></div></div>'''))
P.append(page(4,'Show, don\'t tell',f'''
<div class="head"><div><span class="kick">Show, don't tell</span><h2>One look.<br><em>Three photos.</em></h2></div>
<p class="fw">The pink ghost coffee bar, in the order every look runs: Basic, Styled, Lifestyle.</p></div>
<div class="rooms" style="grid-template-columns:repeat(3,minmax(0,1fr))">
{room2("coffee-basic.jpg","Basic: pink ghost and pumpkin decor pieces on a wood sideboard","Basic","Photo 01","See the pieces","Every piece, laid out.")}
{room2("coffee-styled.jpg","Styled: the pink ghost coffee bar fully set up on a chippy sideboard","Styled","Photo 02","Feel the style","Fully styled, never bare.")}
{room2("coffee-lifestyle.jpg","Lifestyle: Tommy Kate laughing as she sticks paper bats on her kitchen wall","Lifestyle","Photo 03","Picture it in your life","Tommy Kate around her real farmhouse.")}
</div>
<p class="small">Styling examples. AI-generated images can differ from the linked products.</p>'''))
P.append(page(5,'What comes with every look',f'''
<div style="display:flex;flex-direction:column;gap:22px"><span class="kick">What comes with every look</span><h2>The photos open the door.<br>The words get the <em>save.</em></h2></div>
<div style="display:grid;grid-template-columns:380px minmax(0,1fr);gap:40px;align-items:start">
{frame("porch-decor-basic.jpg","Pink Halloween porch flat lay on weathered white boards","<b>Home decor</b> · Basic",840)}
<div style="display:flex;flex-direction:column;gap:18px"><p class="refh">With every look</p>
<div class="refuse" style="gap:22px"><div><strong>Pinterest Pin copy.</strong><span>Three Pins per look.</span></div><div><strong>The Instagram post.</strong><span>Carousel: lifestyle, styled, clean.</span></div><div><strong>Shop-the-look blog post.</strong><span>One page for the whole look.</span></div><div><strong>Where it links.</strong><span>Each Pin links to the Amazon list its products came from.</span></div></div></div></div>'''))
P.append(page(6,'Your taste runs it',f'''
<div class="head"><div><span class="kick">Your taste runs it</span><h2>My pink.<br>Your <em>recipe.</em></h2></div>
<p class="fw"><span class="t">Your first look</span>A weekend outfit, a seasonal shelf, a gift guide your people would save.</p></div>
<div class="rooms" style="grid-template-columns:repeat(4,minmax(0,1fr));gap:18px">
<div class="room"><div class="rp"><img src="img/hoodie-basic.jpg" alt="Hoodie outfit flat lay" style="aspect-ratio:2/3;object-position:50% 0"></div><div class="rb" style="padding:16px"><span class="ck">Campus outfit</span></div></div>
<div class="room"><div class="rp"><img src="img/porch-decor-basic.jpg" alt="Porch decor flat lay" style="aspect-ratio:2/3;object-position:50% 0"></div><div class="rb" style="padding:16px"><span class="ck">Porch decor</span></div></div>
<div class="room"><div class="rp"><img src="img/porch-essentials-lifestyle.jpg" alt="Trick-or-treat porch lifestyle photo" style="aspect-ratio:2/3"></div><div class="rb" style="padding:16px"><span class="ck">Treat night</span></div></div>
<div class="room"><div class="rp"><img src="img/cat-lifestyle.jpg" alt="Costume lifestyle photo on the farmhouse porch" style="aspect-ratio:2/3;object-position:50% 40%"></div><div class="rb" style="padding:16px"><span class="ck">Costume</span></div></div>
</div>
<p class="refh">Three choices you make once</p>
<div class="stair" style="grid-template-columns:repeat(3,minmax(0,1fr));padding-top:30px">
{step(1,"01 · Once","Your theme")}{step(2,"02 · Once","Your visuals","Your own persona, or flat lays only.",lav=True)}{step(3,"03 · Once","Your storefront path")}
</div>'''))
P.append(page(7,'How it runs',f'''
<div class="head"><div><span class="kick">How it runs</span><h2>Three steps.<br>Then it <em>keeps going.</em></h2></div>
<p class="fw"><span class="t">You choose</span>Automatic by default. Turn approvals on for your first few days if you like to check everything.</p></div>
<div class="stair" style="grid-template-columns:repeat(3,minmax(0,1fr))">
{step(1,"01 · First","Set it up once")}{step(2,"02 · Then","It builds 2 looks a day","","2 looks a day = 6 Pins.",lav=True)}{step(3,"03 · Every day","It posts, pins and blogs")}
</div>
{frame("loft-desk.jpg","Laptop left on in the attic loft at night","<b>The computer stays on</b> · you don't have to",440)}'''))
P.append(page(8,"What's inside the kit",f'''
<div style="display:flex;flex-direction:column;gap:22px"><span class="kick">What's inside the kit</span><h2>The pieces behind the <em>pretty.</em></h2></div>
<div class="stair" style="grid-template-columns:repeat(2,minmax(0,1fr));row-gap:84px;grid-auto-rows:minmax(370px,auto);margin-top:16px">
{step(1,"01 · First","Set it up","A guided setup that records your choices.")}{step(2,"02 · Second","Build the looks","The themed-look recipe for any theme or season.",lav=True)}
{step(3,"03 · Third","Keep it running","Scheduled tasks, plus a missed‑run check.",lav=True)}{step(4,"04 · Last","Extend it","Optional blog and Instagram.","Outfit of the Day recipe for Brand Closet™ members.")}
</div>'''))
P.append(page(9,'Honest, up front',f'''
<div style="display:flex;flex-direction:column;gap:22px"><span class="kick">Honest, up front</span><h2>A quick fit check.<br>Then your <em>first look.</em></h2></div>
<div class="refuse p9" style="grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:minmax(300px,auto);gap:24px">
<div><strong>Your tools.</strong><span>Claude desktop and Chrome, Amazon Associates or Influencer, Pinterest, image tools.</span></div>
<div><strong>Your setup.</strong><span>Your own accounts. The computer needs to be on when the tasks run, and the Amazon list step uses the browser on that computer. Tool costs are separate.</span></div>
<div><strong>Your path.</strong><span>Blog and Instagram are optional.</span></div>
<div><strong>How it runs.</strong><span>Automatic by default, with the option to approve everything yourself. We recommend turning approvals on for your first few days.</span></div>
</div>
<p class="note"><strong>The kit does not promise sales or income.</strong></p>'''))
P.append(page(10,'Your next step',f'''
<span class="kick">Your next step</span>
<h1>Ready to build<br>around <em>your taste?</em></h1>
{frame("porch-morning.jpg","Tommy Kate on the farmhouse porch in the morning with her phone and pink tumbler","<b>Planned. Pinned. Posted. Blogged.</b> · You Slept.",640,"60% 50%")}
<a class="btn" href="https://www.thedigitalincomeedit.com/shop/while-you-sleep-storefront">Explore The While-You-Sleep Storefront™</a>
<p class="small">The kit does not promise sales or income.</p>'''))
GLI=f'background-image:{G1},{G2};background-size:64px 64px,47px 47px;'.replace('"',"&quot;")
P=[x.replace('class="frame gl" style="','class="frame" style="background-image:'+G1.replace('"','&quot;')+','+G2.replace('"','&quot;')+';background-size:64px 64px,47px 47px;') for x in P]
open('index.html','w').write(CSS+''.join(P)+'</body></html>\n')
