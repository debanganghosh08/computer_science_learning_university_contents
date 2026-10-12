# MOB302 · Labs and projects

All code compiles in the Swift 6 language mode with complete concurrency checking, and every lab ends with a Memory Graph check after the feature has been opened and closed ten times. Launch and hang measurements are taken on a physical device in a release build when one is available; otherwise report simulator numbers and label them. Labs 2 and 3 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Swift katas | Value semantics, enums with associated values, generics, typed throws | Passing tests; a short note on each `struct` vs `class` choice | 5 h |
| 2 · Leak hunt (no AI) | Find and fix five planted retain cycles (stored closures, delegates, timers, `Task`, notification observers) | Memory Graph screenshots before and after; one-line cause for each | 4 h |
| 3 · Concurrency and Swift 6 migration (no AI) | Parallel loading with task groups; a cache actor with a reentrancy bug; migrate a module to Swift 6 mode | Zero concurrency warnings; a test that fails before the reentrancy fix and passes after | 7 h |
| 4 · SwiftUI identity and layout | Fix identity bugs in a reorderable list; build a custom `Layout` | Video of correct row state after reorder; layout tests at three widths | 5 h |
| 5 · Observation | Move a screen from `ObservableObject` to `@Observable` | `_printChanges` logs showing fewer view updates | 4 h |
| 6 · Navigation and adaptive layout | Path-based navigation with restoration; iPhone, iPad and iPhone Duo postures in Device Hub | Screenshots per posture; deep-link test for cold and warm launch | 5 h |
| 7 · SwiftData migrations | Three schema versions with a custom migration step | Tests upgrading from v1 and v2 to v3 with seeded data | 5 h |
| 8 · Resilient networking | Client against a mock server with failures, slow responses and `304`s; a background upload session | Error-rate report; proof that uploads finish after the app is killed | 5 h |
| 9 · Background tasks, widgets and App Intents | A refresh task, a widget with honest staleness, an App Intent with tests | Two-day log of when refresh ran; App Intents test results | 6 h |
| 10 · Tests and launch time | Swift Testing suite, an XCUITest flow, snapshot tests in English and Hindi, `XCTApplicationLaunchMetric` | CI run; launch time before and after deferring work | 5 h |

## Projects

### P1 · Bilingual flashcards with spaced repetition (L1, ~6 hours)

**Real-world inspiration:** spaced-repetition apps schedule each card just before you would forget it. The SM-2 algorithm, published for SuperMemo in the late 1980s, is simple enough to implement and test in an afternoon.

**What to build:** decks of cards (for example Hindi–English vocabulary), SM-2 scheduling, a daily review screen, statistics, all stored with SwiftData. No network.

**Acceptance criteria:**
- **Correctness:** at least 20 Swift Testing cases for SM-2 (first review, failed recall, ease floor of 1.3, long intervals), all passing.
- **Concurrency:** compiles in Swift 6 mode with zero warnings and no `@unchecked Sendable`.
- **State:** the review session restores after the app is terminated mid-deck.
- **Accessibility:** every control has a VoiceOver label; no truncated text at the largest accessibility text size (snapshot test).
- **Memory:** no leaks after ten open/close cycles of the review screen.

**Stretch goals:** a widget showing cards due today; an App Intent "start review"; iCloud sync with CloudKit.

**What it proves to an employer:** you write correct Swift with tests and handle persistence and accessibility without being reminded.

### P2 · Weather and air-quality app with widgets (L2, ~15 hours)

**Real-world inspiration:** air quality in many Indian cities changes sharply by season, and people check it before going outside. Open-Meteo provides free weather and air-quality APIs without an API key (https://open-meteo.com).

**What to build:** current conditions and a 7-day forecast for saved cities, an air-quality card, a home-screen widget, background refresh, an App Intent ("What is the air quality in Pune?") and offline display of the last good data.

**Acceptance criteria:**
- **Honest staleness:** offline, the app and widget show cached data with an "updated N minutes ago" label; data older than 3 hours is visibly marked stale.
- **Background behaviour:** a two-day log shows when the system ran your refresh task; the app never assumes it ran on schedule.
- **Resilience:** against the course's failing mock server, no crash and no blank screen in 200 scripted requests.
- **Performance:** median launch at most 500 ms (`XCTApplicationLaunchMetric`, 10 iterations, device); no hang over 250 ms in a scripted 5-minute session (Instruments Hangs).
- **Memory:** zero leaks; peak memory reported.
- **Intents:** the App Intent works from Shortcuts and has automated tests.

**Stretch goals:** a Live Activity during a severe-weather alert; Hindi, Tamil and Bengali localisation with snapshot tests; iPad layout.

**What it proves to an employer:** you can integrate networking, background work, widgets and system intents while respecting iOS limits, and you measure rather than guess.

### P3 · Local-services booking app on TestFlight (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** home-services marketplaces such as Urban Company let customers book a professional for a time slot. Your app and its mock backend are an illustrative scenario, not any company's design.

**What to build:**
- **Booking:** browse services, pick a slot, book with optimistic UI and server confirmation, reschedule and cancel; booking history stored with SwiftData.
- **Accounts:** Sign in with Apple plus an email one-time-code flow against a mock server; tokens in the Keychain; in-app account deletion.
- **Reminders:** local notifications before a booking (remote push comes in MOB305); a widget for the next booking.
- **Layouts:** iPhone, iPad and iPhone Duo postures tested in Device Hub.
- **Quality:** Swift Testing, XCUITest for the booking flow, snapshot tests, CI.

**Acceptance criteria:**
- **Real users:** a TestFlight build with at least 10 external testers for 14 days.
- **Stability:** crash-free sessions at least 99.5% over the test (Xcode Organizer, TestFlight or Crashlytics evidence).
- **Performance:** median launch at most 500 ms on a device from the last three years; no hang over 500 ms in a scripted 10-minute session; zero leaks after the full booking flow is repeated ten times.
- **Correctness:** a double-tap on "Book" never creates two bookings (idempotency key, tested); a booking made while offline is either sent once or clearly marked as not sent.
- **Review readiness:** a written pre-review against guidelines 4.8, 5.1.1(v), 3.1.1/3.1.3(e) and 5.1.2 with evidence; a privacy manifest and nutrition label that match the SDKs used.
- **Accessibility:** Accessibility Inspector audit with no errors; recorded VoiceOver walkthrough of booking.
- **Write-up:** README with architecture, measurements table, and a list of AI-generated parts and how each was verified.

**Stretch goals:** App Intents so Siri can show the next booking; Apple Pay in sandbox for a deposit; a watchOS complication.

**What it proves to an employer:** you have taken an iOS app through real testers and review-readiness with numbers for stability, launch and memory, which is what iOS hiring loops probe.

## Feeds into

- [MOB402 On-Device AI for Mobile](../../year_4/MOB402_on_device_ai_for_mobile/README.md): P2 or P3 gains a Foundation Models feature.
- [MOB305 Mobile Integrations](../MOB305_mobile_integrations_payments_maps_notifications/README.md): APNs, payments and passkeys added to P3.
- [MOB401 Mobile Performance, Security and Release Engineering](../../year_4/MOB401_mobile_performance_security_and_release/README.md): P3 goes behind a release pipeline with launch and size gates.
- The [Mobile Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md).
