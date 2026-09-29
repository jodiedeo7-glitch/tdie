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
scheduled_at
publisher
publisher_post_id
status
last_checked_at
error_code
pull_requested
notes

## Run record

run_id
task
started_at
finished_at
result
created_ids[]
failed_ids[]
retryable_ids[]
notes

## Allowed states

intake_needed
ready
building
built
queued
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

A run must check stable IDs before creating work.

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

TIME-SAVING / Metricool:
queued → scheduled → published → verified

If Metricool/ChatGPT requires an approval:
queued → awaiting_approval → scheduled

CREDIT-SAVING / native Pinterest:
queued → customer_scheduling_required → customer_scheduled → verified

A customer_scheduled state records the customer's confirmation that Pinterest shows the Pin in its scheduled area. Use verified only after the customer's confirmation or supported publisher evidence is recorded.

## Pull states

scheduled → pull_requested → pulled
published → pull_requested → pulled
pull_requested → pull_failed

Never infer "pulled" merely because a publisher record disappeared.
