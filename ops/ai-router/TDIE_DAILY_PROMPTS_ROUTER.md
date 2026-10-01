# TDIE Daily Prompts Router | PROVISIONAL, DO NOT ACTIVATE

**Only scope:** Skool's one-image-a-day Daily Prompts lesson (Daily Edits) and matching Daily Free Prompt community post. This is **not** the Premium DFY Content Calendar, the paid DFY Viral Instagram Content Calendar, Threads, or either Amazon line. Do not reuse their research rules, prompts, images, scheduling queues, or QA criteria.

**Known user-approved daily routine:** at 8 AM **America/New_York**, publish that day's dated Daily Prompts lesson; then create the community post headed `<Month Day> Daily Prompt`, using that lesson's image. Post begins `Today's daily is posted!` with **only the word `posted`** linked to the exact lesson URL, followed by brief image-specific engaging copy. The lesson must exist and be read back before the community post is created.

**Source recovery:** SOP 16 and browser-lock/Skool-system snapshots were found locally. The signed-in Claude project lists SOP 16, and the active weekly build instructions were read live. See SOURCE_RECONCILIATION_2026-10-01.md. Current destination state and exact API/UI publication behavior must still be verified before cutover. No task was edited.

## Ownership

- **ChatGPT:** only when asked to create future dated lesson/image concepts, approved copy and image briefs following the **live Daily Prompts SOP 16**. Do not borrow Premium calendar creative rules or turn this into a research-heavy 31-day content calendar.
- **Image provider:** follows live Daily Prompts image rules and the approved master image-generation SOP, not the Premium calendar prompt parameters.
- **Claude:** uses the existing approved 8 AM publisher on Jodie's signed-in Skool account, or a single explicitly approved replacement. Acquires the shared browser lock. Uploads/creates the exact lesson, reads it back, then posts the matching community entry, reads it back, and logs both URLs.
- **Verification:** the dated lesson, correct photo, title, word-only hyperlink, community post and timezone must all be checked separately.

## Transactional publish sequence

1. **Timezone preflight:** confirm the actual task fires at 8 AM local Eastern across DST. A fixed 12:00 UTC task maps to 8 AM EDT but **7 AM EST** after clocks fall back. On 1 Nov 2026 and afterward, 8 AM EST is 13:00 UTC. Prefer an actual `America/New_York` schedule if supported; otherwise approve a documented seasonal change. Do not change an active task without inspecting its real schedule first.
2. Check if today's lesson and community post already exist. Never create duplicates on retry. Confirm the lesson is in the correct Daily Prompts course, with correct access settings; do not touch Premium calendar courses.
3. Confirm the exact approved daily image is ready and matches the lesson. Missing image = HOLD, not improvise with a calendar asset.
4. Create or update the dated lesson, then **read back the published lesson**. An editor save or API 200 is not enough. Capture the real lesson URL and the actual photo.
5. Create the `Daily Free Prompt` community post with heading `<Month Day> Daily Prompt`. The body begins with the required sentence; hyperlink only `posted` to the captured lesson URL. Include brief, relevant image-specific copy; do not change product offers or invent promotional claims.
6. Read back the community post as a user, verify the photo and hyperlink target, and log the actual URL and local timestamp. Mark complete only when **both** items are verified.
7. If lesson succeeds but community post fails, retain the verified lesson and retry only the community step after checking for a duplicate. If the lesson fails, do not post a dangling link.

## Required run log

`local_date,expected_local_time,lesson_status,lesson_url,image_file,community_status,community_url,hyperlink_verified,operator,exception`

`lesson_status` and `community_status` are independent: `NOT_STARTED`, `READY`, `PUBLISHED`, `VERIFIED`, `BLOCKED`.

## Migration gate

Before switching the existing Claude publisher to a new task: export the live SOP 16, live publisher prompt, live scheduled task list and current browser-lock SOP; compare against this router; identify any duplicate writers; test a **single approved date**; verify the result; only then disable the old task and enable a replacement. Do not run two publishers in parallel.

## Current live workflow details recovered 1 October
Weekly builder is ACTIVE Saturday 21:00, trig_01JFD28qXDxECtjjFDwLycui. Build seven days after the latest lesson with photograph, inspect the preceding seven for rotation, stop if the first new date is over 14 days ahead. Eleven-block 2,500–3,000-character prompts and standalone 9:16 reference-based photos; draft lessons, public images, read-back of every lesson. Month folders may be published but future lessons remain DRAFT.

08:00 publisher is trig_014j2sfXvkNSNNeAk5sLc5Qq. Its opened latest session shows Usage limit reached. Verify lesson/community state before retry. Existing community post has a second approved CTA: `Grab it here` hyperlinked to https://www.thedigitalincomeedit.com/resources/weekend-build-challenge, alongside `posted` linked to the lesson. At most two hyperlinks; omit the challenge CTA if the destination is unavailable. Preserve exact approved CTA from current task source rather than substituting a pitch.

SOP16 says historical API writes cannot change draft/published state; the daily task uses publication. Prove current UI capability on one authorized date. Never silently delete/recreate lessons to evade this constraint.
