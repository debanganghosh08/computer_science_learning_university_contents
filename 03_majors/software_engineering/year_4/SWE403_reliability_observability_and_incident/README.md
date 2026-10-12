# SWE403 · Reliability, Observability and Incident Engineering for Developers

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [SWE303](../../year_3/SWE303_programming_languages_in_practice_go_rust/README.md); recommended [SWE305](../../year_3/SWE305_concurrency_and_performance_engineering/README.md) and [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) | [SWE501](../../year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md); deeper operations electives [OPS303](../../../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md), [OPS304](../../../devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md) |

## Why this course matters now

Google's SRE book observes that roughly 70% of outages are due to changes in a live system, and recent public incidents show how developer decisions become global outages. On 12 June 2025, a Google Cloud code path added without a feature flag or error handling met a policy with blank fields and sent Service Control into a global crash loop for hours. On 18 November 2025, a permissions change made Cloudflare's bot-management feature file double in size; Rust code called `unwrap()` on the resulting error and core traffic failed for about three hours. On 19–20 October 2025, a race condition in DynamoDB's DNS automation left the us-east-1 endpoint with no addresses, and the disruption rippled across AWS for about 14.5 hours. In July 2024, a faulty content update for CrowdStrike's Falcon sensor crashed about 8.5 million Windows devices. Meanwhile, AI assistants are used far less for operations than for writing code: only 20% of AI users use them for deploying, operating or troubleshooting production systems (Stack Overflow, October 2026), and DORA 2025 found AI adoption still goes with lower delivery stability. Platform and SRE teams own the infrastructure (taught in OPS303 and OPS304). This course is about the developer's half of reliability: code that is observable, configuration that is validated, changes that roll out safely, and engineers who can lead an incident and learn from it.

## Learning outcomes

By the end you can:

1. **Define** SLIs and SLOs for request, asynchronous and data-freshness workloads, and **alert** on error-budget burn rates instead of symptoms.
2. **Instrument** a service with structured logs, metrics and OpenTelemetry traces that answer questions you did not anticipate, at a controlled cost.
3. **Debug** a production problem from telemetry alone: traces, logs, metrics and continuous profiles.
4. **Implement** resilience in code (deadlines, retry budgets, circuit breakers, bulkheads, fallbacks) and **choose** fail-open or fail-closed per dependency.
5. **Validate** configuration and data pushes like user input, and **roll them out** in stages with kill switches.
6. **Ship** changes with progressive delivery, automated canary analysis, backwards-compatible schema changes and rehearsed rollbacks.
7. **Lead** an incident as incident commander or operations lead, and **communicate** clearly under pressure.
8. **Write** blameless postmortems with contributing factors and action items that reduce risk.

## Chapters and lessons

### Chapter 1 · Reliability from the developer's chair (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Where outages come from | Code changes, configuration and data pushes, dependencies, capacity, latent bugs; "~70% of outages are due to changes" (SRE book) | Classify 10 public postmortems by trigger and by latent cause |
| 1.2 Reading a postmortem | Timeline, impact, trigger, root and contributing factors, remediation | Annotate Cloudflare's 18 Nov 2025 report: which developer practice would have stopped it? |
| 1.3 Operability as a feature | Health and readiness endpoints, graceful shutdown, safe defaults, admin endpoints | Add operability features to a provided service; review each |
| 1.4 Delivery metrics | DORA's change failure rate and recovery time beside throughput; AI as an amplifier | Compute change failure rate for a public repo's releases and reverts |

**Check your understanding:** Why are configuration pushes as dangerous as code deploys? What made the Google Cloud June 2025 bug latent for two weeks? Why should a team track change failure rate alongside deployment frequency?

### Chapter 2 · SLIs and SLOs from the code side (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Choosing SLIs | Availability and latency SLIs measured at the right point; good-event/valid-event ratios | Define SLIs for a payment-status API and a search API |
| 2.2 Writing SLOs | Targets, windows, what users notice; SLOs for dependencies | SLO document for your P2 service |
| 2.3 Error budgets and burn-rate alerts | Multi-window, multi-burn-rate alerting (SRE Workbook) | Implement burn-rate alerts in Prometheus; test with injected errors |
| 2.4 Beyond request/response | SLOs for queues, batch jobs, data freshness, mobile clients | SLO for a nightly settlement job and for a notification pipeline |

**Check your understanding:** Why is a 100% SLO a mistake? Why do burn-rate alerts page less and catch more than threshold alerts? How do you write an SLO for a job that runs once a day?

### Chapter 3 · Structured logging (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Events, not narration | Structured JSON logs, levels, stable field names, correlation and trace IDs | Convert a service's printf logs to structured events |
| 3.2 Canonical log lines | One wide event per request with everything about it (Stripe's practice) | Add canonical log lines; answer 5 questions with one query each |
| 3.3 Privacy and safety | Redacting personal data (DPDP Act 2023), secrets in logs, log injection | Build a redaction filter; test it against planted PII |
| 3.4 Cost and sampling | Volume, retention tiers, dynamic sampling, keeping all errors | Cut log volume by 80% without losing any error event |

**Check your understanding:** Why are wide structured events more useful than many small log lines? What must never appear in logs, and how do you enforce it? Which events should never be sampled?

### Chapter 4 · Metrics in code (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Instrument types | Counters, gauges, histograms; RED (rate, errors, duration) and USE | Instrument an HTTP service with RED metrics |
| 4.2 Histograms and percentiles | Bucket choice, native/exponential histograms, why you cannot average percentiles | Show a wrong p99 from averaging; fix it |
| 4.3 Cardinality | Label explosions (user IDs in labels); exemplars linking metrics to traces | Cause a cardinality explosion in a test Prometheus; repair it |
| 4.4 Conventions | OpenTelemetry semantic conventions; naming and units | Review a dashboard for convention violations |

**Check your understanding:** Why can't you compute a fleet-wide p99 by averaging per-instance p99s? What is the cost of a high-cardinality label? When should a value be a span attribute rather than a metric label?

### Chapter 5 · Distributed tracing (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Spans and context | Trace and span IDs; W3C Trace Context propagation over HTTP, gRPC and message queues | Propagate context through an HTTP → Kafka → worker path |
| 5.2 Instrumentation | Auto-instrumentation vs manual spans; useful attributes; span events | Add manual spans around the business-critical steps |
| 5.3 Sampling | Head vs tail sampling; keeping slow and failed traces | Configure tail sampling in the OpenTelemetry Collector |
| 5.4 Debugging with traces | Critical path analysis, fan-out, retries visible in traces | Find a planted N+1 call and a hidden retry loop from traces |

**Check your understanding:** Why does trace context break at queue boundaries unless you carry it explicitly? What does tail sampling cost, and what does it buy? How do retries appear in a trace, and why do they matter?

### Chapter 6 · Debugging production (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Monitoring vs observability | Known questions (dashboards) vs new questions (high-cardinality exploration) | Answer "which customers on which app version are slow?" without a new deploy |
| 6.2 Correlating signals | Metrics → exemplar trace → logs → profile | Solve a planted latency incident using all four signals |
| 6.3 Continuous profiling in incidents | Comparing profiles before and after a deploy | Find a regression's cause from a differential flame graph |
| 6.4 AI in production debugging | Assistants that summarise logs and traces; hallucinated causes; giving agents read-only access | Give an assistant the incident data; grade its hypotheses against the known cause |

**Check your understanding:** Why do dashboards fail on novel incidents? What does an exemplar save you during an incident? What access would you give an AI agent during an incident, and what would you withhold?

### Chapter 7 · Resilience in code (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Deadlines and retries | Deadline propagation, retry budgets, jittered backoff; the missing randomised backoff in Google Cloud's June 2025 recovery | Add deadlines and retry budgets to a 3-service chain |
| 7.2 Circuit breakers and bulkheads | Isolation per dependency; half-open probing | Isolate a slow dependency so other endpoints stay healthy |
| 7.3 Fail open or fail closed | Per-dependency decision (authorisation vs rate limiting vs quotas); Google's remediation to make Service Control fail open | Decide and implement for 5 dependencies; justify each |
| 7.4 Errors that should not crash | Panics, `unwrap()`, unchecked exceptions in hot paths; crash loops; validating limits before applying them (Cloudflare 2025) | Make a service reject a malformed config while continuing on the last good one |

**Check your understanding:** Why can retries turn a small failure into an outage? When is failing open the wrong choice? What should a service do when its new configuration is invalid?

### Chapter 8 · Feature flags and configuration safety (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Flag types | Release, operational kill switch, experiment, permission; OpenFeature as a vendor-neutral API | Add a kill switch and a release flag via OpenFeature |
| 8.2 Flag debt | Stale flags, repurposed flags, dead code; Knight Capital (1 Aug 2012): old unused code triggered by an incomplete deployment sent over 4 million orders in 45 minutes and lost more than $460 million (SEC) | Find and remove stale flags in a codebase; add an expiry check to CI |
| 8.3 Configuration and data pushes | Treat generated config like untrusted input; schema and size limits; staged rollout of global data (Cloudflare and Google 2025; CrowdStrike 2024) | Build a config pipeline with validation, canary and automatic rollback |
| 8.4 Testing flags | Testing both paths; combinatorial risk | Test matrix for 3 interacting flags |

**Check your understanding:** Why did a "content update" cause one of the largest IT outages ever reported? What makes a repurposed flag dangerous? Why must globally replicated data roll out incrementally?

### Chapter 9 · Safe deploys (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Progressive delivery | Canary, blue/green, rings, percentage rollouts; Argo Rollouts or Flagger | Canary a release with automatic promotion on SLO metrics |
| 9.2 Automated canary analysis | Statistical comparison of canary vs baseline (the approach of Netflix's Kayenta) | Detect a planted 2% error-rate regression automatically |
| 9.3 Compatibility | N/N−1 compatibility for APIs, messages and schemas; deploy ordering with database migrations | Ship a breaking field change in three compatible steps |
| 9.4 Rollback vs roll forward | When rollback is impossible (mobile apps, data migrations); rehearsing rollback | Drill a rollback under load; time it |

**Check your understanding:** Why compare a canary against a baseline instead of against yesterday? What makes a deploy impossible to roll back, and how do you plan for it? Why do you need N−1 compatibility even with fast deploys?

### Chapter 10 · Incident response for developers (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 On-call basics | Alert hygiene, actionable pages, runbooks, handovers | Rewrite 10 noisy alerts into actionable ones with runbooks |
| 10.2 Roles and process | Incident commander, operations lead, communications lead, scribe; severity levels | Role-play a SEV-2 with rotating roles |
| 10.3 Mitigate first | Rollback, flag off, shed load, fail over; diagnose after users are safe | Timed drill: restore service before finding the cause |
| 10.4 Communicating | Status updates for customers and executives; cadence; what not to say | Write three status updates for a payment outage |
| 10.5 Game days | Planned failure injection with hypotheses; learning from the gap | Run a game day on your P2 service |

**Check your understanding:** Why should the incident commander usually not be debugging? What is the first action when a deploy correlates with errors? What makes a customer status update trustworthy?

### Chapter 11 · Postmortems and learning (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Blameless postmortems | Contributing factors over a single root cause; "human error" as a starting point | Write a postmortem for your game day |
| 11.2 Action items that matter | Prioritising fixes that change the system, not reminders; tracking to done | Rank 15 action items from public postmortems by risk reduced |
| 11.3 Learning across incidents | Themes across postmortems; limits of averages like MTTR | Analyse 20 public postmortems for recurring themes |
| 11.4 AI-assisted postmortems | Drafting timelines from chat and telemetry; verifying every timestamp | Have an assistant draft a timeline; correct it against logs |

**Check your understanding:** Why does "the engineer made a typo" end learning instead of starting it? Which action item from Cloudflare's or Google's 2025 reports would you implement first in your own system? Why can mean time to recovery mislead?

### Chapter 12 · Operating your own service (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Running under SLOs | Two weeks of operation with SLOs, alerts and on-call rotation | P3 operation period |
| 12.2 Final game day | Unannounced failures injected by the instructor | Respond, mitigate, write the postmortem |
| 12.3 Error-budget decisions | Using budget burn to decide release pace, freezes and reliability work | Write the error-budget policy you would hand to product managers |
| 12.4 Handover | Service ownership transfer: runbooks, dashboards, known risks, open action items | Hand your service to another team; they run one drill using only your docs |

**Check your understanding:** Which alert fired that should not have, and which did not fire that should have? What did your error budget tell you about release pace? What would you change before handing the service to another team?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Postmortem analysis | — |
| 2 | 2 | Lab 2 · SLOs and burn-rate alerts | — |
| 3 | 3 | Lab 3 · Structured and canonical logs | **P1 due** |
| 4 | 4 | Lab 4 · Metrics without cardinality explosions | — |
| 5 | 5 | Lab 5 · Tracing across a queue | — |
| 6 | 6 | Lab 6 · Telemetry-only debugging | Mid-term (AI off): debug from telemetry |
| 7 | 7 | Lab 7 · Resilience and config validation | — |
| 8 | 8 | Lab 8 · Flags and config pipeline | — |
| 9 | 9 | Lab 9 · Canary analysis | **P2 due** |
| 10 | 10 | Incident drills | — |
| 11 | 10 | Game day | Incident report |
| 12 | 11 | Postmortem workshop | Postmortem |
| 13 | 12 | P3 operation | — |
| 14 | 12 | P3 final game day | **P3 due** |
| 15 | Review | Oral defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting instrumentation and OpenTelemetry Collector configs; writing PromQL and log queries; summarising long log streams and traces into hypotheses; drafting status updates and postmortem timelines (then checking every fact); generating failure scenarios for game days.
- **Do without AI (drills):** SLO and alert design; the mid-term telemetry-debugging exam; incident command in drills; the "five whys / contributing factors" analysis; the final. During a real incident you must be able to reason fast with the tools in front of you.
- **Verify AI output by:** running every generated query against known data; checking every timeline entry against logs or chat timestamps; confirming suggested causes with an independent signal (trace, profile, diff); testing generated alert rules with injected faults before trusting them.
- **Where AI still fails here (show it):** in Lab 6 and in the Chapter 11 postmortem workshop an assistant is given the same telemetry as you. You grade its hypotheses against the planted cause and record (a) confident wrong causes, (b) correlation mistaken for causation (a deploy that coincided but did not cause), (c) invented log lines or metrics, and (d) timeline errors. Remember that operations is where developers use AI least (20% in the 2026 Stack Overflow survey); your log shows why.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (9) and drills | 20% |
| P1, P2, P3 | 10%, 15%, 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence | 20% |

**Mastery gate.** You pass when you can: (1) with AI off, find the cause of a planted production problem in an unfamiliar 4-service system within 45 minutes using only its traces, logs, metrics and profiles; (2) instrument a service to an agreed SLO with burn-rate alerts that fire on injected faults and stay silent on noise over a 48-hour run; (3) act as incident commander in an unannounced game day, restore service within the agreed time, and deliver a blameless postmortem within 48 hours whose action items a reviewer accepts.

## Industry reality

Where this is used (public sources): Google's SRE books (free) define SLOs, error budgets and burn-rate alerting. Public postmortems from Cloudflare (Nov 2025), Google Cloud (Jun 2025) and AWS (Oct 2025) list developer-level remediations: validate internal configuration like user input, feature-flag critical code paths, add randomised backoff, roll out globally replicated data incrementally. OpenTelemetry is the CNCF project for vendor-neutral traces, metrics and logs; OpenFeature is a CNCF project that defines a vendor-neutral feature-flag API. Stripe described canonical log lines as one wide structured event per request.

**Interview questions from this course**

1. *How would you define SLOs for a checkout service?* Strong answer: user-centric SLIs (successful checkouts, latency at the edge), targets tied to business impact, windows, error budget policy, burn-rate alerts, dependency SLOs, what is excluded.
2. *Latency is up for 5% of users. How do you find out why?* Strong answer: slice by high-cardinality attributes (region, app version, customer, endpoint), follow exemplars to traces, check recent deploys and config pushes, compare profiles, confirm with an independent signal.
3. *Walk me through what you do in the first 15 minutes of an incident.* Strong answer: acknowledge, assess impact, declare severity and roles, mitigate first (roll back, disable flag, shed load), communicate on a cadence, keep a timeline.
4. *What can go wrong with feature flags?* Strong answer: stale and repurposed flags (Knight Capital), untested combinations, flag service as a dependency, configuration pushes without validation or staging; mitigations: expiry, ownership, testing both paths, kill switches with safe defaults.
5. *Tell me about a postmortem you wrote.* Strong answer: blameless framing, timeline, contributing factors at several levels (code, process, tooling), action items that change the system, follow-through evidence.

## Resources (free first)

- **Books (free):** Google, *Site Reliability Engineering* — https://sre.google/sre-book/table-of-contents/ ; *The Site Reliability Workbook* — https://sre.google/workbook/table-of-contents/
- **Standards and tools:** OpenTelemetry — https://opentelemetry.io/docs/ ; W3C Trace Context — https://www.w3.org/TR/trace-context/ ; OpenFeature — https://openfeature.dev/ ; Prometheus instrumentation practices — https://prometheus.io/docs/practices/instrumentation/ ; Argo Rollouts — https://argoproj.github.io/rollouts/ ; Grafana Tempo, Loki and Pyroscope — https://grafana.com/oss/
- **Practices:** Stripe, "Fast and flexible observability with canonical log lines" — https://stripe.com/blog/canonical-log-lines ; PagerDuty Incident Response documentation — https://response.pagerduty.com/ ; Learning from Incidents — https://www.learningfromincidents.io/
- **Postmortem collections:** Dan Luu's list — https://github.com/danluu/post-mortems ; Cloudflare blog postmortems — https://blog.cloudflare.com/tag/post-mortem/ ; Google Cloud status history — https://status.cloud.google.com/summary
- **Paid, optional:** Majors, Fong-Jones and Miranda, *Observability Engineering*; Nygard, *Release It!* (2nd ed.).

## Sources

- Google, *Site Reliability Engineering*, Introduction ("roughly 70% of outages are due to changes in a live system") — https://sre.google/sre-book/introduction/ (checked 2026-10)
- Google Cloud, incident report for 12 Jun 2025 (Service Control) — https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW (checked 2026-10)
- Cloudflare, "Cloudflare outage on November 18, 2025" — https://blog.cloudflare.com/18-november-2025-outage/ (checked 2026-10)
- AWS, summary of the 19–20 Oct 2025 us-east-1 disruption — https://aws.amazon.com/message/101925/ (checked 2026-10)
- Microsoft, "Helping our customers through the CrowdStrike outage" (20 Jul 2024; ~8.5 million devices) — https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/ (checked 2026-10)
- US SEC press release 2013-222, Knight Capital (16 Oct 2013) — https://www.sec.gov/news/press-release/2013-222 (checked 2026-10)
- Stack Overflow blog, 2026 survey results (6 Oct 2026) — https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/ ; DORA 2025 announcement — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report (checked 2026-10)

_Last reviewed: 2026-10_
