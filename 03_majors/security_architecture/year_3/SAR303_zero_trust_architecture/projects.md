# SAR303 · Labs and projects

Labs run on your own machine (Docker, a `kind` or `k3d` Kubernetes cluster, Keycloak as the identity provider) or in a personal cloud account with a budget alarm. Everything named below is an *illustrative scenario* unless a source is given. Lab 6 is done without AI assistants. You configure and test only infrastructure you own.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Flat network and tenets | Trace how one compromised laptop reaches a database in a provided flat-network diagram; score the design against the seven SP 800-207 tenets | Annotated path, tenet scores with evidence | 3 h |
| 2 · Trust algorithm | Design a criteria-based trust algorithm for a brokerage back office, then threat-model it with STRIDE | Algorithm inputs, rules, fail behaviour and a threat list | 4 h |
| 3 · Continuous evaluation | Make a risk signal from the IdP (simulated "user risk high" event) revoke an active session in a demo app within 60 seconds | Code, logs with timestamps showing revocation latency | 5 h |
| 4 · Device trust | Issue device certificates from a lab CA, collect five posture checks with osquery and use them as inputs to an OPA decision | Policy, posture queries, allow and deny examples | 5 h |
| 5 · Identity-aware proxy | Put Pomerium in front of a web app and replace static SSH keys with short-lived certificates (Teleport or an OpenSSH CA) | Configuration, proof that direct access is refused, certificate lifetimes | 5 h |
| 6 · Default deny (no AI) | Enforce default deny in every namespace of a lab cluster with Cilium and open only required flows, including DNS | Policy set and a flow test matrix (allowed and denied) with results | 5 h |
| 7 · Data-centric access | Mask PAN-like and Aadhaar-like columns for analysts while support staff see the last four digits | Views or policies, role tests, query outputs | 3 h |
| 8 · Policies and PDP outage | Write 15 access policies in Rego or Cedar with tests; simulate a PDP outage and observe each PEP's behaviour | Policy repository, test results, outage observations against your intended fail behaviour | 4 h |
| 9 · Decision logs and automation | Ship allow and deny decisions to a log store; automate removal of access unused for 60 days | Log samples with inputs, automation script and run record | 4 h |
| 10 · No long-lived keys | Replace a CI pipeline's stored cloud key with OIDC workload identity federation restricted by repository and branch | Workflow, trust policy, a denied run from another branch | 3 h |

## Projects

### P1 · Retire the campus VPN for three apps (L1, ~6 hours)

**Real-world inspiration:** Google's BeyondCorp papers describe moving staff off a privileged network to per-request, identity- and device-aware access ([Google Research](https://research.google/pubs/beyondcorp-a-new-approach-to-enterprise-security/)). The college is an *illustrative scenario*: staff use a VPN to reach an exam portal, a library admin app and an internal Git server.

**What to build:** a lab deployment where all three apps sit behind an identity-aware proxy with Keycloak, passkey or TOTP sign-in, two device tiers, and per-app policies (only exam staff reach the exam portal, only from a managed device).

**Acceptance criteria:**
- A direct request to each app that bypasses the proxy is refused (show the network rule and the failed request).
- Each app verifies the proxy's signed identity assertion; a forged header is rejected.
- A test matrix of 12 access attempts (user × device tier × app) matches the policy 100%.
- Every decision appears in the log with user, device tier, app and result.
- A one-page rollback plan exists and has been tried once.

**Stretch goals:** a browser-only, read-only path for unmanaged devices; session revocation from Lab 3 wired in.

**What it proves to an employer:** you can turn zero trust from a slogan into a working, tested access path.

### P2 · A microsegmented platform for a food-delivery backend (L2, ~15 hours)

**Real-world inspiration:** large delivery and commerce platforms run hundreds of services where one compromised service must not reach payments. NIST SP 800-207A (2023) describes identity-based segmentation for cloud-native applications. The backend is an *illustrative scenario* with orders, payments, restaurants, riders, notifications and an analytics consumer.

**What to build:** the six services on Kubernetes with SPIFFE-style workload identities, mesh mTLS, L7 authorization policies, namespace default deny, and an observe-then-enforce rollout under load.

**Acceptance criteria:**
- A flow matrix of at least 30 service-to-service and egress flows (allowed and denied) matches the enforced policy 100%, verified by an automated test job.
- Payments accepts calls only from checkout on the specified path and method; any other caller gets a deny that is logged.
- Switching from observe to enforce under a steady load test produces zero failed legitimate requests (show the graph).
- The analytics consumer can read only the topics it needs; a test proves it cannot write.
- PDP or mesh control-plane outage behaviour is documented and demonstrated for two services.

**Stretch goals:** egress allow-lists to two external payment endpoints; a comparison of sidecar and ambient mesh overhead.

**What it proves to an employer:** you can deliver segmentation that holds under real traffic without breaking production, which is where most programmes fail.

### P3 · Zero trust programme and reference slice for an Indian bank (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** RBI's 2026 directions for commercial banks require MFA for privileged users and set resilience expectations ([DSCI summary](https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf)); CISA's ZTMM 2.0 and NIST SP 1800-35 give the maturity model and example builds. The bank is an *illustrative scenario*: 2,500 staff, a contracted call centre, an on-premises core banking system, cloud-hosted digital channels and a new internal AI assistant.

**What to build:**
- a ZTMM 2.0 assessment with evidence for every stage you assign;
- a target architecture on the SP 800-207 model: PDP inputs, PEPs, fail behaviour, decision logging;
- a three-year roadmap with dependencies and a costed business case;
- a working reference slice in your lab: Keycloak with passkeys, device posture, an identity-aware proxy, one microsegmented application, session revocation on risk, decision logs, and an agent identity for the AI assistant with per-tool policies and one approval-gated action;
- a metrics dashboard with at least six metrics and their formulas;
- a mapping of the design to the RBI and CERT-In requirements it supports.

**Acceptance criteria:**
- Two reviewers can trace every assigned ZTMM stage to a piece of evidence.
- The roadmap passes a dependency check: no item depends on one scheduled later (checked with a small script or a graph tool).
- In the slice, a test suite of at least 40 access cases (staff, contractor, admin, agent; managed and unmanaged devices) passes 100%.
- A high-risk signal revokes the affected session within 60 seconds (logs with timestamps).
- The AI assistant cannot call the approval-gated tool without a recorded human approval, even when a test document instructs it to (benign canary).
- The business case states costs, retirements (VPN, legacy appliances) and three risks the plan does not address.

**Stretch goals:** OT zones and conduits for the bank's branch devices; a tabletop of a PDP outage with the operations team.

**What it proves to an employer:** you can assess, plan, cost and demonstrate a zero trust programme end to end, which is the core of zero trust architect roles.

## Feeds into

- [SAR401 Cloud Security Architecture](../../year_4/SAR401_cloud_security_architecture/README.md): data perimeters and multi-account guardrails extend Chapters 6–7.
- [SAR402 Identity Architecture at Scale](../../year_4/SAR402_identity_architecture_at_scale/README.md): the identity control plane in depth.
- [SAR403 Security Architecture for AI Systems and Agents](../../year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md): P3's agent identity and approval gating grow into a full agent platform design.
- [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) and the [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md).
