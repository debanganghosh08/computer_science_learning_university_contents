# MOB · Mobile Engineering: interview question bank

| Role and market | Levels | Practise with | Score with |
|---|---|---|---|
| [MOB role page](../../01_market_map/roles/MOB_mobile_engineering.md) | NG → Mid → Sr | [Mock kit](../how_to_run_a_mock_with_any_llm.md) | [Rubrics](../rubrics.md) |

Mobile interviews test platform depth (lifecycles, concurrency, memory), product reliability on devices you do not control (crashes, slow networks, battery), and release discipline, because a bad release cannot be rolled back instantly on users' phones. Questions below cover Android (Kotlin) and iOS (Swift); answer for your platform and know the other at a conceptual level.

## 1. The typical loop

| Round | Duration | What it tests | AI policy you may meet | Mock brief |
|---|---|---|---|---|
| DSA coding | 45 min | Common at product companies | AI-off | Kit 4.1 |
| Platform deep dive | 45–60 min | Lifecycle, concurrency, memory, UI framework internals | AI-off | Kit 4.1 with a QUESTION from section 3 |
| Practical or take-home | 90 min live or a few hours | Build a small app that fetches, caches and displays data, with tests | Varies; take-homes increasingly allow AI with a live defence | Kit 4.10 adapted to mobile |
| Mobile system design | 60 min | Offline, sync, caching, background work, battery, release | AI-off | Kit 4.3 |
| Behavioural | 45 min | Crashes fixed, releases rolled back | AI-off | Kit 4.11 |

## 2. How to use this bank

Answer aloud with a timer, then open the guide. Build the practical questions in a real project. Tags show the lowest level at which each question is common.

## 3. Questions

### Platform fundamentals

**Q1 · NG · Android: the user rotates the phone mid-form. What is destroyed, and how do you keep their input?**

<details><summary>Answer guide</summary>

- **Testing:** Activity lifecycle and state.
- **Strong answer:** a configuration change destroys and recreates the Activity (unless handled manually). UI state that is cheap and small goes in saved instance state (survives process death too); screen data lives in a `ViewModel` (survives rotation but not process death); `SavedStateHandle` in the ViewModel covers both. Persistent data belongs in a database. Test process death with developer options.
- **Common mistakes:** disabling rotation; storing everything in the ViewModel and losing it on process death.
- **Follow-ups:** what survives when the system kills the app in the background?
</details>

**Q2 · NG · iOS: a view controller is never deallocated. Find the retain cycle.**

<details><summary>Answer guide</summary>

- **Testing:** ARC and reference cycles.
- **Strong answer:** ARC frees objects when the strong reference count reaches zero; a cycle (controller → closure → controller via `self`, or delegate declared strong, or timer targeting self) keeps both alive. Fix with `[weak self]` in escaping closures, `weak var delegate`, invalidating timers. Find it with the Memory Graph Debugger or Instruments' Leaks.
- **Common mistakes:** `unowned` everywhere (crashes if the object is gone).
- **Follow-ups:** when is `unowned` appropriate?
</details>

**Q3 · Mid · Kotlin coroutines: what happens when one child coroutine fails inside `viewModelScope`?**

<details><summary>Answer guide</summary>

- **Testing:** structured concurrency.
- **Strong answer:** with a regular `Job`, a failing child cancels its parent and siblings and the exception propagates; `viewModelScope` uses a `SupervisorJob`, so a failing top-level child does not cancel other children, but an unhandled exception still reaches the handler and can crash. Use `try/catch` inside the coroutine or a `CoroutineExceptionHandler`; `supervisorScope` for independent tasks. Cancellation is cooperative: check `isActive` or call suspending functions; never swallow `CancellationException`.
- **Common mistakes:** catching `Exception` generally and swallowing cancellation.
- **Follow-ups:** which dispatcher for disk I/O vs CPU work vs UI?
</details>

**Q4 · Mid · StateFlow, SharedFlow or a cold Flow for: screen state, one-off navigation events, a database query?**

<details><summary>Answer guide</summary>

- **Testing:** reactive streams on Android.
- **Strong answer:** screen state: `StateFlow` (always has a value, conflated, replays latest). One-off events: a `Channel` or `SharedFlow` with care, or better, model events as state that the UI consumes and acknowledges. Database query: cold `Flow` from Room that emits on change, converted with `stateIn` using `WhileSubscribed`. Collect with lifecycle awareness (`repeatOnLifecycle`).
- **Common mistakes:** navigation events in `StateFlow` re-firing after rotation.
- **Follow-ups:** why `WhileSubscribed(5000)` is a common choice.
</details>

**Q5 · Mid · Swift concurrency: an image cache is accessed from many tasks and occasionally crashes.**

<details><summary>Answer guide</summary>

- **Testing:** data races, actors.
- **Strong answer:** a dictionary mutated concurrently is a data race. Make the cache an `actor` (serialised access), or protect with a lock; mark UI updates `@MainActor`; enable strict concurrency checking so the compiler flags non-`Sendable` values crossing tasks. Deduplicate in-flight downloads by storing a `Task` per URL.
- **Common mistakes:** `DispatchQueue.main.async` sprinkled everywhere as a fix.
- **Follow-ups:** actor re-entrancy: what can change across an `await` inside an actor method?
</details>

**Q6 · Mid · SwiftUI: a view model resets every time the parent view updates.**

<details><summary>Answer guide</summary>

- **Testing:** SwiftUI ownership of state.
- **Strong answer:** a view model created with `@ObservedObject var vm = ViewModel()` is recreated whenever the view struct is re-initialised; the owning view should use `@StateObject` (or `@State` with the `@Observable` macro) so SwiftUI keeps it across updates; pass it down as `@ObservedObject` or via the environment. Explain that views are value descriptions, recreated often.
- **Common mistakes:** putting heavy work in view initialisers.
- **Follow-ups:** how do you test a SwiftUI view model in isolation?
</details>

**Q7 · Mid · Jetpack Compose: a list recomposes every item when one item changes.**

<details><summary>Answer guide</summary>

- **Testing:** recomposition and stability.
- **Strong answer:** recomposition skips composables whose inputs are stable and unchanged; unstable parameters (mutable classes, plain `List` from some modules) or lambdas recreated each time defeat skipping. Use immutable data classes, stable collections, `key` in `LazyColumn` items, `remember` for derived objects, and the Compose compiler reports or Layout Inspector recomposition counts to verify.
- **Common mistakes:** adding `remember` randomly.
- **Follow-ups:** `derivedStateOf`: when does it help?
</details>

### Performance and reliability

**Q8 · Mid · Cold start takes 4 seconds on mid-range phones. Improve it.**

<details><summary>Answer guide</summary>

- **Testing:** measurement-led optimisation.
- **Strong answer:** measure first (Android: Macrobenchmark and startup traces; iOS: Instruments App Launch). Common causes: heavy initialisation in `Application`/`AppDelegate` (SDKs, dependency graphs), disk I/O on the main thread, large layouts. Fixes: defer or lazily initialise, move I/O off the main thread, Baseline Profiles on Android to precompile hot paths, show content progressively. Set a budget and track it in CI.
- **Common mistakes:** optimising without a trace; adding a long splash screen.
- **Follow-ups:** a third-party SDK insists on early initialisation; options?
</details>

**Q9 · Mid · Scrolling a feed drops frames.**

<details><summary>Answer guide</summary>

- **Testing:** rendering performance on devices.
- **Strong answer:** a 60 Hz display gives about 16 ms per frame (less at 90 or 120 Hz). Look for main-thread work in bind or compose functions (image decoding, date formatting, JSON parsing), overdraw, deep layouts, large bitmaps. Tools: Perfetto or system traces, Android Studio profiler, Instruments Time Profiler and Core Animation. Fix: precompute view data off the main thread, downsample images, recycle views, avoid layout passes.
- **Common mistakes:** testing only on a flagship phone.
- **Follow-ups:** how do you monitor jank in production?
</details>

**Q10 · Mid · The crash-free rate dropped from 99.8% to 99.1% after a release.**

<details><summary>Answer guide</summary>

- **Testing:** release incident handling.
- **Strong answer:** halt the staged rollout immediately; group crashes by signature, device, OS version and app version in the crash reporter; read stack traces with symbolication (dSYMs, mapping files); disable the feature remotely if a flag exists; fix and release a patch; for Android check ANRs separately. Postmortem: why tests and staged rollout did not catch it earlier.
- **Common mistakes:** waiting for the next scheduled release.
- **Follow-ups:** the crash is only on one manufacturer's devices; how do you reproduce?
</details>

**Q11 · Mid · Android memory leak: an Activity stays in memory after the user leaves.**

<details><summary>Answer guide</summary>

- **Testing:** leak causes on Android.
- **Strong answer:** common causes: a static field or singleton holding an Activity `Context` or a `View`; listeners not unregistered; long-running coroutines or threads referencing the Activity; inner classes holding implicit references. Detect with LeakCanary or heap dumps; fix with application context where appropriate, lifecycle-aware components, and cancelling work in the right scope.
- **Common mistakes:** calling `System.gc()`.
- **Follow-ups:** how do you add leak detection to CI?
</details>

### Data, networking and offline

**Q12 · Mid · Offline-first notes app.**

<details><summary>Answer guide</summary>

- **Testing:** local-first architecture.
- **Strong answer:** the local database (Room, Core Data or SQLite) is the source of truth for the UI; writes go locally first with a pending-sync flag; a sync engine pushes changes with client-generated IDs and versions, pulls server changes since a cursor, and resolves conflicts (last-writer-wins per field, or merge, or user choice for text); retries with backoff when connectivity returns; migrations for the local schema.
- **Common mistakes:** UI reading directly from the network; no conflict strategy.
- **Follow-ups:** the same note edited on two devices offline.
</details>

**Q13 · Mid · Image-heavy feed: loading and caching strategy.**

<details><summary>Answer guide</summary>

- **Testing:** resource management.
- **Strong answer:** a memory cache (LRU sized to a share of available memory) plus a disk cache; downsample to the display size before decoding; request the right size from a CDN; prefetch upcoming items; cancel loads for recycled cells; placeholders with fixed aspect ratios; use a mature library (Coil, Glide, or similar on iOS) and know what it does.
- **Common mistakes:** decoding full-resolution images for thumbnails.
- **Follow-ups:** low-memory warnings; data-saver mode.
</details>

**Q14 · Mid · Upload a 500 MB video reliably even if the user leaves the app.**

<details><summary>Answer guide</summary>

- **Testing:** background execution limits.
- **Strong answer:** Android: `WorkManager` with network constraints, foreground service type for user-visible long uploads as the platform requires. iOS: a background `URLSession` upload task that the system continues. Use resumable, chunked uploads (server supports offsets), checksums per chunk, retry with backoff, and progress persisted locally. Respect metered networks and battery.
- **Common mistakes:** a plain thread or coroutine that dies when the app is killed.
- **Follow-ups:** the server must not create duplicate videos when the client retries.
</details>

**Q15 · NG · Paginated list from an API.**

<details><summary>Answer guide</summary>

- **Testing:** list UI basics.
- **Strong answer:** cursor-based paging from the API; load the next page near the end of the list; loading and error footer with retry; deduplicate items; preserve scroll position on configuration change; use the platform paging library (Android Paging) or a simple state machine; pull-to-refresh resets the cursor.
- **Common mistakes:** loading the same page twice when the user scrolls quickly.
- **Follow-ups:** items are inserted at the top while the user scrolls.
</details>

### Security

**Q16 · Mid · Where and how do you store the user's refresh token?**

<details><summary>Answer guide</summary>

- **Testing:** mobile secure storage.
- **Strong answer:** iOS Keychain with an appropriate accessibility class; Android: encrypt with a key held in the Android Keystore (hardware-backed where available) and store the ciphertext in app-private storage. Never in plain preferences, logs or backups. Short-lived access tokens; rotate refresh tokens; revoke server-side on logout or device loss. Discuss certificate pinning trade-offs (protects against some interception, but needs a rotation plan to avoid locking users out).
- **Common mistakes:** "app storage is private, so plain text is fine".
- **Follow-ups:** rooted or jailbroken devices: what can and cannot you do?
</details>

**Q17 · Mid · Deep links open screens with parameters. What must the app validate?**

<details><summary>Answer guide</summary>

- **Testing:** defensive handling of external input.
- **Strong answer:** treat every deep-link parameter as untrusted input: validate types and allowed values, never use it to build file paths or web view URLs without an allow-list, require authentication for sensitive screens, never perform state-changing actions (payments, deletes) directly from a link without user confirmation. Use verified App Links or Universal Links so other apps cannot claim your domain.
- **Common mistakes:** a deep link that triggers an action immediately.
- **Follow-ups:** how do you test deep-link handling automatically?
</details>

### Mobile system design

**Q18 · Mid · Offline-capable chat app (client side).**

<details><summary>Answer guide</summary>

- **Testing:** mobile system design.
- **Strong answer:** local message store as source of truth; outgoing queue with client message IDs and states (sending, sent, delivered, read, failed); persistent connection while foregrounded, push notifications when backgrounded; sync on reconnect by per-conversation cursor; media upload separate from message send; pagination of history; encryption at rest if required; battery-aware reconnection with backoff.
- **Common mistakes:** keeping a socket open in the background indefinitely.
- **Follow-ups:** message ordering when the device clock is wrong.
</details>

**Q19 · Mid · A payment screen that hands off to a UPI app and returns (illustrative scenario).**

<details><summary>Answer guide</summary>

- **Testing:** handling external flows and uncertain outcomes.
- **Strong answer:** create the payment on your server first with an idempotency key; launch the payment app via the intent or SDK; on return, treat the client-side result as a hint only; show "confirming" and poll your server (which gets the authoritative status from the payment provider via webhook or status API) with a timeout; handle pending states that resolve later; prevent double payment by disabling retry while a payment is pending; clear messaging to the user.
- **Common mistakes:** marking an order paid from the client callback.
- **Follow-ups:** the app is killed while the user is in the payment app.
</details>

**Q20 · Sr · Design the release process for an app with 10 million users.**

<details><summary>Answer guide</summary>

- **Testing:** release engineering on mobile.
- **Strong answer:** trunk-based development with feature flags; automated tests and device-farm runs; internal and beta tracks; staged rollout (1%, 5%, 20%, 50%, 100%) gated on crash-free rate and key metrics; remote kill switches; backward-compatible APIs because old app versions live for months; minimum supported version and a forced-update mechanism for security issues; release notes and on-call during rollout.
- **Common mistakes:** server changes that break old app versions.
- **Follow-ups:** how long do you support old versions, and how do you decide?
</details>

**Q21 · Sr · Design an analytics SDK for the company's apps.**

<details><summary>Answer guide</summary>

- **Testing:** platform SDK design.
- **Strong answer:** an event schema with versioning; local batching to disk, upload on good connectivity and battery, with size limits; consent management (no collection before consent where law requires); PII minimisation; sampling; clock-skew handling; minimal startup cost (lazy init); a tiny public API; tests and a debug view for product teams.
- **Common mistakes:** a network request per event.
- **Follow-ups:** events lost when the app crashes; how do you measure SDK data loss?
</details>

### Testing

**Q22 · Mid · Testing strategy for a mobile app.**

<details><summary>Answer guide</summary>

- **Testing:** test pyramid for devices.
- **Strong answer:** unit tests for view models and domain logic; UI tests (Espresso or Compose testing, XCUITest) for key flows with fake network; screenshot tests for components across themes and font sizes; a small set of end-to-end tests on a device farm covering OS versions and screen sizes; accessibility checks (TalkBack, VoiceOver, dynamic type). Flaky UI tests: idling resources, deterministic test data.
- **Common mistakes:** only manual testing before release.
- **Follow-ups:** which devices do you choose for the farm, and how?
</details>

### AI-era review

**Q23 · Mid · Review this AI-generated ViewModel.**

```kotlin
class ProfileViewModel(private val api: Api) : ViewModel() {
    var profile: Profile? = null
    private val _ui = MutableLiveData<UiState>()
    fun load(id: String) {
        GlobalScope.launch(Dispatchers.IO) {
            profile = api.getProfile(id)
            _ui.value = UiState.Loaded(profile!!)
        }
    }
}
```

<details><summary>Answer guide</summary>

- **Testing:** catching subtle lifecycle and threading bugs.
- **Strong answer:** (1) `GlobalScope` outlives the ViewModel, leaking work and possibly updating a dead screen; use `viewModelScope`. (2) `MutableLiveData.value` must be set on the main thread; from `Dispatchers.IO` it throws; use `postValue` or, better, a `StateFlow`. (3) No error handling: a network failure crashes the coroutine; catch and emit an error state. (4) `!!` and a public mutable `profile` duplicate state; expose immutable state only. (5) Repeated calls launch duplicate loads; cancel the previous job.
- **Common mistakes:** fixing only the scope.
- **Follow-ups:** write a unit test for this ViewModel with a fake API and a test dispatcher.
</details>

**Q24 · Mid · The assistant suggests trusting all certificates to fix "SSL handshake failed" against staging. Would you merge it?**

<details><summary>Answer guide</summary>

- **Testing:** security judgement on AI suggestions.
- **Strong answer:** no. Disabling certificate validation makes every connection open to interception, and such code often leaks into release builds. Fix the real cause: install the staging certificate authority only for debug builds (Android network security configuration with debug overrides; an iOS debug-only configuration), or get a valid certificate for staging. Add a CI check that release builds contain no trust-all code.
- **Common mistakes:** "it is only for staging".
- **Follow-ups:** how would you detect this pattern automatically in code review?
</details>

**Q25 · Sr · Design an on-device AI feature, such as smart replies.**

<details><summary>Answer guide</summary>

- **Testing:** constraints of on-device ML.
- **Strong answer:** decide on-device vs server by privacy, latency, offline needs and cost; model size and download strategy (on-demand delivery, not in the base app); quantisation and hardware acceleration via the platform's ML runtime; latency and battery budgets measured on low-end devices; graceful fallback; evaluation of quality per language (including Hindi and code-mixed text) before rollout; a feature flag and staged rollout; telemetry without collecting message content.
- **Common mistakes:** testing only on flagship phones; logging user text for evaluation without consent.
- **Follow-ups:** how do you update the model without an app release?
</details>

### Behavioural

**Q26 · Mid · Tell me about a release you halted or rolled back.**

<details><summary>Answer guide</summary>

- **Testing:** ownership and judgement under uncertainty.
- **Strong answer:** the signal you saw and how quickly; the decision to halt and who you informed; how users were protected (remote flag, halted rollout, patch); root cause; what changed in the release checklist or monitoring.
- **Common mistakes:** a story where someone else made every decision.
- **Follow-ups:** a time you decided not to roll back; was it right?
</details>

## Sources

- Android Developers documentation (lifecycle, coroutines, WorkManager, App Links, Baseline Profiles; checked October 2026): https://developer.android.com/
- Apple Developer documentation (Swift concurrency, SwiftUI, background URLSession, Keychain; checked October 2026): https://developer.apple.com/documentation/
- Loop structure: [MOB role page](../../01_market_map/roles/MOB_mobile_engineering.md).

_Last reviewed: 2026-10_
