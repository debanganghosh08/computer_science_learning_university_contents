# MOB401 · Labs and projects

Every performance number comes from a release build on a named physical device, with at least 10 iterations, the median and p90, and the device's thermal state noted. One device must be low-end (2–3 GB of RAM). Security work is defensive: it targets only your own apps and the OWASP MASTG reference apps, never third-party apps or services. Labs 2 and 4 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Budgets and baselines | Define budgets for startup, frames, memory, size and bytes per session; capture baselines | Budget table; baseline data with confidence intervals | 4 h |
| 2 · Startup tracing (no AI) | Label every phase of a cold start in Perfetto; generate a Baseline Profile; measure iOS launch | Annotated trace; before/after medians for three changes | 7 h |
| 3 · Jank and hangs | Frame-timing benchmark for a feed; remove one hitch and one hang | `FrameTimingMetric` and Instruments results before and after | 5 h |
| 4 · Memory and ANR triage (no AI) | Fix two leaks; triage 20 provided ANR reports | Retained-size drop; ANR classification with root causes | 6 h |
| 5 · Energy | 60-minute energy measurement of one feature; remove a wake lock or excess polling | Battery Historian or Xcode energy report before and after | 5 h |
| 6 · Size budget | Cut download size by 20%; verify 16 KB alignment; add a CI size check | `bundletool` and App Store Connect size reports; failing CI run on a planted 2% increase | 5 h |
| 7 · Threat model and MASTG tests | STRIDE threat model; five MASTG tests on your own app | Threat model; test results mapped to MASVS controls | 5 h |
| 8 · Secure storage, biometrics, integrity | Non-exportable keys; biometric-bound action; server-verified Play Integrity or App Attest; pinning decision record | Code, tests and a one-page decision record | 7 h |
| 9 · Pipeline and performance gates | Commit-to-store pipeline with signing, tests and statistical performance gates | Pipeline run links; a blocked planted regression | 7 h |
| 10 · Rollout and incident | Staged rollout gates; a simulated bad release; post-mortem | Gate configuration; incident timeline; blameless post-mortem | 4 h |

## Projects

### P1 · Performance audit with a merged-quality fix (L1, ~6 hours)

**Real-world inspiration:** Zomato's published startup project traced every SDK initialised at launch with Perfetto, then removed or lazy-loaded the costly ones, cutting cold start on low- and mid-end devices by up to 30%.

**What to build:** pick your Year 3 app or an open-source Android or iOS app with a public repository. Measure startup, a key scroll and memory; find the largest avoidable cost; fix it; write a report suitable for a pull request.

**Acceptance criteria:**
- **Method:** Macrobenchmark `StartupTimingMetric` or `XCTApplicationLaunchMetric`, at least 10 iterations, release build, low-end device, before and after.
- **Result:** at least a 10% improvement in median time to initial display or launch time, or a documented negative result showing with traces why the obvious fix did not help.
- **Evidence:** annotated trace screenshots; a table of every startup task with its cost.
- **Upstream quality:** the change is small, tested and explained so a maintainer could merge it (submitting upstream is encouraged, not required).

**Stretch goals:** add a Baseline Profile and a startup benchmark to the project's CI; repeat the audit for the scroll path.

**What it proves to an employer:** you measure before you optimise and can explain a performance change with evidence.

### P2 · MASVS assessment and hardening of your own app (L2, ~15 hours)

**Real-world inspiration:** OWASP's MASVS and MASTG are the common reference for mobile security reviews at banks, fintechs and app-security teams. This project applies them defensively to an app you wrote.

**What to build:** a threat model; an assessment of your app against every MASVS v2.1.0 control group using MASTG tests; fixes for the findings; automated checks so they do not return.

**Acceptance criteria:**
- **Coverage:** a findings table covering all eight MASVS groups, each finding with severity, evidence, fix or accepted risk with justification.
- **Storage:** an automated test shows no tokens or personal data in plaintext in app storage, logs or backups after a full user session.
- **Platform:** a manifest and entitlements check in CI fails on any exported component without a written justification.
- **Secrets:** a scripted search of the release APK/IPA finds no API secrets.
- **Integrity:** a sensitive endpoint rejects requests without a valid, server-verified Play Integrity verdict or App Attest assertion (tested with a debug-signed build of your own app).
- **Network:** cleartext traffic disabled; a written pinning decision following platform guidance (backup pins and expiry, or a reasoned decision not to pin).
- **Privacy:** at least one identifier or permission removed under MASVS-PRIVACY, with the user-facing impact described.

**Stretch goals:** a biometric-bound key for a high-value action with a fallback that is not weaker than the original; screenshot and app-switcher protection for sensitive screens; a MASVS-RESILIENCE discussion of what obfuscation does and does not buy.

**What it proves to an employer:** you can review and harden a mobile app against the industry standard and keep it hardened with automation, a core skill for mobile security and fintech teams.

### P3 · Release pipeline with performance, size and crash gates (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** large mobile teams ship on release trains with automated quality gates and staged rollouts, because a bad mobile build cannot be pulled back from users' phones. Your pipeline is an illustrative scenario at student scale, built on real store tooling.

**What to build:**
- **CI:** unit, screenshot and instrumented tests (Firebase Test Lab or local devices); flaky-test quarantine; build caching.
- **Gates:** startup and frame-timing benchmarks with statistical thresholds; per-module size budgets; MASVS checks from P2.
- **CD:** signing without secrets in the repository; Fastlane or Gradle Play Publisher to the Play internal track, and to TestFlight for iOS.
- **Rollout automation:** staged rollout percentages with a halting rule that reads crash and ANR data (Crashlytics, the Play Developer Reporting API or Sentry); symbol uploads (R8 mappings, dSYMs).
- **Operations:** kill switches through remote config; a release runbook; a release-readiness checklist covering policy deadlines.

**Acceptance criteria:**
- **Speed:** commit to internal track or TestFlight in under 30 minutes for a typical change.
- **Gates work:** a planted 5% startup regression and a planted 2% size increase each block the pipeline; a gate's false-alarm rate over 20 unchanged runs is reported and under 10%.
- **Test health:** flaky rate under 2% over the last 50 runs.
- **Production quality:** two releases through a closed test or TestFlight (at least 12 testers) with crash-free users at least 99.5% and no ANR cluster above Play's 0.47% threshold.
- **Halting:** a deliberately crashing build is halted automatically at or before 20% rollout, and the timeline is recorded.
- **Debuggability:** a crash from an obfuscated release build is symbolicated in the dashboard within 10 minutes.
- **Write-up:** pipeline diagram, gate statistics, incident post-mortem from the halting drill, and the compliance calendar for the next 12 months.

**Stretch goals:** release-train automation (weekly branch cut, release notes from commit messages); per-device-tier dashboards; a canary channel of internal users before every rollout.

**What it proves to an employer:** you can own mobile release engineering, the role that keeps large apps fast and stable as many engineers ship at once.

## Feeds into

- [MOB501 Frontier Seminar](../../year_5/MOB501_frontier_seminar_wearables_ar_and_ambient/README.md): performance budgets for watches, headsets and glasses.
- [MOB403 Mobile System Design](../MOB403_mobile_system_design/README.md) and [MOB404 Mobile Analytics, Experimentation and Growth Engineering](../MOB404_mobile_analytics_experimentation_and_growth/README.md): gates and kill switches become part of every design and experiment.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) and the [Mobile Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md).
