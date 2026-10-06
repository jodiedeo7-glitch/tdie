# Board setup live test, 6 October 2026

Scope: Steps 2 and 4 of `kit/02_SETUP_PROMPT.txt`, starting from branch `fix/wys-automatic-kit-audit-20261002` at `43e7e0294fe42107729d59f3c4a7dc83b8fa1fd6`. This is a bounded board test, not a full customer-flow or release pass. Customer account data and write receipts stay outside the distributable kit.

## Verified tests

- Read the authenticated official Pinterest saved-board inventory and three existing WYS board pages. Exact names and public URLs were visible; each of those three pages explicitly displayed Public board. The outfit specialty board displayed two sections, Fall and Halloween. The other two displayed no sections.
- Recovered the exact previously approved structure from the referenced setup conversation's visible recommendation and approval sequence. No board names were inferred from the curation profile.
- Verified connected Metricool brand identity and opened its official web editor using the existing Google sign-in. No password was entered.
- Metricool's official Pinterest board dropdown listed existing boards, including the three independently verified public boards. Its Add control opened a Create new board form with only a name field.
- An approved 53-character name was rejected with the visible provider error `Code: 400 - Name should be less than 50 characters`. No board-create pass was recorded for that submission. The form did not prevent submission in advance.
- Seven other missing approved names below 50 characters were created through that documented Metricool route. Each returned an exact numeric ID in the selected Board field, and all seven appeared in the board dropdown afterward. No post content or media was supplied, and Schedule remained disabled.
- Existing WYS board IDs were resolved by matching selected names to the actual numeric Board field. No test Pin was created to obtain an ID.
- Discarded the unsaved editor. Complete before/after scheduled-post readbacks for 6–20 October in America/New_York matched exactly: 42 returned records, including all returned copy, media, destination boards, dates and flags. No scheduled-post mutation was attempted. This comparison does not claim coverage outside that date range.
- Follow-up after the customer's explicit shorter-name approval: reconciled the live selector, then created and read back the three shorter equivalents. All ten approved core names now have exact Metricool IDs. The family-board first result was unclear; discarded the empty editor, reloaded the official planner and confirmed the exact name absent before one retry. The selector then listed all three new names, including one matching family name. The follow-up schedule comparison again matched all 42 complete returned records.
- Organization-board manual completion readback: the generic public-page reader failed, but the authenticated official browser opened the exact customer-returned URL. It displayed the expected board name, the full prepared description, an explicit Public board indicator and all four agreed sections with actual section links. A fresh reload returned the same board and section set. Saved owning-service text and screenshot evidence locally. This proves the bounded interactive readback in this account, not logged-out access, every client account or unattended scheduled access.

## Blockers and unverified work

- Resolved name-limit issue: the original 53-character name failed live; the 52- and 50-character names were initially held. The customer subsequently approved exact shorter equivalents, and all three were created with matching ID readbacks. No unapproved truncation or rename was used.
- Description and section editing were not exposed by Metricool's tested Add board form. Agreed sections remain pending. A name-only creation is not complete board setup.
- The organization board now has owning-service public-status, URL, description and four-section readback evidence. The other nine new boards still need their respective details and readbacks. Publisher availability is recorded separately.
- Direct Pinterest browser automation permission is unverified. The current Pinterest guidelines require explicit approval for automation; a working authenticated official UI is not sufficient evidence. The existing observations are recorded accurately, without certifying a permitted recurring native-browser route.
- The local interactive Metricool test does not prove cloud access or a separate scheduled run.
- The planner displayed a 20-post monthly allowance. This conflicts with the earlier customer intake answer of a paid plan; capacity must be reconciled before enabling the requested pace. No account upgrade or plan change was attempted.
- Prepared an account-specific completion packet with the ten exact names/IDs, copy-ready descriptions, unchanged section lists and current official Pinterest instructions. The next customer action is to complete details on one already-created board and return its actual URL. Prepared instructions and customer reports do not themselves pass the remaining live tests.

## Flow defects repaired in source

1. Board-name validation must precede submission, and an approved over-limit name needs a specific shorter-name decision.
2. Board setup must check the connected publisher's documented creation route before assigning manual work. It must record name creation, description editing, sections, public evidence and ID mapping independently, preserving completed writes when another capability is blocked.
3. The client-flow response ended with unresolved setup status instead of a concrete resolution. The customer explicitly rejected that behavior. The setup prompt and execution contract now require an authorized repair, an exact permission/choice question, or precise customer instructions, while independent work continues. This is a communication-flow repair; it is not evidence that the remaining board capabilities passed.
4. The follow-up assigned a direct Pinterest step without offering browser help versus manual completion. The customer required that choice and selected manual for the current board-details step to save credits. The prompt and contract now require the choice before a UI handoff, state any browser-access prerequisite and preserve the overall automation mode when a single step is manual. Remaining board details await the customer's result; this choice is not a live capability-test pass.
5. A generic reader error led to asking for customer confirmation instead of testing the explicitly requested official browser readback. The browser read succeeded and persisted after reload. The setup prompt now distinguishes reader failure from board failure, checks exact saved fields through the owning service and requires the same verification in each client's actual account.

Source changes do not certify PDFs, ZIP delivery, unattended operation or release readiness. This test does not rebuild or replace delivery artifacts.

## Sources checked

- [Metricool: Schedule and Post on Pinterest](https://help.metricool.com/schedule-and-post-on-pinterest-sbiz3), documents selecting or creating the destination board in Pinterest settings.
- [Pinterest community guidelines](https://policy.pinterest.com/en/community-guidelines), automation approval and supported-access rules.
- [Pinterest current Terms of Service](https://policy.pinterest.com/en/terms-of-service), automated-access permission. The announced November 2026 terms were not treated as already effective.
