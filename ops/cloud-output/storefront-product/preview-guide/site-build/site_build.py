# Builds the WYS preview guide from the live site's own home-page markup and CSS.
import re,sys
dist=sys.argv[1]; out=sys.argv[2]
src=open(dist+'/index.html').read()
head=src[:src.index('<body')]
head=re.sub(r'<script.*?</script>','',head,flags=re.S)
head=re.sub(r'<noscript>.*?</noscript>','',head,flags=re.S)
head=re.sub(r'<!--.*?-->','',head,flags=re.S)
head=re.sub(r'<meta (?!charset)[^>]*>','',head)
head=re.sub(r'<link rel="(?:canonical|icon|apple-touch-icon|preconnect|dns-prefetch|alternate)"[^>]*>','',head)
head=re.sub(r'<title>.*?</title>','<title>WYS Free Preview Guide</title>',head,flags=re.S)
GL=open(sys.argv[3]).read().strip()
G1=re.search(r'--glitter:(url\("[^"]*"\))',GL).group(1); G2=re.search(r'--glitter2:(url\("[^"]*"\))',GL).group(1)
I='/_wysguide-img/'
extra='''<style>
html,body{background:#fff!important}
body:before{display:none!important}
:root{%s}
.gpage{width:720px;height:960px;overflow:hidden;position:relative;background:#FFFBF8;display:flex;flex-direction:column;break-after:page;page-break-after:always}
.gpage:last-child{break-after:auto;page-break-after:auto}
.gpage>.gbody{flex:1;min-height:0;display:flex;flex-direction:column}
.gfoot{flex:none;margin:0 24px;padding:12px 0 18px;border-top:1px solid #E8D9CC;display:flex;justify-content:space-between;font:700 11px/1 Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#6B5A60}
.gfoot b{color:#B8245F}
body .gpage figure.gframe.glit{background-color:#FFD7E9!important;background-image:%s,%s!important;background-size:64px 64px,47px 47px!important;background-repeat:repeat!important}
.trio{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.trio img{display:block;width:100%%;aspect-ratio:4/5;object-fit:cover;border-radius:10px}
@page{size:720px 960px;margin:0}
.gframe{margin:0;padding:14px;border-radius:28px;outline:1px solid #E891B6;box-shadow:0 12px 30px rgba(184,36,95,.094);display:flex;flex-direction:column}
.gframe .gimg{flex:1;min-height:0;border-radius:12px 12px 0 0;overflow:hidden;background:#F4EDE6}
.gframe .gimg>img{display:block;width:100%%;height:100%%;object-fit:cover}
.gframe .trio{padding:0;background:#FFFCFE;border-radius:12px 12px 0 0;padding:8px 8px 0}
.gframe .trio img{display:block;width:100%%;aspect-ratio:4/5;object-fit:cover;border-radius:8px}
.gframe figcaption{flex:none;background:#FFFCFE;border-radius:0 0 12px 12px;padding:10px 16px;text-align:center}
.cover-photo .trio img{position:static!important;inset:auto!important;width:100%%!important;height:auto!important;aspect-ratio:4/5!important;object-fit:cover!important;border-radius:10px!important}
#p4 .e-art-img{height:auto!important;aspect-ratio:4/5!important;overflow:hidden}
#p4 .e-art-img img{width:100%%!important;height:100%%!important;object-fit:cover!important}
#p4 .rooms{grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:14px!important}
#p4 .e-art-img img{aspect-ratio:4/5;object-fit:cover;height:auto!important}
#p6 .e-sec,#p7 .e-sec{padding-top:36px!important;padding-bottom:0!important}
#p6 .stair,#p7 .stair{margin-top:28px!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:12px!important}
#p3 .tdie-manifesto p{font-size:44px!important}

</style>
''' % (GL,G1,G2)
head=head.replace('</head>',extra+'</head>')
CID=' data-astro-cid-lcdefpme'
def cid(html):
    return re.sub(r'<([a-z][a-z0-9]*)(\s|>|/)',lambda m:'<'+m.group(1)+CID+m.group(2),html)
def page(n,inner):
    return f'<div class="gpage" id="p{n}"><div class="gbody">{cid(inner)}</div><div class="gfoot"><span>The While-You-Sleep Storefront™ · Free preview guide</span><b>{n:02d} / 10</b></div></div>\n'
def photo(src,alt,cap,style='',imgstyle=''):
    return f'<figure class="gframe glit" style="{style}"><div class="gimg"><img src="{I}{src}" alt="{alt}" style="{imgstyle}"></div><figcaption><span class="e-credit">{cap}</span></figcaption></figure>'
def trio(items,cap):
    imgs=''.join(f'<img src="{I}{a}" alt="{b}">' for a,b in items)
    return f'<figure class="gframe glit" style="margin:0 24px;align-self:start;height:auto;flex:none"><div class="trio">{imgs}</div><figcaption><span class="e-credit">{cap}</span></figcaption></figure>'
P=[]
P.append(page(1,f'''<section class="cover" style="flex:1"><div class="mast" aria-hidden="true"><span>The While-You-Sleep Storefront™</span><i></i><span>Free preview guide</span></div>
<div class="cover-copy"><p class="e-kick">Customized · Guided setup · Automatic after setup</p><h1>Your taste. A repeatable <em>system.</em></h1>
<p class="e-lede"><strong>Planned. Pinned. Posted. Blogged. You Slept.</strong></p>
<ul class="cover-meta"><li><b>3</b><span>photos<br>per look</span></li><li><b>3</b><span>Pins<br>per look</span></li><li><b>2</b><span>looks<br>a day</span></li></ul></div>
{trio([("plaid-basic.jpg","Basic: pink plaid shacket outfit laid out on wood floorboards"),("plaid-styled.jpg","Styled: the plaid outfit hung by a farmhouse window with pumpkins and apples"),("plaid-lifestyle.jpg","Lifestyle: Tommy Kate laughing at the pumpkin patch in the plaid outfit")],"<b>One look</b> · Basic, Styled, Lifestyle")}
</section>'''))
P.append(page(2,f'''<section class="fam" style="flex:1"><div class="fam-in"><p class="e-kick">The part nobody tells you</p><h2>You found the look. <em>Now what?</em></h2>
<p class="e-lede">Every single look comes with four jobs. Tomorrow brings a new look and the same four jobs.</p>
<ul class="fam-list"><li>The photos</li><li>The words</li><li>Where people shop it</li><li>Doing it all again tomorrow</li></ul>
<p class="fam-note"><strong>6 Pins a day. By hand?</strong> Passive income isn't passive when you are the one doing every job.</p></div>
<div style="padding:0 24px">{photo("kitchen-late.jpg","Late night at the kitchen island with a laptop","<b>Another late one</b> · the four jobs, again","height:330px")}</div></section>'''))
P.append(page(3,f'''<section class="faceless" style="flex:1"><div style="padding:24px 24px 0">{photo("nightstand.jpg","Nightstand at night with a phone, a book and a pink tumbler beside the bed","<b>Lights out</b> · the list is not on you","height:430px")}</div>
<div class="faceless-copy"><p class="e-kick">Here's the shift</p><h2>What if the treadmill ran <em>without you?</em></h2>
<p class="e-lede">The While-You-Sleep Storefront™ does the jobs for you. Set it up once. Then no constantly making lists.</p></div></section>
<div class="tdie-manifesto"><span class="tdie-manifesto-kicker">Jodie, on why she built it</span><p><em>“NO THINKING.”</em></p></div>'''))
def room(img,alt,ex,h3,p):
    return f'<li><div class="room"><figure class="e-artifact"><div class="e-art-img"><img src="{I}{img}" alt="{alt}"></div><figcaption><b>{ex}</b></figcaption></figure><span class="room-body"><h3>{h3}</h3><p>{p}</p></span></div></li>'
P.append(page(4,f'''<section class="e-sec showroom" id="showroom" style="flex:1"><div class="e-wrap"><div class="show-head"><div><p class="e-kick">Show, don't tell</p><h2 class="e-d2">One look. <em>Three photos.</em></h2></div><p>Styling examples. AI-generated images can differ from the linked products.</p></div>
<ul class="rooms">{room("coffee-basic.jpg","Basic: pink ghost and pumpkin decor pieces on a wood sideboard","Photo 01 · Basic","See the pieces","Every piece, laid out.")}{room("coffee-styled.jpg","Styled: the pink ghost coffee bar fully set up on a chippy sideboard","Photo 02 · Styled","Feel the style","Fully styled, never bare.")}{room("coffee-lifestyle.jpg","Lifestyle: Tommy Kate laughing as she sticks paper bats on her kitchen wall","Photo 03 · Lifestyle","Picture it in your life","Tommy Kate around her real farmhouse.")}</ul></div></section>'''))
P.append(page(5,f'''<section class="faceless" style="flex:1"><div style="padding:24px 24px 0">{photo("porch-decor-basic.jpg","Pink Halloween porch flat lay on weathered white boards","<b>Home decor</b> · Basic","height:220px")}</div>
<div class="faceless-copy"><p class="e-kick">What comes with every look</p><h2>The photos open the door. The words get the <em>save.</em></h2>
<p class="refuse-h">With every look</p><ul class="refuse"><li><strong>Pinterest Pin copy.</strong><span>Three Pins per look.</span></li><li><strong>The Instagram post.</strong><span>Carousel: lifestyle, styled, clean.</span></li><li><strong>Shop-the-look blog post.</strong><span>One page for the whole look.</span></li><li><strong>Where it links.</strong><span>Each Pin links to the Amazon list its products came from.</span></li></ul></div></section>'''))
def step(i,ord_,w,p,b=''):
    body=f'<p>{p}{"<b>"+b+"</b>" if b else ""}</p>' if (p or b) else ''
    return f'<li class="step" style="--i:{i}"><span class="dot" aria-hidden="true"></span><h3><span class="ord">{ord_}</span><span class="w">{w}</span></h3>{body}</li>'
P.append(page(6,f'''<section class="e-sec" id="method" style="flex:1"><div class="e-wrap"><div class="method-head"><div><p class="e-kick">Your taste runs it</p><h2 class="e-d2">My pink. Your <em>recipe.</em></h2></div>
<p class="forwards"><span class="fw">Picture your first look</span>A weekend outfit, a seasonal shelf, a gift guide your people would save.</p></div>
<figure class="gframe glit" style="margin-top:4px"><div class="trio" style="grid-template-columns:repeat(4,minmax(0,1fr))"><img src="{I}hoodie-basic.jpg" alt="Hoodie outfit flat lay"><img src="{I}porch-decor-basic.jpg" alt="Porch decor flat lay"><img src="{I}porch-essentials-lifestyle.jpg" alt="Trick-or-treat porch lifestyle photo"><img src="{I}cat-lifestyle.jpg" alt="Costume lifestyle photo on the farmhouse porch" style="object-position:50% 40%"></div><figcaption><span class="e-credit"><b>Four looks</b> · campus outfit, porch decor, treat night, costume</span></figcaption></figure>
<ol class="stair">{step(0,"01 · Once","Your theme","")}{step(1,"02 · Once","Your visuals","Your own persona, or flat lays only.")}{step(2,"03 · Once","Your storefront path","")}</ol></div></section>'''))
P.append(page(7,f'''<section class="e-sec" id="method" style="flex:1"><div class="e-wrap"><div class="method-head"><div><p class="e-kick">How it runs</p><h2 class="e-d2">Three steps. Then it <em>keeps going.</em></h2></div>
<p class="forwards"><span class="fw">You choose</span>Automatic by default. Turn approvals on for your first few days if you like to check everything.</p></div>
<ol class="stair">{step(0,"01 · First","Set it up once","")}{step(1,"02 · Then","It builds 2 looks a day","2 looks a day = 6 Pins.")}{step(2,"03 · Every day","It posts, pins and blogs","The computer stays on. You don't have to.")}</ol>
{photo("loft-desk.jpg","Laptop left on in the attic loft at night","<b>The computer stays on</b> · you don't have to","height:220px;margin-top:20px")}</div></section>'''))
P.append(page(8,f'''<section class="e-sec" id="method" style="flex:1"><div class="e-wrap"><div class="method-head"><div><p class="e-kick">What's inside the kit</p><h2 class="e-d2">The pieces behind the <em>pretty.</em></h2></div>
<p class="forwards"><span class="fw">4 parts</span><strong>1 system.</strong></p></div>
<ol class="stair">{step(0,"01 · First","Set it up","A guided setup that records your choices.")}{step(1,"02 · Second","Build the looks","The themed-look recipe for any theme or season.")}{step(2,"03 · Third","Keep it running","Scheduled tasks, plus a missed-run check.")}{step(3,"04 · Last","Extend it","Optional blog and Instagram.","Outfit of the Day recipe for Brand Closet™ members.")}</ol></div></section>'''))
P.append(page(9,f'''<section class="faceless" style="flex:1"><div class="faceless-copy"><p class="e-kick">Honest, up front</p><h2>A quick fit check. Then your <em>first look.</em></h2>
<ul class="refuse"><li><strong>Your tools.</strong><span>Claude desktop and Chrome, Amazon Associates or Influencer, Pinterest, image tools.</span></li><li><strong>Your setup.</strong><span>Your own accounts. The computer needs to be on when the tasks run, and the Amazon list step uses the browser on that computer. Tool costs are separate.</span></li><li><strong>Your path.</strong><span>Blog and Instagram are optional.</span></li><li><strong>How it runs.</strong><span>Automatic by default, with the option to approve everything yourself. We recommend turning approvals on for your first few days.</span></li></ul>
<p class="fam-note" style="margin-top:22px"><strong>The kit does not promise sales or income.</strong></p></div></section>'''))
P.append(page(10,f'''<section class="cover" style="flex:1"><div class="cover-copy"><p class="e-kick">Your next step</p><h1>Ready to build around <em>your taste?</em></h1>
<div class="e-actions"><a class="e-btn" href="https://www.thedigitalincomeedit.com/shop/while-you-sleep-storefront">Explore The While-You-Sleep Storefront™ <span class="ar" aria-hidden="true">→</span></a></div>
<p class="e-lede" style="margin-top:14px">The kit does not promise sales or income.</p></div>
<div style="padding:0 24px">{photo("porch-morning.jpg","Tommy Kate on the farmhouse porch in the morning with her phone and pink tumbler","<b>Planned. Pinned. Posted. Blogged.</b> · You Slept.","height:420px")}</div></section>'''))
GLI='background-image:'+G1.replace('"',"&quot;")+','+G2.replace('"',"&quot;")+';background-size:64px 64px,47px 47px;background-color:#FFD7E9;'
P=[x.replace('class="gframe glit" style="','class="gframe glit" style="'+GLI) for x in P]
open(out,'w').write(head+'<body class="e-page sales-page"'+CID+'>\n'+''.join(P)+'</body></html>\n')
