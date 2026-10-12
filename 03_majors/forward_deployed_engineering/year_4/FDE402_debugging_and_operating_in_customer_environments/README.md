# FDE402 · Debugging and Operating in Customer Environments

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [FDE302](../../year_3/FDE302_customer_discovery_and_requirements_engineering/README.md); assumes [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md), [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [FDE303](../../year_3/FDE303_rapid_integration_engineering_apis_legacy/README.md); [OPS303](../../../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md) recommended | [FDE404](../FDE404_field_studio_three_simulated_customer/README.md), [OV12](../../../../04_overlaps/OV12_agent_infrastructure_platform/), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

## Why this course matters now

Your software works on your laptop and in your cloud. At the customer it sits behind a proxy that rewrites TLS certificates, inside a network with no internet access, on a Kubernetes distribution you have never used, logged in through an identity provider configured by someone who left last year, and you may not be allowed to see the logs. A Palantir Delta describes spending customer-site days "monitoring, debugging, deploying, or configuring our software for that customer" (2019). Palantir built Apollo to deliver software across "connected and disconnected, air-gapped environments" with controls required for accreditation frameworks such as FedRAMP, IL5 and IL6; OpenAI now hires forward deployed engineers for government and a Forward Deployed Security Engineer. AI helps here: assistants read stack traces, summarise thousands of log lines and propose likely causes; Razorpay's FDE posting mentions agents for incident triage. But only 20% of developers who use AI use it for "deploying, operating, or troubleshooting production systems" (Stack Overflow 2026), and an assistant that confidently names the wrong root cause during a customer's outage costs hours and trust. This course teaches you to deploy into environments you do not control, debug with incomplete access, run incidents with customers, and hand a system over so that it keeps running without you.

## Learning outcomes

By the end you can:

1. **Survey** a customer environment in the first days (network, identity, platform, change process, access rules) and **record** its constraints.
2. **Diagnose** network failures caused by proxies, TLS interception, DNS, firewalls and MTU, using curl, openssl, dig, traceroute and packet captures (with permission).
3. **Diagnose** identity failures (SAML and OIDC misconfiguration, clock skew, certificate rotation, group claims, conditional access).
4. **Package** and **deploy** software into air-gapped or on-premises Kubernetes with offline registries, SBOMs, signatures and repeatable upgrades.
5. **Run** AI workloads on premises (open-weight models on vLLM or Ollama), with offline evaluation and capacity checks.
6. **Design** observability that works without direct access: structured logs with correlation IDs, redaction, support bundles and health endpoints.
7. **Lead** an incident with a customer: severity, roles, communication cadence, regulatory reporting (CERT-In six-hour rule in India) and a blameless postmortem.
8. **Write** runbooks and **complete** a support handover with measurable acceptance criteria.
9. **Use** AI for diagnosis safely: read-only scopes, redacted inputs, and hypotheses tested before acting.

## Chapters and lessons

### Chapter 1 · The environment you do not control (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Environment survey | Network zones, egress rules, proxies, DNS, identity provider, platform (VMs, Kubernetes, OpenShift), OS images, change windows, approval boards | Fill an environment survey for an illustrative state-government department |
| 1.2 Access models | Your laptop, the customer's laptop, virtual desktops, jump hosts, screen-share only; what you can and cannot run | Plan debugging for each access model |
| 1.3 Change control | Change advisory boards, maintenance windows, emergency changes; why a one-line fix can take two weeks | Write a change request for a configuration fix |
| 1.4 First-day checklist | Accounts, VPN, test credentials, contacts, escalation paths, where logs go | Build a reusable first-day checklist |

**Check your understanding:** Why should the environment survey happen before the first deployment? What can you debug if you only have screen-share access? Why do change windows shape your release plan?

### Chapter 2 · Network debugging (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Layer by layer | DNS → TCP → TLS → HTTP; tools at each layer (dig, nc, curl -v, openssl s_client) | Diagnose five planted failures in a lab network, one per layer |
| 2.2 Corporate proxies | Explicit proxies, PAC files, `HTTP(S)_PROXY` and `NO_PROXY`, proxy authentication, tools that ignore proxy settings | Make Python, Node and a container runtime all work through an authenticated proxy |
| 2.3 TLS interception | Corporate root CAs, certificate chains, trust stores per runtime (OS, Java, Python certifi, Node) | Fix "certificate verify failed" behind an intercepting proxy without disabling verification |
| 2.4 Firewalls and allowlists | Egress allowlists by domain or IP, what a vendor endpoint list must contain, timeouts that look like bugs | Write a precise egress allowlist request for your application |
| 2.5 Odd failures | Split-horizon DNS, MTU and fragmentation, idle-connection timeouts, IPv6 surprises | Reproduce an idle-timeout failure and fix it with keepalives |
| 2.6 Packet captures | tcpdump and Wireshark with written permission; reading a TLS handshake | Capture and annotate a failing handshake in your lab |

**Check your understanding:** Why is setting `verify=False` never the fix? How do you tell a firewall drop from a slow server? What evidence do you bring to the customer's network team?

### Chapter 3 · Identity in the wild (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 SAML failures | Clock skew, expired or rotated signing certificates, wrong audience or ACS URL, NameID format changes | Diagnose four planted SAML failures from logs and browser traces |
| 3.2 OIDC failures | Issuer mismatch, key rotation (JWKS caching), redirect URI rules, token size limits | Diagnose three planted OIDC failures |
| 3.3 Group and policy surprises | Group claim overflow, nested groups, conditional access and device policies | Handle a user in 400 groups without breaking login |
| 3.4 Service identities | Expired service-account passwords, certificate-based auth, secrets rotated by the customer | Design alerting for credentials that expire |

**Check your understanding:** Why do SAML failures cluster around certificate rotation dates? What should your app do when the IdP's signing key changes? Who at the customer owns each identity failure?

### Chapter 4 · On-premises and air-gapped deployment (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Why customers run disconnected | Defence, government, critical infrastructure, regulated finance; accreditation | Classify five illustrative customers by connectivity and accreditation needs |
| 4.2 Packaging | Container images and Helm charts bundled for offline transfer; offline package mirrors; Zarf for declarative air-gapped packages | Build an offline bundle and deploy it into a Kubernetes cluster with no internet |
| 4.3 Supply-chain evidence | SBOMs (CycloneDX, SPDX), image signing and verification (Sigstore cosign), vulnerability scans the customer will run | Produce an SBOM and signatures; verify them inside the air-gapped cluster |
| 4.4 Upgrades and constraints | Repeatable upgrades, schema migrations, rollback; Apollo's model of product constraints plus environment constraints (for example, when changes are allowed) | Run an upgrade with a migration and a rollback; document environment constraints |
| 4.5 Licences and telemetry | Licence keys offline, opt-in telemetry, what you can learn without phoning home | Design an offline licence check and a manual telemetry export |

**Check your understanding:** What breaks first when a deployment has no internet? Why do customers ask for SBOMs, and what do they do with them? How do you ship a security patch to a site you cannot reach?

### Chapter 5 · AI on premises (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Serving open-weight models | vLLM and Ollama; GPU drivers and memory; quantisation trade-offs | Serve an open-weight model offline and measure tokens per second |
| 5.2 Moving models | Weight files, checksums, licences, transfer approvals | Package model weights with checksums and a licence note |
| 5.3 Capacity | Concurrency, context length, latency budgets; sizing from measured load | Load-test your model server and write a sizing note |
| 5.4 Offline evaluation | Running the eval suite inside the environment; comparing with the hosted model | Run an FDE304-style eval offline; report the quality gap |

**Check your understanding:** Why does a model that fits in GPU memory still fail under concurrent load? What do you check before carrying model weights into a secure site? How do you decide whether an on-premises model is good enough?

### Chapter 6 · Observability without access (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Logs designed for strangers | Structured logs, correlation IDs, error codes customers can read out over the phone | Retrofit structured logging and error codes into a service |
| 6.2 Redaction | Never logging secrets or personal data; tested redaction | Add redaction and prove it with tests on seeded sensitive values |
| 6.3 Support bundles | Collecting logs, configs and health checks into one archive the customer can review before sending (troubleshoot.sh pattern) | Build a support-bundle command with a redaction step |
| 6.4 Local telemetry | OpenTelemetry collectors exporting to the customer's own tools or to files | Configure a collector that exports traces locally |
| 6.5 Health and diagnostics | Health endpoints, self-tests, a diagnostic CLI that checks DNS, proxy, IdP and database reachability | Write a diagnostic command that catches the Chapter 2 failures |

**Check your understanding:** Why should error codes be designed for phone conversations? What must a support bundle never contain? How does a diagnostic self-test shorten an incident?

### Chapter 7 · Remote debugging discipline (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Hypothesis-driven debugging | Observations, hypotheses, tests that distinguish them; avoiding random changes | Keep a debugging log for a planted fault and solve it in the fewest steps |
| 7.2 Debugging through others | Writing exact commands with expected outputs for a customer engineer to run | Solve a fault by email only, through a classmate who runs your commands |
| 7.3 Reproduction | Building a local replica of the customer environment (proxy, IdP, OS image) | Reproduce a customer-only bug in a lab replica |
| 7.4 Bisecting | Configuration and version bisection; differences between working and failing sites | Find the breaking config change by bisection |

**Check your understanding:** Why do random changes make outages longer? What makes a command safe to send to a customer? When is building a replica worth the time?

### Chapter 8 · Incidents with customers (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Severity and roles | Severity definitions tied to impact; incident commander, communications lead, subject experts (Google SRE incident management; PagerDuty incident response guide) | Write severity definitions and role cards for a deployment |
| 8.2 Communication cadence | Status updates on a fixed schedule; what is known, unknown and next; customer and internal channels | Run a simulated incident with updates every 30 minutes |
| 8.3 Regulatory reporting | India's CERT-In directions (2022): report cyber incidents within six hours and keep system logs for 180 days within India; contract notification clauses | Add reporting steps and log retention to the incident runbook |
| 8.4 Mitigation first | Rollback, feature flags, failover, manual workarounds before root cause | Mitigate a simulated outage before diagnosing it |
| 8.5 Postmortems | Blameless postmortems, timelines, contributing factors, action items with owners (SRE workbook) | Write a postmortem for the simulated incident and present it to the "customer" |

**Check your understanding:** Why mitigate before finding the root cause? What should a status update contain when you know nothing new? How does a six-hour reporting rule change the first hour of an incident?

### Chapter 9 · Runbooks and game days (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Runbook structure | Trigger, checks, steps with expected output, verification, rollback, escalation | Write runbooks for the five most likely failures of your system |
| 9.2 Automating runbooks | Scripts for repeatable steps; keeping humans on decisions | Automate two runbook steps with safety checks |
| 9.3 Game days | Injecting failures with the customer's team; measuring time to detect and recover | Run a game day; record detection and recovery times |
| 9.4 Keeping runbooks true | Testing runbooks after every change; ownership | Add a runbook test to your release checklist |

**Check your understanding:** What makes a runbook step verifiable? Why run game days with the customer's team rather than your own? How do runbooks go stale?

### Chapter 10 · Support handover (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Support tiers | L1 (triage), L2 (configuration and known issues), L3 (engineering); who owns what at the customer and the vendor | Draw the support model for your deployment |
| 10.2 Knowledge transfer | Shadowing, reverse shadowing, known-issues database, recorded walkthroughs | Run a reverse-shadow session where the support team operates and you observe |
| 10.3 Acceptance criteria | Measurable handover criteria: tickets resolved without you, runbooks executed, on-call readiness | Define and test handover criteria |
| 10.4 Service levels | Response and resolution targets; Razorpay's FDE posting asks for acknowledgement of merchant issues within two hours | Draft service levels and check them against your on-call capacity |

**Check your understanding:** Why does handover fail when it is a single meeting? What evidence shows a support team is ready? Who should own a recurring issue after handover?

### Chapter 11 · AI for operations, safely (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 AI-assisted triage | Summarising logs and traces, clustering errors, suggesting hypotheses | Use an assistant on a redacted support bundle; score its hypotheses against the known cause |
| 11.2 Guardrails for operations agents | Read-only scopes, approval for any change, audit logs, no customer data in unapproved tools | Write the permission policy for an operations agent in a customer environment |
| 11.3 Failure modes | Confident wrong root causes, hallucinated commands, actions on the wrong environment | Collect three AI diagnosis failures from your labs with evidence |
| 11.4 Measuring AI triage | Hypothesis hit rate, time to correct diagnosis with and without AI, rate of unsafe suggestions | Time the diagnosis of five faults with and without an assistant; report both and the unsafe-suggestion count |

**Check your understanding:** Why must AI-suggested commands be read before they run? What data can you give an assistant from a customer's logs? How do you measure whether AI triage helped?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Environment survey and change request | — |
| 2 | 2 | Lab 2 · Layer-by-layer network faults | — |
| 3 | 2 | Lab 3 · Proxy and TLS interception | **P1 due** |
| 4 | 3 | Lab 4 · Identity failures | — |
| 5 | 4 | Lab 5 · Air-gapped Kubernetes deployment | — |
| 6 | 4 | Lab 5 (cont.): SBOM, signing and upgrade | — |
| 7 | 5 | Lab 6 · On-premises model serving | Mid-term (AI off): live diagnosis |
| 8 | 6 | Lab 7 · Logs, redaction and support bundle | — |
| 9 | 7 | Lab 8 · Debugging by email | **P2 due** |
| 10 | 8 | Lab 9 · Incident simulation | — |
| 11 | 8 | Lab 9 (cont.): postmortem | Postmortem |
| 12 | 9 | Lab 10 · Game day | — |
| 13 | 10 | Lab 11 · Reverse shadow and handover | — |
| 14 | 11 | Lab 12 · AI triage evaluation | **P3 due** |
| 15 | Review | Timed fault-finding exam; P3 defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar error messages and configuration formats, summarising redacted logs, drafting runbooks from your notes, generating Helm and Zarf configuration for you to review, writing diagnostic scripts.
- **Do without AI (drills):** the mid-term live diagnosis; network and identity fault labs (first attempt); incident command in simulations; the final timed fault-finding exam. At a customer site you may have no AI tools at all.
- **Verify AI output by:** testing every proposed hypothesis with a distinguishing check before acting; running AI-written commands in your replica first; reviewing generated manifests against the customer's policies; scoring AI triage against known causes.
- **Where AI still fails here (show it):** in Lab 12, record wrong root causes stated with confidence, commands that would change production when only a read was needed, and advice to disable TLS verification. Report how many AI hypotheses were correct.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (12) | 30% |
| Projects P1–P3 | 35% |
| Postmortem and runbooks | 5% |
| Mid-term (AI off) | 10% |
| Final timed fault-finding exam (AI off) + P3 defence | 20% |

**Mastery gate.** You pass when you can: (1) find and fix four planted faults (one each in network, TLS, identity and deployment) in an unfamiliar replica environment within three hours, AI off, with a written debugging log; (2) deploy and upgrade a packaged application in an air-gapped cluster with verified signatures and an SBOM; (3) lead a 60-minute simulated incident with a customer, meeting the communication cadence and the reporting step, and deliver a blameless postmortem.

## Industry reality

Palantir documents Apollo as its system for deploying to cloud, on-premises and air-gapped environments under accreditation frameworks; open-source tools such as Zarf exist for air-gapped delivery. Government and defence deployments are an explicit hiring area (OpenAI's forward deployed roles for government). In India, CERT-In's 2022 directions set incident reporting and log retention duties for service providers and organisations. Support-bundle tooling, SBOM requirements and signed artefacts are now common in enterprise procurement. Operating production systems remains one of the least AI-automated parts of software work (Stack Overflow 2026).

**Interview questions from this course**

1. *Your app cannot reach its API from the customer's network. Debug it.* Strong answer: layer by layer (DNS, TCP, TLS, HTTP); checks proxy settings per runtime, TLS interception and trust stores, egress allowlists; gathers evidence for the network team; never disables verification.
2. *How do you deploy to a customer with no internet access?* Strong answer: offline bundle of images, charts and dependencies; SBOM and signatures; verification inside; upgrade and rollback plan; licence and telemetry without phoning home; documentation for the customer's operators.
3. *You cannot see the customer's logs. How do you debug?* Strong answer: structured logs with correlation IDs and error codes; redacted support bundles reviewed by the customer; diagnostic commands with expected output; hypothesis-driven steps; a local replica.
4. *Walk me through the first hour of a Sev-1 at a customer.* Strong answer: declare severity, assign roles, open channels, status cadence, mitigate first (rollback, flag, failover), regulatory and contractual notification checks, then root cause; postmortem later.
5. *How do you hand a deployment over to the customer's support team?* Strong answer: support tiers, runbooks tested by them, reverse shadowing, known-issues list, measurable acceptance criteria, service levels, an escalation path to engineering.

## Resources (free first)

- **Incidents and reliability:** Google SRE book, "Managing Incidents" — https://sre.google/sre-book/managing-incidents/ ; SRE workbook, "Postmortem Culture" — https://sre.google/workbook/postmortem-culture/ ; PagerDuty incident response guide — https://response.pagerduty.com/ ; Atlassian incident management handbook — https://www.atlassian.com/incident-management/handbook
- **Air-gapped and on-premises delivery:** Palantir Apollo documentation — https://www.palantir.com/docs/apollo/core/introduction/ ; Zarf — https://docs.zarf.dev/ ; Replicated troubleshoot (support bundles) — https://troubleshoot.sh/ ; Kubernetes documentation — https://kubernetes.io/docs/home/
- **Supply chain:** CycloneDX — https://cyclonedx.org/ ; SPDX — https://spdx.dev/ ; Sigstore — https://www.sigstore.dev/ ; CISA SBOM resources — https://www.cisa.gov/sbom
- **Observability:** OpenTelemetry — https://opentelemetry.io/
- **Network and identity tools:** Wireshark — https://www.wireshark.org/ ; mitmproxy — https://mitmproxy.org/ ; jwt.io (decode tokens from test environments only) — https://jwt.io/ ; Keycloak — https://www.keycloak.org/
- **On-premises AI:** vLLM — https://docs.vllm.ai/en/latest/ ; Ollama — https://ollama.com/
- **India:** CERT-In directions under section 70B(6) (28 Apr 2022) and FAQs — https://www.cert-in.org.in/Directions70B.jsp

## Sources

- Palantir, "Dev versus Delta" (8 Apr 2019) — https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87 (checked 2026-10)
- Palantir Apollo documentation, introduction — https://www.palantir.com/docs/apollo/core/introduction/ (checked 2026-10)
- OpenAI careers search "forward deployed" (12 Oct 2026; government and security FDE roles) — https://openai.com/careers/search/?q=forward%20deployed (checked 2026-10)
- Razorpay, Forward Deployed Engineer (Aug 2026) — https://portfoliojobs.tcv.com/companies/razorpay/jobs/89918935-forward-deployed-engineer (checked 2026-10)
- Stack Overflow, 2026 survey results blog (6 Oct 2026) — https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/ (checked 2026-10)
- CERT-In directions (28 Apr 2022), URL above (checked 2026-10)

_Last reviewed: 2026-10_
