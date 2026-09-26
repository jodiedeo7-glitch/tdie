from common import *
from services import S

SVC = S["instagram"]
CLIENT = "Goosefeather Hollow Homestead"
HANDLE = "goosefeather.hollow"
FILE = "DFY-Viral-Instagram-Content-Calendar_Proof-Sample.pdf"

HANDS = "Google Gemini first (hands in frame), then Nano Banana Pro 2K on Higgsfield"
NOPERSON = "Seedream 4.5 on Higgsfield (no person in frame)"
NEG = "No text, no lettering, no labels with words, no logos, no watermarks, no brand packaging."

PROMPTS = [
 ("IG-1", "Day 1 reel cover: the pantry reset", HANDS,
  "Real-world photograph, vertical 9:16. Close, slightly high-angle shot of a woman's hands and forearms only, placing a clear glass jar of dried white beans onto an open wooden pantry shelf in a lived-in farmhouse kitchen. Rows of clear glass jars with plain blank kraft paper labels, a wicker basket of yellow onions, a folded linen tea towel. Rolled-up oatmeal cotton sweater sleeve, one thin gold ring. The top third of the frame is calm painted shelf wall with nothing important in it, because words will be placed there in the app. Soft window light from the left, late afternoon, gentle real shadows. Mirrorless camera, 35mm lens at f/2.8, natural bokeh on the back shelves. Photorealistic, true-to-life textures, natural imperfections: a few spilled beans, labels slightly uneven. " + NEG),
 ("IG-2", "Day 2 carousel cover: 7 things I stopped buying", NOPERSON,
  "Real-world overhead photograph, 4:5 portrait. A worn butcher block counter in a farmhouse kitchen holding a stack of folded linen kitchen towels, a round sourdough loaf on a board, three beeswax food wraps in muted green, a jar of golden homemade broth and a small bundle of fresh rosemary. The left half of the frame is open butcher block with nothing on it, because the title will be set there. Soft overcast daylight from a window above, even and gentle. Shot straight down on a mirrorless camera, 50mm lens, f/5.6, everything in crisp focus. Photorealistic, lifelike wood grain, crumbs and a knife mark or two on the board. " + NEG),
 ("IG-3", "Day 3 reel cover: apple butter on the stove", HANDS,
  "Real-world photograph, vertical 9:16. A heavy enamel pot of dark apple butter simmering on an old white farmhouse range, steam rising, a woman's hand in a rolled cream flannel sleeve stirring with a long wooden spoon. A bowl of red apples and a cinnamon stick on the counter beside it. The top third is calm tiled backsplash, because words will be placed there in the app. Warm practical light from the range hood plus soft daylight from a side window. Mirrorless camera, 50mm lens at f/2, shallow depth of field, natural bokeh on the apples. Cinematic realism, real steam, a small drip on the side of the pot. " + NEG),
 ("IG-4", "Day 4 single image: the year the garden failed", NOPERSON,
  "Real-world photograph, 4:5 portrait. A cedar raised garden bed at golden hour holding a few survivor squash plants among bare soil, a pair of muddy rubber garden boots and a steel trowel resting on the bed's edge, a weathered red barn soft in the background. Right-third subject, open sky and soft field on the left for the caption card. Low golden-hour sunlight, long real shadows. Mirrorless camera, 85mm lens at f/2.8, compressed background, natural bokeh. Photorealistic, true-to-life soil texture, chewed leaves, honest and a little imperfect. " + NEG),
 ("IG-5", "Day 5 carousel cover: fall canning checklist", NOPERSON,
  "Real-world overhead photograph, 4:5 portrait. A blue and white gingham tablecloth holding empty clean mason jars, a stack of new lids, a wide-mouth canning funnel, a jar lifter, a folded towel and a bowl of pears. The top half has open tablecloth with nothing on it, because the title will be set there. Soft window light, morning, gentle shadows. Shot straight down, mirrorless camera, 35mm lens at f/5.6. Photorealistic, realistic glass reflections, a few water droplets on the jars. " + NEG),
 ("IG-6", "Day 6 reel cover: label every jar in 10 minutes", HANDS,
  "Real-world photograph, vertical 9:16. A woman's hands only, peeling a blank cream sticker label off a sheet and pressing it onto a glass jar of rolled oats at a farmhouse kitchen table. Small scissors, a short stack of label sheets face down, a mug of coffee. Rolled-up soft grey sweatshirt sleeve. The top third is calm, a plain white wall, because words will be placed there in the app. Soft daylight from a window behind, bright and clean. Mirrorless camera, 50mm lens at f/2.8, natural bokeh. Photorealistic, true-to-life paper and glass texture, a slightly crooked label. " + NEG),
 ("IG-7", "Day 7 single image: slow Sunday on the porch", NOPERSON,
  "Real-world photograph, 4:5 portrait. A farmhouse porch in soft overcast light: a wooden rocking chair with a chunky cream knit blanket over the arm, a mug of hot apple cider steaming on a small side table, an old sheepdog asleep on the boards, the pasture and a split-rail fence beyond. Chair in the right third, open porch and sky on the left. Soft overcast daylight, even and quiet. Mirrorless camera, 35mm lens at f/4. Photorealistic, weathered wood, dog hair on the blanket, real and lived in. " + NEG),
 ("ST-1", "Day 3 story frame 1: poll", NOPERSON,
  "Real-world photograph, vertical 9:16. A single jar of fresh apple butter with a gingham cloth tied over the lid, sitting on a farmhouse windowsill with soft blurred orchard trees outside. The jar sits low in the frame; the upper half is calm window light and soft blur, because words and a poll sticker will be placed there in the app. Soft morning daylight. Mirrorless camera, 50mm lens at f/2, natural bokeh. Photorealistic, real glass and fabric texture. " + NEG),
 ("ST-2", "Day 3 story frame 2: question box", NOPERSON,
  "Real-world photograph, vertical 9:16. A wooden cutting board with halved red apples, a paring knife and a small pile of peels on a farmhouse counter, shot from above at a slight angle. Everything sits in the lower third; the upper two thirds are calm counter and soft shadow, because words and a question sticker will be placed there in the app. Soft side window light. Mirrorless camera, 35mm lens at f/4. Photorealistic, juicy cut surfaces, real knife marks. " + NEG),
 ("ST-3", "Day 3 story frame 3: link sticker", NOPERSON,
  "Real-world photograph, vertical 9:16. Six filled jars of apple butter cooling on a folded tea towel on a farmhouse counter, lids catching the light. Jars along the bottom quarter; the middle of the frame is calm soft wall, because words and a link sticker will be placed there in the app. Warm late-afternoon window light. Mirrorless camera, 50mm lens at f/2.8, natural bokeh. Photorealistic, real glass reflections, a small smear on one jar. " + NEG),
]

DAYS = [
 dict(d="Day 1 · Monday", fmt="Reel · 12 to 15 seconds", pid="IG-1", pat="Pattern 1: hands-only process reel",
  hook="The pantry reset I kept putting off", tag="Offer: Pantry Reset Printable Pack",
  cap="It took one Sunday afternoon and a stack of jars. Here's the order I did it in:\n\n1. Everything out. Yes, everything.\n2. Toss anything expired (it was a lot)\n3. Group by how you cook, not by food type\n4. Decant only what you use every week\n5. Label the jars last\n\nThe labels I used are in my Pantry Reset Printable Pack. It's in my link in bio 🫙\n\nSave this for the weekend you finally do yours.",
  tags="#pantryorganization #homesteadkitchen #pantryreset #farmhousekitchen #slowliving"),
 dict(d="Day 2 · Tuesday", fmt="Carousel · 8 slides", pid="IG-2", pat="Pattern 2: save-worthy list carousel",
  hook="7 things I stopped buying on the homestead", tag="Goal: saves and shares",
  cap="Not to be preachy. Just what actually stuck after three years out here.\n\nSlide 2: Paper towels (linen towels, washed weekly)\nSlide 3: Sandwich bread (one sourdough loaf, twice a week)\nSlide 4: Cling film (beeswax wraps)\nSlide 5: Boxed broth (scraps in the freezer, broth on Sunday)\nSlide 6: Salad dressing (jar, oil, vinegar, shake)\nSlide 7: Air freshener (a pot of simmering peels)\nSlide 8: Which one would you drop first?\n\nSave it for your next grocery list.",
  tags="#homesteading #simpleliving #frugalliving #zerowastehome #homesteadlife"),
 dict(d="Day 3 · Wednesday", fmt="Reel · quiet chore, no voiceover", pid="IG-3", pat="Pattern 3: quiet chore with one line of text",
  hook="3 hours. 1 pot. The whole house smells like fall.", tag="Free: Fall Canning Checklist",
  cap="Apple butter day 🍎\n\nPeel, chop, cook low and slow, stir when you walk past. That's really it.\n\nMy full recipe card is inside the free Fall Canning Checklist, link in bio.\n\nWhat's simmering in your kitchen this week?",
  tags="#applebutter #fallcanning #homesteadkitchen #fallbaking #cozyseason"),
 dict(d="Day 4 · Thursday", fmt="Single image · long caption", pid="IG-4", pat="Pattern 2 variant: honest story caption",
  hook="The year the garden failed", tag="Goal: comments",
  cap="Two summers ago almost nothing came up.\n\nThe squash got bugs. The tomatoes split. I stood out here with a trowel and honestly thought about quitting.\n\nWhat I changed the next spring:\n• Smaller beds I could actually keep up with\n• Planting what we eat, not what looks pretty on seed packets\n• One garden notebook, every day, even the boring days\n\nThis year the beds fed us all summer.\n\nIf your garden let you down this year, you're in good company. Tell me what grew and what didn't 👇",
  tags="#gardenfail #raisedbedgarden #homesteadgarden #growyourownfood #gardeninglife"),
 dict(d="Day 5 · Friday", fmt="Carousel · 7 slides", pid="IG-5", pat="Pattern 2: save-worthy list carousel",
  hook="Before you can a single jar, have these", tag="Free: Fall Canning Checklist",
  cap="The checklist I wish someone had handed me before my first canning weekend:\n\nSlide 2: Jars and new lids (never reuse lids)\nSlide 3: A big pot with a rack\nSlide 4: Jar lifter and funnel\nSlide 5: Clean towels, lots of them\nSlide 6: A tested recipe, not a guess\nSlide 7: A clear counter and a free afternoon\n\nThe printable version is free, link in bio. Tape it inside a cupboard door 🫙",
  tags="#canning #canningseason #foodpreservation #homesteadskills #fallcanning"),
 dict(d="Day 6 · Saturday", fmt="Reel · 10 seconds", pid="IG-6", pat="Pattern 1: hands-only process reel",
  hook="Label every jar in 10 minutes", tag="Offer: Pantry Reset Printable Pack",
  cap="Monday I showed you the pantry. Today, the labels.\n\nPrint, cut, peel, stick. Ten minutes for the whole shelf.\n\nThey're in the Pantry Reset Printable Pack with the shelf plan and a restock list. Link in bio 🏷️",
  tags="#pantrylabels #organizedhome #pantryorganization #homesteadkitchen #printables"),
 dict(d="Day 7 · Sunday", fmt="Single image · short caption", pid="IG-7", pat="Rest day: community question",
  hook="Slow Sunday", tag="Goal: comments",
  cap="No chores list today. Cider, the porch and a very tired dog.\n\nWhat does your slow Sunday look like? 🍂",
  tags="#slowsunday #farmhouseporch #slowliving #countrylife #homesteadlife"),
]

CSS3 = """<style>
.phone{width:168px;border-radius:26px;background:#1a1417;padding:7px;box-shadow:0 24px 40px -18px rgba(214,46,115,.55);flex:none}
.phone .scr{border-radius:20px;overflow:hidden;background:#fff}
.phone .top{display:flex;align-items:center;gap:5px;padding:6px 8px;font-size:7px;font-weight:700}
.phone .top i{width:14px;height:14px;border-radius:50%;background:linear-gradient(135deg,#7a8f5c,#e9c46a);display:inline-block}
.ovl{position:absolute;left:6px;right:6px;top:10px;padding:6px 4px;border-radius:8px;background:rgba(26,20,23,.38);text-align:center;font-weight:800;font-size:11px;line-height:1.15;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.45);z-index:3}
.cap{white-space:pre-line;font-size:8.6px;line-height:1.38}
.pr{font-size:7.1px;line-height:1.32;color:#5d5157;background:rgba(255,240,246,.7);border:1px dashed rgba(214,46,115,.35);border-radius:8px;padding:5px 7px}
</style>"""


def pm(pid):
    return next(p for p in PROMPTS if p[0] == pid)


def dayblock(x):
    tall = x["fmt"].startswith("Reel")
    h = "262px" if tall else "200px"
    ph = photo(x["pid"], pm(x["pid"])[1], "100%", h)
    return f'''<div class="card" style="display:flex;gap:14px;padding:12px 14px">
<div class="phone"><div class="scr"><div class="top"><i></i>{HANDLE}</div><div style="position:relative">{ph}<div class="ovl">{esc(x['hook'])}</div></div>
<div style="padding:5px 8px 7px;font-size:7px">♡ &nbsp;💬 &nbsp;➤ <span style="float:right">🔖</span></div></div></div>
<div style="flex:1;min-width:0">
 <div style="display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin-bottom:3px"><span class="serif" style="font-size:17px">{x['d']}</span><span class="tag ink">{x['fmt']}</span><span class="tag gold">{x['tag']}</span></div>
 <div class="xs" style="color:var(--pink);font-weight:700;margin-bottom:4px">{x['pat']} · On-screen text: "{esc(x['hook'])}"</div>
 <div class="cap">{esc(x['cap'])}</div>
 <div class="xs muted" style="margin:4px 0 5px">{x['tags']}</div>
 <div class="pr"><b style="color:var(--pink)">Image prompt {x['pid']}</b> · {esc(pm(x['pid'])[3])}</div>
</div></div>'''


def build():
    T = 7
    P = []
    phones = "".join(f'<div style="transform:rotate({r}deg);margin-top:{m}px"><div class="phone" style="width:150px"><div class="scr"><div class="top"><i></i>{HANDLE}</div><div style="position:relative">{photo(DAYS[i]["pid"], pm(DAYS[i]["pid"])[1], "100%", "230px")}<div class="ovl">{esc(DAYS[i]["hook"])}</div></div></div></div></div>' for i, r, m in [(0, -5, 20), (2, 2, 0), (5, 6, 30)])
    cover = f'''{CSS3}
<div style="display:grid;grid-template-columns:1fr 1.05fr;gap:24px">
<div style="padding-top:12px">
 <div class="kicker">{SVC['name']}</div>
 <h1>One week of a <span class="hl">research-built</span> Instagram calendar.</h1>
 <p class="lede" style="margin:14px 0">Seven finished posts: the format, the on-screen hook, the caption, the hashtags and a complete image prompt for every visual, plus a story set. Built from what's actually going viral for accounts like hers.</p>
 <div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:19px">{CLIENT}</div>
 <div class="small muted">Opal Abernathy runs a faceless homestead account: hands, kitchen, garden, porch. Sells a Pantry Reset Printable Pack and gives away a Fall Canning Checklist. Every call to action points to her link in bio, because Instagram carries no links.</div></div>
 <div style="margin-top:12px" class="fict">★ {FICTIONAL}</div>
</div>
<div style="display:flex;gap:14px;justify-content:center;position:relative;padding-top:6px">{phones}<div class="sticker bub" style="right:-6px;bottom:-40px">7 posts<br>10 prompts<br>1 story set</div></div>
</div>
<div class="hero" style="margin-top:26px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:14px 20px">
 <div><div class="serif" style="font-size:30px;color:#fff">3</div><div class="small">viral patterns from the research</div></div>
 <div><div class="serif" style="font-size:30px;color:#fff">7</div><div class="small">finished posts: 3 reels, 2 carousels, 2 singles</div></div>
 <div><div class="serif" style="font-size:30px;color:#fff">10</div><div class="small">complete image prompts</div></div>
 <div><div class="serif" style="font-size:30px;color:#fff">0</div><div class="small">links on Instagram. Every CTA points to the link in bio</div></div>
</div>'''
    P.append(page(cover, CLIENT, 1, T, "landscape"))

    pats = [("Hands-only process reels", "A chore shown start to finish from the hands, with one line of text in the first second. No face, no voiceover needed."),
            ("Save-worthy list carousels", "A short list with one item per slide and a question on the last slide. In this research they drew the most saves and shares."),
            ("Quiet chores", "A slow, calm clip of one chore with a single line of text. Sound on, no talking.")]
    pc = "".join(f'<div class="card"><div class="num" style="font-size:26px">0{i+1}</div><h3 style="margin-top:4px">{a}</h3><div class="small">{b}</div></div>' for i, (a, b) in enumerate(pats))
    wk = "".join(f'<tr><td class="b">{x["d"]}</td><td>{x["fmt"]}</td><td>{esc(x["hook"])}</td><td>{x["tag"]}</td></tr>' for x in DAYS)
    res = f'''<div class="kicker">Step one is research, not writing</div><h2>What the research found, <span class="hl">and how this week uses it.</span></h2>
<p class="lede" style="margin-bottom:12px">Before a word is written, the build studies 40+ outlier posts from 25+ similar accounts: posts that did far better than that account usually does. Three patterns came out on top for a faceless homestead account. This week uses all three.</p>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">{pc}</div>
<div style="display:grid;grid-template-columns:1.6fr 1fr;gap:14px;margin-top:14px">
<div class="card"><table><tr><th>Day</th><th>Format</th><th>Hook</th><th>Job</th></tr>{wk}</table></div>
<div class="hero" style="align-self:start"><div class="kicker">Rules this week follows</div><ul class="small" style="padding-left:14px"><li>No links anywhere. Every call to action says what's in the link in bio.</li><li>No earnings or income figures.</li><li>At most one selling post a day; the paid pack twice this week, never two days running.</li><li>Every visual has its own complete prompt.</li></ul></div></div>
<div class="xs muted" style="margin-top:8px">In a real build the research file lists every outlier post with its link and numbers. It is summarised here because this sample's client is fictional.</div>'''
    P.append(page(res, CLIENT, 2, T, "landscape"))
    n = 3
    for a, b in [(0, 1), (2, 3), (4, 5)]:
        P.append(page(f'{CSS3}<div class="grid" style="gap:12px">{dayblock(DAYS[a])}{dayblock(DAYS[b])}</div>', CLIENT, n, T, "landscape")); n += 1
    frames = [("ST-1", "Poll sticker", "Apple butter or applesauce? 🍎"), ("ST-2", "Question sticker", "What should I can next?"), ("ST-3", "Link sticker", "Free Fall Canning Checklist 👇")]
    fr = "".join(f'<div><div class="phone" style="width:132px"><div class="scr"><div style="position:relative">{photo(a, pm(a)[1], "100%", "226px")}<div class="ovl" style="top:40px">{esc(c)}<div style="margin:8px auto 0;width:80%;background:#fff;color:var(--ink);border-radius:8px;padding:5px;font-size:8px;text-shadow:none">{b}</div></div></div></div></div><div class="pr" style="margin-top:8px;width:132px"><b style="color:var(--pink)">{a}</b> · {esc(pm(a)[3][:170])}... (full prompt in the prompt file)</div></div>' for a, b, c in frames)
    last = f'''{CSS3}<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:16px">{dayblock(DAYS[6])}
<div class="card"><div class="kicker">Day 3 story set</div><h3>Three frames that turn a reel into replies</h3><div class="xs muted" style="margin-bottom:8px">Story link stickers are the one place a link is allowed on Instagram.</div><div style="display:flex;gap:10px">{fr}</div></div></div>'''
    P.append(page(last, CLIENT, 6, T, "landscape"))
    P.append(order_page(SVC, CLIENT, 7, T, "landscape", "One week: seven finished posts built on three researched patterns, ten complete image prompts and a story set, all pointing to the link in bio. The full service does this for a whole month, starting with the research."))
    return doc(P, "DFY Viral Instagram Content Calendar: proof sample"), FILE, "landscape"
