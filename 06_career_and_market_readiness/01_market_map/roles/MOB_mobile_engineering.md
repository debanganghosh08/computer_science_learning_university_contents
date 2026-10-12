# MOB · Mobile Engineering: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Mobile Engineering major](../../../03_majors/mobile_engineering/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | Android Developer, iOS Developer, Mobile Application Developer, Flutter/React Native Developer |
| Mid | Android Engineer II, iOS Engineer II, Mobile Engineer |
| Senior | Senior Android/iOS Engineer, Mobile Tech Lead |
| Staff and above | Staff Mobile Engineer, Mobile Platform Architect |

Specialised variants: mobile platform engineer (build systems, modularisation, release tooling), mobile performance engineer, mobile SDET, on-device ML engineer (MOB402).

## What the work looks like day to day

- Build screens in Jetpack Compose (Android) or SwiftUI (iOS), or in Flutter or React Native.
- Handle offline use and sync conflicts (MOB304).
- Integrate payments, maps, push notifications and sign-in (MOB305). In India this often means UPI intents, OTP flows and DigiLocker-style identity integrations.
- Profile app start time, frame drops, memory and battery.
- Ship through app-store review, staged rollouts and feature flags; triage crash reports (MOB401).
- Run experiments and read funnel analytics (MOB404).

## Demand signals

**No strong public demand data separates mobile engineers.** Official statistics count them as software developers.

- **US projections.** Software developers +10% from 2025 to 2035 ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)).
- **Pay as a demand signal.** In Levels.fyi's India software engineering data, "Mobile Software Engineer" (median total pay ₹39.6 lakh) and "Android Engineer" (₹37.7 lakh) are among the top-paying titles, above the overall software engineer median of ₹30.6 lakh ([Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india)). This is self-reported data from mostly product companies.
- **AI exposure.** "Web & Mobile App Development" was 8% of Claude Code conversations, a sign that much routine app code is now generated ([Anthropic, Apr 2025](https://www.anthropic.com/research/impact-software-development)).

**Analysis.** Mobile hiring is concentrated in consumer product companies, fintech and commerce. Demand follows the number of companies that treat their app as the main product, not the number of apps.

## How AI is changing the role

**Automated or mostly automated.** Screen layouts from designs, list and form boilerplate, network client code from an API specification, simple unit tests, and translations between Kotlin and Swift or between UI frameworks.

**Augmented.** Crash triage (reading stack traces and grouping crashes), migrating to new platform APIs, accessibility fixes, writing UI tests.

**Growing in value.**

- Platform internals: lifecycles, background execution limits, threading models, memory.
- Performance on low-end Android devices and poor networks.
- Offline-first architecture and conflict resolution.
- Privacy and security: keychain/keystore, certificate pinning decisions, permissions, store policies.
- Release engineering: a bad mobile release cannot be rolled back instantly, because users must update.
- On-device AI: running small models with Core ML, LiteRT (formerly TensorFlow Lite) or ONNX Runtime within memory, latency and battery budgets (MOB402).

**Analysis.** Mobile has a built-in check on AI-generated code: it must run on real devices, pass store review, and survive older OS versions. Engineers who understand those constraints, and who can measure performance on real hardware, keep their value.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Software developers (includes mobile) | Median $135,980; 10th $82,460; 90th $214,670 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) |
| India | Mobile Applications Developer | Average base ₹7.0 lakh (80 profiles, Jan 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Mobile_Applications_Developer/Salary) |
| India | iOS Developer | Average base ₹7.8 lakh (129 profiles, May 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=iOS_Developer/Salary) |
| India | Mobile Software Engineer; Android Engineer (titles within software engineering) | Median total pay ₹39.6 lakh; ₹37.7 lakh (Oct 2026) | Self-reported, mostly product companies | [Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india) |

Payscale samples for mobile titles are small (under 150 profiles); treat them as rough.

## The hiring loop

Typical loop (varies by company):

1. DSA coding round (common at product companies).
2. Platform deep dive: Android activity/fragment lifecycle, coroutines and Flow; or iOS memory management (ARC), concurrency (async/await, actors), SwiftUI state.
3. Practical round or take-home: build a small app that fetches, caches and displays data, with tests.
4. Mobile system design: design an offline-first chat app, an image feed, or a payments screen. Strong answers cover caching, sync, pagination, background work, battery and failure states.
5. Behavioural: a production crash you fixed, a release you rolled back.

See [AI-driven interviews](../../04_ai_driven_interviews/) for how AI-assisted and AI-free rounds differ.

## Durable skills that make you hard to replace

- Deep knowledge of one platform plus working knowledge of the other.
- Profiling: Android Studio Profiler, Instruments, Perfetto.
- Offline sync design and local databases (Room, Core Data, SQLite).
- Secure storage, authentication flows and privacy rules.
- Release engineering and staged rollouts.
- On-device ML integration and measurement.

## Adjacent roles and transitions

- **Frontend**: shared component thinking and web technologies ([FE](FE_frontend_engineering.md)).
- **Backend**: mobile backends, sync services and push infrastructure ([BE](BE_backend_engineering.md)).
- **Embedded and wearables**: Bluetooth Low Energy, watches and devices ([EMB](EMB_embedded_systems_iot.md)); MOB501 covers wearables and AR.
- **Quality engineering**: mobile test automation ([QAE](QAE_software_quality_test_engineering.md)).
- **Growth engineering**: experiments and analytics (MOB404, [DAN](DAN_data_analysis.md)).

## Sources

All checked October 2026.

- BLS, Occupational Outlook Handbook: Software Developers (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
- Levels.fyi, Software Engineer salaries in India (self-reported; 12 Oct 2026). https://www.levels.fyi/t/software-engineer/locations/india
- Payscale India: Mobile Applications Developer; iOS Developer (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Mobile_Applications_Developer/Salary ; https://www.payscale.com/research/IN/Job=iOS_Developer/Salary
- Anthropic, AI's impact on software development (28 Apr 2025). https://www.anthropic.com/research/impact-software-development

_Last reviewed: 2026-10_
