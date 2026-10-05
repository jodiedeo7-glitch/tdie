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
