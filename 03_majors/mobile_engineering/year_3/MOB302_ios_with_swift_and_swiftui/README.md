# MOB302 · iOS with Swift and SwiftUI

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [FND111](../../../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MOB402](../../year_4/MOB402_on_device_ai_for_mobile/README.md), [MOB304](../MOB304_mobile_architecture_offline_first_and_sync/README.md), [MOB305](../MOB305_mobile_integrations_payments_maps_notifications/README.md), [MOB401](../../year_4/MOB401_mobile_performance_security_and_release/README.md) |

Part of the [Mobile Engineering major](../../README.md). You need a Mac with Xcode for the labs; a physical iPhone helps but is not required until P3. Shared lab Macs or a cloud Mac service are acceptable.

## Why this course matters now

iOS had 6.05% of India's mobile OS share in September 2026 (StatCounter), but almost every consumer product that sells globally, and many Indian fintech and commerce apps, ship an iPhone app, and iOS teams are small and senior. The platform shifted in 2026: Swift 6.4 shipped in September with async `defer` blocks and a cancellation shield; iOS 27 and Xcode 27 arrived the same month; a foldable "iPhone Duo" ships on 23 October 2026, so layouts must adapt to new postures. Since 28 April 2026 every upload must be built with Xcode 26 or later, and from April 2027 with the iOS 27 SDK. Xcode 27 runs coding agents from Anthropic, Google and OpenAI inside the IDE. They write SwiftUI quickly. They are much less reliable on what this course drills: data-race safety under Swift 6, retain cycles, actor reentrancy, and the review guidelines that decide whether your app ships at all.

## Learning outcomes

By the end you can:

1. **Write** idiomatic Swift with value types, enums with associated values, protocols, generics and typed errors.
2. **Find and fix** memory leaks and retain cycles with ARC knowledge, the Memory Graph debugger and Instruments.
3. **Build** concurrent code with async/await, task groups, actors and `@MainActor`, and **compile** it cleanly in the Swift 6 language mode with complete data-race checking.
4. **Build** SwiftUI interfaces with correct identity, layout and data flow using the Observation framework, and **diagnose** excess view updates.
5. **Persist** data with SwiftData or Core Data and **store** secrets in the Keychain.
6. **Integrate** networking, background tasks, notifications, widgets and App Intents within iOS limits.
7. **Test** with Swift Testing, XCTest and XCUITest, and **measure** launch time and hangs.
8. **Ship** through TestFlight and App Store review, **anticipating** the guidelines most often hit by new apps.

## Chapters and lessons

### Chapter 1 · Swift for app engineers (weeks 1–2)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Value and reference types | `struct` vs `class`, copy-on-write, `let` semantics | Show a bug caused by shared class state; fix it with a struct |
| 1.2 Optionals and enums | Optional chaining, `guard let`, enums with associated values, exhaustive `switch` | Model an order state machine where illegal states cannot exist |
| 1.3 Protocols and generics | Protocol extensions, associated types, `some` vs `any` (and Swift 6.4's optional `some`/`any` without parentheses) | Write a generic, testable `Repository` protocol |
| 1.4 Errors | `throws`, typed throws, `Result`, mapping errors for the UI | Turn five failure modes of a network call into user-facing messages |
| 1.5 Closures | Capturing, `@escaping`, capture lists | Predict the output of 10 closure-capture puzzles |

**Check your understanding:** When does a `struct` containing an array get copied? Why prefer `some View` over `any View` in SwiftUI? What does a capture list change about lifetime?

### Chapter 2 · Memory and ARC (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Automatic Reference Counting | Retain/release, strong, `weak`, `unowned`, deinit timing | Trace reference counts through a view controller lifecycle |
| 2.2 Retain cycles | Closures stored on `self`, delegates, timers, `Task` capturing `self` | Find three planted cycles with the Memory Graph debugger |
| 2.3 Instruments | Allocations, Leaks, VM tracker; memory warnings and jetsam (the system killing apps for memory) | Profile an image grid; cut peak memory by half |
| 2.4 Ownership | Noncopyable types (`~Copyable`), `borrowing`/`consuming`, `Span` | Model a one-time token that cannot be copied |

**Check your understanding:** Why does `[weak self]` in a long-running `Task` not always prevent work after the screen closes? When is `unowned` safe? What does jetsam do that a desktop OS would not?

### Chapter 3 · Swift concurrency (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 async/await and tasks | Suspension points, `Task`, `async let`, `TaskGroup`, structured vs unstructured tasks | Load a profile, its orders and offers in parallel with correct cancellation |
| 3.2 Cancellation | Cooperative cancellation, `Task.checkCancellation`, Swift 6.4's `withTaskCancellationShield` for cleanup and async `defer` | Cancel a search when the query changes; prove cleanup still runs |
| 3.3 Actors and isolation | Actor isolation, reentrancy across `await`, global actors, `@MainActor` | Fix a cache actor whose invariant breaks across an `await` |
| 3.4 Sendable and data-race safety | `Sendable`, the Swift 6 language mode, Swift 6.2's approachable-concurrency settings (default main-actor isolation) | Migrate a module to Swift 6 mode with zero warnings |
| 3.5 AsyncSequence | `AsyncStream`, bridging delegate and callback APIs, backpressure | Wrap a location delegate as an `AsyncStream` |

**Check your understanding:** An actor method reads state, awaits a network call, then writes state. What can go wrong? Why does `Sendable` matter even on a single-core phone? When should code leave the main actor?

### Chapter 4 · SwiftUI fundamentals (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Views as values | `body` as a function of state; why views are cheap structs | Explain when `body` runs, using `Self._printChanges()` |
| 4.2 Layout | Propose–size–place; stacks, `Grid`, `ViewThatFits`, custom `Layout` | Build a layout that adapts from iPhone to iPad without size checks |
| 4.3 Identity | Structural vs explicit identity, `id(_:)`, `ForEach` with stable IDs | Fix a list where row state jumps after reordering |
| 4.4 Lists and performance | `List`, lazy stacks, iOS 27's lazily loaded, prefetching subviews | Scroll 10,000 rows without hitches in Instruments |
| 4.5 Animation and design | Implicit vs explicit animations, transitions, current system materials and navigation bars | Animate an expanding card with a matched geometry effect |
| 4.6 Accessibility | VoiceOver labels and traits, Dynamic Type up to accessibility sizes, Reduce Motion | Pass an Accessibility Inspector audit on one flow |

**Check your understanding:** Why does replacing `ForEach(items.indices)` with `ForEach(items)` fix animation bugs? What does the layout system do when a child ignores the proposed size? Why test at the largest Dynamic Type size?

### Chapter 5 · Data flow (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Local state | `@State`, `@Binding`, `@FocusState` | A form with validation and focus control |
| 5.2 Observation | `@Observable` models, property-level tracking, `@Bindable`, `@Environment` | Measure update counts before/after moving from `ObservableObject` |
| 5.3 Architecture | MVVM in SwiftUI, unidirectional patterns, The Composable Architecture (TCA) as a case | Build one feature twice (MVVM, reducer-style); compare tests |
| 5.4 Dependency injection | Environment values, protocol witnesses, previews with fakes | Run the same view with live, fake and failing dependencies in previews |

**Check your understanding:** Why does `@Observable` update fewer views than `ObservableObject`? Where should a network call live in SwiftUI? What makes a view hard to preview?

### Chapter 6 · Navigation, scenes and adaptive apps (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 NavigationStack | Value-based navigation, path as state, restoration | Restore a three-level path after relaunch |
| 6.2 Split views and multiplatform | `NavigationSplitView`, size classes, iPad multitasking | One codebase for iPhone and iPad |
| 6.3 New form factors | iPhone Duo postures, Device Hub testing in Xcode 27.1 | Test a flow across poses and orientations |
| 6.4 App lifecycle | `App`, `Scene`, `scenePhase`, `onOpenURL` | Handle a deep link while the app is cold, backgrounded and foregrounded |

**Check your understanding:** Why store the navigation path as data? How should an app react to `scenePhase` becoming `.background`? What breaks when a layout assumes a fixed screen width?

### Chapter 7 · Persistence (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 SwiftData | `@Model`, `ModelContainer`, `#Predicate`, `@Query`, background contexts | A notes app with tags and search |
| 7.2 Migrations | `VersionedSchema`, `SchemaMigrationPlan`, lightweight vs custom | Ship v1 → v2 → v3; test upgrade from v1 |
| 7.3 Core Data and SQLite | Contexts, faulting, batch operations; when GRDB or raw SQLite wins | Import 50,000 rows with Core Data batch insert; compare times |
| 7.4 Keychain and files | Keychain items and access control, file protection classes, app groups | Store a refresh token so it is unreadable before first unlock |

**Check your understanding:** What does a file protection class protect against, and what not? When would you pick Core Data over SwiftData in 2026? Why test the upgrade from the oldest supported schema?

### Chapter 8 · Networking (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 URLSession with async/await | Requests, `Codable`, custom decoding, typed errors | Client for a public API with full error mapping |
| 8.2 Resilience | Timeouts, retries with jitter for idempotent calls, `NWPathMonitor` | Survive a mock server with 30% failures |
| 8.3 Caching and images | `URLCache`, `ETag`, `AsyncImage` limits, downsampling with Image I/O | Halve memory on an image grid |
| 8.4 Background transfers | Background `URLSession` for uploads that continue after suspension | Upload 20 photos; kill the app; confirm completion |

**Check your understanding:** Why does a background `URLSession` survive app suspension when an `async` call does not? What can go wrong decoding dates from a server? Which calls may be retried automatically?

### Chapter 9 · System integration and background work (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Background execution | `BGAppRefreshTask` (opportunistic), `BGProcessingTask`, `BGContinuedProcessingTask` for user-started work | Log when the system actually runs your refresh over two days |
| 9.2 Notifications | `UNUserNotificationCenter`, provisional authorization, categories and actions (push in MOB305) | A reminder flow with an actionable notification |
| 9.3 Widgets and Live Activities | WidgetKit timelines, interactive widgets, ActivityKit basics | A widget that never shows stale data without a timestamp |
| 9.4 App Intents | Intents, entities, Shortcuts; iOS 27 entity schemas for the Spotlight semantic index; the App Intents Testing framework | Expose "add expense" as an intent and test it |
| 9.5 Permissions and purpose strings | Camera, photos (limited library), location, contacts; writing honest purpose strings | Make every feature work with the most limited grant |

**Check your understanding:** Why can't you schedule a background refresh for an exact time? How should a widget behave when its data is old? What does an App Intent expose to the system, and what must you validate?

### Chapter 10 · Testing and tooling (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Swift Testing | `@Test`, `#expect`, parameterised tests, traits; mixing with XCTest | Port 20 XCTests; add parameterised edge cases |
| 10.2 UI tests | XCUITest, accessibility identifiers, launch arguments for fakes | An end-to-end checkout test with a fake server |
| 10.3 Snapshot tests | Testing light/dark, Dynamic Type and locales | Catch a planted truncation in Hindi |
| 10.4 Launch and hangs | `XCTApplicationLaunchMetric`, Instruments Time Profiler and Hangs, Xcode Organizer | Cut launch time by deferring work from `init` |

**Check your understanding:** What does a UI test prove that a snapshot test cannot? Why measure launch on a device rather than the simulator? What counts as a hang?

### Chapter 11 · Shipping through the App Store (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Signing | Certificates, provisioning profiles, capabilities and entitlements; automatic vs manual signing | Archive and upload with no manual Keychain steps |
| 11.2 TestFlight | Internal and external testers, beta review, feedback | Run a TestFlight build with 10 external testers |
| 11.3 Review realities | 4.8 equivalent login option; 5.1.1(v) in-app account deletion; 3.1.1 in-app purchase for digital unlocks vs 3.1.3(e) other methods for physical goods; 2.5.2 no downloaded code that changes features; 5.1.2 consent, including disclosure of sharing with third-party AI | Pre-review your P3 against these and write the evidence |
| 11.4 Privacy requirements | Privacy nutrition labels, privacy manifests and required-reason APIs (since May 2024), App Tracking Transparency, age-rating questionnaire | Produce a privacy manifest that matches your SDKs |
| 11.5 Release | SDK minimums (Xcode 26 now, iOS 27 SDK from April 2027), phased release over 7 days, expedited review, responding in Resolution Center | Write a release checklist and a rejection-response template |

**Check your understanding:** Your app offers Google sign-in only: what does 4.8 require? A food app sells meal subscriptions delivered to homes: which payment rule applies? Why might an app that downloads JavaScript feature bundles be rejected?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Swift katas | — |
| 2 | 1 | Lab 1 (cont.) | Order state machine |
| 3 | 2 | Lab 2 · Leak hunt | Leak report |
| 4 | 3 | Lab 3 · Concurrency | **P1 due** |
| 5 | 3–4 | Lab 3 (cont.) | Swift 6 migration with zero warnings |
| 6 | 4 | Lab 4 · SwiftUI identity and layout | — |
| 7 | 5 | Lab 5 · Observation | Mid-term (AI off) |
| 8 | 6 | Lab 6 · Navigation and adaptive layout | — |
| 9 | 7 | Lab 7 · SwiftData migrations | — |
| 10 | 8 | Lab 8 · Resilient networking | **P2 due** |
| 11 | 9 | Lab 9 · Background tasks and widgets | — |
| 12 | 9 | Lab 9 (cont.) | App Intents demo |
| 13 | 10 | Lab 10 · Tests and launch time | — |
| 14 | 11 | TestFlight | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** SwiftUI layout drafts from a sketch; `Codable` models from JSON; test scaffolding; explaining a crash log or a compiler concurrency diagnostic; first drafts of purpose strings and review notes. Xcode 27's coding agents (models from Anthropic, Google or OpenAI), Claude Code, Cursor and GitHub Copilot all do this.
- **Do without AI (drills):** the leak hunt; actor reentrancy and `Sendable` fixes by hand; a weekly 45-minute "list → detail with loading and error states" build; the mid-term and final.
- **Verify AI output by:** (1) compiling in Swift 6 language mode with complete concurrency checking; (2) running Instruments Leaks and the Memory Graph after the feature is used and dismissed; (3) checking every API against developer.apple.com for the current SDK; (4) testing at the largest Dynamic Type size and with VoiceOver; (5) reading the relevant review guideline yourself.
- **Where AI still fails here (collect your own evidence):** log each generated change that (a) silenced a concurrency diagnostic with `@unchecked Sendable` or `nonisolated(unsafe)` instead of fixing it; (b) created a retain cycle through a stored closure or `Task`; (c) used a deprecated API or a pre-Observation pattern; (d) would break a review guideline (for example sign-in without an equivalent option). The log is graded.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 25% |
| AI failure log | 5% |

**Mastery gate.** You pass when you can, with AI tools off and in 2 hours: build a two-screen SwiftUI app that loads a paginated API into SwiftData, shows loading, error and empty states, cancels in-flight work when the user leaves, compiles in Swift 6 mode with no warnings, and has no leaks in the Memory Graph after ten open/close cycles; then explain a planted actor-reentrancy bug and fix it.

## Industry reality

Apple's requirements are engineering deadlines: the Xcode 26 SDK minimum since April 2026, the iOS 27 SDK from April 2027, privacy manifests since May 2024, and age-rating questions that had to be answered by January 2026. App Store review applies the guidelines quoted in Chapter 11 to every build. Payscale's whole-market average base for an iOS developer in India was ₹7.8 lakh (129 profiles, May 2026), a small sample ([MOB market page](../../../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md)).

**Interview questions from this course**

1. *A view model stores a closure that references `self`. The screen closes but memory grows. Explain and fix.* Strong answer: retain cycle through the stored closure; capture lists; `Task` capturing `self` keeps it alive until the task ends; shows how the Memory Graph debugger confirms the fix.
2. *What does `@MainActor` guarantee, and what does an actor not guarantee?* Strong answer: isolation means one task touches the state at a time, but state can change across any `await` (reentrancy); re-check invariants after suspension; `Sendable` for values that cross isolation boundaries.
3. *A SwiftUI list re-renders too often and stutters. Diagnose it.* Strong answer: unstable identity, a model that invalidates too broadly, expensive `body`, image decoding on the main thread; uses `_printChanges`, the SwiftUI and Hangs instruments, and measures on a device.
4. *SwiftData, Core Data or SQLite for an offline app with 100,000 rows and sync?* Strong answer: compares migration tooling, batch operations, concurrency model, query control and testability; picks based on sync needs; plans the upgrade path from the oldest schema.
5. *Your app was rejected under guideline 4.8 or 5.1.1(v). What do you do?* Strong answer: reads the guideline, fixes rather than argues where it applies, adds Sign in with Apple or another compliant option or in-app deletion, replies in Resolution Center with evidence, and adds the check to the release checklist.

## Resources (free first)

- **Language:** *The Swift Programming Language* — https://docs.swift.org/swift-book/ ; Swift Evolution proposals — https://www.swift.org/swift-evolution/
- **Courses:** Apple's Develop in Swift and SwiftUI tutorials — https://developer.apple.com/tutorials/swiftui ; Stanford CS193p (Developing Apps for iOS) — https://cs193p.sites.stanford.edu/ ; Hacking with Swift, 100 Days of SwiftUI — https://www.hackingwithswift.com/100/swiftui
- **Documentation:** SwiftData — https://developer.apple.com/documentation/swiftdata ; Background tasks — https://developer.apple.com/documentation/backgroundtasks ; App Intents — https://developer.apple.com/documentation/appintents ; Human Interface Guidelines — https://developer.apple.com/design/human-interface-guidelines/
- **Policy:** App Review Guidelines — https://developer.apple.com/app-store/review/guidelines/ ; Upcoming requirements — https://developer.apple.com/news/upcoming-requirements/
- **Case study code:** The Composable Architecture — https://github.com/pointfreeco/swift-composable-architecture
- **Paid, optional:** WWDC session videos are free; paid courses (for example Point-Free) go deeper on architecture but are not required.

## Sources

- Swift.org, "Swift 6.4 Released" (15 Sep 2026) — https://www.swift.org/blog/swift-6.4-released/ (checked 2026-10)
- Apple Developer News: App Store submissions open for iOS 27 and Xcode 27, iOS 27 SDK required from April 2027 (9 Sep 2026); iPhone Duo (5 Oct 2026) — https://developer.apple.com/news/ (checked 2026-10)
- Apple, Upcoming requirements (Xcode 26 SDK since 28 Apr 2026; iOS 13 minimum target since 9 Sep 2026; privacy manifests since 1 May 2024; age ratings) — https://developer.apple.com/news/upcoming-requirements/ (checked 2026-10)
- Apple, What's new in iOS 27 — https://developer.apple.com/ios/whats-new/ ; Xcode — https://developer.apple.com/xcode/ (checked 2026-10)
- Apple, App Review Guidelines (4.8, 5.1.1(v), 3.1.1, 3.1.3(e), 2.5.2, 5.1.2) — https://developer.apple.com/app-store/review/guidelines/ (checked 2026-10)
- StatCounter, Mobile OS market share India (Sep 2026) — https://gs.statcounter.com/os-market-share/mobile/india (checked 2026-10)
- Payscale India, iOS Developer (May 2026) — https://www.payscale.com/research/IN/Job=iOS_Developer/Salary (checked 2026-10)

_Last reviewed: 2026-10_
