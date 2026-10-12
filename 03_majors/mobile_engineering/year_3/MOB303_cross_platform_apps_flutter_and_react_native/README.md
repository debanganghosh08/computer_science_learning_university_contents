# MOB303 · Cross-Platform Apps: Flutter and React Native

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [FND111](../../../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MOB403](../../year_4/MOB403_mobile_system_design/README.md), [MOB304](../MOB304_mobile_architecture_offline_first_and_sync/README.md) |

Part of the [Mobile Engineering major](../../README.md). Taken in the same semester as [MOB301](../MOB301_android_with_kotlin_and_jetpack_compose/README.md) and [MOB302](../MOB302_ios_with_swift_and_swiftui/README.md); Chapters 8–9 assume you have started both. [FE302 React](../../../frontend_engineering/year_3/FE302_react_and_component_architecture/README.md) is a helpful elective for the React Native half.

## Why this course matters now

Most startups and many large companies ship one codebase to both platforms, and the three serious options changed a lot between 2025 and 2026. React Native 0.82 (October 2025) was the first release to run entirely on the New Architecture, and 0.84 (February 2026) made the Hermes V1 engine the default. Flutter reached 3.47 in August 2026, with Widget Previews stable and its Impeller renderer replacing Skia on mobile. Kotlin Multiplatform and Compose Multiplatform are stable on Android and iOS, so teams can share logic, or logic and UI, in Kotlin. Swift 6.4 ships a Swift SDK for Android, making the opposite direction possible too. AI tools write cross-platform UI code fluently, and translating between frameworks is now cheap. Choosing the right approach is not: it depends on your team, your performance budget, how much platform API you need and who will maintain the code in three years. This course teaches all three approaches deeply enough to choose, and to drop into native code when the framework stops.

## Learning outcomes

By the end you can:

1. **Explain** how Flutter, React Native and Kotlin/Compose Multiplatform turn state into pixels, and **predict** where each will be slow.
2. **Build** a production-structured Flutter app with Dart, a state-management approach, navigation and tests.
3. **Build** a React Native app on the New Architecture with Expo, TypeScript and tests.
4. **Write** native modules for both (a Flutter plugin with Pigeon, a Turbo Native Module) in Kotlin and Swift.
5. **Share** business logic with Kotlin Multiplatform, and **integrate** it into native UIs on both platforms.
6. **Measure** startup, frame time, memory and app size of the same app built three ways, under the same conditions.
7. **Decide** between native, Flutter, React Native and KMP for a stated product and team, in a written architecture decision record (ADR).
8. **Apply** store rules to over-the-air code updates and plan a safe rollout.

## Chapters and lessons

### Chapter 1 · The landscape and how to choose (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Four rendering models | Own renderer (Flutter/Impeller); native views from JavaScript (React Native/Fabric); shared logic with native UI (KMP); shared Compose UI drawn by Skia on iOS (Compose Multiplatform) | Draw the path from a tap to a pixel for each |
| 1.2 Case studies | Airbnb's 2018 decision to sunset React Native; Dropbox's 2019 write-up on the hidden cost of shared C++; Shopify's 2020 move to React Native; Netflix's 2020 KMP studio apps | Summarise each decision's stated reasons in one table |
| 1.3 A decision framework | Team skills, performance needs, platform API surface, app size, hiring market, long-term ownership | Score three product briefs and defend the scores |
| 1.4 What AI changes | Translation between frameworks is cheap; architecture choices and native debugging are not | Translate one screen across frameworks with AI; list what broke |

**Check your understanding:** Why did Dropbox find shared C++ more costly than expected? Which kind of app suffers most from a non-native rendering model? What changes in the decision if the team is three web developers?

### Chapter 2 · Dart essentials (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Types and null safety | Sound null safety, `late`, generics, records and patterns, sealed classes, dot shorthands (Dart 3.10) | Model API results as a sealed hierarchy with exhaustive `switch` |
| 2.2 Async | `Future`, `Stream`, `async*`, event loop and microtasks | Predict the print order of 10 async snippets |
| 2.3 Isolates | Memory isolation, `Isolate.run`, when JSON parsing must leave the UI isolate | Parse a 20 MB JSON file without dropping frames |
| 2.4 Tooling | `dart analyze`, lints, `build_runner`, code generation trade-offs | Set strict analysis options and clear all warnings |

**Check your understanding:** Why does a long synchronous loop freeze a Flutter app even though Dart has async? What does "sound" null safety guarantee? When is an isolate worth its startup cost?

### Chapter 3 · Flutter UI internals (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Three trees | Widgets, Elements, RenderObjects; why rebuilding widgets is cheap | Trace a rebuild with the DevTools widget inspector |
| 3.2 Layout | "Constraints go down, sizes go up, parent sets position"; unbounded constraint errors | Fix five classic layout exceptions |
| 3.3 Keys and lists | `ValueKey`, `GlobalKey`, slivers, `ListView.builder` | Keep row state correct when a list reorders |
| 3.4 Rendering | Impeller, raster vs UI thread, layers, `RepaintBoundary` | Find a jank source with the DevTools performance view |
| 3.5 Platform look and accessibility | Material 3, Cupertino widgets, `Semantics`, text scaling | Pass TalkBack and VoiceOver checks on one screen |

**Check your understanding:** Why does a `Column` inside a `ListView` without bounds throw? When does a key change behaviour? Why can a frame be slow on the raster thread when your Dart code is fast?

### Chapter 4 · Flutter state, architecture and testing (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 State options | `setState`, `InheritedWidget`, Provider, Riverpod, Bloc: what each costs | Build one feature with two approaches; compare test code |
| 4.2 Architecture | Flutter's app architecture guide: views, view models, repositories, services | Restructure a sample app to the guide |
| 4.3 Navigation | `go_router`, deep links, nested navigation | Deep-link into a nested tab |
| 4.4 Testing | Unit, widget and golden tests; `integration_test` on devices | 30 widget tests and 4 golden tests in CI |
| 4.5 Local data and networking | `drift` or `sqflite`, `dio`/`http`, JSON code generation | An offline cache with typed errors |

**Check your understanding:** When does global state make testing harder? What does a golden test catch that a widget test misses? Where should a repository live in Flutter's recommended architecture?

### Chapter 5 · Flutter platform integration and performance (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Platform channels | Method and event channels, threading on each side | Read battery-saver state on both platforms |
| 5.2 Pigeon and FFI | Type-safe generated channels; `dart:ffi` for C libraries | Replace a hand-written channel with Pigeon |
| 5.3 Plugins and packages | Federated plugins, Swift Package Manager and Gradle integration, auditing dependencies | Audit five popular packages for maintenance and permissions |
| 5.4 Size and startup | `--analyze-size`, deferred components, tree shaking icons, release vs profile vs debug | Cut release size by 20% and explain each cut |
| 5.5 Add-to-app | Embedding Flutter in an existing native app; engine warm-up cost | Add a Flutter screen to the MOB301 app |

**Check your understanding:** Why must performance be measured in profile mode, not debug? What does a platform channel cost per call? When does add-to-app make sense for a large existing app?

### Chapter 6 · React Native on the New Architecture (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The architecture | JSI (JavaScript Interface), the Fabric renderer, Turbo Modules, Codegen, bridgeless mode; the legacy bridge is gone | Explain a state update from `setState` to a native view |
| 6.2 Hermes V1 | Bytecode precompilation, startup, memory; the default since 0.84 | Compare startup with and without bytecode precompilation |
| 6.3 Expo | Expo as the recommended framework, development builds, config plugins, EAS Build | Create an app with a config plugin that edits native files |
| 6.4 Over-the-air updates | JavaScript bundle updates (expo-updates), runtime versions, rollback; Google Play's policy exempts interpreted code with indirect API access, Apple's 2.5.2 limits feature changes | Ship a fix over the air to a test channel and roll it back |
| 6.5 Upgrading | React Native release cadence, strict TypeScript API (0.87), Android Gradle Plugin 9 and Node 22 minimums | Upgrade a two-version-old app; log every breaking change |

**Check your understanding:** What did removing the bridge change about synchronous calls to native code? Why must an OTA update be tied to a runtime version? What may an OTA update not change?

### Chapter 7 · React Native app engineering (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 React for mobile | React 19 features, effects and their cleanup, memoisation | Fix a screen that refetches on every render |
| 7.2 Navigation and state | Expo Router or React Navigation; Zustand or Redux Toolkit; TanStack Query for server state | Build list → detail → edit with cache invalidation |
| 7.3 Lists and animation | `FlatList` vs FlashList, Reanimated worklets, the new Animation Backend (0.85) | Scroll 5,000 rows at steady frame rate on a low-end device |
| 7.4 Testing | Jest, React Native Testing Library, end-to-end with Maestro or Detox | A Maestro flow for login and checkout |

**Check your understanding:** Why do worklets run animations smoothly while JavaScript is busy? What belongs in server-state caches versus app state? Why is a list with inline arrow functions slower?

### Chapter 8 · Native modules for both frameworks (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Turbo Native Modules | A typed spec, Codegen, Kotlin and Swift implementations | Expose secure storage (Keystore/Keychain) to JavaScript |
| 8.2 Native views | Fabric native components; Flutter platform views and their costs | Embed a native map view in both frameworks |
| 8.3 Lifecycle and threads | Activity/scene lifecycle events, main-thread rules, permissions from native code | Request a permission correctly from a module |
| 8.4 When to go native | Deciding per feature; keeping a native escape hatch | Write the rule your team will follow |

**Check your understanding:** Why must a native module never block the JavaScript thread? What do platform views cost in Flutter? How do you test a native module in CI?

### Chapter 9 · Kotlin Multiplatform and Compose Multiplatform (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 KMP basics | Targets, source sets, `expect`/`actual`, what is stable (Android, iOS, desktop) and what is beta (Wasm) | Share a validation and pricing module |
| 9.2 Shared data layer | Ktor client, `kotlinx.serialization`, Room 3 or SQLDelight, coroutines on iOS | One repository used by Android and iOS |
| 9.3 Swift interop | Objective-C header export, suspend functions and Flows from Swift, SKIE | Call a Flow from SwiftUI without leaks |
| 9.4 Compose Multiplatform | Shared UI on iOS, mixing with SwiftUI, accessibility and text input differences | One shared screen inside a native iOS app |
| 9.5 The other direction | Swift SDK for Android (Swift 6.4, NDK 30): status and trade-offs | Compile a small Swift library for Android |

**Check your understanding:** What does KMP share that Flutter does not force you to share? What is lost when Compose draws iOS UI instead of UIKit? How do you cancel a Kotlin coroutine from Swift?

### Chapter 10 · Measuring and deciding (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 A fair benchmark | Same features, release builds, same devices; startup, frame timing, memory, size, energy | Benchmark your P2 apps |
| 10.2 Total cost | Build times, upgrade effort, dependency risk, hiring | Estimate a two-year cost for each approach |
| 10.3 Architecture decision records | Context, options, decision, consequences, review date | Write an ADR for a real Indian startup brief (illustrative) |
| 10.4 Migration paths | Incremental adoption: add-to-app, brownfield React Native, KMP module by module | Plan a 6-month migration for a native app |

**Check your understanding:** Why is "Flutter is faster" or "React Native is faster" not a meaningful claim without a workload? What costs show up only in year two? When should an ADR be revisited?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Tap-to-pixel diagrams | Case-study table |
| 2 | 2 | Lab 2 · Dart async and isolates | — |
| 3 | 3 | Lab 3 · Flutter layout and rendering | — |
| 4 | 4 | Lab 4 · Flutter architecture and tests | **P1 due** |
| 5 | 4 | Lab 4 (cont.) | — |
| 6 | 5 | Lab 5 · Pigeon plugin and size | Size report |
| 7 | 6 | Lab 6 · React Native with Expo | Mid-term (AI off) |
| 8 | 6 | Lab 6 (cont.) · OTA update and rollback | — |
| 9 | 7 | Lab 7 · Lists, animation, Maestro | — |
| 10 | 8 | Lab 8 · Native modules both ways | **P2 due** |
| 11 | 9 | Lab 9 · KMP shared module | — |
| 12 | 9 | Lab 9 (cont.) | Swift interop demo |
| 13 | 10 | Lab 10 · Three-way benchmark | — |
| 14 | 10 | — | **P3 due** + ADR |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** translating a screen between Flutter, React Native and Compose; generating Pigeon or Codegen specs from a description; widget, golden and Jest test scaffolding; upgrade guides between versions. Claude Code, Cursor, GitHub Copilot, Gemini in Android Studio and Xcode 27's coding agents all help, and Flutter documents "agent-plugins" for AI tools.
- **Do without AI (drills):** Flutter layout exceptions; Dart and JavaScript event-loop ordering; a native module written by hand on both sides; the mid-term and final.
- **Verify AI output by:** (1) checking the framework version it assumed against the project's lockfile, because generated code often targets older APIs (the legacy React Native bridge, pre-Dart-3 syntax); (2) measuring in profile or release builds on a low-end device; (3) running the native module's tests on both platforms; (4) reading the license and maintenance status of every package it adds.
- **Where AI still fails here (collect your own evidence):** keep a log of generated code that used removed React Native legacy-architecture APIs, blocked the UI thread or isolate, added an abandoned package, or "fixed" a platform bug only on one platform. Bring the log to the Chapter 10 discussion.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 and ADR | 25% |
| AI failure log | 5% |

**Mastery gate.** You pass when you can, with AI tools off: (1) in 90 minutes, build a list-detail app with an offline cache in either Flutter or React Native, with tests; (2) in 45 minutes, add a native module that returns a value from Kotlin and Swift; (3) given benchmark numbers for three implementations, write a one-page recommendation that a reviewer cannot fault on method.

## Industry reality

Large companies have publicly gone in different directions. Airbnb's engineering team wrote in 2018 that it was sunsetting React Native, citing a mix of technical and organisational challenges. Dropbox described in 2019 why it stopped sharing C++ between its iOS and Android apps. Shopify announced in 2020 that new mobile apps would use React Native. Netflix described sharing Kotlin code across its Android and iOS studio apps in 2020. The lesson is not which framework wins, but that each decision was made for team and product reasons, then revisited.

**Interview questions from this course**

1. *Explain what happens between a tap and a screen update in React Native's New Architecture and in Flutter.* Strong answer: JSI and Fabric with a shadow tree committed to native views versus Flutter's widget/element/render trees painted by Impeller; where each can drop frames; threads involved.
2. *A Flutter list janks on first scroll. Diagnose it.* Strong answer: profile-mode measurement; UI vs raster thread in DevTools; oversized image decoding (`cacheWidth`); expensive builds; missing `RepaintBoundary`; confirms with frame timings on a low-end device.
3. *A three-person Indian fintech startup asks: native, Flutter, React Native or KMP?* Strong answer: asks about team skills, required platform APIs (UPI intents, biometrics, SMS retrieval), app size, security review needs and hiring; gives a reasoned choice with an exit path, not a slogan.
4. *How would you share code between iOS and Android without sharing UI?* Strong answer: KMP for domain and data layers; interop costs (Swift API shape, coroutine bridging); testing; what Dropbox learned about shared code ownership and tooling.
5. *What may an over-the-air JavaScript update change, and how do you ship one safely?* Strong answer: store-policy limits; runtime-version matching; staged rollout of the update; automatic rollback on crash spikes; never bypassing review for new features.

## Resources (free first)

- **Flutter and Dart:** Flutter docs — https://docs.flutter.dev/ ; app architecture guide — https://docs.flutter.dev/app-architecture ; Dart language tour — https://dart.dev/language
- **React Native:** docs — https://reactnative.dev/docs/getting-started ; New Architecture — https://reactnative.dev/architecture/landing-page ; Expo docs — https://docs.expo.dev/ ; React docs — https://react.dev/
- **Kotlin Multiplatform:** docs — https://kotlinlang.org/docs/multiplatform.html ; supported platforms — https://kotlinlang.org/docs/multiplatform/supported-platforms.html
- **Case studies:** Airbnb, "React Native at Airbnb" (2018) — https://medium.com/airbnb-engineering/react-native-at-airbnb-f95aa460be1c ; Dropbox, "The (not so) hidden cost of sharing code between iOS and Android" (2019) — https://dropbox.tech/mobile/the-not-so-hidden-cost-of-sharing-code-between-ios-and-android ; Shopify, "React Native is the Future of Mobile at Shopify" (2020) — https://shopify.engineering/react-native-future-mobile-shopify ; Netflix, "Netflix Android and iOS Studio Apps — now powered by Kotlin Multiplatform" (2020) — https://netflixtechblog.com/netflix-android-and-ios-studio-apps-kotlin-multiplatform-d6d4d8d25d23
- **Testing tools:** Maestro — https://maestro.dev/ ; React Native Testing Library — https://callstack.github.io/react-native-testing-library/

## Sources

- React Native blog: 0.80 (Jun 2025, legacy architecture frozen), 0.82 (Oct 2025, New Architecture only), 0.84 (Feb 2026, Hermes V1 default), 0.85 (Apr 2026), 0.86 (Jun 2026), 0.87 (Aug 2026) — https://reactnative.dev/blog (checked 2026-10)
- Flutter, What's new (3.38 Nov 2025; 3.41 Feb 2026; 3.44 May 2026; 3.47 Aug 2026) — https://docs.flutter.dev/release/whats-new (checked 2026-10)
- Kotlin, Multiplatform supported platforms and stability — https://kotlinlang.org/docs/multiplatform/supported-platforms.html (checked 2026-10)
- Swift.org, "Swift 6.4 Released" (Swift SDK for Android, 15 Sep 2026) — https://www.swift.org/blog/swift-6.4-released/ (checked 2026-10)
- Apple, App Review Guidelines 2.5.2 — https://developer.apple.com/app-store/review/guidelines/ (checked 2026-10)
- Google Play, Device and Network Abuse policy (self-updating apps; interpreter exception) — https://support.google.com/googleplay/android-developer/answer/9888379 (checked 2026-10)
- Case-study posts as listed under Resources (checked 2026-10)

_Last reviewed: 2026-10_
