import numpy as np, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
F='/home/claude/tdie/ops/scripts/etsy_pin_render/fonts/'
P='/home/claude/tdie/etsy-photos/'
GOLD=(196,164,104); INK=(34,28,30); PINK=(232,30,120); CREAM=(252,246,236)
def font(n,s):
    f=ImageFont.truetype(F+n,s)
    return f
def glitter(size,seed=7):
    rng=np.random.default_rng(seed); w,h=size
    n=rng.random((h,w)); base=np.zeros((h,w,3),np.float32); base[:]=PINK
    shade=np.linspace(1.1,0.85,h)[:,None,None]; img=base*shade
    img=img*(1-(n>0.93)[...,None]*0.35-(n<0.05)[...,None]*0.45)+(n>0.985)[...,None]*np.array([255,225,240])*0.9+((n>0.93)&(n<=0.985))[...,None]*np.array([255,120,180])*0.35
    im=Image.fromarray(np.clip(img,0,255).astype(np.uint8)); d=ImageDraw.Draw(im)
    for _ in range(int(w*h/700)):
        x,y=rng.integers(0,w),rng.integers(0,h); r=int(rng.integers(1,4))
        d.ellipse([x-r,y-r,x+r,y+r],fill=(255,240,248) if rng.random()<0.6 else (255,214,120))
    return im
def text_glitter(canvas,xy,txt,f,seed=3):
    m=Image.new('L',canvas.size,0); ImageDraw.Draw(m).text(xy,txt,font=f,fill=255)
    sh=Image.new('RGBA',canvas.size,(120,0,50,0)); sh.putalpha(m.filter(ImageFilter.GaussianBlur(6)).point(lambda v:int(v*0.35)))
    canvas.alpha_composite(sh,(4,6))
    g=glitter(canvas.size,seed).convert('RGBA'); g.putalpha(m); canvas.alpha_composite(g)
def satin(W,H):
    src=Image.open(P+'4582721757-main.jpg').convert('RGB')
    strip=src.crop((1660,0,2000,2000)).rotate(90,expand=True)  # 2000x340
    s=strip.resize((W,int(340*W/2000)))
    out=Image.new('RGB',(W,H)); y=0; flip=False
    while y<H:
        out.paste(ImageOps.flip(s) if flip else s,(0,y)); y+=s.height; flip=not flip
    return out.filter(ImageFilter.GaussianBlur(2)).convert('RGBA')
def framed(path,size,angle):
    im=Image.open(path).convert('RGB').resize((size,size),Image.LANCZOS)
    b=Image.new('RGB',(size+28,size+28),CREAM); b.paste(im,(14,14))
    d=ImageDraw.Draw(b); d.rectangle([5,5,size+22,size+22],outline=GOLD,width=3)
    b=b.convert('RGBA').rotate(angle,expand=True,resample=Image.BICUBIC)
    sh=Image.new('RGBA',b.size,(60,0,30,0)); sh.putalpha(b.split()[3].filter(ImageFilter.GaussianBlur(14)).point(lambda v:int(v*0.4)))
    return b,sh
def center_text(d,cx,y,t,f,fill,spacing=0):
    w=d.textlength(t,font=f); d.text((cx-w/2,y),t,font=f,fill=fill)

# ---------- BANNER 3360x840 ----------
W,H=3360,840
c=satin(W,H)
photos=['4619956076','4542364231','4581368845','4582721757','4542348249','4619956076']
items=[('4619956076',-4,'L',70),('4542364231',4,'L',590),('4582721757',-4,'R',590),('4542348249',4,'R',70)]
for pid,a,side,off in items:
    b,sh=framed(P+pid+'-main.jpg',540,a); y=(H-b.height)//2
    x=off if side=='L' else W-off-b.width
    c.alpha_composite(sh,(x+10,y+16)); c.alpha_composite(b,(x,y))
# center cream panel with gold hairline
px0,px1,py0,py1=1210,2150,110,730
d=ImageDraw.Draw(c)
d.rectangle([px0,py0,px1,py1],fill=CREAM+(255,)); d.rectangle([px0+16,py0+16,px1-16,py1-16],outline=GOLD,width=3)
cx=(px0+px1)//2
k=font('GildaDisplay-Regular.ttf',72)
center_text(d,cx,py0+48,'The Digital',k,INK)
f=font('GildaDisplay-Regular.ttf',160)
tw=d.textlength('Income Edit',font=f); text_glitter(c,(cx-tw/2,py0+130),'Income Edit',f)
d=ImageDraw.Draw(c)
d.line([cx-300,py0+370,cx+300,py0+370],fill=GOLD,width=3)
s=font('Allison-Regular.ttf',96); center_text(d,cx,py0+385,'for your life and your business',s,INK)
k2=font('Montserrat%5Bwght%5D.ttf',26); k2.set_variation_by_axes([600])
center_text(d,cx,py0+530,'PLANNERS  ·  PRINTABLES  ·  BUSINESS WORKBOOKS',k2,INK)
c.convert('RGB').save('banner.jpg',quality=93)

# ---------- ICON 1000x1000 ----------
S=1000
src=Image.open(P+'4582721757-main.jpg').convert('RGB')
bg=src.crop((1620,1000,2000,1380)).resize((S,S)).filter(ImageFilter.GaussianBlur(3)).convert('RGBA')
d=ImageDraw.Draw(bg)
d.ellipse([70,70,930,930],fill=CREAM+(255,)); d.ellipse([92,92,908,908],outline=GOLD,width=4)
k=font('Montserrat%5Bwght%5D.ttf',44); k.set_variation_by_axes([600])
center_text(d,500,265,'THE DIGITAL',k,INK)
f=font('GildaDisplay-Regular.ttf',205)
tw=d.textlength('Income',font=f); text_glitter(bg,(500-tw/2,345),'Income',f,seed=11)
d=ImageDraw.Draw(bg)
f2=font('GildaDisplay-Regular.ttf',150); center_text(d,500,585,'Edit',f2,INK)
bg.convert('RGB').save('icon.jpg',quality=95)
