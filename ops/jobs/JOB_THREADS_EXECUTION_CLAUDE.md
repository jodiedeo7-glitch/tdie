## Migration preflight

NOT ACTIVATED. This file is an instruction packet, not a created or edited scheduled task.
Schedule intent: `CRON_TZ=America/New_York`. Run only in the exact Eastern window from the inspected existing schedule or approved packet. No new recurring time is assigned by this file. No computer-dependent execution before 7 AM Eastern; prepare early content slots in advance. Daily publisher intent is 8 AM Eastern, subject to current SOP 16 and DST read-back.

READ FIRST: `ops/canon/canon.json`, `ops/canon/TDIE_CANON.md`, `ops/TDIE_AI_ROUTER.md`, `ops/ai-router/EXECUTION_CONTRACT.md`, `ops/ai-router/SOURCE_REGISTER.json`, `ops/cloud-kit/CLAUDE_SOURCE_CHECK_RULE.md`, plus the exact workflow and packet named below. Missing live SOPs block the affected operation. Image work also reads `ops/cloud-kit/TDIE_IMAGE_GENERATION_MASTER.md`; Skool/Facebook copy requires the live posting system.

Voice: Jodie except Premium member calendar and TDIE Instagram, which use Tommy Kate. Paid client work uses that client's approved voice. No em dashes, invented prices/products/links, or income claims on Facebook/Instagram.

VERIFY: re-read the live object before claiming any account operation complete. For research/files, inspect the saved result and all required QA. Keep scheduled, published and delivered evidence separate.
REPORT: follow `ops/cloud-kit/CLAUDE_SOURCE_CHECK_RULE.md`; one factual success line when all checks passed, material exceptions only. Full deliverables are not shortened.

# Job: Threads scheduling, replies and read-back | CLAUDE

**Only run after Jodie approves the first rebuilt week and any governing system changes.** This is an execution job, not a content-generation job.

1. Read the current live Claude Project `TDIE_THREADS_SYSTEM.md`, browser-lock procedure and automation task schedule. Compare with the approved router and manifest. If a conflict affects posting, STOP that item and report it once.
2. Acquire the shared **account-level** browser lock before touching `@nursemadedigital`. Confirm no other scheduled task or human session is posting. Do not use a second browser session to bypass the lock.
3. Inspect Account Status and existing scheduled posts. Check remaining native scheduler capacity; the repo's ~25-slot figure is unverified. Compare `post_id`, timestamp and content fingerprint with existing posts before adding anything. Never double-post on a retry.
4. Schedule only the approved `READY` rows in bounded chunks. Preserve copy exactly. If scheduling is unsupported, hold the item. For a blank/frozen page, follow the browser fallback rule below before reporting failure. Do not silently publish immediately instead of scheduling.
5. Read back every scheduled item from the actual account view. Record its URL/ID when available, local and platform time, content fingerprint and observed status. Mark `VERIFIED` only when the relevant state is visible.
6. Publish the approved own-link OFFER reply immediately after the verified 13:00 parent exists. Keep the single daily article reply at +60 minutes after its verified parent, never reuse an article within a week. Check whether the platform can schedule replies; otherwise use a separate authorized operation or leave it pending. Apply the same rule to article replies. No pasted links on other people's posts, no unsolicited DMs and no bulk automated engagement.
7. Release the lock according to the live lock SOP, including after errors. Save `execution-log.csv` with all rows and distinct reply statuses; report exceptions and outstanding work without claiming completion.
8. On Friday, if authorized, capture real 7-day Insights and recommendation eligibility; hand the observed metrics to ChatGPT. Do not fabricate metrics or infer why a post grew.

Never update canon from an unverified UI state. Never edit product prices, bio or offer rotation without explicit approval.

## Browser recovery boundary
Do not bypass an account warning, approval, unknown lock owner or unsupported platform action. Recover UI/session failures within the held lock. The following legacy fallback applies to an operator with those tools; it does not assert those browsers or SendUserMessage exist in another runtime. Use the verified equivalent route and ordinary failure report when unavailable. Never claim unavailable tools were tried.

BROWSER FALLBACK RULE (standing instruction from Jodie, added 27 Sep 2026; overrides any earlier line in this prompt that says to stop the moment a browser, tab or sign-in problem appears):
If a tab freezes, a site isn't signed in, a control stops responding, or the browser otherwise won't cooperate, do not stop or report yet.
1. Try every other route first: switch browsers (her Chrome via Claude in Chrome <-> the built-in browser in the Claude desktop app, in either direction, whichever this prompt named first), open a fresh tab, and check whether the other browser is already signed in to the site. Never type a password.
2. If every route is exhausted, try all likely fixes and resets: reload the page, close and reopen the tab, wait 30 to 60 seconds and retry, clear the stuck state (close any open composer or modal, discard only drafts this run created), and reconnect or re-select the browser.
3. Only then give Jodie a fail notice through SendUserMessage: what failed, what you tried, and her exact numbered next steps (for example: open Chrome, sign in to X, then re-run this task). Keep the browser lock and reporting rules above.
