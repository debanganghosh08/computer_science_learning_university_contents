# MOB301 · Labs and projects

Every lab and project runs on two targets: a current emulator image (API 36 or newer) and a low-memory profile (a physical phone with 2–3 GB of RAM, or an emulator configured with 2 GB). Measurements use release builds unless a lab says otherwise. Labs 3 and 5 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Kotlin and Gradle | Kotlin katas (null safety, sealed types, collections); a multi-module project with a version catalog | Passing kata tests; module graph screenshot | 4 h |
| 2 · Coroutines with virtual time | Retry with backoff, timeouts, cancellation, a debounced search Flow | Tests under `runTest` that run in under 1 s total despite minutes of virtual delay | 6 h |
| 3 · Lifecycle and process death (no AI) | Log every lifecycle callback; restore a 3-screen flow after `adb shell am kill` | Callback logs for rotation, split-screen and kill; a video of exact restoration | 4 h |
| 4 · Recomposition | Measure and reduce recompositions on a feed screen | Before/after counts from Layout Inspector; Compose compiler report diff | 5 h |
| 5 · Architecture refactor (no AI) | Split a 600-line Activity into ViewModel, repository and data sources with Hilt | Diff, dependency graph, unit tests for the ViewModel | 6 h |
| 6 · Navigation 3 and adaptive UI | List-detail flow with deep links; phone, foldable and tablet layouts | Screenshots at three window size classes; deep-link test commands | 5 h |
| 7 · Room migrations | Three schema versions with an auto-migration and a manual one; one module on Room 3 | `MigrationTestHelper` tests for every path, including v1 → v3 | 5 h |
| 8 · Resilient networking | Client against a mock server with 30% failures, slow responses and `304` responses | Error-rate and data-usage report; retry only on idempotent calls | 5 h |
| 9 · WorkManager under Doze | Upload queue with constraints; force Doze and App Standby with `adb` | Timeline of when work actually ran; `onTimeout` handling for a `dataSync` service | 5 h |
| 10 · Test suite and release | Compose UI tests, screenshot tests at 200% font scale, a custom lint rule, an R8 release bundle | CI run link; `bundletool get-size total` output | 6 h |

## Projects

### P1 · Offline transit timetable (L1, ~6 hours)

**Real-world inspiration:** many Indian cities publish transit schedules as GTFS (General Transit Feed Specification) files; Delhi's Open Transit Data portal is one example (https://otd.delhi.gov.in). Commuters need timetables that work underground with no signal.

**What to build:** import a GTFS subset (stops, routes, trips, stop times) into Room on first launch. Search stops by name; show the next five departures; star favourite stops. No network after import.

**Acceptance criteria:**
- **Offline:** every feature works in airplane mode after first import.
- **Speed:** stop search returns in under 100 ms over at least 5,000 stops (logged timing, release build, low-memory target).
- **State:** the departures screen restores exactly after rotation and after `adb shell am kill`.
- **Accessibility:** Accessibility Scanner reports zero errors; all text readable at 200% font scale.
- **Tests:** at least 20 unit tests, including the "next departure after midnight" case.

**Stretch goals:** a home-screen widget for a favourite stop; Hindi and English UI.

**What it proves to an employer:** you can build a correct, offline Compose app with a real data model and handle the lifecycle without help.

### P2 · Shop credit ledger with backup (L2, ~15 hours)

**Real-world inspiration:** digital ledger ("khata") apps such as Khatabook and OkCredit moved small-shop credit records from paper notebooks to phones. This specification is an illustrative scenario, not either company's design.

**What to build:** customers, credit and payment entries, running balances, monthly statements, an encrypted backup to a provided mock server through WorkManager, CSV export through the Storage Access Framework, and English and Hindi strings.

**Acceptance criteria:**
- **Correctness:** balances equal the sum of entries after 10,000 random operations (property test).
- **Data evolution:** three schema versions with migration tests for every path; no data loss when upgrading from v1 directly to v3.
- **Smoothness:** scrolling a 10,000-entry ledger shows under 1% janky frames, measured with Macrobenchmark `FrameTimingMetric` on the low-memory target.
- **Backup reliability:** a backup scheduled offline completes after network returns, after a reboot and after forced Doze. Every case is logged with timestamps.
- **Size:** download size of the release bundle at most 8 MB for a typical device (`bundletool get-size total`).
- **Privacy:** only the permissions the app needs; a Data safety form that matches what it does.

**Stretch goals:** biometric unlock; a shared-statement deep link; Room 3 for the whole app.

**What it proves to an employer:** you can build a data-heavy offline app that keeps money records correct across upgrades and background limits, which is everyday work at Indian fintech and commerce companies.

### P3 · Store-ready civic reporting app (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** public grievance apps let citizens photograph a problem (a pothole, an overflowing bin), tag a location and track it to resolution. The app you build is an illustrative scenario backed by a mock server you also write or the course provides.

**What to build:**
- **Reporting:** capture or pick a photo (photo picker, no storage permission), approximate location by default with an opt-in for precise, category and description.
- **Offline-first:** reports queue locally and upload through WorkManager with resumable, idempotent uploads.
- **Browsing:** a paginated list and detail of nearby reports with status history; adaptive list-detail on large screens.
- **Notifications:** status changes delivered as notifications (polling or a mock push), with a runtime permission request at the right moment.
- **Quality:** Hilt, Room, Navigation 3, a Baseline Profile, unit, UI and screenshot tests in CI.

**Acceptance criteria:**
- **Real users:** published to a Play closed test with at least 12 testers opted in for 14 days (the rule for new personal accounts).
- **Stability:** crash-free users at least 99.5% and zero ANRs over the test period (Play Console or Crashlytics screenshots).
- **Startup:** cold-start time to initial display, median of 10 runs with Macrobenchmark `StartupTimingMetric`: at most 1,000 ms on a mid-range phone and at most 2,000 ms on the low-memory target, with and without the Baseline Profile reported.
- **Size and policy:** download size at most 10 MB; targets API 36; release build shrunk with R8.
- **Privacy evidence:** a proxy capture of one session shows only the endpoints and data your Data safety form declares.
- **Reliability:** 20 reports created offline are all delivered exactly once after reconnecting, including after the app is killed mid-upload.
- **Accessibility:** a recorded TalkBack walkthrough of the full report flow.
- **Write-up:** README with architecture diagram, measurements table and a list of what AI tools generated and how you verified it.

**Stretch goals:** a Wear OS tile showing the status of your latest report; a Kotlin Multiplatform shared module for models and validation; in-app updates for forced minimum versions.

**What it proves to an employer:** you have shipped an Android app to real testers and can show its stability, startup and size numbers. That is the evidence an entry-level Android hire is asked for.

## Feeds into

- [MOB401 Mobile Performance, Security and Release Engineering](../../year_4/MOB401_mobile_performance_security_and_release/README.md): P3 becomes the app you profile, harden and put behind a release pipeline.
- [MOB304 Mobile Architecture, Offline-First and Sync](../MOB304_mobile_architecture_offline_first_and_sync/README.md) and [MOB305 Mobile Integrations](../MOB305_mobile_integrations_payments_maps_notifications/README.md): add sync, payments, maps and sign-in to P2 or P3.
- The [Mobile Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md).
