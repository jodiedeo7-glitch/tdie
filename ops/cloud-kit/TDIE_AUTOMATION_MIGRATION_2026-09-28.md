# TDIE Automation Architecture Migration
## Implementation Package — 2026-09-28

This file is the implementation source for migrating the TDIE automation system. It supersedes earlier migration drafts.

## Critical rule

Do not delete or duplicate production automations until the replacement for that automation has passed its end-to-end test.

## Architecture

Use this ownership model:

- ChatGPT: research, strategy, creative reasoning, copy, visual QA, reporting, GitHub/repo work.
- Higgsfield through its official ChatGPT integration: image/video generation when the required Higgsfield capability is needed.
- ChatGPT Images: image generation/editing when it produces the required TDIE output without needing Higgsfield.
- Metricool: Pinterest publishing/scheduling and analytics where its current supported Pinterest workflow satisfies the requirement.
- Amazon Creators API: Amazon product retrieval only after the account is confirmed eligible.
- Claude: retain only execution/browser work that has no verified simpler connector/API replacement.
- Deterministic code/state: dates, due-run calculations, IDs, deduplication, leases, retry counts, queue state, reconciliation and validation.

## Immediate migration targets

### 1. Pinterest creative production
Move the creative portion out of the monolithic Claude Pinterest tasks.

ChatGPT owns:
- research/angle
- creative direction
- Pin concept
- image generation
- Pin title
- description
- alt text
- visual QA

Publishing remains separate.

### 2. Pinterest publishing
Test Metricool as the publishing/scheduling layer before changing the production publisher.

Do not treat the Pinterest API as a future-scheduling replacement. Use Pinterest API only for operations it actually documents/supports.

### 3. Higgsfield
Test ChatGPT + official Higgsfield integration against the current Claude → Higgsfield path using one existing approved TDIE asset.

Compare:
- final quality
- identity consistency
- credit consumption
- correction rounds
- manual actions
- total turns
- failure rate

Do not add a second generation step merely to move the workflow between agents.

### 4. Amazon sourcing
Check Creators API eligibility before redesigning Amazon product lookup.

If eligible:
- test SearchItems/GetItems/GetVariations
- compare returned product data against the current browser workflow
- migrate only product retrieval that the API actually replaces

Do not assume Creators API replaces Influencer Idea List/storefront management.

## Storefront scheduled-task redesign

The existing four-job design is:
1. weekly themed-look build
2. nightly Outfit of the Day
3. pull sweep
4. missed-run sweep

The current prompts make Claude perform too much deterministic work.

### Weekly themed-look build
Keep the task as an execution coordinator, but separate:
- deterministic date/slot selection
- creative generation
- Pinterest publishing
- verification
- state updates

The task must not repeatedly infer dates or status from prose when structured state can answer it.

### Nightly OOTD
Keep member-only execution and the paid-content safety rules.

Separate:
- lesson/slot detection
- Amazon product retrieval
- creative generation
- publishing
- verification
- state update

Do not expose, save or upload paid-member lesson assets.

### Pull sweep
Replace AI interpretation of pull state with deterministic state.

A pull sweep should:
1. query structured state for PULL items
2. query the publisher/API for platform state
3. perform only required deletion/action
4. reconcile state
5. leave unresolved items in an exception queue

It should not reread broad markdown logs to infer status.

### Missed-run sweep
Replace LLM inference of missed runs with deterministic due-time logic.

The sweep should compare:
- task ID
- due timestamp
- last successful/started execution
- next scheduled execution
- retry state

It should not infer missed runs from prose row names if structured execution state exists.

## Required state model

Create one canonical structured state record for each content object:

- content_id
- task_id
- recipe_version
- customer_path
- content_type
- source_look_id
- asset_id
- board
- destination_url
- scheduled_at
- platform_id
- platform_status
- local_status
- retry_count
- last_error
- created_at
- updated_at
- approval_status
- generator
- generator_model
- generation_count

Use deterministic IDs/idempotency keys so a retry cannot silently create a duplicate.

## Browser lock

Do not treat a markdown browser lock as the only concurrency control.

Use a timestamped lease:
- owner
- acquired_at
- expires_at
- task_id

Expired leases are recoverable. A task must not wait indefinitely on a stale lock.

## Error handling

Every external action must have:
- bounded retries
- explicit failure state
- last error
- next retry time
- dead-letter/exception state after retry limit
- reconciliation before retrying creation

Never create a new Pin/post simply because the prior action's confirmation was unavailable.

## Asset reuse

Before generating an image:
1. look up an approved matching asset by deterministic asset/content key
2. reuse it when the required composition is identical
3. generate only when no approved asset exists or the required scene is materially different

Do not add a second paid image-generation stage merely to add text if deterministic text overlay can accomplish the requirement.

## Customer-facing safety rules that remain

Retain the existing TDIE rules for:
- paid member content
- no third-party IP
- disclosures
- no passwords
- no prices/brand names where prohibited
- no downloads where prohibited
- correction limits
- scheduling horizon
- renewal-date boundary

## Migration order

1. Pilot ChatGPT + Higgsfield on one existing approved asset.
2. Pilot Metricool on one Pinterest Pin.
3. Pilot ChatGPT creative + Metricool publishing end-to-end.
4. Convert pull/missed-run state handling to deterministic state.
5. Migrate the Pinterest creative factories.
6. Evaluate Amazon Creators API eligibility and pilot if available.
7. Migrate other creative-heavy workflows.
8. Retire only the Claude tasks whose replacements have passed production validation.
9. Update customer-facing documentation after the new production workflow is proven.

## Do not do

- Do not create duplicate scheduled tasks for the same trigger.
- Do not delete existing production tasks before a replacement passes.
- Do not assume an available connector replaces every operation of a platform.
- Do not use an LLM for deterministic date/status/deduplication logic when code/state can do it.
- Do not regenerate approved assets unnecessarily.
- Do not make customer instructions depend on an unverified account capability.

## Verification standard

A migration is complete only when:
1. the new path produces the required artifact;
2. the platform action succeeds;
3. platform state is confirmed;
4. local state is reconciled;
5. a retry/duplicate scenario has been tested;
6. the old task can be safely disabled without creating a gap.

