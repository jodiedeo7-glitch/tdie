from common import *
from services import S

SVC = S["etsy"]
CLIENT = "Bramblewick Paper Goods"
FILE = "DFY-Etsy-Listing-Pack_Proof-Sample.pdf"

TITLE = "Mushroom Recipe Cards Printable, Hand Painted Watercolor Recipe Card Set of 12, Cottagecore Kitchen Gift, 4x6 and 5x7 Download"
TAGS = ["mushroom recipe card", "printable recipes", "watercolor recipe", "cottagecore kitchen", "recipe card set", "4x6 recipe cards",
        "hand painted cards", "woodland kitchen", "foodie gift", "recipe binder", "mushroom decor", "5x7 recipe card", "bridal shower recipe"]
DESC = [
 ("", "Twelve recipe cards, each with a hand-painted watercolor mushroom, ready to print at home tonight. Fill them with the recipes you actually cook, or print a stack for a bridal shower recipe swap."),
 ("WHAT YOU GET", "• 12 recipe card designs, each a different mushroom painted by hand in watercolor\n• Every design in two sizes: 4x6 and 5x7 inches\n• A lined back for each size, so you can print double-sided\n• 2 print-ready PDFs plus a ZIP of high-resolution JPG files"),
 ("HOW IT WORKS", "1. Buy and download the files from your Etsy purchases page\n2. Print on heavy matte cardstock at home or at a print shop\n3. Trim along the guides\n\nThis is a digital download. No physical item will be shipped."),
 ("PRINTING TIPS", "• Matte cardstock (around 100 lb cover) shows the watercolor best\n• Set your printer to Actual Size, not Fit to Page\n• Print one test card first to check colours on your printer"),
 ("GOOD TO KNOW", "Every mushroom is my own original painting. The files are for personal use: print as many as you like for your own kitchen or as gifts. Please don't resell or share the files.\n\nBecause this is an instant digital download, it can't be returned. If a file won't open, message me and I'll sort it out."),
]
PROMPTS = [
 ("ET-1", "Mockup 1 (hero): cards fanned on a table", "Seedream 4.5 on Higgsfield (no person in frame)",
  "Real-world overhead photograph, square 1:1. Four blank white matte 4x6 cards fanned on a worn oak kitchen table next to a small pile of fresh brown cremini and pale oyster mushrooms, a sprig of thyme and a linen napkin. Cards sharp and fully in frame, faces flat to camera so artwork can be placed on them. Soft window light from the upper left, gentle real shadows. Mirrorless camera, 50mm lens at f/5.6, straight down. Photorealistic, true-to-life paper texture, a little soil on the table. No text, no artwork on the cards, no logos, no watermarks."),
 ("ET-2", "Mockup 2: close-up of paper texture", "Seedream 4.5 on Higgsfield (no person in frame)",
  "Real-world macro photograph, square 1:1. One blank white textured watercolor-paper card lying at a slight angle on cream linen, soft raking light across it to show the cotton paper grain, a single dried oak leaf touching the corner. Card face fills most of the frame so artwork can be placed on it. Soft side window light. Mirrorless camera, 90mm macro lens at f/4. Photorealistic, lifelike fibres and deckled edge. No text, no artwork on the card, no logos, no watermarks."),
 ("ET-3", "Mockup 3: recipe binder", "Seedream 4.5 on Higgsfield (no person in frame)",
  "Real-world photograph, square 1:1. An open sage green cloth recipe binder on a farmhouse kitchen counter, two blank white cards slotted into clear sleeves on the open pages, a wooden spoon and a small bowl of flour beside it. Soft daylight from a window behind, gentle shadows. Mirrorless camera, 35mm lens at f/4, three-quarter angle from above. Photorealistic, realistic plastic sleeve reflections kept subtle. No text, no artwork on the cards, no logos, no watermarks."),
 ("ET-4", "Mockup 4: card on a recipe stand", "Seedream 4.5 on Higgsfield (no person in frame)",
  "Real-world photograph, square 1:1. One blank white 5x7 card on a small wooden recipe stand on a kitchen counter, a pot simmering out of focus on the stove behind, a cutting board with sliced mushrooms in front. Card sharp and facing the camera so artwork can be placed on it. Warm late-afternoon window light. Mirrorless camera, 50mm lens at f/2.8, natural bokeh behind. Photorealistic, lived-in kitchen. No text, no artwork on the card, no logos, no watermarks."),
 ("ET-7", "Mockup 7: gift stack tied with twine", "Seedream 4.5 on Higgsfield (no person in frame)",
  "Real-world photograph, square 1:1. A stack of blank white cards tied with natural jute twine and a small sprig of dried lavender, resting on brown kraft paper beside a pair of scissors and a roll of twine. Top card faces the camera so artwork can be placed on it. Soft daylight, gentle shadows. Mirrorless camera, 50mm lens at f/4, slight angle from above. Photorealistic, real twine fibres and paper creases. No text, no artwork on the cards, no logos, no watermarks."),
 ("ET-8", "Mockup 8: printing at home", "Seedream 4.5 on Higgsfield (no person in frame)",
  "Real-world photograph, square 1:1. A compact home inkjet printer on a wooden desk with a freshly printed sheet of white cardstock resting in its output tray, the sheet facing up and flat enough that a printed layout can be placed on it, a paper trimmer and a mug of tea beside it. Soft daylight from a window to the side. Mirrorless camera, 35mm lens at f/4. Photorealistic, realistic plastic and paper surfaces, no brand names visible on the printer. No text, no logos, no watermarks."),
]
MOCK = [("ET-1", "Hero: the set in use"), ("ET-2", "Detail: the paper"), ("ET-3", "In a recipe binder"), ("ET-4", "On the counter"),
        ("GFX-5", "What's included"), ("GFX-6", "Size guide"), ("ET-7", "As a gift"), ("ET-8", "Print at home")]


def gfx(kind, w, h):
    if kind == "GFX-5":
        mini = "".join(f'<div style="background:#fff;border-radius:3px;box-shadow:0 2px 5px rgba(0,0,0,.12);display:flex;align-items:center;justify-content:center"><div style="width:48%;height:48%;border-radius:50% 50% 12% 12%;background:radial-gradient(circle at 40% 30%,#e7c9a6,#b4845c);opacity:.85"></div></div>' for _ in range(12))
        return f'''<div style="width:{w};height:{h};border-radius:12px;background:linear-gradient(160deg,#f3efe6,#e9e2d3);padding:10px;display:flex;flex-direction:column;border:1px solid rgba(200,169,106,.55)">
<div class="serif" style="font-size:13px;color:#3e4a2f;text-align:center">What's included</div><div style="flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:5px;margin:6px 0">{mini}</div>
<div style="font-size:7px;text-align:center;color:#3e4a2f;font-weight:700;letter-spacing:.1em">12 DESIGNS · 4x6 + 5x7 · PDF + JPG</div></div>'''
    return f'''<div style="width:{w};height:{h};border-radius:12px;background:linear-gradient(160deg,#f3efe6,#e9e2d3);padding:10px;position:relative;border:1px solid rgba(200,169,106,.55)">
<div class="serif" style="font-size:13px;color:#3e4a2f;text-align:center">Size guide</div>
<div style="position:absolute;left:18%;bottom:16%;width:40%;height:52%;border:2px dashed #7a8a5e;border-radius:4px;background:rgba(255,255,255,.7)"><div style="position:absolute;bottom:4px;left:6px;font-size:8px;font-weight:800;color:#3e4a2f">5x7 in</div></div>
<div style="position:absolute;left:44%;bottom:16%;width:34%;height:40%;border:2px solid #3e4a2f;border-radius:4px;background:#fff"><div style="position:absolute;bottom:4px;left:6px;font-size:8px;font-weight:800;color:#3e4a2f">4x6 in</div></div></div>'''


def slot(pid, cap, w, h):
    if pid.startswith("GFX"):
        return gfx(pid, w, h)
    return photo(pid, cap, w, h)


def build():
    assert len(TITLE) <= 140, len(TITLE)
    assert len(TAGS) == 13 and all(len(t) <= 20 for t in TAGS), [(t, len(t)) for t in TAGS if len(t) > 20]
    T = 7
    P = []
    thumbs = "".join(f'<div>{slot(a, b, "100%", "74px")}</div>' for a, b in MOCK[1:5])
    listing = f'''<div class="card" style="padding:14px;display:grid;grid-template-columns:1.1fr 1fr;gap:14px">
<div>{slot("ET-1", "Hero: the set in use", "100%", "250px")}<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:6px">{thumbs}</div></div>
<div><div class="xs muted">Bramblewick Paper Goods · Digital download</div><div class="b" style="font-size:12px;line-height:1.35;margin:4px 0 8px">{esc(TITLE)}</div>
<div class="xs"><b>Price:</b> set by the client</div><div class="rule"></div>
<div class="xs" style="line-height:1.6">✓ Digital download<br>✓ Instant download after purchase<br>✓ 2 PDFs + 1 ZIP of JPGs<br>✓ Original art by the shop owner</div>
<div style="margin-top:10px;background:#1a1417;color:#fff;border-radius:999px;text-align:center;padding:8px;font-weight:700;font-size:10px">Buy it now</div></div></div>'''
    cover = f'''<div class="kicker">{SVC['name']}</div>
<h1>One complete <span class="hl">Etsy listing</span>, ready to publish.</h1>
<p class="lede" style="margin:14px 0 16px">Title, all 13 tags, the full description, 8 mockups and the publishing settings, built from the client's own original art. This is one of the 5 (or 10) listings in the pack.</p>
<div style="position:relative">{listing}<div class="sticker bub" style="right:-18px;top:-40px">13 tags<br>8 mockups<br>1 listing</div></div>
<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-top:16px">
<div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:19px">{CLIENT}</div>
<div class="small muted">Elsie Bramwell paints watercolor mushrooms and botanicals and sells them as printables. Every design in this listing is her own original painting: no PLR, no prompt packs, no one else's art.</div></div>
<div class="fict" style="align-self:center">★ {FICTIONAL}</div></div>'''
    P.append(page(cover, CLIENT, 1, T))

    tg = "".join(f'<div class="card tight" style="display:flex;justify-content:space-between;align-items:center"><span class="b">{t}</span><span class="xs muted">{len(t)}/20</span></div>' for t in TAGS)
    P.append(page(f'''<div class="kicker">Title and tags</div><h2>Written for the <span class="hl">search bar</span>, not for a poem.</h2>
<div class="card" style="margin-top:12px"><div class="upper" style="color:var(--pink)">Title · {len(TITLE)} of 140 characters</div><div class="serif" style="font-size:18px;line-height:1.3;margin-top:4px">{esc(TITLE)}</div>
<div class="small muted" style="margin-top:6px">Leads with the phrase a buyer types ("mushroom recipe cards printable"), then the style, the count, the gift angle and both sizes.</div></div>
<div class="upper" style="color:var(--pink);margin:16px 0 8px">All 13 tags · each under Etsy's 20-character limit</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">{tg}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px">
<div class="card"><div class="upper" style="color:var(--pink)">How they're chosen</div><div class="small">Every tag is a phrase a real buyer would type, and none just repeat a single word from the title. Style, use, size and gift searches are all covered.</div></div>
<div class="hero"><div class="kicker">Checked before publishing</div><div class="small">Character counts, no trademarked words, no third-party names, nothing that promises what the file doesn't include.</div></div></div>''', CLIENT, 2, T))

    d = "".join(f'<div style="margin-bottom:10px">{f"<div class=upper style=color:var(--pink);margin-bottom:3px>{h}</div>" if h else ""}<div style="white-space:pre-line;font-size:11.2px;line-height:1.55">{esc(t)}</div></div>' for h, t in DESC)
    P.append(page(f'''<div class="kicker">The description</div><h2>Everything she'd ask, <span class="hl">answered before she asks.</span></h2>
<div style="display:grid;grid-template-columns:1.6fr 1fr;gap:16px;margin-top:12px">
<div class="card" style="padding:18px 20px">{d}</div>
<div class="grid" style="gap:10px;align-content:start">
<div class="card tight"><div class="upper" style="color:var(--pink)">First two lines</div><div class="small">What shows in search previews: what it is, and the one use that sells it.</div></div>
<div class="card tight"><div class="upper" style="color:var(--pink)">Digital, said plainly</div><div class="small">"No physical item will be shipped" heads off the "where is my package?" message.</div></div>
<div class="card tight"><div class="upper" style="color:var(--pink)">Her rights, protected</div><div class="small">Personal use only, original art named as hers.</div></div>
<div class="card tight"><div class="upper" style="color:var(--pink)">Printing help built in</div><div class="small">Actual Size is spelled out, so the cards print at the size she paid for.</div></div></div></div>''', CLIENT, 3, T))

    mocks = "".join(f'<div><div style="position:relative">{slot(a, b, "100%", "205px")}<div class="tag ink" style="position:absolute;left:8px;top:8px">{i+1}</div></div><div class="xs b" style="margin-top:4px">{b}</div></div>' for i, (a, b) in enumerate(MOCK))
    P.append(page(f'''<div class="kicker">The 8 mockups, in listing order</div><h2>Eight images, <span class="hl">eight different jobs.</span></h2>
<p class="lede" style="margin-bottom:12px">Photo scenes are generated with blank cards, then Elsie's own artwork files are placed onto them, so every mockup shows her real designs. Two are designed graphics: what's included and the size guide.</p>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">{mocks}</div>
<div class="card" style="margin-top:14px"><div class="upper" style="color:var(--pink)">Why this order</div><div class="small">1 sells the feeling, 2 proves the quality, 3 and 4 show it in a real kitchen, 5 and 6 answer "what do I get" and "what size", 7 sells the gift, 8 shows how easy printing is.</div></div>''', CLIENT, 4, T))

    ph = "".join(f'<div class="card tight"><div class="b small" style="color:var(--pink)">{p[0]} · {p[1]}</div><div style="margin-top:3px;line-height:1.45;font-size:10px">{esc(p[3])}</div></div>' for p in PROMPTS)
    P.append(page(f'''<div class="kicker">The mockup prompts</div><h2>Every photo scene, <span class="hl">written in full.</span></h2>
<div class="grid" style="gap:10px;margin-top:10px">{ph}</div>''', CLIENT, 5, T))

    rows = [("Category", "Paper and party supplies, recipe cards"), ("Type", "Digital files"), ("Who made it", "I did"), ("What is it", "A finished product"),
            ("When was it made", "2026"), ("Files", "Mushroom-Recipe-Cards-4x6.pdf · Mushroom-Recipe-Cards-5x7.pdf · Mushroom-Recipe-Cards-JPG.zip"),
            ("Price", "Set by the client"), ("Section", "Recipe Cards"), ("Renewal", "Automatic, as set by the client")]
    tb = "".join(f"<tr><td class='b' style='width:120px;font-size:11px;padding:10px 8px'>{a}</td><td style='font-size:11px;padding:10px 8px'>{b}</td></tr>" for a, b in rows)
    chk = ["Title, tags and description pasted and saved", "All 8 mockups uploaded in order, hero first", "All 3 files attached and opened after upload",
           "Listing previewed on phone and desktop", "Published, then opened live from the shop page to confirm it shows"]
    P.append(page(f'''<div class="kicker">Publishing</div><h2>Set up, published <span class="hl">and opened live.</span></h2>
<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:16px;margin-top:12px">
<div class="card"><table><tr><th>Listing setting</th><th>Value</th></tr>{tb}</table></div>
<div class="grid" style="gap:12px;align-content:start"><div class="card"><div class="upper" style="color:var(--pink);margin-bottom:6px">Publishing checklist</div><ul class="clean" style="font-size:11px">{''.join(f"<li>{c}</li>" for c in chk)}</ul></div>
<div class="hero"><div class="kicker">Her designs only</div><div class="small">The pack is built only from the client's own original designs. No PLR, no prompt packs, no affiliate products, no third-party art or names.</div></div></div></div>''', CLIENT, 6, T, zoom=1.12))
    P.append(order_page(SVC, CLIENT, 7, T, "portrait", "One complete listing: a search-led title, 13 tags, a full description, 8 mockups and the publishing settings. The pack is 5 or 10 of these, each built from your own designs."))
    return doc(P, "DFY Etsy Listing Pack: proof sample"), FILE, "portrait"
