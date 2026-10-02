# Scheduled task audit install, Fri 2 Oct 2026 (Eastern)

Note for `claude/TDIE_SCHEDULED_TASK_UPDATES.md` (the project file could not be reached from the cloud session that ran this, so the note is kept here too).

## 2 Oct 2026, scheduled task audit install (cloud session, about 3:00 am ET)

- Before-state: `claude-task-before-state-2026-10-02.md` plus `claude-task-before-state-addendum-2026-10-02.md` (TDIE Handoffs; the addendum holds the 4 tasks created after 05:13 UTC and the current versions of the Deadline watcher, Storefront launch scheduling and Storefront presale open check).
- Deleted 9 finished or expired tasks: trig_01T3tCSUPM2gmLfejsQ5sFT8, trig_014yK1n9evonzxeAUHYJC2yu, trig_01ArzeZdW1zXhJ3g2m6gRVx6, trig_017FVB1bt632m51VjuHjXdc7, trig_01NytGaxwQxcK1jDLZnqtjDg, trig_016cJpnUkEn2qFKWPADv6uyp, trig_01C2NRJdaYXiso6ujocN6ZdG, trig_01TUtZoK3NqUeHhWQjtqi4Fs, trig_01F6oCmn4yiWQJhKka6KhhN2. Kept trig_01Xip6E91Qtcy9uzAoDa3fZs: its last update (05:43 UTC, the one-shot firing) is after 05:13 UTC, so the hard guard left it. It is off and already fired.
- New prompt and model saved and read back (sha256 match) on 3 tasks: trig_019yn2AGsPQocy8gAdaN3oaA (Sunday Threads writer, now claude-opus-5-5), trig_015pm3AJSAmxnrX9wrkSceZo (Skool hot-thread check), trig_015Tcpp8qjBBWSNPywuYjNP2 (Daily missed-run sweep, now claude-sonnet-5-5 and switched on).
- 35 tasks were refused with `needs_device_approval` (bound to computer A5): nothing changed on them, including their models. The exact prompts and models are in `pending-a5.json` and `prompts/` next to this note. They must be approved from a Cowork conversation linked to A5.
- Nightly Brand Closet OOTD pins (trig_017tQcAgu8D9LxjG3MEmNXx3) is still off: its new prompt is waiting on A5 approval, and the switch-on call was denied by the cloud session's permission check.
- Left as they are: trig_019SZFfcJ4ArVwepS9eNyD4x, trig_01XGkTP8Q6XKbj7CuVKnJVc3, trig_01ShjfkWrwxzvhUdo2FE9xnd (edited by another chat after 05:13 UTC), trig_01BSsCCVU5ormYEqk5AMXdov, trig_01UVvrt82tcq43FeBgr6wb11 and the two Storefront Threads link comment tasks.
- Created trig_015HEgWR51VUG2WKhSUvWoex: run once Sun 4 Oct 2026 1:30 pm ET (2026-10-04T17:30:00Z), claude-sonnet-5-5, deletes trig_01QQFUrusBVMJYeSXxh5915i after a SUCCEEDED run that day. It was created with no connectors; whether the fired session has the scheduled-task tools is UNVERIFIED.
- Every prompt that uses a browser now ends with the BROWSER FALLBACK RULE block exactly once (the block was moved to the end where later sections followed it).
- Receipt: `claude-batch-install-receipt-20261002T070624Z.json`.
