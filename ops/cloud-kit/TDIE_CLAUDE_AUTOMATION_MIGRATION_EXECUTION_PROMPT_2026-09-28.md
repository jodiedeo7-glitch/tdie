# TDIE Claude Automation Migration Execution Prompt
## 28 September 2026

Paste the entire contents of this file into a Claude session that has access to the live TDIE Project, Claude Scheduled Tasks, the connected GitHub repository, and the user's signed-in browser when required.

## NON-NEGOTIABLE

This is an implementation task, not an architecture brainstorming task.

Read the current live task list first. Do not assume the repo or old operating manual is the live Scheduled Tasks inventory.

Do not delete or duplicate a production task until its replacement has passed its required test.

Do not move the While-You-Sleep Storefront customer workflow into ChatGPT Scheduled Tasks. Its local-file/local-browser architecture remains in Claude.

## PHASE 1 — LIVE INVENTORY

Open Claude Scheduled and inventory every TDIE production task. Include active, paused, one-off, disabled and expired-looking tasks.

Reconcile the live inventory against:
- the TDIE AI Operating Manual
- the repository
- ops/cloud-kit/TDIE_33_TASK_MIGRATION_MATRIX_2026-09-28.md
- ops/cloud-kit/TDIE_SOCIAL_AUTOMATION_REDESIGN_2026-09-28.md
- ops/cloud-kit/TDIE_MODEL_ASSIGNMENT_BACKCHECK_2026-09-28.md
- the relevant task-specific recipe files

Create a temporary inventory with:
task name, task ID if shown, schedule, model, local/cloud requirement, platforms touched, state files, and status.

Do not change anything during inventory.

## PHASE 2 — CONNECT METRICOOL

If Metricool is not connected to Claude:
connect the official Metricool connector using OAuth.

Confirm the Metricool brand that corresponds to The Digital Income Edit.

Confirm the required TDIE networks are connected in Metricool before migrating any publishing action.

Use Metricool as an execution connector, not as a replacement content brain.

## PHASE 3 — THREADS

Current architecture:
- Sunday writer creates 126 independent posts for the next week.
- Nightly top-up loads tomorrow's 18 posts in the browser.
- Reply checks and approved replies use browser execution.
- Friday readout reads Threads Insights.

Target:
- Keep Sunday research/writing in Claude.
- Route Threads publishing through Metricool.
- Route Threads supported inbox/comment work through Metricool.
- Route approved Threads replies through Metricool.
- Change the nightly top-up so it schedules the next 18 posts through Metricool instead of browser loading, if the current connection supports the required operation.
- Keep the existing nightly task until one full week passes with zero duplicate/missing-post errors.
- Then test whether the entire 7-day set can be scheduled at once from the weekly output. If that succeeds, retire the nightly browser loader.
- Never create one 126-post Thread. These remain independent posts.
- Only one system is the publisher of record for Threads. Never allow browser and Metricool to publish the same queue simultaneously.

## PHASE 4 — PINTEREST

Target:
- Keep the existing TDIE/Legally Blonde/Brand Closet creative rules.
- Separate creative generation from publishing.
- Route scheduling/publishing through Metricool where the exact Pin operation is supported.
- Use the existing CSV structure where batch import is more efficient.
- Do not assume Pinterest API future scheduling exists.
- Keep Pinterest-native/browser deletion for live Pins unless a verified action removes the live Pin.
- Keep the current 60-second pacing/blank-page safety logic until Metricool is proven.
- Do not create duplicate scheduled Pins by running the old and new publishers together.

For each Pinterest factory:
1. build the creative package;
2. validate image/copy/link/board;
3. schedule through one publisher;
4. record the platform ID and Metricool schedule state;
5. verify;
6. mark the state complete.

## PHASE 5 — INSTAGRAM

For professional Instagram accounts that are connected to Metricool:
- move feed-post scheduling to Metricool;
- keep AI-generated-content labeling required by the platform;
- keep Stories with link stickers in the manual/notification path unless Metricool's current API explicitly supports the needed interaction.

Do not assume @itstommykate is available until its account connection is actually verified.

## PHASE 6 — FACEBOOK

Keep the Facebook Group mirror in Claude/browser unless a current verified Group write connector exists.

Metricool Page publishing is not evidence that the Facebook Group mirror can migrate.

## PHASE 7 — SKOOL

Keep Skool execution in Claude/browser.

No verified replacement was established for the exact TDIE Skool write workflows.

Apply the existing Skool voice correction to the six affected tasks:
- 8am Daily Prompt
- Friday Skool week build
- FB daily Skool mirror
- Skool member watch
- Etsy listing package
- weekly Pinterest pin factory

Replace the stale Tommy Kate voice instruction with the current Jodie Skool voice source.

## PHASE 8 — AMAZON

Do not scrape Amazon with background fetches.

Keep loaded-page DOM reading and SiteStripe/Idea List browser work where required.

Check Amazon Creators API eligibility.

If eligible, test product retrieval with SearchItems/GetItems/GetVariations.

Do not migrate SiteStripe short-link generation or Influencer Idea List operations unless the API actually replaces them.

## PHASE 9 — MODELS

The September 25 model table is stale because Sonnet 5.5 released September 28.

Use:
- Sonnet 5.5 for bounded execution and routine browser/tool operations.
- Opus 5.5 for complex writing/design/judgment.
- Fable 5.1 only when the work genuinely needs longer-horizon reasoning beyond Opus 5.5.

Benchmark before downgrading:
- Monthly DFY calendar build
- Friday Skool week build
- Friday numbers/member read
- voice-sensitive reply drafting

Pass criteria:
same required facts,
same or better voice,
same or better completeness,
no new errors,
materially lower usage/cost.

## PHASE 10 — DETERMINISTIC STATE

Do not add a second state system if the existing Command Centre pins collection is sufficient.

For publishing objects, require:
- deterministic content key
- task ID
- source asset
- schedule
- platform
- platform ID
- status
- retry count
- last error
- updated timestamp

Treat prose logs as human-readable audit trails, not as the only source of machine state.

Before creating a new object after any ambiguous failure, query state/platform first. Never create a second object simply because confirmation was missing.

## PHASE 11 — GLOBAL SAFETY

Create one logical publisher-of-record rule per platform.

Create an expiring execution lease rather than relying on an immortal text browser lock.

Each scheduled task that writes externally must:
- acquire the correct lease;
- check pause/kill state;
- verify required account;
- verify destination;
- perform the operation;
- verify the result;
- write state;
- release the lease.

If a lease is stale, recover it after its expiry.

If an action partially succeeds, reconcile before retrying.

## PHASE 12 — BUILD COMPLETION GATES

Upstream build jobs must emit a completion marker before downstream publishers run.

Examples:
- Threads weekly file: 126 valid posts and status READY.
- Daily Prompts batch: 7 valid drafts and status READY.
- Pinterest batch: expected asset count and metadata rows complete.
- Etsy batch: expected listing count and fields complete.

A publisher must refuse partial batches and put them into the exception queue.

## PHASE 13 — REMOVE WASTE

Do not open a browser when no work is due.

Do not reread large files when the required state can answer the question.

Do not regenerate approved images.

Do not run a verification step twice when a single authoritative platform/state read-back proves the result.

Do not use screenshots where text/DOM/API verification proves the same condition.

Do not use high-tier models for deterministic loading/posting/checking.

## PHASE 14 — GITHUB AUDIT

The repository already has a Friday canon audit. It has been changed on the migration branch to use:
cron 0 8 * * 5
timezone America/New_York

Verify the branch change before merging.

## PHASE 15 — TESTS BEFORE RETIREMENT

Test in this order:
A. one Threads post through Metricool;
B. one Pinterest Pin through Metricool;
C. one Instagram feed post through Metricool, if the account is connected;
D. one supported reply through Metricool;
E. one duplicate/retry scenario for each migrated platform;
F. one full scheduled day without the old publisher running in parallel.

Only after these pass:
- disable the replaced browser publishing action;
- leave the parent task if it still performs valid work;
- remove the redundant task only if the replacement fully subsumes it.

## REPORT

At the end report only:
- tasks changed;
- tasks retired;
- connectors connected;
- tests passed;
- tasks still waiting on account access or verification;
- any rollback required.

Do not claim completion if any migration test failed.
