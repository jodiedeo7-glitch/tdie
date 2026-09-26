from common import *
from services import S

SVC = S["threads"]
CLIENT = "Pennywhistle Ledger Studio"
HANDLE = "pennywhistle.ledger"
FILE = "DFY-30-Day-Threads-Calendar_Proof-Sample.pdf"

SLOTS = [("7:30 AM", "Hot take", "One sharp opinion. No link. Starts the day's conversation."),
         ("12:00 PM", "Teach", "One useful, specific tip she can use today. No link."),
         ("5:00 PM", "Offer", "One offer a day. The link goes in the reply, never the post.")]

OFFERS = [("The Quarter-Close Checklist", "Margo's paid checklist: close the books in one sitting"),
          ("Receipt Sorting Cheat Sheet", "Free one-pager that grows her list"),
          ("Books Tune-Up", "90-minute call, her highest-ticket service"),
          ("The Friday Ledger", "Her free weekly email")]

DAYS = [
 ("Day 1", "Monday", [
  "Hot take: your Etsy shop isn't slow. Your books are just vague.\n\nDeposits are not profit. Fees, labels, listing renewals and that ad you forgot about all come out first.\n\nKnow your real margin before you decide the shop \"isn't working.\"",
  "Three numbers every handmade seller should know by Friday:\n\n1. What you actually kept after fees and shipping\n2. What one order costs you in materials\n3. How many orders it takes to cover your monthly bills\n\nNot a spreadsheet with 40 tabs. Three numbers.",
  ("If your receipts live in a shoebox, a camera roll and one very tired email folder, this one's for you.\n\nMy Quarter-Close Checklist walks you through closing your books in one sitting. Every step, in order, with where to click.\n\nLink's in the reply 👇", "Grab the Quarter-Close Checklist here", "The Quarter-Close Checklist")]),
 ("Day 2", "Tuesday", [
  "Unpopular opinion: \"I'll catch up on my books in January\" is a plan to have a very bad January.",
  "How to sort a year of receipts without crying:\n\n• One folder per month, not per category\n• Photograph paper receipts the day you get them\n• Name files date first: 2026-10-06 fabric\n• Categories come last, once everything is in one place\n\nSort first, label second. Always.",
  ("Free thing for you today.\n\nMy Receipt Sorting Cheat Sheet is one page: the folder setup, the file naming rule and the 8 categories most handmade sellers need.\n\nIt's in the reply. Print it and stick it by your packing table.", "Get the free cheat sheet", "Receipt Sorting Cheat Sheet")]),
 ("Day 3", "Wednesday", [
  "Nobody talks about this: the sale you're proudest of might be the one costing you the most.\n\nCustom orders eat hours you never write down.",
  "Quick math for custom orders:\n\nTime one. Actually time it, start to finish, including the messages back and forth.\n\nMultiply by what you'd pay someone else to do it.\n\nIf the price doesn't cover that plus materials, it's not a custom order. It's a favour.",
  ("Want a second set of eyes on your numbers?\n\nA Books Tune-Up is 90 minutes on a call with me. We open your books together, fix what's off, and you leave knowing your real margin on every product.\n\nBooking link's in the reply.", "Book your Books Tune-Up", "Books Tune-Up")]),
 ("Day 4", "Thursday", [
  "\"I don't need a bookkeeper, I'm tiny.\"\n\nTiny is exactly when it's easiest to get it right.",
  "Separate your business money this week. In this order:\n\n1. Open a checking account just for the shop\n2. Point your shop payouts to it\n3. Move every business subscription over, one a day\n4. Pay yourself on the same date each month\n\nMixed accounts are the first thing I untangle for new clients.",
  ("Quarter end is coming. If you'd rather close it calmly than at midnight, the Quarter-Close Checklist is the one I hand every new client.\n\nLink in the reply.", "Grab the Quarter-Close Checklist", "The Quarter-Close Checklist")]),
 ("Day 5", "Friday", [
  "Your accountant is not mad at you. They're mad at the shoebox.",
  "Friday five-minute money check:\n\n☐ Download this week's shop statement\n☐ Drop new receipts in this month's folder\n☐ Look at one subscription you forgot you pay for\n☐ Write down your order count\n\nFive minutes on Friday saves a whole weekend in April.",
  ("Someone asked what the Receipt Sorting Cheat Sheet actually looks like.\n\nOne page. Folders, file names, 8 categories. That's the whole trick, and it's free.\n\nIt's in the reply if you want it.", "Get the free cheat sheet", "Receipt Sorting Cheat Sheet")]),
 ("Day 6", "Saturday", [
  "Saturday confession: I love a messy spreadsheet. I just don't let it anywhere near a tax deadline.",
  "What usually counts as a business expense for handmade sellers (check with your tax pro for your own situation):\n\n• Materials and packaging\n• Shop and listing fees\n• Shipping labels\n• Software you use for the shop\n• A share of your phone bill\n\nKeep the receipt. Every time.",
  ("If you'd rather hand me the mess than read one more tip, a Books Tune-Up is where we start.\n\n90 minutes, your books open on screen, nothing to prepare.\n\nBooking link in the reply.", "Book your Books Tune-Up", "Books Tune-Up")]),
 ("Day 7", "Sunday", [
  "A Sunday reset for your shop takes 20 minutes, not a whole day.",
  "My Sunday 20:\n\n5 min: last week's order count and total\n5 min: receipts into folders\n5 min: one expense to cut or question\n5 min: pick next week's one money task\n\nPaper is fine. The habit matters more than the tool.",
  ("Every Friday I send one short email: one money habit, one thing I fixed for a client, one question to ask your own books.\n\nIt's called The Friday Ledger and it's free. Sign-up link in the reply.", "Join The Friday Ledger", "The Friday Ledger")]),
]

HOOKS = ["Deposits are not profit.", "The shoebox is not a system.", "Your best seller might be your worst earner.",
 "I opened a client's books and found the same subscription three times.", "Stop categorising receipts before you've sorted them.",
 "If you can't name your margin, you can't set your price.", "Tax season starts in October, not April.",
 "Custom orders are where profit goes to hide.", "You don't need an app. You need a Friday.",
 "Pay yourself on purpose, not by accident.", "The five-minute habit that saves a whole weekend.",
 "Your shop fees went up. Did your prices?", "I'm a bookkeeper and I still hate receipts.",
 "The first question I ask every new client.", "Free shipping isn't free. Someone pays it.",
 "What I'd fix first if I opened your books today.", "Three numbers. That's the whole dashboard.",
 "The mistake that makes tax prep take twice as long.", "Mixing accounts feels fine until it doesn't.",
 "Your future self is going to read these books."]

EXTRA_CSS = """
<style>
.tp{background:#fff;border-radius:14px;border:1px solid rgba(26,20,23,.09);padding:10px 12px 10px;box-shadow:0 14px 26px -18px rgba(214,46,115,.55),0 1px 2px rgba(0,0,0,.04);position:relative}
.tp .hd{display:flex;align-items:center;gap:7px;margin-bottom:5px}
.av{width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#1f5b58,#6aa89f);color:#fff;font-weight:800;font-size:8px;display:flex;align-items:center;justify-content:center;flex:none}
.tp .h{font-weight:700;font-size:8.8px}
.tp .t{margin-left:auto}
.tp .bd{white-space:pre-line;font-size:10.2px;line-height:1.45;color:#231c20}
.tp .rp{margin-top:7px;border-left:2px solid rgba(214,46,115,.35);padding:5px 0 1px 9px;font-size:9.4px}
.lk{display:inline-block;margin-top:3px;padding:2px 8px;border-radius:6px;background:#f2f6f5;border:1px solid #cfe0dd;color:#1f5b58;font-weight:600;font-size:7.8px}
.ctr{font-size:7px;color:#8b7d83;margin-top:5px;text-align:right}
.dayhead{display:flex;align-items:baseline;gap:10px;margin-bottom:8px}
.dayhead .serif{font-size:26px}
</style>"""


def post(text, slot, reply=None):
    rp = ""
    if reply:
        rp = f'<div class="rp"><div class="hd" style="margin-bottom:2px"><div class="av" style="width:16px;height:16px;font-size:6px">PL</div><span class="h">{HANDLE}</span><span class="xs muted">reply, 1 min later</span></div>{esc(reply[0])} 👉<br><span class="lk">link: {esc(reply[1])} page</span></div>'
    n = len(text)
    return f'''<div class="tp"><div class="hd"><div class="av">PL</div><span class="h">{HANDLE}</span><span class="tag {'ink' if slot[1]=='Offer' else ('gold' if slot[1]=='Teach' else '')} t">{slot[0]} · {slot[1]}</span></div>
<div class="bd">{esc(text)}</div>{rp}<div class="ctr">{n}/500 characters</div></div>'''


def day_col(d):
    name, wd, posts = d
    cells = []
    for i, p in enumerate(posts):
        if isinstance(p, tuple):
            cells.append(post(p[0], SLOTS[i], (p[1], p[2])))
        else:
            cells.append(post(p, SLOTS[i]))
    return f'''<div><div class="dayhead"><span class="serif">{name}</span><span class="kicker" style="margin:0">{wd}</span></div>
<div class="grid" style="gap:9px">{''.join(cells)}</div></div>'''


def build():
    T = 7
    pages = []
    # 1 cover
    fan = f'''<div style="position:relative;height:430px">
<div style="position:absolute;right:170px;top:40px;width:250px;transform:rotate(-7deg)">{post(DAYS[1][2][0], SLOTS[0])}</div>
<div style="position:absolute;right:10px;top:10px;width:270px;transform:rotate(4deg)">{post(DAYS[0][2][1], SLOTS[1])}</div>
<div style="position:absolute;right:95px;top:215px;width:275px;transform:rotate(-1.5deg)">{post(DAYS[2][2][2][0], SLOTS[2], (DAYS[2][2][2][1], DAYS[2][2][2][2]))}</div>
<div class="sticker" style="left:18px;top:250px">Week 1<br>21 posts<br>ready</div>
</div>'''
    cover = f'''{EXTRA_CSS}
<div style="display:grid;grid-template-columns:1fr 1.15fr;gap:24px;align-items:start">
<div style="padding-top:18px">
  <div class="kicker">{SVC['name']}</div>
  <h1>The first week of a <span class="hl">Threads calendar</span>, written and ready to post.</h1>
  <p class="lede" style="margin:16px 0 18px">Every post below is finished copy, in the client's voice, on the client's slot plan. She opens the calendar, copies the day, and posts. No blank box at 7:30 in the morning.</p>
  <div class="card" style="margin-bottom:14px">
    <div class="upper" style="color:var(--pink);margin-bottom:6px">Built for</div>
    <div class="serif" style="font-size:19px">{CLIENT}</div>
    <div class="small muted" style="margin-top:3px">Margo Quill, a bookkeeper for Etsy and handmade sellers. Posts as herself. Voice: dry, plain, a bit cheeky, zero jargon. Sells a checklist, a free cheat sheet, a 90-minute call and a free weekly email.</div>
  </div>
  <div style="display:flex;gap:10px;flex-wrap:wrap"><span class="tag">7 days</span><span class="tag">21 posts</span><span class="tag">7 offers, links in replies</span><span class="tag gold">20-hook bank</span></div>
  <div style="margin-top:16px" class="fict">★ {FICTIONAL}</div>
</div>
{fan}
</div>
<div class="hero" style="margin-top:6px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:14px 20px">
 <div><div class="serif" style="font-size:30px;color:#fff">21</div><div class="small">finished posts, one full week</div></div>
 <div><div class="serif" style="font-size:30px;color:#fff">3</div><div class="small">slots a day: hot take, teach, offer</div></div>
 <div><div class="serif" style="font-size:30px;color:#fff">7</div><div class="small">offers, each with its link in the reply</div></div>
 <div><div class="serif" style="font-size:30px;color:#fff">20</div><div class="small">hooks in the bank for off-plan days</div></div>
</div>'''
    pages.append(page(cover, CLIENT, 1, T, "landscape"))

    # 2 plan
    rows = "".join(f"<tr><td class='b' style='color:var(--pink)'>{t}</td><td class='b'>{j}</td><td>{r}</td></tr>" for t, j, r in SLOTS)
    glance = ""
    for d in DAYS:
        offer = d[2][2][2]
        glance += f'''<div class="card tight" style="text-align:center"><div class="serif" style="font-size:15px">{d[1][:3]}</div>
<div class="xs muted" style="margin:4px 0">Hot take · Teach</div><div class="tag ink" style="white-space:normal;line-height:1.2">{esc(offer)}</div></div>'''
    offers = "".join(f"<li><b>{esc(a)}</b><br><span class='muted small'>{esc(b)}</span></li>" for a, b in OFFERS)
    plan = f'''{EXTRA_CSS}
<div class="kicker">The daily slot plan</div>
<h2>Three posts a day. <span class="hl">One of them sells.</span></h2>
<p class="lede" style="margin-bottom:14px">Margo's 30 days run on the same three slots, so the account feels alive all day without her thinking about it. The offer always has its link in a reply, never in the post.</p>
<div style="display:grid;grid-template-columns:1.35fr 1fr;gap:16px">
 <div class="card"><table><tr><th>Time (her time zone)</th><th>Slot</th><th>What goes here</th></tr>{rows}</table>
 <div class="rule"></div>
 <div class="upper" style="color:var(--pink);margin-bottom:8px">Week 1 at a glance</div>
 <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:7px">{glance}</div></div>
 <div class="grid" style="gap:12px">
  <div class="card"><div class="upper" style="color:var(--pink);margin-bottom:8px">Offers in rotation</div><ul class="clean">{offers}</ul></div>
  <div class="hero"><div class="kicker">Spread rule used</div><div class="small">No offer two days running. No offer more than twice a week. Free and paid alternate so the feed never reads as all selling.</div></div>
 </div>
</div>'''
    pages.append(page(plan, CLIENT, 2, T, "landscape"))

    # 3-5 two days each
    n = 3
    for a, b in [(0, 1), (2, 3), (4, 5)]:
        body = f'''{EXTRA_CSS}<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">{day_col(DAYS[a])}{day_col(DAYS[b])}</div>'''
        pages.append(page(body, CLIENT, n, T, "landscape")); n += 1
    # 6 day 7 + hooks
    hooks = "".join(f'<div class="card tight small" style="display:flex;gap:8px;align-items:flex-start"><span class="serif hl" style="font-size:14px;line-height:1">{i+1:02d}</span><span>{esc(h)}</span></div>' for i, h in enumerate(HOOKS))
    body = f'''{EXTRA_CSS}<div style="display:grid;grid-template-columns:.9fr 1.3fr;gap:22px">{day_col(DAYS[6])}
<div><div class="kicker">The hook bank</div><h2>20 openers for <span class="hl">off-plan days.</span></h2>
<p class="small muted" style="margin-bottom:10px">When something happens in her week, Margo grabs a hook and writes the rest in her own words. Every hook is in her voice and none repeat a post in the calendar.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:7px">{hooks}</div></div></div>'''
    pages.append(page(body, CLIENT, 6, T, "landscape"))
    pages.append(order_page(SVC, CLIENT, 7, T, "landscape",
        "A full week: 21 finished posts on a slot plan, seven offers with their links in the replies, and a hook bank. The real calendar runs 30 days, written the same way for your offers and your voice."))
    return doc(pages, "DFY 30-Day Threads Calendar: proof sample"), FILE, "landscape"
