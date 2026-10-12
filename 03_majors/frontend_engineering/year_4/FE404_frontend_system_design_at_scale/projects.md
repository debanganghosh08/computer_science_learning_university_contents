# FE404 · Labs and projects

Each project has two parts: a design document (requirements, estimates, architecture, data model and API, budgets, accessibility, internationalisation, failure handling, decision records) and a working implementation that proves the riskiest parts of the design. Every design is reviewed by classmates in the format of a real design review. The OT lab and every timed design are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Requirements and estimates | Turn 3 one-line prompts into written requirements, estimates and ADRs | Requirements sheets; bytes-and-requests estimates for each first screen | 3 h |
| 2 · Feed at scale | Virtualised mixed-height feed with live insertions, normalised entities and the APG feed pattern | Memory flat over 5,000 items; screen-reader script; no scroll jump on insertion | 6 h |
| 3 · Typeahead and forms | Station typeahead matching Hindi, English and transliterated queries; 40-field form with autosave and cross-device conflict detection | Match tests; autosave conflict test | 5 h |
| 4 · OT from scratch (no AI), then CRDT | Plain-text OT with a central server; the same editor on Yjs | Convergence fuzz: 10,000 random operations across 3 clients for each | 8 h |
| 5 · Offline sync | Two devices and a server syncing 10,000 records through a sync engine or CRDTs; conflict UX | Conflict test cases; sync-state UI; eviction survival | 6 h |
| 6 · Data layer | BFF for a 6-service home screen; normalised cache updates; a breaking API change with old clients | BFF design; cache update tests; migration plan | 4 h |
| 7 · Micro-frontends | Compose two independently deployed apps; then a modular monolith of the same features | Bytes, INP and deploy-independence comparison | 5 h |
| 8 · Governance | Governance model and component definition of done for 30 teams | Written model; adoption metric plan | 3 h |
| 9 · Indic and RTL | One screen correct in `en-IN`, `hi-IN`, `ta-IN` and `ur-IN`; pseudo-localisation in CI | Screenshots; CI catching a hard-coded string | 4 h |
| 10 · Reliability and privacy | Client-side SLOs, third-party policy, telemetry audit against DPDP Act principles, dashboard design | SLO document; minimised telemetry schema; dashboard mock-up | 5 h |

## Projects

### P1 · Feed design and proof of concept (L1, ~6 hours)

**Real-world inspiration:** "Design a news feed" is the most common frontend system design question. The feed here, a local-news app for Indian cities with posts in several languages, is an **illustrative scenario**.

**What to build:** a 4–6 page design document and a proof of concept of the riskiest part: virtualised rendering of mixed-height, mixed-language posts with images, live insertion of new posts, and optimistic likes.

**Acceptance criteria:**
- **Design document:** covers all rubric lines (requirements, estimates, architecture, data model and API, performance budget, accessibility, i18n, failure handling, trade-offs), with at least 3 ADRs.
- **Proof of concept:** LCP at most 2.5 s for the first post and INP at most 200 ms on like, on the FE304 baseline mobile profile.
- **Memory:** scrolling through 2,000 posts keeps heap growth under 20 MB.
- **Accessibility:** passes a screen-reader script using the APG feed pattern; a "load more" control exists.
- **Text:** Hindi and English posts render without clipped text or broken truncation.

**Stretch goals:** video autoplay rules with data saver; prefetch of the next page tuned by connection type.

**What it proves to an employer:** you can design and prove the most common senior frontend interview problem to a production standard.

### P2 · Offline-first field data app (L2, ~15 hours)

**Real-world inspiration:** community health and field workers often record data in places with weak or no connectivity, and then sync later. The app, a household-visit record tool for a health programme, is an **illustrative scenario** with synthetic data only.

**What to build:** an installable PWA with:
- local-first storage (IndexedDB or OPFS) of households, visits and follow-up tasks;
- sync through a sync engine or CRDTs to a server, with per-field conflict policies and a conflict-resolution screen;
- a visible sync state on every record, and encrypted local storage;
- schema migrations across two app versions, and a Hindi interface with an English toggle.

**Acceptance criteria:**
- **Offline:** with the network off, a scripted 7-day simulation (500 visits, 200 edits to shared households from two devices) completes with no errors and no lost data.
- **Sync:** after reconnection, 1,000 pending changes sync within 30 s on the FE304 baseline network; both devices and the server converge (checked automatically).
- **Conflicts:** all 12 provided conflict cases resolve according to your documented policy; cases needing a human appear on the conflict screen with both versions shown.
- **Storage:** total local storage under 50 MB for the simulated data set; the app survives a storage eviction by re-syncing, and tells the user.
- **Migration:** a version-2 schema change migrates local data on devices that were offline during the deploy.
- **Accessibility and device:** TalkBack walkthrough of recording a visit; works at 200% font scale on a low-cost Android phone.

**Stretch goals:** peer-to-peer sync between two nearby devices; a data-minimised export for supervisors.

**What it proves to an employer:** you can design data systems that work where networks fail, which is one of the hardest and most valued frontend architecture skills.

### P3 · Collaborative document editor (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Google Docs (operational transformation) and Figma (a server-authoritative, CRDT-inspired system) show two public approaches to multiplayer editing. Yjs and Automerge make CRDT-based collaboration available as open-source libraries.

**What to build:** a "Docs-lite" editor with:
- rich text (headings, bold, lists, links) built on Yjs or Automerge;
- live presence (cursors and selections with names), comments anchored to text, and per-user undo;
- offline editing with merge on reconnect;
- document permissions (owner, editor, commenter, viewer) enforced on the server, version history with restore, and a relay server with snapshots and compaction;
- Hindi, English and Urdu text in one document;
- a full design document, including why you chose this CRDT over OT, and a load-test report.

**Acceptance criteria:**
- **Convergence:** a fuzz test of 10,000 random concurrent operations (insert, delete, format, comment) across 3 clients with random network partitions always converges to identical documents. No interleaving anomalies appear in a provided concurrent-typing test.
- **Latency:** local echo is under 16 ms; remote edits appear within 150 ms at P95 on a local network and within 400 ms at P95 under the FE304 baseline network profile.
- **Scale:** the relay serves 50 concurrent editors on one document and 1,000 open documents on one instance without data loss (load-test evidence); snapshots keep document load time under 1 s for a document with 100,000 historical operations.
- **Offline:** a client offline for 30 minutes with 500 edits merges without losing either side's work.
- **Permissions:** commenters and viewers cannot change content through any message or API (tests at the server).
- **Text correctness:** cursor movement, selection and deletion are grapheme-correct in Devanagari and Tamil; Urdu paragraphs render right-to-left with correct bidirectional handling of embedded English.
- **Accessibility:** the editor is usable with NVDA (formatting announced, comments reachable), and other users' presence is announced politely.
- **Design review:** you defend the design for 20 minutes against examiner questions.

**Stretch goals:** suggestion (track-changes) mode; end-to-end encryption of document contents with server-blind relay; an AI writing assistant whose edits arrive as a separate, reviewable user (preview of FE403 and FE501).

**What it proves to an employer:** you can design, build and defend one of the hardest systems in frontend engineering, with correctness proven by tests rather than claimed.

## Feeds into

- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): your mock designs and P3 become interview material.
- [FE501 Frontier Seminar](../../year_5/FE501_frontier_seminar_multimodal_spatial_and_on/README.md): local-first and collaboration research.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): collaboration, offline-first and design-system capstones.
- The flagship [FE industry project](../../../../06_career_and_market_readiness/05_industry_projects/FE_frontend_engineering.md).
