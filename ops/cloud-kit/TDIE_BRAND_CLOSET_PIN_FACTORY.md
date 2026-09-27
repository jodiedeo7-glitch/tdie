# BRAND CLOSET OOTD PIN FACTORY

> **🖼️ IMAGE RULES (Jodie, 25 September 2026). Read before any image prompt or generation.** Every image prompt and every generated image follows `claude/TDIE_IMAGE_GENERATION_MASTER.md`, which wins over anything older in this document. Canon beats generic words like "luxury" or "editorial": Tommy Kate is photographed in her own world (farmhouse, pink attic gaming loft, porch, kitchen, living room, pasture, red barn, garden beds, golden retriever), never a Paris apartment, café, marble office, mansion or influencer set. Every prompt with her in it opens: "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Her locked features are never written in words, not even as "same face" or "same freckles". Her glitter-flecked pink iced coffee tumbler is in every photo of Tommy Kate, and it is never the only pink item: her clothes can be candy pink and other pink pieces can be in the frame with her (Jodie, 26 Sep 2026). Frames without her carry exactly one intentional saturated candy-pink object. (Product flat lays and collages with no person follow LB recipe section 4, per Jodie's example pins, 26 Sep 2026). Real lens and real light language, photorealism language, no text or logos in the photo. **Tool order (standing rule):** any image with the avatar or a person goes to Google Gemini first, reference sheet attached, while Gemini has credits, then Nano Banana Pro at 2K on Higgsfield, reference sheet attached. Any image with no person goes to Seedream 4.5 on Higgsfield. Garbled text or an unsatisfactory image re-runs on Nano Banana Pro at 2K on Higgsfield. No other image generator, and never Canva.

> **🔒 BROWSER LOCK AND NO DOWNLOADS (Jodie, 26 September 2026).** Every run follows `claude/TDIE_BROWSER_LOCK.md`: take the Command Centre browser lock before opening Chrome, wait and retry if another task holds it, release it at the end even after a failure. Nothing is saved to Jodie's computer: no Downloads\BC-pins folders. Rose's flat lay is captured as a screenshot into the cloud workspace, and images move by the capture method in LB recipe section 3c.

### Current, 27 September 2026. Single live copy. The recipe behind the nightly "Brand Closet OOTD pins" scheduled task.

**What this is:** every day Rose Berry posts an Outfit of the Day in The Brand Closet™ Skool group (Jodie is a paying member). Each night, after Rose has posted, this task turns that day's outfit into two of Jodie's own Amazon affiliate pins: one flat lay and one lifestyle photo of Tommy Kate wearing the outfit. It runs alongside the Legally Blonde line and uses the same machinery (`claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`, including its section 3c fast path), so everything in that recipe applies unless this file says otherwise.

**Founder instruction, 24 Sep 2026:** go to the Brand Closet every night, when no other automation is running, find the daily outfit, make a flat lay and a lifestyle image for Pinterest, and schedule both. Never post the two pins of the same outfit on the same day; separate them by a few days to widen reach.

---

## 1. WHERE THE OUTFIT LIVES (checked live 24 Sep 2026)

- Group: `https://www.skool.com/the-brand-closet`. Classroom course **"Outfit of the Day Closet"** (`/classroom/272075b5`), with month folders ("➤ SEPTEMBER") holding one lesson per outfit. Lessons are titled by date ("September 24") or by a name ("Downtown After Dark"). Some days have more than one lesson.
- Each lesson holds: the outfit flat lay image, one or two ready-made lifestyle prompts written for "the woman in image 1 wearing the outfit in image 2", and a **"Link to Outfit"** button.
- "Link to Outfit" goes to a Benable list owned by someone else (`benable.com/breckettemariexo/<month>-trending-outfits-you-must-have`), split into dated sections ("September 10- Dressed Down"). Those are Amazon products, but the links pay THEIR owner, not Jodie.
- The community post in the OOTD category (by rose-berry-3526) announces it each morning. Rose usually posts between 7:30 am and 3 pm ET, weekdays.
- Find new lessons by reading `__NEXT_DATA__` on the course page (walk `pageProps.course` children; each lesson has `metadata.title`, `id`, `updatedAt`). Open a lesson with `?md=<lesson id>` and read it with get_page_text.

## 2. RULES THAT NEVER MOVE

- **Public boards only (added 27 Sep 2026).** Before the first pin of every run, open every board this recipe posts to and confirm it is public (no lock icon, "Keep this board secret" off). If any board is secret, schedule nothing, finish the images and log them as built, and tell Jodie in one line: "Board [name] is secret, so I held tonight's pins." The TK Outfits board sat on secret from the first run until 27 Sep 2026 and every pin on it reached nobody.
- **The pin link is Jodie's own Amazon Idea List, built from her storefront editor with her tag (`jodiedeo0c-20`).** Never the Benable link, never Rose's links, never the Brand Closet URL. We re-find each item on Amazon and build Jodie's own list.
- **Rose's images are references only.** Her flat lay photo and her prompts are paid member content: never post them, never upload them anywhere public. Every pin image is newly generated. Capture her flat lay as a screenshot into the cloud workspace (it stays there); never save it to Jodie's computer.
- Every Legally Blonde rule applies: disclosure line in every description, copy limits, no prices, no em dashes, IP out of every image (strip brand cues from Rose's prompts: no LV monogram, no Target, no red carts, no logos), persona lock (never describe Tommy Kate's locked features, never write "blonde" in an image prompt), realism method (section 3b of the LB recipe), fresh Pinterest tab per pin, never hammer Pinterest.
- **Pinterest safety (rewritten 27 Sep 2026).** One Pinterest tab at a time, a fresh tab for every pin, closed when that pin is done. Wait 60 seconds between one pin's Publish and the next pin's new tab. Schedule at most 6 pins in a row, then pause 5 minutes. Verify by reading the scheduled pins page's text with JavaScript, not by screenshots. If a page loads blank or the composer freezes, close the tab, wait 60 seconds and open a new one. If Pinterest serves blank pages twice in a row, stop scheduling for this run, keep every finished pin, log it as "built, not scheduled", and end. Never retry a third time in the same run. The next pull sweep picks the leftovers up.
- **Amazon search (changed 27 Sep 2026):** open each search in the tab and read the loaded results page with JavaScript, as LB recipe section 3c now says. Never `fetch()` Amazon pages in the background.
- Nothing is posted to Skool, Facebook, Threads or Instagram by this task. It reads the Brand Closet and closes that tab within the first few minutes.

## 3. SPACING (founder rule, 24 Sep 2026, applies to all of Jodie's Pinterest pins)

- The flat lay and the lifestyle pin of the same outfit never post on the same day.
- Flat lay: **16:30 ET, the day after the outfit's Skool date.** Lifestyle: **09:30 ET, three days after the flat lay.**
- If a slot is already taken (two outfits in one day, or a catch-up night), move to the same slot on the next free day. Keep the two pins of one outfit at least 3 days apart, and never schedule more than 14 days ahead.
- **Past-due slots (added 27 Sep 2026).** If the flat lay's normal slot (4:30 pm ET the day after the outfit) has already passed, use the first 4:30 pm ET slot from tomorrow that has no Brand Closet™ flat lay yet. The lifestyle pin goes at 9:30 am ET three days after the flat lay. One Brand Closet™ flat lay and one Brand Closet™ lifestyle pin per day at most. Never more than 14 days ahead.
- These half-hour slots stay clear of the TDIE factory (08:00, 11:00, 14:00, 17:00, 20:00) and the Legally Blonde line (12:30, 13:30, 15:30, 18:30, 20:30, 21:30, 22:00, 22:30).

## 4. BOARD

- `Pink Outfit of the Day | Amazon Fashion Finds` (renamed from `TK Outfits` on 27 Sep 2026 and made public, with a real description). It is the same board: every pin and scheduled pin on it moved with the rename. If the rename has not happened yet, use `TK Outfits` only once it is public, and name it in the report. Never create a board without a real description.

## 5. IMAGES

- **Flat lay (no person):** follow LB recipe section 4 exactly (rewritten 26 Sep 2026 from Jodie's example pins: full, abundant, styled, textured or coloured background, big two-typeface title set on the image; plain white layouts with a small title are out). Seedream 4.5 on Higgsfield, Unlimited ON, 2K, 2:3 (changed from 4K on 27 Sep 2026: the pin is saved at 1000 by 1500, so 4K detail was discarded). Attach a style reference from the Command Centre `stylerefs` collection, the product sheet (LB recipe section 3c), and Rose's flat lay screenshot as the item reference. The title lockup names the look in 3 to 5 words (for example "FALL ERRANDS / outfit formula"). Alternate the styled flat lay and the "that girl" collage night to night.
- **Lifestyle (Tommy Kate):** Gemini first, one chat per outfit, attachments in order: style reference (a lifestyle photo from the repo, LB recipe section 3b.2), Omni seed (JPEG under 400 KB), product sheet, Rose's flat lay screenshot. Start from Rose's lifestyle prompt for the scene idea, then rewrite it into the LB recipe section 5 template: identity line first, every item named, face hidden or not the focus in most shots (mirror selfie with the phone covering her face, chin-down crop, over-the-shoulder walk-away, or detail shot), her own world, phone-photo realism, no text, no logos, no store names. Nano Banana Pro 2K on Higgsfield once Gemini's free images run out.
- QA both at feed size. Fix the lifestyle photo in the same Gemini chat (or on Nano Banana Pro 2K); fix the flat lay on Higgsfield (Seedream 4.5 re-run, or Nano Banana Pro 2K), never in Gemini. Two correction rounds at most per image; grain, small crops and tiny stray marks are fixed by hand in the cloud workspace.

## 6. LOG AND COMMAND CENTRE

- Log: `claude/BRAND_CLOSET_PIN_LOG.md`. One row per outfit: Skool lesson title and id, look name, items (name, ASIN, Jodie's SiteStripe link), Idea List URL, flat lay title and date/time, lifestyle title and date/time, verified yes/no. Every run reads it first (never repeat a lesson) and writes it back in full last.
- Leftovers (27 Sep 2026): any pin logged "built, not scheduled" is picked up by the next pull sweep (noon or 6 pm ET), up to 4 per sweep, before the next build run.
- Command Centre Pinterest tab: after each pin is verified on Pinterest's scheduled page, write one doc into collection `pins` of `claude.ai/artifact/7sggSqfNcfRDscpy3fsg4C` exactly as LB recipe section 8b says, with doc id `YYYY-MM-DD-HHMM-bc-N` and `source: "brand-closet"`.

## 7. THE SCHEDULED TASK

- **Nightly Brand Closet OOTD pins:** Sunday to Friday nights at 9:20 pm ET (trig_017tQcAgu8D9LxjG3MEmNXx3). Chosen because it is after Rose has posted and clear of every other automation: the 9 pm hot-thread check exits in a minute, the 10:30 pm Skool sweep starts after this run has left Skool, and the 11:30 pm Threads load follows it. Saturday night is skipped because the weekly Daily Prompts build runs then; Saturday outfits (rare) are caught up on Sunday night. It takes the browser lock first (`claude/TDIE_BROWSER_LOCK.md`).
- **Which lessons (changed 27 Sep 2026).** Work through outfit lessons from the last 14 days that are not logged as scheduled, oldest first, up to 2 a night. A lesson logged as partly sourced or built is finished first: re-use every piece and link already in the log, source only what's missing, and never start that outfit over. A lesson older than 14 days that is still unfinished is logged "skipped (too old)" and never picked up again. Stop starting new outfits at 11:10 pm so the run is out before the Threads load.
- **Nothing new, no browser work (added 27 Sep 2026).** Check the Outfit of the Day Closet course first, in one tab. If there is no lesson from the last 14 days that isn't logged as scheduled, and the log has no pin logged "built, not scheduled", close the tab, release the browser lock, and end with the one line "No new outfits tonight." Do not open Amazon, Higgsfield, Gemini or Pinterest.
- The "Daily missed-run sweep" re-fires it the next morning if her computer was off; the lock stops that re-run from colliding with the morning tasks.

**The Digital Income Edit, Brand Closet OOTD Pin Factory, 27 September 2026**
