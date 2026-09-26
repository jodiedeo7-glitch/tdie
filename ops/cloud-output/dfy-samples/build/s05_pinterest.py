from common import *
from services import S

SVC = S["pinterest"]
CLIENT = "Wildwren Planner Co."
FILE = "DFY-30-Days-of-Pinterest_Proof-Sample.pdf"

NEG = "No text, no lettering, no logos, no watermarks, no brand names on anything."
PROMPTS = [
 ("PIN-1", "Pin 1 background: Sunday planning table", "Seedream 4.5 on Higgsfield (no person in frame)",
  "Real-world overhead photograph, portrait 2:3. A wooden kitchen table on a Sunday afternoon: an open spiral planner with blank pages, a sharpened pencil, a mug of tea, a small jar of dried lavender and a few autumn leaves near the edge. The bottom half is calm open wood with nothing on it, because a title will be set there. Soft window light from the left, long gentle shadows. Mirrorless camera, 35mm lens at f/5.6, shot straight down. Photorealistic, true-to-life wood grain and paper texture, a tea ring on the table. " + NEG),
 ("PIN-5", "Pin 5 background: fridge meal plan", "Seedream 4.5 on Higgsfield (no person in frame)",
  "Real-world photograph, portrait 2:3. The door of a cream vintage-style fridge in a bright family kitchen, a blank printed weekly grid held on with two wooden magnets, a child's crayon drawing beside it, a bowl of apples on the counter below. The upper half is calm fridge door, because a title will be set there. Soft daylight from a window to the right. Mirrorless camera, 50mm lens at f/4, gentle depth of field. Photorealistic, realistic enamel reflections, a smudge or two on the door. " + NEG),
]

PINS = [
 dict(n=1, layout="Editorial cover", overlay=("Your Autumn", "Reset Starts Here"),
  title="Autumn Reset Planner Printable: Plan Meals, Budget and Chores in One Sunday Sitting",
  desc="This autumn reset planner printable puts your meals, budget and chores on one page set, so Sunday planning takes one cup of tea instead of the whole afternoon. It has a weekly meal grid, a simple spending tracker, a chore rotation the kids can follow and a brain dump page for everything else. Print it at home on regular paper, clip it to the fridge and start the week knowing what's for dinner. #autumnplanner #printableplanner #sundayreset #mealplanning",
  alt="Overhead photo of an open planner, pencil and mug of tea on a wooden table with autumn leaves, with the words Your Autumn Reset Starts Here set across the bottom half.",
  board="Printable Planners", when="Day 1 · 8:00 PM"),
 dict(n=2, layout="Number lead", overlay=("7 Pages", "That Save Sundays"),
  title="7 Printable Planner Pages That Save Your Sunday (Meal Plan, Budget, Chores and More)",
  desc="Seven printable planner pages that do the Sunday thinking for you: a weekly meal plan, a grocery list sorted by aisle, a spending tracker, a bill calendar, a chore chart, a school-week overview and a brain dump page. Each one fits on a single sheet, prints in black and white and works on a clipboard or in a binder. Pick the three you need most and start there. The rest will be waiting when you're ready. #plannerpages #printables #weeklyplanner #organizedmom",
  alt="Graphic listing seven printable planner pages with the number 7 in large type and the words Pages That Save Sundays on a sage green background with small cream page icons.",
  board="Printable Planners", when="Day 2 · 8:00 PM"),
 dict(n=3, layout="Colour block", overlay=("Budget Without", "the Spreadsheet"),
  title="Simple Monthly Budget Printable for Families Who Hate Spreadsheets (Print and Go)",
  desc="A simple monthly budget printable for families who have tried the spreadsheet and quietly given up. One page for the money coming in, one for the bills going out, and one small box for the fun money so nobody feels punished. Fill it in with a pencil on the first of the month, check it on Sundays and adjust as you go. No formulas, no apps, no logins to forget. Just paper that sits on the fridge where everyone can see it. #budgetprintable #familybudget #moneyplanner",
  alt="Sage and cream colour block graphic with the words Budget Without the Spreadsheet in large serif type above a small illustrated budget page with three labelled boxes.",
  board="Budget and Money Printables", when="Day 3 · 8:00 PM"),
 dict(n=4, layout="Quote card", overlay=("Plan Weeks,", "Not Days"),
  title="Plan Weeks, Not Days: The Sunday Planning Habit That Makes Busy Weeks Feel Calmer",
  desc="Plan weeks, not days. When you only plan today, every morning starts with the same scramble. When you give Sunday twenty minutes, the week already knows what's for dinner, which bills are due and who is doing the dishes on Thursday. This is the one habit behind every page in the Autumn Reset Planner, and you can start it this Sunday with nothing but a pencil and a printed weekly grid. Save this for the Sunday you want a calmer week. #weeklyplanning #sundayreset #plannerideas",
  alt="Quote card in cream with a thin sage border reading Plan Weeks, Not Days in large serif type, with a coral quote mark and the words The Sunday Habit underneath.",
  board="Planning Tips", when="Day 4 · 8:00 PM"),
 dict(n=5, layout="Torn paper", overlay=("Meal Plan", "in 20 Minutes"),
  title="How to Meal Plan in 20 Minutes a Week With One Printable Grid on the Fridge",
  desc="How to meal plan in about twenty minutes a week: write down the three dinners everyone already likes, add two new ones, and fill the last two nights with leftovers and a freezer meal. Put it on a printable grid on the fridge so nobody has to ask what's for dinner. The grocery list on the back sorts itself by aisle, which cuts the shop down too. This fridge grid is page one of the Autumn Reset Planner and prints on regular paper. #mealplanning #mealplanprintable #familydinners",
  alt="Photo of a weekly meal plan grid held on a cream fridge with wooden magnets, under a torn paper strip reading Meal Plan in 20 Minutes in dark green serif type.",
  board="Meal Planning", when="Day 5 · 8:00 PM"),
]

CSS5 = """<style>
.pin{position:relative;width:250px;height:375px;border-radius:14px;overflow:hidden;box-shadow:0 24px 40px -18px rgba(214,46,115,.5),0 2px 6px rgba(0,0,0,.08);flex:none;font-family:'Inter'}
.pin .ser{font-family:'Newsreader',serif;font-weight:600;letter-spacing:-.01em}
.pin .lock{position:absolute;left:0;right:0;bottom:10px;text-align:center;font-size:6px;letter-spacing:.2em;font-weight:800;text-transform:uppercase}
.copy{font-size:9.2px;line-height:1.42}
.cnt{font-size:7.5px;color:#8b7d83;font-weight:600}
</style>"""
SAGE, DEEP, CREAM, CORAL = "#9DB39A", "#2F4A3A", "#F7F3EA", "#E9876B"


def pin_html(p):
    a, b = p["overlay"]
    L = p["layout"]
    if L == "Editorial cover":
        return f'''<div class="pin">{photo("PIN-1", "Sunday planning table", "100%", "100%", "border-radius:0;position:absolute;inset:0")}
<div style="position:absolute;left:0;right:0;bottom:0;height:48%;background:linear-gradient(transparent,{CREAM} 38%)"></div>
<div style="position:absolute;left:16px;right:16px;bottom:34px;text-align:center"><div class="ser" style="font-size:25px;line-height:1.02;color:{DEEP}">{a}<br><span style="color:{CORAL}">{b}</span></div></div>
<div class="lock" style="color:{DEEP}">Wildwren Planner Co.</div></div>'''
    if L == "Number lead":
        pages = "".join(f'<div style="width:26px;height:34px;background:{CREAM};border-radius:3px;box-shadow:0 3px 6px rgba(0,0,0,.15);transform:rotate({r}deg)"></div>' for r in (-8, -3, 2, 6, -4, 3, -6))
        return f'''<div class="pin" style="background:radial-gradient(circle at 70% 20%,#b6c9b2,{SAGE} 60%,#86a083)">
<div class="ser" style="position:absolute;left:18px;top:14px;font-size:150px;line-height:1;color:{CREAM}">7</div>
<div style="position:absolute;left:18px;right:18px;top:176px"><div class="ser" style="font-size:24px;line-height:1.05;color:{DEEP}">{a}<br>{b}</div></div>
<div style="position:absolute;left:18px;right:18px;bottom:36px;display:flex;gap:4px;justify-content:center">{pages}</div>
<div class="lock" style="color:{DEEP}">Wildwren Planner Co.</div></div>'''
    if L == "Colour block":
        return f'''<div class="pin" style="background:{CREAM}">
<div style="position:absolute;left:0;right:0;top:0;height:56%;background:linear-gradient(160deg,{DEEP},#3f5f4b)"></div>
<div style="position:absolute;left:18px;right:18px;top:40px"><div class="xs" style="color:{SAGE};font-weight:800;letter-spacing:.2em">PRINT AND GO</div><div class="ser" style="font-size:28px;line-height:1.02;color:{CREAM};margin-top:6px">{a}<br><span style="color:{CORAL}">{b}</span></div></div>
<div style="position:absolute;left:40px;right:40px;top:150px;height:132px;background:#fff;border-radius:6px;box-shadow:0 14px 24px -10px rgba(0,0,0,.35);padding:10px;transform:rotate(-3deg)">
 <div style="font-size:6.5px;font-weight:800;color:{DEEP};letter-spacing:.14em">MONTHLY BUDGET</div>
 {''.join(f'<div style="margin-top:6px;border:1px solid {SAGE};border-radius:3px;height:26px;padding:3px 5px;font-size:6px;color:{DEEP}">{t}</div>' for t in ("Money in", "Bills out", "Fun money"))}</div>
<div class="lock" style="color:{DEEP}">Wildwren Planner Co.</div></div>'''
    if L == "Quote card":
        return f'''<div class="pin" style="background:radial-gradient(circle at 30% 20%,#fffdf8,{CREAM} 70%)">
<div style="position:absolute;inset:12px;border:1.5px solid {SAGE};border-radius:8px"></div>
<div class="ser" style="position:absolute;left:24px;top:40px;font-size:70px;color:{CORAL};line-height:1">“</div>
<div style="position:absolute;left:26px;right:26px;top:108px;text-align:center"><div class="ser" style="font-size:34px;line-height:1.02;color:{DEEP}">{a}<br><span style="color:{CORAL}">{b}</span></div>
<div style="margin:18px auto 0;width:40px;height:2px;background:{SAGE}"></div><div style="font-size:7px;letter-spacing:.2em;font-weight:800;color:{DEEP};margin-top:10px">THE SUNDAY HABIT</div></div>
<div class="lock" style="color:{DEEP}">Wildwren Planner Co.</div></div>'''
    return f'''<div class="pin">{photo("PIN-5", "Fridge meal plan", "100%", "100%", "border-radius:0;position:absolute;inset:0")}
<div style="position:absolute;left:-6px;right:-6px;top:36px;padding:16px 20px 18px;background:{CREAM};clip-path:polygon(0 8%,6% 0,14% 6%,24% 1%,33% 7%,45% 0,57% 6%,68% 1%,79% 7%,90% 0,100% 6%,100% 92%,93% 100%,82% 94%,70% 100%,58% 95%,46% 100%,35% 94%,22% 100%,11% 95%,0 100%);box-shadow:0 8px 16px rgba(0,0,0,.2)">
<div class="ser" style="font-size:28px;line-height:1.02;color:{DEEP};text-align:center">{a}<br><span style="color:{CORAL}">{b}</span></div></div>
<div class="lock" style="color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.5)">Wildwren Planner Co.</div></div>'''


def copyblock(p):
    return f'''<div class="copy">
<div style="display:flex;gap:6px;align-items:center;margin-bottom:6px"><span class="serif" style="font-size:20px">Pin {p['n']}</span><span class="tag ink">{p['layout']}</span><span class="tag gold">{p['when']}</span></div>
<div class="upper" style="color:var(--pink)">Title <span class="cnt">{len(p['title'])} chars (60 to 100)</span></div><div class="b" style="margin-bottom:6px">{esc(p['title'])}</div>
<div class="upper" style="color:var(--pink)">Description <span class="cnt">{len(p['desc'])} chars (450 to 500)</span></div><div style="margin-bottom:6px">{esc(p['desc'])}</div>
<div class="upper" style="color:var(--pink)">Alt text <span class="cnt">{len(p['alt'])} chars (150 to 200)</span></div><div style="margin-bottom:6px">{esc(p['alt'])}</div>
<div class="xs"><b>Board:</b> {p['board']} &nbsp;·&nbsp; <b>Links to:</b> the Autumn Reset Planner product page &nbsp;·&nbsp; <b>Overlay:</b> {len((p['overlay'][0]+' '+p['overlay'][1]).split())} words</div></div>'''


def build():
    for p in PINS:
        assert 60 <= len(p["title"]) <= 100, (p["n"], len(p["title"]))
        assert 450 <= len(p["desc"]) <= 500, (p["n"], len(p["desc"]))
        assert 150 <= len(p["alt"]) <= 200, (p["n"], len(p["alt"]))
    T = 6
    P = []
    fan = "".join(f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg) scale(.72);transform-origin:top left">{pin_html(PINS[i])}</div>' for i, x, y, r in [(1, 0, 60, -6), (0, 105, 10, 2), (3, 200, 80, 6)])
    cover = f'''{CSS5}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
<div style="padding-top:10px"><div class="kicker">{SVC['name']}</div>
<h1>Five finished pins, <span class="hl">designed, written</span> and scheduled.</h1>
<p class="lede" style="margin:14px 0">Every pin is a finished design in the client's brand, with its title, a 450 to 500 character description, alt text, board and posting slot. This is what 5 of her 30 look like.</p>
<div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:19px">{CLIENT}</div>
<div class="small muted">Tessa Lark sells printable planners for busy families from her own site. Brand colours: sage, deep green, cream and a coral accent. Every pin in this set points to her Autumn Reset Planner.</div></div>
<div style="margin-top:12px" class="fict">★ {FICTIONAL}</div></div>
<div style="position:relative;height:520px">{fan}<div class="sticker bub" style="left:30px;top:350px">5 of 30<br>pins<br>shown</div></div></div>'''
    P.append(page(cover, CLIENT, 1, T))
    n = 2
    for i in (0, 2):
        blocks = "".join(f'<div class="card" style="display:flex;gap:16px;align-items:flex-start">{pin_html(PINS[j])}{copyblock(PINS[j])}</div>' for j in (i, i + 1))
        P.append(page(f'{CSS5}<div class="grid" style="gap:14px">{blocks}</div>', CLIENT, n, T)); n += 1
    sched = "".join(f"<tr><td class='b'>{p['when']}</td><td>Pin {p['n']}</td><td>{esc(p['overlay'][0] + ' ' + p['overlay'][1])}</td><td>{p['board']}</td><td><span class='tag'>Scheduled</span></td></tr>" for p in PINS)
    layouts = "".join(f'<span class="tag" style="margin:2px">{p["layout"]}</span>' for p in PINS)
    P.append(page(f'''{CSS5}<div style="display:flex;gap:16px;align-items:flex-start" class="card">{pin_html(PINS[4])}{copyblock(PINS[4])}</div>
<div style="display:grid;grid-template-columns:1.5fr 1fr;gap:14px;margin-top:14px">
<div class="card"><div class="upper" style="color:var(--pink);margin-bottom:6px">The schedule, as loaded into her Pinterest</div><table><tr><th>Slot</th><th>Pin</th><th>Overlay</th><th>Board</th><th>Status</th></tr>{sched}</table></div>
<div class="grid" style="gap:10px"><div class="card"><div class="upper" style="color:var(--pink)">Five layouts, no repeats</div><div style="margin-top:5px">{layouts}</div></div>
<div class="hero"><div class="kicker">Checked on every pin</div><div class="small">Overlay 3 to 5 words. Title, description and alt text inside Pinterest's limits (counts shown on each pin). No prices on any pin. Each pin opened in the scheduler after loading.</div></div></div></div>''', CLIENT, 4, T))
    P.append(page(f'''{CSS5}<div class="kicker">The whole order at pin size</div><h2>Five pins side by side, <span class="hl">the way her board will look.</span></h2>
<div style="display:flex;gap:10px;margin-top:16px;justify-content:center">{''.join(f'<div style="transform:scale(.55);transform-origin:top center;width:138px">{pin_html(p)}</div>' for p in PINS)}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:-150px">
<div class="card"><div class="upper" style="color:var(--pink)">Why they don't look the same</div><div class="small">Five layouts in five pins. Pins that all look alike blur together in a feed, so no layout repeats inside a batch.</div></div>
<div class="card"><div class="upper" style="color:var(--pink)">Where they point</div><div class="small">Every pin links to the one product page the client chose for this month, so every click lands somewhere that can sell.</div></div>
<div class="card"><div class="upper" style="color:var(--pink)">What she does</div><div class="small">Nothing. The 30 pins arrive scheduled, one a day, and each is checked in her scheduler after loading.</div></div></div>''', CLIENT, 5, T))
    P.append(order_page(SVC, CLIENT, 6, T, "portrait", "Five finished pins in five different layouts, each with a title, a 450 to 500 character description, alt text, a board and a posting slot. The 30-pin order is this, thirty times, scheduled one a day."))
    return doc(P, "DFY 30 Days of Pinterest: proof sample"), FILE, "portrait"
