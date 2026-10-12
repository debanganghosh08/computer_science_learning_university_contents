# MOB301 · Android with Kotlin and Jetpack Compose

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [FND111](../../../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MOB401](../../year_4/MOB401_mobile_performance_security_and_release/README.md), [MOB304](../MOB304_mobile_architecture_offline_first_and_sync/README.md), [MOB305](../MOB305_mobile_integrations_payments_maps_notifications/README.md) |

Part of the [Mobile Engineering major](../../README.md). You arrive knowing Java or TypeScript and no Android. You leave able to ship a Play-ready app.

## Why this course matters now

Android ran on 93.89% of India's mobile devices in September 2026 (StatCounter), so for most Indian products "the app" means the Android app. The platform moves fast: Kotlin 2.4 shipped in June 2026, Navigation 3 became stable in November 2025, and Room 3.0 is coroutine-first and Kotlin Multiplatform-ready. From 31 August 2026, new apps and updates on Google Play must target Android 16 (API level 36). Gemini in Android Studio now has an agent mode that writes Compose screens, fixes Gradle errors and analyses crashes. On Google's Android Bench leaderboard of real Android development tasks, the best model scored 84.5 out of 100 in July 2026. What the tools still get wrong is the platform itself: process death, the main thread, background limits, permissions and the cheap phone your users actually own. This course teaches those first, so you can tell when generated code will fail in production.

## Learning outcomes

By the end you can:

1. **Write** idiomatic Kotlin: null safety, sealed hierarchies, extension functions, and structured concurrency with coroutines and Flow, **tested** with virtual time.
2. **Explain** the Android process and Activity lifecycle, and **preserve** state across configuration changes and process death.
3. **Build** Compose UIs with correct state hoisting, side effects and stable parameters, and **measure** recomposition.
4. **Structure** an app with ViewModels, a repository layer and dependency injection, following Google's guide to app architecture.
5. **Persist** data with Room (2.x and 3.x) and DataStore, with **tested** migrations.
6. **Schedule** reliable background work with WorkManager and **respect** Doze, App Standby buckets and foreground-service time limits.
7. **Request** permissions with the least access needed, and **complete** a Play Data safety form that matches what the app does.
8. **Ship** a signed, shrunk App Bundle through Play Console tracks, meeting the current target-API policy, and **read** Android vitals.

## Chapters and lessons

### Chapter 1 · Kotlin for Android engineers (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Types and null safety | `?`, `!!`, smart casts, platform types from Java; why `lateinit` hides crashes | Port a 300-line Java class; remove every `!!` |
| 1.2 Modelling with sealed types | `data`, `sealed interface`, exhaustive `when`, value classes | Model a payment result (success, pending, failed with reason) so illegal states cannot compile |
| 1.3 Functions and lambdas | Extension functions, higher-order functions, `inline`, scope functions (`let`, `apply`, `run`) and when they hurt readability | Rewrite 10 snippets; argue each scope-function choice |
| 1.4 Collections and sequences | Eager vs lazy evaluation, `Sequence` for large pipelines | Time a 10⁶-element pipeline both ways |
| 1.5 Build system | Gradle Kotlin DSL, version catalogs, the K2 compiler, KSP vs KAPT | Create a multi-module project with a version catalog |

**Check your understanding:** Why can a Kotlin `String` from a Java method still be null at runtime? When does a sealed interface beat an enum? What does `inline` change in the bytecode, and when is it worth it?

### Chapter 2 · Coroutines and Flow (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Structured concurrency | `CoroutineScope`, `Job`, `SupervisorJob`, parent–child cancellation | Draw the job tree of a screen that loads three sources |
| 2.2 Dispatchers and main-safety | `Main`, `IO`, `Default`; `withContext`; "suspend functions must be main-safe" | Find the main-thread disk read in a sample app with StrictMode |
| 2.3 Cancellation and exceptions | Cooperative cancellation, `CancellationException` must not be swallowed, `launch` vs `async` propagation, `CoroutineExceptionHandler` | Fix five planted bugs that leak work or swallow cancellation |
| 2.4 Flow | Cold `Flow` vs hot `StateFlow`/`SharedFlow`; `map`, `combine`, `flatMapLatest`, `debounce`, `stateIn` with `WhileSubscribed(5_000)` | Build a search box: debounce, cancel stale queries, show loading |
| 2.5 Testing concurrency | `runTest`, `StandardTestDispatcher`, virtual time, Turbine | Test a retry-with-backoff function without real delays |

**Check your understanding:** Why does catching `Exception` inside a coroutine break cancellation? What is the difference between `StateFlow` and a `SharedFlow` with `replay = 1`? Why use `WhileSubscribed(5_000)` instead of `Eagerly` for UI state?

### Chapter 3 · The Android app model (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Processes and components | Application, Activity, Service, BroadcastReceiver, ContentProvider; the manifest; each app is a Linux user in a sandbox | Inspect your app's process and UID with `adb shell ps` |
| 3.2 Activity lifecycle | `onCreate` → `onDestroy`; configuration changes; multi-window | Log every callback across rotation, split-screen and back |
| 3.3 Process death | Low-memory kill, `SavedStateHandle`, `rememberSaveable`; "Don't keep activities" | Kill your app with `adb shell am kill` and restore the exact screen |
| 3.4 The main thread | Looper, Handler, input dispatch; an ANR (Application Not Responding) fires after 5 seconds without responding to input | Trigger and read an ANR trace |
| 3.5 Modern platform rules | Edge-to-edge by default (Android 15), predictive back, and Android 17 ignoring orientation and resizability restrictions on large screens | Fix insets and test on a resizable emulator |

**Check your understanding:** What survives a rotation but not process death? Why can a `BroadcastReceiver` cause an ANR? An app works on a phone but breaks on a tablet running Android 17: what changed?

### Chapter 4 · Jetpack Compose fundamentals (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Composition and recomposition | Composables as functions of state; positional memoisation; `remember`, `mutableStateOf` | Count recompositions with Layout Inspector |
| 4.2 State hoisting and UDF | Stateless vs stateful composables; state down, events up | Refactor a stateful form into a hoisted, previewable one |
| 4.3 Layout and lists | `Row`/`Column`/`Box`, modifier order, `LazyColumn` with `key` and `contentType` | Build a 5,000-item list; prove items keep state when reordered |
| 4.4 Side effects | `LaunchedEffect`, `DisposableEffect`, `rememberCoroutineScope`, `derivedStateOf`, `snapshotFlow` | Fix a screen that restarts a network call on every recomposition |
| 4.5 Stability and performance | Strong skipping, `@Stable`/`@Immutable`, unstable collections, Compose compiler reports | Read compiler reports; make three composables skippable |
| 4.6 Material 3 and accessibility | Theming, dynamic colour, semantics, 48 dp touch targets, TalkBack, 200% font scale | Pass Accessibility Scanner with zero errors on one screen |

**Check your understanding:** Why does modifier order change both layout and click area? What makes a parameter "unstable", and what does it cost? When is `derivedStateOf` the wrong tool?

### Chapter 5 · App architecture (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 ViewModel | `viewModelScope`, `SavedStateHandle`, what must never be held (Context, Views) | Find the Activity leak in a sample with LeakCanary |
| 5.2 UI state modelling | One immutable `UiState` per screen; loading/content/error; events as state | Model a paginated list including "load more failed" |
| 5.3 Data and domain layers | Repositories as single source of truth; optional use cases; mappers | Split a 600-line ViewModel into layers |
| 5.4 Dependency injection | Hilt modules and scopes; manual DI to see what Hilt generates | Implement the same graph both ways |
| 5.5 Lifecycle-aware collection | `collectAsStateWithLifecycle`, `repeatOnLifecycle` | Show a flow that keeps collecting in the background, then fix it |

**Check your understanding:** Why is a `Context` in a ViewModel a leak? When are use cases worth adding? How should a one-time "payment succeeded" message reach the UI?

### Chapter 6 · Navigation and adaptive UI (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Navigation 3 | A back stack you own as state, `NavDisplay`, scenes, type-safe keys | Build a three-level flow with arguments and back handling |
| 6.2 Deep links into navigation | Mapping URIs to back-stack entries; synthetic back stacks | Open a product detail from `adb shell am start -d` |
| 6.3 Adaptive layouts | Window size classes, list-detail and supporting-pane layouts, foldable postures | One layout that works on phone, foldable and tablet |
| 6.4 Predictive back and transitions | Back gesture previews; shared element transitions | Add predictive back to a custom screen |

**Check your understanding:** What does owning the back stack as state make easier to test? How should a deep link behave if the user is logged out? Why must layouts adapt to window size, not device type?

### Chapter 7 · Local data (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Room basics | Entities, DAOs, relations, `Flow` queries, transactions | A notes database with tags (many-to-many) |
| 7.2 Migrations | Versioned schemas, auto-migrations, `MigrationTestHelper` | Ship v1 → v2 → v3 and test every path, including v1 → v3 |
| 7.3 Room 3.0 | `androidx.room3`: suspend-only DAOs, required `SQLiteDriver`, KSP only, `Flow`-based invalidation | Migrate a Room 2 module and list every change |
| 7.4 DataStore and files | Preferences vs Proto DataStore; why not `SharedPreferences`; scoped storage and the photo picker | Move settings to Proto DataStore with a migration |
| 7.5 SQLite performance | Indices, `EXPLAIN QUERY PLAN`, batching writes in one transaction | Make a 50,000-row insert 20× faster |

**Check your understanding:** Why must you test v1 → v3 and not only v2 → v3? What does Room 3 gain by requiring coroutines? Why do 50,000 single-row inserts run slowly?

### Chapter 8 · Networking (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 HTTP clients | Retrofit + OkHttp or Ktor client; `kotlinx.serialization`; interceptors | Client for a public API with typed errors |
| 8.2 Failure handling | Timeouts, retries with exponential backoff and jitter, only for idempotent calls | Survive a mock server that fails 30% of requests |
| 8.3 Caching | OkHttp cache, `ETag` and `If-None-Match`, offline reads from Room | Show a `304 Not Modified` in the network inspector |
| 8.4 Images | Coil: memory and disk caches, downsampling, placeholders | Halve peak memory on an image grid |
| 8.5 Network awareness | `ConnectivityManager` callbacks, metered networks, Data Saver | Defer large downloads to unmetered networks |

**Check your understanding:** Which requests may be retried automatically, and why? What does an `ETag` save the user in data and time? Why can "isOnline() returned true" still mean the request fails?

### Chapter 9 · Background work and system limits (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 WorkManager | Constraints, unique work, chaining, backoff, expedited work | Upload queue that survives reboot |
| 9.2 Doze and App Standby | Maintenance windows, standby buckets, what wakes an app | Force Doze with `adb shell dumpsys deviceidle force-idle` and observe |
| 9.3 Foreground services | Required service types; from Android 15, `dataSync` and `mediaProcessing` services may run 6 hours in 24, then `onTimeout` | Handle `onTimeout` correctly in a sync service |
| 9.4 Notifications | Channels, `POST_NOTIFICATIONS` runtime permission (Android 13+), progress notifications | A download with progress and cancel |
| 9.5 Alarms and exact timing | Exact-alarm permission; why most apps should not need one | Replace an exact alarm with WorkManager |

**Check your understanding:** Why might periodic work run hours late? What happens if a `dataSync` service ignores `onTimeout`? When is a foreground service the right choice over WorkManager?

### Chapter 10 · Permissions, privacy and platform security (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Runtime permissions | Rationale UX, "don't ask again", approximate vs precise location | A location flow that still works if the user declines |
| 10.2 Least privilege | Photo picker instead of storage permission; intents instead of permissions | Remove two permissions from a sample app without losing features |
| 10.3 Component security | `exported` components, `PendingIntent` mutability, intent validation | Review a manifest and fix every unnecessary export |
| 10.4 Data safety | Play's Data safety form; mapping each SDK's collection to the form | Complete the form for your P2 app with evidence |

**Check your understanding:** Why does the photo picker improve privacy and conversion at once? What can a malicious app do with an exported Activity that trusts its extras? Who is responsible when a third-party SDK collects data your form does not declare?

### Chapter 11 · Testing and quality (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Unit tests | ViewModels with fakes, coroutine test rules, Turbine | 90% branch coverage on one feature's ViewModel |
| 11.2 Compose UI tests | Semantics tree, `createComposeRule`, idling | Test the search screen end to end |
| 11.3 Screenshot tests | Roborazzi or Paparazzi; testing dark theme and 200% font scale | Catch a planted layout regression |
| 11.4 Static analysis | Android Lint, detekt, custom lint rule | Write a lint rule that bans `GlobalScope` |

**Check your understanding:** What does a Robolectric test prove that a pure unit test cannot, and what does it miss? Why test at 200% font scale? Which bugs can only an instrumented test on a device find?

### Chapter 12 · Shipping to Google Play (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Release builds | App Bundles, R8 shrinking, keep rules, `versionCode` | Compare debug and release download size with `bundletool` |
| 12.2 Signing | Play App Signing, upload keys, key loss recovery | Set up signing with no secrets in Git |
| 12.3 Tracks and testing rules | Internal, closed, open and production tracks; new personal accounts need 12 testers opted in for 14 days before production | Publish to an internal track |
| 12.4 Policy deadlines | Target API 36 from 31 Aug 2026 (extension to 1 Nov 2026); 16 KB page-size support for updates from 1 Feb 2027; developer verification (from 30 Sep 2026 in four countries, global in 2027) | Write your app's compliance calendar |
| 12.5 Android vitals and staged rollout | User-perceived crash rate threshold 1.09% and ANR rate 0.47% (8% per phone model); staged rollout and halting | Roll out to 10%, read vitals, decide |

**Check your understanding:** Why can R8 break an app that worked in debug? What happens to an app that misses the target-API deadline? Why halt a rollout at 10% rather than roll back?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Kotlin katas and Gradle | Multi-module skeleton |
| 2 | 2 | Lab 2 · Coroutines with virtual time | — |
| 3 | 2 | Lab 2 (cont.) | Flow search box |
| 4 | 3 | Lab 3 · Lifecycle and process death | **P1 due** |
| 5 | 4 | Lab 4 · Recomposition | — |
| 6 | 4 | Lab 4 (cont.) | Accessibility report |
| 7 | 5 | Lab 5 · Architecture refactor | Mid-term (AI off) |
| 8 | 6 | Lab 6 · Navigation 3 and adaptive UI | — |
| 9 | 7 | Lab 7 · Room migrations | — |
| 10 | 8 | Lab 8 · Resilient networking | **P2 due** |
| 11 | 9 | Lab 9 · WorkManager under Doze | — |
| 12 | 10 | Lab 9 (cont.) | Data safety form with evidence |
| 13 | 11 | Lab 10 · Test suite | — |
| 14 | 12 | Lab 10 (cont.) | **P3 due** (internal or closed track) |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first drafts of Compose screens from a sketch; Room entities and DAOs from a schema; test scaffolding; explaining a stack trace or Gradle error; migrating a View-based screen to Compose. Gemini in Android Studio (agent mode, App Quality Insights crash analysis, Compose preview generation), Claude Code, GitHub Copilot and Cursor all do this.
- **Do without AI (drills):** the lifecycle and process-death lab; coroutine cancellation and exception propagation by hand; a weekly 45-minute "build a list-detail screen from scratch" drill; the mid-term and final. You cannot review generated concurrency code you could not write.
- **Verify AI output by:** (1) running it under StrictMode and LeakCanary; (2) rotating, killing the process and returning; (3) checking recomposition counts in Layout Inspector; (4) running Android Lint, which flags many deprecated APIs; (5) checking every API against the current developer.android.com page, because models trained earlier suggest older APIs.
- **Where AI still fails here (collect your own evidence):** keep a log of every generated suggestion that (a) used a deprecated or removed API (for example `onActivityResult`, `AsyncTask`, Room 2 APIs in a Room 3 module); (b) launched work in `GlobalScope` or swallowed `CancellationException`; (c) lost state on process death; (d) requested a broader permission than needed. Benchmarks such as Android Bench test whether patches pass tests; they do not test behaviour after process death or on a 2 GB device. Your log is graded.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 25% |
| AI failure log | 5% |

**Mastery gate.** You pass when you can, with AI tools off and in 2 hours: build a two-screen Compose app that loads a paginated API into Room, shows loading, error and empty states, survives rotation and process death without refetching, and passes a provided UI test; then explain, from a trace you capture, why one screen recomposes too often and fix it.

## Industry reality

Google's own sample, Now in Android, uses the architecture taught here (Compose, ViewModels, repositories, Room, WorkManager, Hilt, modularisation). Zomato reported up to 30% faster cold starts on low- and mid-end devices, 60% fewer out-of-memory issues and about 1.5 percentage points more completed orders after removing unused SDKs, lazy-loading libraries and flattening layouts. Play may reduce the visibility of apps that exceed Android vitals thresholds and show a warning on their store listing.

**Interview questions from this course**

1. *What happens to screen state on rotation, and on process death?* Strong answer: ViewModel survives configuration change but not process death; small UI state goes in `SavedStateHandle` or `rememberSaveable`, large state in a database; shows how to test with "Don't keep activities" or `adb shell am kill`.
2. *Compare `StateFlow`, `SharedFlow` and `Channel` for UI state and one-off events.* Strong answer: `StateFlow` is conflated and always has a value; events can be lost or replayed with the wrong choice; prefers modelling events as state that the UI consumes; mentions lifecycle-aware collection.
3. *A `LazyColumn` stutters while scrolling. How do you find out why?* Strong answer: release build with Baseline Profile; recomposition counts; missing `key`s or unstable parameters; heavy work in composition; oversized image decoding; confirms with Macrobenchmark frame timing or a Perfetto trace, not by eye.
4. *Upload 50 photos reliably even if the user leaves the app.* Strong answer: WorkManager unique work with network constraint; idempotent, resumable uploads; progress via a foreground notification within service-type limits; backoff; what happens after reboot and when the user cancels.
5. *A `viewModelScope` is cancelled during a network call. What happens, and how do exceptions propagate in `launch` vs `async`?* Strong answer: cooperative cancellation at suspension points; `CancellationException` must propagate; `launch` reports to the parent, `async` holds until `await`; `SupervisorJob` isolates sibling failures.

## Resources (free first)

- **Official course:** Android Basics with Compose — https://developer.android.com/courses/android-basics-compose/course
- **Documentation:** Kotlin docs and coroutines guide — https://kotlinlang.org/docs/coroutines-guide.html ; Compose — https://developer.android.com/compose ; Guide to app architecture — https://developer.android.com/topic/architecture ; Room 3 release notes — https://developer.android.com/jetpack/androidx/releases/room3 ; Navigation 3 — https://developer.android.com/jetpack/androidx/releases/navigation3 ; Background work — https://developer.android.com/develop/background-work/background-tasks
- **Reference app:** Now in Android — https://github.com/android/nowinandroid
- **Policy:** Target API requirements — https://developer.android.com/google/play/requirements/target-sdk ; Android vitals — https://developer.android.com/topic/performance/vitals
- **Tools:** LeakCanary — https://square.github.io/leakcanary/ ; Turbine — https://github.com/cashapp/turbine ; Roborazzi — https://github.com/takahirom/roborazzi
- **Paid, optional:** Moskala, *Kotlin Coroutines: Deep Dive* (Leanpub). The official coroutines guide covers the essentials free.

## Sources

- StatCounter, Mobile OS market share India (Sep 2026) — https://gs.statcounter.com/os-market-share/mobile/india (checked 2026-10)
- Kotlin releases (2.4.0, 3 Jun 2026) — https://kotlinlang.org/docs/releases.html (checked 2026-10)
- Navigation 3 release notes (1.0.0 stable, 19 Nov 2025) — https://developer.android.com/jetpack/androidx/releases/navigation3 (checked 2026-10)
- Room 3 release notes (3.0.3, 9 Sep 2026) — https://developer.android.com/jetpack/androidx/releases/room3 (checked 2026-10)
- Target API level requirements — https://developer.android.com/google/play/requirements/target-sdk ; 16 KB page sizes — https://developer.android.com/guide/practices/page-sizes ; Developer verification — https://developer.android.com/developer-verification (checked 2026-10)
- Foreground service timeouts — https://developer.android.com/develop/background-work/services/fgs/timeout (checked 2026-10)
- Android vitals thresholds — https://developer.android.com/topic/performance/vitals (checked 2026-10)
- Play Console Help, testing requirements for new personal developer accounts — https://support.google.com/googleplay/android-developer/answer/14151465 (checked 2026-10)
- Android 17 behaviour changes — https://developer.android.com/about/versions/17 (checked 2026-10)
- Gemini in Android Studio — https://developer.android.com/studio/gemini/overview (checked 2026-10)
- Android Developers Blog, Android Bench (8 Jul 2026) — https://android-developers.googleblog.com/2026/07/android-bench-llm-measurement.html (checked 2026-10)
- Zomato developer story — https://developer.android.com/stories/apps/zomato (checked 2026-10)

_Last reviewed: 2026-10_
