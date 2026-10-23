"""Found It pin: white handwritten lettering laid over a text-free photo of one product,
copied from Jodie's 23 Oct 2026 example ("I found this lamp on" / arrow / "Amazon ♡").
Usage:
python3 make_found_it_pin.py in.jpg out.jpg "I found this mushroom lamp on" [arrow_side]
arrow_side: left (default) or right, the side of the photo the arrow and "Amazon" sit on.
"""
import sys, os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
HAND = os.path.join(FS, 'ShadowsIntoLightTwo-Regular.ttf')
WHITE = (255, 255, 255, 255)
SH = (0, 0, 0, 190)

src, out, top = sys.argv[1:4]
side = sys.argv[4] if len(sys.argv) > 4 else 'left'

img = Image.open(src).convert('RGB')
W = 1000
img = img.resize((W, int(img.height * W / img.width)), Image.LANCZOS)
H = int(W * 1.5)
if img.height > H:
    y0 = (img.height - H) // 2
    img = img.crop((0, y0, W, y0 + H))
W, H = img.size
canvas = img.convert('RGBA')


def fit(text, maxw, start):
    s = start
    while s > 24:
        f = ImageFont.truetype(HAND, s)
        b = f.getbbox(text)
        if b[2] - b[0] <= maxw:
            return f
        s -= 2
    return ImageFont.truetype(HAND, s)


# wrap the top line onto two lines if it would get too small on one
words = top.split()
f_one = fit(top, W * 0.90, 110)
if f_one.size >= 74 or len(words) < 4:
    lines = [top]
    ft = f_one
else:
    cut = math.ceil(len(words) / 2)
    lines = [' '.join(words[:cut]), ' '.join(words[cut:])]
    ft = fit(max(lines, key=len), W * 0.86, 110)

layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(layer)
sd = ImageDraw.Draw(shadow)


def text(xy, s, font, anchor):
    sd.text((xy[0] + 2, xy[1] + 3), s, font=font, fill=SH, anchor=anchor)
    d.text(xy, s, font=font, fill=WHITE, anchor=anchor)


y = int(H * 0.035)
lh = int(ft.size * 1.05)
for ln in lines:
    text((W // 2, y), ln, ft, 'mt')
    y += lh

# "Amazon" + heart at the middle of one side, arrow curving up toward the centre
fa = ImageFont.truetype(HAND, 92)
ax = int(W * 0.06) if side == 'left' else int(W * 0.94)
ay = int(H * 0.52)
anchor = 'ls' if side == 'left' else 'rs'
word = 'Amazon'
text((ax, ay), word, fa, anchor)
wb = fa.getbbox(word)
ww = wb[2] - wb[0]
hx = ax + ww + 48 if side == 'left' else ax - ww - 48
hy = ay - 34
r = 30
heart = []
for t in range(0, 361, 4):
    a = math.radians(t)
    heart.append((hx + r * 16 * math.sin(a) ** 3 / 16,
                  hy - r * (13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)) / 16))
sd.polygon([(x + 2, y + 3) for x, y in heart], fill=SH)
d.polygon(heart, fill=WHITE)

# hand-drawn arrow above the word, curving up and in toward the product (as in the example)
dirn = 1 if side == 'left' else -1
sx = ax + dirn * ww * 0.30
sy = ay - 110
ex = sx + dirn * 150
ey = sy - 190
cx = sx - dirn * 10
cy = sy - 110
pts = []
for i in range(41):
    t = i / 40
    pts.append(((1 - t) ** 2 * sx + 2 * (1 - t) * t * cx + t * t * ex,
                (1 - t) ** 2 * sy + 2 * (1 - t) * t * cy + t * t * ey))
sd.line([(x + 2, y + 3) for x, y in pts], fill=SH, width=7, joint='curve')
d.line(pts, fill=WHITE, width=7, joint='curve')
ang = math.atan2(pts[-1][1] - pts[-4][1], pts[-1][0] - pts[-4][0])
for da in (2.5, -2.5):
    hx2 = ex + 40 * math.cos(ang + da)
    hy2 = ey + 40 * math.sin(ang + da)
    sd.line([(ex + 2, ey + 3), (hx2 + 2, hy2 + 3)], fill=SH, width=7)
    d.line([(ex, ey), (hx2, hy2)], fill=WHITE, width=7)

shadow = shadow.filter(ImageFilter.GaussianBlur(4))
canvas = Image.alpha_composite(canvas, shadow)
canvas = Image.alpha_composite(canvas, layer)
canvas.convert('RGB').save(out, quality=92)
print(out, canvas.size)
