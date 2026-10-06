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

## READY: CORE_PINTEREST October 12–18, 2026, v1

- Producer: ChatGPT. Publisher: Claude, confirmed private pinterest-owner.json on October 6. No cutover or account mutation.
- Packet: ops/cloud-output/core-pinterest-2026-10-12--18-v1/manifest.json
- Drive folder: https://drive.google.com/drive/folders/1oo2d1S3CBPzOLq8o0aDYWvNyIhZxn7rT
- Main content Drive ID: 1BOzobFsztqPUAa88IXb6xdBRHFrkbUsb
- Exact UTF-8 pins.csv SHA-256: `6e95ad69d1310292f71dccae1381755612ee122af1146e2f9179079608804eeb`. Drive download readback passed.
- State: QA_PASSED; APPROVED by standing weekly creative authorization in recovered factory section A, within existing ten-layout system. No individual contact-sheet approval claimed. First new visual systems still require review.
- 28 pins, four per day, within accepted 4–6/day cadence. Five boards, no adjacent repeats, close cousins at least 72 hours apart across weeks. Final full-size and thumbnail visual review passed. Validator zero errors.
- Private recovered sources remain private. All pins use current source-based evergreen copy, not invented historical approved copy.
- Claude must download and hash pins.csv, read current owner/claims/live account, verify board IDs, skip exact versions already scheduled, and retain provider IDs/UUIDs plus content readbacks. All slots below are proposed future Eastern slots. READY is not SCHEDULED or PUBLISHED.
- WYS hold remains ACTIVE. Amazon, Brand Closet, Legally Blonde and Premium are separate.
- Native AI label ON is intent only. Actual AI disclosure is in description and alt.
- Canonical public URLs are the immutable commit URLs in manifest.json; ancillary row-details main-branch candidates are not load sources. All 28 canonical downloads matched hashes.
- Manifest Drive ID: 1DZJ0ghSLxkqMM0Bo67jPvjAAqQaX3wgV. Contact sheet Drive ID: 1Z56POyyUp2ZrGfCPxPb9E8rlvWPRpysM.
- Failures: none for READY rows.

| Proposed Eastern slot | Asset ID | Board ID | Drive PNG ID | Exact PNG SHA-256 |
|---|---|---|---|---|
| 2026-10-12 08:00 | core-w42-04-ai-generator-identity-v1 | 1122311238330664775 | 1xxqtoV1-LElC5crxv5c02k6WGI3mP-vF | 78c94ca101c4a415aa056cec8af8489690d3093005dec7557f3d87225cd1bd33 |
| 2026-10-12 11:00 | core-w42-06-affiliate-recommendation-v1 | 1122311238330664770 | 1eYqUU-Ja4JoWbOZyohPYbmEaXrFohbg0 | 58ae9be3353cf190f1ba350a5837046d35d506a1676b5d860054db71bf886078 |
| 2026-10-12 14:00 | core-w42-03-launch-checklist-v1 | 1122311238330664783 | 1no52ZSjLUdypZnE9s4m8tIfOi-86VqPd | 5768f01fdde2f3eebeb90367132ded230b8769de9a046819ed5cc24b00c4399c |
| 2026-10-12 17:00 | core-w42-05-shopify-fulfilment-v1 | 1122311238330664773 | 1w7F1t3anoUwQR8sADu0w6WuQfbB7OX8r | 246e8fb90e1cf44499b940119ece8618717b57cb464d3421ddb3c194a9ba964d |
| 2026-10-13 08:00 | core-w42-01-niche-selection-v1 | 1122311238330664775 | 1RNLQ9tVlYxg_0ozLPEmj5M3yys82CUID | 90827232639701e41329058438935cca0a07230563063ffd924e14758bd8053f |
| 2026-10-13 11:00 | core-w42-02-finished-work-scoreboard-v1 | 1122311238330666079 | 1AB_Fa-zz0JeXr8ohPbDc_1QD2Wc93dSx | 6c435aa10072bcdefbc4c55e11ec3d0ce75424260747d4d757063f4889b314f1 |
| 2026-10-13 14:00 | core-w42-07-first-offer-scope-v1 | 1122311238330664773 | 1uI1aejBPTcFAFYOUDi792wGyArwEpxSy | 71d5ebfa96daac55da32f8a7392e159e7d8544917ddb529006094c02624add79 |
| 2026-10-13 17:00 | core-w42-08-audience-question-bank-v1 | 1122311238330664783 | 1djEnsWsOIXSEvObmmQ3WKapbgqNNbkjv | 76bc1ae2949e75947d86d69e03fdf969e255aae8bec59c98fa568cbee69455f3 |
| 2026-10-14 08:00 | core-w42-09-brand-recognition-v1 | 1122311238330664775 | 1Idh2LhFp_Pad_-aeHRfSB3Rdq-0SyQIv | 73d29e9f4a0aa9b7ab4a25d94b833c63d40bccc2ebd8cbd92932b7d3b455a08c |
| 2026-10-14 11:00 | core-w42-10-evergreen-blog-writing-v1 | 1122311238330664773 | 1JF3xkqaxaH6_vitx_wBXOhbrOD3rJqfV | 0bbbfa01fab618a1ca902ce9148bed36164168cb62d47890b2a46426542c7294 |
| 2026-10-14 14:00 | core-w42-11-automation-sequence-v1 | 1122311238330664775 | 1n0mmjf256DeScwn9DaD1pqDKqu2U6HL9 | e84af40fd4a12eaeb918abc66a9e7919c67257304f6e457ba3dc53e475f98f46 |
| 2026-10-14 17:00 | core-w42-12-existing-content-inventory-v1 | 1122311238330664783 | 1ktMKEvCJYc53d8TUSqv0OziDUBmYwauJ | f2273ce2d0a24e3c8d8e8cdd85398e23eddf3237cf843eb78b331b10e23dc109 |
| 2026-10-15 08:00 | core-w42-13-welcome-email-planning-v1 | 1122311238330664770 | 1IpYIm8mLWmkpC0NTb2n7KGESSt_BhqWA | 6e9c766c018358e43ace69ee495e53569f29599fc4d8bde5490536e1b0d745cd |
| 2026-10-15 11:00 | core-w42-14-pinterest-keyword-writing-v1 | 1122311238330664773 | 1nlDWp1Qhy1Juf3vQ3bxF-5lSe0ccSXO5 | c5859fc6181924b17e571508a1efc8ffd61b664cae3b9c5f0a73ec501e6823ee |
| 2026-10-15 14:00 | core-w42-18-ai-generator-identity-v1 | 1122311238330664775 | 1hqR-zNrdDeFMl38aXgVuWAY8Y0L41LhS | d38453d6ad0ff7bbdd50ac87f07814525ac54c646ec7483f8dccbcc6676ea69d |
| 2026-10-15 17:00 | core-w42-20-affiliate-recommendation-v1 | 1122311238330664770 | 1Dbcg5TUmVbULn-LbErTWrEINV6dAu_0f | 4f5252070bdff61f7753713e5a2fa982111324605031e53c6f6dc07c7a7068b1 |
| 2026-10-16 08:00 | core-w42-17-launch-checklist-v1 | 1122311238330664783 | 1PrBNOr4ackKnJa6Ed_p-263T_OrDeJeu | 7d859155c7af1ee45907fb7fff3b007830c4e6c24424ee197750e82a62e81034 |
| 2026-10-16 11:00 | core-w42-19-shopify-fulfilment-v1 | 1122311238330664773 | 1dqFX4F8ureQDdmFpbb8u08nTY-tME4iR | 11107648719d61def3418e12af8ffa588e49febd1d8a6186798fce88556774dc |
| 2026-10-16 14:00 | core-w42-15-niche-selection-v1 | 1122311238330664775 | 1XxmQ5PDSmhM8sz23wDoFDVDtkKbZBNCa | 189ea530be677793dddc9ce96b83097a3111a9f007d42776894eb0e29c68ca21 |
| 2026-10-16 17:00 | core-w42-16-finished-work-scoreboard-v1 | 1122311238330666079 | 1gYWl4haLQuGbMr1a4zPKzTjoYJ1rtWnp | 57e81d448bb64d3d70c44ce813527f15a1b364d7c053c5ed23bd96a105dec88e |
| 2026-10-17 08:00 | core-w42-21-first-offer-scope-v1 | 1122311238330664773 | 1UwiHslLlUTdL78dalqAFDhCtngB2ZfEk | 4a7b00d76649048d28ffc1234507504a365f376100de7ed965cd68a3ed2f0e46 |
| 2026-10-17 11:00 | core-w42-22-audience-question-bank-v1 | 1122311238330664783 | 1V3jxRmIoDftplSE5IZwLw78qbxguQgf9 | 4abb76231db339ea43d54c9e556e53733fda7136844e043c81f72c1b0ba54b79 |
| 2026-10-17 14:00 | core-w42-23-brand-recognition-v1 | 1122311238330664775 | 1Q8oWX1aV144SyiVXdNzGm7R0wPbq9Fxl | 9302aefd4086dbccd62ce720b789fdd0b719a44197c94bbdcac1ad3412087438 |
| 2026-10-17 17:00 | core-w42-24-evergreen-blog-writing-v1 | 1122311238330664773 | 1R2FOeSsV_309-xIG_P1DPzenA_ImaCQ0 | 2d9d1dcd680ef2c14da53ff0164a620a525c4f3b3fdbd14f5413ebe4972b9386 |
| 2026-10-18 08:00 | core-w42-25-automation-sequence-v1 | 1122311238330664775 | 1sJ1QUdAWkfcHMXKFhmcIIC0tmqLu9_2p | b281f5663f7b9574601d069f401ef1090e6192a1505dda39e09d0b26a3b2f31e |
| 2026-10-18 11:00 | core-w42-26-existing-content-inventory-v1 | 1122311238330664783 | 1hWGx72Eaq-E40UF_u2DIq1LZzXsEjH7R | 59271d986556f7f58f04b4f5dbdb1296108a6201e9cd1efb27be1c7e8c79bbcc |
| 2026-10-18 14:00 | core-w42-27-welcome-email-planning-v1 | 1122311238330664770 | 1OqyncJrEHEQSz2DdiPGX1Jy07vW5uNLH | ddcfaa269558f5ec0ecabfe5442038a3b7372b01a573b08c6def23c14018b28f |
| 2026-10-18 17:00 | core-w42-28-pinterest-keyword-writing-v1 | 1122311238330664773 | 1rKzRwEZhVdCPI1_IZnPtvP9XeFoOtYmT | 13c05db9cbd9c31e21f4e967e55b58ba010bcc789ccddff61d158388c87f45a4 |
