"""One promo Reel for The While-You-Sleep Storefront, made from ONE look's full photo set.

Usage: python3 look_reel.py <slug> <hook 1-4> <out_dir>
Reads src/lifestyle/<slug>.json and <slug>-basic.jpg / -styled.jpg / -lifestyle.jpg, plus the look's Roundup and Found It
pins from public/wys-pins/<slug>/roundup.jpg and found-it.jpg (or ops/wys/newpins/*_<slug_with_underscores>_roundup.jpg / _foundit.jpg).
All five are required (Jodie, 12 Nov 2026: every look has 5 photos; never show a partial set). Seasonal looks are not used.
Writes <out_dir>/<slug>-reel.mp4 (1080x1920, 30 fps, about 23 s, silent) and <slug>-reel-cover.jpg.
Approved design: Jodie picked the "bold" promo (12 Nov 2026). No flat pink backgrounds, lists stacked
with dashes, product name big on the end card, text kept clear of the Instagram caption and buttons.
"""
import os, sys, json, math, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
FD = os.path.join(HERE, 'fonts')
W, H, FPS = 1080, 1920, 30
PINK = (214, 46, 115)
INK = (26, 20, 23)
LIGHT = (255, 240, 246)

HOOKS = {
    1: ('POSTED AT 2 AM.', 'I WAS ASLEEP.'),
    2: ('THIS LOOK WAS MADE', 'WHILE I SLEPT.'),
    3: ("I DIDN'T STYLE THIS.", 'I WAS ASLEEP.'),
    4: ('MY STOREFRONT', 'WORKED THE NIGHT SHIFT.'),
}


def F(name, size, var=None):
    f = ImageFont.truetype(os.path.join(FD, name), size)
    if var:
        f.set_variation_by_name(var)
    return f

ANT = lambda s: F('Anton-Regular.ttf', s)
GLO = lambda s: F('Gloock-Regular.ttf', s)
JOST = lambda s, v='SemiBold': F('Jost.ttf', s, v)
SCRIPT = lambda s: F('yellowtail-latin-400-normal.ttf', s)
BLUSH = (255, 196, 222)      # script accent colour
CHAMP = (246, 226, 206)      # champagne hairlines


def ease(p):
    p = max(0.0, min(1.0, p)); return 1 - (1 - p) ** 3


def ease_back(p):
    p = max(0.0, min(1.0, p)); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2


def fit_text(text, maker, size, max_w):
    d = ImageDraw.Draw(Image.new('RGBA', (5, 5)))
    while size > 20:
        f = maker(size); b = d.textbbox((0, 0), text, font=f)
        if b[2] - b[0] <= max_w: return f
        size -= 4
    return maker(size)


def glow(layer, color=(0, 0, 0), radius=14, strength=1.7, pad=40):
    out = Image.new('RGBA', (layer.width + pad * 2, layer.height + pad * 2), (0, 0, 0, 0))
    g = Image.new('RGBA', layer.size, color + (255,)); g.putalpha(layer.getchannel('A'))
    out.paste(g, (pad, pad), g)
    out = out.filter(ImageFilter.GaussianBlur(radius))
    out.putalpha(out.getchannel('A').point(lambda v: min(255, int(v * strength))))
    out.alpha_composite(layer, (pad, pad)); return out


def label(text, f, fg='white', bg=None, padx=26, pady=14, glow_it=True):
    d = ImageDraw.Draw(Image.new('RGBA', (5, 5))); b = d.textbbox((0, 0), text, font=f)
    w, h = b[2] - b[0] + padx * 2, b[3] - b[1] + pady * 2
    L = Image.new('RGBA', (w, h), (0, 0, 0, 0)); dd = ImageDraw.Draw(L)
    if bg: dd.rectangle((0, 0, w, h), fill=bg)
    dd.text((padx - b[0], pady - b[1]), text, font=f, fill=fg)
    return L if (bg or not glow_it) else glow(L)


def sentence(text):
    t = text.lower(); t = t[:1].upper() + t[1:]
    t = t.replace(' i ', ' I ').replace(' am.', ' AM.')
    if t.startswith('i '): t = 'I ' + t[2:]
    return t


def big(text, size, fg='white', bg=None, max_w=980):
    """Premium type (Jodie, 12 Nov 2026: "more premium/luxury looking with premium text").
    Plain lines: Gloock serif, white, soft dark glow. Accent lines (any bg): blush Yellowtail script with a soft
    deep-rose glow and a thin champagne underline, never a solid colour box."""
    if bg is not None:
        t = sentence(text)
        f = fit_text(t, SCRIPT, int(size * 1.15), max_w - 80)
        L = label(t, f, BLUSH, None, padx=24, pady=18, glow_it=False)
        L = glow(L, (90, 10, 45), 16, 1.6)
        d = ImageDraw.Draw(L); y = L.height - 34
        d.line((L.width * 0.22, y, L.width * 0.78, y), fill=CHAMP + (210,), width=3)
        return L
    f = fit_text(text, GLO, int(size * 0.82), max_w - 60)
    return label(text, f, fg, None)


def stack(lines, gap=12):
    """lines: (text, font, color) -> centred RGBA block."""
    d = ImageDraw.Draw(Image.new('RGBA', (5, 5)))
    rows = [(t, f, c, d.textbbox((0, 0), t, font=f)) for t, f, c in lines]
    w = max(b[2] - b[0] for *_, b in rows) + 20
    h = sum(b[3] - b[1] for *_, b in rows) + gap * (len(rows) - 1) + 20
    L = Image.new('RGBA', (w, h), (0, 0, 0, 0)); dd = ImageDraw.Draw(L); y = 10
    for t, f, c, b in rows:
        dd.text(((w - (b[2] - b[0])) / 2 - b[0], y - b[1]), t, font=f, fill=c); y += b[3] - b[1] + gap
    return L


def shadow(layer, r=22, a=0.35, off=(0, 14), pad=50):
    out = Image.new('RGBA', (layer.width + pad * 2, layer.height + pad * 2), (0, 0, 0, 0))
    s = Image.new('RGBA', layer.size, (30, 10, 20, 255)); s.putalpha(layer.getchannel('A').point(lambda v: int(v * a)))
    out.paste(s, (pad + off[0], pad + off[1]), s); out = out.filter(ImageFilter.GaussianBlur(r))
    out.alpha_composite(layer, (pad, pad)); return out


def pill(text, f, fg, bg, padx=64, pady=32):
    d = ImageDraw.Draw(Image.new('RGBA', (5, 5))); b = d.textbbox((0, 0), text, font=f)
    w, h = b[2] - b[0] + padx * 2, b[3] - b[1] + pady * 2
    P = Image.new('RGBA', (w, h), (0, 0, 0, 0)); dd = ImageDraw.Draw(P)
    dd.rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=bg)
    dd.text((padx - b[0], pady - b[1]), text, font=f, fill=fg); return P


class El:
    def __init__(s, img, cx, cy, t0=0, din=0.4, kind='up', dist=80):
        s.img, s.cx, s.cy, s.t0, s.din, s.kind, s.dist = img, cx, cy, t0, din, kind, dist

    def draw(s, c, t):
        if t < s.t0: return
        p = (t - s.t0) / s.din; e = ease_back(p) if s.kind == 'pop' else ease(p); a = ease(p * 1.5)
        img, dx, dy = s.img, 0, 0
        if s.kind == 'up': dy = (1 - e) * s.dist
        elif s.kind == 'left': dx = (1 - e) * s.dist
        elif s.kind == 'pop':
            k = 0.6 + 0.4 * e
            if abs(k - 1) > 0.005: img = img.resize((max(1, int(img.width * k)), max(1, int(img.height * k))), Image.BILINEAR)
        if a < 0.999:
            img = img.copy(); img.putalpha(img.getchannel('A').point(lambda v: int(v * a)))
        c.alpha_composite(img, (int(s.cx - img.width / 2 + dx), int(s.cy - img.height / 2 + dy)))


def cover_fit(src, z=1.0, cx=0.5, cy=0.5):
    s = max(W / src.width, H / src.height) * z; cw, ch = W / s, H / s
    x, y = src.width * cx, src.height * cy
    x = min(max(x, cw / 2), src.width - cw / 2); y = min(max(y, ch / 2), src.height - ch / 2)
    return src.resize((W, H), Image.BILINEAR, box=(x - cw / 2, y - ch / 2, x + cw / 2, y + ch / 2)).convert('RGBA')


def kenburns(src, t, dur, z0, z1):
    return cover_fit(src, z0 + (z1 - z0) * min(1, t / dur))


def shade():
    m = Image.new('L', (1, H))
    for y in range(H):
        a = 0
        if y < 650: a = int(190 * (1 - y / 650) ** 1.5)
        if y > H - 1000: a = max(a, int(210 * ((y - (H - 1000)) / 1000) ** 1.4))
        m.putpixel((0, y), a)
    L = Image.new('RGBA', (W, H), (20, 8, 14, 255)); L.putalpha(m.resize((W, H))); return L


def rose_backdrop(src):
    """The look's own photo, blurred, under a deep rose wash with a soft glow: rich, never flat."""
    b = cover_fit(src, 1.15).filter(ImageFilter.GaussianBlur(38))
    wash = Image.new('RGBA', (W, H), (96, 18, 56, 140)); b.alpha_composite(wash)
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).ellipse((-250, 250, 1330, 1450), fill=120)
    g = Image.new('RGBA', (W, H), (232, 90, 155, 255)); g.putalpha(m.filter(ImageFilter.GaussianBlur(220)))
    b.alpha_composite(g)
    v = Image.new('L', (1, H))
    for y in range(H): v.putpixel((0, y), int(110 * abs(y / H - 0.5) * 2) ** 1)
    vv = Image.new('RGBA', (W, H), (25, 6, 15, 255)); vv.putalpha(v.resize((W, H))); b.alpha_composite(vv)
    import random; r = random.Random(7); sp = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sp)
    for _ in range(70):
        x, y = r.uniform(0, W), r.uniform(0, H)
        if 260 < x < 820 and 300 < y < 1650 and r.random() < 0.8: continue   # keep sparkle to the edges
        L = r.uniform(3, 10); a = r.randint(90, 200)
        sd.line((x - L, y, x + L, y), fill=(255, 255, 255, a), width=2); sd.line((x, y - L, x, y + L), fill=(255, 255, 255, a), width=2)
        sd.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 255, 255, 230))
    b.alpha_composite(sp.filter(ImageFilter.GaussianBlur(0.6)))
    return b


def extra_photos(slug):
    import glob
    out = {}
    for key, a, b in (('roundup', 'roundup.jpg', '_roundup.jpg'), ('foundit', 'found-it.jpg', '_foundit.jpg')):
        p = os.path.join(REPO, 'public', 'wys-pins', slug, a)
        if not os.path.exists(p):
            g = glob.glob(os.path.join(REPO, 'ops', 'wys', 'newpins', '*_' + slug.replace('-', '_') + b))
            if not g: raise SystemExit(f'MISSING {key} photo for {slug}: needs all 5 photos')
            p = g[0]
        out[key] = Image.open(p).convert('RGB')
    return out


def build(slug, hook_no):
    meta = json.load(open(os.path.join(REPO, 'src', 'lifestyle', slug + '.json')))
    title = meta.get('title') or slug.replace('-', ' ').title()
    ph = {k: Image.open(os.path.join(REPO, 'src', 'lifestyle', f'{slug}-{k}.jpg')).convert('RGB') for k in ('basic', 'styled', 'lifestyle')}
    ph.update(extra_photos(slug))
    h1, h2 = HOOKS[hook_no]
    SH = shade()
    TAG = label('THE WHILE-YOU-SLEEP STOREFRONT™', JOST(30, 'Bold'), glow_it=False, padx=0, pady=0)
    durs = [4.0, 7.6, 4.6, 3.8, 5.6]; total = sum(durs); starts = [sum(durs[:i]) for i in range(5)]

    def chrome(c, si, t):
        p = min(1, (starts[si] + t) / total); d = ImageDraw.Draw(c)
        d.rectangle((60, 70, W - 60, 78), fill=(255, 255, 255, 80))
        d.rectangle((60, 70, 60 + (W - 120) * p, 78), fill=(255, 255, 255, 255))
        c.alpha_composite(glow(TAG, radius=8, strength=1.2), ((W - TAG.width) // 2 - 40, 52))
        d.rectangle((34, 34, W - 34, H - 34), outline=CHAMP + (150,), width=2)

    # 1 hook on the Lifestyle photo
    s1 = [El(big(h1, 140), W / 2, 1010, 0.15, 0.4, 'up', 90), El(big(h2, 150, bg=PINK), W / 2, 1200, 0.9, 0.45, 'pop')]
    def f1(t):
        c = kenburns(ph['lifestyle'], t, durs[0], 1.16, 1.03); c.alpha_composite(SH)
        for e in s1: e.draw(c, t)
        chrome(c, 0, t); return c

    # 2 one look, five ways (full set), on the look's own blurred photo
    B2 = rose_backdrop(ph['lifestyle'])
    lf = JOST(32, 'Bold'); cards = []
    for k, lab in (('basic', 'BASIC'), ('styled', 'STYLED'), ('lifestyle', 'LIFESTYLE'), ('roundup', 'ROUNDUP'), ('foundit', 'FOUND IT')):
        im = ph[k]; w = 540; p = im.resize((w, int(w * im.height / im.width)), Image.LANCZOS).convert('RGBA')
        card = Image.new('RGBA', (w + 20, p.height + 20), (255, 255, 255, 255)); card.paste(p, (10, 10))
        tg = pill(lab, lf, (255, 255, 255), (40, 14, 26, 215), 30, 14); card.alpha_composite(tg, (30, card.height - tg.height - 30))
        cards.append(shadow(card))
    name_line = label(title, fit_text(title, lambda s: JOST(s, 'Medium'), 40, 900), padx=0, pady=0)
    s2 = [El(big('ONE LOOK.', 165), W / 2, 270, 0.05, 0.35, 'pop'),
          El(big('FIVE WAYS.', 165, fg=PINK, bg=(255, 255, 255)), W / 2, 465, 0.4, 0.35, 'pop'),
          El(name_line, W / 2, 600, 0.7, 0.4, 'up', 30)]
    def f2(t):
        c = B2.copy()
        for e in s2: e.draw(c, t)
        for i, card in enumerate(cards):
            st = 0.9 + i * 1.3
            if t < st: continue
            x = W / 2 + (1 - ease((t - st) / 0.5)) * W
            if i < len(cards) - 1 and t > st + 1.3: x = W / 2 - ease((t - st - 1.3) / 0.5) * W
            c.alpha_composite(card, (int(x - card.width / 2), 1110 - card.height // 2))
        chrome(c, 1, t); return c

    # 3 then it makes... (Styled photo)
    lines3 = [('THE PINS.', None), ('THE BLOG POST.', PINK), ('THE CAROUSEL.', None), ('THE IDEA LIST.', PINK)]
    s3 = [El(big('THEN IT MAKES', 90), W / 2, 470, 0.1, 0.35, 'up', 60)]
    for i, (tx, bg) in enumerate(lines3):
        s3.append(El(big(tx, 128, bg=bg), W / 2, 690 + i * 195, 0.5 + i * 0.55, 0.35, 'left', 260))
    DARK = Image.new('RGBA', (W, H), (20, 8, 14, 95))
    def f3(t):
        c = kenburns(ph['styled'], t, durs[2], 1.04, 1.15); c.alpha_composite(SH); c.alpha_composite(DARK)
        for e in s3: e.draw(c, t)
        chrome(c, 2, t); return c

    # 4 every single night (Lifestyle photo, close in on the products; Basic photos carry their own headline)
    s4 = [El(big('EVERY.', 230), W / 2, 640, 0.15, 0.3, 'pop'), El(big('SINGLE.', 230), W / 2, 880, 0.85, 0.3, 'pop'),
          El(big('NIGHT.', 230, bg=PINK), W / 2, 1130, 1.55, 0.3, 'pop')]
    DARK4 = Image.new('RGBA', (W, H), (20, 8, 14, 75))
    def f4(t):
        z = 1.30 + 0.05 * min(1, t / 0.4); c = cover_fit(ph['lifestyle'], z + 0.08 * t / durs[3], 0.5, 0.68)
        c.alpha_composite(SH); c.alpha_composite(DARK4)
        for e in s4: e.draw(c, t)
        chrome(c, 3, t); return c

    # 5 end card on the look's own blurred Styled photo
    B5 = rose_backdrop(ph['styled'])
    name = stack([('The While-You-Sleep', GLO(96), (255, 255, 255)), ('Storefront™', GLO(132), (255, 255, 255))], gap=8)
    lst = stack([(t, JOST(42, 'Medium'), (255, 255, 255)) for t in
                 ('– 2 new looks a night', '– 5 photos per look', '– the Pinterest pins', '– 2 blog posts', '– 2 Instagram carousels')], gap=16)
    s5 = [El(glow(name, (60, 10, 30), 18, 1.3), W / 2, 470, 0.1, 0.5, 'pop'),
          El(big('IT RUNS ITSELF.', 112, fg=PINK, bg=(255, 255, 255)), W / 2, 760, 0.6, 0.35, 'pop'),
          El(lst, W / 2, 1010, 1.0, 0.5, 'up', 40),
          El(pill('SEE HOW IT WORKS', JOST(44, 'SemiBold'), INK, (255, 244, 249)), W / 2, 1265, 1.5, 0.4, 'pop'),
          El(label('Built on Claude. ChatGPT version on the way.', JOST(30, 'Medium'), padx=0, pady=0), W / 2, 1395, 1.9, 0.5, 'up', 20)]
    def f5(t):
        c = B5.copy()
        for e in s5: e.draw(c, t)
        chrome(c, 4, t); return c

    # cover: hook centred in the Instagram grid's safe area
    cv = cover_fit(ph['lifestyle'], 1.05); cv.alpha_composite(Image.new('RGBA', (W, H), (20, 8, 14, 70)))
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).rectangle((0, 640, W, 1280), fill=160)
    band = Image.new('RGBA', (W, H), (20, 8, 14, 255)); band.putalpha(m.filter(ImageFilter.GaussianBlur(120))); cv.alpha_composite(band)
    for el in (El(big(h1, 132), W / 2, 830), El(big(h2, 140, bg=PINK), W / 2, 1010)):
        el.draw(cv, 9)
    t2 = label('THE WHILE-YOU-SLEEP STOREFRONT™', JOST(34, 'Bold'), padx=0, pady=0); cv.alpha_composite(t2, ((W - t2.width) // 2, 1130))
    return [(durs[0], f1), (durs[1], f2), (durs[2], f3), (durs[3], f4), (durs[4], f5)], cv.convert('RGB')


def render(scenes, out_mp4, xfade=0.3):
    parts, last = [], None
    for i, (dur, fn) in enumerate(scenes):
        p = out_mp4[:-4] + f'-s{i}.mp4'; tmp = p[:-4] + '.part.mp4'
        pr = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                               '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-pix_fmt', 'yuv420p', tmp], stdin=subprocess.PIPE)
        for k in range(int(round(dur * FPS))):
            t = k / FPS; fr = fn(t).convert('RGB')
            if last is not None and t < xfade: fr = Image.blend(last, fr, ease(t / xfade))
            pr.stdin.write(fr.tobytes()); lf = fr
        pr.stdin.close(); assert pr.wait() == 0; os.replace(tmp, p); parts.append(p); last = lf
    lst = out_mp4 + '.txt'
    open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
    # silent audio track so every platform accepts it
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo',
                    '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-shortest', '-movflags', '+faststart', out_mp4], check=True)
    for p in parts: os.remove(p)
    os.remove(lst)


if __name__ == '__main__':
    slug, hook, out = sys.argv[1], int(sys.argv[2]), os.path.abspath(sys.argv[3])
    os.makedirs(out, exist_ok=True)
    scenes, cover = build(slug, hook)
    if len(sys.argv) > 4 and sys.argv[4] == 'frames':
        for i, (d, fn) in enumerate(scenes):
            fn(d - 0.6).convert('RGB').save(os.path.join(out, f'{slug}-frame{i+1}.jpg'), quality=90)
        cover.save(os.path.join(out, f'{slug}-reel-cover.jpg'), quality=90)
    else:
        render(scenes, os.path.join(out, f'{slug}-reel.mp4'))
        cover.save(os.path.join(out, f'{slug}-reel-cover.jpg'), quality=90)
