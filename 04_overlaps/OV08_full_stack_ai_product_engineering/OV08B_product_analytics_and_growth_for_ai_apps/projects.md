# OV08B · Labs and projects

Labs use your OV08A product where it has real users, and a provided synthetic event generator (2 million events, 40,000 users, with planted bugs: duplicate events, bots, a redirect that biases assignment) where it does not. Analytics must respect the consent and purpose rules set in Lab 10; prompt and output text never enters the analytics store. Lab 5, all power calculations, the mid-term and the final are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Metric tree | North Star, inputs, guardrails and an activation definition tied to successful outcomes | Metric tree; activation definition with a validation plan | 4 h |
| 2 · Tracking plan and event CI | 25-event plan with typed schemas; CI validation; identity stitching; bot and internal-user filters | Plan; CI blocking a malformed event; count of filtered events | 6 h |
| 3 · AI signals joined to traces | Accept, edit distance, copy, regenerate, abandon and feedback events carrying trace IDs | Query linking a cohort's first-answer quality signal to its traces | 5 h |
| 4 · dbt models and data tests | Sessions, daily activity, funnel and retention models; uniqueness and freshness tests; reconciliation with server counts | Passing dbt build; a test catching the planted duplicate bug | 6 h |
| 5 · Retention and survival (no AI) | Cohort retention table and Kaplan–Meier curves by first-week experience | Notebook; results within 1% of the key | 5 h |
| 6 · Production quality review | Stratified 200-item sample; judge calibrated on 100 human labels; quality by cohort | Review protocol; agreement statistics; quality dashboard | 6 h |
| 7 · Trustworthy experiments | Detect a planted SRM; A/A test; CUPED; simulate peeking; run one sequential test; one prompt A/B with cost and latency guardrails | Readout per experiment with intervals and decision | 10 h |
| 8 · Onboarding experiment | Change onboarding to shorten time to first success; holdout | Pre-registration; result; decision | 5 h |
| 9 · Unit economics | Cost to serve per cohort from traces; margin under three limit policies; payback model | Spreadsheet or notebook with sensitivity table | 5 h |
| 10 · Consent and attribution audit | Check what fires before consent; purpose of each event; three attribution models compared | Audit with fixes; attribution comparison | 4 h |

## Projects

### P1 · Instrumented AI feature with a trustworthy event pipeline (L1, ~6 hours)

**Real-world inspiration:** acceptance rate as the metric that best reflected perceived productivity in GitHub's Copilot study (Ziegler et al., 2022).

**What to build:** instrumentation for one AI feature: tracking plan, client and server events, identity handling, AI implicit signals joined to traces, and a warehouse table of daily activity.

**Acceptance criteria:**
- Event schemas validated in CI; a malformed event fails the build.
- Server-confirmed outcomes reconcile with production counts within 1% over a week (or over the synthetic dataset).
- Bot and internal traffic filtered; the report states how many events and users were removed.
- At least four implicit AI signals recorded with trace IDs; no prompt or output text stored in analytics (a scanner over the events table finds none).

**Stretch goals:** an event-loss estimate for ad blockers; a data contract with the backend team.

**What it proves to an employer:** you can produce numbers that other people can trust.

### P2 · Experimentation toolkit for prompts and models (L2, ~15 hours)

**Real-world inspiration:** CUPED (Deng et al., 2013) and the SRM taxonomy (Fabijan et al., 2019) from Microsoft's experimentation platform; always-valid inference for continuous monitoring (Johari et al.).

**What to build:** an experiment library and readout generator for your product: deterministic assignment by user, exposure logging, SRM check, CUPED, a sequential test option, guardrails for cost per task, latency and refusal rate, and a templated one-page readout.

**Acceptance criteria:**
- **Assignment:** hashing-based assignment reproduces the same arm for a user across devices and sessions (tested on 10,000 users).
- **SRM:** the planted redirect bug is flagged (p < 0.001) and the readout refuses to report effects until resolved.
- **Validity:** 1,000 simulated A/A tests show a false-positive rate within 4–6% at α = 0.05 for the fixed-horizon test, and within the nominal rate for the sequential method under daily peeking.
- **Sensitivity:** CUPED reduces the variance of the primary metric by at least 20% on the provided data, with the reduction reported.
- **Guardrails:** a variant that raises cost per task by more than 15% is marked "do not ship" regardless of engagement.
- **One real experiment:** a prompt or model change run on your product (or the synthetic stream), with pre-registration and a written decision.

**Stretch goals:** interleaving for a ranking change; heterogeneous effects by language with multiplicity correction.

**What it proves to an employer:** you can run experiments on AI features whose results deserve belief.

### P3 · Growth and value review of a live AI product (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** the measurement problems unique to AI products: quality as a metric, marginal cost per action, and signals that live in the interface.

**What to build:** a complete measurement and growth review of your OV08A product (or a partner's product with permission): metric tree, dashboards with linked definitions, retention by cohort, production quality review joined to engagement, two experiments (one on onboarding, one on a prompt or model), unit economics per cohort, a consent and attribution audit, and a decision memo recommending what to build, fix or remove next.

**Acceptance criteria:**
- **Data quality:** every dashboard metric is defined once in code; reconciliation tests pass; definitions are linked from every chart.
- **Retention:** cohort retention and Kaplan–Meier curves with cohort sizes and confidence bands.
- **Quality:** a stratified weekly review of at least 200 items for 3 weeks with a calibrated judge (agreement ≥ 85%) and its association with 2-week retention, reported with caveats.
- **Experiments:** two completed experiments with pre-registration, SRM checks and guardrails; at least one decision follows the guardrail even if engagement improved.
- **Economics:** cost to serve and gross margin per cohort; the heavy-user tail quantified; one limit or pricing proposal with simulated impact.
- **Privacy:** consent audit passes (no non-essential tracking before consent); no content in analytics; notice text included.
- **Decision memo:** two pages, reviewed by a panel; every number traceable to a query.
- **AI-error log:** at least five AI-generated analysis errors you caught, with the check that caught each.

**Stretch goals:** a natural-experiment analysis of an outage or staggered launch; a public, privacy-safe usage report with thresholds.

**What it proves to an employer:** you can tell a founder or product lead what is working, what it costs, and what to do next, with numbers that hold up.

## Feeds into

The OV08 capstone in the [overlap README](../README.md); [LCH502](../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) for founders; [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) for a thesis on measuring AI product quality; and product and growth interview loops in [06_career_and_market_readiness](../../../06_career_and_market_readiness/).
