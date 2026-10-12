# MOB404 · Mobile Analytics, Experimentation and Growth Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [MOB304](../../year_3/MOB304_mobile_architecture_offline_first_and_sync/README.md) | [OV08](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/README.md), [OV07](../../../../04_overlaps/OV07_privacy_engineering/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [Mobile Engineering major](../../README.md). You need a shipped app from Year 3 (MOB301, MOB302 or MOB303 P3) to instrument. Statistics come from [FND116 Probability and Statistics I](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md); [DAN302 Business Statistics and Experimentation](../../../data_analysis/year_3/DAN302_business_statistics_and_experimentation/README.md) is a recommended elective beforehand.

## Why this course matters now

Mobile teams are judged on what users do, and the evidence comes from events, funnels and controlled experiments. Small engineering changes move business numbers: Zomato reported about 1.5 percentage points more completed orders after a startup-speed project, and a Google Play analysis associated every 6 MB of APK size with about 1% fewer installs. Measurement rules tightened at the same time. Apple's guideline 5.1.2 requires explicit permission through App Tracking Transparency (ATT) to track users, and from iOS 27.2 the EU gets an alternative ATT prompt. Google retired most Privacy Sandbox technologies in October 2025, including Topics and Attribution Reporting on Android. Firebase Dynamic Links shut down in August 2025. India's DPDP Rules phase in notice and consent duties by 2027, and India's consumer regulator notified guidelines against dark patterns in 2023. AI tools now write SQL for funnels, summarise dashboards and propose experiments. They do not catch a sample-ratio mismatch, a metric that double-counts offline events or an experiment that ships code only some users have installed. This course teaches growth engineering that is statistically valid, privacy-respecting and honest.

## Learning outcomes

By the end you can:

1. **Define** product metrics (north star, funnels, retention cohorts, guardrails) as precise, versioned code.
2. **Instrument** apps with a tracking plan, schemas, identity handling and an offline-safe event pipeline that loses and duplicates almost nothing.
3. **Build** feature flags and remote config that work offline and at cold start without slowing it.
4. **Design** A/B tests with correct randomisation units, power analysis and stopping rules, and **analyse** them, including variance reduction.
5. **Detect** invalid experiments: sample-ratio mismatch, exposure bugs, novelty effects, version-adoption lag and interference.
6. **Implement** attribution and deep-link measurement within ATT, AdAttributionKit, Play Install Referrer and post-Privacy-Sandbox realities.
7. **Engineer** growth levers (onboarding, notifications, referrals, ratings, store listing tests, app size and speed) and **measure** their trade-offs.
8. **Apply** consent, store disclosure and anti-dark-pattern rules to every growth feature.

## Chapters and lessons

### Chapter 1 · Metrics that matter (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 North star and inputs | One outcome metric and the input metrics that drive it | Write a metric tree for a food-delivery app (illustrative) |
| 1.2 Funnels | Steps, conversion, time-to-convert, where mobile funnels leak (permissions, OTP, payment app switches) | Build a checkout funnel in SQL from sample events |
| 1.3 Retention | D1/D7/D30 cohorts, rolling vs bounded retention, resurrection | Cohort table from 1 million synthetic events |
| 1.4 Guardrails | Crash-free rate, ANR rate, startup time, latency, uninstalls, unsubscribes | Choose guardrails for three experiments |
| 1.5 Metrics as code | Definitions in version control, tests, owners | Write and test three metric definitions |

**Check your understanding:** Why can a feature raise conversion and still be bad? What is the difference between rolling and bounded retention, and when does it matter? Why version metric definitions?

### Chapter 2 · Event instrumentation (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Tracking plans | Event naming, properties, schemas (JSON Schema), versioning, reviews | Write a tracking plan for your Year 3 app |
| 2.2 Identity | Anonymous install IDs, login merges, multiple devices, reinstall | Handle a user who installs, browses, logs in and switches phones |
| 2.3 Reliable delivery | Outbox-based queues (from MOB304), batching, retries, deduplication IDs, offline periods | Lose under 0.1% of events across 50 kill/offline cycles |
| 2.4 Time | Device clock skew, client vs server timestamps, sessionisation | Correct a dataset with skewed device clocks |
| 2.5 SDK cost and quality | Startup and size cost of analytics SDKs; schema validation; data-quality tests | Measure your SDK's startup cost; block invalid events in CI |

**Check your understanding:** Why does a missing deduplication ID inflate conversion? What goes wrong if you sessionise using device time? How much startup time is an analytics SDK worth?

### Chapter 3 · Pipelines and analysis (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 From device to warehouse | Firebase export to BigQuery, open-source pipelines (RudderStack, PostHog), event collectors | Load a day of events into a warehouse |
| 3.2 SQL for product analysis | Window functions for funnels, cohorts and retention | Recreate three dashboard numbers by hand in SQL |
| 3.3 Data contracts | Schema ownership between app and data teams; breaking-change rules | Ship a property rename without breaking a dashboard |
| 3.4 AI-assisted analysis | Text-to-SQL and notebook assistants; checking generated queries | Find the bug in five AI-written funnel queries |

**Check your understanding:** Why do dashboards built on raw events disagree with each other? What makes a funnel query double-count? How do you check an AI-written query you cannot fully read?

### Chapter 4 · Feature flags and remote config (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Flag types | Release, experiment, operational kill switch, permission flags; lifetimes | Classify 20 flags in a sample app |
| 4.2 Evaluation | Server-side vs on-device evaluation; caching; safe defaults when config cannot load | Cold start with no network uses correct defaults |
| 4.3 Standards and tools | OpenFeature; Firebase Remote Config, GrowthBook, PostHog, Statsig, LaunchDarkly | Swap providers behind an OpenFeature interface |
| 4.4 Flag debt | Expiry dates, cleanup automation, testing flag combinations | A CI check for expired flags |

**Check your understanding:** When config cannot load, should a feature behind a kill switch default to on or off, and what decides it? What does on-device flag evaluation reveal to someone inspecting the app? Why do old flags cause incidents?

### Chapter 5 · A/B testing fundamentals (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Randomisation | Unit (user, device, install), deterministic hashing with salts, consistent assignment across platforms | Assign 100,000 IDs identically on Android, iOS and server |
| 5.2 Hypotheses and power | Minimum detectable effect, sample size, test duration | Compute sample size for a 2% relative lift |
| 5.3 Analysis | Difference in means and proportions, confidence intervals, ratio metrics and the delta method | Analyse a provided experiment |
| 5.4 Peeking and stopping | Why repeated looks inflate false positives; sequential tests | Simulate peeking; measure the false-positive rate |
| 5.5 Many metrics | Multiple comparisons, primary vs secondary metrics, guardrails | Pre-register an experiment plan |

**Check your understanding:** Why is per-session randomisation wrong for most app experiments? What happens to your error rate if you check results daily and stop at the first significant day? Why declare the primary metric before starting?

### Chapter 6 · Mobile-specific experiment pitfalls (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Version adoption lag | Code must ship in a binary before a flag can expose it; users on old versions | Model how long until 80% of users can see a variant |
| 6.2 Exposure and sample-ratio mismatch | Logging exposure at the right moment; SRM checks (Fabijan et al., KDD 2019) | Diagnose three planted SRM causes |
| 6.3 Novelty, learning and seasonality | Novelty and primacy effects; festival and payday seasonality in India | Detect a novelty effect in time-series results |
| 6.4 Interference | Marketplaces and social features; switchback and cluster designs | Design a test for a delivery-fee change |
| 6.5 Variance reduction | CUPED (Deng et al., WSDM 2013), stratification, holdouts | Cut required sample size with CUPED on provided data |

**Check your understanding:** An experiment shows a 52/48 split instead of 50/50: why is that alarming? Why can't you A/B test delivery fees by user in a marketplace? What does a long-term holdout tell you that a two-week test cannot?

### Chapter 7 · Attribution and privacy (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Install attribution | Play Install Referrer API, mobile measurement partners, deferred deep links after Firebase Dynamic Links | Attribute installs from three test campaigns |
| 7.2 iOS rules | ATT prompt rules, AdAttributionKit and SKAdNetwork, Apple's prohibition on tracking without permission; the EU alternative ATT prompt (iOS 27.2) | Design an ATT pre-prompt that informs without pressuring |
| 7.3 Android after Privacy Sandbox | Google's October 2025 retirement of Topics, Attribution Reporting and SDK Runtime; what remains | Write an Android measurement plan for 2027 |
| 7.4 Consent and disclosure | DPDP notice and consent; Play Data safety and Apple privacy labels must match SDK behaviour | Audit your app's analytics against its disclosures |

**Check your understanding:** Why is fingerprinting a device to replace ATT not acceptable? What can you still measure on iOS without tracking permission? What happens when the Data safety form and real traffic disagree?

### Chapter 8 · Growth levers (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Onboarding and activation | Time to first value, permission timing, OTP friction | Test two onboarding orders with synthetic users |
| 8.2 Notifications | Opt-in priming, frequency caps, measuring opt-outs and uninstalls, quiet hours | Design a notification policy with guardrails |
| 8.3 Referrals | Deep-link invites, rewards, defensive fraud checks (self-referrals, device farms) | Build referral attribution with abuse checks |
| 8.4 Ratings and store pages | Play In-App Review and Apple's review request rules; Play store listing experiments; App Store product page optimisation | Plan a store-listing test |
| 8.5 Speed and size as growth | Startup time and download size as conversion levers (Zomato, Google Play data) | Estimate install impact of a 10 MB reduction |

**Check your understanding:** Why can more notifications raise D1 retention and lower D30? What makes a referral programme easy to abuse? Why is app size a growth metric in India?

### Chapter 9 · Personalisation and ethics (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Bandits | Thompson sampling vs fixed A/B tests; when bandits mislead | Simulate a bandit and an A/B test on the same data |
| 9.2 Personalisation | Simple rules, recommendations, uplift modelling (concepts) | Target a promotion with an uplift baseline |
| 9.3 Dark patterns | India's 2023 dark-pattern guidelines (false urgency, basket sneaking, confirm shaming, subscription traps); deceptive design in general | Audit three app flows and fix any dark pattern |
| 9.4 Fairness and user welfare | Long-term harms of engagement optimisation; guardrails for vulnerable users | Add a welfare guardrail to an experiment plan |

**Check your understanding:** When does a bandit give a misleading answer about which variant is better? Why can a "limited time" banner be illegal in India? What guardrail would stop an experiment that harms users but lifts revenue?

### Chapter 10 · Building an experimentation platform (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Architecture | Assignment service, config delivery, exposure logging, analysis pipeline, results UI | Design document for a small platform |
| 10.2 Automation | SRM alerts, guardrail auto-stop, A/A tests as health checks | Run 1,000 simulated A/A tests through your pipeline |
| 10.3 Governance | Experiment review, pre-registration, documentation, privacy review | Write the review checklist |
| 10.4 Build vs buy | Costs and lock-in of vendors vs open-source vs in-house | Recommendation memo for a 20-engineer startup |

**Check your understanding:** Why run A/A tests continuously? What should trigger an automatic stop? When is building your own platform a mistake?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Metric tree and metrics as code | — |
| 2 | 2 | Lab 2 · Tracking plan and identity | — |
| 3 | 2 | Lab 3 · Reliable event queue | **P1 due** |
| 4 | 3 | Lab 4 · Warehouse SQL | — |
| 5 | 4 | Lab 5 · Flags with safe defaults | — |
| 6 | 5 | Lab 6 · Power and peeking simulations | — |
| 7 | 5 | Lab 6 (cont.) | Mid-term (AI off) |
| 8 | 6 | Lab 7 · SRM and CUPED | — |
| 9 | 7 | Lab 8 · Attribution and disclosure audit | — |
| 10 | 8 | Lab 9 · Growth levers | **P2 due** |
| 11 | 8 | Lab 9 (cont.) · Referral abuse checks | — |
| 12 | 9 | Lab 10 · Bandits and dark-pattern audit | — |
| 13 | 10 | Platform build | — |
| 14 | 10 | A/A health checks | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting tracking plans and schemas; writing SQL for funnels and cohorts (then checking it); generating synthetic event data; explaining statistical methods; reviewing an experiment plan for missing guardrails.
- **Do without AI (drills):** power and sample-size calculations; diagnosing SRM; deciding the randomisation unit; reading an experiment result and writing the decision; the mid-term and final.
- **Verify AI output by:** (1) reproducing every dashboard number with a hand-written query on a small sample; (2) running A/A simulations through any analysis code; (3) checking that exposure is logged where the user can first see the change; (4) comparing disclosures with a network capture.
- **Where AI still fails here (collect your own evidence):** keep examples of generated queries that double-count events, ignore deduplication or time zones (IST vs UTC day boundaries), analyse per-session when assignment was per-user, or declare a winner after peeking. Each entry needs the check that caught it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 25% |
| Privacy and dark-pattern audit | 5% |

**Mastery gate.** You pass when you can, with AI tools off: (1) design an experiment for a stated mobile change, choosing unit, metrics, guardrails, sample size and duration, in 30 minutes; (2) given raw results with a planted problem (SRM, peeking, version lag or double-counted events), find it and state the correct decision; (3) show your P3 platform's A/A false-positive rate within 4–6% over 1,000 simulations.

## Industry reality

Netflix has described experimentation as central to its product decisions in its technology blog, and Kohavi, Tang and Xu's *Trustworthy Online Controlled Experiments* (2020) documents practices from large experimentation platforms. On mobile, the binary-release cycle adds problems the web does not have: features must ship before they can be tested, and old versions linger. Privacy rules shape what can be measured: ATT on iOS, the retirement of Privacy Sandbox on Android, store disclosure rules, and India's DPDP Rules and 2023 dark-pattern guidelines.

**Interview questions from this course**

1. *Test a redesigned checkout button. Walk through the experiment end to end.* Strong answer: hypothesis and primary metric; per-user randomisation; exposure at first render; guardrails (crashes, latency, refunds); power and duration including weekly cycles; version-adoption plan; SRM check; decision rule written in advance.
2. *Treatment shows +8% conversion, but the split is 52/48 with p < 0.001 for SRM. What now?* Strong answer: results are untrusted; look for exposure-logging bugs, crashes in one arm, bot or old-version filtering, redirect differences; fix and rerun rather than adjust.
3. *How do you measure install attribution on iOS and on Android in 2026?* Strong answer: ATT consent rules and AdAttributionKit/SKAdNetwork aggregate data; Play Install Referrer; deep links after Dynamic Links; the retirement of Privacy Sandbox on Android; no fingerprinting; disclosures that match.
4. *Design a feature flag system that works offline and does not slow startup.* Strong answer: cached config with safe defaults; asynchronous refresh; flags read once per session for experiments; on-device evaluation trade-offs; kill switches; expiry and cleanup.
5. *Push notifications raised D1 retention but uninstalls also rose. Decide.* Strong answer: looks at long-term retention and holdouts; counts opt-outs and uninstalls as guardrails; segments by user type; considers frequency caps; makes a decision that weighs user welfare, not only the short-term metric.

## Resources (free first)

- **Experimentation:** Kohavi et al., "Trustworthy online controlled experiments: five puzzling outcomes explained" (KDD 2012); Deng et al., "Improving the sensitivity of online controlled experiments by utilizing pre-experiment data" (CUPED, WSDM 2013); Fabijan et al., "Diagnosing sample ratio mismatch in online controlled experiments" (KDD 2019); Netflix Technology Blog, "It's All A/Bout Testing" (2016) — https://netflixtechblog.com/its-all-a-bout-testing-the-netflix-experimentation-platform-4e1ca458c15
- **Tools:** Firebase Remote Config — https://firebase.google.com/docs/remote-config ; Firebase A/B Testing — https://firebase.google.com/docs/ab-testing ; OpenFeature — https://openfeature.dev/ ; GrowthBook — https://www.growthbook.io/ ; PostHog — https://posthog.com/
- **Platform rules:** App Tracking Transparency — https://developer.apple.com/documentation/apptrackingtransparency ; AdAttributionKit — https://developer.apple.com/documentation/adattributionkit ; Play Install Referrer — https://developer.android.com/google/play/installreferrer ; Privacy Sandbox status — https://privacysandbox.google.com/overview/status ; Play Data safety — https://support.google.com/googleplay/android-developer/answer/10787469
- **Paid, optional:** Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020). The papers above cover the core methods.

## Sources

- Apple, App Review Guidelines 5.1.2 (ATT permission required for tracking) — https://developer.apple.com/app-store/review/guidelines/ ; Apple Developer News, EU ATT update (16 Sep 2026) — https://developer.apple.com/news/ (checked 2026-10)
- Google, "Update on Plans for Privacy Sandbox Technologies" (Oct 2025) — https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies ; status page — https://privacysandbox.google.com/overview/status (checked 2026-10)
- Firebase Dynamic Links FAQ (shutdown 25 Aug 2025) — https://firebase.google.com/support/dynamic-links-faq (checked 2026-10)
- Press Information Bureau, DPDP Rules 2025 (Nov 2025) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf (checked 2026-10)
- SCC Online, "CCPA notifies Guidelines for Prevention and Regulation of Dark Patterns, 2023" (4 Dec 2023) — https://www.scconline.com/blog/post/2023/12/04/ccpa-notifies-guidelines-for-prevention-and-regulation-of-dark-patterns-2023-legal-news/ (checked 2026-10)
- Zomato developer story — https://developer.android.com/stories/apps/zomato ; Google Play, "Shrinking APKs, growing installs" (2017) — https://medium.com/googleplaydev/shrinking-apks-growing-installs-5d3fcba23ce2 (checked 2026-10)

_Last reviewed: 2026-10_
