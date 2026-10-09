---
name: wys-storefront
description: Guide While-You-Sleep Storefront setup with resumable customer preferences and source-backed operation records. Use for WYS setup, themed shopping edits, BASIC/STYLED/LIFESTYLE preparation, or resuming a WYS session. Keep founder work, customer work, and unrelated TDIE products separate.
---

# While-You-Sleep Storefront

Treat this version as a development implementation. Installation does not establish that generation, publication, scheduling, delivery or independent review passed.

## Establish authority and customer

For founder work, read current AGENTS.md and the full claude/WYS_REFERENCE_PACK_2026-10-07.md in jodiedeo7-glitch/tdie before acting. Respect the current release hold and generation pause. Historical archives are evidence, never current instructions.

For customer work, use the customer's authorized policy and private saved profile. Never transfer founder identity, affiliate tags, boards, pets, home, task IDs, imagery, prices or permissions. Read references/workflow.md before content preparation.

Use existing exact answers and evidence first. The bundled question bank is a replacement, not the recovered original questionnaire. Never invent missing answers, original timestamps or source messages. Do not ask the customer to gather material available through authorized tools.

## Guide setup and save immediately

Use scripts/session.py and references/question-bank.json. Present one missing topic, its guided choices and downstream use. Allow specific custom detail. Show category branches only for selected categories. Resolve existing exact evidence before asking.

Run commands relative to this skill directory. Create PRIVATE_PATH outside public repositories:

```bash
python scripts/session.py init --state PRIVATE_PATH --customer CUSTOMER_ID
python scripts/session.py next --state PRIVATE_PATH
python scripts/session.py answer --state PRIVATE_PATH --question QUESTION_ID --input PRIVATE_ANSWER_FILE --revision REVISION
python scripts/session.py status --state PRIVATE_PATH
```

Each answer envelope contains value, evidence, and timezone-aware answered_at. Value contains selected (choice strings) and detail (exact customer wording). Category preferences additionally use value.categories, with each selected category mapping each branch ID to selected/detail. Budget values need period and max_attempts_per_role; paid routes additionally need per_look_limit, period_limit and unit.

For recovered direct instructions with unknown original dates, use source_kind recovered_direct_instruction, answered_at null, and accurate recorded_at. Never pretend today's capture time is the original answer time.

Save and read back each confirmed answer immediately with the current revision. Use --correction only for explicit customer corrections. Continue at the next unanswered topic. No-persona skips only persona-world intake; it does not establish a working no-persona output variant.

Record every consequential decision, operation, rejection, error, approval and result as an event with original source evidence:

```bash
python scripts/session.py event --state PRIVATE_PATH --input PRIVATE_EVENT_FILE --revision REVISION
```

An event envelope uses value, evidence and answered_at. Include actual external IDs, precise status, payload fingerprint and timestamps in value when relevant. This script does not automatically capture conversations: the operator must call it. Preserve available raw messages separately with source IDs and fidelity limits; summaries never replace originals.

Save changed state using the environment's durable private-file mechanism and retain the same file identity/version. Scratch files, browser local storage and chat memory alone do not establish durable storage. Commit only authorized code and non-sensitive verification records to public repositories.

## Verify real capabilities separately

Completed preferences mean intake recorded only. Verify real account path, destinations, disclosures, reference rights, provider/model, finite budget, connected tools, durable state and step ownership. A selected provider is not a connected account. Verify changing platform claims against authoritative current sources.

Require independently recorded acceptance and explicit release clearance before customer distribution or activation. Do not conduct the independent audit yourself or represent another OpenAI agent as independent after the user rejects that route.

## Continue authorized work

Follow references/workflow.md. Reload private state before every operation. Apply exact customer answers and account-specific verified configuration. Finish independent preparation when dependent operations are blocked.

Use supported connected tools. Do not default to Higgsfield, native generation or a browser. Persist a finite cost/attempt reservation before paid attempts; failed and uncertain attempts count. Reconcile uncertain external writes before retrying.

Inspect actual outputs and preserve rejections. A rejected STYLED image cannot authorize LIFESTYLE. Instruction compliance, hashes and script fixtures do not prove image acceptance or live operation. Keep one writer per destination; inspect existing records before creating or scheduling; read back each real write. Distinguish prepared, submitted, scheduled, published and delivered.

Continue until the authorized task is complete or an actual access/input/permission boundary requires the user. Report the result or that exact boundary, not another plan or admission.
