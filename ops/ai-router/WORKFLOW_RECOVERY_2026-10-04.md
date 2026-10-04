# TDIE workflow recovery audit, 4 October 2026

Status: PARTIAL. Repository and ChatGPT definitions inspected directly. Claude's pasted inventory is user-supplied, not a fresh API read. Historical installation receipts were read from the private TDIE Handoffs folder. No Claude task, customer campaign, product price, social post or delivery flow was changed by this audit.

## Confirmed cause and limits

- Commit f542c348deba0408ec7dcaa652c5d04e0dc6f014 brought main level with cloudflare-migration and removed operational documents, queues, validators and pin media. The actual changed-file list confirms the removals.
- Commit 6183849f26487a8c2934f02d280ae9cc57877da3 restored 75 files from b840382. That restored files; it did not reconcile all surviving instructions or repair scheduler definitions.
- The 2 October 07:06 UTC Claude installation receipt reports 3 updates, 35 device-approval blocks, 9 deletions and 1 creation. The 23:20 UTC follow-up reports 0 changes, 30 tasks edited elsewhere and 5 old IDs gone. Of its 35 comparisons, 11 matched intended prompt hashes and 24 did not, including the 5 missing IDs. A hash mismatch proves difference, not which version is correct.
- The later receipt says the Pink Finds cleanup task had no connectors to list/delete tasks. Its current capability remains UNVERIFIED.
- Current ChatGPT readback: 25 tasks, 9 enabled and 16 disabled. One enabled task is the unrelated Legal Nurse Roles search. Disabled includes completed one-offs; do not interpret all 16 as intentionally paused recurring work.
- The shared Pinterest folder listing returned no pinterest-owner.json. Both ChatGPT creative producers remain disabled. This is not authority to take over or to activate another writer.
- Metricool read for October 4–12 returned 20 objects across Pinterest AND Threads. Filter by provider and workflow. It returned a Pinterest PUBLISHED status as well as pending/draft objects despite the connector description saying scheduled-only. Record actual provider fields; disappearance or an aggregate count is never publication proof.
- WYS_LIVE_TEST.md's current checkpoint retains the release hold and distinguishes the failed original kit, partial repaired system, and unverified unattended sourcing. The product-of-record file distinguishes the Claude desktop kit from the uncertified V2/KIT6 candidate. Do not use one architecture's test as evidence for the other.

## Repository corrections in this change

1. Root source-read/recovery instruction: current main for operational instructions, cloudflare-migration for production site changes; preserve branch-specific files and never restore a whole branch or scheduler from an old snapshot.
2. Canon tool-stack wording recognizes already documented scoped exceptions without authorizing new integrations or granting new account access.
3. Image-generator exclusion now explicitly preserves Gemini, Nano Banana Pro, Seedream and Midjourney under existing rules; Canva remains a design tool, not a photography generator.
4. Core Pinterest routing uses the founder Metricool-only account rule, preserving one writer and unresolved cutover. Unsupported AI-label evidence is not fabricated.
5. Shared execution contract recognizes founder Threads standing authorization and Premium draft-review intake; it does not grant public release.
6. Historical October 1 migration documents are explicitly bounded as dated observations.

## ChatGPT prompt corrections applied and independently read back

| Task | Correction | State and timing |
|---|---|---|
| TDIE SEO Audit | Removed stale Vercel/host uncertainty; current Cloudflare branch and post-deploy verification | Preserved |
| TDIE Premium activation | Removed false claim that the stale-worker test is absent/due October 15; current test exists October 13, 09:00 Eastern; actual PASS still required | Preserved |
| TDIE free Daily Prompts preparation | Removed copied Saturday 21:00 Claude cadence conflicting with this task's saved Saturday 08:00 schedule; remains inactive | Preserved |

No routine task was activated, paused, rescheduled or run. These are instruction repairs, not successful production runs.

## Required owner/tool boundaries

| System | Preparation | Execution and verification |
|---|---|---|
| Founder Threads | ChatGPT weekly bank, 42 parents at six daily slots; Jodie's voice | Claude imports and schedules, reconciles replies separately. Routine QA-passed batches need no manual approval under October 3 decision |
| Daily Edits / free Daily Prompts | Existing Claude SOP16 weekly builder; ChatGPT preparation remains inactive unless reassigned | Existing Claude 08:00 lesson and matching community publisher; universal look, never Premium assets |
| Premium DFY | ChatGPT next-month phased research/creation after October 11 activation checks; October ownership remains Claude in current task definitions | Claude loads complete weeks as drafts for review, releases only approved weeks. Member Threads are two/day, separate from founder Threads |
| Core Pinterest | ChatGPT designated creative producer; live cutover incomplete | One reconciled operator using Metricool for founder account; no native Pinterest scheduling fallback |
| Founder WYS / themed Amazon / Brand Closet | ChatGPT connector-supported preparation and production after scoped handoff | Available authorized browser operator captures Amazon sources, own links and Idea Lists; one Metricool publisher. Existing operators remain until cutover is proven |
| Customer WYS kit | Exact product/version of record and buyer-selected path | Test on the instructed runtime. Founder Metricool migration does not silently rewrite the Claude desktop/native-Pinterest buyer kit |
| Weekend Ecosystem | Existing product and approved copy/code owners | Preserve paid-sale email → Make → MailerLite Buyers group → existing access automation; no competing access workflow |
| MailerLite | Copy preparation as assigned | Claude MailerLite plugin ONLY, including reads. No browser fallback |
| Skool / Facebook / Instagram | Exact current posting SOP and assigned packet producer | Claude/current approved account operator, own account checks and readback; existing authorizations only |
| Value Vault / Pretty & Paid | Product creation separate from store listings and entitlement | Preserve canon tier distinctions and flagged Vault Unlock state; do not publish listings merely because a build task ran |
| Website | Codex source changes and visual QA | Cloudflare production branch; complete mobile/desktop live QA where page changes occur |
| Paid client calendar | Client-specific research, approval and assets | Separate client workflow; never Premium membership or Daily Edits inputs |

Tool availability in this audit: GitHub, Drive and Metricool reads succeeded. Computer Use skill was read; its required node_repl runtime was absent from this session's tool registry. No Claude scheduler or MailerLite plugin was exposed here. This does not establish availability in Claude or a future unattended runtime.

## Disposition of every group in the pasted Claude inventory

All Claude enabled states below are from the user's pasted list, not independently re-read. Preserve them until the current full prompt, live destination and newer authorization are reconciled.

| Pasted task(s) | Repair/check required |
|---|---|
| DAILY EDITS 08:00; weekly build Thursday 21:00 | Keep SOP16 and lesson/community dedupe. Thursday differs from October 1 Saturday snapshot; do not roll back without the newer decision |
| FB daily mirror; today's mirror retry | One source post and one FB destination; reconcile partial post/comment success before retry |
| Daily missed-run sweep | Catch up only missing authorized work; never resume held launches or revive paused tasks |
| TEST CLEAN missed-run; pull sweep; nightly outfit; weekly themed looks; today's outfit check; Idea List review check | Six test tasks, separate isolated objects and exact kit version. Reconcile test window/results; retire only completed fixtures, never treat them as founder production |
| Due-time dispatcher | 13:06 cannot meet an immediate 13:00 offer reply; 12:06 cannot meet exact 12:00 TEACH+60. FB +5 needs actual parent time. Inspect supported due mechanism; do not claim exact timing from this cron |
| Deadline watcher | Alerts must not become a second creator. Terminal producer state/authorized transfer required; stale-worker fence still unproven. 04:20 must be cloud-only |
| All-platforms reply check | Serialize account writes; no unapproved outreach; preserve separate parent/reply evidence |
| DFY post maker 00:40 | Inspect whether October member work or a separate Instagram adaptation. No second monthly calendar creator; no computer-dependent execution before 07:00 |
| Threads queue top-up; Sunday Threads writer 06:00 | Sunday should consume ChatGPT's bank under current split, not independently rewrite it. Six/day, no routine approval gate. 06:00 must be cloud-only if preparatory; browser work obeys 07:00 limit |
| Skool member watch; inactive-member sweep | Different purposes; retain paused state. Do not restore removed nudges or perform member removals from this audit |
| Paused @the.faceless.homestead.mama poster; monthly insights; weekly test readout | Reconcile old handle with current @itstommykate source/account before any activation; data must retain actual account identity |
| October DFY load; Premium loader; October 19 loader switch-on | Keep October correction work separate from next-month production. Recheck complete draft-review contract, approval and dates before enabling/releasing |
| Weekly Pinterest factory | Metricool-only founder account; check cutover and finished-packet intake. Existing older body still creates its own batch; do not enable ChatGPT publisher alongside it |
| Brand Closet OOTD; Legally Blonde factory | Separate source queues and own links. No same-look duplicate; preserve flat lay/lifestyle spacing and source readback |
| Pretty & Paid build; Etsy package | Build proof precedes listing; preserve first-six accepted image checkpoint if applicable. No new listing or stock promise from a scheduled task title |
| Warm-member DFY offers | Draft only; investigate failure without sending messages |
| Friday numbers | Claude evidence export due 12:15, ChatGPT analysis at 12:30. Avoid duplicate analysis/copy work; verify hashes and account periods |
| Friday Pink Finds email | MailerLite plugin only; exact current campaign and audience |
| Friday Skool week build | Current posting SOP, finished packet, slot/duplicate checks, SkoolKit readback |
| Pink Finds October 1/4 group posts; cleanup | Date-bound series; inspect annual-repeat risk in raw cron. Cleanup needs scheduler tools; old receipt says missing. No deletion before verified completion |
| Remove Kit block from access email | Narrow Weekend Ecosystem bonus edit tonight; MailerLite plugin only. Restore automation and reconcile in-flight buyers; do not pause unrelated access |
| Storefront vault lessons; presale check | Release hold governs; do not resume based on launch dates |
| FB1 first-comment pair; FB2 first-comment pair | Compare full prompt, parent ID and destination before retiring a duplicate; both copies remain paused |
| Native pin publication check | Reconcile scope with ChatGPT daily publication checker and founder no-Pinterest-browser rule; customer-native testing is distinct |
| Pink Finds “sale is live” email | Verify WHICH sale. Do not assume Amazon seasonal sale equals WYS launch or pause it solely by title |
| WYS cancel test | Read-only verification of isolated cancel fixture; do not republish |
| Storefront Threads comments October 6/9 | Preserve launch hold; never post orphan comments without verified approved parent |
| Affiliate kit/presale-buyer post; presale closes/code off | Preserve hold; no delivery, code or commercial changes based on dates alone |
| Launch morning pair | Compare payloads and ownership; paused duplicates are not proof of safe future activation |
| Last-call check; sale ends/price reset; launch wrap-up | Read-only check may remain read-only, but must never autonomously release hold, send sales copy or change price |
| Claude stale-worker check October 14 | Coordinate with actual ChatGPT October 13 test and real transfer event; October 15 prose is obsolete. No PASS from schedule existence |
| Ended Brand Closet browser-lock retry | Historical failed/ended run. Inspect partial writes before any replacement; do not recreate automatically |

## Remaining blockers and next evidence

Claude must export its CURRENT full inventory including exact prompts, stable IDs, enabled state, model, tools, schedule/timezone, last-run result, updated_at and next run. Task names and the October 2 hashes are insufficient for a safe overwrite. The saved receipt identifies prior device approval failures; do not bypass them. If still present, finish all unblocked tasks and report the exact approval action.

Use the current private TDIE Handoffs installation receipts and THREADS_AUTOMATIC_HANDOFF_2026-10-03.md as comparison evidence, not blanket replacement prompts. Save an immutable before snapshot and per-field diff privately. Map replacement IDs by workflow, account and prompt, not name alone. Re-read each edited task and verify one bounded authorized destination result before declaring its workflow healthy.

Do not upload private task prompts, account payloads, tokens, customer data or detailed private receipts to this public repository.
