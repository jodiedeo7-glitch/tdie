# Find Your Door — result emails (MailerLite)

The quiz page shows every result on screen and keeps it there — no result is ever emailed. Under the result, the form subscribes people to the weekly list and tags them with the door they landed on. It is live whenever `MAILERLITE_API_KEY` is set. Steps 1–3 below are what turns those tagged signups into the five door emails; until they're done, people simply join the list.

## Setup — about 20 minutes, once

1. **Create the five groups by hand** in MailerLite (Subscribers → Groups), named exactly:
   `Quiz — Membership Standard` · `Quiz — Membership Premium` · `Quiz — Pretty & Paid PLR Vault` · `Quiz — The Weekend Ecosystem` · `Quiz — Earn With Skool`
2. **Create the eight text fields by hand** (Subscribers → Fields), named exactly:
   `quiz_door`, `quiz_stage`, `quiz_goal`, `quiz_stuck`, `quiz_fear`, `quiz_reframe`, `quiz_first_move`, `quiz_time`
   The function looks both up by name. (It can also create missing ones, but only once the form is live — too late for building the automations below.)
3. **Build five automations.** Trigger: *When subscriber joins a group* → pick one quiz group → one email (below). Turn each on.
4. **In Vercel, confirm `MAILERLITE_API_KEY` exists** (Production). That key alone is what the form needs.
5. **Test** with your own email: the email arrives, the answers fill in, and you sit in one quiz group only.

Merge tags below use MailerLite's `{$field}` format. **Unverified:** the first-name fallback syntax `{$name|default:'there'}` — replace it with the fallback inserted by the editor's own personalisation button.

---

## Email 1 — Membership Standard

**Subject:** Your door: Membership Standard
**Preview text:** Your read, your first three moves, and the fear worth naming.

Hi {$name|default:'there'},

Here's what you told me, and what I'd do about it.

**Where you are:** {$quiz_stage}
**What has to be true:** {$quiz_goal}
**Where it stops moving:** {$quiz_stuck}
**What's underneath it:** {$quiz_fear}

{$quiz_reframe}

Your door is **Membership Standard**. You don't need more information — you need the order it goes in. Standard is the build curriculum: your AI twin and brand, your offer, content, email and Pinterest, in the sequence I'd follow if I started again tomorrow.

**Your first three moves**
1. Start the trial and open the start-here trainings before anything else.
2. Build your AI twin and brand first, so everything after it looks like one business.
3. Shape one offer inside The Monetization Edit before you make a single product.

You told me you have {$quiz_time}. Protect that time, and give it to move one first.

Membership Standard is $9 a month after a free 7-day trial, and you can leave from inside the Skool app whenever you like.

[Start Standard — 7 days free →](https://www.skool.com/thedigitalincomeedit/plans)

Warmly,
Jodie
The Digital Income Edit™
www.thedigitalincomeedit.com

---

## Email 2 — Membership Premium

**Subject:** Your door: Membership Premium
**Preview text:** The blank caption box doesn't get a vote anymore.

Hi {$name|default:'there'},

Here's what you told me, and what I'd do about it.

**Where you are:** {$quiz_stage}
**What has to be true:** {$quiz_goal}
**Where it stops moving:** {$quiz_stuck}
**What's underneath it:** {$quiz_fear}

{$quiz_reframe}

Your door is **Membership Premium**. Your business isn't the problem — the daily writing is. Premium hands you the month already written: 31 days of finished posts, released a week at a time around the 1st, 62 Threads posts, and a start-frame and motion prompt for every Reel. It also includes everything in Standard, plus The Ads Edit™, The Offer Edit, The Funnel Edit and Scaling & Systems.

**Your first three moves**
1. Start the trial and open this month's DFY Content Calendar.
2. Point the calendar's offer days at the one thing you sell.
3. Schedule the first week in a single sitting, then stop thinking about it.

You told me you have {$quiz_time}. With the writing done for you, that time goes to your offer instead of your captions.

Membership Premium is $27 a month after a free 7-day trial, and you can leave from inside the Skool app whenever you like.

[Start Premium — 7 days free →](https://www.skool.com/thedigitalincomeedit/plans)

Warmly,
Jodie
The Digital Income Edit™
www.thedigitalincomeedit.com

---

## Email 3 — Pretty & Paid PLR Vault™

**Subject:** Your door: Pretty & Paid PLR Vault™
**Preview text:** Your shelf is the bottleneck. Here's how to fill it this week.

Hi {$name|default:'there'},

Here's what you told me, and what I'd do about it.

**Where you are:** {$quiz_stage}
**What has to be true:** {$quiz_goal}
**Where it stops moving:** {$quiz_stuck}
**What's underneath it:** {$quiz_fear}

{$quiz_reframe}

Your door is **Pretty & Paid PLR Vault™**. Your shop isn't struggling because you can't sell; it's struggling because the shelf is empty and every new product starts on a blank page. The Vault gives you finished planners, journals, guides, eBooks, printables and coloring sets — Canva-editable, with a full PLR license — plus faceless Reel packs, Pinterest and carousel templates, and training for Etsy, Stan Store, Beacons and Canva rebranding. PLR Glow Studio writes your mockup prompts, SEO titles, descriptions and tags. Twenty new products arrive every month.

**Your first three moves**
1. Pick the three products that fit your niche — not ten.
2. Rebrand them in Canva: your colours, your fonts, your name.
3. Let PLR Glow Studio write the titles, descriptions and tags, then list all three.

You told me you have {$quiz_time}. Three products is a realistic first week at that pace.

Pretty & Paid PLR Vault™ is its own subscription at $11 a month. What you download stays yours, and your license survives if you ever cancel.

[Open Pretty & Paid PLR Vault™ →](https://www.thedigitalincomeedit.com/shop/pretty-and-paid-plr-vault)

Warmly,
Jodie
The Digital Income Edit™
www.thedigitalincomeedit.com

---

## Email 4 — The Weekend Ecosystem™

**Subject:** Your door: The Weekend Ecosystem™
**Preview text:** You already wrote the blog posts. They're just behind a login.

Hi {$name|default:'there'},

Here's what you told me, and what I'd do about it.

**Where you are:** {$quiz_stage}
**What has to be true:** {$quiz_goal}
**Where it stops moving:** {$quiz_stuck}
**What's underneath it:** {$quiz_fear}

{$quiz_reframe}

Your door is **The Weekend Ecosystem™**. You're not short on content; you're short on a place to put it. Over one weekend, the course turns what you've already made — lessons, calls, PDFs, posts — into a website on a domain you own and a blog a stranger can find on Google, with email capture and your offers routed from every article. Claude writes every file. You paste the prompt, read what came back, and say yes or say what to change.

**Your first three moves**
1. Friday night: list everything you've already made. You'll find more than you expect.
2. Saturday: your site goes live and your best lessons become articles.
3. Sunday: email capture, offers on every article, and the system that keeps it running.

You told me you have {$quiz_time}. The build is sixteen hours in six chunks, and you can spread it across three weekends if that fits your life better.

The Weekend Ecosystem™ is $97, paid once, with every future update included.

[See The Weekend Ecosystem™ →](https://www.thedigitalincomeedit.com/shop/weekend-ecosystem)

Warmly,
Jodie
The Digital Income Edit™
www.thedigitalincomeedit.com

---

## Email 5 — Earn With Skool (SCC)

**Subject:** Your door: your own Skool community
**Preview text:** You're already doing the job. You just haven't opened the room.

Hi {$name|default:'there'},

Here's what you told me, and what I'd do about it.

**Where you are:** {$quiz_stage}
**What has to be true:** {$quiz_goal}
**Where it stops moving:** {$quiz_stuck}
**What's underneath it:** {$quiz_fear}

{$quiz_reframe}

Your door is your own community, and the course I point people to for building one is **Earn With Skool (SCC)**. You're already the one answering questions in other people's groups. That isn't a sign you aren't ready — it's the job description.

**Your first three moves**
1. Write down the ten questions people already ask you. That's your first curriculum.
2. Stop waiting to feel qualified, and decide the one result your group is for.
3. Open the room, then learn to earn from it.

You told me you have {$quiz_time}. Move one takes an evening, whatever your schedule looks like.

Earn With Skool (SCC) is $97, paid once.

[See Earn With Skool (SCC) →](https://www.thedigitalincomeedit.com/go/earn-with-skool-scc)

*Affiliate disclosure: Earn With Skool (SCC) isn't my product. I earn a commission if you buy through this link, at no extra cost to you. The owner sets the price and can change it without notice.*

Warmly,
Jodie
The Digital Income Edit™
www.thedigitalincomeedit.com
