# TDIE Threads Router

**Scope:** `@nursemadedigital` only, with Jodie writing as herself. This router does not govern Premium DFY Content Calendar, the paid Instagram calendar, Skool Daily Prompts, or Pinterest.

**Sources checked (repo snapshot plus 1 October recovery/live audit):** `ops/cloud-kit/TDIE_THREADS_SYSTEM.md`, `ops/cloud-kit/TDIE_JODIE_THREADS_VOICE.md`, `ops/cloud-kit/JOB_THREADS_VIRAL_RESEARCH.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/canon/canon.json`, `ops/canon/TDIE_CANON.md`. The Threads system in the repo is explicitly a **copy** of a live Claude Project document and omits the live scheduled-task table. The 57-entry live task inventory and recovered 27 September rebuilt system are now included under ops/ai-router and ops/source-evidence. Source course PDFs were not needed to verify the already adopted live cadence. Before activating, Claude must reconcile these with the live Project, task list, account status, and platform behavior. No schedules or live rules have been changed by this patch.

## One writer, one account operator

- **ChatGPT | research + creative:** independently conduct source-backed account/post research; produce the evidence register; analyze what is observed vs creator-reported vs inferred; draft proposed changes for Jodie's approval; produce the complete weekly post bank, article replies and offer replies; validate voice, links, timing, duplication, claims and the handoff manifest. Do not pretend to have private Insights.
- **Claude | account operator:** automatically consume QA-passed `READY` batches under the established system without asking Jodie for per-batch approval, including the first pilot; check current account health and scheduled queue; hold the existing browser lock; schedule only authorized `READY` rows; verify each item from the account; publish/link self-replies only where supported and permitted; record observed URLs, status and exceptions. No research, creative rewrites or opportunistic posting while the browser is open.
- **Jodie | authority:** on 3 October 2026 at 18:25 Eastern, removed the approval requirement for routine founder Threads batches, including the first pilot. Schedule them automatically after QA under the established system. Changes to the governing schedule, profile/bio or offer rules still require explicit authorization; do not auto-adopt external course advice or research conclusions.
- **Code/QA:** validate the handoff CSV with `ops/scripts/validate_threads_manifest.py`; never use QA success as proof an item was published.

## Sequence

1. **Research, blind to the existing Threads rules.** Follow the original `JOB_THREADS_VIRAL_RESEARCH.md` research-first approach. Attempt 30 small/new creators; label all timelines VERIFIED, REPORTED, INFERRED, or UNAVAILABLE. Do not manufacture follower history or imply correlation establishes causation. Save `ACCOUNTS.csv`, `EVIDENCE.md`, `REPORT.md`, including counterexamples and limitations.
2. **Compare with the existing system only after research is saved.** Create `PROPOSED_THREADS_RULE_CHANGES.md` with KEEP/CHANGE/CUT and source-backed reasoning. The live writer and loader inspected 1 October both explicitly use the 27 September rebuild: 6/day, 42/week. Adopt that existing setting. The older uploaded 18/day copy is superseded; do not restore it. New strategic changes still require approval.
3. **Generate QA-passed weekly bank outside the browser.** Use the established system and Jodie's Threads voice file, not Tommy Kate voice. Confirm offers and URLs against current canon and live shop before marking the packet READY. Use existing week-file convention plus `threads-manifest.csv` and `qa.md`.
4. **Automatic routine batches, Jodie decision 3 October 2026.** The first pilot and later weekly batches under the established system require no manual approval. After research, editorial, factual and deterministic QA, set producer_state `QA_PASSED`, approval_state `NOT_REQUIRED`, and record this standing authorization in approval_basis. Claude schedules READY rows automatically after preflight. New strategic changes remain proposals requiring authorization. No approval for other workflows is changed. For legacy CSV validation, approval=`APPROVED` means standing authorization under this decision, never evidence of a per-batch review; parent status and each distinct reply status may become READY.
5. **Claude preflight.** Read live Project Threads rules, account status, scheduled queue, task schedule and browser-lock procedure. Resolve any mismatch once and hold rather than guessing. Check whether native scheduler, approved API or existing supported tool is more reliable; do not claim one exists without verifying it.
6. **Single operator execution.** Reserve the one-account browser lock before interacting. Reconcile existing scheduled items by date/time and content fingerprint. Never blindly duplicate posts. Schedule in bounded chunks with live read-back. A browser failure leaves unscheduled rows `READY` or `BLOCKED`, never `VERIFIED`.
7. **Replies are independent actions.** The 1 PM offer link reply is due immediately after its parent goes live; use a reply queue with parent URL. Article replies also require a verified parent and genuine article match. If scheduled replies are not natively supported, queue a separate allowed operation. Never mark a future reply completed just because the parent post is scheduled.
8. **Friday analytics.** Claude exports actual 7-day Insights and account-status evidence if available. ChatGPT reviews the observed results, including new followers per post where the platform supplies it. Do not attribute growth to a hook without supporting evidence.

## Existing documented rules preserved until approved change

- Six daily slots: 07:00 OPEN, 09:00 ASK, 11:00 TEACH, 13:00 OFFER, 15:00 PROOF or TAKE, 17:00 UPDATE Eastern. One offer/day; link in an immediate self-reply. At most one article reply/day under TEACH, queued for +60 minutes after parent; no article twice/week. TEACH may carry up to four numbered self-replies, each under 500 characters. Native queue capacity is documented as ~25, **not verified live**. If fewer slots are free than tomorrow's batch needs, stop and reconcile; do not overwrite.
- Under 500 characters; no URL in post body; no pasted URLs in comments on other accounts; no unsolicited DMs; no invented results, fake scarcity or fake testimonials; no em dashes; no faith content; no Tommy Kate/farmhouse/gamer references on Jodie's personal Threads account.
- Existing campaign overrides are date-scoped. For 1, 3 and 4 October 2026, the documented Weekend Ecosystem/Kit offer requires **approved launch copy** from the missing live Project document; HOLD these offer rows if that copy is unavailable. Never manufacture a deadline or extend an expired promotion.
- Genuine engagement is a human interaction, not a bulk engagement bot. Any outreach or reply must follow account and platform rules; this router does not authorize automated mass follows, comments or DMs.

## Critical safety rules

- The former Threads account was disabled after concurrent automations, per the repo. Enforce **one writer per live account**, not merely one writer per task. Do not let an unrelated task bypass the lock. If ownership is unknown, STOP.
- **Idempotency:** `account + local_date + local_time + content_hash` identifies a post. On retry, inspect the account before creating anything. Do not post a second copy because an earlier action timed out.
- **Status is evidence-based:** routine founder batches use `DRAFT -> QA_PASSED + approval_state NOT_REQUIRED -> READY -> SCHEDULED -> VERIFIED`, with `BLOCKED` for exceptions. Whichever assistant did the work (Claude, ChatGPT, Codex or any other) may assert `SCHEDULED/VERIFIED`, and only after observing live state. A post and its reply have distinct statuses.
- Source-of-truth: live account for actual posting state; live Claude Project for current Threads workflow until migrated; canon for product facts; this router governs task ownership only. If these disagree, flag and pause the affected action.

## Output contract

`ops/cloud-output/threads/<week-start>/`:
- `RESEARCH.md` and source-backed account evidence (for research weeks)
- `PROPOSED_THREADS_RULE_CHANGES.md` (only for system revisions)
- `threads-week-YYYY-MM-DD.md` (human-readable final copy)
- `threads-manifest.csv` (one row per parent post; distinct reply fields)
- `qa.md` (deterministic and editorial QA)
- `execution-log.csv` (Claude writes actual results, parent URLs, reply URLs, timestamps, failure reasons)
- `insights.md` (observed platform data, not estimates)

**Done means:** copy QA-passed and authorized under the standing system, all intended posts/replies individually accounted for, account status checked, no duplicates, all failed/blocked items visible. Writing a bank is not publishing it.
