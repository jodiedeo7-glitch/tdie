CUSTOMER EXECUTION POLICY, CANDIDATE REPAIR 4
AUTOMATIC and REVIEW_FIRST are distinct setup choices. All production instructions below use the matching authorization gate. Historical originals are preserved outside this candidate.

During setup, record AUTOMATION_MODE = AUTOMATIC or REVIEW_FIRST in MY_RECIPE.txt and structured state. AUTOMATIC is available only after the customer explicitly authorizes ongoing creation and scheduling within a recorded policy. Record the authorization text, actor, time, permitted accounts, exact board IDs/sections, destination paths, image provider/model, generation budget and period, look pace, channels, schedule/timezone, end date or revocation condition, and customer-supplied sourcing requirement. Do not invent authorization or a budget. If any required field is missing, finish setup before enabling recurring production.

AUTOMATIC: For each eligible look, execute the connected production recipe through publication without requesting ordinary per-image, copy or post approval. Use only complete authorized product rows. Apply every source, rights, image, copy, destination, public-board, cost, timing and duplicate check. After all checks pass, record approval_actor=automation_policy, approval_basis=the saved customer policy ID, policy_version, QA evidence, approved_at and the exact final asset/copy/destination/account/board/section/format/disclosure/timezone/schedule fingerprint. Customer selection fields are used only in REVIEW_FIRST; AUTOMATIC records policy authorization fields instead. Never mark a gate passed merely because the policy exists. Changed output invalidates its old fingerprint: rerun affected QA and policy checks, then record a new fingerprint automatically if still within the authorized policy. A changed account, model, board, destination scope, budget or authorization requires setup authorization again.

REVIEW_FIRST: Keep the original explicit per-Pin customer selection and scheduling authorization. Manual publishing remains customer-controlled. The customer chooses this mode to review every output or conserve connected-service credits.

In AUTOMATIC mode, preflight paid generation against the saved budget and approved model. Record expected and actual charges. Within that authorization, a preflight display is information, not another approval stop. No subscriptions, upgrades, silent model substitution or new account permissions. If an input, budget or capability is unavailable, record the affected item and continue independent eligible work. Only essential login, reauthentication or security verification needs immediate customer action. Never bypass platform approval/security requirements. Missing customer-supplied product intake is a prerequisite failure, not proof of unattended sourcing.

Persist write intent before mutations. Unknown outcome means reconcile provider IDs before retry, never recreate blindly. Resume only missing work. Reconciliation monitors actual publication, not merely scheduling. An initial controlled publisher test may be scheduled under the saved policy after all publication gates pass; read back the schedule before declaring the publisher configured, and independently verify its live publication. A future schedule is not publication.

Customer instructions alone do not establish runtime reliability. Declare unattended production verified only after a separate actual scheduled execution completes the intended connected stages, persists results, resumes safely and produces independently verified live posts. Account availability and external security challenges can still interrupt a run.

END CUSTOMER EXECUTION POLICY

# While-You-Sleep Storefront™ - State Schema

The structured state is authoritative. Markdown files are human-readable views/exports.

## IDs

LOOK_ID
PIN_ID
PRODUCT_ID / ASIN
IMAGE_ID
PUBLISHER_POST_ID
BOARD_ID
RUN_ID

## Automation policy and authorization records

Top-level: AUTOMATION_MODE (AUTOMATIC or REVIEW_FIRST), AUTOMATION_POLICY.
Policy fields: policy_id, version, authorization_text, authorization_actor, authorized_at, permitted accounts, boards/sections, destinations, provider/model/resolution, generation budget and period/spent, channels, pace, schedules/timezone, end_condition, revoked_at, sourcing_method.
Pin/blog/Instagram authorization fields: approval_actor (automation_policy or customer), approval_basis, policy_version, approved_at, qa_evidence, qa_passed, authorization_fingerprint. Preserve schedule_authorization_fingerprint as the Pin compatibility field. Fingerprints bind complete output, asset hashes, account, board/section, destination, disclosure, format, AI label when applicable and schedule/timezone. customer_selected/customer_schedule_authorized and their timestamps apply only to REVIEW_FIRST and must not be invented in AUTOMATIC.
An expired or revoked policy cannot authorize new writes. Reconcile existing provider objects regardless of mode. Changed output reruns QA; changed scope requires renewed authorization. Missing input/capability blocks affected work while independent work continues. Record login/security requirements; never bypass them.

## Look record

look_id
look_date
window
look_name
kind
board_id
board_name
products[]
destination_type
destination_url
image_ids[]
pin_ids[]
status
created_at
updated_at
error_code
notes

## Product record

Also preserve the approved written description, color/variant, shape/cut, material or explicitly unasserted material, distinctive details, source actor/method, rights evidence and intake fingerprint. Product selection remains a customer prerequisite unless a currently authorized integration is verified.


product_id
asin
short_name
source
affiliate_link
destination_path
status
last_checked_at
notes

## Image record

Also record generation write_attempt_id, exact prompt and prompt fingerprint, job_id, input reference IDs/rights, output-model readback, actual credit spend, attempt history, raw/final asset SHA256, deterministic layout version, and visual QA evidence. Persist the intent before paid submission. Unknown job outcome blocks retry until provider reconciliation. Reuse an existing valid IMAGE_ID; do not pay again on replay.


image_id
look_id
pin_id
provider
model
asset_location
generation_attempt
status
commercial_rights_recorded
created_at
notes

## Pin record

pin_id
look_id
image_id
title
description
alt_text
destination_url
board_id
board_name
board_url
board_public_verified
board_assignment_verified
board_verification_method
board_verified_at
disclosure_present
metadata_reviewed_at
scheduled_at
publisher
publisher_post_id
customer_selected
customer_selection_at
customer_schedule_authorized
schedule_authorization_at
schedule_authorization_fingerprint
publisher_post_uuid
write_attempt_id
write_outcome
verification_scope
verification_evidence
verified_at
status
last_checked_at
error_code
pull_requested
notes

## Run record

run_id
task
work_window_key
claim_owner
claim_expires_at
last_heartbeat_at
started_at
finished_at
result
created_ids[]
failed_ids[]
retryable_ids[]
notes

## Allowed states

intake_needed
sourcing
missed
write_outcome_unknown
ready
building
built
queued
customer_review_required
awaiting_approval
customer_scheduling_required
scheduled
customer_scheduled
published
verified
pull_requested
pulled
pull_failed
failed
dropped

## Idempotency

Track a blog object by stable look_id + slug, source/asset hashes, commit/deployment ID and live URL. Track Instagram separately by stable post ID + ordered asset/copy/account/schedule fingerprint and provider UUID. These records use the same write-intent, approval-invalidation and unknown-outcome rules as Pins. A new process must read saved state before any external create. Test partial-sibling, missing-input and ambiguous-write fixtures in an isolated namespace; simulated fixture success is not live provider proof.


A run must check stable IDs before creating work. Atomically claim task + work_window_key with an owner and expiry before production. If the state backend cannot atomically claim the window, use one operator at a time and record that manual serialization; do not claim concurrent execution is safe. Reconcile an expired claim before taking over; expiry is not evidence that an external write failed.

Persist write_attempt_id, exact payload fingerprint and pending write_outcome before a publisher mutation. If the response is lost or ambiguous, set write_outcome_unknown and read back through the supported publisher. Never blindly retry a create. Keep the stable publisher_post_uuid as well as publisher_post_id where the publisher exposes both; an edit may replace the numeric ID. Resume only after reconciliation establishes the actual outcome.

Duplicate prevention order:
1. LOOK_ID
2. PIN_ID
3. IMAGE_ID
4. PUBLISHER_POST_ID
5. deterministic fingerprint of destination + board + scheduled time + title

If an existing record is found, reconcile it. Do not create a second object.

## Markdown exports

pin-tab.md:
human-readable publishing queue.

storefront-log.md:
human-readable look, lesson and run history.

pin-drafts.md:
human-readable copy and asset references.

browser-lock.txt:
LEGACY LOCAL MODE ONLY. It is not used by cloud execution.

## Publisher states

Apply the mode-specific authorization gate in 12_STATE_SCHEMA.md: AUTOMATIC validates the saved policy scope and all QA, then records automation_policy authorization and the exact fingerprint without another ordinary customer approval. REVIEW_FIRST requires exact customer selection and schedule authorization. Changed output invalidates the fingerprint and reruns the gate; missing QA or authorization prevents the affected write.

TIME-SAVING / Metricool:
AUTOMATIC: built → queued (passing QA + saved policy authorization + exact fingerprint) → awaiting_approval only if platform security/review requires it → scheduled → published → verified.
REVIEW_FIRST: built → customer_review_required → queued (exact customer selection and schedule authorization) → scheduled → published → verified.

CREDIT-SAVING / native Pinterest:
customer_review_required → customer_scheduling_required → customer_scheduled → published → verified

customer_scheduled records the customer’s confirmation of a native schedule only. scheduled records publisher-confirmed scheduling only. published requires actual live publication evidence; verified requires independent checks of the live image, destination, board, disclosure and metadata. Store verification_scope, evidence and time. These statuses do not replace passing QA and mode-specific authorization.

## Pull states

scheduled → pull_requested → pulled
published → pull_requested → pulled
pull_requested → pull_failed

Never infer "pulled" merely because a publisher record disappeared.

## Recipe state mapping

Use sourcing while identifying pieces. Use intake_needed when an authorized product row is missing; do not store the compound value sourcing/intake_needed. Use missed for an unstarted lesson outside the documented eligibility window, with its date and reason. queued means internal work awaiting preparation; it does not mean a publisher accepted a schedule. Blockers use error_code and notes with the appropriate allowed status; do not invent new status strings.

