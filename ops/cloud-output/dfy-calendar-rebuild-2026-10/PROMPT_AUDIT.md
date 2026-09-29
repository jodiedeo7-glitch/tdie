# OCTOBER DFY CONTENT CALENDAR PROMPT AUDIT

Date: 29 September 2026
Scope: Premium Monthly DFY Content Calendar only.

## Findings

### 1. Personal image workflow leaked into calendar production
The general image master contains a standing vendor sequence for Jodie's own work. That sequence was capable of being inherited by a calendar task even though the Premium Calendar is a member-facing product.

Impact: members could be told to use tools they do not own, and calendar production could optimize for Jodie's workflow instead of the creative result.

Fix: calendar-specific production rules now explicitly override vendor choice. Prompts are model-agnostic. Nano Banana Pro is optional only.

### 2. Reel output was underspecified
The prior creation prompt required a start frame and a motion prompt but did not enforce two complete production methods.

Impact: a Reel could ship with one workflow only, making the product less useful across tools.

Fix: every Reel now requires:
- Version A, one-step video + exact on-screen text
- Version B, two-step video-only generation + separate editor text instructions

The two versions must describe the same concept.

### 3. The two-step text boundary was not enforced
Without a hard rule, actual overlay copy could be inserted into a video-only prompt.

Fix: QA now rejects any two-step video prompt containing the actual overlay wording. The text lives in a separate editor block.

### 4. The calendar deliverable was incomplete
The site and membership copy promise 31 Instagram days, 62 Threads posts, and a start-frame and motion prompt for every Reel.

The prior creation prompt explicitly covered 31 days and Reel prompts but did not require the 62 Threads posts.

Fix: creation now requires exactly 31 Instagram days and exactly 62 Threads posts.

### 5. Research evidence was too weakly defined
The prior research prompt said to collect 40 outliers but did not define what evidence was strong enough to call a post an outlier.

Impact: a post with a large raw view count could be mistaken for an account-relative outlier.

Fix: research now distinguishes:
- qualifying outlier
- observed high-performer candidate

A qualifying outlier needs an account-relative evidence basis. Candidates do not count toward the 40-row gate.

### 6. Research lacked an explicit stop gate
The prior process did not force a stop when the evidence threshold was not actually met.

Fix: the research prompt now stops with PARTIAL status when 40 qualifying outliers from 25 qualifying accounts cannot be demonstrated.

### 7. Pattern extraction did not require row-level traceability
The prior research prompt required pattern counts but did not make supporting row IDs mandatory for every rule.

Fix: every research-derived build rule must cite supporting research row IDs.

### 8. Competitor tactics could be copied as if they were TDIE rules
A competitor's raw link, earnings claim, faith framing, or aggressive comment CTA could be mistaken for a recommended tactic.

Fix: research now separates observed patterns from non-replicable patterns. Competitor behavior is evidence, not permission.

### 9. Creation prompt did not fully restate current offer/link constraints
The old creation prompt did not enforce the complete current spread and Instagram link rules.

Fix: current canon spread rules and Meta link rules are explicit in the creation prompt and production rules.

### 10. No explicit no-copy safeguard
The old prompt could encourage trend replication without defining what "replication" means.

Fix: research extracts mechanisms and structures only. Calendar copy must be original TDIE wording.

## Result

The research prompt is now evidence-gated and traceable.
The creation prompt is now schema-gated and platform-aware.
The calendar-specific production rules prevent Jodie's private image workflow from leaking into the member product.
