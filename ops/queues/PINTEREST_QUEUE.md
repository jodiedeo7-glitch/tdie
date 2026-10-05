> **Current core Pinterest reconciliation (4 October 2026):** Read `ops/ai-router/CORE_PINTEREST_RECONCILIATION_2026-10-04.md` first. It supersedes conflicting legacy browser, ownership-fallback, missing-source and vocabulary instructions below. This repository edit does not change live tasks or prove a publishing cutover.

# PINTEREST EXECUTION QUEUE

> **MIDJOURNEY, STANDING RULE (Jodie, 3 October 2026).** Jodie has an active Midjourney subscription, signed in in her browser, with far more free generations than Higgsfield. Whenever an image would come out better in Midjourney, use Midjourney, with or without a person. This amends every tool-order line in this file that says no other image generator is used. Canva is still never an image generator. Full rule: section M of claude/TDIE_IMAGE_GENERATION_MASTER.md.


This queue contains core Pinterest Metricool execution work for the verified publisher.

## Entry template

### Batch: <batch-id>
- Packet: `<path>`
- Created by: ChatGPT
- Contact sheet approved: YES / NO / NOT REQUIRED
- Pins READY: <count>
- Persona images still required: <count>
- Earliest proposed slot: <date time ET>
- Status: WAITING / RUNNING / PARTIAL / VERIFIED / BLOCKED

### Verified publisher execution
Read the current router and reconciliation, then follow its Metricool procedure against the exact packet. Verify ownership before writes. Record per-row platform IDs, observed scheduling state, readback evidence and failures. Do not open Pinterest to schedule or verify scheduled state.

### Never do in this queue
- topic research
- copy rewrites
- image generation
- layout design
- new product claims
- pricing decisions

## Live batches

### Batch: core-pinterest-2026-10-05-recovery-v1
- Packet: `ops/cloud-output/core-pinterest-2026-10-05-recovery-v1/README.md`
- Exact manifest: `ops/cloud-output/core-pinterest-2026-10-05-recovery-v1/pins.csv`
- Contact sheet: `ops/cloud-output/core-pinterest-2026-10-05-recovery-v1/contact-sheet.png`
- Created by: ChatGPT
- Contact sheet approved: NOT REQUIRED — existing layout system; standing weekly creative authorization, not individual contact-sheet approval.
- Pins READY: 2 (POOL 3 and POOL 5, new dated variants)
- Persona images still required: 0
- Earliest proposed slot: 2026-10-05 11:00 America/New_York; if elapsed use next permitted future core slot and record actual time.
- Status: SCHEDULED (2 of 2) — verified by Metricool readback 4 Oct 2026, 10:15 PM ET. Not yet PUBLISHED.
- Publisher: Claude, after re-verifying the private owner file. Metricool only.
- Scope: Two-pin recovery packet, not a full weekly batch. Amazon unchanged; WYS held.
- Execution receipt (Claude, 4 Oct 2026, about 10:13 PM ET; Metricool brand 7142540 only, no browser):
  - Ownership re-verified before writes: private `pinterest-owner.json` read back, owner Claude, scope CORE_PINTEREST. Amazon and WYS unchanged.
  - Duplicate check: `getScheduledPosts` for 5-6 Oct found no pin with either title; the core line had no pins scheduled from 5 Oct. Amazon, test and Threads objects untouched.
  - Packet verified: zip identical to commit d97bba2; manifest validator 0 errors; public image URLs returned HTTP 200; Metricool-hosted media SHA-256 equals the manifest hash for both pins.
  - Slots: both proposed times (5 Oct 11:00 and 14:00 ET) were still in the future, so they were kept. The two times were swapped between the pins: the 4 Oct 17:00 core pin used board id 1122311238330664773 (Beginner Online Business Ideas), so POOL 3 on that board at 11:00 would have repeated it back to back.
  - POOL 5 `freebie-delivery`: Metricool id 388146134, uuid 8097789177337630272, 2026-10-05 11:00 America/New_York, board "Faceless Digital Marketing for Beginners" (id 1122311238330664775), pending, autoPublish true, draft false.
  - POOL 3 `dfy-service-menu`: Metricool id 388146190, uuid 4524484013037537713, 2026-10-05 14:00 America/New_York, board "Beginner Online Business Ideas" (id 1122311238330664773), pending, autoPublish true, draft false.
  - Readback of both: title, description, alt text, destination https://www.skool.com/thedigitalincomeedit/about, media and time all match pins.csv exactly. Count of core pins in 5 Oct 10:00-15:00 window: 2.
  - AI disclosure: Metricool has no native AI-label field for Pinterest. The manifest's ai_label ON is intent only; the AI-generated photo disclosure is carried in the copy and alt text. A native label is NOT claimed.
  - SCHEDULED is not PUBLISHED. Publication to be checked after the slots pass.


### Batch: core-pinterest-2026-10-06--11-catchup-v1
- Packet: `ops/cloud-output/core-pinterest-2026-10-06--11-catchup-v1/README.md`
- Exact copy/slots/hashes: `ops/cloud-output/core-pinterest-2026-10-06--11-catchup-v1/pins.csv`
- Contract: `ops/cloud-output/core-pinterest-2026-10-06--11-catchup-v1/manifest.json`
- Contact sheet: `ops/cloud-output/core-pinterest-2026-10-06--11-catchup-v1/contact-sheet.png`
- Private packet folder: https://drive.google.com/drive/folders/1053LTR3S69x-cPEPkbml5fmJ9T5pVHVO
- Private ZIP ID: `1n_kdLgHSizm8WFBVrCGcRIU73633Cece`; SHA-256 `d1d698c412b4773f472c9cf2aa4378c43a004367a51f63080ec481baf6f705a6` (Drive raw readback identical to local ZIP).
- Exact pins.csv SHA-256: `d2d96f4774900e962b05f347f60fc18bdd4d6322d6355e18a491749986db0134`.
- Created by: ChatGPT. Verified publisher: Claude for CORE_PINTEREST only, re-read before account writes.
- Contact sheet approved: NOT REQUIRED, established canon ten-layout system under standing weekly creative authorization; no claim of individual contact-sheet approval. First-new-visual-system review still applies.
- Pins READY: 24, four per day October6–11, 2026. Persona images still required: 0. New photo generations/spend: 0.
- Status: SCHEDULED (24 of 24) in Metricool brand 7142540 by Claude on 2026-10-04 (11:46 PM to 11:50 PM ET), all before the 2026-10-06 08:00 ET first slot. Not yet PUBLISHED.
- Earliest proposed slot: 2026-10-06 08:00 America/New_York. Load the catch-up before that slot; do not wait for the Sunday Oct11 weekly run. If any slot has elapsed, use a permitted future slot and revalidate family spacing/rotation.
- Scheduling: sort by date/time. Thursday and Sunday email/automation times are intentionally swapped. Five boards, no adjacent repeat, cousins >=72h; first email >=75h from preserved Monday freebie route.
- Preserve Monday rows 388146134/8097789177337630272 (Oct5 11:00) and 388146190/4524484013037537713 (Oct5 14:00). Latest live read sees those two core rows only. Full-week28-pin coverage is not claimed; this batch fills Tuesday–Sunday.
- Source/QA: current validator 0 errors; all24 full-size/thumbnail images reviewed; every public URL HTTP200 and exact SHA-256 verified against assets commit `e91744b88a21031a5390cfe6920bbf2a872b1bc3`. Exact asset IDs/hashes and source IDs are in manifest.json. Native AI label is intent only; truthful AI disclosure is in each description and alt.
- Legacy backlog: POOL6 actual comparison recovered. Checklist05/07 angles rebuilt with new dated sourced copy. Four additional complete new copy variants06/08/09/10 remain HOLD in checklist-copy-holds.csv for current-brand PNGs and spacing; historical missing approved copy was not invented.
- Claude action: re-read owner and current live Metricool7142540, resolve all five board IDs from current evidence, reconcile duplicates, schedule future exact READY rows through Metricool only, read back each result, then append actual IDs/times/boards/asset matches and any failures here. No Pinterest browser. Account lock/concurrency still applies.
- Execution receipt (Claude, CORE_PINTEREST, Metricool only, no Pinterest browser):
  - Slots kept exactly as in pins.csv (all future). Duplicates checked first: none. Monday 388146134 and 388146190 untouched and still scheduled (Oct 5 11:00 and 14:00).
  - Every pin: pending, autoPublish true, draft false, destination https://www.skool.com/thedigitalincomeedit/about, pinNewFormat false.
  - Independent getScheduledPosts readback Oct 5-12: 24 of 24 match pins.csv on title, description, alt text, link and time; Metricool-hosted media SHA-256 matched pins.csv asset_sha256 for 24 of 24. Core pins in window: 26 (24 plus Monday's 2). Amazon-line and WYS test objects untouched.
  - Rows (time ET | Metricool id | pin id | board id):
    - 2026-10-06 08:00 | 388182714 | core-catchup-01-pool6-six-faces-2026-10-v1 | 1122311238330664775
    - 2026-10-06 11:00 | 388182769 | core-catchup-02-niche-three-circles-2026-10-v1 | 1122311238330664773
    - 2026-10-06 14:00 | 388182785 | core-catchup-03-checklist-plan-first-2026-10-v1 | 1122311238330664783
    - 2026-10-06 17:00 | 388182796 | core-catchup-04-finish-list-2026-10-v1 | 1122311238330666079
    - 2026-10-07 08:00 | 388182880 | core-catchup-05-offer-bottleneck-2026-10-v1 | 1122311238330664770
    - 2026-10-07 11:00 | 388182893 | core-catchup-06-questions-not-topics-2026-10-v1 | 1122311238330664783
    - 2026-10-07 14:00 | 388182903 | core-catchup-07-logo-off-test-2026-10-v1 | 1122311238330664775
    - 2026-10-07 17:00 | 388182928 | core-catchup-08-blog-answer-first-2026-10-v1 | 1122311238330664773
    - 2026-10-08 08:00 | 388182994 | core-catchup-11-manual-before-auto-2026-10-v1 | 1122311238330664775
    - 2026-10-08 11:00 | 388183014 | core-catchup-10-content-inventory-2026-10-v1 | 1122311238330664783
    - 2026-10-08 14:00 | 388183032 | core-catchup-09-welcome-email-purpose-2026-10-v1 | 1122311238330664770
    - 2026-10-08 17:00 | 388183041 | core-catchup-12-pin-title-topic-2026-10-v1 | 1122311238330664773
    - 2026-10-09 08:00 | 388183375 | core-catchup-13-identity-before-pretty-2026-10-v1 | 1122311238330664783
    - 2026-10-09 11:00 | 388183388 | core-catchup-14-niche-test-2026-10-v1 | 1122311238330664773
    - 2026-10-09 14:00 | 388183402 | core-catchup-15-checklist-close-2026-10-v1 | 1122311238330664775
    - 2026-10-09 17:00 | 388183414 | core-catchup-16-study-not-score-2026-10-v1 | 1122311238330666079
    - 2026-10-10 08:00 | 388183542 | core-catchup-17-offer-one-person-2026-10-v1 | 1122311238330664770
    - 2026-10-10 11:00 | 388183561 | core-catchup-18-content-answer-shape-2026-10-v1 | 1122311238330664783
    - 2026-10-10 14:00 | 388183600 | core-catchup-19-brand-opinion-2026-10-v1 | 1122311238330664775
    - 2026-10-10 17:00 | 388183611 | core-catchup-20-blog-heading-check-2026-10-v1 | 1122311238330664773
    - 2026-10-11 08:00 | 388183655 | core-catchup-23-automation-proof-2026-10-v1 | 1122311238330664775
    - 2026-10-11 11:00 | 388183668 | core-catchup-22-inventory-adapt-2026-10-v1 | 1122311238330664783
    - 2026-10-11 14:00 | 388183681 | core-catchup-21-email-outline-2026-10-v1 | 1122311238330664770
    - 2026-10-11 17:00 | 388183693 | core-catchup-24-pin-description-clarity-2026-10-v1 | 1122311238330664773
  - Four checklist-copy holds (06/08/09/10) remain HOLD, not scheduled. No 28-per-week coverage claimed.
  - AI disclosure: Metricool has no native AI-label field; ai_label ON is intent only, disclosure is in copy and alt. Native label NOT claimed.
  - SCHEDULED is not PUBLISHED; publication to be checked after slots pass.
- Errors for READY rows: none. Execution complete. Amazon, Brand Closet, Legally Blonde, Premium and Daily Prompts are separate; WYS hold remains ACTIVE.
