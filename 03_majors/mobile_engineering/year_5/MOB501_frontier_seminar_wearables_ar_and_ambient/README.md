# MOB501 · Frontier Seminar: Wearables, AR and Ambient Computing

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [MOB401](../../year_4/MOB401_mobile_performance_security_and_release/README.md), [MOB403](../../year_4/MOB403_mobile_system_design/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [Mobile Engineering major](../../README.md). Taken alongside [RES501 Research Methods](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md). This is a seminar: each week you read papers and platform documentation, one student presents and leads the critique, and everyone builds or measures something small. The semester ends with a reproduction or extension that could become a thesis. [MOB402 On-Device AI](../../year_4/MOB402_on_device_ai_for_mobile/README.md) is strongly recommended. Hardware (watches, a headset, glasses) is shared from a course pool; emulators cover most labs.

## Why this course matters now

The phone is becoming the hub for devices that are worn, looked through or spoken to. Android XR now spans headsets, wired XR glasses, audio glasses and display glasses; its SDK reached Developer Preview 4 in 2026, with Jetpack Compose for XR and a separate Compose Glimmer toolkit for display glasses. visionOS 27 renders Gaussian splats in RealityKit, lights real rooms with virtual light and tracks custom accessories at up to 90 Hz. Wear OS 7 recommends Compose and documents a migration from tiles to widgets. A foldable iPhone ships on 23 October 2026, and Android 17 ignores apps' orientation and resizability restrictions on large screens. Operating systems are also opening apps to assistants: iOS 27's App Intents feed the Spotlight semantic index, and Android's AppFunctions library (alpha in October 2026) lets apps expose tasks to AI assistants. Research on agents that operate phone apps, on SLAM and on neural scene representations moves fast. Much of what is announced is a demo; some of it will define the next decade of mobile work. This seminar trains you to tell which is which, with measurement and reproduction.

## Learning outcomes

By the end you can:

1. **Read** a research paper or platform announcement critically, separating measured results, demos and marketing.
2. **Build** for watch platforms (Wear OS 7, watchOS) within battery, glanceability and connectivity limits.
3. **Explain** visual-inertial odometry, SLAM, anchors and depth estimation, and **measure** tracking drift.
4. **Build** a spatial or AR experience on visionOS, Android XR or ARCore/ARKit, and **evaluate** it against comfort and performance budgets.
5. **Design** multimodal assistants for glasses and watches with explicit privacy, bystander and battery constraints.
6. **Expose** app capabilities to system assistants (App Intents, AppFunctions) safely, and **analyse** research on agents that operate apps.
7. **Adapt** apps to foldables and new form factors with measured layout and continuity behaviour.
8. **Reproduce or extend** a published result and **write** a research-grade report others can rerun.

## Chapters and lessons

### Chapter 1 · How to read the frontier (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Visions and their record | Weiser's "The Computer for the 21st Century" (1991) and "calm technology" (Weiser and Brown, 1996): what came true and what did not | Two-page critique of one prediction |
| 1.2 Reading papers | Claims, baselines, datasets, ablations, threats to validity | Annotate a SLAM paper with the RES502 template |
| 1.3 Reading announcements | Developer previews vs stable APIs; device availability; what a keynote demo proves | Classify ten 2026 announcements by maturity |
| 1.4 Reproducibility | Artifact availability, hardware dependence, reporting variance | Plan a reproduction for your final project |

**Check your understanding:** What evidence would convince you a platform feature is production-ready? Why do mobile and XR results often fail to reproduce? Which of Weiser's ideas are now constrained by battery rather than computing power?

### Chapter 2 · Wearables I: watch platforms (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Constraints | Tiny screens, glances under 5 seconds, battery measured in days, intermittent phone connection | Redesign a phone feature as a 3-second glance |
| 2.2 Wear OS 7 | Compose for Wear OS, `TransformingLazyColumn`, tiles and the move to widgets, complications, Watch Face Format | A complication and a widget for one data source |
| 2.3 watchOS | SwiftUI on watch, complications and Smart Stack widgets, background refresh budgets | The same feature on watchOS |
| 2.4 Phone–watch data | Data layer APIs, Watch Connectivity, standalone vs companion apps, sync when apart | Measure sync delay and battery cost |

**Check your understanding:** Why should a watch app defer work until charging when possible? What breaks when the phone is out of range? When is a complication better than an app?

### Chapter 3 · Wearables II: sensors, health and devices (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Health platforms | Health Connect and HealthKit: permissions, data types, provenance | Read and write step and heart-rate data with consent |
| 3.2 Sensor processing | Sampling rates, filtering, step detection, heart-rate from PPG (concepts), validation against reference devices | Build a step counter; compare with a reference |
| 3.3 Bluetooth Low Energy | GATT services, connection intervals, background scanning limits, reconnection | Talk to a BLE device or simulator |
| 3.4 Claims and regulation | Wellness vs medical claims; medical-device regulation (CDSCO in India, FDA in the US) at concept level | Rewrite three feature descriptions to avoid unsupported medical claims |

**Check your understanding:** Why can step counts differ by 20% between devices? What does BLE connection interval trade? When does a health feature become a medical device?

### Chapter 4 · AR foundations (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Tracking | Visual-inertial odometry; PTAM (Klein and Murray, 2007), MSCKF (Mourikis and Roumeliotis, 2007), ORB-SLAM (Mur-Artal et al., 2015) | Explain one paper's pipeline in a diagram |
| 4.2 Understanding the scene | Planes, depth (ARCore Depth API, LiDAR), semantic segmentation, light estimation | Place objects that respect occlusion |
| 4.3 Anchors | Local, cloud and geospatial anchors (ARCore Geospatial API), drift and relocalisation | Measure anchor drift over a 50 m walk |
| 4.4 Neural scenes | NeRF (Mildenhall et al., 2020) and 3D Gaussian Splatting (Kerbl et al., 2023); capture and rendering on device | Capture a room as splats; view on a phone or headset |

**Check your understanding:** Why do AR objects drift in featureless corridors? What does depth add beyond planes? Why did Gaussian splatting spread faster on devices than NeRF?

### Chapter 5 · Spatial computing platforms (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 visionOS 27 | Windows, volumes, immersive spaces; RealityKit lighting of physical spaces, Gaussian splats, foveated streaming, object tracking | Port a 2D app to a window; add one volume |
| 5.2 Android XR | Headsets and wired XR glasses; existing apps as 2D panels; Jetpack Compose for XR, SceneCore, ARCore for Jetpack XR | Spatialise a Compose app on the XR emulator |
| 5.3 Engines and standards | Unity, Godot, Unreal, OpenXR, WebXR; React Native on Meta Quest (2026) | Same scene in an engine and a native toolkit; compare effort |
| 5.4 Comfort and performance | Frame rates of 90 Hz and above, motion-to-photon latency, text legibility, input (gaze, hands, voice) | Measure frame time and comfort ratings with five testers |

**Check your understanding:** Why does dropping frames matter more in a headset than on a phone? When should an app stay a 2D window? What do OpenXR and WebXR buy you, and what do they cost?

### Chapter 6 · Glasses and multimodal assistants (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Glasses form factors | Audio glasses, display glasses, wired XR glasses; Compose Glimmer for display glasses | Design a two-line display experience |
| 6.2 Multimodal pipelines | Camera + microphone + on-device or cloud models; latency and battery budgets from MOB402 | Prototype "what am I looking at?" on a phone camera |
| 6.3 Bystanders | Recording indicators, consent of people nearby, data retention | Write a bystander-privacy policy for your prototype |
| 6.4 Accessibility | Assistive uses for low-vision and hard-of-hearing users | Evaluate a captioning prototype with criteria from users |

**Check your understanding:** Why is battery the main design constraint for glasses? How should a camera-based assistant treat faces of bystanders? Which uses justify always-available sensing?

### Chapter 7 · Ambient computing and agents that use apps (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Exposing app actions | iOS App Intents with entity schemas and View Annotations (iOS 27); Android AppFunctions (alpha) | Expose two actions with confirmation for side effects |
| 7.2 Agents operating phones | Android in the Wild (Rawles et al., 2023), AndroidWorld (Rawles et al., 2024), AppAgent (Zhang et al., 2023), Ferret-UI (You et al., 2024) | Reproduce a small AndroidWorld-style task evaluation |
| 7.3 Safety of delegated actions | Confirmation, scopes, undo, audit logs; prompt injection through screen content | Threat-model an agent that can send payments (design only) |
| 7.4 Surfaces beyond apps | Widgets, Live Activities and Android Live Updates, cars (Android Auto, CarPlay), smart home (Matter) | Design a feature across three surfaces |

**Check your understanding:** Which app actions should an assistant never perform without confirmation? Why do agents that read screens fail on custom UIs? What does an app lose when users reach it only through an assistant?

### Chapter 8 · New form factors (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Foldables | Postures, hinge areas, continuity across fold and unfold; iPhone Duo (Oct 2026) and Android foldables | Make a flow continuous across fold states |
| 8.2 Large screens | Android 17 ignoring orientation and resizability restrictions; window size classes; iPad multitasking | Fix an app that assumed portrait phones |
| 8.3 Desktop and connected displays | Desktop windowing, keyboard and mouse input, phone-as-computer modes | Add keyboard shortcuts and pointer support |

**Check your understanding:** What state must survive a fold? Why did Android stop honouring orientation locks on large screens? How should navigation change with a keyboard?

### Chapter 9 · Privacy, safety and society (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Always-on sensing | Data minimisation, on-device processing, retention; DPDP consent duties | Data-flow diagram for your project with retention periods |
| 9.2 Health and location data | Sensitivity, inference risks, aggregation | Show a re-identification risk in a synthetic location trace |
| 9.3 Safety and attention | Distraction in cars and while walking, notification overload, wellbeing | Define safety rules for your prototype |

**Check your understanding:** Why is on-device processing necessary but not sufficient for privacy? What can be inferred from a week of location data? Who is responsible for distraction caused by a glasses app?

### Chapter 10 · Research project (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Proposal | Question, prior work, method, expected result, threats to validity | Two-page proposal reviewed by peers |
| 10.2 Execution | Measurement harnesses, repeated trials, variance, negative results | Weekly progress note with raw data |
| 10.3 Reporting | Paper-style report, artefact packaging, rerun instructions | A classmate reruns your artefact |

**Check your understanding:** What makes a negative result worth publishing? How many trials do you need for a stable drift measurement? What must your artefact include for someone to rerun it?

## Weekly rhythm

| Week | Chapter | Seminar and lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Reading the frontier | Prediction critique |
| 2 | 2 | Watch platforms lab | — |
| 3 | 3 | Sensors and BLE lab | **P1 due** (critical review) |
| 4 | 4 | Tracking and drift lab | Drift measurements |
| 5 | 5 | visionOS and Android XR lab | — |
| 6 | 5 | Comfort and performance study | — |
| 7 | 6 | Glasses and multimodal prototype | Bystander policy |
| 8 | 7 | App Intents and AppFunctions | — |
| 9 | 7 | Agent evaluation reproduction | **P2 due** (prototype) |
| 10 | 8 | Foldables lab | — |
| 11 | 9 | Privacy and safety review | Data-flow diagram |
| 12 | 10 | Project proposals | Proposal |
| 13 | 10 | Project work | Progress note |
| 14 | 10 | Rerun session | **P3 due** |
| 15 | Review | Research talks | Oral defence |

## Working with AI in this course

- **Use AI for:** summarising papers before you read them fully (then checking the summary against the paper); generating scaffolding for XR and watch projects; translating sample code between Unity, RealityKit and Jetpack XR; drafting related-work sections that you then verify citation by citation.
- **Do without AI (drills):** every seminar critique; the drift and comfort measurement designs; the project proposal; the oral defence.
- **Verify AI output by:** (1) opening every cited paper and checking that it says what the summary claims; (2) checking API maturity (developer preview, alpha, stable) on official pages; (3) measuring on hardware, not in the simulator, before stating performance.
- **Where AI still fails here (collect your own evidence):** summaries of fast-moving platforms often mix up preview and shipped features, invent API names, or cite papers that do not exist. Keep a log of every incorrect citation or API you catch; it is part of the seminar grade.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Seminar presentations and critiques | 20% |
| Weekly labs and measurements | 20% |
| P1 critical review and P2 prototype | 20% |
| P3 research project (report, artefact, rerun) | 30% |
| Oral defence | 10% |

**Mastery gate.** You pass when (1) a classmate reruns your P3 artefact from your instructions and gets results within your reported variance; (2) you defend your method orally, including its threats to validity; (3) your critical review identifies at least one substantive limitation in a published paper or platform claim, with evidence.

## Industry reality

Platform owners are investing in new surfaces at the same time: Android XR across four device types, visionOS 27's rendering and tracking features, Wear OS 7, a foldable iPhone, and system-level assistant hooks on both platforms. Most of these surfaces still reuse phone apps (Android XR runs existing 2D apps as panels), so mobile engineers who understand performance budgets, privacy and system integration are the people who extend products onto them. Research benchmarks such as AndroidWorld measure how well AI agents operate real apps, which affects how apps should expose their actions.

**Interview questions from this course**

1. *Should our app build a visionOS or Android XR version now?* Strong answer: users and device availability; whether a 2D window suffices; cost of 3D content; performance and comfort budgets; a small experiment before a full build.
2. *Design a watch feature for a food-delivery app.* Strong answer: one glanceable state (order status), complication or widget, push-driven updates, behaviour when the phone is out of range, battery cost.
3. *How would you let a system assistant reorder a past purchase in your app?* Strong answer: expose the action via App Intents or AppFunctions; confirmation before payment; scopes and audit; idempotency; handling prompt injection and wrong-item risks.
4. *Our AR anchors drift in malls. Why, and what can we do?* Strong answer: featureless or reflective surfaces, lighting, VIO error growth; relocalisation, geospatial or cloud anchors, user re-anchoring; measuring drift.
5. *What privacy design does a camera-based glasses assistant need?* Strong answer: on-device processing by default, visible recording indicators, bystander handling, retention limits, consent and disclosures, accessibility benefits weighed against risks.

## Resources (free first)

- **Platforms:** Android XR — https://developer.android.com/develop/xr ; visionOS — https://developer.apple.com/visionos/ ; Wear OS — https://developer.android.com/training/wearables ; watchOS — https://developer.apple.com/watchos/ ; ARCore — https://developers.google.com/ar ; ARKit — https://developer.apple.com/augmented-reality/arkit/ ; OpenXR — https://www.khronos.org/openxr/ ; Health Connect — https://developer.android.com/health-and-fitness/guides/health-connect ; HealthKit — https://developer.apple.com/documentation/healthkit ; App Intents — https://developer.apple.com/documentation/appintents ; AppFunctions — https://developer.android.com/jetpack/androidx/releases/appfunctions ; Matter — https://csa-iot.org/all-solutions/matter/
- **Classic papers:** Weiser, "The Computer for the 21st Century", *Scientific American* (1991); Weiser and Brown, "The Coming Age of Calm Technology" (1996); Azuma, "A Survey of Augmented Reality", *Presence* (1997); Klein and Murray, "Parallel Tracking and Mapping for Small AR Workspaces" (ISMAR 2007); Mourikis and Roumeliotis, "A Multi-State Constraint Kalman Filter for Vision-aided Inertial Navigation" (ICRA 2007); Mur-Artal, Montiel and Tardós, "ORB-SLAM" (IEEE T-RO 2015)
- **Recent papers:** Mildenhall et al., NeRF (arXiv 2003.08934); Kerbl et al., 3D Gaussian Splatting (arXiv 2308.04079); Rawles et al., Android in the Wild (arXiv 2307.10088); Rawles et al., AndroidWorld (arXiv 2405.14573); Zhang et al., AppAgent (arXiv 2312.13771); You et al., Ferret-UI (arXiv 2404.05719)

## Sources

- Android Developers, Android XR (device types, Developer Preview 4, Jetpack XR, Compose Glimmer) — https://developer.android.com/develop/xr (checked 2026-10)
- Apple, What's new in visionOS 27 — https://developer.apple.com/visionos/whats-new/ (checked 2026-10)
- Android Developers, Wear OS (Wear OS 7, Compose for Wear OS, widgets) — https://developer.android.com/training/wearables ; Play target API for Wear OS — https://developer.android.com/google/play/requirements/target-sdk (checked 2026-10)
- Apple Developer News, iPhone Duo (5 Oct 2026) — https://developer.apple.com/news/ ; What's new in iOS 27 (App Intents) — https://developer.apple.com/ios/whats-new/ (checked 2026-10)
- Android Developers, AppFunctions release notes (1.0.0-alpha13, 7 Oct 2026) — https://developer.android.com/jetpack/androidx/releases/appfunctions (checked 2026-10)
- Android 17 behaviour changes — https://developer.android.com/about/versions/17 (checked 2026-10)
- React Native blog, "React Native Comes to Meta Quest" (Feb 2026) — https://reactnative.dev/blog (checked 2026-10)

_Last reviewed: 2026-10_
