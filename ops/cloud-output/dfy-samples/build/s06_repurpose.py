from common import *
from services import S

SVC = S["repurpose"]
CLIENT = "The Pocket Plot Garden Club"
FILE = "DFY-Repurposing-Pack_Proof-Sample.pdf"
ART = "Your Windowsill Can Grow a Salad: Starting Seeds Indoors This Fall"
NEG = "No text, no lettering, no seed packets with words, no logos, no watermarks."

PROMPTS = [
 ("RP-1", "Pin 1 background: windowsill tray", "Seedream 4.5 on Higgsfield (no person in frame)",
  "Real-world photograph, portrait 2:3. A shallow terracotta-coloured seed tray full of bright green pea shoots and baby lettuce on a painted white kitchen windowsill, a small glass jug of water beside it, frosty autumn garden soft through the window. The tray sits in the lower half; the upper half is calm window light and soft blur, because a title will be set there. Cool morning daylight from the window, gentle backlight through the leaves. Mirrorless camera, 50mm lens at f/2.8, natural bokeh. Photorealistic, true-to-life leaf texture, a few grains of soil on the sill. " + NEG),
 ("RP-2", "Reel cover: first snip", "Google Gemini first (hands in frame), then Nano Banana Pro 2K on Higgsfield",
  "Real-world photograph, vertical 9:16. A woman's hands only, snipping pea shoots from a windowsill tray with small kitchen scissors into a white bowl. Rolled sleeve of a moss green knit cardigan, short unpainted nails. The top third is calm window and soft wall, because words will be placed there in the app. Soft morning window light from behind, leaves glowing. Mirrorless camera, 50mm lens at f/2, shallow depth of field. Photorealistic, real soil crumbs, natural hand position. " + NEG),
]

INVENTORY = [("Pinterest pins", 10, 1), ("Carousel", 1, 1), ("Threads posts", 8, 1), ("Reels", 2, 1), ("Facebook post", 1, 1), ("Email", 1, 1), ("Community post", 1, 0)]

PIN = dict(overlay=("Grow a Salad", "on a Windowsill"),
  title="Grow a Salad on Your Windowsill: Starting Seeds Indoors This Fall (Beginner Guide)",
  desc="You can grow a salad on your windowsill this fall with one shallow tray, a bag of seed-starting mix and a sunny spot. This beginner guide covers the four easiest crops to start indoors, how deep to sow, why you water from below and how to keep leggy seedlings from flopping over. Pea shoots are ready to snip in a few weeks, and lettuce follows soon after. Read the full guide and start your first tray this weekend. #indoorgardening #windowsillgarden #growyourownfood",
  alt="Photo of a seed tray of pea shoots and baby lettuce on a white kitchen windowsill, with the words Grow a Salad on a Windowsill set in dark green serif type across the top.")

SLIDES = [("Grow a salad", "on your windowsill", "Swipe for the whole method 👉"),
 ("What you need", "", "A sunny window · a shallow tray · seed-starting mix · a spray bottle"),
 ("Pick fast growers", "", "Pea shoots · arugula · loose-leaf lettuce · radish microgreens"),
 ("Sow shallow", "", "Press seeds onto the mix and barely cover them. Deep seeds sulk."),
 ("Water from below", "", "Pour water into the tray underneath. The roots drink, the leaves stay dry."),
 ("Turn it daily", "", "A quarter turn every morning stops them leaning toward the glass."),
 ("First snip", "", "Pea shoots are usually ready in two to three weeks. Cut above the lowest leaves."),
 ("Want the full guide?", "", "The whole method, with a shopping list, is at the link in bio. Save this for Saturday.")]

THREADS = "Your windowsill is a garden you haven't planted yet.\n\nOne shallow tray. Pea shoots, arugula, a bit of lettuce. Water from underneath, turn it every morning, and in a few weeks you're snipping a salad in your socks in November.\n\nI wrote the whole method up this week. Link in the reply."

REEL = [("0 to 2s", "Close on the tray, leaves backlit", "On screen: \"This salad grew on my windowsill\""),
 ("2 to 6s", "Hands press seeds into the tray (from last month's footage)", "On screen: \"4 seeds. 1 tray. No garden.\""),
 ("6 to 11s", "Water poured into the base tray", "On screen: \"Water from below\""),
 ("11 to 15s", "Tray turned a quarter turn", "On screen: \"Turn it every morning\""),
 ("15 to 21s", "Scissors snip pea shoots into a white bowl", "On screen: \"Snip. Eat. Regrow.\""),
 ("21 to 24s", "Bowl on the counter, hand drizzles dressing", "On screen: \"Full method: link in bio\"")]

FB = ("Raise your hand if your garden is finished for the year but you're not 🙋‍♀️\n\nYou can keep growing all winter on a sunny windowsill. One shallow tray, some seed-starting mix and the right seeds (pea shoots, arugula, loose lettuce, radish microgreens).\n\nThe two tricks that make it work: water from underneath and give the tray a quarter turn every morning.\n\nI put the whole method, with a shopping list, into this week's guide. It's in the comments 👇",
      "Here's the full windowsill salad guide:", "link to the article")

EMAIL = dict(subject="Your windowsill is a garden", preview="One tray, four seeds, salad by Thanksgiving-ish.",
 body=["Hi friend,", "The beds are put to bed. The garlic's in. And I am already restless.",
       "So this week I did what I do every November: I turned the kitchen windowsill into a tiny salad farm. It takes one shallow tray and about ten minutes to start.",
       "Here's the short version:", "• Pick fast growers: pea shoots, arugula, loose-leaf lettuce, radish microgreens\n• Sow shallow, barely covered\n• Water from below, never on the leaves\n• Give the tray a quarter turn every morning",
       "That's honestly most of it. The rest (the shopping list, how to stop leggy seedlings, when to cut) is in the full guide.",
       "BTN:Read the windowsill salad guide", "If you start a tray, hit reply and tell me what you planted. I read every one.", "Happy growing,\nJune"])

CSS6 = """<style>.slide{position:relative;width:150px;height:188px;border-radius:10px;overflow:hidden;box-shadow:0 14px 26px -14px rgba(214,46,115,.5);padding:14px 12px;display:flex;flex-direction:column;justify-content:space-between}
.sl-a{background:linear-gradient(160deg,#2F4A3A,#4c6b52);color:#F7F3EA}.sl-b{background:#F7F3EA;color:#2F4A3A;border:1px solid #d8d0bf}
.pinx{position:relative;width:250px;height:375px;border-radius:14px;overflow:hidden;box-shadow:0 24px 40px -18px rgba(214,46,115,.5);flex:none}
.mono{white-space:pre-line}</style>"""


def pin():
    a, b = PIN["overlay"]
    return f'''<div class="pinx">{photo("RP-1", "Windowsill tray", "100%", "100%", "border-radius:0;position:absolute;inset:0")}
<div style="position:absolute;left:0;right:0;top:0;height:46%;background:linear-gradient(#F7F3EA 55%,transparent)"></div>
<div style="position:absolute;left:14px;right:14px;top:34px;text-align:center" class="serif"><div style="font-size:30px;line-height:1.02;color:#2F4A3A">{a}<br><span style="color:#c9573f">{b}</span></div></div>
<div style="position:absolute;bottom:10px;left:0;right:0;text-align:center;font-size:6px;letter-spacing:.2em;font-weight:800;color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.5)">THE POCKET PLOT GARDEN CLUB</div></div>'''


def slide(i, s):
    cls = "sl-a" if i in (0, 7) else "sl-b"
    return f'''<div class="slide {cls}"><div class="xs b" style="letter-spacing:.14em;opacity:.8">{i+1}/8</div>
<div><div class="serif" style="font-size:{22 if i in (0, 7) else 18}px;line-height:1.05">{esc(s[0])}{'<br><span style="color:#E9876B">' + esc(s[1]) + '</span>' if s[1] else ''}</div><div style="font-size:8.6px;line-height:1.35;margin-top:7px">{esc(s[2])}</div></div>
<div class="xs" style="letter-spacing:.14em;font-weight:800;opacity:.7">POCKET PLOT</div></div>'''


def build():
    assert 60 <= len(PIN["title"]) <= 100 and 450 <= len(PIN["desc"]) <= 500 and 150 <= len(PIN["alt"]) <= 200, (len(PIN["title"]), len(PIN["desc"]), len(PIN["alt"]))
    assert len(THREADS) <= 500
    T = 8
    P = []
    cover = f'''{CSS6}
<div class="kicker">{SVC['name']}</div>
<h1>One article in. <span class="hl">24 finished assets</span> out.</h1>
<p class="lede" style="margin:14px 0 16px">Here are 6 of the 24, finished and ready to post, all made from one garden club article. Every one is written for its own platform: the pin, the carousel, the Threads post, the reel, the Facebook post and the email.</p>
<div style="display:grid;grid-template-columns:1fr 1.1fr;gap:20px;align-items:start">
<div><div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:19px">{CLIENT}</div>
<div class="small muted">June Calloway runs a small-space gardening club with a blog and an email list. The article: <b>"{ART}."</b> Voice: friendly, practical, a little dry.</div></div>
<div class="fict" style="margin-top:12px">★ {FICTIONAL}</div>
<div class="hero" style="margin-top:16px"><div class="kicker">In this sample</div><div class="serif" style="font-size:44px;line-height:1;color:#fff">6 <span style="font-size:20px">of 24</span></div><div class="small">1 pin · the carousel · 1 Threads post · 1 reel · the Facebook post · the email</div></div></div>
<div style="position:relative;height:420px">
<div style="position:absolute;left:-10px;top:0;transform:rotate(-4deg) scale(.9);transform-origin:top left">{pin()}</div>
<div style="position:absolute;right:-6px;top:20px;transform:rotate(6deg)">{slide(0, SLIDES[0])}</div>
<div style="position:absolute;right:10px;top:230px;transform:rotate(-3deg)">{slide(4, SLIDES[4])}</div>
<div class="sticker bub" style="left:-30px;top:300px">Ready<br>to post</div></div></div>'''
    P.append(page(cover, CLIENT, 1, T))

    inv = ""
    for name, total, shown in INVENTORY:
        boxes = "".join(f'<div style="width:24px;height:24px;border-radius:6px;{"background:linear-gradient(135deg,#D62E73,#FF8AC2);box-shadow:0 4px 10px -4px rgba(214,46,115,.7)" if k < shown else "background:#fff;border:1px solid rgba(200,169,106,.6)"}"></div>' for k in range(total))
        inv += f'<tr><td class="b" style="width:120px">{name}</td><td style="width:40px" class="serif hl">{total}</td><td><div style="display:flex;gap:5px;flex-wrap:wrap">{boxes}</div></td></tr>'
    art = f'''<div class="kicker">The source</div><h2>The one article <span class="hl">everything comes from.</span></h2>
<div class="card" style="margin:10px 0 16px;display:grid;grid-template-columns:1.4fr 1fr;gap:16px">
<div><div class="serif" style="font-size:18px;line-height:1.2">{ART}</div><div class="small muted" style="margin-top:6px">About 1,400 words on June's blog. Covers the four easiest crops to start indoors, sowing depth, watering from below, turning the tray, stopping leggy seedlings and when to make the first cut, plus a shopping list.</div></div>
<div class="small"><div class="upper" style="color:var(--pink);margin-bottom:5px">Ideas pulled from it</div><ul class="clean"><li>The four fast growers</li><li>Water from below</li><li>The quarter turn</li><li>Leggy seedlings, fixed</li><li>The first snip</li></ul></div></div>
<div class="kicker">The pack</div><h2>All 24. <span class="hl">The pink ones are in this sample.</span></h2>
<div class="card" style="margin-top:10px"><table>{inv}</table><div class="rule"></div><div class="small"><b>24 assets:</b> 10 Pinterest pins, 1 carousel, 8 Threads posts, 2 reels, 1 Facebook post, 1 email, 1 community post.</div></div>'''
    P.append(page(art, CLIENT, 2, T))

    pt = f'''{CSS6}<div style="display:grid;grid-template-columns:auto 1fr;gap:18px">
<div>{pin()}</div>
<div><div class="kicker">Asset 1 of 24 · Pinterest pin 1</div><h3>Pin 1, designed and written</h3>
<div class="upper" style="color:var(--pink);margin-top:6px">Title · {len(PIN['title'])} chars</div><div class="b small">{esc(PIN['title'])}</div>
<div class="upper" style="color:var(--pink);margin-top:6px">Description · {len(PIN['desc'])} chars</div><div class="small">{esc(PIN['desc'])}</div>
<div class="upper" style="color:var(--pink);margin-top:6px">Alt text · {len(PIN['alt'])} chars</div><div class="small">{esc(PIN['alt'])}</div>
<div class="xs" style="margin-top:6px"><b>Links to:</b> the article · <b>Board:</b> Indoor Gardening</div></div></div>
<div class="card" style="margin-top:18px"><div class="kicker">Asset 12 of 24 · Threads post 1</div>
<div style="display:flex;gap:8px;align-items:center;margin-bottom:6px"><div style="width:26px;height:26px;border-radius:50%;background:linear-gradient(135deg,#2F4A3A,#9DB39A)"></div><b>pocketplot.club</b><span class="tag gold" style="margin-left:auto">{len(THREADS)}/500 characters</span></div>
<div class="mono" style="font-size:13px;line-height:1.55">{esc(THREADS)}</div>
<div style="margin-top:8px;border-left:2px solid rgba(214,46,115,.35);padding-left:10px" class="small"><b>Reply, 1 minute later:</b> The full windowsill salad guide is here 👉 <span class="tag">link to the article</span></div></div>'''
    P.append(page(pt, CLIENT, 3, T, zoom=1.08))

    sl = "".join(slide(i, s) for i, s in enumerate(SLIDES))
    car = f'''{CSS6}<div class="kicker">Asset 11 of 24 · The carousel</div><h2>Eight slides, <span class="hl">one idea each.</span></h2>
<p class="lede" style="margin-bottom:14px">Built to be saved. The first slide makes the promise, the middle slides teach one step each, and the last slide sends her to the full guide through the link in bio.</p>
<div style="display:grid;grid-template-columns:repeat(4,150px);gap:18px 22px;justify-content:center">{sl}</div>
<div class="card" style="margin-top:18px"><div class="upper" style="color:var(--pink)">Caption</div><div class="small mono">Your garden's done for the year. Your windowsill isn't 🌱\n\nSave this for the weekend, grab a shallow tray and start with pea shoots. They're the fastest win.\n\nThe full guide, with a shopping list, is at the link in bio.\n\n#windowsillgarden #indoorgardening #growyourownfood #smallspacegardening</div></div>'''
    P.append(page(car, CLIENT, 4, T))

    rr = "".join(f"<tr><td class='b' style='color:var(--pink);width:62px'>{a}</td><td>{esc(b)}</td><td>{esc(c)}</td></tr>" for a, b, c in REEL)
    reel = f'''<div class="kicker">Asset 21 of 24 · Reel 1</div><h2>A 24-second reel, <span class="hl">shot list and all.</span></h2>
<div style="display:grid;grid-template-columns:200px 1fr;gap:18px;margin-top:12px">
<div>{photo("RP-2", "Reel cover: first snip", "200px", "356px")}<div class="xs muted" style="margin-top:6px">Cover frame, prompt RP-2</div></div>
<div><div class="card"><table><tr><th>Time</th><th>Shot</th><th>Text on screen</th></tr>{rr}</table></div>
<div class="card" style="margin-top:12px"><div class="upper" style="color:var(--pink)">Audio</div><div class="small">No voiceover. A calm acoustic track picked from the app's library on posting day.</div>
<div class="upper" style="color:var(--pink);margin-top:8px">Caption</div><div class="small mono">It's November and I'm still harvesting 🥗\n\nOne tray on a sunny windowsill: pea shoots, arugula, a bit of lettuce. Water from below and turn it every morning.\n\nThe full method is at the link in bio.</div></div>
<div class="hero" style="margin-top:12px"><div class="kicker">Footage</div><div class="small">Filmed on June's phone from a one-page shot list sent with the pack. Every clip is 2 to 6 seconds, so the edit is quick.</div></div></div></div>'''
    P.append(page(reel, CLIENT, 5, T))

    fb = f'''<div class="kicker">Asset 22 of 24 · Facebook post</div><h2>The Facebook post, <span class="hl">link in the first comment.</span></h2>
<div class="card" style="margin-top:12px">
<div style="display:flex;gap:8px;align-items:center;margin-bottom:8px"><div style="width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,#2F4A3A,#9DB39A)"></div><div><b>The Pocket Plot Garden Club</b><div class="xs muted">Page post · scheduled</div></div></div>
<div class="mono" style="font-size:13px;line-height:1.55">{esc(FB[0])}</div>
<div style="margin-top:10px;background:#f4f1ec;border-radius:12px;padding:10px 12px"><div style="display:flex;gap:6px;align-items:center"><div style="width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#2F4A3A,#9DB39A)"></div><b class="small">The Pocket Plot Garden Club</b><span class="tag gold" style="margin-left:auto">First comment · 5 minutes after posting</span></div>
<div style="font-size:12px;margin-top:6px">{esc(FB[1])}<br><span class="tag" style="margin-top:4px">{FB[2]}</span></div></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:16px">
<div class="card"><div class="upper" style="color:var(--pink)">Why the link waits</div><div class="small">Meta shows posts with a link in the body to fewer people. The post names the guide in words; the link goes in the first comment.</div></div>
<div class="card"><div class="upper" style="color:var(--pink)">What it asks for</div><div class="small">One thing: read the guide. The opening line gets the hands up, the middle gives two real tips, the close points down.</div></div>
<div class="hero"><div class="kicker">Checked live</div><div class="small">The post is not counted as done until the first comment with the link has been seen live.</div></div></div>'''
    P.append(page(fb, CLIENT, 6, T, zoom=1.15))

    body = ""
    for b in EMAIL["body"]:
        if b.startswith("BTN:"):
            body += f'<div style="text-align:center;margin:12px 0"><span style="display:inline-block;background:#2F4A3A;color:#F7F3EA;border-radius:999px;padding:10px 22px;font-weight:700;font-size:11px">{esc(b[4:])}</span></div>'
        else:
            body += f'<p class="mono" style="font-size:11.5px;line-height:1.55;margin-bottom:9px">{esc(b)}</p>'.replace("in the full guide.", 'in the <u style="color:#2F4A3A;font-weight:700">full guide</u>.')
    em = f'''<div class="kicker">Asset 23 of 24 · The email</div><h2>The email, <span class="hl">ready to send to her list.</span></h2>
<div style="display:grid;grid-template-columns:1.5fr 1fr;gap:16px;margin-top:12px">
<div class="card" style="padding:0;overflow:hidden"><div style="background:#f7f3ea;padding:10px 16px;border-bottom:1px solid rgba(200,169,106,.5)" class="small"><b>From:</b> June at Pocket Plot<br><b>Subject:</b> {esc(EMAIL['subject'])}<br><b>Preview:</b> {esc(EMAIL['preview'])}</div>
<div style="padding:16px 20px">{body}</div></div>
<div class="grid" style="gap:12px;align-content:start"><div class="card"><div class="upper" style="color:var(--pink)">One ask</div><div class="small">Read the guide. The link sits on the words of the button, and the same link goes on "full guide" earlier in the email.</div></div>
<div class="card"><div class="upper" style="color:var(--pink)">In her voice</div><div class="small">Written from the intake form's voice notes: short sentences, garden in-jokes, signs off as June.</div></div>
<div class="hero"><div class="kicker">Still in the full pack</div><div class="small">9 more pins, 7 more Threads posts, a second reel and the community post, all from the same article.</div></div></div></div>'''
    P.append(page(em, CLIENT, 7, T))
    P.append(order_page(SVC, CLIENT, 8, T, "portrait", "Six finished assets from one article: a pin with full copy, an eight-slide carousel, a Threads post, a reel with its shot list, a Facebook post with its first comment and an email. The full pack is 24, made the same way."))
    return doc(P, "DFY Repurposing Pack: proof sample"), FILE, "portrait"
