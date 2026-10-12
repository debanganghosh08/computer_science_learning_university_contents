# MOB404 · Labs and projects

The course provides a user simulator that generates realistic event streams (installs, sessions, funnels, offline gaps, skewed clocks, reinstalls and app-version lag) with planted effects you must find. Experiments on real people happen only inside your own closed test or TestFlight group, with informed consent and no deception, and never use dark patterns. Labs 6 and 7 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Metric tree and metrics as code | North star, inputs and guardrails for a food-delivery app (illustrative); three metric definitions with tests | Metric tree; tested SQL definitions in version control | 4 h |
| 2 · Tracking plan and identity | Tracking plan for your Year 3 app; install, login, reinstall and device-switch identity cases | Plan with schemas; identity test cases passing | 5 h |
| 3 · Reliable event queue | Outbox-based event queue with batching, retries and deduplication IDs | Loss and duplicate rates across 50 kill/offline cycles | 5 h |
| 4 · Warehouse SQL | Funnels, cohorts and retention in SQL; find bugs in five AI-written queries | Queries; bug list with explanations; IST vs UTC day-boundary test | 5 h |
| 5 · Flags with safe defaults | OpenFeature interface over two providers; cold start with no network | Tests for defaults, caching and an expired-flag CI check | 4 h |
| 6 · Power and peeking (no AI) | Sample-size calculations; simulate daily peeking and measure false positives | Hand calculations; simulation plots | 5 h |
| 7 · SRM and CUPED (no AI) | Diagnose three planted SRM causes; apply CUPED to provided data | Diagnosis notes; variance reduction achieved | 5 h |
| 8 · Attribution and disclosure audit | Play Install Referrer and a deferred deep link; compare analytics traffic with Data safety and privacy labels | Attribution results; audit table of mismatches and fixes | 5 h |
| 9 · Growth levers | Onboarding order test and notification policy in the simulator; referral attribution with abuse checks | Results with guardrails; blocked self-referral and device-farm cases | 6 h |
| 10 · Bandits and dark-pattern audit | Thompson sampling vs A/B on the same data; audit three flows against India's 2023 dark-pattern guidelines | Simulation comparison; audit with fixes | 4 h |

## Projects

### P1 · Trustworthy instrumentation for your app (L1, ~6 hours)

**Real-world inspiration:** product teams at consumer apps rely on event data for every decision, and the most common failure is not the analysis but missing, duplicated or mis-timed events from phones that go offline and get killed.

**What to build:** a tracking plan with JSON Schemas for your Year 3 app; an event queue on the outbox pattern; identity handling for anonymous and logged-in users; schema validation in CI; an updated Data safety form and privacy label.

**Acceptance criteria:**
- **Completeness:** across 50 scripted kill and offline cycles, under 0.1% of events are lost and under 0.1% duplicated (reconciled against a device-side ledger).
- **Cost:** the SDK adds under 30 ms to median cold start (10 runs, release build, low-end device).
- **Quality gate:** an event that violates its schema fails CI.
- **Time:** events carry both client and server timestamps; a test with a device clock set 3 hours wrong produces correct session boundaries.
- **Honesty:** disclosures match a network capture of one session.

**Stretch goals:** sampling for high-volume events; a debug overlay that shows events as they fire.

**What it proves to an employer:** you can produce event data analysts can trust, which most mobile teams struggle with.

### P2 · A valid experiment, start to finish (L2, ~15 hours)

**Real-world inspiration:** experimentation teams pre-register experiments, compute power, check sample-ratio mismatch and reduce variance with methods such as CUPED (Deng et al., 2013). This project applies the full method to a simulated population.

**What to build:** a feature flag and two variants of a flow in your app; a pre-registration document (hypothesis, unit, primary metric, guardrails, sample size, duration, decision rule); exposure logging; an analysis notebook with confidence intervals, an SRM check and CUPED; runs against the user simulator.

**Acceptance criteria:**
- **Calibration:** over 1,000 simulated A/A tests, your pipeline's false-positive rate is between 4% and 6% at α = 0.05.
- **Power:** a planted 3% relative lift is detected in at least 80% of 500 simulated runs at your computed sample size.
- **Validity checks:** all three planted problems are caught: an SRM caused by exposure logging, a version-lag effect and a novelty effect.
- **Variance reduction:** CUPED reduces the required sample size, and the reduction is reported.
- **Decision:** a one-page decision memo that follows the pre-registered rule.

**Stretch goals:** a sequential testing method that allows safe early stopping; a switchback design for a simulated marketplace-fee change.

**What it proves to an employer:** you can run experiments whose results deserve to be believed, which is rarer than running experiments.

### P3 · Mobile experimentation platform (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** companies with large apps build or buy experimentation platforms with deterministic assignment, config delivery, exposure logging, automated health checks and guardrail-based stopping. Open-source tools such as GrowthBook and PostHog show the components. Your platform is an illustrative scenario at student scale.

**What to build:**
- **Assignment SDKs:** for Android and iOS (or one cross-platform SDK) plus the server, using the same salted hash so every surface agrees.
- **Config delivery:** safe defaults, caching, asynchronous refresh, no work on the startup critical path.
- **Exposure logging:** through your P1 pipeline into a warehouse.
- **Analysis service:** metrics as code, confidence intervals, SRM alerts, CUPED, guardrails with automatic stop, a results page.
- **Governance:** a review checklist covering pre-registration, privacy (DPDP notice and consent, ATT applicability, store disclosures) and dark-pattern rules.
- **One real experiment:** a low-risk change (for example onboarding copy) in your closed test or TestFlight group, with consent; the small sample means you report the method and the honest uncertainty, not a "winner".

**Acceptance criteria:**
- **Consistency:** 100,000 IDs receive identical assignments on Android, iOS and the server.
- **Startup:** config fetching adds no measurable time to median cold start (shown with traces and 10-run medians).
- **Calibration:** A/A false-positive rate between 4% and 6% over 1,000 simulated tests run through the full platform.
- **Automatic stop:** a planted 1-percentage-point rise in crash rate in one arm triggers an alert and stops the experiment within one analysis cycle.
- **SRM:** a planted 51/49 split on 200,000 users raises an SRM alert.
- **Governance:** the completed review checklist for the real experiment, including the consent text shown to testers.

**Stretch goals:** multi-armed bandit mode with guardrails; mutually exclusive experiment layers; holdout groups for long-term effects.

**What it proves to an employer:** you can build the system that lets a mobile team learn safely and quickly, a senior growth-engineering skill that also anchors a founder's product practice.

## Feeds into

- [OV08 Full-Stack AI Product Engineering](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/README.md): OV08B's product analytics for AI apps builds on this platform.
- [OV07 Privacy Engineering](../../../../04_overlaps/OV07_privacy_engineering/README.md): consent, disclosure and measurement under privacy law.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) and the [Mobile Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md).
