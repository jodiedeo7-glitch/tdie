# BRAND_CLOSET queue

Scope: BRAND_CLOSET_OOTD. Template only; no real pending items or active task is established here. Read ops/TDIE_AI_ROUTER.md and ops/ai-router/EXECUTION_CONTRACT.md.

Each authorized item records task ID, exact source packet, account, asset paths, dependencies, approval, requested local time, prior observed state, exact operation, independent verification and rollback. Maintain operation state separately in the approved manifest. Inspect live state before retry; no duplicate writers. Keep internal/customer/client data isolated.
