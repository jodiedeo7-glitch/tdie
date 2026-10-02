Read 14_AUTOMATIC_EXECUTION_CONTRACT.txt first. Its main-path and capability rules apply throughout this file.

# The While-You-Sleep Storefront™: Automation Rules and State

This file has two parts. Part A is the rule book every task and every chat follows. Part B is the record-keeping layout (the "state") that stops work from being lost or done twice. Every task reads this file at the start of every run.

# PART A. THE AUTOMATION RULES

## A1. Two modes, chosen once at setup

Setup saves AUTOMATION_MODE in MY_RECIPE.txt and in the state. It is one of:

AUTOMATIC. The customer authorizes a written scope once, during setup (A2). After that, every Pin, blog page or Instagram post that passes every check inside that scope is scheduled without asking again. For each one, record:
- approval_actor = automation_policy
- approval_basis = the saved policy_id, and policy_version
- qa_evidence and qa_passed (which checks ran and what they showed)
- approved_at
- authorization_fingerprint: an exact record of the final image (file hash), title, description, alt text, link, account, board, section, disclosure, format, AI label where it applies, scheduled time and time zone.
A policy existing is never a pass by itself. Every check still has to pass for every output. Platform consent must also be compatible with the proposed arrangement; see 14_AUTOMATIC_EXECUTION_CONTRACT.txt. Blanket customer scope does not establish a Pinterest developer-policy exception.

REVIEW_FIRST. Nothing is scheduled until the customer picks the exact finished Pin (or post) and says yes to its time. Record customer_selected, customer_selection_at, customer_schedule_authorized, schedule_authorization_at and schedule_authorization_fingerprint. These fields are only ever filled in REVIEW_FIRST and are never invented in AUTOMATIC. Native or manual publishing always stays in the customer's hands.

## A2. What an Automatic scope must contain

The customer's own authorization words, who gave them, when, the permitted accounts, exact board IDs and sections, destination types and paths, image provider, model and resolution, generation budget and its period, looks per week, channels (Pinterest, blog, Instagram), schedule and time zone, an end date or "until I revoke it", and how products are supplied. If any item is missing, finish setup before turning on recurring production. Never invent permission or a budget. Save it as AUTOMATION_POLICY with a policy_id and version.

## A3. When something changes

A changed output (new image, edited copy, new time) loses its old fingerprint. Re-run the affected checks. In AUTOMATIC, record a new fingerprint automatically if it is still inside the saved scope. In REVIEW_FIRST, ask the customer again. A change of account, model, board, destination scope, budget or authorization needs setup authorization again. An expired or revoked policy cannot authorize anything new.

## A4. Spending

Before any paid image generation, check it against the saved budget and the approved model, and record the expected cost and then the actual cost. Reserve expected costs before submitting; count retries, failures and uncertain outcomes. This workflow ledger is not a hard provider account spending cap. In AUTOMATIC, showing the cost is information, not another approval stop. Never buy a subscription or upgrade, never switch model or provider quietly, never ask for new account permissions.

## A5. When something is missing or blocked

Record the affected item and the reason (error_code and notes), then carry on with any other work that does not depend on it. Only a sign-in, re-sign-in or security check needs the customer right away. Never get around a platform's approval or security step. AUTOMATIC product sourcing and destination creation belong to the saved tested operator. Missing access queues the affected item with a precise capability blocker. Product rows are the customer's job only when they chose that manual/mixed assignment. Follow 14_AUTOMATIC_EXECUTION_CONTRACT.txt.

## A6. No duplicates, ever

Before any create, schedule, upload, commit or post, save what you are about to do: write_attempt_id, the exact payload fingerprint, and write_outcome = pending. If the reply is lost or unclear, set write_outcome_unknown and look the object up through the publisher before doing anything else. Never repeat a create blindly. A new run reads the saved state before any outside action and resumes only the missing work. Reuse an existing valid IMAGE_ID instead of paying for a new image.

## A7. Scheduled is not published

scheduled means the publisher confirmed it is queued. customer_scheduled means the customer confirmed they queued it natively. published needs evidence it is live. verified needs the live image, link, board, disclosure and text checked against the approved version. Record verification_scope, verification_evidence and verified_at for each.

## A8. What "fully automated" means

Never call a setup fully automated or unattended until one separate scheduled run has completed its connected steps, saved its results, resumed safely and produced live posts that were checked. A saved prompt, a draft or a schedule is not that proof. Sign-in problems and security checks on outside accounts can still interrupt any run.

# PART B. THE STATE

The structured state is the source of truth. The markdown files (storefront-log.md, pin-tab.md, pin-drafts.md) are readable views made from it.

CLOUD mode: a Google Sheet named STOREFRONT_STATE with tabs AUTOMATION_POLICY, CAPABILITIES, LOOKS, PRODUCTS, IMAGES, PINS, BLOG, INSTAGRAM, LESSONS, RUNS, ERRORS. The PINS tab has a PULL column the customer can type in.
LOCAL or CREDIT-SAVING mode: a file named storefront-state.json with the same sections.

## Capability record

action, operator, service, account, access_method, terms_permission_evidence, tested_at, result, readback_evidence, scheduled_runtime_available, last_checked_at, error_code. Record publishing_permission_evidence separately from customer authorization.

## IDs

LOOK_ID, PIN_ID, PRODUCT_ID / ASIN, IMAGE_ID, PUBLISHER_POST_ID, BOARD_ID, RUN_ID

## Automation policy

Top level: AUTOMATION_MODE (AUTOMATIC or REVIEW_FIRST), AUTOMATION_POLICY.
Policy fields: policy_id, version, authorization_text, authorization_actor, authorized_at, permitted_accounts, boards_sections, destinations, provider, model, resolution, generation_budget, budget_period, budget_spent, channels, pace, schedules, timezone, end_condition, revoked_at, sourcing_method.

Authorization fields on every Pin, blog page and Instagram post: approval_actor (automation_policy or customer), approval_basis, policy_version, approved_at, qa_evidence, qa_passed, authorization_fingerprint. Keep schedule_authorization_fingerprint as the Pin's REVIEW_FIRST field.

## Look record

look_id, look_date, window, look_name, kind (outfit, theme list, roundup, ootd), board_id, board_name, products[], destination_type, destination_url, image_ids[], pin_ids[], blog_slug, instagram_post_id, status, created_at, updated_at, error_code, notes

## Product record

product_id, asin, short_name, description (the approved written description), color_variant, shape_cut, material (or "not asserted"), details, source (who supplied it and how), rights_evidence, affiliate_link, destination_path, intake_fingerprint, status, last_checked_at, notes

## Image record

image_id, look_id, pin_id, provider, model, resolution, prompt, prompt_fingerprint, job_id, input_reference_ids, input_rights, write_attempt_id, generation_attempt, attempt_history, expected_cost, actual_cost, raw_sha256, final_sha256, layout_version, asset_location, visual_qa_evidence, commercial_rights_recorded, status, created_at, notes

## Pin record

pin_id, look_id, image_id, title, description, alt_text, destination_url, board_id, board_name, board_url, board_public_verified, board_assignment_verified, board_verification_method, board_verified_at, disclosure_present, metadata_reviewed_at, scheduled_at, timezone, publisher, publisher_post_id, publisher_post_uuid, approval_actor, approval_basis, policy_version, approved_at, qa_evidence, qa_passed, authorization_fingerprint, customer_selected, customer_selection_at, customer_schedule_authorized, schedule_authorization_at, schedule_authorization_fingerprint, write_attempt_id, write_outcome, verification_scope, verification_evidence, verified_at, status, last_checked_at, error_code, pull_requested, notes

Keep publisher_post_uuid as well as publisher_post_id where the publisher gives both. An edit can replace the number; the UUID stays.

## Blog record (when BLOG HALF is on)

look_id, slug, json_sha256, image_sha256s, commit_id, deployment_id, live_url, approval fields, write_attempt_id, write_outcome, status, verified_at

## Instagram record (when INSTAGRAM is on)

post_id, look_id, ordered_image_ids, caption, account, format, ai_label, scheduled_at, publisher, publisher_post_id, publisher_post_uuid, approval fields, write_attempt_id, write_outcome, status, verified_at

## Lesson record (Outfit of the Day only)

lesson_id, lesson_title, lesson_date, look_id, status (sourcing, intake_needed, built, missed, dropped), idea_list, pin_ids[], notes

## Run record

run_id, task, work_window_key, claim_owner, claim_expires_at, last_heartbeat_at, started_at, finished_at, result, created_ids[], failed_ids[], retryable_ids[], notes

## Allowed status values

intake_needed, sourcing, missed, write_outcome_unknown, ready, building, built, queued, customer_review_required, awaiting_approval, customer_scheduling_required, scheduled, customer_scheduled, published, verified, pull_requested, pulled, pull_failed, failed, dropped

Use only these. Put the reason for a block in error_code and notes. Never invent a new status or combine two (for example, never "sourcing/intake_needed").

What some of them mean:
- sourcing: identifying the pieces of a look.
- intake_needed: an authorized product row is missing.
- missed: an unstarted Outfit of the Day lesson that fell outside the 14-day window. Record its date and the reason.
- queued: internal work waiting for its next step. It does NOT mean a publisher accepted a schedule.
- awaiting_approval: only when the platform itself requires a review or security step.

## Running one task at a time

Before production, claim the run: write task + work_window_key with an owner and an expiry time. If another active run owns the same window, reconcile it instead of starting a second one. If the state can't do a safe claim (for example a plain file edited by hand), run one task at a time and note that in the run record. An expired claim does not prove that its outside writes failed: check before taking over.

## Duplicate check order

1. LOOK_ID
2. PIN_ID
3. IMAGE_ID
4. PUBLISHER_POST_ID / UUID
5. a fingerprint of destination + board + scheduled time + title

If a match is found, reconcile it. Never create a second object.

## Status paths

CONNECTED PUBLISHING (Metricool):
AUTOMATIC: built → queued (all checks passed, inside the saved scope, fingerprint recorded) → awaiting_approval only if the platform requires it → scheduled → published → verified
REVIEW_FIRST: built → customer_review_required → queued (customer picked it and authorized its time) → scheduled → published → verified

NATIVE PINTEREST (customer schedules it):
customer_review_required (REVIEW_FIRST only) → customer_scheduling_required → customer_scheduled → published → verified

For Metricool, PENDING means the post is scheduled and waiting for its time. It does not mean review is needed. A Metricool post does not have to appear in Pinterest's own Scheduled Pins list before it publishes.

## Pulling a Pin

scheduled → pull_requested → pulled
published → pull_requested → pulled
pull_requested → pull_failed

Never mark a Pin pulled just because a publisher record disappeared. Deleting a Metricool record does not remove a Pin that is already live on Pinterest.

## The readable views

pin-tab.md: the publishing queue, by day.
storefront-log.md: looks, Outfit of the Day lessons and run history.
pin-drafts.md: every Pin's copy and image reference.
shopping-list.md: the agent's next sourcing queue in AUTOMATIC; customer assignments only for explicitly chosen manual steps.

PULL MARKS: the customer can ask to pull a Pin by typing PULL in its PULL column (CLOUD sheet) or next to it in pin-tab.md (LOCAL and manual). Every task, at its start and before it rewrites any readable view, copies every PULL mark into the state as pull_requested, so a mark is never lost when a view is rebuilt.
browser-lock.txt: LOCAL mode only, if you run browser steps on your own computer. Not used in CLOUD mode.
