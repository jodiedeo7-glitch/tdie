# Customer content dependencies

Derived general operations from the WYS master; no founder configuration or release approval. Original founder questionnaire unrecovered. The bundled question bank is the separately created replacement.

| Step | Required inputs | Result evidence |
| --- | --- | --- |
| Setup | Exact preferences, sources, private durable state | Intake followed by separate capability verification |
| Sourcing | Category brief, sourcing route, rights, real variants | Actual products, facts and authorized destinations |
| BASIC | Confirmed products and category styling | Overhead real-surface flat lay, distinguishable products, no generated text |
| STYLED | Accepted matching BASIC, same product facts | New category-specific scene with products in use, no person |
| LIFESTYLE | Accepted matching STYLED and authorized identity if selected | Different angle/framing/viewpoint, natural activity, product continuity |
| Graphics | Accepted photographs and approved copy | Separate labels/graphics, never generated lettering in photos |
| Blog | Actual destinations, disclosure, accepted images, approved article | Staged article, public page only after authorized verified publication |
| Pinterest | Actual public board, exact media/copy/link/disclosure/schedule | External ID and scheduling/publication readback |
| Instagram | Verified destination policy, required prior Pinterest result, approved content | External ID and scheduling/publication readback |
| Reconciliation | Saved intents, budgets, external IDs and receipts | Actual current status, exceptions, resumable next action |

Use category-specific presentation: clothes need believable volume, folds, seams and fabric. Home/dorm/car products need plausible placement and scale. Jewelry/beauty/perfume need actual shapes and factual feature handling. Books/gifts need accurate contents and suitability. One successful category never passes every category.

Separate linked products from styling extras. Never invent facts, prices, availability, preferences, affiliate status or income results. Verify destinations and disclosures. For no-persona customers, require a separately verified variant; never insert somebody else's identity.

Before attempts record profile revision, provider/model, prompt/reference hashes, dimensions, finite cost/attempt allowance and ownership. After attempts preserve request ID, cost/result, checksums, concrete acceptance/rejection and evidence. Budget approval is not output acceptance.

Production needs relevant-category visual evidence, real account/destination verification, duplicate prevention, resume/error behavior, first authorized publication and separate scheduled execution. Local fixtures and documentation do not establish these. Respect current holds.

## Session writer upgrade and checks

The session writer uses a POSIX OS lease. A live writer excludes another writer; process death releases the lease. The persistent `.write-lease` file is retained to keep every writer on the same inode. Platforms without `fcntl` fail closed. Windows and network-filesystem locking are unverified.

Stop all older session writers before upgrading. If an old `.lock` marker remains, the new writer reports `LEGACY_LOCK_RECONCILE_REQUIRED`. Reconcile the prior writer and saved state before removing that marker; never remove a lock just because it is old.

Run `python -m unittest discover -s tests -v` from the plugin root. These tests relocate the package and run the CLI with synthetic customer answers, verify complete intake and resume, retain all ten category briefs, exercise explicit correction and stale revisions, and kill a live writer before resuming. This verifies the packaged session script on the tested POSIX runtime. It does not verify installation in ChatGPT, durable remote storage, provider calls, customer delivery or publication.
