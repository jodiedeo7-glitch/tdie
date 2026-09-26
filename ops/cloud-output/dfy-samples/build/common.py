"""Shared TDIE design system for the DFY proof sample PDFs.

Palette, type and components follow ops/cloud-kit/TDIE_DESIGN_RULES.md:
Luxury Cream base, Signature Hot Pink, Bubblegum, Muted Gold as a thin line only,
near-black text, Newsreader SemiBold headlines, Inter for everything else.
"""
import html, os

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, "images")
FICTIONAL = "Sample built for a fictional client."

DISCOUNTS = ("Membership Premium members 15% off. A service's first 2 clients get 25% off "
             "in exchange for a testimonial. The two do not stack.")

GRAIN = "url(data:image/png;base64," + open(os.path.join(HERE, "grain.b64")).read().strip() + ")"

CSS = r"""
@font-face{font-family:'Inter';font-style:normal;font-weight:100 900;src:url('fonts/Inter-normal-400.woff2') format('woff2');}
@font-face{font-family:'Newsreader';font-style:normal;font-weight:600;src:url('fonts/Newsreader-normal-600.woff2') format('woff2');}
:root{--cream:#FBF8F5;--pink:#D62E73;--bub:#FF8AC2;--gold:#C8A96A;--ink:#1A1417;--muted:#5d5157;--soft:#fff0f6;}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--cream);color:var(--ink);font-family:'Inter',sans-serif;font-size:10.5px;line-height:1.45;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{position:relative;overflow:hidden;page-break-after:always;break-after:page;
  background:
    radial-gradient(ellipse 55% 45% at 92% 6%, rgba(255,138,194,.30), transparent 70%),
    radial-gradient(ellipse 50% 40% at 0% 100%, rgba(214,46,115,.12), transparent 70%),
    radial-gradient(ellipse 40% 35% at 45% 55%, rgba(255,255,255,.9), transparent 70%),
    linear-gradient(160deg,#fdfbf9 0%,#fbf5f1 55%,#f9eef0 100%);}
.page::before{content:"";position:absolute;inset:0;background-image:GRAIN;opacity:.7;pointer-events:none;z-index:0}
.page:last-child{page-break-after:auto;break-after:auto}
.portrait{width:8.5in;height:11in;padding:.55in .6in .75in}
.landscape{width:11in;height:8.5in;padding:.5in .6in .7in}
.page > *{position:relative;z-index:1}
.brand{display:flex;justify-content:space-between;align-items:center;font-size:8.5px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--ink);margin-bottom:20px}
.brand .dot{display:inline-block;width:9px;height:9px;border-radius:50%;background:linear-gradient(135deg,var(--pink),var(--bub));margin-right:9px;vertical-align:-1px;box-shadow:0 0 0 3px rgba(255,138,194,.25)}
.brand .r{color:var(--pink)}
.foot{position:absolute;left:.6in;right:.6in;bottom:.32in;display:flex;justify-content:space-between;align-items:center;font-size:8px;letter-spacing:.06em;color:var(--muted);border-top:1px solid var(--gold);padding-top:7px;z-index:2}
.foot b{color:var(--pink);font-weight:700}
.kicker{font-weight:800;font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:var(--pink);margin-bottom:8px}
h1,h2,h3,.serif{font-family:'Newsreader',serif;font-weight:600;color:var(--ink);letter-spacing:-.01em}
h1{font-size:46px;line-height:1.02}
h2{font-size:28px;line-height:1.08;margin-bottom:6px}
h3{font-size:17px;line-height:1.15;margin-bottom:4px}
.hl{color:var(--pink)}
.lede{font-size:12.5px;line-height:1.5;color:#3a3035;max-width:560px}
.card{background:rgba(255,255,255,.80);border:1px solid rgba(200,169,106,.6);border-radius:16px;padding:14px 16px;
  box-shadow:0 22px 44px -22px rgba(214,46,115,.42),0 3px 10px rgba(26,20,23,.05),inset 0 1px 0 rgba(255,255,255,.9)}
.card.tight{padding:10px 12px}
.hero{position:relative;overflow:hidden;border-radius:18px;color:#fff;padding:16px 18px;
  background:linear-gradient(135deg,#D62E73 0%,#e8508f 55%,#FF8AC2 100%);
  box-shadow:0 26px 48px -20px rgba(214,46,115,.65),inset 0 1px 0 rgba(255,255,255,.35)}
.hero::after{content:"";position:absolute;top:-40%;left:-20%;width:80%;height:120%;background:linear-gradient(115deg,rgba(255,255,255,.28),rgba(255,255,255,0) 60%);transform:rotate(8deg);pointer-events:none}
.hero h1,.hero h2,.hero h3{color:#fff}
.hero .kicker{color:#fff;opacity:.92}
.sticker{position:absolute;width:104px;height:104px;border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;
  font-weight:800;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pink);line-height:1.15;padding:14px;
  background:#fff;box-shadow:0 14px 26px -10px rgba(214,46,115,.55),0 2px 4px rgba(0,0,0,.06);transform:rotate(-9deg);z-index:5}
.sticker::after{content:"";position:absolute;inset:6px;border-radius:50%;border:1.5px dashed rgba(214,46,115,.55)}
.sticker.bub{background:var(--bub);color:#fff}
.sticker.bub::after{border-color:rgba(255,255,255,.8)}
.sticker.sm{width:78px;height:78px;font-size:8px;padding:10px}
.pill{display:inline-block;padding:9px 20px;border-radius:999px;color:#fff;font-weight:800;font-size:10px;letter-spacing:.16em;text-transform:uppercase;text-decoration:none;
  background:linear-gradient(135deg,#D62E73,#FF6FAE);box-shadow:0 10px 20px -8px rgba(214,46,115,.7)}
.tag{display:inline-block;white-space:nowrap;padding:3px 9px;border-radius:999px;font-size:8px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;background:var(--soft);color:var(--pink);border:1px solid rgba(214,46,115,.25)}
.tag.gold{background:#fbf5ea;color:#8a6d34;border-color:rgba(200,169,106,.6)}
.tag.ink{background:var(--ink);color:#fff;border-color:var(--ink)}
.rule{height:1px;background:var(--gold);margin:12px 0}
.grid{display:grid;gap:14px}
.muted{color:var(--muted)}
.small{font-size:9px}
.xs{font-size:8px}
.b{font-weight:700}
.upper{text-transform:uppercase;letter-spacing:.14em;font-weight:800;font-size:8px}
.fict{display:inline-flex;align-items:center;gap:8px;padding:7px 14px;border-radius:999px;background:#fff;border:1.5px dashed var(--pink);color:var(--pink);font-weight:800;font-size:9.5px;letter-spacing:.06em;box-shadow:0 8px 18px -10px rgba(214,46,115,.6)}
.photo{position:relative;overflow:hidden;border-radius:14px;background:
   radial-gradient(ellipse 70% 60% at 70% 30%, rgba(255,255,255,.95), transparent 70%),
   linear-gradient(145deg,#f6e9e4 0%,#efdfe3 45%,#f7efe6 100%);
   border:1px solid rgba(200,169,106,.55);box-shadow:inset 0 0 0 6px rgba(255,255,255,.55),0 16px 30px -18px rgba(214,46,115,.45)}
.photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.photo .ph{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end;padding:10px 12px;color:#6b5a60}
.photo .ph .lens{position:absolute;top:50%;left:50%;width:44px;height:44px;margin:-30px 0 0 -22px;border-radius:50%;border:2px solid rgba(214,46,115,.45);box-shadow:0 0 0 7px rgba(255,255,255,.7),0 0 0 8px rgba(200,169,106,.5)}
.photo .ph .lens::after{content:"";position:absolute;inset:11px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fff,rgba(214,46,115,.45))}
.photo .ph .cap{font-size:7.5px;line-height:1.3;background:rgba(255,255,255,.82);border-radius:8px;padding:5px 7px;border:1px solid rgba(200,169,106,.45)}
.photo .ph .cap b{color:var(--pink);letter-spacing:.1em;text-transform:uppercase;font-size:7px}
table{border-collapse:collapse;width:100%}
th{font-size:7.5px;text-transform:uppercase;letter-spacing:.14em;color:var(--pink);text-align:left;font-weight:800;padding:6px 8px;border-bottom:1px solid var(--gold)}
td{padding:7px 8px;vertical-align:top;border-bottom:1px solid rgba(200,169,106,.28);font-size:9.6px}
ul.clean{list-style:none}
ul.clean li{padding-left:15px;position:relative;margin-bottom:4px}
ul.clean li::before{content:"";position:absolute;left:0;top:5px;width:7px;height:7px;border-radius:50%;background:linear-gradient(135deg,var(--pink),var(--bub))}
a{color:var(--pink)}
.num{font-family:'Newsreader',serif;font-weight:600;font-size:34px;line-height:1;color:var(--pink)}
""".replace("GRAIN", GRAIN)


def esc(s):
    return html.escape(s, quote=False)


def page(body, client, n, total, orient="portrait", extra_cls="", zoom=1.0):
    if zoom != 1.0:
        body = f'<div style="zoom:{zoom}">{body}</div>'
    return f"""<section class="page {orient} {extra_cls}">
<div class="brand"><div><span class="dot"></span>THE DIGITAL INCOME EDIT™</div><div class="r">DFY PROOF SAMPLE</div></div>
{body}
<div class="foot"><span><b>{FICTIONAL}</b> &nbsp;·&nbsp; Client: {client}</span><span>{n} / {total}</span></div>
</section>"""


def photo(pid, prompt_label, w="100%", h="200px", style="", title=""):
    """A photo slot. If images/<pid>.jpg or .png exists it is used; otherwise a designed placeholder."""
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        p = os.path.join(IMG_DIR, pid + ext)
        if os.path.exists(p):
            return f'<div class="photo" style="width:{w};height:{h};{style}"><img src="images/{pid}{ext}"></div>'
    t = f"<br>{title}" if title else ""
    return (f'<div class="photo" style="width:{w};height:{h};{style}"><div class="ph"><div class="lens"></div>'
            f'<div class="cap"><b>Photo {pid}</b>{t}<br>{prompt_label}</div></div></div>')


def order_page(svc, client, n, total, orient="portrait", closing=""):
    """Closing page: what the full service includes, price display, order word, discounts. All from canon / DFY doc."""
    items = "".join(f"<li>{esc(x)}</li>" for x in svc["full"])
    por = orient == "portrait"
    body = f"""
<style>.op-por h2{{font-size:40px}} .op-por .lede{{font-size:14px;max-width:none}} .op-por ul.clean li{{font-size:12px;margin-bottom:7px}} .op-por .grid4 .card{{padding:16px}} .op-por .grid4 .b{{font-size:12px}}</style>
<div class="{'op-por' if por else ''}">
<div style="display:grid;grid-template-columns:{'1fr' if por else '1.25fr 1fr'};gap:22px;margin-top:10px">
  <div>
    <div class="kicker">What you just looked at</div>
    <h2>This was one slice. <span class="hl">Here is the whole order.</span></h2>
    <p class="lede" style="margin:8px 0 14px">{closing}</p>
    <div class="card"><div class="upper" style="color:var(--pink);margin-bottom:8px">The full {esc(svc['name'])} includes</div><ul class="clean" style="{'columns:2;column-gap:18px' if por and len(svc['full'])>5 else ''}">{items}</ul></div>
  </div>
  <div style="position:relative">
    <div class="hero" style="padding:22px 22px 24px">
      <div class="kicker">Price</div>
      <div class="serif" style="font-size:22px;line-height:1.2;color:#fff">{esc(svc['price'])}</div>
      <div class="rule" style="background:rgba(255,255,255,.55)"></div>
      <div class="kicker">Order word</div>
      <div class="serif" style="font-size:17px;line-height:1.25;color:#fff">{esc(svc['word']).replace(' / ', ' · ')}</div>
      {f'<div class="small" style="margin-top:10px;opacity:.95">{esc(svc["time"])}</div>' if svc.get('time') else ''}
    </div>
    <div class="card" style="margin-top:14px"><div class="upper" style="color:var(--pink);margin-bottom:5px">Discounts</div><div class="small">{esc(DISCOUNTS)}</div></div>
    <div style="margin-top:18px;text-align:center"><a class="pill" href="{svc['url']}">DM me {esc(svc['dm'])} on Skool</a>
    <div class="xs muted" style="margin-top:8px">Ordering: DM the word, fill in the short intake form, then pay the link I send you.</div></div>
    <div class="sticker sm" style="right:-16px;bottom:-30px">Real work, real scope</div>
  </div>
</div>
<div class="grid4" style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:{'34px' if por else '22px'}">
 <div class="card tight"><div class="num" style="font-size:24px">1</div><div class="b">DM the word</div><div class="xs muted">Send me the order word on Skool.</div></div>
 <div class="card tight"><div class="num" style="font-size:24px">2</div><div class="b">Short intake form</div><div class="xs muted">So the build fits your business.</div></div>
 <div class="card tight"><div class="num" style="font-size:24px">3</div><div class="b">Payment link</div><div class="xs muted">I send it once the form is in.</div></div>
 <div class="card tight"><div class="num" style="font-size:24px">4</div><div class="b">Your finished build</div><div class="xs muted">Built for you, like the pages before this one.</div></div>
</div>
<div style="margin-top:16px" class="fict">★ {FICTIONAL} Every name, number and detail in it is made up so you can judge the work.</div>
</div>
"""
    return page(body, client, n, total, orient)


def doc(pages_html, title):
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{esc(title)}</title><style>{CSS}</style></head><body>{''.join(pages_html)}</body></html>"""
