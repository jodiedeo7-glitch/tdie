# WYS repository persistence incident, 9 October 2026

This is an incident record, not a new WYS operating authority, independent audit, or release approval. The current WYS master and founder restrictions still govern. This record covers evidence available in this session; it is not a reconstructed complete transcript.

## Founder instruction and current restrictions

The founder states that every step, conversation, and decision was required to be committed to this repository. She states that rules were installed to prevent this loss of continuity. Those statements must not be reduced to casual conversation or treated as a new preference.

The founder explicitly stopped self-review and review delegated to another OpenAI agent. That reviewer was interrupted. The founder rejected proceeding in Claude after the assistant opened a fresh Claude cloud-browser tab. No Claude audit was submitted. Do not resume either route based on this incident record.

The founder rejected being told to download and attach files that the assistant should attempt to handle. The assistant must verify actual access before claiming it can submit a handoff.

## Evidence checked against connected GitHub

On 9 October, the assistant read current default-branch canon and recent commits using the GitHub connector, and fetched the consolidation commit's actual diff.

- Current canon explicitly requires canon changes in the repository and project copies on the same day. Its Decision 99 records an earlier repository canon lag of twelve decisions. This is evidence of a prior continuity failure, not proof that every subsequent conversation was archived.
- Commit a51c2ef1d764b0bac0d0acc332ea82c06162f921 (7 October) consolidates WYS into one authority and removes superseded instruction files. Its diff was inspected. Historical deletion in a commit must not be confused with evidence that the complete conversation history was saved or that history cannot be recovered.
- Connected recent history contains WYS runtime work on 9 October: 9a77e3c3be1f7c8d5809146280a59a679f764be5, aa63fe0e9b959f7cb901d04cfeb4670393e93589, 7639e8170440c9739e99a99ab5bf47436d8fc07b, b6f0d86e329174965a1f369381a9bb928e81fad3, ff290f863d7be8e5a80f2ac720f659df5e0962d1, 32e6e0c387ee5f59a1d33f2a41317d17bc213bc4, 3fa9012819938ae14bd41dc60b96ac3df3bee150, and 402d4ed29995bcadfd26520ee40431e50018fa15.
- The local checkout HEAD was ec51d44b0acbab7d501dfe161e23957a96496eb1, older than connected default-branch runtime commits. Local untracked runtime status alone was therefore not evidence of missing remote runtime commits.
- A code search for WYS-Source-Only-Handoff returned no default-branch results. This search is not an exhaustive proof of absence across all branches.

## Work left outside this repository in this session

The assistant created these artifacts in the working environment and saved them as files, without completing a repository commit:

1. WYS-External-Audit-Packet-20261009.zip. Initial construction passed integrity checks, but a later local inspection found a truncated unreadable ZIP. Cause is UNVERIFIED. It was reconstructed as WYS-Audit-Review-Source-20261009.zip.
2. WYS-Audit-Review-Source-20261009.zip. Saved replacement and post-save CRC were checked. SHA256: d1b4a6df9f2592b5138cb73ff1a9447543ed80a01309518df635b8c93a799d64. The file is a confidential source snapshot, not a customer package or audit verdict.
3. WYS-Source-Only-Handoff.txt. Contains 26 verbatim source sections and no audit verdict. SHA256: a1a7b56267fa5cbcc661de2db7e245e7ccd46ca176292e448700293f0cdcc24a. It is a partial snapshot, not the entire project history, and does not embed images.
4. An initialized wys-storefront skill skeleton under the remote-skills working checkout. SKILL.md still contained TODO placeholders when inspected. The required skill git synchronization was not completed by this assistant in this session. It is not a completed plugin, customer installation, or verified distribution.
5. An isolated fix/wys-runtime-repair-20261009 local worktree was created. Creating a worktree did not commit or push a repair.

Private images, questionnaire answers, access details, and the source-only handoff have not been copied into the repository by this incident record. The record preserves their known provenance and limits without treating private evidence as a public customer deliverable.

## Missing or unverified evidence

- Complete original founder questionnaire and answers have not been recovered in this session.
- Complete verbatim project conversation history, especially original assistant turns, is not available in this session.
- Exact original rationale for the plugin refusal and external-browser/Higgsfield recommendations is not recovered. Later assistant explanations cannot substitute for that evidence.
- A complete numbered ledger proving the reported 86 problems and 12 fixes has not been located in the records examined here.
- No verified customer installation or full repeatable customer run is established by this record.
- Current account-level scheduled jobs, project-file parity, and live publication are not established by repository commits.

## What failed in this session

The assistant created handoffs and a skill skeleton without completing and verifying repository persistence, then handed file-transfer steps back to the founder. It continued to explain instead of resolving the requested independent-review route, and selected an OpenAI subagent that the founder rejected. These are recorded as execution failures; the existence of some runtime commits does not satisfy the requirement to preserve every conversation and decision.

This incident record preserves the currently known gap. It does not repair missing history, complete the plugin, establish an independent verdict, or clear the release hold.
