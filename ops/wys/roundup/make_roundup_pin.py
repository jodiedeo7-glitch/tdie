"""Amazon-list roundup pin: headline lettering laid over a look photo, copied from Jodie's
'Spooky Cute HALLOWEEN DECOR You'll Love This Year' example (pink script / heavy black caps /
white script line with emoji). Usage:
python3 make_roundup_pin.py in.jpg out.jpg "Pink Thanksgiving" "TABLE DECOR" "You'll Love This Year" "🥧💗" [#line1hex]
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
SCRIPT = os.path.join(FS, 'pacifico-latin-400-normal.woff')
CAPS = os.path.join(FS, 'anton-latin-400-normal.woff')
SUB = os.path.join(FS, 'dancing-script-latin-700-normal.woff')
EMOJI = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'

PINK = (236, 72, 145)
INK = (26, 20, 23)
WHITE = (255, 255, 255)

src, out, l1, l2, l3 = sys.argv[1:6]
emo = sys.argv[6] if len(sys.argv) > 6 else ''
if len(sys.argv) > 7:
    PINK = tuple(int(sys.argv[7].lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

img = Image.open(src).convert('RGB')
W = 1000
img = img.resize((W, int(img.height * W / img.width)), Image.LANCZOS)
H = int(W * 1.5)
img = img.crop((0, 0, W, H)) if img.height >= H else img
W, H = img.size
canvas = img.convert('RGBA')


def fit(path, text, maxw, start):
    s = start
    while s > 20:
        f = ImageFont.truetype(path, s)
        if f.getbbox(text)[2] - f.getbbox(text)[0] <= maxw:
            return f
        s -= 2
    return ImageFont.truetype(path, s)


f1 = fit(SCRIPT, l1, W * 0.82, 140)
f2 = fit(CAPS, l2, W * 0.70, 130)
f3 = fit(SUB, l3, W * 0.62, 68)

# soft light haze at the very top so the lettering reads (feathered, never a box)
haze = Image.new('L', (W, H), 0)
hd = ImageDraw.Draw(haze)
hd.ellipse((-W * 0.15, -H * 0.20, W * 1.15, H * 0.36), fill=70)
haze = haze.filter(ImageFilter.GaussianBlur(70))
white = Image.new('RGBA', (W, H), (255, 245, 248, 255))
canvas = Image.composite(white, canvas, haze)

layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(layer)
sd = ImageDraw.Draw(shadow)


def line(font, text, y, fill, stroke, sw, shade):
    b = font.getbbox(text, stroke_width=sw)
    w = b[2] - b[0]
    x = (W - w) / 2 - b[0]
    sd.text((x + 3, y + 6), text, font=font, fill=shade, stroke_width=sw, stroke_fill=shade)
    d.text((x, y), text, font=font, fill=fill, stroke_width=sw, stroke_fill=stroke)
    return y + (b[3] - b[1])


y = 26
y = line(f1, l1, y, PINK, WHITE, 7, (120, 30, 70, 120)) - 4
y = line(f2, l2, y, INK, WHITE, 6, (0, 0, 0, 90)) + 4

# subtitle + emoji measured together
b3 = f3.getbbox(l3, stroke_width=2)
w3 = b3[2] - b3[0]
esz = int((b3[3] - b3[1]) * 1.05)
ew = (esz + 4) * len(emo)
x3 = (W - (w3 + (14 if emo else 0) + ew)) / 2 - b3[0]
sd.text((x3 + 2, y + 4), l3, font=f3, fill=(60, 20, 40, 170), stroke_width=2, stroke_fill=(60, 20, 40, 170))
d.text((x3, y), l3, font=f3, fill=WHITE, stroke_width=3, stroke_fill=(150, 25, 80))
if emo:
    ef = ImageFont.truetype(EMOJI, 109)
    ex = x3 + b3[0] + w3 + 14
    for ch in emo:
        e = Image.new('RGBA', (140, 140), (0, 0, 0, 0))
        ImageDraw.Draw(e).text((0, 0), ch, font=ef, embedded_color=True)
        e = e.crop(e.getbbox()).resize((esz, esz), Image.LANCZOS)
        layer.alpha_composite(e, (int(ex), int(y + b3[1] + (b3[3] - b3[1] - esz) / 2 - 2)))
        ex += esz + 4

shadow = shadow.filter(ImageFilter.GaussianBlur(6))
canvas.alpha_composite(shadow)
canvas.alpha_composite(layer)
canvas.convert('RGB').save(out, quality=92)
print(out, canvas.size)
