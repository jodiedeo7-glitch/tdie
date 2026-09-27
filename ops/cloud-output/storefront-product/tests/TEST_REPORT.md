# Buyer tests: The While-You-Sleep Storefront™ kit

27 Sep 2026. Four realistic buyers, each run as two roles: Claude running `02_SETUP_PROMPT.txt` with the buyer's natural (sometimes vague) answers, then the scheduled task desk-running one look through the recipes. Nothing was browsed: ASINs, links and Idea Lists in the desk runs are marked simulated, and anything that depends on live Pinterest, Amazon or Claude app behaviour is marked unverified.

The files in each buyer folder (INTERVIEW.md, MY_RECIPE.txt, logs, MY_SCHEDULED_TASKS.txt, DESK_RUN.md) were produced from the **first draft** of the kit. Every finding below was then fixed in the kit, and round 2 (bottom of this file) re-ran all four buyers against the revised kit.

| Buyer | Path | Folder |
|---|---|---|
| 1 · Kayla | Influencer, persona, clothing + home, 5 looks/week, no site | `buyer-1-influencer-persona/` |
| 2 · Dana | Associates only, no persona, Squarespace site, computer off after 6 pm, 3 looks/week | `buyer-2-associates-no-persona/` |
| 3 · Priya | Weekend Ecosystem™ site, Influencer, persona, dark academia, 7 looks/week | `buyer-3-weekend-ecosystem/` |
| 4 · Jess | Brand Closet™ member ($9 tier), Influencer, persona, pink outfits | `buyer-4-brand-closet/` |

Pin copy in every desk run landed inside the limits (titles 76 to 91 characters, descriptions 488 to 498 including the disclosure, alt text 164 to 198). No slot collisions between the two automations in any test (closest two pins 3 hours apart).

## Round 1 findings and what was done

**Expected at the desktop finish, not defects:** the build note and two versions in `05_RECOMMEND_IT_TOO.txt` (finish step 1 keeps one), the `BEACONS_PRODUCT_URL` token in `11_WHATS_NEXT.txt` (finish step 4 fills it), and the Setup Guide PDF (it was rendering in parallel; it is now in `kit/`).

| # | Found by | Problem | Fixed in |
|---|---|---|---|
| 1 | 1, 3, 4 | Browser lock went "stale" after 2 hours, so the 6 pm sweep could take Chrome in the middle of a 5-hour Saturday build; the lock had no date | 03 R16: dated lock, refreshed every look or 20 minutes, stale only after 45 minutes |
| 2 | 1, 3 | Leftovers could never be finished: images lived only in one run, the log kept only titles | New `pin-drafts.md` (full copy plus where each image lives in the generator history); 03 Part 7 step 4 re-captures the image or regenerates once |
| 3 | 2 | A run killed after Publish but before verifying would schedule the same pin twice | 03 Part 6: "scheduled, not verified" written straight after Publish; leftovers check the scheduled page first |
| 4 | 1, 2, 3, 4 | "First day with no pin 1" pointed at today (25 minutes away) and broke at paces under 7 | LOOK DAYS set in setup by pace; builds start after today; never a pin 1 within 3 hours; at most 4 looks a run, a Wednesday run at 6 or 7 a week |
| 5 | 1, 3 | Persona path had no rule for home, desk or gift looks | 03 Part 4 and 07 P8: persona for outfits only; theme lists use the other collage |
| 6 | 1, 2 | Format A and B were written for "that girl" outfits only | Format A has outfit and vignette versions; Format B accents and background suit the theme |
| 7 | 1, 2, 3, 4 | R3 said the description ends with the disclosure, Part 5 put hashtags after it; #ad sat below the fold | Description starts "#ad " and ends with the disclosure line; hashtags before it |
| 8 | 2 | Associates-only on Squarespace: no page spec, images couldn't reach the site, pins could point at pages not yet live, "no building, no posting" was false for her | 08 rewritten: page-file spec, images saved by her from her generator history, pins wait until the page loads, the hand-work stated in 00, 01, 08 and at setup |
| 9 | 2 | Setup never asked the site platform, the Associates site listing or the Pinterest domain test; "no-website fallback" didn't exist | 02 question 3 rewritten (a to f): platform, SITE PAGE BASE, both checks, and a kind stop when there's no storefront and no site |
| 10 | 2 | "Move any time her computer is off" moved pin slots too | 02: only RUN times move; PIN slots post from Pinterest; nightly run 2 hours and evening sweep 1 hour before shutdown |
| 11 | 3 | Blog half: the task couldn't put a JSON through a file input, didn't know the category slugs, and the field names didn't match | 09: images via the upload page, JSON via GitHub's new-file page in one paste, LIFESTYLE CATEGORIES line, one field list (`listLink`) used in both places |
| 12 | 3 | Blog half needed a code session, GitHub sign-in, canonical tags, a noindex rule for empty categories, a forgiving loader, a retry when the page isn't live | 09 STEP 1 and STEP 3 rewritten; 01 item 7 (GitHub) |
| 13 | 4 | Rose's lifestyle prompt: "reference only" vs "scene idea" vs PERSONA WORLD disagreed | 04 B4: at most the moment and mood, rewritten, set in a PERSONA WORLD place, every brand, store, chain, device, cup-size or menu cue removed |
| 14 | 4 | Rose's flat lay screenshot had no rule for where it lives; Benable names and ASINs could still drive Amazon searches | 04 B1 and B2: screenshot stays inside the run; never search from Benable or lesson text |
| 15 | 4 | Lesson logged only at the end (duplicates after a crash); locked or renamed course read as "no new outfits" forever; no backlog cap | 04 steps 2 to 4: logged at once by address, clear message if the course can't be opened, newest 4 of a backlog, OUTFITS PER NIGHT |
| 16 | 4 | Setup asked times before membership | 02: The Brand Closet™ is question 5, times question 6 |
| 17 | 4 | Recommend-it card implied a free join gets the Outfit of the Day | 05 card: "Where my outfit ideas come from", tiers stated exactly; pin line no longer promises "every day" |
| 18 | 1, 3 | Calendar windows too small for the pace; no start rule for holidays; ideas could carry prices, brands or characters | 02 THEME CALENDAR: sized to pace, holidays start about 6 weeks out, no prices, brands, people or characters |
| 19 | 2 | Scripted fetching of Amazon search pages risks the Associates account | 03 R18 and Part 3: read pages as they load, never fetch in the background |
| 20 | 1, 3 | Recipe's own example title promised speed ("You Can Order This Week") | Example replaced |
| 21 | all | Smaller items: "It is Saturday" hard-coded, AI label fallback, Pinterest time zone check, board sections, lock-icon wording, pull cutoff, sleep settings, run length, Nano Banana backup, persona format list, book titles, hero-piece definition, first-sales rule, Influencer approval note, named time zones, Saturday exit for the nightly run, two-time schedule fallbacks | 02, 03, 04, 06, 07, 01, 00 |

**Decisions made, not changed:**
- The disclosure on buyers' pins is `#ad As an Amazon Associate I earn from qualifying purchases.` on both paths: that is the statement Amazon's own rules give. Jodie's own pins keep canon's Influencer wording (Decision 101); the kit doesn't change her setup.
- The Brand Closet™ join line stays exactly as instructed ("Affiliate link: I earn a commission if you join, at no extra cost to you."), although buyer 4 noted a free join pays nothing. Flagged in the job report.
- "About 5 minutes to start" stays (it is the brief's buyer promise and Jodie's own words); the kit now says plainly that runs take longer and that the setup has a couple of follow-ups.

## Round 2

See `ROUND_2.md` in this folder.

## Canon checks on this folder

`run_checks.py` flags four review hits inside the buyer folders. Each is a simulated buyer's own words or a tester's note about the kit refusing them ("she's blonde", "barbie vibes", "hair color", a character-count note), kept as evidence that the kit's rules held. None appears in anything a buyer receives. One fail hit (a retired colour word in a simulated look idea) was reworded.

## After round 2: founder decisions (27 Sep 2026)

Applied to the kit after round 2: the Brand Closet™ line now uses the facts from Jodie's real recipe (course address, lesson contents, `__NEXT_DATA__` read, 3-day window with an out-by time, Saturday caught up on Sunday); the join line reads "if you upgrade"; a fourth task (the daily missed-run sweep) and a Runs table were added; the requirements page states the account risk; a board marked TEST may stay secret for a dry run. The open items in `ROUND_2.md` are answered by the live test in the desktop finish (queue section 4, step 9), which gates the presale.
