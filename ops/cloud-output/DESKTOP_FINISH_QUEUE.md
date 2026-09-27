# DESKTOP FINISH QUEUE

Account-only steps left by cloud sessions. Each job adds one numbered section with every file path, piece of copy and exact step written in. The DESKTOP FINISH prompt in `ops/cloud-kit/CLOUD_CREDIT_JOBS.md` works through this file on Jodie's computer and marks each section DONE with the date.

## 1 · One-Sentence Offer tool: link from The Offer Edit's opening lesson (26 Sep 2026)

Cloud session could not reach Skool (network policy blocks skool.com; no signed-in browser). Canon Decision 120.

1. Open https://www.skool.com/thedigitalincomeedit/classroom/c47c7df7 signed in as Jodie. Open the first lesson of The Offer Edit.
2. Edit the lesson. At the very end of the body, add this one line as its own paragraph:

   Want to test your sentence before you build the rest? Run it through the free One-Sentence Offer tool. Two minutes, no email.

3. Select the words **the free One-Sentence Offer tool** and hyperlink them to `https://www.thedigitalincomeedit.com/resources/one-sentence-offer`. No raw URL in the text.
4. Save. Reload the lesson and read the line back from the page: the wording matches step 2 exactly and the link opens the tool.
5. Mark this section DONE with the date.

## 2 · The Weekend Ecosystem™ Beacons description (revised 26 Sep 2026)

Jodie is pasting the revised description herself (sent in chat 26 Sep 2026). Remaining step only: on Mon 5 Oct 2026, after the Keep It Running Kit ends (4 Oct, 11:59 pm Eastern), replace the description with the "after 4 Oct" version saved in `ops/cloud-output/WE_BEACONS_DESCRIPTION.md`, then read it back from the public checkout page.

## 3 · The Weekend Ecosystem™ cover, carousel, OG and Meta ads (Job 10, 27 Sep 2026)

All files are in `ops/cloud-output/we-creatives/` (see its `README.md`, `AD_COPY.md`, `PHOTO_PROMPTS.md`, `CONTACT_SHEET.jpg`). The cloud session could not use Gemini, Higgsfield, Beacons or Meta.

1. **Generate the one placeholder photo.** Open Google Gemini, attach `public/images/library/avatar-seed-omni-reference.png`, paste the full prompt under "pay-plan-pasture-blanket.jpg" in `ops/cloud-output/we-creatives/PHOTO_PROMPTS.md`. If Gemini has no credits or the face drifts, use Nano Banana Pro at 2K on Higgsfield with the same reference. Check: her glitter pink tumbler with lavender straw is in frame, no text in the image, she sits in the right third. Save it as `ops/cloud-output/we-creatives/photos/pay-plan-pasture-blanket.jpg`. From the repo root run `node ops/cloud-output/we-creatives/render.mjs ad-payplan`, open the four `png/ad-payplan-*.png` files and confirm the placeholder box is gone, then commit and push.
2. **Beacons carousel.** Open the Beacons product for The Weekend Ecosystem™ (checkout `https://links.thedigitalincomeedit.com/shop/f7b54195-6a0e-4e95-8b92-fc203770176c`) in the Beacons editor. Replace the product images with, in this order:
   1. `ops/cloud-output/we-creatives/png/beacons-hero-keep-it-running-kit.png` (while the Kit runs, until Sun 4 Oct 2026, 11:59 pm Eastern)
   2. `ops/cloud-output/we-creatives/png/beacons-2-what-you-get.png`
   3. `ops/cloud-output/we-creatives/png/beacons-3-review.png`
   Save. Open the public checkout page and read the carousel back: three images, in that order.
3. **On Mon 5 Oct 2026** (after the Kit ends), swap image 1 for `ops/cloud-output/we-creatives/png/beacons-1-hero.png`. Read it back from the public page. (Same day as section 2's description swap.)
4. **Facebook Sharing Debugger.** Go to https://developers.facebook.com/tools/debug/, enter `https://www.thedigitalincomeedit.com/shop/weekend-ecosystem`, click **Scrape Again**. Confirm the preview image is the new one (`/og/weekend-ecosystem-2026-09.jpg`: porch photo left, loft photo right, "A business that keeps selling on the Tuesday you're too tired to post." in the centre card).
5. **Meta Ads Manager: only with Jodie's go.** Ask Jodie first. When she says go: five ads, one per angle in `AD_COPY.md` (ideal, preview, build, payplan once step 1 is done, review). Each ad: upload its four `png/ad-[angle]-*.png` sizes as placement assets (1080 × 1080 and 1080 × 1350 for feeds, 1080 × 1920 for Stories and Reels, 1200 × 628 for right column), paste Primary text, Headline and Description from `AD_COPY.md` exactly, CTA button **Learn More**, website URL `https://www.thedigitalincomeedit.com/weekend-ecosystem/preview`. No link in any caption. Budget, audience and schedule are Jodie's call. Leave the ads paused until she approves the preview.
6. Mark this section DONE with the date.

## 4 · Threads viral research, rebuilt system and October 2026 month (Job 13, 27 Sep 2026)

All files are in `ops/cloud-output/threads-research-2026-10/`: `REPORT.md`, `EVIDENCE.md`, `ACCOUNTS.csv` (the research), `TDIE_THREADS_SYSTEM_v-rebuilt.md` (change log at the top), `TDIE_JODIE_THREADS_VOICE_v-rebuilt.md` (one section added, change log at the top), and the five week files `threads-week-2026-09-28.md` (Thu 1 to Sun 4 Oct), `threads-week-2026-10-05.md`, `threads-week-2026-10-12.md`, `threads-week-2026-10-19.md`, `threads-week-2026-10-26.md` (Mon 26 to Sat 31 Oct). The cloud session could not open the claude.ai Project, Threads or the scheduled tasks.

**Do nothing below until Jodie has approved the rebuilt system, the voice addition and the week files. If she approves the system but not the bio, skip step 4.**

1. **Copy the rebuilt system into the Project as the live copy.** Open the Project doc `claude/TDIE_THREADS_SYSTEM.md`. Replace its body with the full contents of `ops/cloud-output/threads-research-2026-10/TDIE_THREADS_SYSTEM_v-rebuilt.md`, keeping the Project doc's dated change-history notes at the top and its automation task table (Section 11) below, and adding one dated line to the change history: "27 Sep 2026: rebuilt from the Threads viral research (Job 13); 6 posts a day, 1 PM offer, daily reply block; see the change log." Update `ops/cloud-kit/TDIE_THREADS_SYSTEM.md` in the repo to the same text and push.
2. **Copy the voice addition.** Open `claude/TDIE_JODIE_THREADS_VOICE.md` in the Project. Insert the section "THE ORIGIN LINE AND REAL SMALL NUMBERS" from `TDIE_JODIE_THREADS_VOICE_v-rebuilt.md` after "HOW SHE ACTUALLY TALKS", with the dated note. Update `ops/cloud-kit/TDIE_JODIE_THREADS_VOICE.md` to match and push.
3. **Copy the five week files into the Project** as `claude/threads-week-2026-09-28.md`, `claude/threads-week-2026-10-05.md`, `claude/threads-week-2026-10-12.md`, `claude/threads-week-2026-10-19.md`, `claude/threads-week-2026-10-26.md`, contents exactly as in the repo (including the `CHARS:` lines, which the loader ignores). On Thu 1, Sat 3 and Sun 4 Oct, if `claude/TDIE_ECOSYSTEM_KIT_SOCIAL.md` Part 2 has approved Kit text, paste it over the 1 PM OFFER post marked "SWAP FOR APPROVED KIT TEXT IF YOU HAVE IT" and keep the link reply line.
4. **Bio and display name (only with Jodie's explicit yes).** Signed in to Threads as @nursemadedigital, open Edit profile. Display name: `Jodie DeOliveira | Faceless Income with AI`. Bio, two lines exactly:
   ```
   For women building faceless online income with AI. Systems, not hustle.
   I built The Digital Income Edit™ solo, with Claude. This account is me.
   ```
   Link field stays `https://www.thedigitalincomeedit.com/resources/find-your-door`. Save, reload the public profile, read both lines back and confirm there is no em dash anywhere.
5. **Update the Sunday Threads-writing scheduled task.** Open the task. Change every reference from "18 posts a day, Section 1 slots" to "6 posts a day at 7 AM, 9 AM, 11 AM, 1 PM, 3 PM, 5 PM Eastern per `claude/TDIE_THREADS_SYSTEM.md` Section 1", the weekly total from 126 to 42, the offer slot from 5 PM to 1 PM with "LINK REPLY (post immediately)" instead of the 7 PM pinned comment, and the file format to the Section 5 block in the rebuilt system (OPEN, ASK, TEACH with numbered self-replies, OFFER, PROOF or TAKE, UPDATE). Add: "Read `claude/TDIE_JODIE_THREADS_VOICE.md` including THE ORIGIN LINE AND REAL SMALL NUMBERS." Add the Friday method: "Before writing, read last week's Friday readout and reuse the shapes of the top 3 posts by replies in the 7 AM and 3 PM slots." Keep the time zone, the source reads, the verify step and the one-line reporting standard the task already carries.
6. **Update the nightly Threads-loading scheduled task.** Change "load tomorrow's 18 posts" to "load tomorrow's 6 posts (7 AM, 9 AM, 11 AM, 1 PM, 3 PM, 5 PM Eastern) from the current week file `claude/threads-week-YYYY-MM-DD.md`; a TEACH post's numbered self-replies (`1/`, `2/`...) are posted as replies to the 11 AM post in order; the 1 PM offer's LINK REPLY is posted as Jodie's first reply immediately after the offer post; an ARTICLE REPLY line is posted as a reply to the 11 AM post". Remove the 7 PM pinned-comment step and the goodnight step. Keep the rule that only one automated session may act on the account at a time, and that the daily reply block is never automated.
7. Read both tasks back after saving and confirm the slot list, the file names and the one-session rule appear exactly as written above.
8. Mark this section DONE with the date.
