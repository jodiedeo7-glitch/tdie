from common import *
from services import S

SVC = S["skool"]
CLIENT = "The Crumb & Kettle Circle"
OWNER = "Delia Fenwick"
FILE = "DFY-Skool-Autopilot_Proof-Sample.pdf"

SLOTS = [("7:00 AM", "Morning check-in"), ("11:00 AM", "Teach"), ("3:00 PM", "Wins & show-and-tell"), ("7:30 PM", "Community or offer")]

# (title, body, kind)  kind: talk | teach | win | sell | free
W = [
 ("Monday", [
  ("☕ Monday check-in", "Good morning, bakers ☕\n\nWhat's rising in your kitchen this week?\n\nDrop one word. Mine's \"focaccia\" 🫓", "talk"),
  ("The poke test, finally explained 👉", "Springs back fast: give it more time.\nSprings back slowly and leaves a small dent: bake it.\nDoesn't spring back at all: it went a bit long. Bake it anyway and call it rustic 😅\n\nThat's the whole test.", "teach"),
  ("Show me your crumb 📸", "Post a photo of your last loaf, cut side up.\n\nNo judging. Flat loaves welcome. Some of my best lessons came from bread that looked like a frisbee 🥏", "win"),
  ("Weekend Loaf Workshop: doors are open 🍞", "If you've been winging it with sourdough, this is your weekend.\n\nThe Weekend Loaf Workshop takes you from starter to sliced loaf in two days, step by step.\n\n👉 Save your seat here", "sell")]),
 ("Tuesday", [
  ("Coffee or tea while the dough rests? ☕🫖", "Settle this for me.\n\nCoffee 👉 ☕\nTea 👉 🫖\n\nVote in the comments 😂", "talk"),
  ("Why your loaf spreads flat (it's usually one thing)", "Nine times out of ten it's shaping, not your starter.\n\n1. Pre-shape a loose round, rest 20 minutes\n2. Final shape tight, like tucking in a blanket\n3. Seam side up in the basket\n\nTry it and report back 👇", "teach"),
  ("Wins thread 🏆", "Tell me one thing that went right in your kitchen this week.\n\nA loaf, a cookie, a clean oven. It all counts 💛", "win"),
  ("Who's new? 👋", "Joined this week? Say hi below and tell us what you bake most.\n\nEveryone else: give them a warm welcome. That's how this place stays cosy 🫶", "talk")]),
 ("Wednesday", [
  ("Midweek starter check 🌡️", "How's your starter feeling today?\n\n🔥 bubbly and wild\n😴 sleepy\n💀 we don't talk about it\n\nNo shame in 💀. We fix those here.", "talk"),
  ("Feed your starter on your schedule, not its", "You don't have to feed it at 6 AM.\n\nKeep it in the fridge between bakes. Pull it out the night before, feed it, and it's ready by morning.\n\nOnce a week in the fridge is plenty for most of us.", "teach"),
  ("First loaf vs latest loaf 📸", "Got both? Post them side by side.\n\nThis is my favourite thread every single week 😍", "win"),
  ("What we're baking in the Crumb Club 🥐", "Crumb Club members get a new bake-along every Sunday, the full recipe archive and a monthly live Q&A with me.\n\nIf you're baking every week anyway, come bake with us.\n\n👉 Join the Crumb Club", "sell")]),
 ("Thursday", [
  ("What's going in the oven this weekend? 🔥", "Quick one: what are you baking this weekend?\n\nI'll pick three and share tips in tomorrow's post 👀", "talk"),
  ("Steam without a Dutch oven", "No Dutch oven? No problem.\n\nPut a metal tray on the bottom rack while the oven heats. Slide the loaf in, pour a cup of hot water into the tray, shut the door fast.\n\nMitts on. Face back. Steam is hot 🔥", "teach"),
  ("Tiny wins only ✨", "Weighed instead of guessed? Remembered to feed the starter? Didn't open the oven early?\n\nTiny wins go here. They add up 💪", "win"),
  ("Your worst bake ever 😂", "Let's be honest. Tell me about the loaf that went wrong.\n\nMine was a brick so dense the dog walked away from it. Your turn 👇", "talk")]),
 ("Friday", [
  ("Friday feels 🎉", "It's Friday. What are you baking to celebrate?\n\nPizza night counts. Toast counts. Cookies definitely count 🍪", "talk"),
  ("Your weekend plan (from yesterday's thread)", "You asked, here's the plan:\n\n🍕 Pizza: make the dough tonight, bake tomorrow. It tastes better after a night in the fridge.\n🥖 Baguettes: shape gently, bake hot.\n🍪 Cookies: chill the dough 30 minutes. Worth it.\n\nTag me in your photos 📸", "teach"),
  ("Weekend baking buddies 🤝", "Baking this weekend? Say what and when below.\n\nFind someone baking the same thing and cheer each other on 📣", "win"),
  ("The workshop starts tomorrow morning ☀️", "Two days, one loaf, every step laid out.\n\nIf you've wanted to finally get sourdough right, the Weekend Loaf Workshop is this weekend.\n\n👉 Save your seat", "sell")]),
 ("Saturday", [
  ("Saturday bake-along 🧑‍🍳", "Who's in the kitchen this morning?\n\nCheck in below and post your progress through the day 🕐", "talk"),
  ("The one tool worth buying", "A kitchen scale. That's it.\n\nCups lie. Grams don't.\n\nIf your recipes are in cups, convert once, write the grams on the card and never think about it again ✍️", "teach"),
  ("Your kitchen right now 📸", "Show us the real thing. Flour everywhere, bowls in the sink, dog waiting for crumbs 🐶\n\nReal kitchens only.", "win"),
  ("Saturday night recipe swap 📖", "Share one recipe that never fails you. Type it out below.\n\nLet's build the group's favourites list together 💛", "talk")]),
 ("Sunday", [
  ("Slow Sunday ☕", "No baking pressure today.\n\nWhat's one thing you want to try next week? Write it here so we can cheer you on 😉", "talk"),
  ("Store bread so it's still good on Wednesday", "Cut side down on a board for day one.\nAfter that, a bread bag or a clean tea towel.\nNot the fridge. It goes stale faster in there.\n\nFreeze what you won't eat by day three. Toast it straight from frozen 🧊", "teach"),
  ("This week's MVP 🏅", "Who helped you this week? Tag them and say thanks.\n\nThis group runs on bakers helping bakers 🫶", "win"),
  ("Starter acting up? Free rescue guide 🆘", "If your starter went quiet this week, don't toss it.\n\nThe Starter Rescue Guide is free for members: 5 fixes, in the order to try them.\n\n👉 Get the Starter Rescue Guide", "free")]),
]

QUIET = [
 ("Rosalind P.", "16 days", "Posted two loaves in September", "Hey Rosalind! Haven't seen your bakes in a bit and I miss them 🥖 How's your starter holding up? No pressure, just checking in 💛"),
 ("Tomasz W.", "21 days", "Asked about rye flour on day one", "Tomasz! Did you ever try that rye loaf? Wednesday's post is all about starters, might be a good one for you 👀"),
 ("Janelle O.", "14 days", "Joined the last workshop", "Hi Janelle 👋 How did your loaves turn out after the workshop? Would love to see a crumb shot if you have one 📸"),
 ("Priscilla D.", "30 days", "Very active in August", "Priscilla, the group's been quieter without you 😅 Anything I can help with? Even a flat loaf is welcome here."),
 ("Arlo M.", "18 days", "Only liked posts, never commented", "Hey Arlo! Glad you're here. What's the one bake you want to get right this year? I'll point you to the right lesson 🍞"),
 ("Wren T.", "25 days", "Shared a pizza win in September", "Wren! That pizza photo still lives in my head 🍕 Are you baking this weekend? Friday's post has a plan for pizza night."),
]

KIND = {"talk": ("Talk", "tag gold"), "teach": ("Teach", "tag"), "win": ("Wins", "tag gold"), "sell": ("Offer", "tag ink"), "free": ("Free resource", "tag")}

CSS2 = """<style>
.sk{background:#fff;border-radius:12px;border:1px solid rgba(26,20,23,.08);padding:9px 11px;box-shadow:0 12px 22px -16px rgba(214,46,115,.5)}
.sk .hd{display:flex;align-items:center;gap:6px;margin-bottom:4px}
.sk .av{width:20px;height:20px;border-radius:50%;background:linear-gradient(135deg,#2f6f73,#f4c95d);color:#fff;font-weight:800;font-size:7.5px;display:flex;align-items:center;justify-content:center}
.sk .ti{font-weight:800;font-size:10px;margin-bottom:2px}
.sk .bd{white-space:pre-line;font-size:9.2px;line-height:1.4;color:#2a2226}
.sk .lnk{color:#2f6f73;font-weight:700;text-decoration:underline}
</style>"""


def post(p, slot):
    t, body, kind = p
    lab, cls = KIND[kind]
    b = esc(body)
    if "👉" in b:
        pre, cta = b.rsplit("👉", 1)
        b = pre + '👉 <span class="lnk">' + cta.strip() + "</span>"
    return f'''<div class="sk"><div class="hd"><div class="av">DF</div><span class="b xs">{OWNER}</span><span class="xs muted">· {slot[0]}</span><span class="{cls}" style="margin-left:auto">{lab}</span></div>
<div class="ti">{esc(t)}</div><div class="bd">{b}</div></div>'''


def daycol(d):
    return f'<div><div style="display:flex;align-items:baseline;gap:8px;margin-bottom:7px"><span class="serif" style="font-size:24px">{d[0]}</span><span class="kicker" style="margin:0">4 posts · scheduled</span></div><div class="grid" style="gap:8px">{"".join(post(p, SLOTS[i]) for i, p in enumerate(d[1]))}</div></div>'


def build():
    T = 8
    P = []
    grid = ""
    for d in W:
        cells = "".join(f'<div style="padding:5px 6px;border-radius:8px;margin-bottom:5px;font-size:7.6px;line-height:1.25;{"background:linear-gradient(135deg,#D62E73,#FF6FAE);color:#fff;font-weight:700" if p[2]=="sell" else "background:rgba(255,255,255,.85);border:1px solid rgba(200,169,106,.45)"}">{esc(p[0])}</div>' for p in d[1])
        grid += f'<div><div class="serif" style="font-size:14px;text-align:center;margin-bottom:5px">{d[0][:3]}</div>{cells}</div>'
    cover = f'''{CSS2}
<div style="display:grid;grid-template-columns:1fr 1.1fr;gap:28px">
<div style="padding-top:14px">
 <div class="kicker">{SVC['name']}</div>
 <h1>A full week of <span class="hl">community posts</span>, written and scheduled.</h1>
 <p class="lede" style="margin:14px 0">Four posts a day, seven days, in the owner's own voice. Loaded into her SkoolKit, published automatically each day, plus the list of members who've gone quiet and exactly what to say to them.</p>
 <div class="card"><div class="upper" style="color:var(--pink);margin-bottom:5px">Built for</div><div class="serif" style="font-size:19px">{CLIENT}</div>
 <div class="small muted">{OWNER} runs a Skool community for home bakers. Voice: warm, funny, lots of emoji, short lines. Sells a paid tier (the Crumb Club) and a two-day Weekend Loaf Workshop, and gives members a free Starter Rescue Guide.</div></div>
 <div style="margin-top:14px" class="fict">★ {FICTIONAL}</div>
</div>
<div style="position:relative">
 <div class="card" style="padding:12px"><div class="upper" style="color:var(--pink);margin-bottom:8px">The week, at a glance</div><div style="display:grid;grid-template-columns:repeat(7,1fr);gap:5px">{grid}</div>
 <div class="xs muted" style="margin-top:4px">Pink = the day's one selling post. Three this week, never two days running for the same offer.</div></div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px">
  <div style="transform:rotate(-2.5deg)">{post(W[0][1][1], SLOTS[1])}</div>
  <div style="transform:rotate(2deg);margin-top:14px">{post(W[2][1][3], SLOTS[3])}</div></div>
 <div class="sticker bub" style="left:120px;bottom:-120px">28 posts<br>+ quiet<br>list</div>
</div></div>'''
    P.append(page(cover, CLIENT, 1, T, "landscape"))

    rows = "".join(f"<tr><td class='b' style='color:var(--pink)'>{a}</td><td class='b'>{b}</td><td>{c}</td></tr>" for (a, b), c in zip(SLOTS, [
        "A light question that gets replies before work. No selling.", "One useful baking lesson a day. Always teaching first.",
        "Members show their bakes. Delia replies to every one.", "Community post, or the day's one offer. At most one selling post a day."]))
    plan = f'''<div class="kicker">How the month is built</div><h2>Four slots. <span class="hl">Teach first, sell third.</span></h2>
<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:16px;margin-top:10px">
<div class="card"><table><tr><th>Slot</th><th>Job</th><th>Rule</th></tr>{rows}</table></div>
<div class="grid" style="gap:12px">
 <div class="hero"><div class="kicker">Spread rules used</div><div class="small">At most one selling post a day. Never two selling posts back to back. The same offer never two days running, and never more than twice a week. Nothing repeats inside 14 days.</div></div>
 <div class="card"><div class="upper" style="color:var(--pink)">Daily auto-publish</div><div class="small">Every post sits in her SkoolKit on its slot. Each morning the day's four are checked live after they publish.</div></div>
 <div class="card"><div class="upper" style="color:var(--pink)">Links</div><div class="small">Every link sits on the call-to-action words. No bare web addresses in the feed.</div></div>
</div></div>
<div class="card" style="margin-top:14px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;text-align:center">
 <div><div class="num">28</div><div class="xs muted">posts this week</div></div><div><div class="num">7</div><div class="xs muted">teaching posts</div></div><div><div class="num">3</div><div class="xs muted">selling posts</div></div><div><div class="num">6</div><div class="xs muted">quiet members flagged</div></div></div>'''
    P.append(page(plan, CLIENT, 2, T, "landscape", zoom=1.2))
    n = 3
    for a, b in [(0, 1), (2, 3), (4, 5)]:
        P.append(page(f'{CSS2}<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">{daycol(W[a])}{daycol(W[b])}</div>', CLIENT, n, T, "landscape")); n += 1
    logrows = "".join(f"<tr><td class='b'>{d[0]}</td><td>4 of 4 published</td><td>Each post opened live after publishing</td><td><span class='tag'>Checked</span></td></tr>" for d in W)
    P.append(page(f'''{CSS2}<div style="display:grid;grid-template-columns:1fr 1.1fr;gap:20px">{daycol(W[6])}
<div><div class="kicker">Daily auto-publish</div><h2>Every post, <span class="hl">seen live.</span></h2><p class="small muted" style="margin-bottom:10px">The owner gets this log each week. A post only counts once it's been opened in the feed.</p>
<div class="card"><table><tr><th>Day</th><th>Published</th><th>Check</th><th>Status</th></tr>{logrows}</table></div></div></div>''', CLIENT, 6, T, "landscape"))
    qrows = "".join(f"<tr><td class='b'>{a}</td><td>{b}</td><td class='muted'>{c}</td><td>{esc(d)}</td></tr>" for a, b, c, d in QUIET)
    P.append(page(f'''<div class="kicker">The weekly quiet-member DM list</div><h2>Six members drifting. <span class="hl">Six messages ready to send.</span></h2>
<p class="lede" style="margin-bottom:12px">Every Monday the owner gets the members who've gone quiet, what they did last, and a short message in her voice. She sends them herself, so they come from a real person.</p>
<div class="card"><table><tr><th style="width:80px">Member</th><th style="width:70px">Quiet for</th><th style="width:150px">Last seen doing</th><th>Message to send</th></tr>{qrows}</table></div>
<div class="card tight" style="margin-top:12px"><span class="small"><b>Why it's in the service:</b> a message from the owner, by name, about something the member actually did, reads nothing like another broadcast.</span></div>''', CLIENT, 7, T, "landscape", zoom=1.18))
    P.append(order_page(SVC, CLIENT, 8, T, "landscape", "A full week: 28 posts across four daily slots, three selling posts spread by the rules, a publish log checked live, and the quiet-member list with messages ready to send. The setup month does this for every week."))
    return doc(P, "DFY Skool Autopilot: proof sample"), FILE, "landscape"
