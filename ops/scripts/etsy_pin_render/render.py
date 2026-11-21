import json, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

S = 2  # render scale
W, H = 1000 * S, 1500 * S
import os
F = os.environ.get('PIN_FONTS', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')) + '/'
CREAM = (251, 246, 241)
INK = (26, 20, 23)
PINK = (231, 41, 125)
GOLD = (196, 164, 106)


def font(name, size):
    return ImageFont.truetype(F + name, size * S)


def glitter_fill(size, seed):
    rng = np.random.default_rng(seed)
    w, h = size
    base = np.zeros((h, w, 3), np.float32)
    base[:] = PINK
    # fine sparkle noise
    n = rng.random((h, w))
    light = (n > 0.985)[..., None] * np.array([255, 225, 240]) * 0.9
    mid = ((n > 0.93) & (n <= 0.985))[..., None] * np.array([255, 120, 180]) * 0.35
    dark = (n < 0.05)[..., None] * np.array([150, 10, 70]) * 0.4
    shade = np.linspace(1.08, 0.88, h)[:, None, None]
    img = base * shade
    img = img * (1 - (n > 0.93)[..., None] * 0.35 - (n < 0.05)[..., None] * 0.4) + light + mid + dark
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    # a few bigger flecks
    d = ImageDraw.Draw(im)
    for _ in range(int(w * h / 900)):
        x, y = rng.integers(0, w), rng.integers(0, h)
        r = rng.integers(1, 3) * S
        c = (255, 240, 248) if rng.random() < 0.6 else (255, 214, 120)
        d.ellipse([x - r, y - r, x + r, y + r], fill=c)
    return im


def layout_words(words, fnt, maxw, draw):
    lines, cur = [], []
    for w in words:
        test = cur + [w]
        txt = ' '.join(t for t, _ in test)
        if draw.textlength(txt, font=fnt) <= maxw or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = [w]
    if cur:
        lines.append(cur)
    return lines


def render(spec, out):
    img = Image.new('RGB', (W, H), CREAM)
    # soft paper grain
    g = (np.random.default_rng(1).normal(0, 3.2, (H, W, 1))).repeat(3, 2)
    img = Image.fromarray(np.clip(np.asarray(img, np.float32) + g, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img)

    # kicker
    kf = ImageFont.truetype(F + 'Montserrat%5Bwght%5D.ttf', 24 * S)
    try:
        kf.set_variation_by_axes([600])
    except Exception:
        pass
    kick = spec['kicker'].upper()
    spaced = '  '.join(kick.split(' '))
    tw = d.textlength(spaced, font=kf)
    d.text(((W - tw) / 2, 40 * S), spaced, font=kf, fill=PINK)

    # headline: words tagged turn (glitter pink) or plain (ink)
    words = []
    for part in spec['headline']:
        is_turn = part.startswith('*')
        for w in part.strip('*').split():
            words.append((w, is_turn))
    size = spec.get('size', 100)
    import itertools
    best = None
    n = len(words)
    while best is None:
     hf = font('GildaDisplay-Regular.ttf', size)
     maxw = W - 100 * S
     for k in (2, 3):
        for cuts in itertools.combinations(range(1, n), k - 1):
            idx = (0,) + cuts + (n,)
            ls = [words[idx[j]:idx[j + 1]] for j in range(k)]
            wid = [d.textlength(' '.join(t for t, _ in l), font=hf) for l in ls]
            if max(wid) > maxw:
                continue
            lone = sum(1 for l in ls if len(l) == 1)
            score = (lone, k, max(wid) - min(wid))
            if best is None or score < best[0]:
                best = (score, ls)
        if best and best[0][0] == 0:
            break
     if (best is None or best[0][0] > 0) and size > 84:
        size -= 4; best = None
     elif best is None:
        raise SystemExit('cannot fit ' + spec['file'])
    lines = best[1]
    lh = int(size * 1.08 * S)
    y = 84 * S
    block_h = lh * len(lines)
    top_space = 430 * S - y
    y += max(0, (top_space - block_h) // 2) - 6 * S
    for line in lines:
        txt = ' '.join(t for t, _ in line)
        lw = d.textlength(txt, font=hf)
        x = (W - lw) / 2
        for i, (t, turn) in enumerate(line):
            piece = t + (' ' if i < len(line) - 1 else '')
            if turn:
                bb = d.textbbox((0, 0), t, font=hf)
                mask = Image.new('L', (bb[2] + 8 * S, bb[3] + 8 * S), 0)
                ImageDraw.Draw(mask).text((0, 0), t, font=hf, fill=255)
                gl = glitter_fill(mask.size, sum(map(ord, t)) % 1000)
                img.paste(gl, (int(x), int(y)), mask)
            else:
                d.text((x, y), t, font=hf, fill=INK)
            x += d.textlength(piece, font=hf)
        y += lh

    # photo, square in a square frame
    ph = Image.open(spec['photo']).convert('RGB')
    P = 850 * S
    ph = ph.resize((P, P), Image.LANCZOS)
    px, py = (W - P) // 2, 478 * S
    shadow = Image.new('L', (P + 80 * S, P + 80 * S), 0)
    ImageDraw.Draw(shadow).rectangle([40 * S, 52 * S, P + 40 * S, P + 52 * S], fill=70)
    shadow = shadow.filter(ImageFilter.GaussianBlur(18 * S))
    img.paste((180, 150, 150), (px - 40 * S, py - 40 * S), shadow)
    img.paste(ph, (px, py))
    d = ImageDraw.Draw(img)
    pad = 12 * S
    d.rectangle([px - pad, py - pad, px + P + pad, py + P + pad], outline=GOLD, width=2 * S)

    # bottom row: button + lockup
    by = 1365 * S
    bf = ImageFont.truetype(F + 'Poppins-SemiBold.ttf', 30 * S)
    label = 'Shop it on Etsy'
    lw = d.textlength(label, font=bf)
    bw, bh = lw + 120 * S, 76 * S
    bx = 60 * S
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=38 * S, fill=(255, 255, 255), outline=INK, width=2 * S)
    d.text((bx + 38 * S, by + 18 * S), label, font=bf, fill=INK)
    ax = bx + 38 * S + lw + 18 * S
    ay = by + bh // 2
    d.line([ax, ay, ax + 34 * S, ay], fill=PINK, width=4 * S)
    d.polygon([(ax + 36 * S, ay), (ax + 22 * S, ay - 11 * S), (ax + 22 * S, ay + 11 * S)], fill=PINK)

    lf = ImageFont.truetype(F + 'Poppins-SemiBold.ttf', 26 * S)
    sf = ImageFont.truetype(F + 'Poppins-Regular.ttf', 21 * S)
    l1 = 'THE DIGITAL INCOME EDIT™'
    l2 = 'www.thedigitalincomeedit.com'
    rx = W - 60 * S
    d.text((rx - d.textlength(l1, font=lf), by + 6 * S), l1, font=lf, fill=INK)
    d.text((rx - d.textlength(l2, font=sf), by + 44 * S), l2, font=sf, fill=PINK)

    img = img.resize((1000, 1500), Image.LANCZOS)
    img.save(out, optimize=True)


if __name__ == '__main__':
    specs = json.load(open(sys.argv[1]))
    for s in specs:
        render(s, os.path.join(sys.argv[2] if len(sys.argv) > 2 else 'out', s['file']))
        print('ok', s['file'])
