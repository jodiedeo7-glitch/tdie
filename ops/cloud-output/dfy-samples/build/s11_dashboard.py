from common import *
from services import S

SVC = S["dashboard"]
CLIENT = "Clementine Loom Knit Patterns"
FILE = "DFY-Custom-Business-Dashboard_Proof-Sample.pdf"
HTML = "DFY-Custom-Business-Dashboard_Sample_Clementine-Loom.html"

PARTS = [
 ("Five numbers she checks", "Pattern sales, revenue, Etsy shop views, email subscribers and pin outbound clicks, each with its change against last month worked out."),
 ("Six months of revenue", "A bar for each month. This month in her teal, the rest in clementine."),
 ("Monthly goal ring", "She types her goal once. The ring, the percentage and the \"to go\" line update from her revenue."),
 ("Conversion and average order", "Worked out for her from numbers she already entered. No formulas to maintain."),
 ("Top 5 patterns", "Her best sellers this month with a bar for each, so the winner is obvious."),
 ("This week's focus", "Four tasks she can tick off. Ticks stay put when she comes back."),
]


def build():
    T = 4
    P = []
    cover = f'''<div style="display:grid;grid-template-columns:.9fr 1.5fr;gap:22px;align-items:start">
<div style="padding-top:8px"><div class="kicker">{SVC['name']}</div>
<h1 style="font-size:40px">A working <span class="hl">one-page dashboard</span>, in her colours.</h1>
<p class="lede" style="margin:12px 0 14px">Not a picture of a dashboard. The actual file: open it in any browser, pick a month, type in this month's numbers, and every total, chart and goal updates.</p>
<div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:18px">{CLIENT}</div>
<div class="small muted">Nora Beckett sells knitting patterns on Etsy and her own list. Brand colours: clementine orange, deep teal and cream. She wanted the numbers she actually checks, on one page, without logging into four apps.</div></div>
<div class="fict" style="margin-top:12px">★ {FICTIONAL}</div></div>
<div style="position:relative"><div class="card" style="padding:8px"><img src="dashboard-shot.png" style="width:100%;border-radius:10px;display:block"></div>
<div class="sticker bub" style="left:-34px;bottom:-40px">Working<br>file<br>included</div></div></div>
<div class="hero" style="margin-top:30px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:14px 20px">
 <div><div class="serif" style="font-size:28px;color:#fff">1</div><div class="small">file, opens in any browser</div></div>
 <div><div class="serif" style="font-size:28px;color:#fff">5</div><div class="small">numbers she tracks, with month-on-month change</div></div>
 <div><div class="serif" style="font-size:28px;color:#fff">6</div><div class="small">months of history, switchable by month</div></div>
 <div><div class="serif" style="font-size:28px;color:#fff">0</div><div class="small">logins, subscriptions or formulas to maintain</div></div></div>'''
    P.append(page(cover, CLIENT, 1, T, "landscape"))
    parts = "".join(f'<div class="card tight"><div style="display:flex;gap:8px;align-items:baseline"><span class="num" style="font-size:22px">{i+1}</span><span class="b">{a}</span></div><div class="small muted" style="margin-top:3px">{esc(b)}</div></div>' for i, (a, b) in enumerate(PARTS))
    P.append(page(f'''<div class="kicker">What's on the page</div><h2>Six blocks. <span class="hl">Each one answers a question she used to go looking for.</span></h2>
<div style="display:grid;grid-template-columns:1.45fr 1fr;gap:18px;margin-top:10px">
<div class="card" style="padding:8px"><img src="dashboard-shot.png" style="width:100%;border-radius:10px;display:block"></div>
<div class="grid" style="gap:8px">{parts}</div></div>''', CLIENT, 2, T, "landscape"))
    steps = [("Open the file", "Double-click it. It opens in her browser, on her laptop or her phone. Nothing to install."),
             ("Press \"Update this month's numbers\"", "Each number becomes a box. She types in what her Etsy stats, email platform and Pinterest analytics say."),
             ("Press \"Save numbers\"", "Every change, chart, goal and percentage updates at once, and the numbers are kept on that device for next time."),
             ("Switch months", "The month menu shows any of the six months, with the change against the month before.")]
    st = "".join(f'<div class="card"><div class="num" style="font-size:26px">{i+1}</div><div class="b" style="margin:4px 0">{esc(a)}</div><div class="small muted">{esc(b)}</div></div>' for i, (a, b) in enumerate(steps))
    P.append(page(f'''<div style="display:grid;grid-template-columns:1.6fr 1fr;gap:22px">
<div><div class="kicker">How she uses it</div><h2>Once a month, <span class="hl">five minutes.</span></h2>
<p class="lede" style="margin-bottom:14px">The dashboard was built around the numbers Nora told us she checks. Updating it takes the time it takes to copy five numbers.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">{st}</div>
<div class="hero" style="margin-top:14px"><div class="kicker">Tested before handover</div><div class="small">Opened on desktop and phone. Numbers edited and saved, the goal ring and percentages recalculated, the page reloaded to confirm the numbers stayed, and every month switched.</div></div>
<div class="card" style="margin-top:12px"><div class="upper" style="color:var(--pink)">Try it yourself</div><div class="small" style="margin-top:4px">The working file, <b>{HTML}</b>, comes with this sample. Open it, press "Update this month's numbers", change the revenue, save, and watch the goal ring move. Reload the page and your number is still there.</div></div></div>
<div style="position:relative"><div class="card" style="padding:6px;height:540px;overflow:hidden"><img src="dashboard-mobile.png" style="width:100%;border-radius:10px;display:block"></div><div class="xs muted" style="margin-top:6px;text-align:center">Same file on a phone</div>
<div class="sticker sm" style="right:-14px;top:-14px">Phone<br>ready</div></div></div>''', CLIENT, 3, T, "landscape"))
    P.append(order_page(SVC, CLIENT, 4, T, "landscape", "A working one-page dashboard in the client's colours with the five numbers she tracks, a goal ring, six months of history and a weekly focus list, tested on desktop and phone. The file itself comes with this sample."))
    return doc(P, "DFY Custom Business Dashboard: proof sample"), FILE, "landscape"
