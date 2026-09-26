from common import *
from services import S

SVC = S["persona"]
CLIENT = "Saltbox Cove Candle Co."
FILE = "30-Days-of-AI-Persona-Photo-Prompts_Proof-Sample.pdf"
ID = "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference."
TOOL = "Google Gemini first, Marnie's reference sheet attached, then Nano Banana Pro 2K on Higgsfield"
NEG = "No text, no lettering, no labels with words, no logos, no watermarks. Not a showroom, not a fashion set."

WORLD = [
 ("Where she lives", "A grey-shingled cottage above a small working harbour. Low ceilings, a cast-iron wood stove, wide pine floorboards, a kitchen table that's always half covered in order slips."),
 ("Where she works", "The old boathouse at the bottom of the garden, now her candle studio: steel pouring pots, rows of cooling jars on pine shelves, a big window onto the water."),
 ("Who's with her", "Pilot, a black Labrador who follows her everywhere and is usually a little damp."),
 ("What she wears", "Cream fisherman sweaters, striped long-sleeve tees, a waxed canvas apron, wide-leg linen trousers, yellow rain boots. Hair worn up in a clip or a loose braid. Never blazers, never glam."),
 ("Her signature prop", "A sea-glass green enamel mug with a chipped rim. It's in every frame she's in."),
 ("The feeling", "Salt air, hard-working hands, quiet and warm. Nice things that are used every day, never staged."),
]

PROMPTS = [
 ("PP-01", "Day 1 · Pouring wax in the boathouse", TOOL,
  ID + " Setting: her candle studio in an old boathouse, pine shelves of cooling glass jars behind her, a big window onto a grey harbour. Action: she carefully pours melted wax from a steel pouring pot into a row of empty amber jars on the workbench, concentrating. Wardrobe: a cream fisherman sweater with the sleeves pushed up, a waxed canvas apron, hair up in a tortoiseshell claw clip, small gold hoop earrings. Her sea-glass green enamel mug with a chipped rim sits on the workbench beside the jars. Register: hard-working and warm, real craft, nothing staged. Composition: she stands in the right third of the frame, the left side is calm window light and soft shelving with nothing important in it, face unobstructed. Lighting: soft overcast daylight from the harbour window, a faint rim of light on the rising steam. Camera: mirrorless, 35mm lens at f/2.8, natural bokeh on the back shelves. Photorealistic, true-to-life wax sheen and glass reflections, a few drips on the bench, real fabric texture. " + NEG),
 ("PP-02", "Day 2 · Dawn walk on the shingle beach", TOOL,
  ID + " Setting: the shingle beach below her cottage at dawn, the harbour wall and a few moored boats soft in the distance. Action: walking along the waterline with Pilot, her black Labrador, running just ahead, a wicker basket of driftwood on her arm, looking out at the water. Wardrobe: a long olive waxed jacket over a striped long-sleeve tee, wide-leg linen trousers rolled at the ankle, yellow rain boots, hair in a loose braid. Her sea-glass green enamel mug is in her free hand, steam rising. Composition: she walks in the right third, open sky and sea on the left, natural perspective. Lighting: soft dawn light, low and pale gold, gentle haze over the water. Camera: mirrorless, 85mm lens at f/2.8, compressed background, natural bokeh. Photorealistic, wet stones, real movement in the dog's coat, cinematic realism. " + NEG),
 ("PP-03", "Day 3 · Packing orders at the kitchen table", TOOL,
  ID + " Setting: her cottage kitchen table by the window, pine floorboards, the wood stove just visible behind. Action: wrapping a candle jar in plain cream tissue and tying a box with natural twine, a short stack of packed boxes beside her. Wardrobe: an oatmeal knit cardigan over a white tee, sleeves pushed up, a thin gold chain, hair up in a claw clip. Her sea-glass green enamel mug with a chipped rim sits on the table among the tissue. Composition: she sits in the right third, the left side is calm table and window light with nothing important in it, face unobstructed. Lighting: soft morning window light from the left, gentle real shadows. Camera: mirrorless, 50mm lens at f/2.8, shallow depth of field. Photorealistic, crinkled tissue, twine fibres, a pencil and order slips on the table. " + NEG),
 ("PP-04", "Day 4 · Evening by the wood stove", TOOL,
  ID + " Setting: her small cottage living room in the evening, the cast-iron wood stove glowing, a low shelf of books, one of her candles lit on the side table. Action: curled in a worn linen armchair reading a paperback, Pilot asleep on the rug at her feet. Wardrobe: a cream fisherman sweater, soft grey lounge trousers, thick wool socks, hair down and loose. Her sea-glass green enamel mug with a chipped rim is in her hand. Composition: the armchair sits in the right third, the left side is soft warm shadow and bookshelf, face unobstructed. Lighting: practical light only, the stove glow and the candle, warm and low, nothing brighter than the scene allows. Camera: mirrorless, 50mm lens at f/1.8, natural bokeh, slight grain. Photorealistic, real firelight falloff, lived-in textures, a throw slipping off the chair arm. " + NEG),
 ("PP-05", "Day 5 · Sea glass in the tide pools", TOOL,
  ID + " Setting: rocky tide pools at low tide below the harbour, seaweed and barnacled rocks, an overcast sky. Action: crouched at the edge of a pool, turning a piece of pale green sea glass in her fingers, a small canvas pouch of collected pieces beside her. Wardrobe: a navy striped long-sleeve tee under an open rain jacket, rolled linen trousers, yellow rain boots, hair in a low bun. Her sea-glass green enamel mug with a chipped rim rests on a flat rock beside her. Composition: she crouches in the right third, the left is open water and rock texture, face unobstructed in a three-quarter view. Lighting: soft overcast daylight, even and cool. Camera: mirrorless, 35mm lens at f/4. Photorealistic, wet rock sheen, real seaweed texture, damp denim-blue light. " + NEG),
]

MONTH = ["Pouring wax in the boathouse", "Dawn walk on the shingle beach", "Packing orders at the kitchen table", "Evening by the wood stove", "Sea glass in the tide pools",
 "Labelling jars at the workbench", "Harbour market stall, setting up", "Trimming wicks, close on her hands", "Rainy window, testing a new scent", "Pilot's muddy paws at the door",
 "Garden herbs for a new blend", "Loading the car for the post office", "Writing notes to customers", "Boat ride across the harbour", "Cleaning pouring pots at the sink",
 "Morning coffee on the cottage step", "Photographing products on driftwood", "Stacking firewood for winter", "Candle-making class at the studio", "Sunset on the harbour wall",
 "Sorting the month's orders", "Drying lavender in the rafters", "Stormy afternoon, lighting candles", "Fixing a fence with Pilot watching", "Unboxing a new batch of jars",
 "Walking home with fish and bread", "Sketching label ideas at the table", "Swim at the cove, towel and robe", "Sunday soup on the stove", "Month-end: the studio tidy, lights on"]


def pr(i):
    p = PROMPTS[i]
    return f'''<div class="card" style="display:grid;grid-template-columns:200px 1fr;gap:16px;padding:14px">
{photo(p[0], p[1], "200px", "300px")}
<div><div style="display:flex;gap:6px;align-items:center;margin-bottom:5px"><span class="serif" style="font-size:18px">{p[1]}</span></div><span class="tag ink">{p[0]}</span> <span class="tag gold">Copy-paste prompt</span>
<div style="font-size:9.6px;line-height:1.5;margin-top:7px;background:rgba(255,255,255,.7);border:1px dashed rgba(214,46,115,.35);border-radius:10px;padding:9px 11px">{esc(p[3])}</div>
<div class="xs muted" style="margin-top:5px"><b>Tool:</b> {p[2]}</div></div></div>'''


def build():
    T = 6
    P = []
    strip = "".join(f'<div style="transform:rotate({r}deg)">{photo(PROMPTS[i][0], PROMPTS[i][1].split(" · ")[1], "120px", "180px")}</div>' for i, r in [(0, -4), (1, 2), (2, -1.5), (3, 3), (4, -2)])
    cover = f'''<div class="kicker">{SVC['name']}</div>
<h1>Five finished persona prompts, <span class="hl">and the world they come from.</span></h1>
<p class="lede" style="margin:14px 0 16px">Every prompt is copy-paste ready and opens by locking her identity to the reference sheet. Each day is a different place, outfit and story in the persona's own world, so thirty photos read as thirty real days.</p>
<div style="display:flex;gap:10px;justify-content:center;margin:10px 0 22px">{strip}</div>
<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:14px">
<div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:19px">{CLIENT}</div>
<div class="small muted">Maren Ashby makes hand-poured candles in a coastal town and runs her brand without showing her own face. Her AI persona, Marnie, is the face of the brand, built from Maren's own reference sheet.</div></div>
<div><div class="fict">★ {FICTIONAL}</div><div class="hero" style="margin-top:10px"><div class="small">5 of 30 prompts shown, with their 5 photo slots. The full order is 30 prompts, 30 finished photos and this written world.</div></div></div></div>'''
    P.append(page(cover, CLIENT, 1, T))
    w = "".join(f'<div class="card"><div class="upper" style="color:var(--pink)">{a}</div><div style="font-size:10.8px;line-height:1.5;margin-top:4px">{esc(b)}</div></div>' for a, b in WORLD)
    P.append(page(f'''<div class="kicker">The persona's written world</div><h2>Before any prompt: <span class="hl">where Marnie actually lives.</span></h2>
<p class="lede" style="margin-bottom:14px">This page is what keeps thirty photos consistent. Every prompt pulls its place, clothes and props from here, so she's always the same woman in the same world.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">{w}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px">
<div class="hero"><div class="kicker">Never written in a prompt</div><div class="small">Her face, features, skin, eye colour, hair colour, hair length, body shape or age. Those come from the reference sheet alone. Writing them in words is what makes a persona drift.</div></div>
<div class="card"><div class="upper" style="color:var(--pink)">Written freely</div><div class="small">How her hair is worn, what she wears, jewellery, footwear, what she's doing, where she is and how the light falls.</div></div></div>''', CLIENT, 2, T, zoom=1.1))
    P.append(page(f'<div class="kicker">Prompts 1 and 2</div><div class="grid" style="gap:14px;margin-top:6px">{pr(0)}{pr(1)}</div>', CLIENT, 3, T))
    P.append(page(f'<div class="kicker">Prompts 3 and 4</div><div class="grid" style="gap:14px;margin-top:6px">{pr(2)}{pr(3)}</div>', CLIENT, 4, T))
    mm = "".join(f'<div style="display:flex;gap:6px;font-size:8.8px;padding:3px 0;border-bottom:1px solid rgba(200,169,106,.3);{"font-weight:700;color:var(--pink)" if i < 5 else ""}"><span style="width:18px">{i+1}</span><span>{esc(t)}</span></div>' for i, t in enumerate(MONTH))
    P.append(page(f'''<div class="kicker">Prompt 5, and the month</div><div class="grid" style="gap:14px;margin-top:6px">{pr(4)}
<div class="card"><div class="upper" style="color:var(--pink);margin-bottom:6px">The 30-day map · the five in pink are in this sample</div><div style="columns:2;column-gap:22px">{mm}</div>
<div class="xs muted" style="margin-top:6px">No setting or story repeats inside the month.</div></div></div>''', CLIENT, 5, T))
    P.append(order_page(SVC, CLIENT, 6, T, "portrait", "Five copy-paste prompts, each with its photo slot, the persona's written world and the full 30-day map. The order is all 30 prompts plus 30 finished photos."))
    return doc(P, "30 Days of AI Persona Photo Prompts: proof sample"), FILE, "portrait"
