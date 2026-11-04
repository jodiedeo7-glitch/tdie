## Migration preflight

NOT ACTIVATED. This file is an instruction packet, not a created or edited scheduled task.
Schedule intent: `CRON_TZ=America/New_York`. Run only in the exact Eastern window from the inspected existing schedule or approved packet. No new recurring time is assigned by this file. No computer-dependent execution before 7 AM Eastern; prepare early content slots in advance. Daily publisher intent is 8 AM Eastern, subject to current SOP 16 and DST read-back.

READ FIRST: `ops/canon/canon.json`, `ops/canon/TDIE_CANON.md`, `ops/TDIE_AI_ROUTER.md`, `ops/ai-router/EXECUTION_CONTRACT.md`, `ops/ai-router/SOURCE_REGISTER.json`, `ops/cloud-kit/CLAUDE_SOURCE_CHECK_RULE.md`, plus the exact workflow and packet named below. Missing live SOPs block the affected operation. Image work also reads `ops/cloud-kit/TDIE_IMAGE_GENERATION_MASTER.md`; Skool/Facebook copy requires the live posting system.

Voice: Jodie except Premium member calendar and TDIE Instagram, which use Tommy Kate. Paid client work uses that client's approved voice. No em dashes, invented prices/products/links, or income claims on Facebook/Instagram.

VERIFY: re-read the live object before claiming any account operation complete. For research/files, inspect the saved result and all required QA. Keep scheduled, published and delivered evidence separate.
REPORT: follow `ops/cloud-kit/CLAUDE_SOURCE_CHECK_RULE.md`; one factual success line when all checks passed, material exceptions only. Full deliverables are not shortened.

# Job: Threads research, weekly writing and QA | CHATGPT

Do not open a signed-in Threads browser as part of writing. Do not execute any scheduled posts.

1. Read `ops/ai-router/TDIE_THREADS_ROUTER.md` and the repo's source files named there. **For a research rebuild, finish and save the independent research first, before consulting existing content advice.** A new system requires source-backed observations, counts, counterexamples and Jodie's approval.
2. For a routine weekly bank, read the currently approved live Threads rules (or request a verified export if unavailable), `TDIE_JODIE_THREADS_VOICE.md`, the latest canon and live promotional overrides. Treat the 28 Sep repo snapshot as historical, not proof of today's active offers.
3. Receive the target week, approved slot schedule, verified offer rotation, live article index and latest platform metrics. If one is unavailable, mark the affected rows `BLOCKED` with pending approval; do not invent account facts.
4. Draft posts in Jodie's own voice, not Tommy Kate's. Use the current observed six-slot/day, 42/week rebuild; never restore the older uploaded 18/day copy. Write the first line last; use distinct hooks, truthful specifics and natural language. No em dashes, faith content, fake scarcity, earnings claims without source, URLs in bodies or product names outside the designated offer slot under the current rules.
5. Include exact approved offer names, current price where relevant, exact approved links **only in the corresponding reply field**. Flag 1/3/4 Oct Kit slots if approved Project copy is missing. Add an article reply only if the article actually exists and fits; cap at two per day and do not repeat the same article in a week under the current rules.
6. Produce both the approved weekly Markdown file and a CSV with the schema in `THREADS_MANIFEST_SCHEMA.md`. Generate stable `post_id` and `content_hash` values. Replies have their own independent `reply_status` and due time.
7. Run `python ops/scripts/validate_threads_manifest.py <manifest.csv>` and then editorial QA for voice, accuracy, claim sourcing, research relevance and campaign dates. Attach the results. Deterministic validation is necessary but not sufficient.
8. Hand off only `APPROVED`/`READY` rows to Claude. Do not edit Claude's scheduled tasks or mark anything posted. Route any browser failure back as a precise exception, not an invitation for Claude to rewrite the post.
