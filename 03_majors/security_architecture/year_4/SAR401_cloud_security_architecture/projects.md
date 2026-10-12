# SAR401 · Labs and projects

Labs run in a personal cloud organisation on one provider (AWS, Azure or Google Cloud) with a budget alarm at a small amount (for example US$10) and alerts at 50%, 80% and 100%; P3 also needs a second provider on paper. Tear down billable resources the same day. Only test your own accounts; CloudGoat runs in your own account and flaws.cloud is a public, legal training site. Lab 3 is done without AI assistants. All organisations below are *illustrative scenarios* unless a source is given.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Case chains | Break down the Capital One (2019), Snowflake customer (2024) and Exchange Online (2023) chains; complete two flaws.cloud levels | Chain diagrams with the guardrail that would have broken each; defensive notes for each level | 3 h |
| 2 · Guardrails and test matrix | Deploy six preventive guardrails with paired detective controls; run a 20-case test matrix automatically | Policies, CI job and matrix results (100% expected = actual) | 5 h |
| 3 · IAM evaluation and ABAC (no AI) | Predict 15 allow/deny outcomes across identity, resource, boundary, session and organisation policies; implement tag-based access and try to re-tag your way in | Predictions, actual results, explanation of every miss, a failed re-tag attempt | 4 h |
| 4 · Data perimeter | Build identity, resource and network perimeters around a bucket and a database | Policies, and five blocked exfiltration attempts from a second account and the internet | 5 h |
| 5 · Egress and metadata | Restrict a workload's egress to two FQDNs; enforce IMDSv2 (or equivalent) organisation-wide | Firewall rules, a blocked egress log, a failed legacy metadata call | 4 h |
| 6 · Keys and discovery | Write key policies separating key administrators from users; scan synthetic data with Indian identifiers and tune detection | Key policies, denied decrypt by an administrator, detection precision before and after tuning | 4 h |
| 7 · Log archive and containment | Send organisation audit logs to a write-once archive in a separate account; dry-run a "compromised role" containment runbook | Denied deletion by a workload admin, runbook with timings | 5 h |
| 8 · Posture and attack paths | Run Prowler (or an equivalent) on your organisation; triage the top 20 findings; draw three attack paths and cut each | Triage table, paths, fixes and re-scan evidence | 4 h |
| 9 · Kubernetes hardening | Remove cluster-admin from humans and pipelines, enforce the restricted Pod Security Standard and signed images, add three Falco rules | Policies, a rejected pod, triggered benign Falco alerts | 4 h |
| 10 · AI policy audit and CI gate | Have an assistant draft five policies; validate them with automated checks; gate policy pull requests on the checks | Defect log, fixed policies, a blocked pull request | 3 h |

## Projects

### P1 · Hardening your own cloud organisation (L1, ~6 hours)

**Real-world inspiration:** AWS's data perimeter guidance and the equivalent Google Cloud and Azure mechanisms are designed so that valid credentials alone are not enough to move data out ([AWS](https://aws.amazon.com/identity/data-perimeters-on-aws/)).

**What to build:** extend your CLD301 P1 foundation (or build one) with a data perimeter around one storage bucket, metadata-service hardening, an immutable log archive and an automated guardrail test matrix.

**Acceptance criteria:**
- A request to the bucket from a principal outside your organisation fails, as does a request from inside the organisation through an unexpected network (both logged).
- Legacy metadata calls fail on every instance (show the configuration and a failed call).
- A workload administrator cannot delete or overwrite archived logs (denied call shown).
- The guardrail matrix (at least 12 cases) runs in CI and passes 100%.
- **Cost ceiling:** US$3.

**Stretch goals:** a detective alert on any change to the perimeter policies; a monthly entitlement report.

**What it proves to an employer:** you secure an environment against the most common cloud failure, valid credentials used in the wrong place.

### P2 · Cloud security architecture for a hospital chain (L2, ~15 hours)

**Real-world inspiration:** hospitals hold the most sensitive personal data and face ransomware and records theft; India's DPDP Act and CERT-In directions apply, and residency matters for patient data. The hospital chain is an *illustrative scenario*: 12 hospitals moving their records system, imaging archive and patient app to one cloud in Indian regions.

**What to build:** an architecture package and a partial implementation:
- organisation structure and guardrails;
- IAM for clinicians' applications, IT staff, vendors and workloads;
- data perimeters and network design with private service access;
- key hierarchy and custody choice for records and imaging;
- logging, detection routing and forensic readiness;
- PaaS hardening for the managed database and storage;
- a residency and regulation map.

**Acceptance criteria:**
- Ten documented exfiltration attempts (from a second account, from the internet with stolen test credentials, by public snapshot, by cross-account copy and others) all fail, with logs.
- All in-scope accounts pass at least 90% of CIS Level 1 checks in Prowler or an equivalent, with every remaining failure risk-accepted in writing.
- Vendor access is time-bound and every vendor session is logged.
- A restore of the records database into an isolated recovery account works and its keys are not usable by the production account.
- The regulation map links each control to a DPDP, CERT-In or sector requirement with a source; unverifiable items are marked "(unconfirmed)".
- **Cost ceiling:** US$15; destroy resources after each session.

**Stretch goals:** a managed AI service for discharge summaries behind private endpoints with prompt logging and redaction; detection of abnormal access to celebrity patient records (illustrative).

**What it proves to an employer:** you can design and partly build a regulated cloud estate whose controls are tested, not assumed.

### P3 · Multi-account security architecture for a payments company (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** payment companies in India operate under RBI directions, NPCI rules and CERT-In reporting, and most run on public cloud. The company is an *illustrative scenario*: a UPI-style payments app, merchant APIs, a fraud engine on Kubernetes, a data platform and an AI support assistant using a managed model, across about 40 accounts (or subscriptions or projects).

**What to build:**
- the full design package: organisation tree, guardrails, IAM, data perimeters, network, keys, logging, detection, Kubernetes, serverless and AI service controls, an operations-agent permission model, and a mapping to a second provider;
- an infrastructure-as-code implementation of a representative slice (management, security, log archive, network and two workload accounts);
- a guardrail test matrix of at least 40 cases in CI;
- a red-team-style exfiltration test plan against your own slice, executed with written self-authorisation and scope;
- a regulation and evidence map; and a cost estimate.

**Acceptance criteria:**
- The 40-case guardrail matrix passes 100% in CI, and a deliberately broken guardrail makes the job fail.
- All ten exfiltration paths in your plan are blocked or detected within 15 minutes, with evidence for each.
- No long-lived access keys exist anywhere in the slice (automated check).
- The operations agent's role can read everything needed for investigation, can propose changes only through pull requests, and is denied direct writes to production (shown).
- The managed AI service is reachable only privately, has quotas and spend alerts, and logs prompts with redaction of synthetic personal data.
- The second-provider mapping names a concrete service and policy for every control.
- You defend the design in a 25-minute oral; the panel describes an incident (stolen CI credentials, or a public snapshot) and you show the controls, logs and runbook steps that apply.
- **Cost ceiling:** US$40 total.

**Stretch goals:** cross-cloud identity federation for the data platform; an attack-path analysis comparing an open-source stack with a commercial CNAPP trial.

**What it proves to an employer:** this is the work of a cloud security architect, tested end to end and ready to walk through in an interview.

## Feeds into

- [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md): with CLD301 and SEC303.
- [SAR404 Resilience and Security Strategy](../SAR404_resilience_business_continuity_and_security/README.md): isolated recovery accounts and immutable backups.
- [SAR501 Frontier Seminar](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md): confidential computing and autonomous operations research.
- The [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md): P3 is its cloud foundation.
