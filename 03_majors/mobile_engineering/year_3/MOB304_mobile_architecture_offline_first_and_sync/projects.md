# MOB304 · Labs and projects

The course provides a **sync lab server** with seeded fault injection: it drops, delays, duplicates and reorders requests, returns 5xx errors, and can skew its clock. Every lab and project runs against it, and every result reports the seed so anyone can replay it. Work in Kotlin (Android) or Swift (iOS); P3 may use a cross-platform stack from MOB303. Labs 4 and 6 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Same screen, two patterns | Implement a filterable list in MVVM and in MVI | Both versions with tests; a one-page comparison of test effort and bug surface | 4 h |
| 2 · State machines | Model an order lifecycle including cancel, refund and "payment pending" | State diagram; reducer with 100% branch coverage; three illegal transitions rejected | 4 h |
| 3 · Modularisation and build times | Split a provided monolith into feature and core modules with enforced rules | Module graph; a failing build for a forbidden dependency; clean and incremental build times before and after | 6 h |
| 4 · Outbox with crash injection (no AI) | Local write plus outbox entry in one transaction; sender with retries | Kill-point report: 200 random kills, zero lost or duplicated writes | 6 h |
| 5 · Delta sync and idempotent push | Cursor-based pull with tombstones; idempotency keys on push | Replay-everything-twice test passing; initial sync of 200,000 rows on the low-end device with time and peak memory | 7 h |
| 6 · Conflict strategies (no AI) | Last-writer-wins, field-level merge, server-authoritative rule; implement an OR-Set | 20 classified scenarios with outcomes; OR-Set convergence tests | 6 h |
| 7 · Background limits | Run periodic sync under Doze and each App Standby bucket, or iOS background refresh | Two-day timeline of real sync times; sync-timing contract | 4 h |
| 8 · Caching | Stale-while-revalidate list, conditional requests, storage budget with eviction | Bytes saved; storage under 150 MB after a heavy-use script | 4 h |
| 9 · Deterministic simulation | Seeded fake clock, network and server; find a planted bug | The failing seed, the trace, the fix and the passing rerun | 6 h |
| 10 · Old clients and upgrades | Upgrade from v1 to v4 with pending outbox entries; a soft and hard update gate | Upgrade test results; a design for one breaking API change | 4 h |

## Projects

### P1 · Offline task list with an outbox (L1, ~6 hours)

**Real-world inspiration:** delivery agents, sales staff and technicians record work where signal drops in basements, lifts and rural areas. This app is an illustrative scenario.

**What to build:** a task list (create, edit, complete, delete) that reads only from the local database, writes through an outbox, and syncs with the lab server. Each item shows synced, pending or failed state.

**Acceptance criteria:**
- **No lost or duplicated writes:** after 1,000 random online/offline toggles and 50 forced kills, the server and device hold the same tasks, with zero duplicates (automated check).
- **Honest UI:** pending and failed items are visibly marked; a failed item can be retried or discarded.
- **Instant UI:** every user action updates the screen within one frame, regardless of network.
- **Tests:** at least 15 unit tests for the outbox, including ordering of an edit followed by a delete.

**Stretch goals:** batch outbox sends; a "last synced" indicator; sync on reconnect.

**What it proves to an employer:** you understand why the local write and the queued send must be atomic, the first thing interviewers probe in offline-first design.

### P2 · Field survey app that works for a week offline (L2, ~15 hours)

**Real-world inspiration:** health and development surveys in low-connectivity areas use open-source tools such as ODK Collect (https://getodk.org), where enumerators fill forms for days and upload later. Your app is an illustrative scenario, not ODK's design.

**What to build:** forms defined by a provided JSON schema; records with photos and GPS; assignments pulled from the server by delta sync; results pushed through an outbox; shared household records that two enumerators may edit offline (field-level merge with a written rule per field); an encrypted local database with keys in Keystore or Keychain.

**Acceptance criteria:**
- **Endurance:** after a scripted week offline (5,000 records, 500 photos), sync completes on a 3G-like network profile in under 10 minutes and resumes correctly after two forced kills mid-sync.
- **Exactly once:** zero duplicate records or photos on the server (automated reconciliation).
- **Conflicts:** 20 provided concurrent-edit scenarios resolve exactly as your written rules say; ambiguous ones are flagged for review instead of silently overwritten.
- **Security:** the database file copied off the device is unreadable without the key; logging out wipes all survey data (verified).
- **Battery:** when idle and online, the app wakes the radio for sync at most 4 times per hour (log evidence).
- **Data use:** photos are resized and compressed before upload; report bytes per record.

**Stretch goals:** partial sync by region; a supervisor dashboard showing per-device sync lag; form schema versioning with migration of in-progress records.

**What it proves to an employer:** you can build a data-collection app that survives the real conditions of field work, the same problems faced by logistics, agritech and public-health apps in India.

### P3 · Collaborative household lists with CRDTs (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** shared lists (groceries, chores, packing) are edited by several family members on different phones, often offline. Ink & Switch's local-first essay and libraries such as Automerge and Yjs show how CRDTs let replicas converge without a central lock. Your app is an illustrative scenario.

**What to build:**
- **Data model:** lists with items that can be added, edited, checked, reordered and deleted concurrently, using Automerge, Yjs (through a cross-platform stack) or CRDTs you implement.
- **Sync:** a relay server you write that stores and forwards changes; it never needs to understand the data.
- **History:** who changed what, with undo of your own changes.
- **Sharing:** invite by link (deep links come in MOB305; a code is enough here).
- **Simulation:** a deterministic multi-replica simulator in CI.

**Acceptance criteria:**
- **Convergence:** with 3 replicas and 10,000 random operations, including concurrent add/remove of the same item and concurrent reorders, all replicas are identical after sync, across 1,000 seeds.
- **Robustness:** 1,000 simulated histories with random kills, duplicated and reordered messages lose no operation.
- **Size:** document size and sync payload per operation reported; compaction keeps a year-long simulated list under a stated budget that you justify.
- **Performance:** initial load of a 10,000-item list under 2 seconds on the low-end device; sync of 1,000 queued operations under 10 seconds on a 3G-like profile.
- **Upgrades:** a v1 → v3 upgrade with pending operations passes.
- **Write-up:** design document with the CRDT choices, a failure-mode table, and the simulator's most interesting bug with its seed.

**Stretch goals:** end-to-end encryption of changes so the relay sees only ciphertext; rich-text notes on items using a sequence CRDT; a measured comparison with a server-authoritative design.

**What it proves to an employer:** you can design, implement and prove correct a sync system, which is senior-level work in collaborative, productivity and offline-first apps.

## Feeds into

- [MOB404 Mobile Analytics, Experimentation and Growth Engineering](../../year_4/MOB404_mobile_analytics_experimentation_and_growth/README.md): the outbox pattern becomes the reliable analytics event queue.
- [MOB403 Mobile System Design](../../year_4/MOB403_mobile_system_design/README.md): offline-first notes and chat cases build directly on P2 and P3.
- [MOB305 Mobile Integrations](../MOB305_mobile_integrations_payments_maps_notifications/README.md): push-triggered sync and invite deep links.
- The [Mobile Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md) and a [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) capstone on local-first systems.
