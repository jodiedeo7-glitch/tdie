# REEL RULE OVERRIDE (Jodie, 14-15 Nov 2026). THIS BLOCK WINS OVER EVERY LINE BELOW.

The Reel job is: find viral Reels and COPY THEM for TDIE / Tommy Kate. Not adapt. Not "inspired by". Not new original copy.

1. SOURCE QUALIFICATION (both numbers, read from the post itself, never estimated): the source is an Instagram Reel with at least 10,000 views AND at least 10x the posting account's follower count. A Reel failing either number is NOT a source and is never called viral. "5X median", "high-performer", "engagement" and "usable with change" do not qualify a source.
2. NICHE: digital income, online business, faceless, creator, UGC, affiliate, digital products only. NEVER farm, homestead, craft, pet/animal, baking, travel, art, celebrity or brand accounts. NEVER TikTok.
3. COPY MEANS: recreate the source Reel itself. Same shot sequence, same pacing, same on-screen words, the original's own text look (font, box, size, placement), same caption structure, same CTA mechanism, same kind of audio. Tommy Kate or the TDIE persona takes the place of the person. Change ONLY the person, TDIE offer words, and any earnings or income promise. Never swap in unrelated stock or AI footage. Never use your own layout or one blanket text style.
4. PER-REEL RECORD before anything is built or scheduled: source link, views, followers, ratio, in-niche yes/no, then a side-by-side of the source and the finished Reel, ending in one line: "TRUE COPY" or "NOT A COPY: <what differs>". Only TRUE COPY may be scheduled.
5. Any line below that says adapt, adaptation, inspired, original wording, do not copy, preserve the mechanism, 5X, high-performer, supporting pattern, or usable with change is VOID for Reels.
6. Full rule file: TDIE_REEL_COPY_RULES.md in the Drive folder "TDIE Task Files".

---

# TDIE Premium DFY Content Calendar Router

> **MIDJOURNEY, STANDING RULE (Jodie, 3 October 2026).** Jodie has an active Midjourney subscription, signed in in her browser, with far more free generations than Higgsfield. Whenever an image would come out better in Midjourney, use Midjourney, with or without a person. This amends every tool-order line in this file that says no other image generator is used. Canva is still never an image generator. Full rule: section M of claude/TDIE_IMAGE_GENERATION_MASTER.md.


## Scope
This router governs ONLY the Membership Premium DFY Content Calendar ("the calendar").

It does NOT govern:
- Daily Prompts / Daily Edits
- DFY Viral Instagram Content Calendar client service
- Threads calendar
- Pinterest calendar

Those systems remain separate.

## World (Jodie, 2 October 2026, Decision 124)
Every calendar image and video prompt follows `ops/cloud-kit/TDIE_DFY_CALENDAR_TOMMY_KATE_WORLD.md`: Tommy Kate's real life, every named object repeated, including the Hello Kitty and Kuromi plushies in her loft. The Daily Edits look (`ops/cloud-kit/TDIE_DAILY_EDITS_UNIVERSAL_LOOK.md`) is never used here. Side-by-side: `ops/cloud-kit/TDIE_DFY_CALENDAR_VS_DAILY_EDITS.md`.

## Canon
Follow `ops/canon/canon.json` → `content_calendar_rules` and Decisions 80, 111, 115, 117 in `ops/canon/TDIE_CANON.md`.

## Required sequence

### Stage 1 — Research — CHATGPT
1. Collect >=75 qualifying examples using the authoritative evidence classes.
2. Source >=40 same-niche, similar-creator, normally-not-viral accounts.
3. Exclude celebrities, huge accounts, and brands.
4. Record why each post qualifies as an outlier.
5. Count recurring patterns.
6. Build a replication plan in TDIE's own voice.
7. Name any standing rule the evidence overrides and cite the proof in the research file.


### Posting-time evidence
Posting-time research is mandatory for every monthly Premium calendar research cycle.
- For every qualifying Instagram Reel where the source exposes it, capture the exact publish timestamp, source timezone, normalized America/New_York time, and day of week.
- If exact time or timezone cannot be verified, write `NOT VERIFIED`; never infer a clock time from the displayed date.
- Compare VERIFIED OUTLIER / VIRAL ANALYTICS EXAMPLE timing against the creator's own normal posting distribution where the source supports it. Keep HIGH-PERFORMER timing separate when no account-relative baseline exists.
- Produce a monthly timing analysis with sample sizes, day-of-week counts, time-window counts, and any creator-relative differences. Correlation is not causation.
- The monthly build rules must include a recommended Instagram posting window only when supported by the current research. If evidence is insufficient, label the research-derived window `UNVERIFIED` and use the member/account's own Instagram audience-activity data when available rather than inventing a universal best time.
- Every finished Instagram calendar day must include a recommended posting time or window and the evidence basis used for it.

OUTPUT:
- `PREMIUM_CALENDAR_RESEARCH_<YYYY-MM>.md
- `PREMIUM_CALENDAR_BUILD_RULES_<YYYY-MM>.md`

### Stage 2 — Calendar architecture — CHATGPT
Build the month around the evidence.

Required canon:
- Two-week rollout.
- Research begins at the start of the final week of the preceding month.
- Release one week every 3–4 days across the final week of the preceding month and first week of the covered month.
- Never promise the whole month before the 1st.
- (Decision 132, 13 Nov 2026) All promotion limits are retired: no cap on selling posts per day, no back-to-back rule, no offer-repeat or affiliate-spacing rule, no 14-day no-repeat window. Schedule offers from claude/TDIE_PROMOTION_MASTER_PLAN.md. Meta link rules still apply.
- Instagram: no links anywhere; CTA points to link in bio. Story link stickers excepted.
- Facebook: link goes in first comment 5 minutes after publishing.
- Model-agnostic member production and two-path Reel QA per current production rules.

OUTPUT:
- `PREMIUM_CALENDAR_PLAN_<YYYY-MM>.md`

### Stage 3 — Copy + creative — CHATGPT
Create the finished weekly content packet.

For each post include:
- date
- platform
- format
- objective
- hook
- final caption/body
- CTA
- offer slot, if any
- first-comment copy for Facebook, if needed
- visual concept
- image/video generation prompt when required
- asset filename
- status

ChatGPT also performs:
- voice QA
- repetition QA
- selling-spread QA
- link-rule QA
- research-rule QA

OUTPUT:
- `PREMIUM_CALENDAR_WEEK_<N>_<YYYY-MM>.md`
- assets/graphics as applicable
- `PREMIUM_CALENDAR_EXECUTION_MANIFEST_<YYYY-MM>.csv`

### Stage 4 — Specialized visual generation — IMAGE TOOL / HIGGSFIELD / GEMINI
Only when the approved creative requires generated photography/video.

Do NOT redesign the calendar.
Do NOT rewrite copy.
Do NOT invent new offers.
Return only the requested finished asset.

### Stage 5 — Platform execution — CLAUDE
Claude receives only approved weekly packets and finished assets.

Claude may:
- upload
- schedule
- set first comments where supported
- verify links / link-in-bio CTA compliance
- read back scheduled items
- report platform failures

Claude may NOT:
- rewrite strategy because the browser is open
- replace research-backed hooks with generic ones
- merge Daily Prompts into the calendar
- change offer rotation
- invent new content to fill gaps without routing back to ChatGPT

OUTPUT:
- `PREMIUM_CALENDAR_EXECUTION_LOG_<YYYY-MM>.md`

### Stage 6 — Verification — CHATGPT + CLAUDE
Claude verifies live platform state.
ChatGPT verifies the completed log against the approved manifest and canon.

A week is COMPLETE only when:
- all scheduled content exists
- dates/times match
- correct asset attached
- correct copy loaded
- Meta link rules satisfied
- selling spread satisfied
- failures/retries documented

## Hard separation rule
The Daily Prompts / Daily Edits system is NEVER a source, queue, fallback, content bank, or naming alias for this calendar.

## Current repository production rules govern
Read ops/cloud-kit/TDIE_DFY_CALENDAR_PRODUCTION_RULES.md before this packet. The authoritative 29 September 2026 rules supersede the older 40-post/25-account threshold and personal vendor pipeline here. Require at least 75 qualifying examples, 40 unique accounts, 30 tightly adjacent accounts and 20 verified account-relative outliers or credible analytics/benchmark examples. Preserve evidence classes and unknown-field boundaries. Research must pass its stop gate before calendar writing. Premium October acceptance is 31 Instagram days and 62 member Threads, distinct from founder Threads at six/day. Member prompts are model agnostic and beginner usable: optional persona, standalone static prompts, each Reel one concept with Version A containing exact timed overlay text and Version B text-free with a separate editable overlay block. No mandatory Gemini, Nano Banana or Higgsfield sequence; no private seed dependency. Long Reels require research-supported sustained explanation and compatible talking-head production, never padded cinematic footage. All spread, link, claims, per-day and per-prompt QA in the authoritative file apply. These changes apply only to the Premium member calendar, not Daily Prompts or paid client work.
