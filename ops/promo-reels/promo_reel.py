#!/usr/bin/env python3
"""TDIE promo reel renderer (1080x1920, 30 fps, MP4, no audio).

Usage:
  python3 promo_reel.py CONFIG.json OUT.mp4            # full video
  python3 promo_reel.py CONFIG.json OUT.mp4 --stills   # contact sheet of stills only (OUT.stills.jpg)

CONFIG keys:
  repo: path to the tdie repo checkout (photos are paths relative to it)
  fonts: folder holding gloock/jost/yellowtail .ttf files
  sparkle: path (relative to repo) of public/images/brand/sparkle-glow.webp
  header: product name shown small at the top of every scene except the end card
  scenes: list, each {"type": ..., "dur": seconds, ...}
    hook:   {"line1", "line2", "photo"}                      big serif line + pink script line + one photo
    triple: {"line1", "line2", "photos":[3], "labels":[3]}   three photos one after another, each with a label chip
    pile:   {"kicker", "words":[n], "photos":[n]}            one word per photo, photos stack up
    quote:  {"kicker", "quote", "name", "source", "photo"?}  a real review, verbatim, with 5 stars
    slept:  {"line1", "line2", "photo"}                      like hook, slow zoom inside the frame
    end:    {"kicker", "name1", "name2", "photos":[3], "lines":[...], "small", "button"}
Photos keep their own shape (the frame always matches the photo; nothing is cropped).
"""
import sys, json, math, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

cfg = json.load(open(sys.argv[1])); OUT = sys.argv[2]; STILLS = '--stills' in sys.argv
R = cfg['repo'].rstrip('/') + '/'; FD = cfg['fonts'].rstrip('/') + '/'
W, H, FPS = 1080, 1920, 30
BG = (255, 247, 250); INK = (42, 26, 34); PINK = (224, 69, 143); KICK = (214, 51, 132); SOFT = (138, 90, 112)

def F(n, s): return ImageFont.truetype(FD + n, s)
GL = lambda s: F('gloock-latin-400-normal.ttf', s)
YT = lambda s: F('yellowtail-latin-400-normal.ttf', s)
J5 = lambda s: F('jost-latin-500-normal.ttf', s)
J6 = lambda s: F('jost-latin-600-normal.ttf', s)

def eo(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def prog(t, a, d): return eo((t - a) / d)

_cache = {}
def photo(p):
    if p not in _cache: _cache[p] = Image.open(R + p).convert('RGB')
    return _cache[p]

def card(img, maxw, maxh, angle=0, zoom=1.0):
    iw, ih = img.size; r = ih / iw
    w = maxw; h = int(w * r)
    if h > maxh: h = maxh; w = int(h / r)
    if zoom != 1.0:
        cw, ch = iw / zoom, ih / zoom
        img = img.crop(((iw - cw) / 2, (ih - ch) / 2, (iw + cw) / 2, (ih + ch) / 2))
    b = max(10, w // 55)
    c = Image.new('RGBA', (w + 2 * b, h + 2 * b), (255, 255, 255, 255))
    c.paste(img.resize((w, h), Image.LANCZOS), (b, b))
    pad = 60
    out = Image.new('RGBA', (c.width + 2 * pad, c.height + 2 * pad), (0, 0, 0, 0))
    out.paste(Image.new('RGBA', c.size, (214, 51, 132, 70)), (pad, pad + 18))
    out = out.filter(ImageFilter.GaussianBlur(22)); out.alpha_composite(c, (pad, pad))
    if angle: out = out.rotate(angle, resample=Image.BICUBIC, expand=True)
    return out

def place(base, im, cx, cy, alpha=1.0, scale=1.0):
    if alpha <= 0: return
    if scale != 1.0: im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BILINEAR)
    if alpha < 1:
        im = im.copy(); im.putalpha(im.getchannel('A').point(lambda v: int(v * alpha)))
    base.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))

def fit(font_fn, size, s, maxw):
    d = ImageDraw.Draw(Image.new('L', (1, 1)))
    while size > 20 and d.textlength(s, font=font_fn(size)) > maxw: size -= 4
    return font_fn(size)

def text(base, s, font, cy, fill, alpha=1.0, dy=0, cx=W / 2, spacing=0):
    if alpha <= 0 or not s: return
    lay = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    if spacing:
        ws = [d.textlength(ch, font=font) + spacing for ch in s]; x = cx - (sum(ws) - spacing) / 2
        for ch, wd in zip(s, ws): d.text((x, cy + dy), ch, font=font, fill=fill + (int(255 * alpha),), anchor='lm'); x += wd
    else:
        d.text((cx, cy + dy), s, font=font, fill=fill + (int(255 * alpha),), anchor='mm')
    base.alpha_composite(lay)

def wrap(s, font, maxw):
    d = ImageDraw.Draw(Image.new('L', (1, 1))); out, cur = [], ''
    for w in s.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out

def chip(base, s, cy, alpha):
    if alpha <= 0: return
    f = J6(34); lay = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    tw = sum(d.textlength(ch, font=f) + 6 for ch in s) - 6; a = int(255 * alpha)
    d.rounded_rectangle((W / 2 - tw / 2 - 44, cy - 38, W / 2 + tw / 2 + 44, cy + 38), radius=38, fill=(255, 255, 255, a), outline=PINK + (a,), width=4)
    base.alpha_composite(lay); text(base, s, f, cy, INK, alpha, spacing=6)

def stars(base, cy, alpha, n=5, r=26):
    if alpha <= 0: return
    lay = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i in range(n):
        cx = W / 2 + (i - (n - 1) / 2) * (r * 2.6)
        pts = [(cx + (r if k % 2 == 0 else r * .45) * math.sin(k * math.pi / 5), cy - (r if k % 2 == 0 else r * .45) * math.cos(k * math.pi / 5)) for k in range(10)]
        d.polygon(pts, fill=PINK + (int(255 * alpha),))
    base.alpha_composite(lay)

sp = Image.open(R + cfg.get('sparkle', 'public/images/brand/sparkle-glow.webp')).convert('RGBA')
sp = sp.resize((int(sp.width * 1.3), int(sp.height * 1.3)), Image.LANCZOS); sp_br = sp.rotate(180)
glow = Image.new('RGBA', (W, H), BG + (255,))
g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse((-150, 300, W + 150, H - 200), fill=200)
wl = Image.new('RGBA', (W, H), (255, 255, 255, 0)); wl.putalpha(g.filter(ImageFilter.GaussianBlur(160))); glow.alpha_composite(wl)

def background(t):
    b = glow.copy(); dx = math.sin(t * .8) * 14; dy = math.cos(t * .6) * 10; a = .75 + .2 * math.sin(t * 2.2)
    place(b, sp, 170 + dx, 140 + dy, a); place(b, sp_br, W - 170 - dx, H - 160 - dy, a); return b

HEADER = cfg['header']
def header(b): text(b, HEADER, fit(GL, 50, HEADER, W - 120), 128, PINK)

# ---- scene builders: each returns fn(local_t, global_t) -> RGBA frame ----
def mk_hook(sc, zoom=False):
    l1 = fit(GL, 84, sc['line1'], W - 120); l2 = fit(YT, 170 if not zoom else 230, sc['line2'], W - 120)
    c0 = None if zoom else card(photo(sc['photo']), 760, 1000, -1.5)
    def f(t, T):
        b = background(T); header(b)
        p1 = prog(t, .1, .4); text(b, sc['line1'], l1, 300, INK, p1, dy=30 * (1 - p1))
        p2 = prog(t, .45, .4); text(b, sc['line2'], l2, 450, PINK, p2, dy=30 * (1 - p2))
        p = prog(t, .25, .6)
        if zoom:
            c = card(photo(sc['photo']), 760, 1000, 1, zoom=1 + .07 * min(1, t / sc['dur']))
            place(b, c, W / 2, 1140 + 120 * (1 - p), p)
        else:
            place(b, c0, W / 2, 1140 + 260 * (1 - p), p, .96 + .04 * min(1, t / sc['dur']))
        return b
    return f

def mk_triple(sc):
    cs = [card(photo(p), 760, 1000, a) for p, a in zip(sc['photos'], (1.5, -1.5, 1))]
    l1 = fit(GL, 100, sc['line1'], W - 120); l2 = fit(YT, 150, sc['line2'], W - 120)
    seg = (sc['dur'] - .2) / 3
    def f(t, T):
        b = background(T); header(b)
        text(b, sc['line1'], l1, 290, INK, prog(t, 0, .35)); text(b, sc['line2'], l2, 430, PINK, prog(t, .25, .35))
        for i in range(3):
            st = i * seg
            if t < st: break
            p = prog(t, st, .45); nxt = i < 2 and t >= st + seg
            if nxt:
                q = prog(t, st + seg, .45)
                if q < 1: place(b, cs[i], W / 2 - 160 * q, 1120, 1 - q, 1 - .08 * q)
            else:
                place(b, cs[i], W / 2 + 700 * (1 - p), 1120, p); chip(b, sc['labels'][i], 1680, prog(t, st + .2, .3))
        return b
    return f

def mk_pile(sc):
    n = len(sc['words']); angs = (-6, 4, -3, 5, -4, 3)
    cs = [card(photo(p), 640, 860, angs[i % 6]) for i, p in enumerate(sc['photos'])]
    seg = sc['dur'] / n; wf = [fit(GL, 150, w, W - 120) for w in sc['words']]
    def f(t, T):
        b = background(T); header(b)
        text(b, sc.get('kicker', ''), J6(34), 230, KICK, prog(t, 0, .3), spacing=8)
        k = min(n - 1, int(t // seg))
        for i in range(k + 1):
            p = prog(t, i * seg, .35)
            place(b, cs[i], W / 2 + (-30 if i % 2 else 30) * (k - i), 1060 + (i - k) * 26, p if i == k else 1, 1.12 - .12 * p)
        pw = prog(t - k * seg, 0, .3); text(b, sc['words'][k], wf[k], 380, INK, pw, dy=40 * (1 - pw))
        d = ImageDraw.Draw(b)
        for i in range(n):
            x = W / 2 + (i - (n - 1) / 2) * 44; d.ellipse((x - 9, 491, x + 9, 509), fill=PINK if i <= k else (240, 200, 220))
        return b
    return f

def mk_quote(sc):
    qf = GL(64); lines = wrap('“' + sc['quote'] + '”', qf, W - 160)
    c0 = card(photo(sc['photo']), 520, 560, 2) if sc.get('photo') else None
    def f(t, T):
        b = background(T); header(b)
        text(b, sc.get('kicker', ''), J6(34), 240, KICK, prog(t, 0, .3), spacing=8)
        stars(b, 320, prog(t, .15, .3))
        y0 = 420
        for i, ln in enumerate(lines):
            p = prog(t, .35 + i * .12, .35); text(b, ln, qf, y0 + i * 82, INK, p, dy=20 * (1 - p))
        y = y0 + len(lines) * 82 + 40
        p = prog(t, .9, .4); text(b, sc['name'], YT(90), y + 30, PINK, p)
        text(b, sc.get('source', ''), J5(30), y + 110, SOFT, p)
        if c0: q = prog(t, 1.1, .5); place(b, c0, W / 2, min(1540, y + 160 + c0.height / 2 - 40), q)
        return b
    return f

def mk_end(sc):
    fan = [card(photo(p), 360, 480, a) for p, a in zip(sc['photos'], (9, -9, 0))]
    n1 = fit(GL, 98, sc['name1'], W - 100); n2 = fit(GL, 98, sc['name2'], W - 100)
    def f(t, T):
        b = background(T)
        text(b, sc.get('kicker', ''), J6(32), 190, KICK, prog(t, 0, .4), spacing=8)
        p = prog(t, .1, .5); text(b, sc['name1'], n1, 300, INK, p, dy=24 * (1 - p)); text(b, sc['name2'], n2, 410, INK, p, dy=24 * (1 - p))
        for i, (dx, dy) in enumerate(((-250, 760), (250, 760), (0, 735))):
            if i < len(fan): q = prog(t, .35 + i * .15, .45); place(b, fan[i], W / 2 + dx * q, dy + 80 * (1 - q), q)
        y = 1080
        for j, ln in enumerate(sc.get('lines', [])):
            q = prog(t, 1.1 + j * .2, .4)
            if j == 0 and ln.isupper(): text(b, ln, J6(32), y, KICK, q, spacing=8); y += 66
            else: text(b, ln, fit(J5, 44, ln, W - 80), y, INK, q); y += 70
        q = prog(t, 1.6, .4); text(b, sc.get('small', ''), fit(J5, 34, sc.get('small', ''), W - 80), y + 6, SOFT, q)
        q3 = prog(t, 1.9, .4)
        if q3 > 0 and sc.get('button'):
            f2 = J6(40); lay = Image.new('RGBA', b.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
            tw = d.textlength(sc['button'], font=f2); hw = (tw / 2 + 60) * (1 + .03 * math.sin(max(0, t - 2.3) * 4))
            by = max(1350, y + 130)
            a3 = int(255 * q3)  # white button, Muted Gold hairline, near-black text, pink arrow (no pink-filled buttons, CLAUDE.md 11 Oct 2026)
            d.rounded_rectangle((W / 2 - hw - 30, by - 46, W / 2 + hw + 30, by + 46), radius=46, fill=(255, 255, 255, a3), outline=(200, 169, 106, a3), width=3)
            b.alpha_composite(lay); aw = d.textlength('  →', font=f2)
            text(b, sc['button'], f2, by, (26, 20, 23), q3, cx=W / 2 - aw / 2)
            # pink arrow drawn as lines (the Jost fonts have no arrow glyph, so a text arrow rendered as nothing)
            la = Image.new('RGBA', b.size, (0, 0, 0, 0)); da = ImageDraw.Draw(la); ax = W / 2 + tw / 2 - aw / 2 + 22; pc = PINK + (a3,)
            da.line((ax, by + 2, ax + 34, by + 2), fill=pc, width=5); da.line((ax + 20, by - 12, ax + 35, by + 2, ax + 20, by + 16), fill=pc, width=5, joint='curve')
            b.alpha_composite(la)
        return b
    return f

MK = {'hook': mk_hook, 'slept': lambda s: mk_hook(s, zoom=True), 'triple': mk_triple, 'pile': mk_pile, 'quote': mk_quote, 'end': mk_end}
SC = [(MK[s['type']](s), s['dur']) for s in cfg['scenes']]
starts, acc = [], 0
for _, d in SC: starts.append(acc); acc += d
TOTAL = acc; XF = .25

def frame(T):
    for i, (fn, d) in enumerate(SC):
        if T < starts[i] + d or i == len(SC) - 1:
            lt = T - starts[i]; im = fn(lt, T)
            if i > 0 and lt < XF:
                pf, pd = SC[i - 1]; im = Image.blend(pf(pd - .001, T), im, lt / XF)
            return im

if STILLS:
    ts = []
    for i, (_, d) in enumerate(SC): ts += [starts[i] + d * .45, starts[i] + d * .95]
    sh = Image.new('RGB', (270 * len(ts), 480), 'white')
    for j, T in enumerate(ts): sh.paste(frame(T).convert('RGB').resize((270, 480)), (270 * j, 0))
    sh.save(OUT + '.stills.jpg', quality=85); print('stills', OUT + '.stills.jpg')
else:
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                           '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', OUT], stdin=subprocess.PIPE)
    for k in range(int(TOTAL * FPS)): ff.stdin.write(frame(k / FPS).convert('RGB').tobytes())
    ff.stdin.close(); ff.wait(); print('done', OUT, TOTAL)
