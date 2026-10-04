# Shared execution contract

Each operation uses a stable `task_id` and exactly one `workflow_id`. Required state and manifest fields are in `ops/ai-router/WORKFLOW_REGISTRY.json` and `ops/ai-router/templates/operation-manifest.json`.

## States
`DRAFT -> QA_PASSED -> APPROVED -> READY -> RUNNING -> APPLIED -> VERIFIED -> COMPLETE`.
`BLOCKED` records a dependency or an explicit prohibition. `FAILED` means a known failed attempt. `UNKNOWN` means a write may have taken effect but read-back was lost. `CANCELLED` and `SUPERSEDED` require a reason. A ready item requires a complete packet and the workflow's applicable authorization. Founder Threads routine batches use standing authorization and approval_state NOT_REQUIRED under the 3 October decision, not a new per-batch approval. A complete QA-passed Premium week with PENDING_REVIEW may be loaded as DRAFT for review; public release still requires APPROVED. Read the current workflow router and private v2 handoff contract before acting; do not collapse producer, approval and consumer states. A generic `VERIFIED` operation records `observed_state` separately, such as SCHEDULED or PUBLISHED. Scheduled is never published.

Existing pin, Threads and Daily-specific statuses remain intact as adapter states; they are not silently converted. READY maps to ready, SCHEDULED/PUBLISHED maps to applied, VERIFIED maps to verified only with evidence. Replies have their own IDs and status. A customer manual action records `customer_scheduling_required` then `customer_scheduled`, with read-back still required; `pull_failed` remains a failure, not success.

## Claim, write and recover
1. Read the approved packet and current live account state; reconcile stable ID, exact content hash and requested timestamp before writing.
2. Acquire the existing account lock using its live SOP. Do not invent its location or bypass an unknown owner. Store claim owner and lease evidence. Serialize any shared browser as required by that SOP.
3. Persist RUNNING before action. Do exactly the approved operation. Immediately record APPLIED with platform ID when observed. If the outcome is ambiguous, record UNKNOWN and stop blind retries.
4. Read back the intended object independently and record account, URL/ID, exact content/asset match, local/UTC time, observed state and captured evidence. A scheduled object read-back verifies scheduling only.
5. Check partial success on retry. Finish only the missing lesson, community post, parent, reply or delivery action. No duplicate creates. If no reliable read-back exists, leave UNVERIFIED/BLOCKED.
6. Release only the lock owned by this run. Preserve errors and remaining work. No immediate-post substitute for failed scheduling.

## Scheduling and deadline protection
`CRON_TZ=America/New_York` expresses intent, not proof the scheduler supports timezone handling. Check actual scheduler semantics and DST with a live inventory. Founder override, 4 October 2026: the computer stays on 24/7; long production work is authorized overnight. The old pre-07:00 computer-work prohibition is superseded. Public posting and client-facing deadlines stay unchanged unless separately authorized. Shared-browser production must checkpoint safely and defer remaining batches when they would block due client-facing work; never interrupt an in-flight or ambiguous write. Check actual durations, retries and monthly/weekly intersections rather than treating staggered start times as non-overlap. Update task prose and retry/deadline references with schedule changes. Shared-account busy windows from the current live SOP win over proposed windows. Historical October campaigns are evidence to inspect, never instructions to replay.

## Approvals and data boundaries
The user's audit/package request authorizes local consolidation. It does not activate a task or authorize customer emails, DMs, purchases, pricing, ad spend or publishing. Reuse existing authorization where documented; ask only for a genuinely missing essential approval. Internal manifests remain internal. Never transfer Jodie's IDs, logs, links, codes or locks into a buyer kit. Paid client manifests are isolated per client.
