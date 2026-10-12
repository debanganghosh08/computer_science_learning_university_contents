# MOB401 · Mobile Performance, Security and Release Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [MOB301](../../year_3/MOB301_android_with_kotlin_and_jetpack_compose/README.md) | [MOB501](../../year_5/MOB501_frontier_seminar_wearables_ar_and_ambient/README.md) |

Part of the [Mobile Engineering major](../../README.md). The catalog lists MOB301; the course teaches Android and iOS side by side, so students who took [MOB302](../../year_3/MOB302_ios_with_swift_and_swiftui/README.md) will use it too. Bring your best app from Year 3: it is the patient for every lab. Security content is defensive and uses only your own apps and the OWASP MASTG reference apps.

## Why this course matters now

App stores now act on performance and stability. Google Play may reduce the visibility of apps whose user-perceived crash rate exceeds 1.09% or ANR rate exceeds 0.47%, and treats cold starts of 5 seconds or more as excessive. Memory and code-optimisation thresholds may affect store visibility from February 2027. Zomato reported cold-start improvements of up to 30% on low- and mid-end devices, 60% fewer out-of-memory issues and more completed orders after a startup project. Releases are harder to undo than on the web: users must update, so a bad build lives on phones for months. Policy deadlines arrive every year: target API 36 on Play from 31 August 2026, 16 KB memory-page support for updates from 1 February 2027, and the iOS 27 SDK from April 2027. AI tools now read crash reports and suggest fixes (App Quality Insights in Android Studio, Xcode 27's coding agents). They cannot tell you which of 40 startup tasks matters on a 3 GB phone, whether pinning a certificate will lock users out next year, or when to halt a rollout. This course teaches measurement, defensive security against OWASP MASVS, and release engineering as one discipline.

## Learning outcomes

By the end you can:

1. **Measure** startup, frame time, hangs, ANRs, memory, battery and size in the lab and in the field, by device tier and percentile.
2. **Diagnose** regressions from Perfetto, Android Studio profiler and Instruments traces, and **fix** them with evidence.
3. **Reduce** app size with R8, resource shrinking, feature modules and asset delivery, and **enforce** a size budget in CI.
4. **Threat-model** a mobile app and **assess** it against the eight OWASP MASVS control groups using MASTG tests.
5. **Implement** secure storage, hardware-backed keys, biometric binding, app integrity checks and network security, and **decide** on certificate pinning with stated trade-offs.
6. **Build** CI/CD pipelines with Fastlane, Gradle and Xcode tooling, including signing, tests, benchmarks and store uploads.
7. **Run** staged rollouts and phased releases with crash and ANR gates, symbolication and halting rules.
8. **Plan** for store policy and platform deadlines as engineering work.

## Chapters and lessons

### Chapter 1 · Performance thinking (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 User-centred metrics | Startup (TTID, TTFD), frame time, hangs, ANRs, memory, battery, network bytes, size | Define a performance budget for your app |
| 1.2 Percentiles and device tiers | p50 vs p90 vs p99; why averages hide low-end users | Segment a provided dataset by RAM tier |
| 1.3 Lab vs field | Macrobenchmark and XCTest metrics vs Android vitals, Xcode Organizer and MetricKit | Compare a lab number and a field number for the same metric |
| 1.4 Noise and rigour | Warm-up, thermal state, iterations, confidence intervals | Show two "regressions" that are only noise |

**Check your understanding:** Why can a p50 improvement hide a p99 regression? What does field data catch that lab data cannot? How many iterations do you need before trusting a 5% change?

### Chapter 2 · Startup (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Android startup anatomy | Process creation, `Application.onCreate`, content providers, first frame; cold, warm and hot starts | Trace a cold start in Perfetto and label every phase |
| 2.2 Fixing Android startup | App Startup library, lazy SDK initialisation, removing unused SDKs, `reportFullyDrawn` | Remove or defer three SDK inits; measure each change |
| 2.3 Baseline and startup profiles | Ahead-of-time compilation of hot paths, DEX layout | Generate a Baseline Profile; report the gain over 10 runs |
| 2.4 iOS launch | Pre-main (dyld, dynamic vs static frameworks), `init` work, first frame; `XCTApplicationLaunchMetric` | Merge dynamic frameworks; measure launch on a device |
| 2.5 Case study | Zomato's startup project: Perfetto per-SDK tracing, lazy Facebook SDK, ViewStubs | Reproduce the method on your own app |

**Check your understanding:** Why does an SDK initialised in a `ContentProvider` slow startup even if you never call it? What does a Baseline Profile change on the device? Why do dynamic frameworks cost launch time on iOS?

### Chapter 3 · Rendering and jank (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Frame deadlines | 16.7 ms at 60 Hz, 8.3 ms at 120 Hz; Choreographer and RenderThread; Core Animation commits | Find the slowest frame in a scroll trace |
| 3.2 Compose and SwiftUI costs | Recomposition and view updates, layout passes, image decoding on the main thread | Cut janky frames in a feed by half |
| 3.3 Measurement | Macrobenchmark `FrameTimingMetric`, JankStats, Instruments Animation Hitches | Add a frame-timing benchmark to CI |
| 3.4 Hangs | iOS hangs (main thread blocked for 250 ms or more), Android main-thread blocking | Find and remove a hang with Time Profiler |

**Check your understanding:** Why does a 120 Hz screen make jank more likely? What is the difference between a hitch and a hang? Why can image decoding cause jank even when it is "async"?

### Chapter 4 · Memory and ANRs (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Memory models | Java/Kotlin heap vs native memory; bitmaps; iOS dirty memory and jetsam limits | Profile peak memory on a 2–3 GB device |
| 4.2 Leaks | LeakCanary, heap dumps, Memory Graph debugger | Fix two leaks; show the retained-size drop |
| 4.3 ANR causes | Main-thread I/O, lock contention, slow broadcast receivers, binder calls | Reproduce and fix three ANR types |
| 4.4 Tools | StrictMode, ANR traces, Play's ANR clusters, Xcode Organizer hang reports | Triage a provided set of 20 ANR reports |

**Check your understanding:** Why do bitmaps cause out-of-memory crashes more than other objects? What makes an ANR happen only on some devices? How do you tell lock contention from slow I/O in a trace?

### Chapter 5 · Battery and network (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Energy basics | Radio states and tail energy, wake locks, GPS cost, CPU frequency and thermal throttling | Estimate the energy cost of polling every 30 s vs batching |
| 5.2 Android rules | Excessive partial wake locks (5% threshold), Doze, background location | Remove a wake lock without breaking a feature |
| 5.3 Measuring | Battery Historian, Android Studio Power Profiler, Xcode energy reports | A 60-minute energy report for one feature |
| 5.4 Network efficiency | Compression, HTTP/2 and HTTP/3, image formats, bytes per session | Cut bytes per session by 30% |

**Check your understanding:** Why can three small requests cost more battery than one large one? What does Doze do to network access? Why should energy tests run for an hour, not a minute?

### Chapter 6 · App size (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Anatomy | AAB/APK and IPA contents; download vs install size; Play's 200 MB compressed limit for bundles | Break your app's size into code, resources, native libraries and assets |
| 6.2 Shrinking | R8 full mode, resource shrinking, removing unused locales and densities, vector assets | Cut download size by 20% |
| 6.3 Delivery | Play Feature Delivery and Asset Delivery; iOS App Thinning and on-demand resources | Move a rarely used feature to an on-demand module |
| 6.4 Native code | 16 KB page alignment (required for updates from 1 Feb 2027), stripping symbols | Verify 16 KB alignment of every `.so` in your bundle |
| 6.5 Size budgets | Per-module budgets, CI checks, the India data-cost context | Fail a CI build on a 2% size increase |

**Check your understanding:** Why is download size, not APK size, what users pay for? What can R8 break, and how do keep rules fix it? Why did Google make 16 KB page support mandatory?

### Chapter 7 · Mobile threat modelling and OWASP MASVS (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Threats | Lost or stolen device, malicious co-installed app, hostile network, reverse engineering, compromised SDK | Threat-model your app with STRIDE |
| 7.2 MASVS | v2.1.0 control groups: STORAGE, CRYPTO, AUTH, NETWORK, PLATFORM, CODE, RESILIENCE, PRIVACY | Map each group to parts of your app |
| 7.3 MASTG and MASWE | Using MASTG tests and MASWE weakness entries as a defensive checklist | Run five MASTG storage and network tests on your own app |
| 7.4 Privacy controls | MASVS-PRIVACY: data minimisation, identifiers, transparency, user control | Remove one identifier and one permission |

**Check your understanding:** Which MASVS groups apply to every app, and which only to high-risk apps? What is the difference between a weakness (MASWE) and a test (MASTG)? Why is "the attacker has the APK" the default assumption?

### Chapter 8 · Secure implementation (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Secrets and storage | Android Keystore and iOS Keychain, hardware-backed and StrongBox/Secure Enclave keys, file protection, wiping on logout | Encrypt tokens with a non-exportable key |
| 8.2 Biometrics | `BiometricPrompt` with a `CryptoObject`; LocalAuthentication with Keychain access control | Bind a payment confirmation to a biometric-gated key |
| 8.3 Platform interaction | Exported components, intent and deep-link validation, WebView hardening, pasteboard and screenshots of sensitive screens | Fix five platform-interaction findings in a sample |
| 8.4 Network security | TLS only, Network Security Config, App Transport Security; certificate pinning: Android's documentation recommends against it unless you use backup pins and short expiry | Write a pinning decision record for a payments app |
| 8.5 App integrity | Play Integrity API and App Attest, verified on the server; obfuscation and its limits | Gate a sensitive API on a server-verified integrity verdict |

**Check your understanding:** Why does a key that can be exported defeat the Keystore? What outage can pinning cause, and how do backup pins and expiry reduce it? Why must integrity verdicts be checked on the server?

### Chapter 9 · CI/CD for mobile (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Builds | Variants and flavours, reproducible builds, build caching | Make two clean builds byte-comparable where possible |
| 9.2 Signing | Play App Signing and upload keys; Apple certificates and profiles; secrets in CI | Sign in CI with no secrets in the repository |
| 9.3 Pipelines | GitHub Actions or similar; Fastlane lanes; Gradle Play Publisher; Xcode Cloud or `xcodebuild` | One pipeline from commit to internal track and TestFlight |
| 9.4 Test strategy | Unit, screenshot and instrumented tests; device farms such as Firebase Test Lab; flaky-test quarantine | Cut pipeline time while keeping coverage |
| 9.5 Performance gates | Macrobenchmark and launch metrics in CI with statistical thresholds | Block a planted 5% startup regression |

**Check your understanding:** What happens if you lose an upload key, and what if you lose the app signing key? Why do performance gates need statistics? Which tests belong on every commit and which nightly?

### Chapter 10 · Rollouts and production (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Staged rollouts | Play percentage rollouts and halting; Apple's 7-day phased release; release trains | Write rollout gates: crash-free, ANR and key-flow thresholds |
| 10.2 Crash reporting | Crashlytics, Sentry, MetricKit; symbolication with R8 mappings and dSYMs; crash-free users vs sessions | Symbolicate an obfuscated crash end to end |
| 10.3 Flags and forced updates | Kill switches, remote config, Play in-app updates, minimum-version gates | Disable a broken feature without a release |
| 10.4 Incidents | Hotfix process, communication, post-mortems | Run a simulated bad-release incident |

**Check your understanding:** Why halt rather than roll back a mobile release? When are crash-free sessions misleading? What can a kill switch not fix?

### Chapter 11 · Policy and platform deadlines as engineering (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 The calendar | Play target API 36 (31 Aug 2026, extension to 1 Nov 2026); 16 KB pages (1 Feb 2027); Xcode 26 SDK minimum and iOS 27 SDK from April 2027; Android developer verification (global in 2027) | Build a 12-month compliance calendar |
| 11.2 Store-visible quality | Android vitals thresholds, store warnings, memory thresholds from Feb 2027 | Write alert rules tied to the thresholds |
| 11.3 Release readiness review | A checklist joining performance, security, policy and rollback | Run the review on a classmate's app |

**Check your understanding:** What happens to an existing app that does not raise its target API? Why plan platform migrations a year ahead? Who in a company should own the compliance calendar?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Budgets and baselines | Performance budget |
| 2 | 2 | Lab 2 · Startup tracing | — |
| 3 | 2 | Lab 2 (cont.) · Baseline Profiles and iOS launch | **P1 due** |
| 4 | 3 | Lab 3 · Jank and hangs | — |
| 5 | 4 | Lab 4 · Memory and ANR triage | — |
| 6 | 5 | Lab 5 · Energy | Energy report |
| 7 | 6 | Lab 6 · Size budget | Mid-term (AI off) |
| 8 | 7 | Lab 7 · Threat model and MASTG tests | — |
| 9 | 8 | Lab 8 · Secure storage and biometrics | — |
| 10 | 8 | Lab 8 (cont.) · Integrity and pinning decision | **P2 due** |
| 11 | 9 | Lab 9 · Pipeline | — |
| 12 | 9 | Lab 9 (cont.) · Performance gates | — |
| 13 | 10 | Lab 10 · Rollout and incident | — |
| 14 | 11 | Release readiness reviews | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** grouping and explaining crash clusters (App Quality Insights, Crashlytics AI features, or pasting symbolicated traces into Claude or ChatGPT); drafting Fastlane lanes and CI YAML; explaining trace sections; drafting threat-model tables and MASVS checklists; writing release notes.
- **Do without AI (drills):** reading a Perfetto startup trace and an Instruments time profile; triaging ANR reports; the threat model; the pinning decision; the mid-term and final.
- **Verify AI output by:** (1) never accepting a performance fix without before/after numbers from at least 10 runs on a low-end device; (2) checking security advice against MASVS/MASTG and the platform's own security pages; (3) dry-running CI changes on a branch with a planted regression; (4) confirming policy dates on the official requirement pages.
- **Where AI still fails here (collect your own evidence):** log suggestions that optimised code not on the critical path, "fixed" an ANR by moving work to a thread that still blocked on a lock, recommended hard-coded certificate pins without backups or expiry, or recommended client-side-only integrity checks. Each entry needs the measurement or test that exposed it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 25% |
| Release readiness review of a peer's app | 5% |

**Mastery gate.** You pass when you can, with AI tools off: (1) from a provided Perfetto or Instruments trace, name the cause of a startup or jank regression within 30 minutes and propose a fix; (2) threat-model a provided app and list its top five MASVS findings with fixes; (3) show your pipeline blocking a planted 5% startup regression and a 2% size regression, and halting a staged rollout when a crash threshold is crossed.

## Industry reality

Android vitals thresholds (1.09% crash rate, 0.47% ANR rate, 8% for any single phone model) are public, and Play may warn users on the store listing of apps that exceed them. Zomato's published startup work used Perfetto to trace every SDK initialised at startup, then removed or lazy-loaded them. A Google Play analysis found each 6 MB of APK size associated with about a 1% lower install conversion. OWASP's MASVS v2.1.0 (January 2024) added the PRIVACY group and is the common reference for mobile security reviews. Android's documentation cautions against certificate pinning because a server certificate change can lock users out until they update.

**Interview questions from this course**

1. *Cold start regressed by 300 ms in the last release. How do you find the cause?* Strong answer: confirms with field data by device tier; reproduces with Macrobenchmark; compares Perfetto traces between releases; checks new SDK inits, content providers, missing Baseline Profile and main-thread I/O; fixes and adds a CI gate.
2. *ANR rate is 0.6% overall and much higher on a few low-RAM models. Triage it.* Strong answer: reads ANR clusters and traces; separates main-thread I/O, lock contention and binder calls; tests on those devices; ships fixes behind staged rollout; watches the per-device 8% threshold.
3. *Should our payments app pin certificates?* Strong answer: explains the attack pinning stops and the outage it can cause; follows platform guidance on backup pins and expiry or prefers Certificate Transparency and integrity checks; has a remote kill switch plan.
4. *Design the release process for a 50-engineer mobile team.* Strong answer: release trains and branch cuts; automated gates (tests, size, startup); staged rollout with crash-free and ANR thresholds; halting rules; hotfix path; owners and on-call; symbol uploads.
5. *How do you store an auth token securely on both platforms?* Strong answer: Keystore/Keychain-backed encryption with non-exportable keys; appropriate accessibility class; biometric binding where needed; wipe on logout; MASVS-STORAGE and MASVS-AUTH references; no tokens in logs or backups.

## Resources (free first)

- **Performance:** Android performance docs and Macrobenchmark — https://developer.android.com/topic/performance ; Baseline Profiles — https://developer.android.com/topic/performance/baselineprofiles/overview ; Perfetto — https://perfetto.dev/ ; Apple, Improving your app's performance — https://developer.apple.com/documentation/xcode/improving-your-app-s-performance ; MetricKit — https://developer.apple.com/documentation/metrickit
- **Size:** Reduce your app size — https://developer.android.com/topic/performance/reduce-apk-size ; 16 KB page sizes — https://developer.android.com/guide/practices/page-sizes
- **Security (defensive):** OWASP MASVS — https://mas.owasp.org/MASVS/ ; MASTG — https://mas.owasp.org/MASTG/ ; MASWE — https://mas.owasp.org/MASWE/ ; Android security and SSL guidance — https://developer.android.com/privacy-and-security/security-ssl ; Play Integrity API — https://developer.android.com/google/play/integrity ; Apple App Attest — https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity
- **Release:** fastlane docs — https://docs.fastlane.tools/ ; Gradle Play Publisher — https://github.com/Triple-T/gradle-play-publisher ; Firebase Crashlytics — https://firebase.google.com/docs/crashlytics ; Firebase Test Lab — https://firebase.google.com/docs/test-lab
- **Case study:** Zomato developer story — https://developer.android.com/stories/apps/zomato

## Sources

- Android vitals thresholds and visibility — https://developer.android.com/topic/performance/vitals ; excessive startup thresholds — https://developer.android.com/google/play/vitals/launch-time (checked 2026-10)
- Target API requirements — https://developer.android.com/google/play/requirements/target-sdk ; 16 KB page sizes — https://developer.android.com/guide/practices/page-sizes ; developer verification — https://developer.android.com/developer-verification (checked 2026-10)
- Apple, Upcoming requirements; Developer News (iOS 27 SDK from April 2027) — https://developer.apple.com/news/upcoming-requirements/ ; https://developer.apple.com/news/ (checked 2026-10)
- OWASP MASVS releases (v2.1.0, 18 Jan 2024) — https://github.com/OWASP/masvs/releases (checked 2026-10)
- Android Developers, security with network protocols (pinning caution) — https://developer.android.com/privacy-and-security/security-ssl (checked 2026-10)
- Zomato developer story — https://developer.android.com/stories/apps/zomato ; Google Play, "Shrinking APKs, growing installs" (2017) — https://medium.com/googleplaydev/shrinking-apks-growing-installs-5d3fcba23ce2 (checked 2026-10)
- Gemini in Android Studio (App Quality Insights) — https://developer.android.com/studio/gemini/overview ; Xcode — https://developer.apple.com/xcode/ (checked 2026-10)

_Last reviewed: 2026-10_
