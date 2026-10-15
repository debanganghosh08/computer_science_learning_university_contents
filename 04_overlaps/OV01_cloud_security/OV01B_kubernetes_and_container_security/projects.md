# OV01B · Labs and projects

Use a local cluster (kind or k3d) for most labs and one small managed cluster (EKS, AKS or GKE) in your own sandbox account for cloud-identity and node labs. Deliberately vulnerable scenarios (Kubernetes Goat) run only on your own clusters. Every lab ships manifests and policies in Git, a test that proves the control works, and a note on what broke and why.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Clusters and threat model | Build a local and a managed cluster with teardown scripts; draw the data-flow diagram with trust boundaries; map three public incidents to the threat matrix | Scripts, diagram, mapping table | 4 h |
| 2 · Benchmark and audit policy | Run kube-bench on both clusters; classify each failure (fix, provider-owned, accepted); enable KMS encryption for Secrets in the local cluster; write an audit policy | Classification table, etcd proof that a Secret is encrypted, audit policy with measured log volume | 5 h |
| 3 · RBAC audit | Audit a provided RBAC set with planted escalation paths; reduce a team's access to least privilege; set up SSO-based human access on the managed cluster | Ranked findings, before/after `kubectl auth can-i --list` output, SSO configuration | 5 h |
| 4 · Admission policy | Enforce `restricted` Pod Security Standards on two namespaces; write the same three custom rules in ValidatingAdmissionPolicy and Kyverno (or Gatekeeper); test in CI | Policies, test suites (pass and fail manifests), CI run, webhook-outage experiment notes | 6 h |
| 5 · Workload hardening | Harden three sample services (securityContext, seccomp profile recorded with Security Profiles Operator, user namespaces) | Change log of every breakage and fix; proof that each control is active | 5 h |
| 6 · Sandboxing and tenancy | Run one workload under gVisor via RuntimeClass on an isolated node pool; benchmark latency under runc and gVisor | Benchmark table (p50/p99), tenancy recommendation for two illustrative teams | 4 h |
| 7 · Network policy and mTLS | Default-deny ingress and egress with only required flows; FQDN egress with Cilium; mesh or Cilium encryption; block pod access to the metadata service | Policy set, connectivity test matrix (expected vs actual), proof of plaintext rejection | 5 h |
| 8 · Secrets and certificates | Serve dynamic database credentials from Vault or OpenBao; issue short-lived workload certificates with cert-manager; check backup encryption | Rotation demo log, certificate lifetimes, backup access review | 4 h |
| 9 · Signed images only | Sign images in CI with keyless cosign; enforce `verifyImages` with provenance requirement; restrict registries | Admission test results: signed accepted, unsigned rejected, wrong-identity rejected | 4 h |
| 10 · Falco and audit detections | Five Falco rules for your app plus four audit-log detections shipped to the OV01A pipeline; compromised-pod exercise | Rules with tests, alert samples, evidence bundle, persistence checklist | 7 h |

## Projects

### P1 · Hardened namespace baseline (L1, ~6 hours)

**Real-world inspiration.** The restricted Pod Security Standard and the CIS Kubernetes Benchmark are the first things platform security teams enforce on shared clusters; most of the effort is fixing workloads, not writing policy.

**What to build.** A reusable "secure namespace" package (Helm chart or Kustomize base) that creates a namespace with restricted Pod Security Admission labels, default-deny network policies with DNS allowed, a ResourceQuota and LimitRange, a least-privilege service account with no token mount, and a sample workload that runs under all of it.

**Acceptance criteria**
- Applying the package to an empty cluster yields a running sample app with zero Pod Security Admission warnings.
- A test suite of at least 10 manifests (privileged pod, hostPath, root user, missing limits, etc.) is rejected with the expected message; 3 compliant manifests are accepted.
- A connectivity test shows only the declared flows succeed (at least 6 allowed and 6 denied cases).
- The README explains each control in one sentence and lists what an application must change to fit.

**Stretch goals.** Publish the package to an OCI registry, signed; add a Kyverno policy report summary to the README.

**What it proves to an employer.** You can turn security standards into something application teams can adopt in one command.

### P2 · Cluster policy and supply-chain gate (L2, ~15 hours)

**Real-world inspiration.** Platform teams gate what reaches production at admission: Pod Security Standards, organisation rules, and signature verification, with exceptions that expire. A webhook that fails the wrong way can block every deploy, so rollout discipline matters as much as rules.

**What to build.** A policy repository for the managed cluster: at least 12 rules (Pod Security beyond PSS, registry allow-list, required labels and owners, image signature and provenance verification, no `latest` tags, no NodePort services, resource limits), an exception mechanism with expiry, CI tests, and a staged rollout plan.

**Acceptance criteria**
- Every rule has passing and failing test manifests; CI blocks merges when tests fail.
- Rollout evidence: one week (or a compressed simulated week) in audit mode with a policy report, then enforce; violations reduced to zero or covered by dated exceptions.
- Signature verification rejects an unsigned image, an image signed by a different repository's workflow identity, and an image without a provenance attestation.
- Webhook failure behaviour is documented and tested: the cluster's system namespaces keep working during a simulated policy-engine outage.
- p95 admission latency added by policies is measured and stays under 200 ms for a deployment of 20 pods.

**Stretch goals.** Implement half the rules as native ValidatingAdmissionPolicy and compare latency and operational burden with the engine.

**What it proves to an employer.** You can enforce security at scale without becoming the team that breaks deployments.

### P3 · Detect and respond on Kubernetes (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Cryptomining on exposed clusters, container escapes such as CVE-2024-21626, and exposed ingress admission endpoints (CVE-2025-1974) all show that prevention fails sometimes; runtime detection and a rehearsed response decide the outcome. The exercise scenario is illustrative and runs only on your clusters.

**What to build.** A runtime security stack and response playbook for the managed cluster:
1. Falco (or Tetragon in observe mode) with rules tuned to the application's behaviour, plus Kubernetes audit-log detections, all routed to one alert queue with OV01A's cloud detections.
2. Response automation: a quarantine controller or script that applies a deny-all network policy to a labelled pod, cordons its node, captures logs, events and a container checkpoint where supported, and records hashes.
3. A persistence sweep script (new ClusterRoleBindings, webhooks, DaemonSets, CronJobs, service-account tokens, cloud role changes).
4. A game day run by a classmate with three announced scenarios (for example a shell in a container, an unexpected outbound connection, a new privileged binding).

**Acceptance criteria**
- Detection: all three scenarios alert within 2 minutes of the action; over 72 hours of normal load the stack raises ≤ 3 false positives, each tuned with a documented exception.
- Containment: each scenario is contained within 15 minutes of the alert without deleting evidence; the evidence bundle includes hashes and a chain-of-custody log.
- The persistence sweep finds a planted persistence mechanism the exercise leader adds without telling you.
- Recovery: the affected workload is redeployed from Git (GitOps or pipeline) with rotated credentials, and a test proves old credentials no longer work.
- A blameless after-action review lists root causes, detection gaps and at least five dated actions.

**Stretch goals.** Measure the runtime overhead of Falco or Tetragon on request latency and node CPU; compare rule coverage with the MITRE ATT&CK Containers matrix and publish the gaps.

**What it proves to an employer.** You can run Kubernetes security end to end: harden, detect, contain, investigate and recover. This is the profile container security and platform security teams hire for, and it maps closely to the CKS domains.

## Feeds into

- The [OV01 capstone](../README.md): P2 and P3 become the cluster half of the capstone estate.
- [OV03 DevSecOps](../../OV03_devsecops/README.md): the signature gate in P2 is the consumer side of OV03A's provenance and signing work.
- [CLD501 Frontier Seminar: Sovereign Cloud, Confidential Computing and Planet-Scale Infrastructure](../../../03_majors/cloud_engineering/year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md): sandboxed runtimes and confidential containers extend Chapter 6.
- [THS501 Thesis or Capstone I](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): measuring the cost and coverage of runtime detection is a thesis-sized question.
