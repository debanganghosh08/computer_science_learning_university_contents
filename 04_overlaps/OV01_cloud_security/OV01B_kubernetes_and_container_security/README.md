# OV01B · Kubernetes and Container Security

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 (CKS level) | [CLD301](../../../03_majors/cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md), [SEC303](../../../03_majors/cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md); corequisite [SAR401](../../../03_majors/security_architecture/year_4/SAR401_cloud_security_architecture/README.md); strongly recommended [CLD303](../../../03_majors/cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) and [OV01A](../OV01A_cloud_security_posture_detection_and_response/README.md) | [CLD501](../../../03_majors/cloud_engineering/year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md), [SAR501](../../../03_majors/security_architecture/year_5/SAR501_frontier_seminar_post_quantum_migration/README.md), [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [OV01 Cloud Security overlap](../README.md). CLD303 teaches how Kubernetes works; SAR401 Chapter 9 places it in a cloud security architecture. This course makes a cluster hard to break, quick to detect abuse in, and possible to investigate.

## Why this course matters now

Kubernetes is where most new backend and AI workloads run, and its defaults favour getting started over safety. Incidents show the pattern: in 2018 attackers mined cryptocurrency on Tesla's cloud through a Kubernetes console left without a password ([WIRED](https://www.wired.com/story/cryptojacking-tesla-amazon-cloud/)); in January 2024 the "Leaky Vessels" runc flaw (CVE-2024-21626) allowed container breakout from a crafted image ([Snyk](https://www.snyk.io/blog/cve-2024-21626-runc-process-cwd-container-breakout/)); in March 2025 the Kubernetes Security Response Committee warned that ingress-nginx vulnerabilities, including CVE-2025-1974, "could make it easy for attackers to take over your Kubernetes cluster" ([Kubernetes blog](https://kubernetes.io/blog/2025/03/24/ingress-nginx-cve-2025-1974/)); and GPU nodes added their own escape risks, such as CVE-2024-0132 in the NVIDIA Container Toolkit ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-0132)). The platform has improved fast: user namespaces for pods and MutatingAdmissionPolicy both became stable in Kubernetes v1.36, and Kyverno graduated in the CNCF in March 2026. AI assistants now draft manifests, RBAC and policies in seconds, and they often get security fields subtly wrong. Someone still has to know which permission is an escalation path, which policy will block a deploy at 2 a.m., and what to do when Falco fires.

## Learning outcomes

By the end you can:

1. **Threat-model** a cluster using the Microsoft Threat Matrix for Kubernetes and MITRE ATT&CK for Containers, and **name** the controls for each stage.
2. **Harden** a control plane and nodes to the CIS Kubernetes Benchmark, and **explain** every remaining failure as accepted, managed by the provider, or out of scope.
3. **Audit** RBAC for escalation-prone permissions and **reduce** human and workload access to least privilege.
4. **Enforce** Pod Security Standards and custom rules with Pod Security Admission, ValidatingAdmissionPolicy, MutatingAdmissionPolicy, Kyverno or Gatekeeper, rolled out safely from audit to enforce.
5. **Isolate** workloads with security contexts, seccomp, AppArmor or SELinux, user namespaces, sandboxed runtimes and network policy, and **measure** what each control blocks.
6. **Verify** image signatures and attestations at admission and **manage** vulnerable images with SBOMs and VEX.
7. **Detect** runtime threats with Falco or Tetragon and Kubernetes audit logs, and **respond** to a compromised pod while preserving evidence.
8. **Pass** CKS-style hands-on tasks under time pressure.

## Chapters and lessons

### Chapter 1 · Threat model of a cluster (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Kubernetes for security engineers | The API server as the front door; etcd holds every Secret; kubelet APIs; CNI and CSI plugins; admission chain (fast recap of CLD303 for students without it) | Draw a cluster data-flow diagram with trust boundaries |
| 1.2 Threat matrices | Microsoft's Threat Matrix for Kubernetes; MITRE ATT&CK Containers; the CNCF TAG Security cloud native security whitepaper | Map Tesla 2018, Leaky Vessels and IngressNightmare to matrix cells |
| 1.3 Who attacks clusters and why | Cryptomining, credential theft to the cloud account, data theft, supply-chain implants; why the cloud IAM role of a node is the real prize | List the cloud permissions reachable from one node in your lab |
| 1.4 The legal lab | kind or k3d locally, a managed cluster in your sandbox, Kubernetes Goat for deliberately vulnerable scenarios, Killercoda for timed practice | Build both clusters with a teardown script |

**Check your understanding:** Why is "can create pods" in a namespace close to "can read every Secret that namespace's service accounts can"? Which matrix stage does a public dashboard enable? Why does node identity matter more on managed clusters than self-managed ones?

### Chapter 2 · Benchmarks and control-plane hardening (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 CIS Kubernetes Benchmark | Control plane, etcd, node and policy sections; kube-bench; managed-provider variants (EKS, AKS, GKE) and what the provider owns | Run kube-bench on both clusters; classify every failure |
| 2.2 API server settings | Anonymous auth, authorisation modes (Node, RBAC), admission plugins, structured authentication configuration, API exposure (private endpoints, authorised networks) | Close public API access on the managed cluster without locking yourself out |
| 2.3 etcd and Secrets at rest | Encryption at rest with a KMS v2 provider; etcd TLS and access; why etcd backups are as sensitive as the cluster | Enable KMS encryption in the lab; prove a Secret is unreadable in etcd |
| 2.4 Audit policy design | Levels (None, Metadata, Request, RequestResponse), avoiding Secret bodies in logs, volume and cost; NSA and CISA Kubernetes Hardening Guidance | Write an audit policy; measure log volume per hour |

**Check your understanding:** Which CIS checks are meaningless on a managed control plane, and who answers for them? Why log Secret access at Metadata level only? What breaks if the KMS provider is unavailable?

### Chapter 3 · Authentication and RBAC in depth (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Human access | OIDC and cloud IAM mapping (EKS access entries, GKE IAM, AKS with Entra ID), short-lived credentials, no shared kubeconfigs, break-glass | Replace a static admin kubeconfig with SSO and a break-glass path |
| 3.2 Escalation-prone permissions | Verbs and resources to review: `escalate`, `bind`, `impersonate`, pod creation, `nodes/proxy`, reading Secrets, creating service-account tokens, wildcard rules (named for review, not for use) | Audit a provided RBAC set with `kubectl auth can-i --list` and a graph tool; rank risks |
| 3.3 Service accounts | Bound projected tokens, `automountServiceAccountToken: false`, per-workload accounts, token audiences | Remove token mounts from workloads that do not call the API |
| 3.4 Workload identity to the cloud | EKS Pod Identity and IRSA, GKE Workload Identity Federation, Azure Workload Identity; scoping cloud roles per service account | Grant one pod read access to one bucket; prove others cannot |

**Check your understanding:** Why is `bind` on ClusterRoles as dangerous as `cluster-admin`? What does a pod lose if its token is not mounted, and what does an attacker lose? How would you find every pod that can reach production data in the cloud account?

### Chapter 4 · Admission control and policy (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Pod Security Standards | Privileged, baseline and restricted profiles; Pod Security Admission labels (enforce, audit, warn); exemptions | Move a namespace from baseline to restricted; fix the workloads that fail |
| 4.2 Native policy with CEL | ValidatingAdmissionPolicy (stable since v1.30) and MutatingAdmissionPolicy (stable since v1.36); bindings, parameters, match conditions | Write a policy requiring resource limits and non-latest image tags |
| 4.3 Policy engines | Kyverno (CNCF graduated March 2026) and OPA Gatekeeper; validate, mutate, generate, verify-images; policy reports | Implement the same three rules in Kyverno and Gatekeeper; compare |
| 4.4 Rolling out safely | Audit → warn → enforce; exceptions with expiry; webhook `failurePolicy` and availability; testing policies in CI | Simulate a webhook outage; document the deploy impact and your chosen failure mode |

**Check your understanding:** When should an admission webhook fail closed, and what must be true for that to be safe? Why roll out in audit mode first? What does native CEL policy remove from your operational burden?

### Chapter 5 · Workload hardening (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Security context | `runAsNonRoot`, `readOnlyRootFilesystem`, `allowPrivilegeEscalation: false`, dropping all capabilities and adding back only what is needed | Harden three sample workloads; record each change that broke them and the fix |
| 5.2 Syscall and LSM controls | seccomp `RuntimeDefault` and custom profiles, AppArmor fields, SELinux contexts; Security Profiles Operator to record profiles | Record a seccomp profile for one service and enforce it |
| 5.3 User namespaces | `hostUsers: false` (stable since v1.36): root in the container is unprivileged on the host; limits and runtime support | Show the host UID mapping for a pod with and without user namespaces |
| 5.4 Resource controls as security | Requests, limits, ResourceQuota and LimitRange against denial of service and cost abuse | Contain a CPU-burning pod within its namespace quota |

**Check your understanding:** Which single securityContext field blocks the most real escapes, and why? What does a read-only root filesystem force developers to change? Why do user namespaces reduce the impact of runtime bugs like CVE-2024-21626?

### Chapter 6 · Isolation and multi-tenancy (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Namespaces are not walls | What a namespace isolates and what it does not (nodes, kernel, cluster-scoped resources, DNS) | Write the tenancy threat model for two teams sharing a cluster |
| 6.2 Sandboxed runtimes | gVisor and Kata Containers via RuntimeClass; GKE Sandbox; performance cost | Benchmark a service under runc and gVisor |
| 6.3 Node isolation | Dedicated node pools with taints, host namespaces and `hostPath` risks, node-level blast radius | Pin an untrusted workload to an isolated pool |
| 6.4 Tenancy models | Namespace per tenant, virtual clusters (vCluster), cluster per tenant; cost against isolation | Recommend a model for three illustrative tenants and defend it |

**Check your understanding:** When is a separate cluster the only honest answer? What does gVisor protect against that seccomp does not? Why are `hostPath` mounts a policy priority?

### Chapter 7 · Network security (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 NetworkPolicy | Default deny ingress and egress, namespace and pod selectors, DNS egress exceptions, testing policies | Apply default deny to the lab app and restore only needed flows |
| 7.2 Beyond the core API | Cilium policies (L7, DNS/FQDN-aware egress), observing flows with Hubble | Restrict egress to two external domains |
| 7.3 Encryption in the cluster | Service mesh mTLS (Istio ambient, Linkerd), Cilium transparent encryption; identity-based authorisation | Enable mTLS and prove plaintext is rejected |
| 7.4 Exposure points | Ingress controllers and Gateway API implementations, admission webhooks reachable from the pod network (the IngressNightmare lesson), cloud metadata endpoints from pods | Block pod access to the instance metadata service and verify |

**Check your understanding:** Why is egress control the most-skipped and most-valuable policy? What did IngressNightmare reveal about trusting in-cluster network reachability? When is a mesh worth its operational cost for security alone?

### Chapter 8 · Secrets and sensitive data (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Secrets done right | Mounted files over environment variables, rotation, least access per service account | Rotate a database credential without restarting all pods |
| 8.2 External secret stores | External Secrets Operator, Secrets Store CSI Driver, HashiCorp Vault or OpenBao dynamic credentials | Serve short-lived database credentials from Vault to one workload |
| 8.3 Certificates for workloads | cert-manager, Pod Certificates (stable in v1.37), SPIFFE identities | Issue workload certificates with a 24-hour lifetime |
| 8.4 Backups and snapshots | Velero backups and etcd snapshots contain Secrets; encryption and access to backup storage | Show that a lab backup is encrypted and access-restricted |

**Check your understanding:** Why are environment variables a weaker home for secrets than files? What is the real secret in a cluster that uses an external store? Who can read your cluster backups today?

### Chapter 9 · Supply chain at the cluster door (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Image scanning that helps | Trivy and Grype, SBOM-based scanning, VEX to suppress non-exploitable findings, fix-available filters | Cut a 300-CVE image report to the actionable set with VEX |
| 9.2 Minimal images | Distroless, Wolfi-based and scratch images; rebuild cadence; digest pinning | Rebuild a service on a minimal base; compare CVE counts and size |
| 9.3 Signature and attestation verification | Kyverno `verifyImages` and Sigstore policy-controller; keyless identities; requiring provenance attestations | Reject unsigned images and images built outside your pipeline |
| 9.4 Registries | Private registries, immutability, pull-through caches, admission rules on allowed registries | Allow only your registry; test with a public image |

**Check your understanding:** Why is "zero CVEs" a poor target? What exactly does a keyless signature prove about an image? Where does OV03A take this further?

### Chapter 10 · Runtime detection and incident response (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Falco | Syscall and audit-log sources via eBPF, rules, macros, lists, exceptions; Falco graduated in the CNCF in February 2024 | Write five rules for your app's expected behaviour; tune false positives |
| 10.2 eBPF enforcement | Tetragon tracing policies, observe versus enforce, kernel requirements | Kill a process that writes to a protected path, in observe mode first |
| 10.3 Audit-log detections | `exec` into pods, new cluster-admin bindings, privileged pod creation, Secret reads by unusual service accounts, anonymous requests | Ship audit logs to the OV01A pipeline; add four detections |
| 10.4 Responding to a compromised pod | Quarantine with a label-selected deny policy, cordon the node, capture logs and container state (kubelet checkpoint API, beta since v1.30), preserve before deleting | Run the compromised-pod exercise; produce an evidence bundle |
| 10.5 Eradication and recovery | Rebuild from known-good images and manifests via GitOps, rotate service-account and cloud credentials, check for persistence (new bindings, webhooks, DaemonSets, CronJobs) | Write the persistence checklist and run it on the exercise cluster |

**Check your understanding:** Why delete a compromised pod last, not first? What persistence would an attacker with cluster-admin leave that a pod restart does not remove? How do you tell a Falco true positive from a debugging session?

### Chapter 11 · Nodes and runtimes (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Container-optimised operating systems | Bottlerocket, Talos, Flatcar, Container-Optimized OS: immutable roots, minimal packages, update models | Compare attack surface (packages, open ports) of two node images |
| 11.2 Kubelet hardening | Webhook authentication and authorisation, read-only port off, certificate rotation, node restriction | Verify kubelet settings on every node with a script |
| 11.3 Runtime patching | runc and containerd advisories, node upgrade cadence, surge upgrades without downtime | Plan and execute a node image upgrade with zero failed requests |
| 11.4 GPU nodes | NVIDIA Container Toolkit and GPU Operator advisories (CVE-2024-0132), MIG versus time-slicing isolation for shared GPUs | Write the isolation note for a shared GPU node pool |

**Check your understanding:** Why are immutable node images easier to defend than patched long-lived nodes? Which GPU sharing mode gives memory isolation? How fast must a node fleet move after a runtime escape advisory?

### Chapter 12 · AI and Kubernetes security; CKS readiness (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Reviewing AI-drafted manifests and policies | Common failures: missing securityContext fields, over-broad RBAC, policies that match nothing, deprecated APIs | Review ten AI-drafted manifests and policies; record every defect |
| 12.2 Agents with cluster access | Read-only roles for diagnosis agents, PR-based changes, MCP servers for Kubernetes with scoped credentials, audit | Design and test the RBAC for a diagnosis agent |
| 12.3 AI workloads | Model-serving pods, model artefact integrity, egress from inference pods, multi-tenant GPU isolation | Threat-model a model-serving namespace |
| 12.4 CKS readiness | Domains: Cluster Setup 15%, Cluster Hardening 15%, System Hardening 10%, Minimize Microservice Vulnerabilities 20%, Supply Chain Security 20%, Monitoring, Logging and Runtime Security 20%; exam based on v1.35; CKA required first | Two timed mock exams on Killercoda-style tasks |

**Check your understanding:** Why does an AI-drafted policy that "passes" deserve suspicion? What is the least privilege a diagnosis agent needs to explain a CrashLoopBackOff? Which CKS domain is weakest for you, by measured mock score?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Clusters and threat model | Data-flow diagram |
| 2 | 2 | Lab 2 · Benchmark and audit policy | kube-bench classification |
| 3 | 3 | Lab 3 · RBAC audit | — |
| 4 | 4 | Lab 4 · Admission policy | **P1 due** |
| 5 | 5 | Lab 5 · Workload hardening | Hardening change log |
| 6 | 6 | Lab 6 · Sandboxing and tenancy | — |
| 7 | 7 | Lab 7 · Network policy and mTLS | Mid-term (AI off): manifest and RBAC review |
| 8 | 8 | Lab 8 · Secrets and certificates | — |
| 9 | 9 | Lab 9 · Signed images only | **P2 due** |
| 10 | 10 | Lab 10 · Falco and audit detections | — |
| 11 | 10 | Compromised-pod exercise | Evidence bundle |
| 12 | 11 | Node upgrade drill | — |
| 13 | 12 | AI review and agent RBAC | Mock CKS 1 |
| 14 | 12 | Mock CKS 2 | **P3 due** |
| 15 | Review | Timed hands-on exam and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** drafting Kyverno, Gatekeeper and CEL policies from a written rule; explaining a Falco rule or an audit event; generating test manifests that should pass and fail a policy; summarising kube-bench output.
- **Do without AI (drills):** RBAC review by hand; writing securityContext blocks and NetworkPolicies from memory; the timed mock exams (the CKS exam has no AI assistance); the mid-term and final.
- **Verify AI output by:** running every policy against a test suite of compliant and non-compliant manifests (`kyverno test`, `gator verify`, or CEL policy tests) before applying; checking API versions against your cluster version; confirming RBAC with `kubectl auth can-i` for named subjects rather than reading YAML.
- **Where AI still fails here:** keep a log of AI-drafted manifests and policies that looked correct but failed your tests. Expect to record policies matching the wrong resource kinds, network policies that silently allow all egress, and RBAC rules with wildcards added "for convenience".

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final: timed hands-on exam (AI off) + oral defence of P3 | 30% |

**Mastery gate.** You pass when you can, with AI tools off, within two hours on a fresh cluster: (1) bring a namespace to the restricted Pod Security Standard with its workloads still running; (2) find and remove two planted RBAC escalation paths; (3) block unsigned images; (4) write a Falco rule that catches a described behaviour; (5) contain a planted compromised pod and list the evidence you kept.

## Industry reality

Managed Kubernetes moved the control plane to providers, but not RBAC, admission, workload settings or runtime detection. Public advisories show where the risk lands: ingress controllers exposed admission endpoints to the pod network in 2025, and the Kubernetes project announced the retirement of ingress-nginx in November 2025 ([Kubernetes blog](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)); runtime and GPU toolkit escapes recur yearly. The CKS exam is the most recognised hands-on signal for this work ([Linux Foundation](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/)).

**Interview questions from this course**

1. *A developer asks for `cluster-admin` "just for debugging". What do you give them?* Strong answer: refuses standing cluster-admin; offers a namespaced role with read access to logs and events, `pods/exec` only in non-production or via just-in-time elevation with expiry and audit; mentions ephemeral debug containers and break-glass.
2. *How would you stop unsigned images reaching production?* Strong answer: sign in the pipeline with keyless Sigstore identities; verify at admission with Kyverno or policy-controller, matched to the pipeline identity and repository; require provenance; handle system namespaces and emergencies with audited exceptions; monitors the webhook's availability.
3. *Falco alerts: shell spawned in a production container. Walk me through it.* Strong answer: check context (who, which pod, any linked `exec` in the audit log), quarantine with network policy, preserve logs and container state, check the service account's permissions and recent API calls, hunt for persistence, rebuild from known-good images, rotate credentials.
4. *What does the restricted Pod Security Standard require, and what usually breaks?* Strong answer: non-root, no privilege escalation, all capabilities dropped, seccomp set, no host namespaces or hostPath; breaks images that run as root, write to the filesystem, or bind low ports; fixes include image changes and emptyDir mounts.
5. *Two teams share a cluster. One runs untrusted customer code. Design the isolation.* Strong answer: separate node pool with taints, sandboxed runtime (gVisor or Kata), restricted PSS, default-deny network policy with tight egress, no service-account token, separate cloud identity, quotas; states when a separate cluster is required instead.

## Resources (free first)

- **Official:** Kubernetes security concepts — https://kubernetes.io/docs/concepts/security/ ; Pod Security Admission — https://kubernetes.io/docs/concepts/security/pod-security-admission/ ; ValidatingAdmissionPolicy — https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/ ; auditing — https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/ ; user namespaces — https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/
- **Guidance:** NSA and CISA Kubernetes Hardening Guidance (CISA alert with links) — https://www.cisa.gov/news-events/alerts/2022/03/15/updated-kubernetes-hardening-guide ; CIS Benchmarks — https://www.cisecurity.org/cis-benchmarks ; MITRE ATT&CK Containers — https://attack.mitre.org/matrices/enterprise/containers/ ; Microsoft Threat Matrix for Kubernetes — https://microsoft.github.io/Threat-Matrix-for-Kubernetes/ ; CNCF TAG Security — https://github.com/cncf/tag-security
- **Tools:** kube-bench — https://github.com/aquasecurity/kube-bench ; Kubescape — https://kubescape.io/ ; Kyverno — https://kyverno.io/docs/ ; Gatekeeper — https://open-policy-agent.github.io/gatekeeper/website/docs/ ; Falco — https://falco.org/docs/ ; Tetragon — https://tetragon.io/ ; Trivy — https://trivy.dev/ ; gVisor — https://github.com/google/gvisor ; Security Profiles Operator — https://github.com/kubernetes-sigs/security-profiles-operator
- **Practice:** Kubernetes Goat — https://github.com/madhuakula/kubernetes-goat ; Killercoda — https://killercoda.com/
- **Paid, optional:** CKS exam ($445 at the time of writing; requires a passed CKA).

## Sources

All checked 12 Oct 2026.

- WIRED, "Hackers Hijacked Tesla's Cloud to Mine Cryptocurrency" (Feb 2018) — https://www.wired.com/story/cryptojacking-tesla-amazon-cloud/
- Snyk, CVE-2024-21626 runc container breakout (Jan 2024) — https://www.snyk.io/blog/cve-2024-21626-runc-process-cwd-container-breakout/
- Kubernetes blog, "Ingress-nginx CVE-2025-1974: What You Need to Know" (24 Mar 2025) — https://kubernetes.io/blog/2025/03/24/ingress-nginx-cve-2025-1974/ ; ingress-nginx retirement (11 Nov 2025) — https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/
- NVD, CVE-2024-0132 (NVIDIA Container Toolkit, published 26 Sep 2024) — https://nvd.nist.gov/vuln/detail/CVE-2024-0132
- Kubernetes documentation feature states: Pod Security Admission stable since v1.25; MutatingAdmissionPolicy stable since v1.36 — https://kubernetes.io/docs/reference/access-authn-authz/mutating-admission-policy/ ; user namespaces stable since v1.36 — https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/ ; kubelet checkpoint API beta since v1.30 — https://kubernetes.io/docs/reference/node/kubelet-checkpoint-api/
- Kubernetes v1.37 release (26 Aug 2026; Pod Certificates stable) — https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/
- CNCF, Falco graduation (29 Feb 2024) — https://www.cncf.io/announcements/2024/02/29/cloud-native-computing-foundation-announces-falco-graduation/ ; Kyverno graduation (16 Mar 2026) per the CNCF landscape data — https://github.com/cncf/landscape
- Linux Foundation, CKS exam page (domains and weights, Kubernetes v1.35, CKA prerequisite, price) — https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/

_Last reviewed: 2026-10_
