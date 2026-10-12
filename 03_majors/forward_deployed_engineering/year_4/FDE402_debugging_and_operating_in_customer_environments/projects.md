# FDE402 · Labs and projects

All labs run in replica environments you build or the course provides: local virtual machines or Kubernetes clusters, an intercepting proxy, an identity provider (Keycloak), and a network with egress blocked. Packet captures and debugging tools are used only on systems you own or have written permission to test. Every project includes a debugging log (observation, hypothesis, test, result) and redacted artefacts.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Environment survey and change request | Survey an illustrative state-government department's environment from a written brief and interviews; write a change request for a configuration fix | Survey, constraints list, change request | 3 h |
| 2 · Layer-by-layer network faults | Diagnose five planted faults (DNS, TCP, TLS, HTTP, MTU) with dig, nc, curl, openssl and traceroute | Debugging log per fault, evidence pack for a network team | 4 h |
| 3 · Proxy and TLS interception | Make Python, Node, Java and a container runtime work through an authenticated, TLS-intercepting proxy without disabling verification | Configuration per runtime, trust-store notes, test script | 5 h |
| 4 · Identity failures | Diagnose seven planted SAML and OIDC faults (clock skew, rotated certificates, audience, JWKS caching, redirect URI, group overflow) | Diagnoses with traces, fixes, alerting for expiring credentials | 5 h |
| 5 · Air-gapped Kubernetes | Package an application (images, charts, dependencies) for offline transfer with Zarf or an equivalent; generate SBOMs and signatures; deploy, verify, upgrade with a migration, roll back | Bundle, SBOM, verification log, upgrade and rollback evidence | 8 h |
| 6 · On-premises model serving | Serve an open-weight model offline with vLLM or Ollama; load-test; run an eval suite offline and compare with a hosted model | Throughput and latency results, sizing note, quality gap | 5 h |
| 7 · Logs, redaction and support bundle | Structured logs with correlation IDs and error codes; tested redaction; a support-bundle command; a diagnostic CLI | Code, redaction tests, sample bundle | 5 h |
| 8 · Debugging by email | Fix a fault in a classmate's replica only by sending commands with expected outputs | Email thread, number of round trips, reflection | 3 h |
| 9 · Incident simulation and postmortem | 60-minute simulated Sev-1 with roles and 30-minute updates; CERT-In reporting step; blameless postmortem presented to the "customer" | Timeline, updates, postmortem | 5 h |
| 10 · Game day | Inject three failures with another team acting as customer operators; measure time to detect and recover | Game-day plan, measurements, runbook fixes | 4 h |
| 11 · Reverse shadow and handover | The support team (classmates) operates your system for three days while you observe; test handover criteria | Handover criteria, results, known-issues list | 4 h |
| 12 · AI triage evaluation | Give an assistant redacted support bundles from ten known faults; score its hypotheses and proposed commands | Scoring table, unsafe suggestions, operations-agent permission policy | 3 h |

## Projects

### P1 · A diagnostic toolkit for restricted networks (L1, ~6 hours)

**Real-world inspiration.** Customer-site work includes "monitoring, debugging, deploying, or configuring our software" (Palantir Delta, 2019); enterprises commonly route traffic through intercepting proxies with private certificate authorities (analysis).

**What to build.** A command-line diagnostic tool that a customer's engineer can run to check everything your application needs: DNS resolution, proxy settings per runtime, TLS chain and trust store, egress to each required endpoint, IdP metadata reachability, database connectivity and clock offset. Output is human-readable and pasteable, with a redacted JSON form.

**Acceptance criteria**
- Detects every fault in Lab 2 and Lab 3 replicas, with a clear message naming the failing layer.
- Runs without internet access and without admin rights.
- Never prints secrets; redaction is covered by tests.
- A classmate unfamiliar with it uses it to find a planted fault in under 15 minutes.

**Stretch goals.** Produce an egress allowlist request automatically from your application's configuration.

**What it proves to an employer.** You shorten customer incidents by making problems visible to the people who can fix them.

### P2 · Air-gapped delivery of an AI application (L2, ~15 hours)

**Real-world inspiration.** Palantir's Apollo documentation describes autonomous deployment across "connected and disconnected, air-gapped environments" with controls for FedRAMP, IL5 and IL6; open-source tools such as Zarf package software for air-gapped Kubernetes.

**What to build.** Deliver your FDE304 application (or a provided retrieval assistant) into an air-gapped replica for an illustrative defence-sector public undertaking: offline bundle including an open-weight model served by vLLM or Ollama, SBOMs, signed images, offline licence check, structured logging with support bundles, and a documented upgrade with a data migration and a rollback.

**Acceptance criteria**
- Fresh install in the disconnected cluster completes from the bundle alone; no network calls leave the cluster (verified with egress logs).
- Signature verification and SBOM checks run inside the environment and block a tampered image.
- Offline eval shows the on-premises model's quality against the hosted baseline on at least 100 cases, with a go/no-go note.
- Upgrade and rollback each complete within a stated window with no data loss.
- An operator guide that a classmate follows to install and upgrade without help.

**Stretch goals.** Add an environment-constraints file (maintenance windows, minimum versions) that your upgrade script respects.

**What it proves to an employer.** You can deliver to the customers with the hardest constraints, which many vendors cannot serve.

### P3 · Operate, break and hand over a customer deployment (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Google's SRE practices for incident management and blameless postmortems; CERT-In's 2022 directions on incident reporting within six hours and 180-day log retention in India; Razorpay's FDE expectation that merchant issues are acknowledged within two hours (2026).

**What to build.** Operate a deployment for an illustrative private hospital chain in Hyderabad (your FDE304 P3 system or a provided one) in an on-premises replica for three weeks with a classmate team acting as the hospital's IT department and support desk. Build observability without direct access, write runbooks for the top failures, run two game days and one surprise incident injected by the instructor, and complete a handover to the hospital's support team with measurable criteria.

**Acceptance criteria**
- Time to detect and time to recover measured for every injected failure; the second game day shows improvement over the first.
- The surprise incident is run with roles, a fixed update cadence, the reporting step and a published blameless postmortem with owned action items.
- Runbooks cover at least five failure modes, each executed successfully by the support team.
- Handover criteria met: the support team resolves at least three tickets without you and executes one upgrade.
- An AI triage evaluation on the incidents shows its hit rate and every unsafe suggestion it made.

**Stretch goals.** Automate two runbooks with approval gates and show reduced recovery time.

**What it proves to an employer.** You can keep a customer's system running, lead them through failure, and leave them self-sufficient.

## Feeds into

- [FDE404 Field Studio](../FDE404_field_studio_three_simulated_customer/README.md): every simulated deployment includes an operations and handover phase.
- [OV12 Agent Infrastructure and Platform Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/): operating agents in production.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): incident data and AI-triage evaluations make good capstone studies.
