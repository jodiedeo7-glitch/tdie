import sys, random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
F=os.environ.get('PIN_FONTS','/tmp/pinfonts')+'/'
LIB='/home/claude/tdie/public/images/library/'
S=2; W,H=1000*S,1500*S
CREAM=(251,246,238); INK=(26,20,23); PINK=(214,46,115); GOLD=(200,169,106); WHITE=(255,255,255)
def jost(sz,wt=400):
    f=ImageFont.truetype(F+'Jost[wght].ttf',sz*S)
    try: f.set_variation_by_axes([wt])
    except Exception: pass
    return f
def gl(sz): return ImageFont.truetype(F+'Gloock-Regular.ttf',sz*S)
def yt(sz): return ImageFont.truetype(F+'Yellowtail-Regular.ttf',sz*S)
def sparkle(d,x,y,r,col):
    x*=S;y*=S;r*=S
    pts=[(x,y-r),(x+r*.22,y-r*.22),(x+r,y),(x+r*.22,y+r*.22),(x,y+r),(x-r*.22,y+r*.22),(x-r,y),(x-r*.22,y-r*.22)]
    d.polygon(pts,fill=col)
def wrap(d,text,font,maxw):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=font)<=maxw*S: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines
def wrapl(d,lab,txt,bf,bb,maxw):
    labw=d.textlength(lab+' ',font=bb)/S
    words=txt.split(); lines=[]; cur=''; avail=maxw-labw
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=bf)<=avail*S: cur=t
        else:
            lines.append(cur); cur=w; avail=maxw
    if cur: lines.append(cur)
    return lines
def render(p,out):
    im=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(im)
    M=56; CW=1000-2*M
    # frame hairline
    d.rectangle([24*S,24*S,(1000-24)*S,(1500-24)*S],outline=GOLD,width=2*S)
    y=58
    kf=jost(30,600)
    d.text((M*S,y*S),' '.join(p['kicker']),font=kf,fill=PINK) if False else None
    k=p['kicker']; x=M*S
    for ch in k:
        d.text((x,y*S),ch,font=kf,fill=PINK); x+=d.textlength(ch,font=kf)+3*S
    y+=52
    # headline with one stressed word, measured wrapping
    hf=gl(100); sf=yt(112)
    lines=[]
    for part in p['headline'].split('|'):
        ln=[]
        for w in part.split():
            isS=(w==p['stress']); f=sf if isS else hf
            tw=d.textlength(w+' ',font=f)/S+(16 if isS else 0)
            ln.append((w,isS,tw))
        wsum=sum(t[2] for t in ln)-d.textlength(' ',font=hf)/S
        if wsum>CW: print('HEADLINE OVERFLOW',p['id'],part,wsum)
        lines.append(ln)
    p['_hlines']=len(lines)
    for ln in lines:
        x=M*S
        for w,isS,tw in ln:
            if isS:
                d.text((x,(y-4)*S),w,font=sf,fill=PINK)
                wl=d.textlength(w,font=sf)/S
                for (fx,fy,r,c) in [(.1,.15,13,GOLD),(.5,-.05,9,WHITE),(.93,.2,12,GOLD),(.3,.95,8,GOLD)]:
                    sparkle(d,x/S+wl*fx,y+12+fy*70,r,c)
            else:
                d.text((x,y*S),w,font=hf,fill=INK)
            x+=tw*S
        y+=104
    y+=6
    d.line([M*S,y*S,(1000-M)*S,y*S],fill=GOLD,width=2*S); y+=18
    # measure body
    bf=jost(40,400); bb=jost(40,700)
    items=[]
    if p.get('sub'): items.append(('sub',p['sub']))
    for lab,txt in p['rows']: items.append(('row',(lab,txt)))
    items.append(('take',p['take']))
    # estimate heights
    lh=50; gap=10
    total=0; plan=[]
    for kind,val in items:
        if kind=='sub':
            ls=wrap(d,val,jost(40,500),CW); plan.append((kind,val,ls)); total+=len(ls)*lh+gap
        elif kind=='row':
            lab,txt=val
            ls=wrapl(d,lab,txt,bf,bb,CW); plan.append((kind,val,ls)); total+=len(ls)*lh+gap
        else:
            ls=wrap(d,val,gl(44),CW); plan.append((kind,val,ls)); total+=len(ls)*54+gap+10
    foot=150
    photo_h=1500-58-y-total-foot-30
    p['_photo_h']=photo_h; p['_y_after_head']=y
    if photo_h<150: print(p['id'],'WARN photo_h',photo_h); 
    ph=max(photo_h,120)
    # photo
    ph_im=Image.open(LIB+p['photo']).convert('RGB')
    tw_,th_=CW*S,ph*S
    r=max(tw_/ph_im.width,th_/ph_im.height)
    ph_im=ph_im.resize((int(ph_im.width*r)+1,int(ph_im.height*r)+1),Image.LANCZOS)
    fx,fy=p.get('focus',(.5,.5))
    l=int((ph_im.width-tw_)*fx); t=int((ph_im.height-th_)*fy)
    ph_im=ph_im.crop((l,t,l+tw_,t+th_))
    im.paste(ph_im,(M*S,y*S))
    d.rectangle([M*S,y*S,(M+CW)*S,(y+ph)*S],outline=GOLD,width=2*S)
    sparkle(d,M+CW-60,y+48,22,WHITE); sparkle(d,M+CW-100,y+80,10,WHITE)
    y+=ph+22
    # body
    for kind,val,ls in plan:
        if kind=='sub':
            for l_ in ls: d.text((M*S,y*S),l_,font=jost(40,500),fill=INK); y+=lh
            y+=gap
        elif kind=='row':
            lab,txt=val
            labw=d.textlength(lab+' ',font=bb)
            d.text((M*S,y*S),lab,font=bb,fill=PINK)
            d.text((M*S+labw,y*S),ls[0],font=bf,fill=INK); y+=lh
            for l_ in ls[1:]: d.text((M*S,y*S),l_,font=bf,fill=INK); y+=lh
            y+=gap
        else:
            y+=10
            d.line([M*S,(y-6)*S,(M+120)*S,(y-6)*S],fill=PINK,width=3*S)
            for l_ in ls: d.text((M*S,y*S),l_,font=gl(44),fill=INK); y+=54
    p['_y_end']=y
    # footer
    fy=1500-58-118
    d.line([M*S,fy*S,(1000-M)*S,fy*S],fill=GOLD,width=2*S)
    lf=gl(34); df=jost(26,500)
    t1='THE DIGITAL INCOME EDIT™'; t2='www.thedigitalincomeedit.com'
    d.text((M*S,(fy+14)*S),t1,font=lf,fill=INK)
    d.text((M*S,(fy+62)*S),t2,font=df,fill=INK)
    cta='Learn more on Skool'
    cf=jost(28,600); cw=d.textlength(cta,font=cf)/S
    bw=cw+64; bx1=1000-M; bx0=bx1-bw; by0=fy+34; by1=by0+58
    d.rounded_rectangle([bx0*S,by0*S,bx1*S,by1*S],radius=31*S,fill=WHITE,outline=INK,width=2*S)
    d.text(((bx0+32)*S,(by0+10)*S),cta,font=cf,fill=INK)
    # grain
    random.seed(3)
    g=Image.effect_noise((W,H),12).convert('L')
    im=Image.blend(im,Image.merge('RGB',(g,g,g)),0.02)
    im=im.resize((1000,1500),Image.LANCZOS)
    im.save(out,optimize=True)
    return p
