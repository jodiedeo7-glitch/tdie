from common import *
from services import S

SVC = S["automation"]
CLIENT = "Velvet Turnip Printables"
FILE = "Run-It-Like-Mine-DFY-Automation-Setup_The-Engine_Proof-Sample.pdf"

AUTOS = [
 ("8 AM Publisher", "Every day, 8:00 AM", "Publishes the day's queued blog post on Hattie's site, opens the live page to check it loaded, then posts the announcement in her Skool community with the link on the words.", "Live post URL + community post, both read back"),
 ("Pin Factory", "Every day, 1:00 PM", "Designs 3 pins from that week's printables, writes the title, description and alt text, and schedules them into her Pinterest for the next day.", "3 pins scheduled, each opened in Pinterest to confirm"),
 ("Friday Readout", "Fridays, 4:00 PM", "Pulls the week's numbers (site visits, Etsy orders, email sign-ups, pin clicks) into a one-page readout and sends it to her inbox with the one thing to fix next week.", "Readout email, numbers checked against each source"),
]

# (day, time, automation, status, what it did, how it checked)
LOG = [
 ("Mon 12", "8:00 AM", "8 AM Publisher", "ok", "Published \"5 Chore Charts That Survive Real Kids\". Posted the announcement in the Velvet Turnip Club.", "Opened the live page (loaded, images present). Reloaded the community post: live, link on the words."),
 ("Mon 12", "1:00 PM", "Pin Factory", "ok", "Designed 3 pins for the Weekly Meal Planner. Scheduled for Tue 8:00, 12:00, 19:00.", "Opened each scheduled pin: image, title, description and link all correct."),
 ("Tue 13", "8:00 AM", "8 AM Publisher", "ok", "Published \"The Fridge Door Planner Method\". Community post live.", "Live page loaded. Community post read back."),
 ("Tue 13", "1:00 PM", "Pin Factory", "held", "Pinterest composer froze on pin 2. Closed the tab, opened a fresh one, rebuilt pin 2. Scheduled all 3.", "All 3 opened in the scheduled list. Hiccup noted for Hattie, nothing for her to do."),
 ("Wed 14", "8:00 AM", "8 AM Publisher", "ok", "Published \"Lunchbox Notes Kids Actually Read\". Community post live.", "Live page loaded. Community post read back."),
 ("Wed 14", "1:00 PM", "Pin Factory", "ok", "3 pins for Lunchbox Notes printable. Scheduled for Thu.", "Each pin opened and checked."),
 ("Thu 15", "8:00 AM", "8 AM Publisher", "ok", "Published \"A Screen-Time Chart Without the Fight\". Community post live.", "Live page loaded. Community post read back."),
 ("Thu 15", "1:00 PM", "Pin Factory", "ok", "3 pins for the Screen-Time Chart. Scheduled for Fri.", "Each pin opened and checked."),
 ("Fri 16", "8:00 AM", "8 AM Publisher", "ok", "Published \"Sunday Reset Printables, Ranked\". Community post live.", "Live page loaded. Community post read back."),
 ("Fri 16", "1:00 PM", "Pin Factory", "ok", "3 pins for the Sunday Reset bundle. Scheduled for Sat.", "Each pin opened and checked."),
 ("Fri 16", "4:00 PM", "Friday Readout", "ok", "Built the week's readout and emailed it to Hattie (page 5).", "Every number matched against its source before sending."),
 ("Sat 17", "8:00 AM", "8 AM Publisher", "skip", "Nothing in the publish queue for Saturday. Skipped on purpose and said so.", "Queue checked twice. No post, no empty announcement."),
 ("Sat 17", "1:00 PM", "Pin Factory", "ok", "3 pins for the Holiday Gift Tags printable. Scheduled for Sun.", "Each pin opened and checked."),
 ("Sun 18", "8:00 AM", "8 AM Publisher", "ok", "Published \"Gift Tags You Can Print Tonight\". Community post live.", "Live page loaded. Community post read back."),
 ("Sun 18", "1:00 PM", "Pin Factory", "ok", "3 pins for the Weekly Meal Planner (new angle). Scheduled for Mon.", "Each pin opened and checked. No design repeated from this week."),
]
BADGE = {"ok": ("Ran", "tag"), "held": ("Recovered", "tag gold"), "skip": ("Skipped, on purpose", "tag ink")}


def row(r):
    lab, cls = BADGE[r[3]]
    return f"<tr><td class='b'>{r[0]}</td><td>{r[1]}</td><td class='b' style='color:var(--pink)'>{r[2]}</td><td><span class='{cls}'>{lab}</span></td><td>{esc(r[4])}</td><td class='muted'>{esc(r[5])}</td></tr>"


def daystrip(days):
    out = ""
    for d in days:
        rs = [r for r in LOG if r[0] == d]
        ok = len(rs)
        out += f'<div class="card tight" style="text-align:center"><div class="serif" style="font-size:18px">{d}</div><div class="xs muted">{len(rs)} scheduled runs</div><div class="num" style="font-size:22px;margin-top:4px">{ok}/{len(rs)}</div><div class="xs muted">handled and reported</div></div>'
    return f'<div style="display:grid;grid-template-columns:repeat({len(days)},1fr);gap:12px;margin-top:16px">{out}</div>'


def logtable(rows):
    return f"<div class='card' style='padding:8px 10px'><table><tr><th style='width:52px'>Day</th><th style='width:52px'>Time</th><th style='width:92px'>Automation</th><th style='width:90px'>Status</th><th>What it did</th><th>How it checked</th></tr>{''.join(row(r) for r in rows)}</table></div>"


def build():
    T = 7
    P = []
    counts = {"ok": sum(r[3] == "ok" for r in LOG), "held": sum(r[3] == "held" for r in LOG), "skip": sum(r[3] == "skip" for r in LOG)}
    minis = "".join(f'''<div class="card tight" style="transform:rotate({rot}deg);margin-bottom:10px"><div class="upper" style="color:var(--pink)">{a[1]}</div><div class="serif" style="font-size:16px">{a[0]}</div><div class="xs muted">{esc(a[2][:92])}...</div></div>''' for a, rot in zip(AUTOS, (-2, 1.5, -1)))
    cover = f'''
<div style="display:grid;grid-template-columns:1.2fr 1fr;gap:30px">
<div style="padding-top:16px">
 <div class="kicker">{SVC['name']} · The Engine</div>
 <h1>One week of <span class="hl">The Engine</span>, running on its own.</h1>
 <p class="lede" style="margin:14px 0 16px">This is the real run log a client gets: three automations set up on her own Claude account, every run written down, every result checked. Including the day something froze, and the day there was nothing to publish.</p>
 <div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:19px">{CLIENT}</div>
 <div class="small muted">Hattie Marlowe sells printable meal planners and chore charts on her own site and on Etsy, with a small Skool community called the Velvet Turnip Club. She picked 3 automations: the 8 AM Publisher, the Pin Factory and the Friday Readout.</div></div>
 <div style="margin-top:14px" class="fict">★ {FICTIONAL}</div>
</div>
<div style="position:relative;padding-top:30px">{minis}
 <div class="sticker bub" style="right:-12px;bottom:-40px">15 runs<br>logged<br>this week</div></div>
</div>
<div class="hero" style="margin-top:26px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:14px 20px">
 <div><div class="serif" style="font-size:30px;color:#fff">3</div><div class="small">automations on her own account</div></div>
 <div><div class="serif" style="font-size:30px;color:#fff">{counts['ok']}</div><div class="small">clean runs</div></div>
 <div><div class="serif" style="font-size:30px;color:#fff">{counts['held']}</div><div class="small">hiccup, fixed in the same run</div></div>
 <div><div class="serif" style="font-size:30px;color:#fff">{counts['skip']}</div><div class="small">skip, on purpose, reported</div></div>
</div>'''
    P.append(page(cover, CLIENT, 1, T, "landscape"))

    cards = "".join(f'''<div class="card"><div class="tag">{a[1]}</div><h3 style="margin-top:8px">{a[0]}</h3><p class="small" style="margin:4px 0 8px">{esc(a[2])}</p><div class="rule" style="margin:8px 0"></div><div class="xs"><span class="upper" style="color:var(--pink)">Proof it ran</span><br>{esc(a[3])}</div></div>''' for a in AUTOS)
    setup = f'''
<div class="kicker">What was installed</div>
<h2>Three automations. <span class="hl">Her account, her voice.</span></h2>
<p class="lede" style="margin-bottom:14px">Each one runs as a scheduled task on Hattie's own Claude account, so she owns it. Each one reads her voice file first and checks its own work before it reports.</p>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px">{cards}</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:16px">
 <div class="card tight"><div class="upper" style="color:var(--pink)">Handover day</div><div class="small">A test run of all three before handover. Every output opened live before sign-off.</div></div>
 <div class="card tight"><div class="upper" style="color:var(--pink)">Instruction sheet</div><div class="small">One plain page per automation: what it does, when, where the output lands, how to pause it.</div></div>
 <div class="card tight"><div class="upper" style="color:var(--pink)">The run log rule</div><div class="small">Nothing is logged as done until the result is opened and seen. A task that returns without error is not proof.</div></div>
</div>'''
    P.append(page(setup, CLIENT, 2, T, "landscape", zoom=1.18))

    P.append(page(f'<div class="kicker">Run log · week of 12 October</div><h2>Monday to Wednesday</h2><div style="margin-top:8px">{logtable(LOG[:6])}</div>{daystrip(["Mon 12","Tue 13","Wed 14"])}', CLIENT, 3, T, "landscape"))
    P.append(page(f'<div class="kicker">Run log · week of 12 October</div><h2>Thursday to Sunday</h2><div style="margin-top:8px">{logtable(LOG[6:])}</div>{daystrip(["Thu 15","Fri 16","Sat 17","Sun 18"])}', CLIENT, 4, T, "landscape"))

    nums = [("Site visits", "1,284", "up from 1,102"), ("Etsy orders", "37", "up from 31"), ("New email sign-ups", "58", "up from 44"), ("Pin outbound clicks", "412", "up from 356")]
    tiles = "".join(f'<div class="card" style="text-align:center"><div class="upper muted">{a}</div><div class="num" style="margin:6px 0">{b}</div><div class="xs muted">{c} last week</div></div>' for a, b, c in nums)
    readout = f'''
<div style="display:grid;grid-template-columns:1fr 1.4fr;gap:24px">
<div><div class="kicker">What landed in her inbox, Friday 4:00 PM</div><h2>The Friday Readout, <span class="hl">exactly as sent.</span></h2>
<p class="lede">One page. The four numbers she tracks, what moved them, and one thing to fix. No dashboard to log into.</p>
<div class="card" style="margin-top:14px"><div class="upper" style="color:var(--pink)">Where every number came from</div><ul class="clean small" style="margin-top:6px"><li>Site visits: her site analytics</li><li>Etsy orders: Etsy shop stats</li><li>Sign-ups: her email platform</li><li>Pin clicks: Pinterest analytics</li></ul><div class="xs muted" style="margin-top:6px">Each number read from its source and matched before the email went out.</div></div></div>
<div class="card" style="padding:18px 20px;position:relative">
 <div class="xs muted">From: Friday Readout · To: Hattie · Subject: Your week: orders up, one pin carried it</div><div class="rule"></div>
 <div class="serif" style="font-size:20px;margin-bottom:10px">Week of 12 October</div>
 <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px">{tiles}</div>
 <div class="rule"></div>
 <div class="small"><b>What moved it:</b> Tuesday's Weekly Meal Planner pin drove about a third of this week's pin clicks. The Lunchbox Notes post got the most time on page.</div>
 <div class="hero" style="margin-top:12px;padding:12px 16px"><div class="kicker">One thing for next week</div><div class="small">Your Sunday Reset bundle page has no pin pointing to it yet. The Pin Factory has 3 queued for Monday. Nothing for you to do.</div></div>
 <div class="sticker sm" style="right:-18px;top:-22px">Sent<br>4:00 PM</div>
</div></div>'''
    P.append(page(readout, CLIENT, 5, T, "landscape"))

    sheets = ''.join(f'<div class="card"><h3>{a[0]}</h3><table><tr><td class="b">Runs</td><td>{a[1]}</td></tr><tr><td class="b">Reads first</td><td>Her voice file and the week&#39;s queue</td></tr><tr><td class="b">Output</td><td>{esc(a[3])}</td></tr><tr><td class="b">To pause</td><td>Scheduled tasks, switch it off. Nothing is lost.</td></tr><tr><td class="b">If it fails</td><td>It says so in the run report, in plain English, with what it tried.</td></tr></table></div>' for a in AUTOS)
    tp = f'''
<div class="kicker">The instruction sheet</div><h2>What Hattie keeps <span class="hl">so she never needs me.</span></h2>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:12px">
{sheets}
</div>
<div class="card" style="margin-top:14px;display:flex;gap:16px;align-items:center"><span class="tag ink">Care Plan option</span><span class="small">The Care Plan is a separate monthly option. Without it, the instruction sheet is everything she needs to run, pause or restart each automation.</span></div>'''
    P.append(page(tp, CLIENT, 6, T, "landscape", zoom=1.22))
    P.append(order_page(SVC, CLIENT, 7, T, "landscape", "A week of The Engine: three automations installed on the client's own account, fifteen logged runs, one recovered hiccup, one honest skip, and the Friday Readout she actually received."))
    return doc(P, "Run It Like Mine: The Engine proof sample"), FILE, "landscape"
