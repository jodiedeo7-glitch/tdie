from common import *
from services import S

SVC = S["email"]
CLIENT = "Paperlark Planner Studio"
OWNER = "Priya Holloway"
OFFER = "The Sunday Reset Notion Course"
FILE = "DFY-6-Email-Sales-Series_Proof-Sample.pdf"

SERIES = [
 (1, "Can't do the tech", "I didn't know what a database was either", "Tuesday", True),
 (2, "No time", "Twenty minutes on a Sunday", "Thursday", False),
 (3, "Price", "What $79 actually buys you", "Saturday", False),
 (4, "No refunds / what if it isn't what I think", "No refunds. Read this first.", "Monday", True),
 (5, "Not enough content", "You don't need a busy life for this", "Wednesday", False),
 (6, "I'll do it later", "Later is exactly why this exists", "Thursday", False),
]

E1 = dict(subject="I didn't know what a database was either", preview="You don't need to be a tech person for this one.",
 paras=["Hi there,",
  "Can I tell you the thing I hear most about Notion?",
  "\"It looks amazing. I'd never be able to set it up.\"",
  "I get it. The first time I opened Notion I stared at a blank page for twenty minutes and closed the tab.",
  "Here's what nobody says out loud: you don't need to understand Notion to use a good Notion planner. You need someone to hand you the finished one and show you the few buttons you'll actually press.",
  "LINK1",
  "You copy my planner into your account in one click. Then short videos walk you through filling in your own week, one page at a time. No building from scratch. No formulas. If you can write a to-do list, you can do this.",
  "The tech is the part I already did for you.",
  "BTN:Get The Sunday Reset Notion Course",
  "Talk soon,\nPriya"])

E4 = dict(subject="No refunds. Read this first.", preview="I'd rather you know exactly what you're getting.",
 paras=["Hi there,",
  "Straight talk today, because you deserve it.",
  "The Sunday Reset Notion Course is a digital course. The second you buy, you get the whole thing: every video, the planner, all of it. So there are no refunds.",
  "Which means I'd much rather you know exactly what's inside before you decide. Here it is:",
  "• The Sunday Reset planner, copied into your Notion in one click\n• Six short video lessons, each under ten minutes\n• A weekly review page that takes about twenty minutes\n• A meal and habit tracker that lives inside the same planner",
  "LINK4",
  "And here's who it isn't for, honestly:",
  "• If you love building systems from scratch, you'll find it too done-for-you.\n• If you don't open a laptop or tablet during the week, a paper planner will suit you better. Truly.",
  "If you read that list and thought \"that's me, that's exactly what I need\", then you already know.",
  "BTN:Get The Sunday Reset Notion Course",
  "xo,\nPriya"])

LINKTXT = {"LINK1": "That's exactly what <u>The Sunday Reset Notion Course</u> is.",
           "LINK4": "Every lesson is listed on <u>the course page</u>, so you can see it all before you pay."}

CSS7 = """<style>.mail{background:#fff;border-radius:16px;overflow:hidden;border:1px solid rgba(200,169,106,.6);box-shadow:0 26px 44px -22px rgba(214,46,115,.45)}
.mail .top{background:linear-gradient(180deg,#f6f3fb,#fff);padding:12px 20px;border-bottom:1px solid #ece6f3;font-size:10px}
.mail .brandbar{background:#3d3a6b;color:#fff;text-align:center;padding:14px;font-family:'Newsreader',serif;font-size:20px;letter-spacing:.02em}
.mail .bd{padding:16px 30px 20px;font-size:12px;line-height:1.6;color:#221c20}
.mail .bd p{margin-bottom:10px;white-space:pre-line}
.mail u{color:#3d3a6b;font-weight:700;text-decoration-thickness:1.5px}
.mbtn{display:inline-block;background:#3d3a6b;color:#fff;border-radius:999px;padding:11px 26px;font-weight:700;font-size:11.5px}
</style>"""


def mail(e):
    ps = ""
    for p in e["paras"]:
        if p.startswith("BTN:"):
            ps += f'<div style="text-align:center;margin:14px 0 16px"><span class="mbtn">{esc(p[4:])}</span></div>'
        elif p in LINKTXT:
            ps += f"<p>{LINKTXT[p]}</p>"
        else:
            ps += f"<p>{esc(p)}</p>"
    return f'''<div class="mail"><div class="top"><b>From:</b> Priya at Paperlark &nbsp;·&nbsp; <b>To:</b> subscriber<br><b>Subject:</b> {esc(e['subject'])}<br><span class="muted"><b>Preview text:</b> {esc(e['preview'])}</span></div>
<div class="brandbar">Paperlark Planner Studio</div><div class="bd">{ps}</div></div>'''


def notes(items):
    return "".join(f'<div class="card tight"><div class="upper" style="color:var(--pink)">{a}</div><div class="small">{b}</div></div>' for a, b in items)


def build():
    T = 6
    P = []
    stack = "".join(f'<div class="card tight" style="position:absolute;left:{20+i*14}px;top:{i*44}px;width:300px;transform:rotate({(-1)**i*1.5}deg);{"background:linear-gradient(135deg,#D62E73,#FF6FAE);color:#fff;border:none" if s[4] else ""}"><div class="xs b" style="letter-spacing:.14em">EMAIL {s[0]} · {s[3].upper()}</div><div class="serif" style="font-size:15px;color:{"#fff" if s[4] else "var(--ink)"}">{esc(s[2])}</div></div>' for i, s in enumerate(SERIES))
    cover = f'''{CSS7}
<div class="kicker">{SVC['name']}</div>
<h1>Six objections. Six emails. <span class="hl">Here are two, in full.</span></h1>
<p class="lede" style="margin:14px 0 18px">Each email answers the one reason a subscriber hasn't bought yet, in the client's voice, with one ask linked twice. Written and scheduled in her MailerLite, with buyers excluded so nobody gets sold what they already own.</p>
<div style="display:grid;grid-template-columns:1fr 1.1fr;gap:24px">
<div><div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:19px">{CLIENT}</div>
<div class="small muted">{OWNER} sells Notion planners and one course, {OFFER}. Her list is warm but hesitant: people love her free templates and stall at the course. Voice: friendly, direct, a bit of sparkle.</div></div>
<div class="fict" style="margin-top:12px">★ {FICTIONAL}</div>
<div class="hero" style="margin-top:16px"><div class="kicker">In this sample</div><div class="small">Email 1 (can't do the tech) and Email 4 (no refunds / what if it isn't what I think), written out in full, plus the whole series plan and the MailerLite setup.</div></div></div>
<div style="position:relative;height:330px">{stack}<div class="sticker bub" style="right:-10px;bottom:-30px">2 of 6<br>in full</div></div></div>'''
    P.append(page(cover, CLIENT, 1, T))

    rows = "".join(f"<tr style='{'background:rgba(255,138,194,.12)' if s[4] else ''}'><td class='serif hl' style='font-size:16px'>{s[0]}</td><td class='b'>{s[1]}</td><td>{esc(s[2])}</td><td>{s[3]}, 11:00 AM</td><td>{'<span class=tag>In this sample</span>' if s[4] else ''}</td></tr>" for s in SERIES)
    plan = f'''<div class="kicker">The series plan</div><h2>One objection per email, <span class="hl">in the order they come up.</span></h2>
<div class="card" style="margin-top:12px"><table><tr><th>#</th><th>Objection</th><th>Subject line</th><th>Sends</th><th></th></tr>{rows}</table></div>
<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:14px">{notes([
 ("One ask, linked twice", "Every email asks for one thing: the course. The link sits on words early in the email and again on the closing button."),
 ("No guarantees, no income claims", "Nothing promises a result or a timeline. The no-refunds email states the policy plainly and shows what's inside instead."),
 ("Buyers excluded", "The whole series goes to active subscribers except the group Sunday Reset Buyers, checked again at send time."),
 ("Read back after scheduling", "Each campaign is opened on its review page after it's scheduled: subject, date, audience, both links.")])}</div>'''
    P.append(page(plan, CLIENT, 2, T, zoom=1.2))

    P.append(page(f'''{CSS7}<div style="display:grid;grid-template-columns:1.55fr 1fr;gap:18px">
<div>{mail(E1)}</div>
<div class="grid" style="gap:10px;align-content:start"><div class="kicker">Email 1 · Can't do the tech</div><h3>Why it's built this way</h3>{notes([
 ("Opens with her own words", "The first line quotes the objection the way subscribers actually say it."),
 ("Takes the fear off the table", "Admits the blank-page moment, then moves the tech to Priya's side: it's already built."),
 ("Link 1 of 2", "On the course name in the middle of the email."),
 ("Link 2 of 2", "On the closing button, same page."),
 ("Sends", "Tuesday, 11:00 AM, to subscribers who haven't bought.")])}</div></div>''', CLIENT, 3, T))

    P.append(page(f'''{CSS7}<div style="display:grid;grid-template-columns:1.55fr 1fr;gap:18px">
<div>{mail(E4)}</div>
<div class="grid" style="gap:10px;align-content:start"><div class="kicker">Email 4 · No refunds</div><h3>Why it's built this way</h3>{notes([
 ("Says the policy first", "No refunds, stated plainly in the third line. No guarantee, no trial, no fine print."),
 ("Replaces the refund with clarity", "Lists exactly what's inside so the reader can judge before she pays."),
 ("Tells the wrong buyer to skip it", "Naming who it isn't for is what makes the right buyer trust the rest."),
 ("Link 1 of 2", "On the words the course page, where every lesson is listed."),
 ("Link 2 of 2", "On the closing button, same page.")])}</div></div>''', CLIENT, 4, T))

    setup = f'''<div class="kicker">What's done inside her MailerLite</div><h2>Written, scheduled <span class="hl">and read back.</span></h2>
<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:16px;margin-top:12px">
<div class="card"><table>
<tr><th>Setting</th><th>Value</th></tr>
<tr><td class="b">Campaign type</td><td>Six regular campaigns, one per objection</td></tr>
<tr><td class="b">Audience</td><td>All active subscribers</td></tr>
<tr><td class="b">Excluded</td><td>Group: Sunday Reset Buyers (re-checked at send time, so a mid-series buyer stops getting sales emails)</td></tr>
<tr><td class="b">Send time</td><td>11:00 AM in her time zone</td></tr>
<tr><td class="b">Links</td><td>Course sales page, twice per email, on words and on the button</td></tr>
<tr><td class="b">Sign-off</td><td>Her own: "Talk soon" and "xo", then Priya</td></tr>
<tr><td class="b">Check</td><td>Each campaign opened on its review page after scheduling</td></tr></table></div>
<div class="grid" style="gap:12px;align-content:start">
<div class="hero"><div class="kicker">What she does</div><div class="small">Reads the six drafts, says yes, and watches them go out. Nothing to build.</div></div>
<div class="card"><div class="upper" style="color:var(--pink)">Still in the full series</div><div class="small">Emails 2, 3, 5 and 6: no time, price, not enough content and I'll do it later, each written the same way.</div></div>
<div class="card"><div class="upper" style="color:var(--pink)">Turnaround</div><div class="small">{SVC['time']}</div></div></div></div>'''
    P.append(page(setup, CLIENT, 5, T, zoom=1.22))
    P.append(order_page(SVC, CLIENT, 6, T, "portrait", "Two of the six emails in full, the series plan with every subject line, and the MailerLite setup with buyers excluded. The full order is all six, written and scheduled the same way for your offer."))
    return doc(P, "DFY 6-Email Sales Series: proof sample"), FILE, "portrait"
