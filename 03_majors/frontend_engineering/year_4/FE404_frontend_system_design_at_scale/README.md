# FE404 · Frontend System Design at Scale

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [FE304](../../year_3/FE304_browser_internals_and_web_performance/README.md) (and in practice [FE302](../../year_3/FE302_react_and_component_architecture/README.md), [FE303](../../year_3/FE303_css_design_systems_and_accessibility/README.md), [FE401](../FE401_full_stack_frameworks_rendering_data_fetching/README.md)) | [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [FE501](../../year_5/FE501_frontier_seminar_multimodal_spatial_and_on/README.md) |

Part of the [Frontend Engineering major](../../README.md). This is the senior course of the major. It pulls together performance (FE304), components and state (FE302), design systems and accessibility (FE303), and rendering and caching (FE401) into design decisions for large products and large teams. It uses the replication and consistency ideas of [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md); backend-side scale is in [SWE401](../../../software_engineering/year_4/SWE401_large_scale_system_design/README.md).

## Why this course matters now

Senior frontend interviews include a frontend system design round: design a news feed, a collaborative editor or a design system, covering rendering strategy, caching, performance budgets and accessibility (see the [FE market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md)). The work behind that round is real and visible in public engineering writing:
- Google Docs built real-time collaboration on operational transformation (2010).
- Figma described a server-authoritative multiplayer system inspired by CRDTs (2019).
- The local-first movement (Ink & Switch, 2019) has since produced CRDT libraries such as Yjs and Automerge 3, and new algorithms such as Eg-walker and Fugue.

Large organisations split frontends across teams with modular monoliths or micro-frontends, and they pay for it in duplicated dependencies and version skew. In India the design must also hold up across a mostly-mobile, mostly-Android audience, many languages and scripts, and patchy connectivity. Coding agents can scaffold any one of these pieces. Choosing between them, writing down the trade-offs and defending them in a review is the senior skill, and it is the hardest part of the job to automate.

## Learning outcomes

By the end you can:

1. **Run** a frontend system design end to end: clarify requirements, set non-functional targets (performance budget, accessibility, i18n, offline), propose an architecture, define the data model and interfaces, and optimise. **Write** it up as a design document with decision records.
2. **Design** feeds, typeahead search, large forms and media-heavy pages that meet Core Web Vitals on a low-end Android baseline.
3. **Compare** operational transformation and CRDTs, and **build** real-time collaboration with presence, offline edits and undo.
4. **Architect** offline-first apps with service workers, IndexedDB or OPFS, sync engines and explicit conflict handling.
5. **Design** the client data layer and API contracts (BFF, REST, GraphQL, real-time), including normalised caches and schema evolution.
6. **Decide** between monolith, modular monolith and micro-frontends for an organisation, and **govern** a design system across many teams.
7. **Internationalise** for many locales, including Indic scripts, transliteration and right-to-left languages, with correct formatting and fonts.
8. **Plan** reliability, security, privacy (India's DPDP Act 2023) and observability for a frontend used by millions.

## Chapters and lessons

### Chapter 1 · The frontend system design method (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Requirements | Functional scope, users and devices, non-functional targets: budgets, accessibility level, languages, offline, SEO | Turn a one-line prompt ("design a social media feed") into 12 written requirements |
| 1.2 A repeatable structure | Requirements, architecture, data model, interface (API), optimisations (GreatFrontEnd's RADIO framework is one public version) | Run the structure on a small problem in 30 minutes |
| 1.3 Estimating | Payload sizes, images per screen, update rates, device memory, network round trips on the FE304 baseline | Estimate bytes and requests for the first screen of a feed |
| 1.4 Writing decisions | Architecture decision records, alternatives considered, reversibility | Write 3 ADRs for a past project |

**Check your understanding:** Which requirement most changes a frontend design: device class, offline, or number of languages? Why do estimates matter even when they are rough? What makes a decision record useful a year later?

### Chapter 2 · Feeds and infinite lists (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Pagination | Cursor vs offset, deduplication, insertion of new items, gaps | Design the client contract for a feed with live insertions |
| 2.2 Rendering at scale | Virtualisation, `content-visibility`, image and video lazy loading without lazy-loading the LCP item | Render 5,000 mixed-height posts with stable memory |
| 2.3 Interactions | Optimistic likes and comments, normalised entities so a like updates everywhere | One like updates the feed, the profile and the notification count |
| 2.4 Accessibility | The APG feed pattern, "load more" vs infinite scroll, keyboard and screen-reader navigation, focus preservation | Make the feed pass a screen-reader script |
| 2.5 Media | Adaptive images and video, autoplay policies, data saver, prefetching the next items | Design a media budget for a 9 Mbps, 100 ms RTT user |

**Check your understanding:** Why does offset pagination break when new posts arrive? What does infinite scroll take away from keyboard and screen-reader users, and how do you give it back? Why normalise entities in a feed client?

### Chapter 3 · Search, typeahead and large forms (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Typeahead | Debounce vs throttle, cancellation, client caching, prefix tries for local data, ranking on the server | Design typeahead for 8,000 railway stations used by millions daily |
| 3.2 Mixed-language queries | Transliteration and Hinglish queries, spelling tolerance, script normalisation | Match "dilli", "Delhi" and "दिल्ली" to one result |
| 3.3 Large forms | Multi-step flows, autosave, draft recovery, validation shared with the server, accessibility of errors | Design a 40-field application with autosave and resume |
| 3.4 Results pages | Filters in the URL, faceting, sorting, back-button behaviour, SEO | Design a results page that survives reload, share and back |

**Check your understanding:** Where should ranking happen, and why not on the client? How do you keep autosave from overwriting a newer draft from another device? Which form state belongs in the URL?

### Chapter 4 · Real-time collaboration (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The problem | Concurrent edits, intention preservation, convergence; why "last write wins" loses work | Show lost edits with two clients and last-write-wins |
| 4.2 Operational transformation | Transform functions, a central server, why Google Docs used it | Implement OT for plain-text insert and delete with a server |
| 4.3 CRDTs | State-based vs operation-based, sequence CRDTs (YATA in Yjs, RGA), Fugue's interleaving fix, Eg-walker; Automerge 3 | Build the same editor on Yjs; test convergence under random concurrent edits |
| 4.4 Rich text and structure | Peritext for formatting, trees and moves, comments anchored to text | Add bold and comments that survive concurrent edits |
| 4.5 Presence and undo | Cursors and selections, awareness, per-user undo in collaborative documents | Per-user undo that does not undo another user's typing |
| 4.6 Server and persistence | Relay servers, snapshots and compaction, authorisation per document, history | Design storage and permissions for 1 million documents |

**Check your understanding:** Why does OT usually need a central server and CRDTs do not? What is the interleaving problem, and why does it matter to users? What does "undo" mean when two people edited the same paragraph?

### Chapter 5 · Offline-first and sync engines (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Local-first principles | Data on the device first, sync as a background process; the seven ideals from Ink & Switch | Score 3 apps you use against the ideals |
| 5.2 Storage | IndexedDB, OPFS (widely available September 2025), quotas, eviction, persistence requests, encryption at rest | Store 10,000 records; measure read/write and survive eviction |
| 5.3 Sync | Change logs, version vectors, sync engines (Replicache/Zero, ElectricSQL), CRDT-based sync | Sync records between two devices and a server with conflicts |
| 5.4 Conflicts and UX | Automatic merge vs user resolution, showing sync state, stale-data labels | Design conflict UX for two health workers editing one record |
| 5.5 App updates offline | Service worker versioning, schema migrations of local data, kill switches | Migrate local data across two app versions safely |

**Check your understanding:** Why is offline-first a data-model decision, not a caching decision? What should a user see when their changes have not synced for two days? What breaks when an app's local schema changes while users are offline?

### Chapter 6 · The client data layer and API contracts (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Backend for frontend | Aggregation, shaping responses per screen, owning the BFF as a frontend team | Design a BFF for a home screen that needs 6 services |
| 6.2 REST, GraphQL, RPC | Over- and under-fetching, persisted queries, type-safe RPC (tRPC-style), caching implications | Choose a protocol for 3 products and defend each |
| 6.3 Normalised caches | Entity caches vs per-query caches, cache updates after mutations, garbage collection | Design cache updates for a "rename project" mutation |
| 6.4 Real-time channels | Polling, SSE, WebSockets; fan-out cost; mobile battery and reconnection | Design live order tracking for a food-delivery app (illustrative) |
| 6.5 Contract evolution | Versioning, additive changes, typed clients from schemas (FE301 P3), deprecations | Plan a breaking change with old mobile web clients still in use |

**Check your understanding:** When does a BFF become a bottleneck? Why do GraphQL clients often need normalised caches? What does a long-lived old client force on your API design?

### Chapter 7 · Large-scale architecture (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Modular monoliths | One deployable, many modules with enforced boundaries; monorepo tooling (FE305) | Split an app into modules with lint-enforced boundaries |
| 7.2 Micro-frontends | Build-time vs run-time composition, Module Federation, single-spa, iframes, edge composition | Compose two independently deployed apps on one page |
| 7.3 The costs | Duplicate frameworks and dependencies, version skew, shared state, inconsistent UX, performance budgets per team | Measure the bytes and INP cost of a micro-frontend split |
| 7.4 Organisation fit | Conway's law, team topologies, ownership of routes and shared shell | Recommend an architecture for a 40-team organisation and for a 6-team one |

**Check your understanding:** What problem do micro-frontends solve, and is it technical or organisational? How do you stop five copies of React from shipping? When is a modular monolith the better answer?

### Chapter 8 · Design-system governance at scale (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Operating models | Central, federated and hybrid teams; contribution and review; support channels | Write a governance model for 30 product teams |
| 8.2 Adoption and change | Adoption metrics (component coverage, detached overrides), versioning, codemods, deprecation windows | Plan a major version rollout across 30 apps |
| 8.3 Quality at the source | Accessibility certification per component, visual regression, token linting, performance budgets per component | Define a component's "definition of done" |
| 8.4 Public examples | GOV.UK Design System, India's UX4G (Design System 3.0, GIGW 3.0 aligned), GitHub Primer | Compare their contribution and support models |

**Check your understanding:** Why do design systems fail even when the components are good? How do you measure real adoption? Who should approve a new component, and how fast?

### Chapter 9 · Internationalisation and localisation (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Messages | ICU MessageFormat, plurals and gender from CLDR, no string concatenation, context for translators | Externalise a 50-string app with correct plurals in Hindi and English |
| 9.2 Formatting | `Intl` dates, numbers (`en-IN` lakh/crore grouping), currencies, relative time, lists; time zones (IST) | Format the same values for `en-IN`, `hi-IN`, `ta-IN` and `ur-IN` |
| 9.3 Indic scripts | Grapheme clusters and `Intl.Segmenter`, shaping (HarfBuzz), conjuncts, line height, font subsetting per script, input methods | Fix cursor movement, truncation and line-breaking in Devanagari and Tamil |
| 9.4 Right-to-left | Urdu and Arabic: `dir`, logical properties, bidirectional isolation of mixed text and numbers, mirrored icons | Make one screen correct in Urdu with mixed English product names |
| 9.5 Workflow | Pseudo-localisation, translation management, machine translation with human review (Bhashini, LLMs), quality checks in CI | Add pseudo-localisation and a missing-translation check to CI |

**Check your understanding:** Why is "Hello, " + name a bug? What breaks when you truncate Hindi text by code units? How do you get machine translation into production safely?

### Chapter 10 · Reliability, security, privacy and observability (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Frontend reliability | Error budgets for client errors, graceful degradation, feature flags, staged rollouts, kill switches | Define SLOs for a checkout flow's client side |
| 10.2 Security at scale | CSP and Trusted Types across many teams, Subresource Integrity, third-party script governance, supply chain (FE305) | Write a third-party script policy with an approval process |
| 10.3 Privacy | India's Digital Personal Data Protection Act 2023: consent, purpose limitation, data minimisation in analytics and logs; consent UX | Audit an app's telemetry for personal data; minimise it |
| 10.4 Observability | RUM by route, device and version; error grouping; session replay and its privacy risks; tracing to the backend | Design a dashboard a director and an on-call engineer would both use |

**Check your understanding:** What does an error budget mean for a frontend team? Why is session replay a privacy risk, and what controls make it acceptable? Who in a 40-team organisation owns a third-party script?

### Chapter 11 · Design reviews and interviews (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Running a design review | Presenting trade-offs, inviting challenge, recording decisions | Review a classmate's P3 design document |
| 11.2 The 45-minute interview | Time-boxing, drawing, stating assumptions, going deep where the interviewer pushes | 4 recorded mocks: news feed, collaborative editor, photo-sharing app, design system |
| 11.3 Designs with AI in the loop | Using AI to explore options and draft documents; defending the design without it | Draft a design with AI, then defend it AI-off in a mock review |

**Check your understanding:** What distinguishes a senior answer from a mid-level one in a frontend design round? When should you go deep instead of broad? How do you show you checked an AI-drafted design?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Requirements and estimates | Requirements and ADRs |
| 2 | 2 | Lab 2 · Feed at scale | Virtualised, accessible feed; **P1 starts** |
| 3 | 3 | Lab 3 · Typeahead and forms | Multilingual typeahead |
| 4 | 4 | Lab 4 · OT from scratch (no AI) | Converging text editor; **P1 due** |
| 5 | 4 | Lab 4 (cont.) · CRDT editor | Yjs editor with fuzz tests |
| 6 | 5 | Lab 5 · Offline sync | Two-device sync with conflicts |
| 7 | 6 | Lab 6 · Data layer | BFF and cache design; mid-term (AI off, timed design) |
| 8 | 7 | Lab 7 · Micro-frontends | Cost measurement; **P2 due** |
| 9 | 8 | Lab 8 · Governance | Governance model |
| 10 | 9 | Lab 9 · Indic and RTL | Four-locale screen |
| 11 | 10 | Lab 10 · Reliability and privacy | SLOs and telemetry audit |
| 12 | 10 | Lab 10 (cont.) | Dashboard design; **P3 starts** |
| 13 | 11 | Mock interviews | 4 recorded designs |
| 14 | 11 | Design review | **P3 due** |
| 15 | Review | P3 defence (design review format) | Final exam (AI off, two 45-minute designs) |

## Working with AI in this course

- **Use AI for:** brainstorming alternatives before you decide; drafting design documents that you then rewrite; generating fuzz tests for convergence; producing pseudo-localisation; reviewing your design for missed requirements.
- **Do without AI (drills):** the OT implementation; every timed design in mock interviews; the mid-term and final (two 45-minute designs at a whiteboard). Interviews for these roles are often AI-off, and you must be able to reason aloud.
- **Verify AI output by:** convergence fuzz tests (thousands of random concurrent operations across three clients); measurements on the FE304 baseline for every performance claim; checking claims about public systems (Google Docs, Figma, Linear) against their own engineering writing; checking every `Intl` behaviour in the target locales in real browsers.
- **Where AI still fails here (collect your own evidence):** AI-drafted designs tend to list every technology instead of choosing. They often ignore low-end devices and non-Latin scripts, claim CRDT properties that a library does not provide, and recommend micro-frontends without costing them. Keep a log of these in your design documents' "rejected suggestions" sections.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1 · P2 · P3 | 10% · 15% · 25% |
| Mid-term (AI off, timed design) | 10% |
| Final (AI off, two 45-minute designs) and P3 defence | 20% |

**Mastery gate.** You pass when you can, with AI off, complete two unseen 45-minute frontend system designs at a whiteboard (for example a collaborative spreadsheet and a multilingual e-commerce search page). Examiners score each on a rubric: requirements, estimates, architecture, data model and API, performance budget, accessibility, i18n, failure handling and trade-offs. You need at least "strong" on 7 of 9 rubric lines in both designs, and you must defend one decision under challenge.

## Industry reality

Frontend system design is a standard senior round, and candidate reports from Indian product companies also describe product-design and machine-coding rounds alongside it (see the [FE market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md) and [AI-driven interviews](../../../../06_career_and_market_readiness/04_ai_driven_interviews/)). Public references for the systems in this course include Google's 2010 description of Docs' collaboration model, Figma's 2019 multiplayer write-up, the Ink & Switch local-first essay, Martin Fowler's site on micro-frontends, and the GOV.UK and UX4G design systems.

**Interview questions from this course**

1. *Design a social news feed.* A strong answer clarifies scope and devices and sets a budget. It covers cursor pagination with deduplication, virtualisation, a media strategy (responsive images, video autoplay rules), optimistic interactions with a normalised cache, real-time insertion without jumping the scroll position, the APG feed pattern for accessibility, and metrics (LCP of the first post, INP on like, memory over a long session).
2. *Design real-time collaboration for a document editor.* A strong answer compares OT (central server, simpler for text) with CRDTs (offline, peer-friendly, metadata cost), picks one with reasons, and covers presence, per-user undo, rich text, permissions, persistence and compaction, reconnection after offline edits, and convergence testing.
3. *Design an offline-first app for field workers with poor connectivity.* A strong answer chooses local-first storage (IndexedDB or OPFS) and a sync engine or CRDTs, with conflict policies per field, sync state shown to users, schema migrations, encryption and quotas, plus an update strategy and kill switch, and tests on low-end devices.
4. *Our organisation has 40 frontend teams. Should we adopt micro-frontends?* A strong answer starts from the organisational problem (deploy independence and ownership), costs the duplicate bytes and version skew, and compares a modular monolith with enforced boundaries. It recommends only with guardrails: shared runtime, per-team budgets and design-system governance.
5. *We are launching in 10 Indian languages and Urdu. What changes in the frontend?* A strong answer covers ICU messages, CLDR plurals, `Intl` formatting with `en-IN` grouping, script-specific fonts and subsetting, grapheme-aware text handling, transliteration in search, RTL with logical properties and bidirectional isolation, pseudo-localisation in CI, and a translation workflow with human review.

## Resources (free first)

- **Method:** [GreatFrontEnd front-end system design playbook](https://www.greatfrontend.com/front-end-system-design-playbook) (partly free); [Front End Interview Handbook](https://frontendinterviewhandbook.com/); [patterns.dev](https://www.patterns.dev/).
- **Collaboration and local-first:** [Local-first software](https://www.inkandswitch.com/essay/local-first/) (Ink & Switch, 2019); [Peritext](https://www.inkandswitch.com/peritext/); [crdt.tech](https://crdt.tech/); [Yjs docs](https://docs.yjs.dev/); [Automerge](https://automerge.org/docs/hello/); Gentle and Kleppmann, [Eg-walker](https://arxiv.org/abs/2409.14252); Weidner and Kleppmann, [Fugue](https://arxiv.org/abs/2305.00583); [Figma: how multiplayer works](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/); [Google Docs collaboration (2010)](https://drive.googleblog.com/2010/09/whats-different-about-new-google-docs.html); [localfirstweb.dev](https://localfirstweb.dev/); [Replicache](https://replicache.dev/), [Zero](https://zero.rocicorp.dev/), [ElectricSQL](https://electric-sql.com/).
- **Architecture:** Cam Jackson, [Micro Frontends](https://martinfowler.com/articles/micro-frontends.html); [Module Federation](https://module-federation.io/); [single-spa](https://single-spa.js.org/); [web.dev PWA course](https://web.dev/learn/pwa).
- **Design systems:** [GOV.UK Design System](https://design-system.service.gov.uk/); [UX4G](https://www.ux4g.gov.in/); [Primer](https://primer.style/).
- **i18n:** [CLDR](https://cldr.unicode.org/); [ICU MessageFormat syntax](https://formatjs.github.io/docs/core-concepts/icu-syntax/); [UAX #29 text segmentation](https://unicode.org/reports/tr29/); [MDN `Intl.Segmenter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter); [HarfBuzz](https://harfbuzz.github.io/); [Noto fonts](https://fonts.google.com/noto); [Bhashini](https://bhashini.gov.in/).
- **Accessibility and privacy:** [APG feed pattern](https://www.w3.org/WAI/ARIA/apg/patterns/feed/); [MeitY data protection framework (DPDP Act 2023)](https://www.meity.gov.in/data-protection-framework).

## Sources

All checked 12 Oct 2026.

- Google Drive Blog, "What's different about the new Google Docs: making collaboration fast" (Sep 2010) — https://drive.googleblog.com/2010/09/whats-different-about-new-google-docs.html
- Figma, "How Figma's multiplayer technology works" (2019) — https://www.figma.com/blog/how-figmas-multiplayer-technology-works/
- Kleppmann, Wiggins, van Hardenberg, McGranaghan, "Local-first software" (Ink & Switch, 2019) — https://www.inkandswitch.com/essay/local-first/
- Gentle and Kleppmann, "Collaborative Text Editing with Eg-walker: Better, Faster, Smaller" (arXiv 2409.14252, Sep 2024) — https://arxiv.org/abs/2409.14252 · Weidner and Kleppmann, "The Art of the Fugue" (arXiv 2305.00583) — https://arxiv.org/abs/2305.00583
- npm registry versions on 12 Oct 2026: yjs 13.6.33, @automerge/automerge 3.5.0, @module-federation/enhanced 2.9.2 — https://registry.npmjs.org/
- UX4G (NeGD, MeitY; Design System 3.0) — https://www.ux4g.gov.in/
- MeitY, Data Protection Framework (Digital Personal Data Protection Act 2023) — https://www.meity.gov.in/data-protection-framework
- web-features 3.42.0 (OPFS widely available Sep 2025; `Intl.Segmenter` Apr 2024; Background Sync not Baseline) — https://web-platform-dx.github.io/web-features/
- Candidate interview report, senior frontend engineer, India (self-reported, Sep 2025: machine coding, DSA, JavaScript, product design and hiring-manager rounds) — https://www.jointaro.com/interviews/companies/flipkart/experiences/senior-frontend-engineer-india-september-16-2025-declined-offer-positive-f89c4ee4/

_Last reviewed: 2026-10_
