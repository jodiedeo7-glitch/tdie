from common import *
from services import S

SVC = S["amazon"]
CLIENT = "Lilac Lane Nursery Finds"
FILE = "DFY-Amazon-Storefront-Launch_Proof-Sample.pdf"
DISC = "#ad As an Amazon Influencer I earn from qualifying purchases."
ID = "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference."
LIFE_TOOL = "Google Gemini first, client's persona reference sheet attached, then Nano Banana Pro 2K on Higgsfield"
FLAT_TOOL = "Seedream 4.5 on Higgsfield, 4K portrait 2:3, style reference and product sheet attached"

LOOKS = [
 dict(n=1, name="Soft Sage Nursery Corner", kind="Theme list", date="Day 1",
  items=["Sage green crib sheet, fitted, muslin", "Cream knit throw blanket with fringe", "Wooden wall shelf with three pegs", "Round jute rug, small",
         "Plush lamb toy in oatmeal", "Linen storage basket with handles", "Warm white dimmable night light"],
  listdesc="A calm sage and cream nursery corner. Soft muslin, natural wood and one very cuddly lamb. Everything linked in one list.",
  a=dict(fmt="Format B: shoppable collage", overlay="SAGE NURSERY / finds",
   prompt="Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a shoppable nursery finds collage for Pinterest, portrait 2:3, on a soft cream background with a faint linen texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: a sage green muslin fitted crib sheet folded, a cream knit throw with fringe, a small wooden peg shelf, a round jute rug, an oatmeal plush lamb, a linen storage basket with handles and a small warm white night light. Add three matching extras: a stack of board books, a sage knit baby hat and a eucalyptus sprig. Pack them around a central title so the canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small leaves and little sparkles. In the middle, set directly on the background, a large two-style title: \"SAGE NURSERY\" in a bold high-contrast serif in capitals with \"finds\" in a thick flowing brush script, deep forest green, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render. No logos, no brand names, no labels on products, no prices, no other text.",
   title="Sage Green Nursery Ideas: 7 Calm Amazon Finds for a Gender Neutral Nursery Corner",
   desc="Sage green nursery ideas for a calm, gender neutral corner: a muslin crib sheet, a cream knit throw, a little peg shelf, a jute rug, the softest oatmeal lamb, a linen basket and a warm night light for 3 am feeds. Soft colours, natural textures, nothing that shouts. It looks put together without looking like a showroom. Every piece is linked in my Amazon storefront. " + DISC + " #sagenursery #nurseryideas #genderneutralnursery",
   alt="Collage of sage and cream nursery items including a crib sheet, knit throw, peg shelf, jute rug, plush lamb, basket and night light around the title Sage Nursery finds."),
  b=dict(fmt="Lifestyle photo: detail shot of hands", pid="AZ-1B",
   prompt=ID + " Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo. Scene: a calm nursery corner in the late afternoon: the sage muslin crib sheet on the crib, the cream knit throw over the arm of a nursing chair, the wooden peg shelf on the wall with the oatmeal lamb sitting on it, the round jute rug and the linen basket on the floor, the night light glowing low. Format: detail shot of her hands smoothing the knit throw over the chair arm, her face not in frame. She wears an oversized oatmeal cardigan and a thin gold bracelet; nails bare. Her lilac enamel travel mug sits on the side table. Make it look like a good-quality photo taken on a phone: 26mm phone lens, natural light from a side window, realistic camera angle, real fabric texture, small real-life imperfections, nothing glossy. Portrait 2:3. No lettering, no signs, no logos, no text anywhere in the frame.",
   title="Calm Sage Nursery Corner on Amazon: The Cosy Reading Chair Setup I'd Copy Tomorrow",
   desc="This calm sage nursery corner is the reading chair setup I'd copy tomorrow: a cream knit throw over the chair, a little peg shelf holding the softest lamb, a jute rug for bare feet and a warm night light that won't wake anyone at 3 am. The muslin crib sheet and linen basket finish it off. Soft, natural and easy to keep tidy with a newborn. Every piece is linked in my Amazon storefront. " + DISC + " #sagenursery #nurserydecor #nurserycorner",
   alt="Close photo of hands smoothing a cream knit throw over a nursing chair in a sage nursery, with a wooden peg shelf, plush lamb, jute rug and glowing night light.")),
 dict(n=2, name="Hospital Bag, Packed Pretty", kind="Theme list", date="Day 2",
  items=["Quilted weekender bag in dusty lilac", "Soft button-front nursing pyjama set", "Nonslip cosy socks, two pairs", "Long phone charging cable, 10 ft",
         "Silk-feel pillowcase", "Newborn going-home set in cream knit", "Travel toiletry pouch set"],
  listdesc="Everything for the hospital bag, in soft lilac and cream. The long charging cable is the one everyone forgets.",
  a=dict(fmt="Format A: styled flat lay", overlay="HOSPITAL BAG / packed pretty",
   prompt="Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the items in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The open dusty lilac quilted weekender bag sits at the centre on rumpled cream linen, with the items laid around it as if being packed: the button-front nursing pyjamas folded, two pairs of cosy socks, a coiled long white charging cable, a silky pillowcase, a tiny cream knit going-home set and a travel toiletry pouch set. Tucked in around them, filling the frame edge to edge with almost no empty background: a small bunch of white ranunculus, a lip balm, a hair claw clip, a paperback book and a pair of newborn mittens. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, small real-life imperfections, photorealistic. Across the upper third, set directly on the photo, a large two-style title: \"HOSPITAL BAG\" in a bold high-contrast serif in capitals, with \"packed pretty\" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels on products, no prices, no other text.",
   title="Hospital Bag Checklist for Mom: 7 Pretty Amazon Finds I'd Actually Pack (Lilac Edition)",
   desc="A hospital bag checklist for mom, packed pretty: a lilac quilted weekender, button-front nursing pyjamas, cosy nonslip socks, a pillowcase that feels like home, a travel toiletry set, a tiny cream knit going-home outfit and a 10 foot charging cable, because the outlet is never near the bed. Pack it at 34 weeks and stop thinking about it. Every piece is linked in my Amazon storefront. " + DISC + " #hospitalbag #hospitalbagchecklist #newmom",
   alt="Overhead flat lay of a lilac quilted weekender bag on cream linen with nursing pyjamas, socks, a charging cable, pillowcase, knit baby outfit and toiletry pouches."),
  b=dict(fmt="Lifestyle photo: chin-down crop", pid="AZ-2B",
   prompt=ID + " Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo. Scene: her front hallway by the door, early morning, the packed dusty lilac quilted weekender bag on a wooden bench with the tiny cream knit going-home set folded on top. Format: chin-down crop from the shoulders to the knees, face out of frame, one hand resting on her pregnant belly and the other on the bag's handle. She wears the soft button-front nursing pyjama top under a long oatmeal cardigan, and cosy socks. Her lilac enamel travel mug sits on the bench. Hair worn in a low claw clip. Make it look like a good-quality photo taken on a phone: 26mm phone lens, soft morning light from the door's glass panel, realistic camera angle, real fabric texture, small real-life imperfections, nothing glossy. Portrait 2:3. No lettering, no signs, no logos, no text anywhere in the frame.",
   title="What's Actually in My Hospital Bag: The Lilac Weekender and Everything Inside It",
   desc="What's actually in my hospital bag, packed and waiting by the door: the lilac quilted weekender, nursing pyjamas soft enough for the whole stay, cosy socks with grips, my own pillowcase, a travel toiletry set and the tiniest cream knit going-home outfit. Plus the 10 foot charging cable, which the nurses will ask to borrow. Every piece is linked in my Amazon storefront. " + DISC + " #hospitalbag #whatsinmybag #thirdtrimester",
   alt="Chin-down photo of a pregnant woman in nursing pyjamas and a long cardigan by the front door, one hand on a lilac quilted bag with a cream knit baby outfit on top.")),
 dict(n=3, name="First Fall Walk", kind="Outfit look", date="Day 3",
  items=["Long camel wrap coat", "Cream cable-knit turtleneck", "High-rise straight-leg jeans", "White leather sneakers",
         "Baby carrier in oatmeal", "Knit baby bonnet in rust", "Crossbody bag in cream"],
  listdesc="The first fall walk with the baby. Warm, easy and good for the photo you'll want later.",
  a=dict(fmt="Format A: styled flat lay", overlay="FIRST FALL / walk",
   prompt="Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the outfit in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The outfit is laid out as if worn, pieces overlapping and touching, on warm wood floorboards: the long camel wrap coat open, the cream cable-knit turtleneck inside it, the straight-leg jeans below, white leather sneakers at the hem, the cream crossbody bag at the hip, and beside them the oatmeal baby carrier with the tiny rust knit bonnet resting on it. Each item matches its screenshot in colour, shape and detail. Tucked in around the outfit, filling the frame edge to edge with almost no empty background: scattered orange maple leaves, a takeaway coffee cup with no print, a pair of sunglasses, a small pumpkin and a knit baby blanket. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, small real-life imperfections, photorealistic. Across the upper third, set directly on the photo, a large two-style title: \"FIRST FALL\" in a bold high-contrast serif in capitals, with \"walk\" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels on products, no prices, no other text.",
   title="Postpartum Fall Outfit Idea: The First Walk With the Baby Look, All on Amazon",
   desc="A postpartum fall outfit idea for the first walk with the baby: a long camel wrap coat that closes over the carrier, a cream cable-knit turtleneck, easy straight-leg jeans and white sneakers you can slip on with one hand. The oatmeal carrier and a tiny rust knit bonnet finish the look. Warm enough for October, easy enough for four hours of sleep. Every piece is linked in my Amazon storefront. " + DISC + " #postpartumoutfit #falloutfit #momstyle",
   alt="Overhead flat lay of a camel coat, cream turtleneck, jeans, white sneakers, cream crossbody bag and an oatmeal baby carrier with a rust knit bonnet on wood floorboards."),
  b=dict(fmt="Lifestyle photo: over-the-shoulder walk-away", pid="AZ-3B",
   prompt=ID + " Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo. She is wearing every item in the third image, matching each one in colour and detail: the long camel wrap coat, the cream cable-knit turtleneck, straight-leg jeans, white leather sneakers, the cream crossbody bag on her left shoulder, and the oatmeal baby carrier on her front with the baby's rust knit bonnet just visible over the top. Format: over-the-shoulder walking away down a quiet tree-lined lane with orange leaves on the ground, her face turned slightly to the side, not the focus. Hair worn in a loose low bun. In one hand, her lilac enamel travel mug. Make it look like a good-quality photo taken on a phone: 26mm phone lens, soft golden afternoon light, realistic camera angle, real fabric texture, small real-life imperfections, nothing glossy. Portrait 2:3. No lettering, no signs, no logos, no text anywhere in the frame.",
   title="First Walk With the Baby This Fall: The Camel Coat Mom Outfit That Fits Over the Carrier",
   desc="Our first walk with the baby this fall, and the camel coat that made it easy: a long wrap coat that fits over the oatmeal carrier, a cream cable-knit turtleneck, straight-leg jeans and white sneakers. The rust knit bonnet peeking over the top is the best part. A cosy mom outfit that works for the coffee run and the photo you'll want later. Every piece is linked in my Amazon storefront. " + DISC + " #momoutfit #fallmomstyle #babywearing",
   alt="Woman walking away down a leafy lane in a camel coat, jeans and white sneakers, wearing an oatmeal baby carrier with a small rust knit bonnet visible over the top.")),
]

PROMPTS = []
for L in LOOKS:
    PROMPTS.append((f"AZ-{L['n']}A", f"Look {L['n']} pin 1: {L['a']['fmt']}", FLAT_TOOL, L["a"]["prompt"]))
    PROMPTS.append((L["b"]["pid"], f"Look {L['n']} pin 2: {L['b']['fmt']}", LIFE_TOOL, L["b"]["prompt"]))


def check():
    for L in LOOKS:
        for k in ("a", "b"):
            p = L[k]
            assert 60 <= len(p["title"]) <= 100, (L["n"], k, "title", len(p["title"]))
            assert 450 <= len(p["desc"]) <= 500, (L["n"], k, "desc", len(p["desc"]))
            assert 150 <= len(p["alt"]) <= 200, (L["n"], k, "alt", len(p["alt"]))
            assert DISC in p["desc"]


def copy(p, label):
    return f'''<div class="card tight"><div class="upper" style="color:var(--pink)">{label}</div>
<div class="b small" style="margin:3px 0">{esc(p['title'])} <span class="xs muted">({len(p['title'])})</span></div>
<div style="font-size:9.8px;line-height:1.45">{esc(p['desc'])} <span class="muted">({len(p['desc'])})</span></div>
<div class="muted" style="margin-top:4px;font-size:9.4px"><b>Alt:</b> {esc(p['alt'])} ({len(p['alt'])})</div></div>'''


def lookpages(L, n, T):
    items = "".join(f'<li>{esc(i)}</li>' for i in L["items"])
    head = f'''<div style="display:flex;align-items:baseline;gap:10px"><span class="kicker" style="margin:0">Look {L['n']} of 3 · {L['kind']}</span></div><h2>{L['name']}</h2>
<div style="display:grid;grid-template-columns:.85fr 1.4fr;gap:14px;margin-top:6px">
<div class="card"><div class="upper" style="color:var(--pink)">Idea List in her storefront</div><div class="serif" style="font-size:16px;margin:4px 0">{L['name']}</div><div class="xs muted" style="margin-bottom:6px">{esc(L['listdesc'])}</div><ul class="clean small">{items}</ul>
<div class="xs muted" style="margin-top:6px">Sourced live on build day: in stock, 4.0 stars or better with 100+ ratings, recorded by ASIN, added to the list by ASIN. No prices on any pin.</div></div>
<div class="grid" style="grid-template-columns:1fr 1fr;gap:10px">
<div><div class="xs b" style="margin-bottom:4px">Pin 1 · {L['a']['fmt']} · {L['date']}</div>{photo(f"AZ-{L['n']}A", L['a']['overlay'], "100%", "330px")}</div>
<div><div class="xs b" style="margin-bottom:4px">Pin 2 · {L['b']['fmt']} · 3 days later</div>{photo(L['b']['pid'], "Lifestyle photo", "100%", "330px")}</div></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px">{copy(L['a'], 'Pin 1 copy')}{copy(L['b'], 'Pin 2 copy')}</div>'''
    return page(head, CLIENT, n, T)


def build():
    check()
    T = 7
    P = []
    tiles = "".join(f'<div class="card tight" style="transform:rotate({r}deg)"><div class="tag">{L["kind"]}</div><div class="serif" style="font-size:17px;margin-top:5px">{L["name"]}</div><div class="xs muted">{len(L["items"])} items · Idea List · 2 pins</div></div>' for L, r in zip(LOOKS, (-2, 1.5, -1)))
    cover = f'''<div class="kicker">{SVC['name']}</div>
<h1>Three storefront looks, <span class="hl">each with its list and its pins.</span></h1>
<p class="lede" style="margin:14px 0 16px">Every look is a finished Idea List in the client's Amazon storefront plus two Pinterest pins, each carrying the #ad disclosure. This is 3 of the 10 in a launch.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
<div><div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:19px">{CLIENT}</div>
<div class="small muted">Carly Dawes runs an Amazon Influencer storefront for new and expecting moms. She's faceless: her lifestyle pins use her own AI persona, from her own reference sheet, with a lilac enamel travel mug as her signature prop.</div></div>
<div class="fict" style="margin-top:12px">★ {FICTIONAL}</div>
<div class="hero" style="margin-top:14px"><div class="kicker">Every pin</div><div class="small">Links to the look's Idea List. Carries "{DISC}" in the description. Never a price.</div></div></div>
<div style="position:relative" class="grid">{tiles}<div class="sticker bub" style="right:-14px;bottom:-50px">3 looks<br>3 lists<br>6 pins</div></div></div>'''
    P.append(page(cover, CLIENT, 1, T))
    rows = "".join(f"<tr><td class='b'>{L['name']}</td><td>{L['date']}: pin 1 ({L['a']['fmt'].split(':')[0]})</td><td>{L['date']} + 3 days: pin 2 (lifestyle)</td><td>{L['name']} Idea List</td></tr>" for L in LOOKS)
    P.append(page(f'''<div class="kicker">How a look is built</div><h2>List first. <span class="hl">Pins second.</span> Never on the same day.</h2>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:12px">
{''.join(f'<div class="card"><div class="num" style="font-size:26px">{i+1}</div><div class="b" style="margin-top:4px">{a}</div><div class="small muted">{b}</div></div>' for i, (a, b) in enumerate([("Source", "Products picked live on Amazon: in stock, well rated, in the look's colours, recorded by ASIN."), ("Build the list", "An Idea List in her storefront, titled for the look, every item added by ASIN."), ("Make pin 1", "A flat lay or shoppable collage, generated fresh. Amazon's photos are reference only."), ("Make pin 2", "A lifestyle photo of her persona using the items, posted 3 days after pin 1.")]))}</div>
<div class="card" style="margin-top:14px"><table><tr><th>Look</th><th>Pin 1</th><th>Pin 2</th><th>Both pins link to</th></tr>{rows}</table></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px">
<div class="card"><div class="upper" style="color:var(--pink)">What stays out of every image</div><div class="small">Logos, brand names, product labels, prices and anyone else's characters or trademarks.</div></div>
<div class="card"><div class="upper" style="color:var(--pink)">Her face stays hers</div><div class="small">Lifestyle pins favour detail shots, chin-down crops and walk-aways. Identity comes only from her reference sheet.</div></div></div>''', CLIENT, 2, T))
    for i, L in enumerate(LOOKS):
        P.append(lookpages(L, 3 + i, T))
    ph = "".join(f'<div class="card tight"><div class="b xs" style="color:var(--pink)">{p[0]} · {p[1]}</div><div class="xs muted">{p[2]}</div><div style="font-size:7.6px;line-height:1.35;margin-top:2px">{esc(p[3])}</div></div>' for p in PROMPTS)
    P.append(page(f'<div class="kicker">The six image prompts, in full</div><div class="grid" style="gap:7px;margin-top:6px">{ph}</div>', CLIENT, 6, T))
    P.append(order_page(SVC, CLIENT, 7, T, "portrait", "Three finished looks: three Idea Lists, six pins with titles, descriptions, alt text and the #ad disclosure, and every image prompt. The launch is ten of these."))
    return doc(P, "DFY Amazon Storefront Launch: proof sample"), FILE, "portrait"
