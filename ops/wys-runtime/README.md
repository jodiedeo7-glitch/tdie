# WYS persistence and acceptance components

Authority: [WYS master](../../claude/WYS_REFERENCE_PACK_2026-10-07.md), including section 27. This directory supplies mechanical checks, not another workflow or a delivered customer product.

Run the component tests:

```bash
python -m unittest discover -s ops/wys-runtime -p 'test_*.py' -v
```

Private state belongs outside this public repository. `profile.py save` merges each original answer immediately, using customer identity and expected revision. Each answer has `value`, `evidence` and timezone-aware `answered_at`. Partial interviews remain durable but cannot prepare generation inputs. Never supply synthetic answers for a real customer. `prepare` reloads all answers for each operation and binds the current profile/master hashes; `verify` requires exact per-field application evidence. It reports input binding only, never external execution or image acceptance.

`mini_test.py` reads category slugs from the actual site category source. `blank_suite` initializes every category as NOT_RUN. `batch_gate` requires that category's complete matching mini-test record and three separate assets with checksums and actual visual-review evidence. Fixture acceptance cannot enable production. Checks are recorded operator evidence; software does not independently prove the truth of a visual review. Live publication and scheduled execution remain separately unverified.

`spend.py reserve` persists a write intent and conservative cost reservation before submission. Existing or uncertain attempts block resubmission; failed attempts still count. Results require service evidence. Changing a provider/model/policy requires reconciliation. Zero provider credits per attempt still requires a finite attempt limit. This component does not call a generation provider.

Integration status: local components tested; no production adapter or scheduled task has been shown to invoke them. Native in-chat generation is the founder's requested mini-test route. No Higgsfield call or credit spend occurred in this repair. The original completed founder questionnaire remains unrecovered; actual category image tests have not run. Do not label the system working from these component results.
