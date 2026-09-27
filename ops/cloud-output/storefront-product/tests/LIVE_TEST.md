# Live test (DESKTOP_FINISH_QUEUE.md section 4, Step 9)

Started Sun 27 Sep 2026, 2:34 pm Eastern. Run in Jodie's own accounts on the throwaway theme "Test: Pink Desk Finds".

## Progress

| Item | Result |
|---|---|
| 1. Secret board `Test: Pink Desk Finds` | DONE 27 Sep, 2:39 pm. Board id 1122311238331258833, privacy read back as secret. |
| 2. Folder, unzip, setup chat | DONE 27 Sep, 2:46 pm. Folder `Documents\While-You-Sleep TEST`, kit unzipped, seed image `avatar-seed-omni-reference.png`. Jodie ran the setup chat with the Step 9 answers; it wrote MY_RECIPE.txt, storefront-log.md, pin-tab.md, pin-drafts.md, browser-lock.txt and MY_SCHEDULED_TASKS.txt straight into the folder. `[TEST]` added after the board name in MY_RECIPE.txt. |
| 3. TEST scheduled tasks, nightly paused one night | DONE 27 Sep, 2:52 pm. Four tasks from MY_SCHEDULED_TASKS.txt, names prefixed "TEST ", each bound to this computer with the folder attached: weekly trig_01CrSDnPbMj3oNZATR9V7om4 (Sat 1:05 pm), nightly trig_01SVVRWuJsdHBVckPq9FH2ty (Sun to Fri 9:00 pm, PAUSED for Sun 27 Sep), pull sweep trig_012CDhUxdbNMQRaPrVtUmLgm (12:00 pm and 6:00 pm), missed-run sweep trig_015vJgKFQLtko2yo1YZwH6N5 (9:45 am). Each prompt carries a TEST wrapper in front of the buyer's text: Jodie's TDIE browser lock, a test-notes.md line, and the Step 9 limits (one look, pins at least 2 days out, "Test:" titles). |
| 4. TEST weekly build by hand | Fired 27 Sep, 2:53 pm (session cse_01XouNBqdxKh8yq75ZsZhNTb). Result: pending. |
| 5. 9:45 am missed-run sweep | pending |
| 6. PULL test | pending |
| 9. Cleanup | pending |

## Stalls and fixes

| # | What happened | File and line | Fix |
|---|---|---|---|
| S1 | Pinterest served blank pages for board create (`/board/create/` redirected to a blank Business Hub; the profile's saved page was blank too). Board made through Pinterest's own page request from a signed-in tab instead. | Not a kit file: Pinterest outage also seen 27 Sep in step 12. The kit's blank-page rule (03 R-rules, 06 BROWSER FALLBACK) already stops after two blanks. | None to the kit. |
| S2 | The setup chat had to invent the TEST-board exception inside MY_SCHEDULED_TASKS.txt. The master task prompts only say "If a board is secret, stop", so a buyer's dry run on a secret test board would stop at the board check. | `kit/06_SCHEDULED_TASK_PROMPTS.txt` line 23 (weekly JOB 2), line 55 (nightly JOB), line 91 (pull sweep JOB 5) | Add ", unless MY_RECIPE.txt marks it TEST" to all three, matching R11 in 03 and B8 in 04. |
| S3 | The missed-run sweep is told to follow the prompts in 06_SCHEDULED_TASK_PROMPTS.txt, the master copy with «FOLDER», «TZ» and «TIME» still unfilled; the setup chat patched it with "(or Task 1 and Task 2 above)", which means nothing inside a scheduled task. | `kit/06_SCHEDULED_TASK_PROMPTS.txt` line 114 (READ FIRST) and line 123 (JOB 5) | The sweep reads MY_SCHEDULED_TASKS.txt (Task 1 and Task 2, already filled in) and follows those. |
| S4 | Step 9 item 2 asks for `TEST` to be added after the board name by hand, but the setup chat already marks a TEST board (02 question 2). Hand-editing risks a second board name. | `DESKTOP_FINISH_QUEUE.md` section 4, Step 9 item 2 (queue doc, not a kit file) | Added as `[TEST]` so the name stays exact. No kit change. |
| S5 | With 11:00 pm shutdown the setup chat moved the nightly run to 9:00 pm, correctly (02 line 48, 2 hours before shutdown). On Jodie's computer that lands inside her own 9:00 to 11:30 pm run window and next to her real 9:20 pm Brand Closet task. The kit's own lock (browser-lock.txt) can't see tasks outside the kit. | `kit/02_SETUP_PROMPT.txt` line 50 | Add one line to the question 6 closing lines: if you already run other Chrome tasks, keep these run times clear of theirs. For this test the TEST tasks also take Jodie's TDIE lock. |

## ROUND_2.md open items, answered from this run

| Open item | Answer from this run |
|---|---|
| Folder attach and file writing in a desktop chat | WORKS. Jodie attached the folder with + > Add folder; the setup chat read the kit files and wrote all six files straight into the folder, no code-block fallback needed. |
| Missed run: skipped or waits | pending (Sun 9:00 pm nightly paused; Mon 9:45 am sweep) |
| Captured screenshot into a page's file input | pending (weekly build) |
| SiteStripe clipboard capture | pending (not needed on the Influencer path with the blog half off, 03 Part 3 step 3; recorded if the run hit it) |
| Brand Closet course name and lesson dates via `__NEXT_DATA__` | pending (nightly catch-up) |
| Pinterest AI label option and scheduler time zone | pending (weekly build) |
| Squarespace code block | not tested: no Squarespace site |
| GitHub default branch | not tested: blog half off |
