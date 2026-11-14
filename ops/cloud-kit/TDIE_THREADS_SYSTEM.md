> **⛔ START HERE — READ THE LIVE SOURCE BEFORE YOU ACT. NEVER WORK FROM MEMORY.**
> Before you write, edit, schedule, post, or send anything based on this file: read it here in full, and open every live source it names (the live Threads account, `canon.json`, and any doc it points to). Never act from memory, from a summary, or from another chat's word. If this file disagrees with a live source — or with what Jodie just told you — **STOP and flag it once. Do not resolve it silently.** Fetch the live file before editing; the project copy is not ground truth.
> **For this file specifically:** the Threads schedule is **18 slots a day** (5:00 AM through the 10:00 PM goodnight) — the exact grid in Section 1, copied from Kira's Daily Posting Schedule PDF. It is **never 14**, and never a different set of slots. Read Section 1 before writing any calendar. **[Superseded 27 Sep 2026 — Job 13 research rebuild. The schedule is now 6 posts a day (7, 9, 11 AM, 1, 3, 5 PM Eastern) plus a daily reply block. Read the new Section 1 below; this sentence is kept only as history.]**
> **REWRITTEN IN FULL 21 September 2026 (Decision 92).** The prior account, `@the.faceless.homestead.mama` (the Tommy Kate AI persona), was permanently disabled by Meta the same day — "we disabled your account... doesn't follow our Community Standards... you cannot request another review of this decision." Threads now runs on `@nursemadedigital`, Jodie posting as herself. Everything persona-specific below is new. Everything mechanical — the schedule, the sales architecture, the hard rules, the engagement window — is Kira Goldberg's Threads Code, unchanged, because none of it was ever about who's posting. **[Superseded 27 Sep 2026 for the mechanical parts — see below.]**
> **SECTION 11 REWRITTEN AGAIN 21 September 2026, evening (founder decision).** The reply-drafting and reply-posting jobs are now two separate scheduled tasks, and Jodie has approved real auto-posting of approved replies on all three platforms, Threads included, now that the root cause of the ban (multiple automations posting to the same Threads account at once) has been identified and fixed. Read Section 11 in full before touching any of these tasks.
> **UPDATED 22 September 2026 (founder request).** The reply-check task now runs three times a day, not two, and each Threads run also suggests 2 to 3 accounts to follow, on top of its niche-account replies. Section 5 and Section 11's table reflect this.
> **UPDATED 22 September 2026, afternoon (founder decision).** Threads replies, outreach comments and follow suggestions now post automatically as soon as they're drafted — no dashboard approval step for Threads. Skool and Facebook are unchanged: those still require Jodie's approval in the Command Centre before anything posts. See Section 5 and Section 11. [Facebook superseded 12 Oct 2026: only Skool waits for approval now.]
> **UPDATED 24 September 2026 (founder decision) — article replies.** A Long Form Teaching post (11 AM or 3 PM) that teaches a topic a live `/learn` article covers now gets a self-reply carrying that article's link, sent by the poster task on its first run at least an hour after the post goes out. Never in the post body. See Section 2a. This is the one new kind of item the poster task sends; no new scheduled task was added. **[Article replies continue under the rebuild; the cap is now one a day, on the 11 AM thread only — see Section 2a below.]**
> **UPDATED 23 September 2026 (founder correction — read this before touching Instagram).** The `@the.faceless.homestead.mama` handle spans TWO different disabled/live states on two different platforms, and this file's history above blurs them. Corrected: the **Threads** profile under that handle is what got permanently disabled by Meta on 21 Sep 2026 (Decision 92) — that's why Threads moved to `@nursemadedigital`. The **Instagram** account `@the.faceless.homestead.mama` was never touched by that disable and is live — it's the account Jodie's Tommy Kate DFY content calendar already runs on (see project file `instagram.md`). Anywhere below that calls the homestead-mama handle "retired" or "disabled" without saying Threads specifically, read it as Threads-only. As of today, the engagement window (Section 5) also runs a light trial on this Instagram account.
> **UPDATED 24 September 2026, later (founder decision) — no DMs, ever; no raw links in outreach/reply comments.** Two new hard rules, added at Jodie's direct request, not in response to any incident: this system never sends a direct message on Threads or Instagram, full stop (see Section 4). And outreach/reply comments left on other people's posts never carry a pasted link — only replies on Jodie's own posts (the offer post's link reply, article self-replies) carry real links, unchanged (see Section 5). For the record: nothing in this system has ever sent a Threads DM, and the documented cause of the Sept 21 ban (Decision 92) was two automations posting to the account at once, not a message — that finding stands.
> **UPDATED 25 September 2026 (founder decision) — ManyChat comment-to-DM approved.** Jodie has directly approved ManyChat comment-to-DM automation on Threads and Instagram — someone comments a trigger word on a post, ManyChat sends them a pre-approved DM with the link. This is the named exception the 24 Sep no-DM rule said would need her sign-off; outreach and reply comments on other people's posts still never turn into a DM. See Section 4 and Section 9.
> **UPDATED 27 September 2026 — rebuilt from research (Job 13, Jodie's approval).** Rebuilt from the Threads viral research: 6 posts a day (was 18), the offer slot moves to 1 PM (was 5 PM), a daily reply block replaces the 30-minute engagement window, and the old capitalised opener labels are cut for five first-line shapes seen at the accounts that actually grew. Full change log below. **Jodie authorised this rebuild, including changes to rules that came from The Threads Code (Kira Goldberg) — where the two differ, this rebuild wins.** Bio and display-name change: approved by Jodie 27 Sep 2026, made live 2 Oct 2026 by the nightly top-up task — see Section 0.

> **UPDATED 12 October 2026 (founder standing approval).** Jodie: "anything outside of skool can be auto approved. no need to add them to my reply tab. standing approval." Facebook and Instagram engagement items now go into the Command Centre as `status: "approved"`, like Threads, and never sit on the Replies tab. Only Skool still waits for her tick. The held Threads outbound items (the dispatcher's policy-threads-outbound switch), the one-session rule and every content rule are unchanged. Recorded in canon.json meta.standing_approval_outside_skool_2026_10_12.

# TDIE THREADS SYSTEM — @nursemadedigital

### Current · 27 September 2026 (rebuilt from the Threads viral research, Job 13 — 6 posts a day, 1 PM offer, daily reply block) · Single live copy, edited in place

**Former governing document on Threads: The Threads Code (Kira Goldberg)** — the Daily Posting Schedule PDF, the 40-page ebook (5-Layer Sales Architecture, hook system, engagement window, bio formula), `Types_of_Threads.docx`, the Claude prompt library. Founder decision, 18 Sep 2026: where The Threads Code and any other TDIE rule conflicted, The Threads Code won on Threads. **Superseded 27 Sep 2026 where it differs from this rebuild** — see the change log immediately below for every line changed and the evidence behind it. `Threads_Unleashed.pdf` (Adam, @piss.off.boss, a different creator) remains a secondary, non-governing voice-craft reference only.

**Voice governance is separate from schedule/mechanics governance.** For what the posts actually say and sound like, **`claude/TDIE_JODIE_THREADS_VOICE.md` sets the voice** and overrides Section 3 below and `TDIE_CANON.md` §7, the same relationship `TDIE_TOMMY_KATE_VOICE.md` used to have for the retired persona. Read it before writing a single post — it now includes one added section, "THE ORIGIN LINE AND REAL SMALL NUMBERS."

---

## CHANGE LOG (27 September 2026 rebuild — every change, with the evidence)

Evidence references are to `ops/cloud-output/threads-research-2026-10/REPORT.md` (findings and pattern table) and `EVIDENCE.md` (post-by-post notes); account codes (A01, A03) are rows in `ACCOUNTS.csv`. The research is built from search excerpts only (the network policy blocked direct page fetches to Threads and every platform checked), so counts are "accounts where the pattern was seen," not proof of cause.

| # | Section | Verdict | What changed | Evidence |
|---|---|---|---|---|
| 1 | Schedule | CHANGE | 18 fixed hourly posts a day (5 AM to 10 PM) becomes **6 posts a day at 7, 9, 11 AM and 1, 3, 5 PM**, plus a daily reply block. | No documented grower in or near the niche posted more than 4 to 5 times a day: Naji's jump came at "4-5 short-forms/day" (A03, VERIFIED); Kumar 1 to 3 a day (A21); Taz about 1.4 a day (1K threads in about two years, A01); @melodijoelperez about 1.4 a day (644 threads, A10); Annisy daily (A05). BlackTwist: 5 to 6 posts a week had the best median growth in March 2026 (8.87%); daily posters' median was 3.35%. Four counter-examples show daily volume alone did not grow accounts (A06, A23, A24, A27). 6 a day (42 a week) sits above every dataset's "10+ a week" bucket and inside the range of the accounts that jumped. |
| 2 | Slot times | CHANGE | Times drawn from the only timing data found: weekday mornings and early afternoon. Evenings dropped. | Buffer, 2.5M posts: 6 to 11 AM weekdays highest median engagement, 6 to 11 PM lowest every day (VERIFIED excerpt). BlackTwist timing study, 109,300 posts: "late morning to early afternoon dominates during the week" (VERIFIED excerpt). Kumar: 9 to 11 AM best on his account (A21). Kira's "highest engagement" gold rows were her own account's data; no other account's data supports them. Weekend days are kept (BlackTwist: Saturday best reach in Feb and Mar, Sunday in Jul). |
| 3 | Post types | CUT and REPLACE | Good Morning, Inspiring Good Morning, Goodnight, SPOILER, "Viral Optimized (built only to get seen)", Non-Sexual Turn On, If Your Finger Touched This, Don't Act Like You Didn't See This, Dear algo, Breaking News, Girl to Girl, The Real Flex, I Promise You and the capitalised opener labels are cut. Replaced by **six post shapes** seen at the jumps. | Not one of the 24 jump accounts showed a good-morning, goodnight, spoiler or "finger" post (0 of 24). Shapes seen: first-person identity or origin opener 8 of 24 plus A07; the creator's own real numbers 9 of 24; long numbered thread 8 of 24; open question or invitation to post your own thing 4 of 24; personal struggle or update 5 of 24 plus A07; contrarian one-liner 3 of 24; audience callout ("Content creators:") A02, A03. Reach-only posts are cut because reach without followers is the most common counter-example (A25, A26, A41, A47). |
| 4 | Hook system | CHANGE | "Never the same hook twice in a day" stays. Kira's "write the first line last" stays. The label list is replaced with **the five first-line shapes** below. | Taz's earliest 30K-view post on a tiny account credits an "I WAS..." first line (A01, VERIFIED, about Oct 2024). Naji's audit of two years of his viral posts found six recurring formats: personal updates, milestones, transformations, calling out an audience, lessons, controversy (A03, REPORTED). No growing account used labelled openers in capitals. |
| 5 | Five-layer sales architecture | KEEP (reworded) | Interrupt, Prove, Teach, Aspire, Convert stay as the daily spine, mapped to the six shapes. Aspire is redefined as "what I built or broke today" and real milestones. | Matches what was observed: identity openers (Interrupt), number-first posts (Prove), numbered threads (Teach), personal updates and milestones (Aspire: Naji's two most-cited formats, A03), product as the punchline (Convert: Gladys's one post produced 102 downloads, A06). |
| 6 | One offer a day | KEEP, slot moved | One offer a day stays. It moves from 5 PM to **1 PM**. The rotation table stays. | Product-name-only-in-the-offer-slot has no counter-evidence strong enough to change it. 5 PM sits at the edge of Buffer's weakest window; 1 PM sits inside both timing datasets' best band (change 2). |
| 7 | Link timing | CHANGE | The 2-hour wait before the link reply is cut. **The link goes in Jodie's first reply straight after posting.** A ManyChat comment-to-DM keyword may be offered in the same reply. | Mosseri, Nov 2024: "We don't downrank links, but we don't place much value on p(click) and people don't like and comment on links much" (VERIFIED). 9 of 24 growing accounts carried a link, a product name or a lead magnet in the growth posts themselves; Lennox, Naji and Tadeas put raw links in the body and grew. Waiting 2 hours has no evidence either way; a reply keeps the body link-free (never-rule) and keeps the CTA visible during the first hour, when replies are happening. |
| 8 | Article replies | KEEP, cap lowered | One a day at most (was two), on the 11 AM thread only. | Links in replies did not stop growth (A10 hands out newsletter links in replies). Fewer posts a day means one teaching thread a day. |
| 9 | Engagement window | CHANGE | 30 minutes after posting becomes **a daily reply block: reply to every comment on Jodie's posts within the hour, and leave 20 genuine comments a day on other accounts' newest posts in the niche.** Following a few accounts stays. | Replies are the most repeated signal: 9 of 24 accounts and every BlackTwist month (Jul 2026 reply ladder 2.90% to 19.00% median growth); Buffer's 128,000-post regression: replying to comments lifts a post's engagement about 42%. Kumar: 20 to 30 accounts a day (A21). Counter: Annisy grew without 50 comments a day (A05), so 20 is the floor, not 50. |
| 10 | Bio and display name | CHANGE (approved 27 Sep 2026; live 2 Oct 2026) | The live bio contained an em dash and did not name the reader. New wording approved and made live 2 Oct 2026 — see Section 0. | Bio matched to a narrowed topic is the cleanest before-and-after in the record: Lennox rewrote his bio to his top three topics after ten slow months (A08); Taz credits "clearly communicating what she provides in her bio" for her 5,000-follower week (A01); Rosette's bio names the reader and the feeling (A12); Tami's failure post-mortem was "narrow the content focus" (A23). The live bio's em dash breaks a brand-wide never-rule. |
| 11 | Weekly build | CHANGE | 7 × 18 = 126 posts becomes **7 × 6 = 42 posts plus a daily reply block**. The repurposing rule changes to **Lennox's method: each Friday, pull the week's top 3 posts by replies and top 1 by new followers, name their shape, and build next week's 7 AM and 3 PM posts from those shapes.** | Lennox's stated method after ten slow months (A08). Gladys: "study your insights to see which formats perform best, every account behaves differently" (A06). Naji: "I studied the platform again, ran tests" before his jump (A03). |
| 12 | Long teaching thread length | CHANGE | The 11 AM thread may run as a numbered multi-post thread: an opening post under 500 characters plus up to four numbered self-replies, each under 500. Every single post stays under 500. | BlackTwist: long-form threads had the most views in every month reported (Jul 2026: 12,899 average views, about 18 times a short post); 8 of 24 jump accounts used long numbered threads. Short posts had the best engagement rate, so the other five slots stay short. |
| 13 | Automation note | CHANGE | Posts may still be scheduled, but the reply block cannot be automated and is the part the evidence ties to growth. Nothing here changes the one-session rule (Section 11). | Every reply behaviour in the record was a person replying (A06, A15, A21, A22). |
| 14 | Content mine (Shopify Edit) | KEEP | Unchanged. | No evidence either way. |
| 15 | Friday readout | KEEP, expanded | Add "top 3 posts by replies, named by shape" and "what I will repeat next week". | Change 11. |
| 16 | Voice file | ADD one section | `claude/TDIE_JODIE_THREADS_VOICE.md` adds "THE ORIGIN LINE AND REAL SMALL NUMBERS". Nothing else in the voice file changed. | Finding 2: first-person identity openers (8 of 24 plus A07) and real numbers in the first line (9 of 24) are the second most repeated pattern, and the voice file had no example of either shape. |

Rules that did not change and never will, whatever the research says: no em dashes; no AI-sounding language; no faith content; no invented numbers, testimonials or scarcity (income figures only if they are real ones Jodie supplied); every product, price and link from `canon.json`; no link in a post body; no DMs except the approved ManyChat comment-to-DM flow; no pasted links in comments on other people's posts; never Tommy Kate on this account; one automated session on the account at a time.

What the research could not settle and this rebuild does not pretend to: whether posting time matters at all (datasets contradict); whether video helps (one data point against, datasets split); whether a bigger account engaging is a trigger (three thin cases); how long the floor lasts (six to sixteen months in the in-niche cases; 14 days to 90 days in the seller-reported ones). Every fast grower in Jodie's exact niche sells a Threads-growth product, so their own numbers are also their marketing — a bias to hold in mind, not a reason to distrust every data point.

Full research: `ops/cloud-output/threads-research-2026-10/REPORT.md` (report), `EVIDENCE.md` (post-by-post notes), `ACCOUNTS.csv` (50 accounts, 162 data points).

---

## ACCOUNT

Threads `@nursemadedigital`, linked to the Instagram account of the same handle. 94 Threads followers on 21 Sep 2026. The prior Threads account `@the.faceless.homestead.mama` was permanently disabled by Meta on 21 Sep 2026 (Decision 92); cause: two automations posting at once. **Persona:** Jodie DeOliveira herself — the founder, owner, coach and mentor of The Digital Income Edit™. Not an AI persona. Not faceless. She writes in first person, as herself, by name and by face. See `TDIE_CANON.md` Decision 92 for why this account is the deliberate exception to the retired-NurseMadeDigital-brand rule and to "The New Faceless" positioning. **Who she writes for:** women who want online income, run by real systems rather than hustle, who want a founder who'll tell them the truth about what actually works.

**Second account in the engagement window (unchanged by this rebuild): Instagram `@the.faceless.homestead.mama`** — the Tommy Kate persona account (see project file `instagram.md`). Live and separate from the disabled Threads profile of the same handle. Section 11 covers what runs there.

## 0 · PROFILE

**Display name, live:** Jodie DeOliveira | Faceless Income with AI

**Bio, live** (two lines, 143 characters, under the 150 limit):
```
For women building faceless online income with AI. Systems, not hustle.
I built The Digital Income Edit™ solo, with Claude. This account is me.
```

**Link field (unchanged):** https://www.thedigitalincomeedit.com/resources/find-your-door

Why this wording: names the reader, names one topic instead of several, keeps the credibility line and the "this account is me" fact, removes the em dash the prior bio had (Evidence: change-log row 10 above).

Edit approved by Jodie 27 Sep 2026 (Job 13 rebuild); made live on the account 2 Oct 2026 by the nightly top-up scheduled task (`trig_011siYi2AzBsXpGVwG91j7MH`), verified live the same run.

## 1 · THE DAY (6 posts, Eastern time, every day including weekends)

| Time | Shape | Layer | Rule |
|---|---|---|---|
| 7:00 AM | OPEN: a first-person identity or origin line, or one contrarian sentence | Interrupt | Short. No product, no link. |
| 9:00 AM | ASK: an open question, or an invitation to post your own thing (your offer sentence, your freebie, your first line) | Interrupt / conversation | Jodie replies to every answer within the hour. |
| 11:00 AM | TEACH: a numbered thread, opening post plus up to four numbered self-replies | Teach | One article reply allowed under it on a genuine match. No product. |
| 1:00 PM | OFFER: a story or a fact with the day's offer as the punchline | Convert | Link in Jodie's first reply straight away. ManyChat keyword optional. Product name lives here only. |
| 3:00 PM | PROOF or TAKE: one real number from the work, or one opinion the industry won't like | Prove | Real numbers only. |
| 5:00 PM | UPDATE: what I built, broke or shipped today, or a real milestone | Aspire | Never staged. Small numbers are fine and are the point. |

Close to the hour is close enough. Weekends keep all six. Nothing after 5 PM.

**Daily reply block (the part the evidence ties to growth) — never automated:**
1. Within 60 minutes of each post, reply to every comment. Replies are answers, not "thank you".
2. 20 genuine comments a day on other accounts' newest posts in the niche (a perspective, an experience or a question, never "great post"). No links, ever, in those comments.
3. Follow a handful of the accounts you commented on.
4. On a day a post moves (replies keep coming), stay in it. Every creator who described a good day described a day of replying.

## 1a · THE FIVE FIRST-LINE SHAPES (never the same shape twice in a day)

Kira's rule stays: write the post, then write the first line last.

1. **The origin line.** "I was [true past state]. [True present fact]." Example shape: "I was a burnt out 46 year old teacher, 11 followers, no clue how to write threads." (A01.) For Jodie: what she was before TDIE, the account Meta disabled, the 94 followers.
2. **The real number.** A figure from the work, first: "Twenty-two approvals and zero lines of code." Real figures only; small ones count.
3. **The named reader.** "[Who]: [truth]." "Content creators: your first 100 followers matter more than your first 1,000 likes." (A02.) Six M self-reference: "If you're X, this is for you."
4. **The open question.** "Genuine question for anyone running a Skool group: ..." Kumar's open questions beat statements three to one on his account (A21).
5. **The unpopular opinion.** One sentence the industry won't like, then why. (A02, A03, A10.)

Cut from the old list: every capitalised label, faith-sounding lines, "finger" hooks, "Dear algo", "SPOILER", good-morning and goodnight posts.

## 1b · THE FIVE LAYERS (kept)

- **Interrupt** (7 AM, 9 AM): the reader feels addressed. No product, no link.
- **Prove** (3 PM): a real number, a timeframe, a name. Lead with the number.
- **Teach** (11 AM): the numbered thread. Insight, system, result.
- **Aspire** (5 PM): what got built or broke today; a real milestone. Never staged.
- **Convert** (1 PM): the product as the punchline of a story. Never a hard pitch, never a headline.

## 2 · THE OFFER ROTATION (1:00 PM lead offer; link in Jodie's first reply; no cap on how many offers a day, Decision 132)

| Day | Offer | Price | Link (goes in the reply, exactly as printed) |
|---|---|---|---|
| Monday | AI Influencer Starter Twin | $97 | https://links.thedigitalincomeedit.com/shop/fdfdf1a4-ce57-4bdb-8a41-df57e5d13c2f |
| Tuesday | The Weekend Build Challenge | free | https://www.thedigitalincomeedit.com/resources/weekend-build-challenge |
| Wednesday | Pretty & Paid PLR Vault™ | $11/month | https://links.thedigitalincomeedit.com/shop/e7555c8f-7348-4ab4-99ce-0569d6dd0839 |
| Thursday | The Weekend Ecosystem™ | $97 one-time | https://www.thedigitalincomeedit.com/weekend-ecosystem/preview (sales page https://www.thedigitalincomeedit.com/shop/weekend-ecosystem only when the post names the price) |
| Friday | The Operating Prompts™ | $19 | https://links.thedigitalincomeedit.com/shop/607fd173-9065-49f3-9a69-7b18ac2b5876 |
| Saturday | The Digital Income Edit™ membership, Standard | $9/month · $99/year, 7-day free trial (Premium quoted alongside as $35/month · $297/year) | https://www.skool.com/thedigitalincomeedit/plans |
| Sunday | Find Your Door quiz | free | https://www.thedigitalincomeedit.com/resources/find-your-door |

**Real-date swaps** (a canon row takes the slot on a real date, named as what it is): the Kit window, Thu 1, Sat 3 and Sun 4 Oct 2026: The Weekend Ecosystem™ with The Keep It Running Kit (six paid guides free with it until Sun 4 Oct 2026, 11:59 pm Eastern), marked "SWAP FOR APPROVED KIT TEXT IF YOU HAVE IT" in the week files. Amazon Prime Big Deal Days, Tue 6 and Wed 7 Oct 2026: the Amazon Influencer Storefront ($0, canon) takes Tue 6 Oct, with the affiliate disclosure in the same reply as the link; Wed 7 keeps the table. From the next day the table returns.

Promotion in the other slots, and the other products the master plan assigns to Threads (`claude/TDIE_PROMOTION_MASTER_PLAN.md`), run on top of this default table. Never promoted on Threads: The Tommy Kate Edit, Pinterest Foundations™, anything in `canon.json` `flagged_not_cut`, the Weekend Ecosystem™ affiliate program, 8 Claude Prompts (retired).

## 2a · ARTICLE REPLIES

When the 11 AM thread genuinely matches a live `/learn` article, one self-reply: a short line in Jodie's voice plus the printed URL (www, no trailing slash). At most **one a day** (lowered from two). Never the same article twice in a week. Not an offer, never names a product. In week files: `ARTICLE REPLY: <text with URL>` under the 11 AM post. Live articles are the pages in `src/pages/learn/` (index: `TDIE_RESOURCE_MAP.md` Part 6).

## 3 · VOICE

**Governing document: `claude/TDIE_JODIE_THREADS_VOICE.md`.** Read it in full before writing, including the added section "THE ORIGIN LINE AND REAL SMALL NUMBERS." In short: Jodie's own real voice — snarky, funny, smart, to the point, an authority, a good seller, not soft, a girls' girl who cheers other women on with specific encouragement and real tips, not generic hype. Never a persona. Never a character.

**Format mechanics stay Kira's, unchanged:** short lines, a line break between every separate thought, contractions, no em dashes ever. Mobile-first: one or two sentences per line, heavy white space. Avoid filler words ("well," "very," "just," "so," "really," "actually," "probably," "already," "finally," "simply," "quickly," "slowly").

The first line is the entire job. Write the post, then write the first line last.

**What's gone, permanently, from this account's voice:** homestead imagery, gamer imagery, farmhouse/chicken/attic references, "she" written about a persona in the third person anywhere. All of it belonged to Tommy Kate, not to Jodie.

## 4 · HARD RULES (fail the post if any is broken)

- No em dashes. Ever.
- No AI-sounding language: "game-changer," "utilize," "delve," "journey," "elevate."
- Product names may appear in any post when the story calls for it (Decision 132, 13 Nov 2026 removed the product-name-only-in-the-offer-slot cap). The link still goes only in a reply, never the body.
- Under 500 characters per post, including every post in a numbered thread.
- Additional banned vocabulary beyond Kira's list: hack, secret, explode, crush it.
- No manufactured scarcity ("limited spots," "joined this week"), no fabricated proof, no invented testimonials, no promises about how fast anything happens. A real deadline (the Kit, the Premium price change) is fine.
- Prices exact, never "from $". Full trademarked names on first reference. Links exactly as `canon.json` prints them.
- **Tier prices are $9/month · $99/year Standard and $35/month · $297/year Premium.** Closed item, not reopened.
- Near Pretty & Paid PLR Vault™, never: upgrade, downgrade, tier, level, step up, next step, plan. Never "the Vault" or "PLR Vault" as a first reference.
- Never "VIP," "Free Community," "free tier."
- **No faith content of any kind.** No God, prayer, blessing, church, scripture, "you were meant to see this." Permanent founder decision.
- Income and earnings claims are PERMITTED (Decision 131, 29 October 2026: income and earnings claims are allowed on every surface.) Real numbers the founder has supplied only. Never invented.
- Never a link in the body. Links live only in replies: the day's 1 PM offer link (posted immediately, not after 2 hours), and up to one article self-reply a day (Section 2a).
- **Never reintroduce Tommy Kate, the homestead persona, or "faceless" framed as Jodie's own personal visibility on this account.**
- **No direct messages from outreach or reply automation** — comments left on other people's posts never turn into a DM. The one named exception: ManyChat comment-to-DM automation on Jodie's own posts (Section 9), triggered only by someone commenting a keyword.
- Only one automated session may act on the live account at a time (Section 11).

## 5 · WEEKLY BUILD (Sunday)

7 days × 6 posts = **42 posts a week**, plus the daily reply block. For each day, follow the schedule in Section 1, **in Jodie's own voice per `claude/TDIE_JODIE_THREADS_VOICE.md`**, with the day's offer from Section 2 in the 1 PM slot. Vary first-line shapes (Section 1a) — never the same one twice in a day.

**Friday method (Lennox's, replacing the old "repurpose one Viral slot" rule):** from Threads Insights, list the week's top 3 posts by replies and top 1 by new followers. Name each one's first-line shape. Next week's 7 AM and 3 PM posts reuse those shapes with new material — not the words, the shape.

Output file: `claude/threads-week-YYYY-MM-DD.md`, dated with the Monday it covers. One block per post:

```
### DAY: Monday 5 October 2026
#### 7:00 AM · OPEN
<post text>
#### 9:00 AM · ASK
<post text>
#### 11:00 AM · TEACH
<opening post>
1/ <self-reply>
2/ <self-reply>
ARTICLE REPLY: <one line with the full /learn URL, only on a genuine match>
#### 1:00 PM · OFFER
<post text>
LINK REPLY (post immediately): <one line> <link exactly as canon prints it>
#### 3:00 PM · PROOF or TAKE
<post text>
#### 5:00 PM · UPDATE
<post text>
```

**This step writes to a project file only — it does not open a browser or touch the live Threads account.** No conflict with the one-session rule in Section 11.

## 6 · LOADING (nightly, desktop-mediated)

Threads' native scheduler is used. Observed queue cap: about 25 scheduled posts (confirmed 19 Sep 2026 — the 26th scheduling attempt silently failed despite a successful-looking banner). At 6 posts a day the queue holds several days plus, so tomorrow's 6 are loaded each night from the current week file to keep a consistent buffer. Each post is loaded as an original post via the composer's three-dot menu → Schedule. A TEACH post's numbered self-replies (`1/`, `2/`...) are posted as replies to the 11 AM post in order, once it's live; the 1 PM offer's `LINK REPLY` is posted as Jodie's first reply immediately after the offer post goes live, not after a wait; an `ARTICLE REPLY:` line is posted as a reply to the 11 AM post.

**Logging into the correct account (added 21 Sep 2026, corrected 23 Sep 2026 — read this before touching the browser).** Multiple Instagram accounts are logged into this Chrome profile, including `the.faceless.homestead.mama` — **that account's Threads profile is disabled; the Instagram account itself is live** (see the note at the top of this file) and is the account the Section 11 Instagram engagement trial runs against. For Threads work specifically, `Continue with Instagram` on the Threads login screen can default to the wrong one, or land on the disabled Threads screen entirely. The reliable method:
1. Go to `instagram.com/accounts/edit/` (or any Instagram page) to see which account is currently active.
2. If it isn't `nursemadedigital`, open the hamburger menu (bottom-left) → **Switch accounts**, and select `nursemadedigital` from the list — it's already logged in on this device, no password needed.
3. From there, a link to the Threads profile (or `threads.com/@nursemadedigital`) opens Threads already authenticated as the right account.
4. If Threads still shows the disabled-account screen, click **Log out** on that screen first, then repeat from step 1 — logging out clears the stuck session.
5. **Never type a password to switch accounts.** If the account switcher doesn't show `nursemadedigital` as an option, stop and tell Jodie — that means it's no longer logged in on this device and needs her to sign in herself.

For the Instagram engagement trial, switch the same way to `the.faceless.homestead.mama` instead — that account works fine on Instagram; it's only its Threads profile that's dead.

Known composer behaviour on threads.com: the composer can drop the first two or three characters typed, so type a throwaway prefix, select all, and retype. The time picker reads 12 as midnight; use 1:00 PM for the midday slot. Opening the schedule menu twice in one tab can freeze it; use a fresh tab per post. Times in Section 1 are a guide, not a fixed requirement.

**The reply block (Section 1) is done by a person or by the one live session — never by a second automation.**

## 7 · FRIDAY READOUT

Threads Insights: for the last 7 days, views, replies, reposts, profile visits, new followers, link clicks. **Top 3 posts by replies, named by shape (Section 1a). Top 1 post by new followers. What gets repeated next week (Section 5's Friday method).** Account Status (Settings → Account → Account Status) must read eligible for recommendation; if it doesn't, stop posting the 1 PM offer slot until it clears and say so. Use the account-switching method in Section 6 to make sure this reads `nursemadedigital`'s own Insights, not a leftover session on another account.

## 8 · CONTENT MINE — THE SHOPIFY EDIT (physical products)

The Digital Income Edit™ has a full 17-lesson Shopify course (print on demand and dropshipping) and a free Shopify Store Kit with a 30-niche vault. This is a **content mine for the TEACH and PROOF/TAKE slots, not a new daily offer** — the seven-day rotation in Section 2 is fixed and does not gain a Shopify day unless the founder adds it to canon.

Raw material, all rule-safe: the 30 niches from the Vault make TEACH threads ("7 things that sell to nurses / dog people / new moms and never need your face"); lesson insights make sharp OPEN one-liners (nothing is made until it's paid for; the store is yours, the marketplace shelf isn't; sample it before you sell it); the Etsy-exodus angle is live and on-audience (`claude/TDIE_ETSY_EXODUS_ANGLE.md`).

Links: run as pure value with no link, or in the 1 PM link reply ONLY if the founder promotes it as the day's offer. Income claims stay off unless a real founder number exists.

## 9 · MANYCHAT COMMENT-TO-DM AUTOMATION — APPROVED AND IN BUILD (rewritten 25 September 2026, founder decision)

**Reversed 25 Sep 2026.** Section 4 called this off the table pending Jodie raising it by name — she has, directly ("Many chat has ALWAYS been ok... Open manychat and set it up"), so ManyChat comment-to-DM automation is now approved and being built for both Threads and Instagram. This is a different mechanic from the original `ManyChat Welcome DM Sequence` doc (which used a "new follower" trigger) — this is **comment-to-DM**: someone comments a trigger word on a post, ManyChat auto-sends them a pre-approved DM with the link to what they asked for.

**Why this doesn't reopen the Section 4 problem:** the no-DM rule was written to stop cold, unsolicited outreach DMs. A comment-to-DM flow only ever messages someone who opted in themselves, by commenting the keyword under a post. It's the same shape as the link-reply mechanic already used everywhere else in this system, just delivered privately because Instagram comments can't carry a clickable link.

**Threads:** ManyChat has native Threads DM automation support — build it there directly.
**Instagram (`@the.faceless.homestead.mama`):** trigger word and destination link are pulled from that day's DFY Content Calendar post — the calendar sets the offer, the automation just delivers it.

Setup status and the live flow details are being built now — see the working notes as they're produced.

## 11 · THE ONE-SESSION RULE — READ THIS BEFORE ANY TRIGGER TOUCHES THREADS OR INSTAGRAM

**REWRITTEN 21 September 2026, evening — founder decision.** The original rule (below, kept for the history) was written the same day the prior account was banned, when the cause was still a leading suspect rather than a confirmed fact and no separate posting mechanism existed yet. Jodie has since identified the actual cause — multiple automations posting to the same Threads account concurrently — and fixed it. She has explicitly asked for real auto-posting of her approved replies on Skool, Facebook, and Threads alike, accepting a short stagger between consecutive Threads posts as the ongoing safety margin rather than a full ban on automated Threads posting.

**Only one automated session may have a browser open against the live Threads account at any given moment.** That principle is unchanged — it's the actual fix, not the earlier blanket "never auto-post" rule. Two sessions logging into and acting on the same Threads account in a tight window reads to Meta as the "high volume" abuse pattern, and is the confirmed cause of the prior account (`@the.faceless.homestead.mama`) getting permanently disabled: a now-deleted duplicate trigger ("Post approved replies") fired at 9:07 PM UTC on 20 Sep 2026, 23 minutes before the main reply-check trigger's scheduled 9:30 PM run, and the account was disabled the next day.

**Updated 22 September 2026 (founder request):** the reply-check row below now runs three times a day instead of two, and each Threads run also drafts 2 to 3 follow suggestions alongside its niche-account replies. Same two-task split as before; only the frequency and the addition of follow-drafting changed.

**Updated 22 September 2026, afternoon (founder decision):** Threads no longer waits in the Command Centre for Jodie's tick. The reply-check task writes every Threads reply, outreach comment and follow suggestion straight in with `status: "approved"`, and the poster task below sends it on its own next run without her reviewing it first. **Skool and Facebook still go in as `status: "pending"` and still wait for her approval** on the Command Centre before anything sends. [Superseded 12 Oct 2026 for Facebook: standing approval, only Skool waits.] This is purely an approval-gate change — it does not touch the one-session rule above or the posting stagger below, both of which stay in force on Threads regardless of who or what approved an item.

**Updated 23 September 2026 (founder decision):** the same reply-check task now also covers Instagram (`@the.faceless.homestead.mama`, the account itself — NOT the disabled Threads profile of the same handle) — see Section 5 for what it does there (follow trial, resharing, natural liking). Instagram items go in `pending`, same as Skool and Facebook, not auto-approved like Threads. [Superseded 12 Oct 2026: Instagram items go in `approved`; only Skool waits.] The one-session rule applies to Instagram exactly as it applies to Threads: never run two automated sessions against the same Instagram account at once.

**The canonical, current list of scheduled tasks that touch the live Threads and/or Instagram accounts. Times re-read from the live scheduled-task list on 24 Sep 2026 (the earlier version of this table had stale times). Post counts and slot times updated 27 Sep 2026 for the Job 13 rebuild — see the tasks themselves for the current wording.**

| Task | When it runs (Eastern, with UTC) | Touches the browser? | Can it post/comment/follow? |
|---|---|---|---|
| All-platforms reply-check + Threads/Instagram engagement (`trig_01YGmXBAn4HYU864aebprtoe`) | 8:30 AM, 1:30 PM and 7:30 PM daily (12:30, 17:30, 23:30 UTC) | Yes | **On Threads: no. It never opens a composer to send anything itself.** Writes every proposed reply, outreach comment, follow suggestion and reshare into the Command Centre's `engagement` collection (https://claude.ai/artifact/7sggSqfNcfRDscpy3fsg4C). Skool items go in as `status: "pending"` for Jodie to approve; Facebook and Instagram items go in as `status: "approved"` (standing approval, 12 Oct 2026). **Threads items go in as `status: "approved"` already** (founder decision, 22 Sep 2026). Every drafted outreach/reply item, on any platform, is a public comment — never a DM (Section 4) — and never carries a pasted link (Section 4). On Instagram it also likes posts live during the same scroll (logged, not queued) and drafts 2–3 follows per run as `pending`. |
| Post approved Command Centre replies (`trig_01TMtwX7Ns9RhKwMGSnyVeoX`) | 9:15 AM, 2:15 PM and 8:15 PM daily (13:15, 18:15, 00:15 UTC), 45 minutes after each reply-check | Yes, only when there's something approved | **Yes. The only task that ever posts or follows.** Reads `engagement` for status "approved" and sends/follows each one, verifying it landed and marking it "posted". Also sends article self-replies (Section 2a) once their time has passed. Waits 60–120 seconds between consecutive Threads items in the same run. Stops a platform at once on any disabled/suspended/restricted notice. Sends public comments only — never a DM. |
| Nightly: top up Threads scheduler queue (`trig_011siYi2AzBsXpGVwG91j7MH`) | 11:30 PM daily (03:30 UTC) | Yes | Loads tomorrow's pre-written posts (Section 6) and writes article-reply items to the Command Centre. |
| Friday ops readout (`trig_01LTeHzmN4VcA9QYURtAjhb9`) | 11:30 AM Fridays (15:30 UTC) | Yes | Read-only on Threads, plus link replies on offer posts that are missing their link. |
| Sunday: write next week's Threads (`trig_019yn2AGsPQocy8gAdaN3oaA`) | 6:00 AM Sundays (10:00 UTC) | **No. Writes to a project file only, never opens a browser** | None |
| Weekly Daily Prompts build (`trig_01JFD28qXDxECtjjFDwLycui`), added 24 Sep 2026 at Jodie's direct request | 9:00 PM Saturdays (01:00 UTC Sunday) | Yes: Skool classroom, Gemini, Higgsfield. **Never Threads, Facebook or Instagram** | Creates draft Daily Prompts lessons in the Skool classroom only; never posts, comments or follows. |
| TDIE: Post today's DFY calendar post to @the.faceless.homestead.mama (`trig_01SWgRtfhndDsaXZXNE8kyBB`), added 25 Sep 2026 | 11:47 AM daily (15:47 UTC) | Yes: Instagram `@the.faceless.homestead.mama` only | Posts the day's Premium DFY Content Calendar post to that Instagram account. It checks the shared log first and waits if another Instagram or Threads task is mid-run. It never touches Threads and never posts a link. |

None of the Threads-touching times overlap. The closest pair is the 7:30 PM reply-check and the 8:15 PM poster, which is deliberate: the poster sends what the reply-check just drafted. **No sixth trigger may be created that touches Threads, Skool, Facebook, or now Instagram.** If a job needs to change, edit one of the tasks above in place — never add a parallel one.

**Any trigger, session, or task about to open a browser against Threads or Instagram should treat this table as the source of truth** for what else might currently be running, and should never open a second session against the same account while another one it knows about could plausibly still be executing.

---

**Original 21 Sep 2026 (morning) version of this section, kept for history:** "Only one automated session may have a browser open against the live Threads account at any given moment. This is not a style preference — running two sessions against the same account close together is the leading suspected cause of the prior account (`@the.faceless.homestead.mama`) getting permanently disabled... TDIE's automation drafts proposed replies for approval; it never auto-posts, except for items Jodie has explicitly approved by name... No fifth trigger may be created that touches Threads, Skool, or Facebook replies." Superseded by the rewrite above — the "never auto-posts" line is no longer accurate and should not be treated as current anywhere it's quoted.

---

This matches `ops/cloud-kit/README_START_HERE.md` (never-rules, prices, links), `canon.json` (every product, price and link above is a `products[]` or `key_pages` row; Premium at $35/month · $297/year), `TDIE_SIX_M_FRAMEWORK.md` (magnet devices, temperature rule, one ask) and the Threads viral research (`ops/cloud-output/threads-research-2026-10/REPORT.md`, Job 13, 27 Sep 2026). Where it differs from The Threads Code, the change log above names the line and the evidence.
