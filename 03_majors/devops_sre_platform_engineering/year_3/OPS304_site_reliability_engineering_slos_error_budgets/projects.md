# OPS304 · Labs and projects

The lab environment is the stack you built in [OPS303](../OPS303_observability_metrics_logs_traces/README.md) (Prometheus, Grafana, Alertmanager, Loki and Tempo on kind), plus Sloth or Pyrra for SLO rules and a chat tool (Mattermost, Slack free tier or Discord) for paging and incident channels. Labs 1, 7 and 8 are done without AI assistance. Incident simulations need at least three students: an incident commander, a responder and a "game master" who injects faults.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Availability arithmetic | Compute downtime budgets, serial/parallel dependency ceilings and the effect of correlated failures for a 6-dependency service | Worked sheet; one proposal to raise the ceiling | 3 h |
| 2 · SLIs three ways | Measure checkout success from service metrics, ingress logs and a synthetic probe for one week of load | Three SLI series, differences explained | 4 h |
| 3 · SLOs and policy | Set SLOs from 30 days of (synthetic) history; write an error budget policy; role-play sign-off with a "product manager" | SLO document, policy, decision log | 4 h |
| 4 · Burn-rate alerts | Generate multiwindow, multi-burn-rate rules with Sloth or Pyrra; unit-test them for 14.4×, 6× and 1× burns and for a low-traffic service | OpenSLO/Sloth YAML, generated rules, passing `promtool` tests | 5 h |
| 5 · Toil audit | Classify 100 tickets or tasks (provided or your own), estimate hours, eliminate the biggest source | Toil report with before/after hours | 4 h |
| 6 · Rotation and runbooks | Design a two-site rotation; write 5 runbooks; have a classmate execute each cold | Policy, runbooks, execution notes and fixes | 4 h |
| 7 · Incident command tabletop | Three 30-minute tabletops with rotating roles (IC, ops, comms, scribe) | Scribe logs, three status updates per incident, self-assessment | 4 h |
| 8 · Post-mortem rewrite | Rewrite a blame-laden post-mortem (provided) into a blameless one with contributing factors and closable actions | Rewritten post-mortem, list of changes and why | 3 h |
| 9 · PRR and restore timing | Run a production readiness review on a classmate's service; time a database restore against its stated RTO | PRR findings, restore timing | 4 h |
| 10 · AI post-mortem audit | Give an AI tool the raw channel and telemetry of one simulated incident; compare its timeline and causes with yours | Line-by-line comparison, omission and error log | 3 h |

## Projects

### P1 · SLOs for a real-shaped service (L1, ~6 hours)

**Real-world inspiration:** the SRE workbook's [Implementing SLOs](https://sre.google/workbook/implementing-slos/) and [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) chapters, which most SLO tools implement directly.

**What to build:** for one service of the OpenTelemetry Demo (for example checkout), define two critical user journeys, three SLIs, SLOs, an error budget policy, burn-rate alerts and an SLO dashboard showing budget remaining.

**Acceptance criteria:**
- **Specification:** each SLI has a written specification and an implementation (exact query), with exclusions justified.
- **Fast burn:** a fault producing a 14.4× burn pages within 5 minutes, verified by injecting it three times.
- **No noise:** a 1× burn sustained for one hour produces no page (ticket only), and a 3-minute blip produces nothing.
- **Tests:** all alert rules pass `promtool` unit tests, including counter resets.
- **Policy:** the error budget policy names who decides, what happens at 50% and 100% spent, and how exceptions work.

**Stretch goals:** a latency SLI computed from native histograms; an SLO for a batch pipeline (freshness).

**What it proves to an employer:** you can turn "make it reliable" into numbers, alerts and decisions, which is the first deliverable of any SRE hire.

### P2 · On-call in a box (L2, ~15 hours)

**Real-world inspiration:** PagerDuty's public [incident response documentation](https://response.pagerduty.com/) and the SRE book's [Being On-Call](https://sre.google/sre-book/being-on-call/) limits (no more than 25% of time on call; at most 2 incidents per 12-hour shift).

**What to build:** a complete on-call system for a team of four:
- a rotation with escalation;
- alerts routed from Alertmanager to a chat channel and a phone notification;
- runbooks linked from every alert;
- an incident bot or slash-command workflow that opens an incident channel, assigns roles and starts a timeline;
- a status page;
- a post-mortem template.

Run a one-week simulated rotation in which a game master injects at least 8 faults at unannounced times (within agreed hours).

**Acceptance criteria:**
- **Actionability:** at least 90% of pages during the week are actionable (each logged with "action taken").
- **Response:** median time to acknowledge under 5 minutes and median time to mitigate under 30 minutes, from bot timestamps.
- **Communication:** every incident has at least three timestamped status updates and a closing summary.
- **Learning:** every incident of severity 2 or above has a blameless post-mortem within 48 hours, and at least 3 action items are completed and verified by the end of the project.
- **Load:** a page-load report shows no responder exceeded 2 incidents in a 12-hour shift, or explains and fixes why.

**Stretch goals:** follow-the-sun handoff between two time zones; automatic CERT-In-style reporting checklist triggered for security-tagged incidents.

**What it proves to an employer:** you can build and run the human system around production, not only the technical one.

### P3 · Reliability engagement for a payment-style system (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** UPI's March–May 2025 outages, which NPCI linked to payment service provider banks sending repeated "check transaction status" requests at high speed. NPCI responded with a 90-second minimum before status checks, caps on balance enquiries and peak-hour limits for system-initiated calls ([MediaNama, May 2025](https://www.medianama.com/2025/05/223-npci-banks-balance-upi-transaction-guidelines/)). The system you build is an *illustrative scenario*. It does not reproduce NPCI's or any bank's real architecture.

**What to build:** a simulated payment flow: a payer app API, a "switch" service, two bank simulators and a status-check API. The bank simulators can be made slow or partially failing. Then act as the SRE team for it:
- critical user journeys, SLIs, SLOs and an error budget policy;
- burn-rate alerting, runbooks and an on-call rotation (reuse P2);
- client-side controls inspired by the circular: a minimum delay before status checks, retry budgets with jittered backoff, and peak-hour throttling of non-customer-initiated calls;
- a game day with four scenarios: slow bank, bad deploy of the switch, retry storm from a misbehaving client, zone loss;
- a post-mortem written to public-blog quality for the worst scenario.

**Acceptance criteria:**
- **SLOs held:** during a 7-day soak with scheduled faults, the payment-success SLO (for example 99.9% over 7 days, scaled from your 28-day policy) is met, or the error budget policy is visibly applied, with decisions logged.
- **Retry storm:** with the controls on, a client misbehaving like the 2025 pattern amplifies load on the switch by no more than 1.2× (measured), compared with at least 5× with controls off.
- **Recovery:** in the bad-deploy scenario, recovery time is under 15 minutes; in the zone-loss scenario, the system stays within its latency SLO with planned headroom.
- **Command:** each game-day scenario has a named IC, a timeline and three status updates; two observers score the command at least "competent" on a published rubric.
- **Learning:** the post-mortem is blameless, has at least 3 contributing factors and closable actions, and one action is implemented and re-tested before hand-in.

**Stretch goals:** an error-budget-aware deploy gate (from [OPS301](../OPS301_ci_cd_engineering/README.md)) that pauses releases when the 6-hour burn exceeds 6×; a capacity plan for a festival-day peak.

**What it proves to an employer:** you can own the reliability of a critical service end to end (targets, alerts, people, incidents and learning), using a failure pattern from a real Indian system.

## Feeds into

- [OPS402 Chaos Engineering and Resilience](../../year_4/OPS402_chaos_engineering_and_resilience/README.md): game days become continuous experiments.
- [OPS404 Performance and Capacity Engineering](../../year_4/OPS404_performance_and_capacity_engineering/README.md): Chapter 10's capacity basics are developed into full models.
- [OPS403 AIOps and Agentic Operations](../../year_4/OPS403_aiops_and_agentic_operations/README.md): your incident data trains and tests AI assistants.
- [OV10A Payment Systems Engineering](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10A_payment_systems_engineering_upi_cards/README.md): P3 is a natural bridge to the FinTech overlap.
- [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): incident-scenario interview practice.
