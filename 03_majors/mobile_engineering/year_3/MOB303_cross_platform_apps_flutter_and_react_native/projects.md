# MOB303 · Labs and projects

Performance numbers in this course are only valid from release or profile builds on a physical device, and every comparison runs on the same device, OS version and network. Each lab names one low-end Android reference device (2–3 GB of RAM) and one iPhone. Labs 2 and 8 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Tap-to-pixel | Diagram the update path in Flutter, React Native (Fabric), KMP with native UI and Compose Multiplatform | Four diagrams with the threads named; case-study table | 3 h |
| 2 · Dart async and isolates (no AI) | Event-loop ordering puzzles; move a 20 MB JSON parse to an isolate | Puzzle answers; frame chart before and after | 4 h |
| 3 · Flutter layout and rendering | Fix five layout exceptions; find a raster-thread bottleneck | Fixed code; DevTools performance screenshots | 5 h |
| 4 · Flutter architecture and tests | Restructure a sample to Flutter's architecture guide; add widget and golden tests | Diff; 30 widget tests and 4 goldens passing in CI | 7 h |
| 5 · Pigeon plugin and size | A type-safe plugin in Kotlin and Swift; reduce release size | Plugin with tests on both platforms; `--analyze-size` before and after | 6 h |
| 6 · React Native with Expo | Development build, config plugin, an OTA update on a test channel and its rollback | Repository; video of update and rollback; runtime-version notes | 6 h |
| 7 · Lists, animation and end-to-end tests | FlashList with 5,000 rows; a Reanimated gesture; a Maestro flow | Frame-timing capture on the low-end device; Maestro run log | 5 h |
| 8 · Native modules both ways (no AI) | A Turbo Native Module and a Flutter plugin exposing Keystore/Keychain storage | Specs, implementations and tests on both platforms | 6 h |
| 9 · KMP shared module | Shared repository with Ktor and Room 3 or SQLDelight, used from Compose and SwiftUI | Shared tests on JVM and iOS simulator; a Flow collected from Swift without leaks | 7 h |
| 10 · Three-way benchmark | Benchmark the same feature in two frameworks plus a native baseline | Method section, raw data and charts | 5 h |

## Projects

### P1 · Street-cricket scorer in Flutter (L1, ~6 hours)

**Real-world inspiration:** local cricket matches are scored on phones in apps such as CricHeroes. Scoring has precise rules (wides, no-balls, byes, overs, innings) that make good test material.

**What to build:** a Flutter app that scores a limited-overs match ball by ball, with undo, a live scorecard, partnership and over summaries, and local storage. No network.

**Acceptance criteria:**
- **Rules:** at least 25 unit tests covering extras, free hits after no-balls, end of over, all out and a tied match; all pass.
- **UI tests:** at least 10 widget tests and 2 golden tests (light and dark).
- **Undo:** any sequence of 50 random balls followed by 50 undos returns to the initial state (property test).
- **Smoothness:** in profile mode on the low-end device, a 30-second scripted scroll of the ball-by-ball list shows no frame over 16 ms on the UI thread.
- **Size:** release APK and IPA sizes reported with `--analyze-size`.

**Stretch goals:** share the scorecard as an image; Hindi UI; a home-screen widget through a plugin.

**What it proves to an employer:** you can build and test a Flutter app with real domain rules and measure its performance correctly.

### P2 · Mandi price tracker, built twice (L2, ~15 hours)

**Real-world inspiration:** India's Open Government Data platform publishes daily wholesale commodity prices from agricultural markets ("mandis"), drawn from AGMARKNET (https://data.gov.in, free API key). Farmers and traders compare prices across nearby markets.

**What to build:** the same app in Flutter and in React Native (Expo): search a commodity, see today's prices in nearby markets, a 30-day trend chart, favourites, offline cache, English and Hindi. Each app includes one native module you write (for example, reading whether Data Saver or Low Data Mode is on, to skip chart downloads).

**Acceptance criteria:**
- **Parity:** both apps pass the same written acceptance script (20 steps), including offline and error states.
- **Measurement:** a comparison table from release builds on the same two devices: cold-start median of 10 runs, frame timing during a scripted scroll, peak memory, download size. Method written so another student can repeat it.
- **Native code:** the native module has tests on both platforms and does not block the UI or JavaScript thread (shown in a trace).
- **Data use:** a full session on mobile data stays under 1.5 MB after the first launch (proxy capture).
- **Localisation:** no truncated Hindi strings (golden or snapshot tests).

**Stretch goals:** a push alert when a price crosses a threshold; Kannada and Marathi; a KMP module shared by native versions.

**What it proves to an employer:** you can deliver in either framework, write native code when needed, and back a technology claim with a fair measurement.

### P3 · Group expense splitter with a shared Kotlin core (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** group expense apps such as Splitwise track who paid what and suggest who should pay whom. The settle-up step is a graph problem: minimise the number of transfers so that every balance reaches zero. Your system is an illustrative scenario.

**What to build:**
- **Shared core (KMP):** groups, expenses with equal, exact and percentage splits, balances, settle-up suggestions, validation, a repository with Room 3 or SQLDelight, a Ktor client and an outbox for offline edits.
- **Native UIs:** Jetpack Compose on Android and SwiftUI on iOS, with one screen in Compose Multiplatform for comparison.
- **Sync:** a small server you write (any stack) with idempotent writes.
- **Release:** an Android internal-track build and a TestFlight build.
- **Decision record:** an ADR explaining why this app uses KMP rather than Flutter or React Native, with numbers from Lab 10.

**Acceptance criteria:**
- **Sharing:** at least 70% of non-UI code lives in the shared module (line counts reported with `cloc`).
- **Correctness:** property tests over 10,000 random groups show balances always sum to zero and settle-up never needs more than n − 1 transfers for n members; rounding never loses a paisa.
- **Same tests, both platforms:** the shared test suite passes on the JVM and the iOS simulator in CI.
- **Offline:** 100 expenses created offline on two devices sync with zero duplicates.
- **Performance:** cold start on each platform within 15% of a native-only baseline app you also build; the Compose Multiplatform screen's frame timing compared with its SwiftUI twin.
- **Swift API quality:** Swift callers use `async` functions and `AsyncSequence` instead of raw callbacks (shown in code review).

**Stretch goals:** UPI intent payment for settle-up (completed properly in MOB305); receipt photo with on-device text recognition (MOB402); a web client using Kotlin/Wasm (beta).

**What it proves to an employer:** you can share real business logic across platforms without hurting either app, and you can justify the architecture with evidence. That is the judgement startups need from their first mobile hire.

## Feeds into

- [MOB403 Mobile System Design](../../year_4/MOB403_mobile_system_design/README.md): P3's shared core and sync become a design case study.
- [MOB304 Mobile Architecture, Offline-First and Sync](../MOB304_mobile_architecture_offline_first_and_sync/README.md): the outbox and sync get conflict resolution.
- [MOB305 Mobile Integrations](../MOB305_mobile_integrations_payments_maps_notifications/README.md): settle-up gains UPI payments.
- The [Mobile Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md).
