# Shared execution contract

Each operation uses a stable `task_id` and exactly one `workflow_id`. Required state and manifest fields are in `ops/ai-router/WORKFLOW_REGISTRY.json` and `ops/ai-router/templates/operation-manifest.json`.

## States
`DRAFT -> QA_PASSED -> APPROVED -> READY -> RUNNING -> APPLIED -> VERIFIED -> COMPLETE`.
`BLOCKED` records a dependency or an explicit prohibition. `FAILED` means a known failed attempt. `UNKNOWN` means a write may have taken effect but read-back was lost. `CANCELLED` and `SUPERSEDED` require a reason. A ready item cannot run without approval and a complete packet. A generic `VERIFIED` operation records `observed_state` separately, such as SCHEDULED or PUBLISHED. Scheduled is never published.

Existing pin, Threads and Daily-specific statuses remain intact as adapter states; they are not silently converted. READY maps to ready, SCHEDULED/PUBLISHED maps to applied, VERIFIED maps to verified only with evidence. Replies have their own IDs and status. A customer manual action records `customer_scheduling_required` then `customer_scheduled`, with read-back still required; `pull_failed` remains a failure, not success.

## Claim, write and recover
1. Read the approved packet and current live account state; reconcile stable ID, exact content hash and requested timestamp before writing.
2. Acquire the existing account lock using its live SOP. Do not invent its location or bypass an unknown owner. Store claim owner and lease evidence. Serialize any shared browser as required by that SOP.
3. Persist RUNNING before action. Do exactly the approved operation. Immediately record APPLIED with platform ID when observed. If the outcome is ambiguous, record UNKNOWN and stop blind retries.
4. Read back the intended object independently and record account, URL/ID, exact content/asset match, local/UTC time, observed state and captured evidence. A scheduled object read-back verifies scheduling only.
5. Check partial success on retry. Finish only the missing lesson, community post, parent, reply or delivery action. No duplicate creates. If no reliable read-back exists, leave UNVERIFIED/BLOCKED.
6. Release only the lock owned by this run. Preserve errors and remaining work. No immediate-post substitute for failed scheduling.

## Scheduling and deadline protection
`CRON_TZ=America/New_York` expresses intent, not proof the scheduler supports timezone handling. Check actual scheduler semantics and DST with a live inventory. Shared-account busy windows from the current live SOP win over proposed windows. Historical October campaigns are evidence to inspect, never instructions to replay.

## Approvals and data boundaries
The user's audit/package request authorizes local consolidation. It does not activate a task or authorize customer emails, DMs, purchases, pricing, ad spend or publishing. Reuse existing authorization where documented; ask only for a genuinely missing essential approval. Internal manifests remain internal. Never transfer Jodie's IDs, logs, links, codes or locks into a buyer kit. Paid client manifests are isolated per client.
