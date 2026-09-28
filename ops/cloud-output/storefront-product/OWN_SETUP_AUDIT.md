# Own-setup audit: Jodie's two Amazon pin automations

Written 27 Sep 2026 in a cloud session. Facts are only the pin-log figures fact-checked on 27 Sep 2026 (supplied with the job) plus the repo copies of the recipes. Nothing here was read live from Pinterest, Amazon or Skool; every account step is in `ops/cloud-output/DESKTOP_FINISH_QUEUE.md` section 4, step 11.

**Two source files are not in the repo:** `claude/TDIE_BRAND_CLOSET_PIN_FACTORY.md` (the line 2 recipe) and `claude/BRAND_CLOSET_PIN_LOG.md` (its log, which holds the hoodie lifestyle pin copy). Fixes to line 2 are therefore written as exact text to add, with where it goes; the desktop finish applies them to the project copy.

Line names used below: **line 1** = the themed-look recipe (`claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`, repo copy `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`), **line 2** = the Brand Closet™ Outfit of the Day recipe.

Scheduled tasks referred to:

| Task | Trigger | Schedule |
|---|---|---|
| Weekly Amazon pin factory (line 1) | trig_01WK6tySP5itdLnFmAiBgnZu | Saturdays 1:05 pm ET |
| Halloween sprint (line 1) | trig_01F6oCmn4yiWQJhKka6KhhN2 | daily 9:00 am, 24 to 30 Sep (cron `0 13 24-30 9 *`, UTC) |
| Nightly Brand Closet OOTD pins (line 2) | trig_017tQcAgu8D9LxjG3MEmNXx3 | Sun to Fri 9:20 pm ET |
| Pinterest pull sweep | trig_015jA7LTzhHTH4cHKA6HuX5r | daily noon and 6 pm ET |

---

## 1 · The secret TK Outfits board

**Problem.** The board TK Outfits is set to Secret. Every line 2 pin scheduled to it reaches nobody: secret boards are not shown in search, the home feed or on the profile. The one verified Brand Closet™ flat lay (the pink color-block hoodie outfit) is scheduled there.

**Fix, on Pinterest (desktop finish, step 11a):**

1. Open the board TK Outfits, click the three dots, Edit board.
2. Rename it to: `Pink Outfit of the Day | Amazon Fashion Finds`
   Why: every other Amazon board is named for the search it wants (`Legally Blonde Outfits | Pink Amazon Fashion`, `Pink Home, Dorm and Car Finds | Amazon`). "TK Outfits" is a name nobody types. Renaming keeps every pin and every scheduled pin on the board; only the board's own web address changes, and no pin links to the board.
3. Description (paste exactly, 334 characters):

   `Pink outfit of the day ideas you can actually order: cozy hoodies, cute sets, easy everyday looks and the shoes, bags and jewelry that finish them. Every outfit is styled head to toe and linked piece by piece in my Amazon storefront Idea Lists. New pink outfits most days. #ad As an Amazon Influencer I earn from qualifying purchases.`

4. Turn **Keep this board secret** OFF. Save.
5. Reload the board page. It must show no lock icon and the new name.
6. Open Pinterest's scheduled pins page in a fresh tab. Find the hoodie flat lay pin. Confirm its board now reads `Pink Outfit of the Day | Amazon Fashion Finds` and the board has no lock icon. Do the same for any other line 2 pin on the scheduled page.
7. Update the log and the Command Centre: in `claude/BRAND_CLOSET_PIN_LOG.md` and in every Command Centre `pins` doc with `source` "brand-closet", replace the board name `TK Outfits` with `Pink Outfit of the Day | Amazon Fashion Finds` (ArtifactData update on each doc, field `board`).

**Recipe lines (exact).**

Line 2 recipe (`claude/TDIE_BRAND_CLOSET_PIN_FACTORY.md`): replace every occurrence of the board name `TK Outfits` with `Pink Outfit of the Day | Amazon Fashion Finds`, and add this as the first bullet of its rules section (section 2):

> - **Public boards only (added 27 Sep 2026).** Before the first pin of every run, open every board this recipe posts to and confirm it is public (no lock icon, "Keep this board secret" off). If any board is secret, schedule nothing, finish the images and log them as built, and tell Jodie in one line: "Board [name] is secret, so I held tonight's pins." The TK Outfits board sat on secret from the first run until 27 Sep 2026 and every pin on it reached nobody.

Line 1 recipe (`TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`), section 1, add after the "Pinterest safety" bullet:

> - **Public boards only (added 27 Sep 2026).** Before the first pin of every run, open both Amazon boards (`Legally Blonde Outfits | Pink Amazon Fashion` and `Pink Home, Dorm and Car Finds | Amazon`) and confirm each is public. If either is secret, schedule nothing, log the finished pins as built, and tell Jodie in one line which board.

**Scheduled-task text (exact).** Add this line to the JOB section of trig_017tQcAgu8D9LxjG3MEmNXx3 and trig_01WK6tySP5itdLnFmAiBgnZu, directly after the browser-lock step:

> Before scheduling anything, open every board this run posts to in a fresh tab and confirm it is public (no lock icon). If one is secret, schedule nothing, log the finished pins as built, and tell Jodie in one line which board.

---

## 2 · The Brand Closet™ backlog

State from the 27 Sep fact-check: one outfit (the pink color-block hoodie) fully built, its flat lay scheduled and verified, its **lifestyle pin finished but unscheduled**. Two outfits (24 Sep and 25 Sep) **partly sourced**. The 25 Sep run stopped when Pinterest went blank.

**Root cause found: the 3-day window drops the backlog.** The nightly run only looks at outfit lessons "from the last 3 days that aren't in the log". From 28 Sep the 24 Sep lesson is outside that window, and from 29 Sep the 25 Sep lesson is too. A partly sourced outfit is never finished: the recipe silently forgets it. Every blank-page stop that lasts more than a day or two loses outfits the same way.

**Recipe lines (exact).** In the line 2 recipe, replace the lesson-selection line (the one that reads "new outfit lessons from the last 3 days that aren't in the log") with:

> - **Which lessons (changed 27 Sep 2026).** Work through outfit lessons from the last 14 days that are not logged as scheduled, oldest first, up to 2 a night. A lesson logged as partly sourced or built is finished first: re-use every piece and link already in the log, source only what's missing, and never start that outfit over. A lesson older than 14 days that is still unfinished is logged "skipped (too old)" and never picked up again.

Add to its scheduling section:

> - **Past-due slots (added 27 Sep 2026).** If the flat lay's normal slot (4:30 pm ET the day after the outfit) has already passed, use the first 4:30 pm ET slot from tomorrow that has no Brand Closet™ flat lay yet. The lifestyle pin goes at 9:30 am ET three days after the flat lay. One Brand Closet™ flat lay and one Brand Closet™ lifestyle pin per day at most. Never more than 14 days ahead.

**The three items now (desktop finish, step 11b).**

1. **Hoodie lifestyle pin.** Its title, description, alt text and Idea List link are in `claude/BRAND_CLOSET_PIN_LOG.md`, hoodie row: use them exactly as logged. Board: `Pink Outfit of the Day | Amazon Fashion Finds` (after section 1). Date: read the hoodie flat lay's posting date from the log (call it F). The lifestyle pin goes at **9:30 am ET on F + 3 days**; if that is today or already past, 9:30 am ET tomorrow; never more than 14 days ahead. AI label on. Verify on the scheduled pins page, write the Command Centre `pins` doc, set the log row to verified.
2. **24 Sep outfit.** Finish sourcing from the log (re-use every piece and link already captured), build the Idea List, the flat lay (Seedream 4.5) and the lifestyle photo (Gemini, seed attached, scene idea only from Rose's prompt with every brand and store cue stripped). Flat lay at 4:30 pm ET on the first day from tomorrow with no Brand Closet™ flat lay; lifestyle at 9:30 am ET three days later.
3. **25 Sep outfit.** Same, one day after the 24 Sep outfit's flat lay (one Brand Closet™ flat lay a day).

The catch-up task in section 4 does all three in the same run as the line 1 stragglers, so nothing waits for Jodie.

---

## 3 · Pinterest blank-page failures (26 and 27 Sep)

**What happened.** Pinterest served blank pages on 26 and 27 Sep, leaving 8 line 1 pins waiting, and stopped the 25 Sep line 2 run. The recipes already stop after two blanks in a row, which is correct: pushing on is how an account gets flagged. The problem is what happens after the stop.

**Three fixes to the browser method (recipe lines, exact).** Line 1 recipe section 1, replace the "Pinterest safety" bullet with:

> - **Pinterest safety (rewritten 27 Sep 2026).** One Pinterest tab at a time, a fresh tab for every pin, closed when that pin is done. Wait 60 seconds between one pin's Publish and the next pin's new tab. Schedule at most 6 pins in a row, then pause 5 minutes. Verify by reading the scheduled pins page's text with JavaScript, not by screenshots. If a page loads blank or the composer freezes, close the tab, wait 60 seconds and open a new one. If Pinterest serves blank pages twice in a row, stop scheduling for this run, keep every finished pin, log it as "built, not scheduled", and end. Never retry a third time in the same run. The next pull sweep picks the leftovers up.

Add the same bullet, word for word, to the line 2 recipe's rules section.

**The leftovers fix (section 5a)** means a stop costs hours, not a week.

**Can the approved Pinterest API app "TDIE- Auto Pin" take over scheduling?**

Short answer: **not yet, and only partly until two things are checked.** Checked 27 Sep 2026 against Pinterest's published access-tier guidance as reported by search (Pinterest's developer site itself is blocked from this cloud session, so each point below is marked):

1. **Trial access cannot post real pins.** Pins and boards created with Trial access are sandbox entities, visible only to their creator. Nobody else sees them. So "TDIE- Auto Pin" on Trial cannot replace the browser today. (Reported by Pinterest's access-tier page in search results; unverified by opening it.)
2. **Standard access can create real pins** on her own boards, with a title, description, link, alt text and image, and can delete pins (which would replace the browser for pulls). Standard also carries higher rate limits. (Reported; unverified.)
3. **Scheduling through the API: unverified.** Third-party guides describe a publish-at time on pin creation (at least 10 minutes and at most 30 days ahead). Pinterest's own reference was not readable from here. If Pinterest's reference confirms it for her app, the API takes over scheduling completely and the blank-page problem disappears for scheduling and pulls. If it doesn't, the API could only publish immediately, which would mean a task running at every slot time on her computer: worse than today. Check before building anything.
4. **The AI label: unverified.** Every Amazon pin carries Pinterest's AI-generated label (recipe rule). If the API cannot set that label, pins made through it would ship without it, and the switch waits until it can. Check this in the same reading.

**Recommendation.** Apply for Standard access now (it takes time), keep the browser method until both checks in points 3 and 4 pass, then switch Part 6 (scheduling) and the pull sweep to the API. Image making, sourcing and Idea Lists stay in the browser either way.

**What the demo video must show** (Pinterest's upgrade guidance, as reported: a recording of the app completing an action with the API; reviewers check the OAuth flow is handled properly and no sensitive information is stored; the OAuth recording is required even when the developer is the only user). Record one continuous screen capture, 2 to 4 minutes, no sound needed, with short on-screen captions:

1. The app "TDIE- Auto Pin" in the Pinterest developer portal: name and app ID visible, the app secret NOT shown.
2. The app starting the OAuth flow: Pinterest's consent screen with the scopes it asks for (boards read, pins read, pins write) and Jodie clicking Allow.
3. The redirect back to the app's redirect address and the app saying it is connected. No access token or secret ever on screen.
4. The app listing her boards (read).
5. The app creating one pin on `Legally Blonde Outfits | Pink Amazon Fashion`: image, title, description ending with `#ad As an Amazon Influencer I earn from qualifying purchases.`, link to one of her Idea Lists, alt text.
6. Opening that pin to show it exists (on Trial it is a sandbox pin visible only to her; say so in a caption).
7. The app deleting that pin (the "pull" feature), then showing it is gone.
8. A closing caption: "Single user (the account owner). Tokens are stored only on the owner's computer and are never shared. No Pinterest user data is stored."

Keep the token in a local file on her computer only, never in the repo, a chat, a project file or the Command Centre.

---

## 4 · Line 1 stragglers

State from the 27 Sep fact-check: 26 pins built. 15 scheduled and verified. **3 scheduled but not yet read back.** **8 waiting** because Pinterest served blank pages on 26 and 27 Sep.

**Fix: one catch-up task (new, one-off).** Create it with `run_once_at` 2:20 pm ET on the day after the desktop finish runs (2:20 pm sits between the 1:30 to 2:15 pm and 4:00 pm busy windows; the browser lock handles any overlap). Exact prompt:

```
PINTEREST CATCH-UP, ONE RUN ONLY (created 27 Sep 2026)
Schedule: run once, 2:20 pm Eastern (America/New_York) on the day after the desktop finish. Needs Jodie's computer on with Chrome signed in to Pinterest and Amazon.

READ FIRST: canon.json; claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md sections 1, 5, 6, 7, 8, 8b; claude/TDIE_BRAND_CLOSET_PIN_FACTORY.md; claude/LB_PIN_LOG.md; claude/BRAND_CLOSET_PIN_LOG.md; claude/TDIE_BROWSER_LOCK.md; claude/CLAUDE_SOURCE_CHECK_RULE.md.

JOB
1. Take the browser lock (claude/TDIE_BROWSER_LOCK.md).
2. Open both Amazon boards and Pink Outfit of the Day | Amazon Fashion Finds in a fresh tab each and confirm each is public. If one is secret, stop and tell Jodie which.
3. The 3 unverified line 1 pins: open Pinterest's scheduled pins page in a fresh tab. For each pin in claude/LB_PIN_LOG.md marked scheduled but not verified, find it by title and time by reading the page text. Found: mark it verified in the log and write its Command Centre pins doc (section 8b). Not found: treat it as not scheduled and add it to step 4.
4. The 8 waiting line 1 pins (and any from step 3): schedule each one, in log order, into the first free line 1 slot from tomorrow: 12:30, 13:30, 15:30, 18:30, 19:30, 20:30, 21:30 Eastern. Rules: a look's lifestyle pin at least 3 days after its flat lay; never two Legally Blonde pins within an hour; never 08:00, 09:30, 11:00, 14:00, 16:30, 17:00 or 20:00 (TDIE factory and Brand Closet slots); nothing past 23 Oct for a Halloween look (the Halloween window ends a week before Halloween), and nothing more than 14 days ahead. Wait 60 seconds between pins and pause 5 minutes after every 6.
5. The Brand Closet backlog, OWN_SETUP_AUDIT.md section 2 (in the repo at ops/cloud-output/storefront-product/): schedule the hoodie lifestyle pin from its logged copy, then finish, build and schedule the 24 Sep and 25 Sep outfits following the line 2 recipe, with the 14-day lesson window and the past-due slot rule.
6. Verify every pin from steps 3 to 5 on the scheduled pins page by reading its text. Write each Command Centre pins doc only after it is verified. Update both logs in full.
7. Release the browser lock.
If Pinterest serves two blank pages in a row: stop, log what's left as built, release the lock, and report the count left. The pull sweep picks them up.

REPORT: one line if everything passed, for example "11 line 1 pins and 5 Brand Closet pins scheduled and verified." Otherwise one line saying exactly what is left and why.

BROWSER FALLBACK RULE (standing instruction from Jodie, added 27 Sep 2026; overrides any earlier line in this prompt that says to stop the moment a browser, tab or sign-in problem appears):
If a tab freezes, a site isn't signed in, a control stops responding, or the browser otherwise won't cooperate, do not stop or report yet.
1. Try every other route first: switch browsers (her Chrome via Claude in Chrome <-> the built-in browser in the Claude desktop app, in either direction, whichever this prompt named first), open a fresh tab, and check whether the other browser is already signed in to the site. Never type a password.
2. If every route is exhausted, try all likely fixes and resets: reload the page, close and reopen the tab, wait 30 to 60 seconds and retry, clear the stuck state (close any open composer or modal, discard only drafts this run created), and reconnect or re-select the browser.
3. Only then give Jodie a fail notice through SendUserMessage: what failed, what you tried, and her exact numbered next steps (for example: open Chrome, sign in to X, then re-run this task). Keep the browser lock and reporting rules above.
```

---

## 5 · Hand-work to remove

**5a. Re-running after a blank-page stop.** Today, pins left over by a blank-page stop wait for the next weekly run (up to 6 days) unless Jodie steps in. Fix: the pull sweep picks up leftovers. Add this block to trig_015jA7LTzhHTH4cHKA6HuX5r's prompt, directly after its pull step (exact):

> LEFTOVERS (added 27 Sep 2026). After the pulls, read claude/LB_PIN_LOG.md and claude/BRAND_CLOSET_PIN_LOG.md without opening a browser. If any pin is logged "built, not scheduled", take the browser lock if you do not already hold it, confirm the board is public, and schedule up to 4 of them into the next free slots for their line (line 1: 12:30, 13:30, 15:30, 18:30, 19:30, 20:30, 21:30; Brand Closet: 16:30 flat lays, 09:30 lifestyle), keeping the 3-day rule, the one-hour gap between Amazon pins, and the 14-day limit. Wait 60 seconds between pins. Verify each on the scheduled pins page by reading its text, write its Command Centre pins doc, update the log. If Pinterest serves two blank pages in a row, stop and leave the rest for the next sweep. If there are no leftovers and no pulls, open no browser.

Add this line to both recipes' log section (line 1 section 8, line 2 its log section):

> Leftovers (27 Sep 2026): any pin logged "built, not scheduled" is picked up by the next pull sweep (noon or 6 pm ET), up to 4 per sweep, before the next build run.

**5b. Instagram stories for @itstommykate.** Stories cannot be posted from Instagram's website, so every queued story stays "queued" and waits for Jodie's phone, and Business Suite can't schedule for the account until the Facebook Page admin access is restored. Fix: stop making stories until @itstommykate is connected to a Page in Business Suite. Line 1 recipe section 8d, replace the "Per look" bullet with (exact):

> - Per look: a FEED post (the lifestyle photo first, then the flat lay or collage as a second carousel image, caption naming the pieces). STORIES PAUSED (27 Sep 2026): no story images are made or queued until @itstommykate is connected to a Facebook Page in Meta Business Suite; then Business Suite schedules a story per look with a link sticker to the Idea List, sticker text "shop this look".

Nothing else in either line needs her hands on a normal day. The Pull button stays: it is an optional glance, not a job.

---

## 6 · Waste

**6a. The Halloween sprint trigger fires again next year.** trig_01F6oCmn4yiWQJhKka6KhhN2 runs on cron `0 13 24-30 9 *`, which has no year: it fires again on 24 Sep 2027 and builds a sprint nobody asked for. Fix: after its last run on 30 Sep 2026, delete trig_01F6oCmn4yiWQJhKka6KhhN2 (desktop finish, step 11f). In the line 1 recipe section 11, replace the sprint bullet with:

> - **Legally Blonde Halloween sprint:** ran daily 9:00 am ET, 24 to 30 September 2026. Trigger deleted after its last run, because its cron has no year and would fire again in September 2027.

**6b. Seedream at 4K for a 1000 by 1500 pin.** Every flat lay is generated at 4K and then captured and saved at 1000 by 1500, so most of the pixels are thrown away, and 4K renders take longer. Line 1 recipe section 4, replace "**Seedream 4.5 on Higgsfield, Unlimited toggle ON, 4K, portrait 2:3**" with:

> **Seedream 4.5 on Higgsfield, Unlimited toggle ON, 2K, portrait 2:3** (changed from 4K on 27 Sep 2026: the pin is saved at 1000 by 1500, so 4K detail was discarded)

Same change in the line 2 recipe wherever it says 4K.

**6c. Queued Instagram stories.** Each queued story is a 1080 by 1920 image encoded into the Command Centre database that nobody can post from the web. Removed by 5b.

**6d. Nightly line 2 run with nothing new.** Add to trig_017tQcAgu8D9LxjG3MEmNXx3's prompt, directly after the browser-lock step (exact):

> Check The Brand Closet™ Outfit of the Day Closet course first, in one tab. If there is no lesson from the last 14 days that isn't logged as scheduled, and claude/BRAND_CLOSET_PIN_LOG.md has no pin logged "built, not scheduled", close the tab, release the browser lock, and end with the one line "No new outfits tonight." Do not open Amazon, Higgsfield, Gemini or Pinterest.

**6e. Screenshots for verification.** Verifying scheduled pins by screenshot costs time and usage; reading the scheduled pins page's text with JavaScript gives the same answer (title, time, board). Covered by the rewritten "Pinterest safety" bullet in section 3.

**6f. Also found while testing the buyer kit (a risk, not waste): background fetches of Amazon.** Line 1 section 3c reads Amazon search results with `fetch('/s?k=...')` from a signed-in amazon.com tab. Amazon's Conditions of Use prohibit robots and data extraction, and this runs inside the account her Associates income sits on. It is faster, but a flagged account costs far more than the minutes saved. Line 1 recipe section 3c, replace the "Amazon search without clicking" bullet with:

> - **Amazon search (changed 27 Sep 2026):** open each search in the tab and read the loaded results page with JavaScript (skip "Sponsored"; read `data-asin`, the h2 text, `.a-icon-alt` for stars, the aria-label ending in "ratings"). Colour variants: open the product page and read `"dimensionValuesDisplayData"`. Never `fetch()` Amazon pages in the background.

Same change in the line 2 recipe if it uses the same method. The buyer kit already works this way (rule R18).

Kept on purpose, not waste: the two-correction cap, the product sheet (one screenshot per look), the tile-and-stitch capture (it is what keeps downloads off Jodie's computer), the Command Centre thumbnails (they are the Pull button's preview), and the twice-daily pull sweep (it opens no browser when there is nothing to do).

---

## What this audit does not change

No settled canon decision. The destination rule (pins link to Idea Lists, never the domain), the disclosure, the generated title overlays (Decision 109), the 3-day spacing, the 14-day scheduling limit, the posting slots, the 31 Mar 2027 renewal, and the Pull button all stay exactly as they are.


## CONTINUATION AUDIT 2026-09-28

This continuation re-read the optimized customer kit and verified the largest launch risks against current official platform rules.

### Changes made
- Replaced autonomous Amazon browsing/SiteStripe/Idea List operations with PRODUCT_SOURCES.md customer intake.
- Removed marketplace screenshots/product sheets from the required AI-input workflow.
- Disabled Brand Closet™ automation pending explicit commercial-use permission.
- Removed the separate missed-run task and folded recovery into the weekly task.
- Made customer image-provider/model selection explicit.
- Added stable IDs and rights state to the persistent workflow.
- Rewrote the obsolete Amazon email-link blanket ban.
- Updated blog-half link handling.

### Current launch status
The customer text kit is architecturally corrected, but the Setup Guide PDF and its renderer are still stale and must be regenerated before the downloadable product is considered internally consistent.
