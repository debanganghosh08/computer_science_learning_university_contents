# Mobile Engineering (MOB) · Learning path

| Code | Years | Entry requirements | Market page | Interview loop |
|---|---|---|---|---|
| MOB | 3–5 (after the common Years 1–2) | [FND111](../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md), [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MOB roles and market](../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

Mobile engineers build the software people carry everywhere: the payment app at a tea stall, the ride-hailing map, the chat that must deliver on a weak 4G signal, the health app on a watch. The work is judged on hardware you do not control. A phone may have 2 GB of RAM, a nearly full disk, a battery saver that freezes your background work, and an operating system three versions old. A release cannot be rolled back instantly, because users must update. App stores review every build against policies that change every year. This major takes you from a Year 2 student who can write typed, tested code to an engineer who can ship and operate native and cross-platform apps at scale, add on-device AI within memory and battery budgets, and design mobile systems in an interview or in a company of one. It ends at the research frontier of wearables, augmented reality and ambient computing.

## 1. Who this major is for, and the roles it leads to

Choose this major if you like building things people touch, care about how software feels (fast, smooth, accessible), and enjoy constraints: memory, battery, network, store policy. It suits people who want to see their work on a stranger's phone and who are willing to measure performance on a cheap device rather than trust a fast laptop.

| Role | What people in it actually do | Where this major prepares you |
|---|---|---|
| Android Engineer (entry to senior) | Build screens in Jetpack Compose, own a feature's data layer, fix crashes and ANRs (Application Not Responding errors), ship through Play Console | MOB301, MOB304, MOB401 |
| iOS Engineer (entry to senior) | Build in SwiftUI with Swift concurrency, manage memory and app lifecycle, pass App Store review, ship through TestFlight | MOB302, MOB304, MOB401 |
| Cross-platform Engineer (Flutter, React Native, Kotlin Multiplatform) | Ship one product to both platforms, write native modules when the framework stops, decide what to share | MOB303, MOB304 |
| Mobile Platform / Infrastructure Engineer | Own build systems, modularisation, CI/CD, release trains, crash and performance dashboards for many teams | MOB304, MOB401, MOB403 |
| Mobile Security Engineer | Threat-model apps, apply OWASP MASVS, review storage, crypto, authentication and network code, run authorized assessments | MOB401, MOB305, OFF402 elective |
| On-device ML Engineer | Run quantized models with LiteRT, Core ML, Gemini Nano or Apple's Foundation Models within latency, memory and energy budgets | MOB402, OV09 |
| Growth / Experimentation Engineer (mobile) | Instrument events, run A/B tests, build feature flags and attribution within privacy rules | MOB404, OV08 |
| Senior / Staff Mobile Engineer, Mobile Architect | Design client architecture for 50+ engineers, lead incidents, set performance and release standards | MOB403, MOB501, THS501–502 |
| Founding Mobile Engineer | Choose native or cross-platform, build v1 alone, add payments, sign-in and push, and keep it alive in production | All of the above, plus LCH502 |

Titles vary: "Mobile Application Developer" at a services firm and "Android Engineer II" at a product company can be the same level. The [MOB market page](../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md) has titles, day-to-day work and pay sources. In Levels.fyi's self-reported India data, "Mobile Software Engineer" (median total pay ₹39.6 lakh) and "Android Engineer" (₹37.7 lakh) sit above the overall software engineer median (₹30.6 lakh); Payscale's whole-market average base for a Mobile Applications Developer is ₹7.0 lakh. The two sources measure different employers and different pay ([market page](../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md)).

## 2. How AI is changing mobile engineering

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation.

**AI tools are built into both platforms' IDEs.** Gemini in Android Studio offers an agent mode, crash analysis through App Quality Insights, Compose preview generation, "Journeys" UI testing and UI generation from images ([Android Developers](https://developer.android.com/studio/gemini/overview)). Xcode 27 supports "coding agents in Xcode, powered by the model of your choice", including frontier models and agents from Anthropic, Google and OpenAI, any agent that speaks the Agent Client Protocol, and tools added through the Model Context Protocol ([Apple](https://developer.apple.com/xcode/)). Flutter's documentation now has "agent-plugins" and an experimental AI evaluations page ([Flutter, Aug 2026](https://docs.flutter.dev/release/whats-new)).

**Models are now scored on real Android work.** Google's Android Bench leaderboard tests models on Android tasks such as Jetpack Compose migrations, wearable networking and platform API updates. In its July 2026 release the top score was 84.5, the next 80.2, and the best open-weight model 72.2 ([Android Developers Blog, Jul 2026](https://android-developers.googleblog.com/2026/07/android-bench-llm-measurement.html)). "Web & Mobile App Development" was 8% of Claude Code conversations in Anthropic's 2025 study ([Anthropic, Apr 2025](https://www.anthropic.com/research/impact-software-development)), and 65.9% of 2026 Stack Overflow respondents use AI coding assistants or agents at work ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data)).

**On-device AI is a platform feature, not a research demo.** Android exposes Gemini Nano through AICore and the ML Kit GenAI APIs (summarization, proofreading, rewriting, image description and a Prompt API, mostly in beta), with inference allowed only while the app is in the foreground and per-app quotas ([ML Kit GenAI](https://developers.google.com/ml-kit/genai)). Apple's Foundation Models framework gives apps a Swift API to its roughly 3-billion-parameter on-device model, compressed with 2-bit quantization-aware training ([Apple ML Research, Jul 2025](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025)). iOS 27 adds image input, a protocol that lets the same code call cloud models such as Claude and Gemini, and Core AI, a new framework for running your own models on device ([Apple, iOS 27](https://developer.apple.com/ios/whats-new/)).

| Mostly automated now | Augmented (you decide, AI helps) | Growing in value |
|---|---|---|
| Screen layouts from designs, list and form boilerplate, network clients from an API spec, simple unit tests, Kotlin↔Swift and framework-to-framework translation | Crash triage from stack traces, platform API migrations, accessibility fixes, UI tests, store-policy checklists | Lifecycles, threading and background limits; performance on low-end devices and poor networks; offline sync and conflict resolution; secure storage and privacy rules; release engineering; on-device AI within budgets |

The table follows the [MOB market page](../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md).

**Analysis.** Mobile has a built-in check on generated code: it must run on real devices, pass store review and survive old OS versions. A benchmark score of 84.5 still means roughly one task in six fails its tests, and benchmark tests do not measure jank on a ₹10,000 phone, battery drain over an hour, or an ANR that appears only under memory pressure. Every course in this major therefore has AI-off drills and verification by measurement: Macrobenchmark and Instruments traces, crash-free rates, size budgets, chaos tests for sync and payments, and evaluation sets for AI features.

## 3. India context

- **Android-first.** In September 2026, Android had 93.89% of India's mobile OS share and iOS 6.05% ([StatCounter](https://gs.statcounter.com/os-market-share/mobile/india)). Most Indian product teams build Android first and treat low-end performance as a core requirement.
- **Low-end devices are normal.** Android (Go edition) targets entry-level phones; its minimum RAM is 2 GB from Android 13 ([Android Developers](https://developer.android.com/guide/topics/androidgo)). Zomato reported cold-start improvements of about 25% on average and up to 30% on low- and mid-end devices, 60% fewer out-of-memory issues and an order-through rate up about 1.5 percentage points after startup work ([Android Developers story](https://developer.android.com/stories/apps/zomato)).
- **App size and data cost.** Google's guidance says users "often avoid downloading apps that seem too large, particularly in emerging markets where devices connect to spotty 2G and 3G networks or work on plans with data limits" ([Android Developers](https://developer.android.com/topic/performance/reduce-apk-size)). A Google Play analysis found that every 6 MB increase in APK size was associated with about a 1% drop in install conversion ([Google Play, 2017](https://medium.com/googleplaydev/shrinking-apks-growing-installs-5d3fcba23ce2)); it is a correlation, and the effect was reported as larger in emerging markets.
- **UPI is the default payment.** UPI processed 24.07 billion transactions worth ₹29.37 lakh crore in September 2026 (NPCI data, as reported by [StartupTalky, Oct 2026](https://startuptalky.com/upi-transactions-september-2026/)). Apps launch UPI apps through intent flows. NPCI ended peer-to-peer "collect requests" from 1 October 2025 to curb fraud; merchant collect continues ([Business Today, Aug 2025](https://www.businesstoday.in/personal-finance/banking/story/npci-to-tighten-upi-rules-peer-to-peer-collect-feature-to-end-in-october-489244-2025-08-13)).
- **Privacy law.** The Digital Personal Data Protection Rules, 2025 were notified in November 2025 with an 18-month phased timeline for core obligations such as notice, consent and breach reporting ([PIB, Nov 2025](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf)).
- **Distribution is changing.** Google's Android developer verification began on 30 September 2026 for installs on certified devices in Brazil, Indonesia, Singapore and Thailand, and expands globally in 2027 ([Android Developers](https://developer.android.com/developer-verification)).

## 4. The 5-year path

### Years 1–2: the common core

Every Year 1–2 course is required. These matter most for mobile engineers:

| Course | Why it matters for MOB |
|---|---|
| [FND111 Programming II (Java and TypeScript)](../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md) | Entry requirement. Java leads to Kotlin; TypeScript leads to React Native |
| [FND114 Web Foundations](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) | HTTP and JSON are how every app talks to its backend |
| [FND115 Databases I](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) | SQLite under Room, SwiftData and Core Data |
| [CS201 Algorithms and Complexity](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | DSA rounds; reasoning about cost on slow CPUs |
| [CS202 Computer Architecture and C](../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) and [CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | Memory, threads, processes and scheduling: the base for lifecycles, ANRs and memory limits |
| [CS204 Computer Networks](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) | TCP, TLS and HTTP/2–3 on lossy mobile links |
| [CS205 Software Engineering I](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | Entry requirement: design, testing, review and CI |
| [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | Every offline-first app is a distributed system with one very unreliable node |
| [CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) | Crypto, authentication and threat models for MOB305 and MOB401 |
| [CS214 Machine Learning Foundations](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) | The base for MOB402 |

### Years 3–5: the major

| Semester | Major courses | Shared courses | Other |
|---|---|---|---|
| 5 (Year 3) | [MOB301 Android with Kotlin and Jetpack Compose](year_3/MOB301_android_with_kotlin_and_jetpack_compose/README.md) · [MOB302 iOS with Swift and SwiftUI](year_3/MOB302_ios_with_swift_and_swiftui/README.md) · [MOB303 Cross-Platform Apps: Flutter and React Native](year_3/MOB303_cross_platform_apps_flutter_and_react_native/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | 1 elective (FE302 or BE301 recommended) |
| 6 (Year 3) | [MOB304 Mobile Architecture, Offline-First and Sync](year_3/MOB304_mobile_architecture_offline_first_and_sync/README.md) · [MOB305 Mobile Integrations: Payments, Maps, Notifications and Identity](year_3/MOB305_mobile_integrations_payments_maps_notifications/README.md) | [CAR301 Career Lab I: DSA Mastery, Portfolio and Open Source](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | 1–2 electives |
| 7 (Year 4) | [MOB401 Mobile Performance, Security and Release Engineering](year_4/MOB401_mobile_performance_security_and_release/README.md) · [MOB402 On-Device AI for Mobile](year_4/MOB402_on_device_ai_for_mobile/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | Overlap course A |
| 8 (Year 4) | [MOB403 Mobile System Design](year_4/MOB403_mobile_system_design/README.md) · [MOB404 Mobile Analytics, Experimentation and Growth Engineering](year_4/MOB404_mobile_analytics_experimentation_and_growth/README.md) | [CAR401 Career Lab II: Interviews, System Design and AI-Driven Assessments](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) | Overlap course B |
| 9 (Year 5) | [MOB501 Frontier Seminar: Wearables, AR and Ambient Computing](year_5/MOB501_frontier_seminar_wearables_ar_and_ambient/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reading, Reproducing and Extending Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) | — |
| 10 (Year 5) | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | Electives |

Prerequisites inside the major (from the catalog): MOB301 → MOB401; MOB302 → MOB402; MOB303 → MOB403; MOB304 → MOB404; MOB401 + MOB403 → MOB501. In practice the Year 4 courses use all five Year 3 courses: MOB401 and MOB402 teach both Android and iOS, MOB403 builds on MOB304's sync and MOB305's integrations, and MOB404 needs a shipped app from MOB301, MOB302 or MOB303. Take all five Year 3 courses before Year 4.

**How the courses connect.** MOB301, MOB302 and MOB303 teach you to build on each platform and decide what to share. MOB304 makes the app work without a network and keeps data consistent; MOB305 connects it to money, maps, push and identity. In Year 4, MOB401 makes it fast, safe and releasable; MOB402 adds AI on the device; MOB403 designs whole systems around the client; MOB404 measures whether any of it helped users. MOB501 asks what replaces the phone screen next.

## 5. Skill map by level

| Level | You can… | Mastery gate (do it, don't describe it) |
|---|---|---|
| L0 → L1 (Year 1) | Write typed, tested programs in Java and TypeScript; use Git; explain an HTTP request and a SQL join | A CLI and a tiny HTTP API with tests and passing CI |
| L2 (end of Year 2) | Explain processes, threads, memory, TCP/TLS and retries with idempotency; design and test small programs | CS203's and CS212's gates; a code review that finds a race condition |
| L3 (end of Year 3) | Ship a native app on each platform and one cross-platform app; make it offline-first with tested conflict resolution; add UPI and card payments, push, deep links and passkey or OTP sign-in | An app in a Play closed test or TestFlight with ≥ 12 testers, ≥ 99% crash-free users, a sync suite showing zero lost or duplicated writes across 1,000 random offline/online cycles, and payments that never double-fulfil in 50 interrupted-payment tests |
| L4 (end of Year 4) | Find and fix startup, jank, memory and ANR problems from traces; harden an app against MASVS; run a release pipeline with staged rollouts; ship an on-device AI feature with an evaluation set; design chat, feed and ride-hailing clients; run a valid A/B test | Pass a 60-minute mobile system design round; show a CI pipeline that blocks a 5% startup regression and a 2% size regression; defend an on-device AI feature with latency, memory, energy and quality numbers |
| L5 (Year 5) | Read, reproduce and extend research on wearables, AR, spatial computing and ambient AI | Submit a reproduction or extension (MOB501 P3) that another student reruns within your reported variance, and defend it orally |

## 6. Recommended overlaps and electives

**Overlaps** (Year 4; course A in semester 7, course B in semester 8):

| Overlap | The real job it maps to | Composed of | Notes for MOB students |
|---|---|---|---|
| [OV08 Full-Stack AI Product Engineering](../../04_overlaps/OV08_full_stack_ai_product_engineering/README.md) | Product or founding engineer who ships AI features end to end, including the app | FE403, BE403, AIE404 | OV08A lists FE302, BE301 and AIE302 as prerequisites: take two as Year 3 electives. OV08B (product analytics for AI apps) pairs with MOB404 |
| [OV09 Edge AI and Secure IoT](../../04_overlaps/OV09_edge_ai_secure_iot/README.md) | On-device ML engineer for phones, wearables and connected devices | EMB401, EMB402, MLE404 | OV09A lists EMB301 and MLE305; take them as electives. Runs alongside MOB402 in semester 7 |
| [OV10 FinTech Systems Engineering](../../04_overlaps/OV10_fintech_systems_engineering/README.md) | Payments and lending apps at fintechs and banks | BE401, SEC305, DEN303 | For students whose MOB305 project went deep on UPI; check its prerequisites early |
| [OV07 Privacy Engineering](../../04_overlaps/OV07_privacy_engineering/README.md) | Privacy engineer for consumer apps (consent, tracking, DPDP) | DEN404, SEC305, PRO301 | A natural partner for MOB404 |

**Electives** (pick 3–5):

- [FE302 React and Component Architecture](../frontend_engineering/year_3/FE302_react_and_component_architecture/README.md): React Native is React; also an OV08A prerequisite.
- [BE301 API Design](../backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md) and [BE305 Authentication and Authorization](../backend_engineering/year_3/BE305_authentication_authorization_and_backend/README.md): you will design and consume mobile APIs in MOB403.
- [QAE305 Mobile and Cross-Browser Testing](../software_quality_test_engineering/year_3/QAE305_mobile_and_cross_browser_testing/README.md): device farms and UI automation at scale.
- [SWE305 Concurrency and Performance Engineering](../software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md): depth for MOB401.
- [SAR302 Threat Modeling](../security_architecture/year_3/SAR302_threat_modeling/README.md) and [OFF402 Mobile and API Security Testing](../ethical_hacking_offensive_security/year_4/OFF402_mobile_and_api_security_testing/README.md): for mobile security roles (authorized testing only).
- [DAN302 Business Statistics and Experimentation](../data_analysis/year_3/DAN302_business_statistics_and_experimentation/README.md): before MOB404.
- [MLE404 Efficient Inference](../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md): quantization depth for MOB402.
- [EMB304 IoT Protocols and Cloud Connectivity](../embedded_systems_iot/year_3/EMB304_iot_protocols_and_cloud_connectivity/README.md): Bluetooth Low Energy and devices for MOB501.
- [FE402 Advanced UI: Animation, Graphics, WebGL and WebGPU](../frontend_engineering/year_4/FE402_advanced_ui_animation_graphics_webgl_and_webgpu/README.md): graphics for AR and custom rendering.
- [SWE304 AI-Assisted Software Engineering](../software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md): agent workflows with review gates.

## 7. Flagship industry project

The MOB flagship is described in [`05_industry_projects/MOB_mobile_engineering.md`](../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md). It is one production-style app, on both platforms, that you design, ship to real testers, measure and break on purpose. Its parts come from the course projects:

- MOB301 P3 or MOB302 P3 (a store-ready native app) or MOB303 P3 (a shared-core app);
- MOB304 P3 (offline-first sync with convergence tests);
- MOB305 P3 (payments, live location, push and passkey sign-in);
- MOB401 P3 (release pipeline with performance and size gates);
- MOB402 P3 (an evaluated on-device AI feature);
- MOB403 P3 (a written system design with a working client);
- MOB404 P3 (an experiment with valid analysis).

Build it across Year 4 and present it in CAR401 and LCH502. It is the evidence that you can do more than lay out screens.

## 8. Certifications (optional, never required)

| Certification | Honest value for mobile engineers |
|---|---|
| Google Associate Android Developer | Retired: Google no longer accepts registrations; existing holders keep it until it expires ([Google Developers](https://developers.google.com/training/certification/associate-android-developer)). |
| Meta Android Developer / iOS Developer Professional Certificates (Coursera) | Structured beginner material. Low hiring signal at product companies; a shipped app says more. |
| Apple App Development with Swift Certified User (Certiport) | Entry-level; useful in schools and some services firms. Low signal for product roles. |
| GIAC Mobile Device Security Analyst (GMOB) | Relevant for mobile security roles; expensive. MOB401 P2 plus authorized practice (OWASP MASTG) shows similar skills. |
| Flutter, React Native or Kotlin Multiplatform | No vendor-run certification from Google, Meta or JetBrains was found (unconfirmed). Open-source contributions carry more weight. |

**Analysis.** Mobile hiring rarely turns on certificates. A public app with real users, a crash-free rate, a startup trace, and a merged pull request to an open-source mobile library do.

## 9. The interview loop for this role

A typical loop (it varies by company; see the [market page](../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md)):

| Round | What is tested | Prepared by |
|---|---|---|
| Online assessment and DSA coding | Arrays, hashing, graphs, often with a mobile twist (LRU image cache, rate-limited polling) | CS201, CAR301 |
| Platform fundamentals | Android: lifecycle and process death, coroutines and Flow, Compose recomposition. iOS: ARC and retain cycles, async/await and actors, SwiftUI state | MOB301, MOB302 |
| Machine coding (60–120 min, or take-home) | Build a small app that fetches, caches, paginates and displays data, with tests, error states and clean architecture | MOB301–MOB304 |
| Mobile system design | Offline-first chat, image feed, ride-hailing, payments screen: API contract, caching, sync, pagination, background work, battery, failure states | MOB403, MOB304, MOB305 |
| Debugging or performance scenario | A janky list, a startup regression or an ANR from a trace | MOB401 |
| AI-assisted coding (growing) | Using AI tools on a realistic task and catching their mistakes. Canva expects backend, ML and frontend candidates to use AI in interviews ([Canva, Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)) | Every MOB course's "Working with AI" section |
| Behavioural | A production crash you fixed, a release you halted, a trade-off you got wrong | IND401, MOB401 |

Some employers forbid AI in live rounds ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)), so prepare both ways. Every MOB course lists five interview questions with what a strong answer covers. Simulations and question banks are in [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/).

## 10. Fast track for working professionals (from web or frontend)

For web or frontend developers with 1–5 years of experience, for example React and TypeScript at a product or services company, who want mobile roles. Budget 12–15 hours a week for about 12 months.

1. **Placement (week 1).** Attempt the mastery gates of [CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) and [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md). If you cannot explain a main-thread deadlock or an idempotent retry, start there. Web developers usually know HTTP well and threads, memory and process lifecycles poorly.
2. **Months 1–2: use what you know.** MOB303's React Native chapters (New Architecture, Expo, native modules). Ship one app to a Play internal test. Learn what the browser was hiding: app lifecycle, permissions, store review.
3. **Months 3–5: go native on one platform.** MOB301 (Android, larger market in India) or MOB302 (iOS). Do its P3 to store quality. Hiring managers test platform depth, and cross-platform engineers still debug native code.
4. **Months 6–7: offline and integrations.** MOB304 and MOB305. These are where web habits (always online, server holds state) fail most.
5. **Months 8–9: performance and release.** MOB401. Profile on a low-end Android device; build a CI pipeline with size and startup gates.
6. **Months 10–11: pick a specialisation.** MOB402 for on-device AI, MOB404 for growth, or the second native platform.
7. **Month 12: interview readiness.** MOB403 case studies, two mock system design rounds, one machine-coding round a week, and CAR401 practice using your shipped app as the anchor story.

## Sources

All checked October 2026.

- StatCounter, Mobile Operating System Market Share India (Sep 2026) — https://gs.statcounter.com/os-market-share/mobile/india
- Android Developers: Gemini in Android Studio — https://developer.android.com/studio/gemini/overview ; Android (Go edition) — https://developer.android.com/guide/topics/androidgo ; Reduce your app size — https://developer.android.com/topic/performance/reduce-apk-size ; Zomato developer story (updated Jan 2022) — https://developer.android.com/stories/apps/zomato ; Android developer verification — https://developer.android.com/developer-verification
- Android Developers Blog, "Evolving how LLMs are measured for Android: the next era of Android Bench" (8 Jul 2026) — https://android-developers.googleblog.com/2026/07/android-bench-llm-measurement.html
- Google, ML Kit GenAI APIs — https://developers.google.com/ml-kit/genai
- Apple: Xcode — https://developer.apple.com/xcode/ ; What's new in iOS 27 — https://developer.apple.com/ios/whats-new/ ; Apple Intelligence Foundation Language Models Tech Report 2025 (Jul 2025) — https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025
- Flutter, What's new (3.47, 12 Aug 2026) — https://docs.flutter.dev/release/whats-new
- Anthropic, *The impact of AI on software development* (28 Apr 2025) — https://www.anthropic.com/research/impact-software-development
- Stack Overflow Developer Survey 2026, AI — https://survey.stackoverflow.co/2026/ai/data
- Google Play Apps & Games, "Shrinking APKs, growing installs" (2017) — https://medium.com/googleplaydev/shrinking-apks-growing-installs-5d3fcba23ce2
- StartupTalky, UPI transactions in September 2026 (NPCI data, Oct 2026) — https://startuptalky.com/upi-transactions-september-2026/
- Business Today, "NPCI to tighten UPI rules: Peer-to-peer collect feature to end in October" (13 Aug 2025) — https://www.businesstoday.in/personal-finance/banking/story/npci-to-tighten-upi-rules-peer-to-peer-collect-feature-to-end-in-october-489244-2025-08-13
- Press Information Bureau, Digital Personal Data Protection Rules, 2025 (Nov 2025) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf
- Google Developers, Associate Android Developer (retired) — https://developers.google.com/training/certification/associate-android-developer
- Canva Engineering, *Yes, you can use AI in our interviews* (11 Jun 2025) — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; Anthropic, candidate AI guidance — https://www.anthropic.com/candidate-ai-guidance
- MOB market page (Levels.fyi and Payscale figures, BLS, hiring loop) — [roles/MOB_mobile_engineering.md](../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md)

_Last reviewed: 2026-10_
