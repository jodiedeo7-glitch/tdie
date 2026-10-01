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

Every Pin starts in customer_review_required. Keep it there until the customer selects the exact finished Pin and explicitly authorizes its schedule after destination, public board, disclosure, image and metadata checks pass. Bind that authorization to a fingerprint of the approved image, title, description, alt text, destination, board, disclosure and scheduled time. If any bound value changes, clear the selection/authorization and return the Pin to customer_review_required.

TIME-SAVING / Metricool:
customer_review_required → awaiting_approval (when a separate platform review is required) → scheduled → published → verified
customer_review_required → scheduled → published → verified (only after per-Pin customer selection and schedule authorization are recorded)

CREDIT-SAVING / native Pinterest:
customer_review_required → customer_scheduling_required → customer_scheduled → published → verified

A customer_scheduled state records the customer's confirmation that Pinterest shows the Pin in its scheduled area. This confirms scheduling only. Remain in customer_scheduled until publication is confirmed. Use published only with an actual published Pin URL or equivalent supported evidence, and verified only after the published image, destination, board, disclosure and metadata are checked. Store verification_scope (schedule or publication), verification_evidence and verified_at. Scheduling evidence must never be labeled publication verification. A scheduled or published state never substitutes for the recorded per-Pin customer selection and schedule authorization.

## Pull states

scheduled → pull_requested → pulled
published → pull_requested → pulled
pull_requested → pull_failed

Never infer "pulled" merely because a publisher record disappeared.

## Recipe state mapping

Use sourcing while identifying pieces. Use intake_needed when an authorized product row is missing; do not store the compound value sourcing/intake_needed. Use missed for an unstarted lesson outside the documented eligibility window, with its date and reason. queued means internal work awaiting preparation; it does not mean a publisher accepted a schedule. Blockers use error_code and notes with the appropriate allowed status; do not invent new status strings.
