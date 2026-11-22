import sys, math, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFilter
src, out, seed = sys.argv[1], sys.argv[2], int(sys.argv[3])
S=1080; FPS=30; N=8*FPS
img=Image.open(src).convert('RGB')
W=img.width
rng=np.random.default_rng(seed)
# sparkles mostly in outer band
sp=[]
while len(sp)<22:
    x,y=rng.uniform(0.04,0.96,2)
    if 0.22<x<0.78 and 0.18<y<0.82: continue
    sp.append((x,y,rng.uniform(10,26),rng.uniform(0,2*math.pi),rng.uniform(0.6,1.4)))
def star(d,cx,cy,r,a):
    col=(255,255,255,int(255*a))
    d.polygon([(cx,cy-r),(cx+r*0.16,cy-r*0.16),(cx+r,cy),(cx+r*0.16,cy+r*0.16),(cx,cy+r),(cx-r*0.16,cy+r*0.16),(cx-r,cy),(cx-r*0.16,cy-r*0.16)],fill=col)
    d.ellipse([cx-r*0.18,cy-r*0.18,cx+r*0.18,cy+r*0.18],fill=(255,240,250,int(255*a)))
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{S}x{S}','-r',str(FPS),'-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',out],stdin=subprocess.PIPE)
for f in range(N):
    t=f/(N-1); e=t*t*(3-2*t)
    z=1.0+0.10*e
    cw=W/z; x0=(W-cw)/2; y0=(W-cw)/2
    fr=img.crop((x0,y0,x0+cw,y0+cw)).resize((S,S),Image.BICUBIC).convert('RGBA')
    ov=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for (sx,sy,r,ph,sp_) in sp:
        a=max(0.0,math.sin(2*math.pi*sp_*t*2+ph))**3
        if a>0.02: star(d,sx*S,sy*S,r*(0.6+0.4*a),a*0.9)
    glow=ov.filter(ImageFilter.GaussianBlur(4))
    fr=Image.alpha_composite(Image.alpha_composite(fr,glow),ov)
    p.stdin.write(fr.convert('RGB').tobytes())
p.stdin.close(); p.wait()
