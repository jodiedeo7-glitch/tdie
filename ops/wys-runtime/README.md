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

## Authorized replacement intake

`intake-question-bank.json` maps required fields to their downstream steps. It contains no completed original questionnaire. Persist newly received answers immediately and retain their exact source. Recovered direct instructions use `source_kind: recovered_direct_instruction`, `answered_at: null`, and an accurate `recorded_at`; do not invent the historical answer time.

`prepare --scope visual_pilot` permits only private basic/styled/lifestyle/graphics inputs with all visual fields present. Publishing and sourcing cannot use that scope. The default production scope still requires complete setup. These guards require caller integration; they are not proof of live execution.

## Executable interview and resume

`intake.py next --profile PRIVATE_PATH` returns the first unanswered question. It starts with business direction and audience, then categories and sourcing route, visual signature, category-specific curation, persona, account/destination, channels, execution preferences, cadence and finite budget. Operator verification remains separate. Resolve existing exact customer evidence before asking each question; never prefill one customer's answers from another customer's brand.

`intake.py answer --profile PRIVATE_PATH --customer CUSTOMER_ID --question QUESTION_ID --answer-file PRIVATE_ANSWER_JSON --expected-revision REVISION` saves an answer immediately, reads it back, and returns the next question. Answer JSON contains the exact `value`, original `evidence`, and timezone-aware `answered_at`. Use `--kind founder` for an authorized founder replacement profile and `--kind fixture` only for explicitly synthetic tests. Customer data never goes in this public repo.

Raw question answers and aggregate curation/visual fields are written in the same atomic profile revision. Grouped answers retain per-component source evidence and all previous history. Blank answers and the interface's `No selection` are unanswered. No-persona skips only the persona-world question; it does not establish that the no-persona generation variant works. Completed preference intake reports `live_setup: NOT_VERIFIED`, not operational readiness.

## Recorded image rejections

`mini_test.py` reads `rejected-assets.json` before accepting a record. It rejects both failed Tommy Kate STYLED image checksums even if a later record contains PASS checkboxes. A missing or malformed rejection registry blocks acceptance. This is protection against reusing known rejected images; it does not independently judge garment volume, product fidelity or aesthetic quality, and it does not establish provider/caller integration. Both STYLED versions in the first private clothing test were rejected.
