# Threads manifest contract

One CSV row = one **parent post**. Optional offer/article replies are distinct operations with distinct statuses. CSV must be UTF-8. Use America/New_York local clock times with an explicit `timezone` column; no assumption that EDT remains in effect after the November DST change.

Columns:

`post_id,date,time,timezone,slot_type,body,hook_label,offer_name,reply_text,reply_due_time,article_reply_text,article_reply_due_time,source_urls,approval,status,reply_status,article_reply_status,content_hash`

- `post_id`: stable `YYYY-MM-DD_HHMM` (or suffixed ID if multiple approved posts share a time). Stable across retries.
- `date`: ISO date. `time`: 24-hour HH:MM local.
- `timezone`: `America/New_York`.
- `slot_type`: `MORNING`, `VIRAL`, `CONNECT`, `QUESTION`, `TEACH`, `OFFER`, `STANDALONE`, `GOODNIGHT`, or `SPOILER`.
- `body`: exact approved parent post; no URLs.
- `hook_label`: distinct named opener within the day if present, otherwise empty.
- `offer_name`: only on approved offer rows; exact canon product name.
- `reply_text`: full approved offer reply with link, if any. `reply_due_time`: `HH:MM` local.
- `article_reply_text`: optional educational self-reply with a verified live `/learn` URL. `article_reply_due_time`: optional local time.
- `source_urls`: semicolon-delimited research/claim sources; never a URL pasted into the body.
- `approval`: `PENDING`, `APPROVED`, or `REJECTED`.
- `status`: `DRAFT`, `QA_PASSED`, `APPROVED`, `READY`, `SCHEDULED`, `VERIFIED`, or `BLOCKED`.
- `reply_status` and `article_reply_status`: `NOT_REQUIRED`, `PENDING`, `READY`, `SCHEDULED`, `VERIFIED`, or `BLOCKED`.
- `content_hash`: SHA-256 hex digest of the exact UTF-8 `body`, lower-case; provides a repeatable fingerprint, not platform evidence.

A new row should not enter the execution queue until `approval=APPROVED`, `status=READY` and QA passes. The validator deliberately does not convert `READY` into `SCHEDULED` or `VERIFIED`.
