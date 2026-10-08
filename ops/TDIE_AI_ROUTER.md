> **WYS authority, 7 October 2026:** [Read the complete WYS master](https://github.com/jodiedeo7-glitch/tdie/blob/main/claude/WYS_REFERENCE_PACK_2026-10-07.md). It is the sole active WYS workflow. This shared document cannot supply WYS generation defaults or override its current three-image prompts, pause or release hold. SOP-15/SOP-16 and unrelated systems retain their own authority.

> Current reconciliation: read `ops/ai-router/SOURCE_RECONCILIATION_2026-10-01.md` and `LIVE_MIGRATION_ACTIONS_2026-10-01.md` before acting. The recovered source register and live task inventory supersede earlier missing-source assumptions and the uploaded eighteen/day Threads copy.

# TDIE AI router

**Tool access rule (Jodie, 8 October 2026): nothing in this repository is ever restricted to Claude only.** Claude, ChatGPT, Codex or any other assistant Jodie uses may do any MailerLite work (reads, forms, groups, drafts, campaigns, test sends, schedules, automations, reports) and any other task, through whatever connector or API access that tool has. Each tool uses its own access and never waits for another tool to hold the connector. Use a connector or API first; a browser is a last resort, only after every other route has failed. Never leave a step undone because a different tool holds the connector: say what is needed and do it with the tool's own route. Any older line that restricts MailerLite, or any other service or task, to Claude only is superseded by this rule.

Consolidated 1 October 2026. Repository implementation is deployed; nine ChatGPT cloud preparation definitions are saved (five active, four paused), the three Codex preparation duplicates are paused, and the existing Sunday Threads task has guarded intake instructions. Full platform cutover remains unverified. Read ops/ai-router/DEPLOYMENT_STATUS_2026-10-01.md for the actual boundary.

## Authority and access
Latest explicit founder corrections govern this migration. Read `ops/canon/canon.json` and `ops/canon/TDIE_CANON.md` for business facts. Live system observations establish actual state; the uploaded repository establishes snapshot evidence only. This router assigns work and does not amend prices, products, images, schedules or business canon.

Find Your Door is no longer automated. Preserve the routing resource and API code; neither is evidence of an active email automation. Never create, migrate or restore its historical email sequence.

Hosting is Cloudflare (worker `tdie-site`, deployed from the `cloudflare-migration` branch). Vercel is retired: ChatGPT migrated the site after the Vercel free tier ran out of space. The staging proposals below add ChatGPT/Codex ownership and mention alternative connectors; treat those as migration proposals. Never reinstate Vercel or overwrite the Cloudflare setup.

## Quality-first allocation
| Layer | Default owner | Required evidence |
|---|---|---|
| Research, strategy, copy and creative preparation | ChatGPT | Sources, complete packet and editorial QA |
| Repository implementation and deterministic checks | Codex | Reviewable diff, tests and rollback |
| Signed-in account operation | Existing approved operator, often Claude | Actual access, permission, capability and read-back |
| Person/photo generation | Canon-approved image provider | Exact approved model, reference and inspected artifact |
| Mechanical monitoring | Existing GitHub Actions | Scoped findings, complete report and dated evidence |

Prefer the verified API/native route when it provides the required behavior and evidence. The names in job filenames identify a proposed handoff, not a claim that a platform is always best. Do not introduce a connector or scheduler merely because a draft mentions it. Pricing and usage cost do not decide creative ownership. Strategy and creative are finished before account execution.

## Separate workflows
| Workflow ID | Router | Queue |
|---|---|---|
| CORE_PINTEREST | `ops/ai-router/TDIE_PINTEREST_ROUTER.md` | `ops/queues/PINTEREST_QUEUE.md` |
| PREMIUM_CALENDAR | `ops/ai-router/TDIE_PREMIUM_CALENDAR_ROUTER.md` | `ops/queues/PREMIUM_CALENDAR_QUEUE.md` |
| DAILY_PROMPTS | `ops/ai-router/TDIE_DAILY_PROMPTS_ROUTER.md` | `ops/queues/DAILY_PROMPTS_QUEUE.md` |
| PAID_VIRAL_INSTAGRAM | `ops/ai-router/TDIE_PAID_VIRAL_INSTAGRAM_ROUTER.md` | `ops/queues/PAID_VIRAL_INSTAGRAM_QUEUE.md` |
| THREADS | `ops/ai-router/TDIE_THREADS_ROUTER.md` | `ops/queues/THREADS_QUEUE.md` |
| INTERNAL_AMAZON | `claude/WYS_REFERENCE_PACK_2026-10-07.md` | `ops/queues/AMAZON_QUEUE.md` |
| BRAND_CLOSET_OOTD | `claude/WYS_REFERENCE_PACK_2026-10-07.md` | `ops/queues/BRAND_CLOSET_QUEUE.md` |
| WYS_CUSTOMER_PRODUCT | `claude/WYS_REFERENCE_PACK_2026-10-07.md` | `ops/queues/STOREFRONT_CUSTOMER_PRODUCT_QUEUE.md` |
| EMAIL | `ops/ai-router/TDIE_EMAIL_COMMERCE_ROUTER.md` | `ops/queues/EMAIL_QUEUE.md` |
| COMMERCE | `ops/ai-router/TDIE_EMAIL_COMMERCE_ROUTER.md` | `ops/queues/COMMERCE_QUEUE.md` |
| SKOOL | `ops/ai-router/TDIE_SKOOL_ROUTER.md` | `ops/queues/SKOOL_QUEUE.md` |
| WEBSITE | `ops/ai-router/TDIE_WEBSITE_ROUTER.md` | `ops/queues/WEBSITE_QUEUE.md` |
| IMAGES | `ops/ai-router/REMAINING_WORKFLOWS.md` | `ops/queues/IMAGE_QUEUE.md` |
| VERIFY | `ops/ai-router/REMAINING_WORKFLOWS.md` | `ops/queues/VERIFY_QUEUE.md` |
| TIKTOK | `ops/ai-router/REMAINING_WORKFLOWS.md` | `ops/queues/TIKTOK_QUEUE.md` |

`ops/queues/` is the only active queue directory; `ops/jobs/` holds job packets. The original `ops/cloud-output/DESKTOP_FINISH_QUEUE.md` is preserved as historical input, not a blanket execution order. Mapped candidates remain `UNVERIFIED` until reconciliation. No staged template is an actual pending task.

## Shared handoff and state
Read `ops/ai-router/EXECUTION_CONTRACT.md`, `ops/ai-router/SOURCE_REGISTER.json` and `ops/ai-router/WORKFLOW_REGISTRY.json`. Every task has a stable ID, workflow, account, exact packet, approval evidence, source hashes, local time, dependencies and independent read-back. Keep parent posts, replies, lessons, community posts and commerce actions as distinct operations. CSV templates are blank headers, not sample live work.

Run deterministic validators before release. Passing package QA does not prove scheduling, publishing, purchase delivery or product readiness. All live dependencies remain UNVERIFIED here.

## Controlled rollout
Follow `ops/ai-router/MIGRATION_SEQUENCE_V2.md`. Prepare and QA outside the live account. Inventory existing tasks read-only, then cut over one writer at a time: disable the old writer before enabling its replacement. Do not run old and new writers in parallel. If the new writer fails, stop it, reconcile partial effects, and restore only one approved prior/manual operator. Never replay expired dates or completed legacy actions.

## Reporting
If all relevant checks passed, report one line with a factual anchor. Report only material exceptions or required action. Preserve full research and actual deliverables. Do not claim a live action from a draft, successful click or task listing.
