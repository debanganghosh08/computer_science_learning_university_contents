# MOB304 · Mobile Architecture, Offline-First and Sync

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [FND111](../../../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MOB404](../../year_4/MOB404_mobile_analytics_experimentation_and_growth/README.md), [MOB403](../../year_4/MOB403_mobile_system_design/README.md) |

Part of the [Mobile Engineering major](../../README.md). Labs can be done on Android (Kotlin) or iOS (Swift); you need one of [MOB301](../MOB301_android_with_kotlin_and_jetpack_compose/README.md), [MOB302](../MOB302_ios_with_swift_and_swiftui/README.md) or [MOB303](../MOB303_cross_platform_apps_flutter_and_react_native/README.md) from semester 5. [CS212 Distributed Systems I](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) supplies the theory used in Chapters 5–6.

## Why this course matters now

Google's Android guidance says users "often avoid downloading apps that seem too large, particularly in emerging markets where devices connect to spotty 2G and 3G networks or work on plans with data limits". The same networks make every action that needs the server a chance to fail. An app that stores data locally first, syncs in the background and resolves conflicts predictably feels fast on any network. Platforms keep tightening background execution: from Android 15, `dataSync` foreground services may run only 6 hours in 24, and iOS runs background refresh when it chooses. Sync itself is becoming a product category: sync engines such as ElectricSQL, PowerSync and Zero, and CRDT (conflict-free replicated data type) libraries such as Automerge and Yjs, package years of research. AI assistants write repositories, DAOs and view models quickly. They do not decide which writer wins when two phones edit the same record offline, and they rarely test what happens when the app is killed between a local write and a network call. This course is about those decisions, and about architecture that keeps a 100-screen app changeable.

## Learning outcomes

By the end you can:

1. **Compare** MVC, MVP, MVVM, MVI and clean architecture, and **choose** the lightest structure that keeps a given app testable.
2. **Model** UI and domain state as explicit types and state machines, so impossible states cannot be represented.
3. **Modularise** an app into feature and core modules with clear dependency rules, and **measure** the effect on build time.
4. **Design** an offline-first data layer where the local database is the source of truth and writes flow through an outbox.
5. **Implement** delta sync with cursors and tombstones, idempotent pushes and retry with backoff.
6. **Resolve** conflicts with last-writer-wins, field-level merges, server-authoritative rules or CRDTs, and **explain** each choice's failure modes.
7. **Schedule** sync within Android and iOS background limits, and **design** caches with explicit invalidation.
8. **Prove** convergence and exactly-once effects with deterministic simulation and property-based tests.

## Chapters and lessons

### Chapter 1 · Architecture patterns and their costs (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why architecture | Testability, change cost, team scaling; the "Massive View Controller" problem | List what makes a sample 2,000-line screen hard to change |
| 1.2 MVC, MVP, MVVM, MVI | Where state lives, who mutates it, how views observe it | Implement one screen in MVVM and MVI; compare tests |
| 1.3 Clean architecture | Domain, data and presentation layers; dependency rule; use cases; when it is overkill | Remove an unnecessary layer from an over-engineered sample |
| 1.4 Case studies | Uber's RIBs, Square's Workflow, The Composable Architecture, Google's Now in Android | One-page comparison: what problem each solved |

**Check your understanding:** What does MVI make easier to debug, and what does it cost? Why can use cases that only forward a call be harmful? Which architecture problems are really organisational problems?

### Chapter 2 · State modelling (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Making illegal states unrepresentable | Sealed types and enums instead of flag combinations | Replace six booleans in a checkout screen with one state type |
| 2.2 State machines | States, events, transitions, guards; statecharts | Model an order: draft → placed → paid → shipped, with cancel and refund |
| 2.3 Reducers and effects | Pure reducers, effects at the edges, time travel for debugging | Write a reducer with 100% branch coverage |
| 2.4 Navigation as state | Back stacks and deep links derived from state | Restore a multi-step flow from saved state |

**Check your understanding:** How many states do six independent booleans allow, and how many are valid? Why keep effects out of the reducer? How should state handle "payment pending for 10 minutes"?

### Chapter 3 · Modularisation at scale (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Module types | Feature, core, API/implementation split, test fixtures | Split an app into 8 modules with a dependency diagram |
| 3.2 Dependency rules | No feature-to-feature dependencies; enforcing with build checks | Add a check that fails the build on a forbidden dependency |
| 3.3 Dependency injection graphs | Scopes, multibinding, replacing implementations in tests | Swap a real repository for a fake in one line |
| 3.4 Build performance | Gradle configuration cache and build scans, Xcode build timing; Bazel and Buck at very large scale | Measure a clean and an incremental build before and after |

**Check your understanding:** Why does an API/implementation split speed up incremental builds? What breaks when features depend on each other directly? When is a monolithic module the right choice?

### Chapter 4 · Local-first data (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The database as source of truth | The UI reads only from local storage; network results are written, then observed | Convert a network-first screen to read from Room or SwiftData |
| 4.2 The outbox | Pending-operation table, ordering, retries, crash safety between local write and send | Kill the app at random points during a write; lose nothing |
| 4.3 Client-generated IDs | UUIDv7 (RFC 9562), temporary IDs vs server IDs, foreign keys before sync | Create linked records offline and sync them |
| 4.4 Optimistic UI | Showing pending state, rollback on rejection, user-visible sync status | Design pending, failed and conflicted states for a list item |
| 4.5 Local-first ideals | Ink & Switch's seven ideals for local-first software; what a server still owns | Score three apps you use against the ideals |

**Check your understanding:** Why must the local write and the outbox entry share one transaction? What breaks if the server assigns IDs to records created offline? Which data should never be optimistic (think money)?

### Chapter 5 · Sync protocols (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Pull: delta sync | Change cursors, `updated_at` pitfalls, tombstones for deletes, paging a large initial sync | Sync 200,000 rows on first login on the low-end device |
| 5.2 Push: idempotent writes | Idempotency keys, server deduplication, ordering per entity | Replay every request twice; prove no duplicates |
| 5.3 Time and versions | Clock skew, Lamport clocks, version vectors, hybrid logical clocks | Show last-writer-wins losing data with skewed clocks |
| 5.4 Triggers | Push-to-sync, on foreground, periodic, on connectivity change; batching to save battery | Log sync triggers over a day; count radio wake-ups |
| 5.5 Sync engines and vendor risk | ElectricSQL, PowerSync, Zero, Firestore offline, CloudKit; lock-in and shutdown risk (Firebase Dynamic Links shut down in August 2025) | Evaluate two engines against your P2 requirements |

**Check your understanding:** Why is `updated_at > lastSync` an unsafe cursor? What does a tombstone cost and when can it be deleted? Why can retrying a non-idempotent request corrupt data?

### Chapter 6 · Conflict resolution (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Detecting conflicts | Base versions, three-way comparison, what counts as a conflict | Classify 20 concurrent-edit scenarios |
| 6.2 Simple strategies | Last-writer-wins per record or per field; server-authoritative rules; Figma's per-property approach with a central server | Implement field-level merge for a contact record |
| 6.3 Domain rules | Inventory cannot go negative, bookings cannot overlap: server validation plus compensation | Handle two offline orders for the last item |
| 6.4 CRDTs | G-Counter, PN-Counter, LWW-Register, OR-Set, sequence CRDTs for text; Automerge and Yjs | Implement an OR-Set and test convergence |
| 6.5 Conflicts users can see | When to ask the user; merge UI; audit history | Design a conflict screen for a shared note |

**Check your understanding:** Why does an OR-Set not lose an add that is concurrent with a remove? When is last-writer-wins acceptable? Why are CRDTs a poor fit for a bank balance?

### Chapter 7 · Background work under OS limits (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Android | WorkManager constraints and backoff, Doze, App Standby buckets, foreground-service types and the Android 15 time limit | Measure how late periodic sync runs in each standby bucket |
| 7.2 iOS | `BGAppRefreshTask` and `BGProcessingTask` (system-scheduled), background `URLSession`, background pushes that the system may throttle | Log real refresh times over two days |
| 7.3 Designing for "eventually" | Sync that tolerates hours of delay; user-triggered sync; stale indicators | Write the sync-timing contract for your P2 app |
| 7.4 Battery and data budgets | Batching, compression, Wi-Fi-only large transfers, respecting Data Saver | Cut a sync's radio wake-ups by half |

**Check your understanding:** Why can't an app promise "sync every 15 minutes" on either platform? What does the user see when sync is late, and is it honest? When is a silent push the wrong trigger?

### Chapter 8 · Caching (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 HTTP caching | `Cache-Control`, `ETag`, conditional requests (RFC 9111) | Measure bytes saved by conditional requests |
| 8.2 Cache tiers | Memory LRU, disk cache, database; time-to-live vs event-based invalidation | Implement stale-while-revalidate for a product list |
| 8.3 Prefetching | Predicting the next screen; prefetching on Wi-Fi and charging only | Prefetch the next page without increasing data use on mobile data |
| 8.4 Storage budgets | Low-storage devices, eviction policies, clearing caches safely | Keep total app storage under 150 MB under heavy use |

**Check your understanding:** What is the difference between a cache and a source of truth? Why can stale-while-revalidate show wrong prices? What should be evicted first when storage is low?

### Chapter 9 · Testing distributed mobile behaviour (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Deterministic simulation | Seeded fake network, fake clock and fake server; replaying failures | Find a sync bug by replaying its seed |
| 9.2 Property-based tests | Convergence ("all replicas equal after sync"), idempotency, no lost writes | Kotest or Swift property tests over 10,000 random histories |
| 9.3 Network conditions | Emulator network throttling, Network Link Conditioner, airplane-mode scripts | Run the P2 suite under 3G-like and lossy profiles |
| 9.4 Upgrade tests | Users skip versions; schema and protocol upgrades from the oldest supported version | Upgrade from v1 to v4 with pending outbox entries |

**Check your understanding:** Why are random network tests without a seed nearly useless for debugging? What property proves a CRDT is correct? What happens to outbox entries written by an older app version?

### Chapter 10 · Evolution, security and old clients (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 API versioning for mobile | Old clients live for years; additive changes, version negotiation, minimum supported version | Design a breaking change that old apps survive |
| 10.2 Forced updates | Remote-config gates, Play in-app updates, graceful degradation | Implement a soft and a hard update prompt |
| 10.3 Local data security | Encrypted databases (SQLCipher), Keystore/Keychain-wrapped keys, wiping data on logout | Prove a logged-out device holds no user data |
| 10.4 Architecture review | Writing and reviewing an architecture document | Review another team's P3 design |

**Check your understanding:** Why does a mobile API need a different deprecation policy from a web API? What can a forced update not fix? Where should the database encryption key live?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Same screen, two patterns | Comparison note |
| 2 | 2 | Lab 2 · State machines | — |
| 3 | 3 | Lab 3 · Modularisation and build times | Build-time report |
| 4 | 4 | Lab 4 · Outbox with crash injection | **P1 due** |
| 5 | 4 | Lab 4 (cont.) | — |
| 6 | 5 | Lab 5 · Delta sync and idempotent push | — |
| 7 | 5 | Lab 5 (cont.) | Mid-term (AI off) |
| 8 | 6 | Lab 6 · Conflict strategies | — |
| 9 | 6 | Lab 6 (cont.) · OR-Set | **P2 due** |
| 10 | 7 | Lab 7 · Background limits | — |
| 11 | 8 | Lab 8 · Caching | — |
| 12 | 9 | Lab 9 · Deterministic simulation | — |
| 13 | 10 | Lab 10 · Old clients and upgrades | — |
| 14 | 10 | Architecture reviews | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating DAOs, entities and mappers; drafting state machines from a written spec (then reviewing every transition); producing randomised test generators; explaining a CRDT paper section; reviewing a sync design for missed cases.
- **Do without AI (drills):** the outbox and crash-injection lab; working through conflict scenarios on paper; implementing one CRDT by hand; the mid-term and final.
- **Verify AI output by:** (1) running it inside the deterministic simulator with crash points between every pair of steps; (2) property tests for convergence and idempotency; (3) checking that every network write has an idempotency key and every delete a tombstone; (4) testing upgrades from the oldest supported version.
- **Where AI still fails here (collect your own evidence):** generated sync code commonly uses `updated_at` as a cursor, retries non-idempotent requests, performs the local write and the network call outside one atomic step, or treats "last write wins" as safe without considering clock skew. Record each case your simulator catches, with its seed.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 25% |
| Architecture review of a peer's design | 5% |

**Mastery gate.** You pass when you can, with AI tools off: (1) design on a whiteboard, in 45 minutes, the data layer and sync protocol for an offline-first app with two editing devices, naming the conflict strategy and its failure modes; (2) given a sync implementation with a planted bug, find a failing seed in the simulator within 30 minutes; (3) show your P3 passing 1,000 random online/offline/kill histories with zero lost or duplicated writes.

## Industry reality

Figma described in 2019 how its multiplayer editing uses a central server as the authority, with last-writer-wins on individual object properties, inspired by CRDTs but not a pure CRDT system. Ink & Switch's 2019 essay "Local-first software" set out seven ideals for apps that keep working without a server, and libraries such as Automerge and Yjs implement CRDTs for collaborative data. Uber published its RIBs architecture as open source; Google's Now in Android sample shows offline-first Room with WorkManager-based sync. Firebase Dynamic Links shut down in August 2025, a reminder that a mobile architecture should isolate third-party services behind interfaces you can replace.

**Interview questions from this course**

1. *Design offline editing of notes on two devices. What happens when both edit the same note offline?* Strong answer: local database as source of truth; outbox; base versions to detect conflicts; picks field-level merge, sequence CRDT or user-resolved conflicts and explains why; covers deletes (tombstones) and attachments.
2. *A user taps "Send" offline. How do you guarantee the message is delivered exactly once?* Strong answer: outbox in the same transaction as the local write; client-generated ID as idempotency key; server deduplication; retries with backoff; ordering per conversation; what the UI shows meanwhile.
3. *MVVM or MVI for a complex checkout screen? When is clean architecture overkill?* Strong answer: compares state ownership and testability; argues from team size and screen complexity; avoids pass-through layers.
4. *First login must sync 200,000 records on a 2 GB phone. How?* Strong answer: paged cursor sync; batched transactions; background work with constraints; progress UI; resumable after kill; memory measured, not assumed.
5. *You must change an API in a breaking way, and 20% of users never update. What do you do?* Strong answer: additive change first; versioned endpoints; minimum-version gate through remote config and in-app updates; server-side compatibility layer; metrics on old-version traffic.

## Resources (free first)

- **Platform guides:** Android, Build an offline-first app — https://developer.android.com/topic/architecture/data-layer/offline-first ; Android guide to app architecture — https://developer.android.com/topic/architecture ; Apple, Background Tasks — https://developer.apple.com/documentation/backgroundtasks ; Apple, Pushing background updates to your app — https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app
- **Local-first and CRDTs:** Kleppmann, Wiggins, van Hardenberg and McGranaghan, "Local-first software" (Ink & Switch, 2019) — https://www.inkandswitch.com/local-first/ ; CRDT resources — https://crdt.tech/ ; Automerge — https://automerge.org/ ; Yjs — https://yjs.dev/
- **Case studies:** Figma, "How Figma's multiplayer technology works" (2019) — https://www.figma.com/blog/how-figmas-multiplayer-technology-works/ ; Uber RIBs — https://github.com/uber/RIBs ; Now in Android — https://github.com/android/nowinandroid ; The Composable Architecture — https://github.com/pointfreeco/swift-composable-architecture
- **Standards and papers:** RFC 9562 (UUIDs, including v7) — https://www.rfc-editor.org/rfc/rfc9562 ; RFC 9111 (HTTP caching) — https://www.rfc-editor.org/rfc/rfc9111 ; Shapiro et al., "Conflict-free Replicated Data Types" (SSS 2011) ; Kulkarni et al., "Logical Physical Clocks" (OPODIS 2014)
- **Paid, optional:** Kleppmann, *Designing Data-Intensive Applications* (O'Reilly); its replication and consistency chapters are the best companion. CS212's free resources cover the same theory.

## Sources

- Android Developers, Reduce your app size (emerging-markets quote) — https://developer.android.com/topic/performance/reduce-apk-size (checked 2026-10)
- Android Developers, Foreground service timeouts (Android 15) — https://developer.android.com/develop/background-work/services/fgs/timeout (checked 2026-10)
- Room 3 release notes — https://developer.android.com/jetpack/androidx/releases/room3 (checked 2026-10)
- Figma blog (2019); Ink & Switch essay (2019); Uber RIBs repository — as listed under Resources (checked 2026-10)
- Firebase Dynamic Links deprecation FAQ (shutdown 25 Aug 2025) — https://firebase.google.com/support/dynamic-links-faq (checked 2026-10)

_Last reviewed: 2026-10_
