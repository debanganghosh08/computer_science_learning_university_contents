# CLD303 · Containers and Kubernetes

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 (CKA level) | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [CLD403](../../year_4/CLD403_finops_and_cloud_cost_engineering/README.md), [CLD404](../../year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md), [OV02 Cloud-Native Backend](../../../../04_overlaps/OV02_cloud_native_backend/README.md) |

Part of the [Cloud Engineering major](../../README.md). Builds on the Linux namespaces and cgroups from [CS203 Operating Systems](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) and on Raft from [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) (etcd is a Raft store). Delivery pipelines and GitOps are taught in [OPS305](../../../devops_sre_platform_engineering/year_3/OPS305_configuration_management_and_gitops/README.md), and metrics, logs and traces in [OPS303](../../../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md); this course is about the cluster itself.

## Why this course matters now

Kubernetes is the operating system of the cloud. It runs Swiggy's production on 10 clusters ([Swiggy Bytes](https://bytes.swiggy.com/how-swiggy-migrated-its-k8s-workload-to-graviton-d2643bbc7871)), it ran Disney+ Hotstar to 25 million concurrent viewers before a redesign for 59 million ([Hotstar](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef)), and Amazon EKS now supports clusters of up to 100,000 nodes for AI training ([AWS, July 2025](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-eks-100000-worker-nodes-per-cluster/)). The platform is still moving fast: v1.37 shipped on 26 August 2026 with 16 features graduating to stable, the widely used Ingress-NGINX controller was retired on 24 March 2026, and Gateway API v1.6 made TCP and UDP routing stable.

AI assistants write manifests and Helm charts well, and fully managed modes (EKS Auto Mode, GKE Autopilot, AKS Automatic) remove much node toil. What remains human is debugging: a pod stuck in `Pending` because of a topology constraint, a `CrashLoopBackOff` caused by a missing secret, DNS timeouts from conntrack exhaustion, or a cluster upgrade that breaks an admission webhook. The CKA exam gives troubleshooting the largest weight, 30% ([Linux Foundation](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)), because that is what the job is.

## Learning outcomes

By the end you can:

1. **Build** small, multi-architecture, signed container images and **explain** what namespaces, cgroups v2 and overlay filesystems do for them.
2. **Explain** every Kubernetes control-plane and node component and **build** a cluster from scratch.
3. **Deploy and operate** stateless and stateful workloads with correct probes, resources, disruption budgets and rollout strategies.
4. **Design** pod networking, Services, NetworkPolicies and Gateway API routing, and **migrate** an Ingress setup to Gateway API.
5. **Secure** a cluster with RBAC, Pod Security Standards, workload identity and encrypted secrets.
6. **Configure** HPA, VPA (including in-place resize), Karpenter or Cluster Autoscaler, and KEDA, and **measure** scale-up time.
7. **Package** applications with Helm 4 and Kustomize and **write** a small operator.
8. **Upgrade** a managed cluster (EKS, GKE or AKS) with zero downtime and **troubleshoot** failures at CKA speed.

## Chapters and lessons

### Chapter 1 · Containers from first principles (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What a container is | Linux namespaces (pid, net, mnt, uts, ipc, user), cgroups v2 limits, overlayfs layers; a container is a process | Create a "container" with `unshare` and `cgcreate`, no Docker |
| 1.2 Images and the OCI | OCI image, runtime and distribution specs; layers and digests; tags versus digests; containerd 2.x and runc | Inspect an image manifest with `crane` or `skopeo` and pull by digest |
| 1.3 Building well | BuildKit, multi-stage builds, distroless and minimal bases, layer caching, `.dockerignore`, non-root users | Shrink a Python image from ~1 GB to under 100 MB |
| 1.4 Multi-arch and supply chain | `buildx` for amd64 and arm64, SBOMs with Syft, signing with Sigstore `cosign`, vulnerability scanning with Trivy | Publish a signed multi-arch image and verify the signature |
| 1.5 Registries | ECR, Artifact Registry, ACR; immutable tags, lifecycle policies, pull-through caches | Configure a lifecycle rule that keeps the last 10 tags |

**Check your understanding:** (1) Why does a container started as root inside a user namespace not have root on the host? (2) What can go wrong when you deploy by tag instead of digest? (3) Why does layer order change build time?

### Chapter 2 · Kubernetes architecture (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The declarative API | Objects, spec and status, controllers and reconciliation loops, level-triggered design | Watch a Deployment controller fix a deleted pod with `kubectl get -w` |
| 2.2 Control plane | API server, etcd (Raft), scheduler, controller manager, cloud controller manager; admission chain | Lab 2: Kubernetes the Hard Way (or `kubeadm`) on three VMs |
| 2.3 Nodes | kubelet, container runtime (CRI), kube-proxy (iptables, IPVS, nftables), CNI and CSI plugins | Trace a pod start through kubelet logs |
| 2.4 Versions and skew | Release cadence (three a year; v1.34–v1.37 supported in October 2026), version-skew policy, deprecations and API removals | List deprecated APIs in a sample manifest set with `kubectl convert` or `pluto` |

**Check your understanding:** (1) What still works for running pods when the API server is down? (2) Why must etcd have an odd number of members? (3) Why is Kubernetes "level-triggered" and why does that matter for recovery?

### Chapter 3 · Workloads (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Pods | Init containers, native sidecar containers (stable since v1.33), shared network and volumes, restart policies | Add a log-shipping sidecar and show it starts before and stops after the app |
| 3.2 Deployments and rollouts | ReplicaSets, `maxSurge`/`maxUnavailable`, rollbacks, revision history | Roll out a bad image and roll back in under a minute |
| 3.3 Health and resources | Liveness, readiness and startup probes; requests and limits; QoS classes; OOMKilled | Cause and fix an OOM kill and a probe-induced restart loop |
| 3.4 StatefulSets, DaemonSets, Jobs | Stable identities, ordered rollout, per-node agents, Jobs with completions and back-off, CronJobs | Run a 3-replica StatefulSet and kill a member |
| 3.5 Disruption | PodDisruptionBudgets, graceful termination, `preStop` hooks, draining nodes | Drain a node during load and prove zero failed requests |

**Check your understanding:** (1) Why can a liveness probe make an outage worse? (2) What QoS class does a pod with requests but no limits get, and what happens under memory pressure? (3) Why does a PDB of `minAvailable: 100%` block upgrades?

### Chapter 4 · Scheduling (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The scheduler | Filtering and scoring, requests (not usage) as the basis, `Pending` reasons | Read scheduler events for five pending pods and fix each |
| 4.2 Placement controls | Node selectors, node and pod affinity/anti-affinity, taints and tolerations | Dedicate a node pool to a workload with taints |
| 4.3 Topology spread | `topologySpreadConstraints` across zones and nodes, `maxSkew`, `whenUnsatisfiable` | Spread 9 replicas evenly over three zones |
| 4.4 Priority and devices | PriorityClasses and preemption; Dynamic Resource Allocation (core stable since v1.34) for GPUs; gang scheduling with the Workload and PodGroup APIs (beta in v1.37) | Request a device through a `ResourceClaim` on a kind cluster with a test driver |

**Check your understanding:** (1) Why can a cluster with 40% free CPU still leave pods pending? (2) What does `maxSkew: 1` cost during a zone outage? (3) Why do distributed training jobs need all-or-nothing scheduling?

### Chapter 5 · Networking (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The pod network model | Every pod gets an IP, no NAT between pods; overlay versus routed CNIs; AWS VPC CNI, Azure CNI, GKE dataplane v2 and Cilium (eBPF) | Capture traffic between two pods on different nodes with `tcpdump` |
| 5.2 Services and DNS | ClusterIP, NodePort, LoadBalancer, headless; EndpointSlices; kube-proxy modes; CoreDNS and `ndots` | Fix a slow-DNS problem caused by `ndots: 5` |
| 5.3 NetworkPolicy | Default deny, namespace and pod selectors, egress control, policy engines (Cilium) | Lock a namespace to only the traffic it needs and prove a blocked path |
| 5.4 From Ingress to Gateway API | Why Ingress-NGINX was retired (24 March 2026); Gateway API roles (GatewayClass, Gateway, HTTPRoute, GRPCRoute, and TCPRoute/UDPRoute stable in v1.6); `ingress2gateway` | Migrate an Ingress with path rewrites to Gateway API and compare behaviour |
| 5.5 Traffic management | Canary and header-based routing in HTTPRoute, timeouts, retries; when a service mesh is worth it | Run a 90/10 canary with HTTPRoute weights |

**Check your understanding:** (1) Why did Kubernetes recommend migrating instead of finding another Ingress-NGINX maintainer? (2) What happens to existing connections when an Endpoint is removed? (3) Why is a NetworkPolicy ignored on some clusters?

### Chapter 6 · Configuration, secrets and access (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 ConfigMaps and Secrets | Mounting versus env vars, reload behaviour, why base64 is not encryption, encryption at rest with a KMS provider | Show a secret in plain text in etcd, then enable KMS encryption |
| 6.2 External secrets | External Secrets Operator or provider CSI drivers pulling from AWS Secrets Manager, Key Vault or Secret Manager | Sync a secret and rotate it without restarting pods |
| 6.3 RBAC | Roles, ClusterRoles, bindings, ServiceAccounts, `kubectl auth can-i`, aggregated roles | Give a CI service account deploy-only rights to one namespace |
| 6.4 Workload identity | EKS Pod Identity and IRSA, GKE Workload Identity Federation, Azure Workload Identity; Pod Certificates (stable in v1.37) | Give a pod read access to one bucket with no static keys |
| 6.5 Admission | Pod Security Standards (privileged, baseline, restricted), ValidatingAdmissionPolicy with CEL, Kyverno or Gatekeeper | Block privileged pods and images from unknown registries |

**Check your understanding:** (1) Who can read every secret in a namespace? (2) Why prefer workload identity over a mounted access key? (3) What breaks if an admission webhook is down and `failurePolicy: Fail`?

### Chapter 7 · Storage (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Volumes and claims | PersistentVolumes, PersistentVolumeClaims, StorageClasses, dynamic provisioning, reclaim policies | Provision a gp3/Hyperdisk/Premium SSD volume through a claim |
| 7.2 CSI and topology | CSI drivers, `WaitForFirstConsumer`, zonal disks and why a pod cannot follow its volume to another zone | Reproduce and fix a pod stuck because its volume is in another zone |
| 7.3 Snapshots and backup | VolumeSnapshots, Velero, application-consistent backups | Back up and restore a namespace with Velero |
| 7.4 Databases on Kubernetes | Operators such as CloudNativePG; when a managed database is the better choice (see CLD305) | Run a 3-instance Postgres with CloudNativePG and fail over the primary |

**Check your understanding:** (1) Why does `ReadWriteOnce` not mean "one pod"? (2) When is running Postgres on Kubernetes a reasonable choice? (3) What does a crash-consistent snapshot miss?

### Chapter 8 · Autoscaling (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 HPA | `autoscaling/v2`, CPU, memory, custom and external metrics, stabilisation windows; metrics API v1 (stable in v1.37) | Scale on requests per second from Prometheus |
| 8.2 VPA and in-place resize | Recommendation versus auto modes; in-place pod resize (stable since v1.35) | Resize a running pod's CPU without a restart |
| 8.3 Node autoscaling | Cluster Autoscaler versus Karpenter (NodePools, consolidation, Spot diversification) | Measure time from pending pod to running pod with each |
| 8.4 Event-driven and to zero | KEDA scalers for queues and cron; scale-to-zero trade-offs | Scale a worker from 0 to 50 on queue depth and back |

**Check your understanding:** (1) Why can HPA and VPA fight each other? (2) What does Karpenter consolidation risk for long-running jobs? (3) Why is scale-up time a design input, not a tuning detail?

### Chapter 9 · Packaging and extending (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Helm 4 | Charts, values, templates, server-side apply and kstatus-based waiting (Helm 4, November 2025), chart signing | Write a chart with a values schema and lint it |
| 9.2 Kustomize | Bases and overlays, patches, generators; when to use Kustomize over Helm | Produce dev and prod overlays without templating |
| 9.3 CRDs and operators | Custom resources, controllers, the operator pattern, Kubebuilder and controller-runtime | Lab 9: a small operator that creates a Deployment and Service from a custom `WebApp` resource |
| 9.4 Choosing operators | Evaluating community operators (maturity, upgrade path, failure modes) | Write an adoption review of one operator |

**Check your understanding:** (1) Why do CRD schema changes need versioning? (2) What happens if your operator crashes mid-reconcile? (3) When is a Helm chart the wrong abstraction?

### Chapter 10 · Managed Kubernetes and upgrades (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 EKS, GKE and AKS | Control-plane responsibility, node options, EKS Auto Mode, GKE Autopilot, AKS Automatic (generally available October 2025); pricing models | Create the same small cluster on two providers with IaC |
| 10.2 Version support | Standard and extended support windows, forced upgrades, add-on compatibility | Build an upgrade calendar for the next 18 months |
| 10.3 Zero-downtime upgrades | Control plane first, surge node pools or blue/green node groups, PDBs, deprecated API checks | Upgrade a cluster one minor version under load with zero failed requests |
| 10.4 Many clusters | Why companies run several clusters (blast radius, regions, compliance), fleet tooling, cluster API | Design the cluster topology for a company in Mumbai and Hyderabad |

**Check your understanding:** (1) What does a fully managed mode take away from you, and when does that hurt? (2) Why upgrade every release instead of every two years? (3) When is one big cluster riskier than five small ones?

### Chapter 11 · Troubleshooting at CKA speed (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 A method | Events, describe, logs, `kubectl debug` with ephemeral containers, node-level checks (`crictl`, `journalctl`) | 20 timed break-fix scenarios (no AI) |
| 11.2 Control-plane failures | Expired certificates, broken static-pod manifests, etcd backup and restore | Restore etcd from a snapshot on a kubeadm cluster |
| 11.3 Networking failures | DNS, CNI misconfiguration, NetworkPolicy blocks, Service selector mismatches, conntrack limits | Find five planted network faults in 60 minutes |
| 11.4 Exam technique | CKA domains (troubleshooting 30%, cluster architecture 25%, services and networking 20%, workloads 15%, storage 10%), imperative commands, `kubectl explain` | Two full killer.sh-style mock exams |

**Check your understanding:** (1) What is the first command you run for a `Pending` pod, and why? (2) How do you debug a distroless container with no shell? (3) What evidence tells you a problem is DNS?

### Chapter 12 · AI and Kubernetes operations (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Assistants for manifests | Generating manifests and charts; checking against the API version, Pod Security Standards and your policies | Generate 10 manifests and run `kubeconform`, policy checks and a dry-run |
| 12.2 Agents for diagnosis | Incident agents (AWS DevOps Agent, Gemini Cloud Assist investigations, Azure Copilot troubleshooting agent) reading cluster state; read-only RBAC for agents | Give an agent read-only access and compare its diagnosis with yours on three faults |
| 12.3 AI workloads on Kubernetes | Preview of CLD404: GPU nodes, DRA, gang scheduling, the CNCF Kubernetes AI Conformance programme | Run a small model server on a GPU node pool or CPU fallback |

**Check your understanding:** (1) Why should a diagnosis agent never hold `delete` rights? (2) What must you check in a generated manifest before applying it? (3) What does AI conformance promise a buyer?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: container by hand, then a signed multi-arch image | Image under 100 MB, signed |
| 2 | 2 | Lab 2: cluster from scratch | Working 3-node cluster |
| 3 | 3 | Lab 3: rollouts, probes, PDBs | Zero-failure drain; P1 starts |
| 4 | 4 | Lab 4: scheduling puzzles | Five pending pods fixed; P1 due |
| 5 | 5 | Lab 5: CNI, Services, DNS | DNS fix write-up |
| 6 | 5 | Lab 6: NetworkPolicy and Gateway API migration | Canary via HTTPRoute; P2 starts |
| 7 | 6 | Lab 7: RBAC, workload identity, admission | Keyless bucket access |
| 8 | 7 | Lab 8: storage, Velero, CloudNativePG | Restore evidence |
| 9 | 8 | Autoscaling measurements | Scale-up timing table; P2 due |
| 10 | 9 | Lab 9: operator | Working `WebApp` operator |
| 11 | 10 | Managed cluster upgrade | Zero-failure upgrade; P3 starts |
| 12 | 11 | Break-fix drills | 20 scenarios timed |
| 13 | 11 | Mock CKA exams | Two scores |
| 14 | 12 | P3 completion | Demo and runbook |
| 15 | Review and exam | — | Practical exam and oral |

## Working with AI in this course

- **Use AI for:** first drafts of manifests, Helm templates and Kustomize overlays; explaining unfamiliar fields (then confirming with `kubectl explain`); summarising long event and log output; generating load-test scripts; scaffolding operator code with Kubebuilder. Named tools: Claude Code, GitHub Copilot, `kubectl-ai`, K8sGPT, Gemini Cloud Assist, AWS DevOps Agent.
- **Do without AI (drills):** all break-fix scenarios in Chapter 11, the mock CKA exams (AI is not allowed in the real exam), building a cluster from scratch, and writing NetworkPolicies from a traffic matrix.
- **Verify AI output by:** `kubectl apply --dry-run=server`, `kubeconform` against your cluster version, Pod Security admission in `restricted` mode, your Kyverno or CEL policies, and a load test before and after.
- **Where AI still fails here (show it):** generated manifests often use removed API versions, omit resource requests, run as root, or still target Ingress-NGINX annotations after its retirement. Ask an assistant to diagnose a `Pending` pod from partial output and count how often it guesses instead of asking for `kubectl describe`. Record the results in your P3 report.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Practical exam (CKA-style, 2 hours, no AI) | 25% |
| Oral (architecture and upgrade plan) | 5% |

**Mastery gate:** you pass when you can, without AI help, (a) score at least 75% on a 2-hour CKA-style practical with 17 tasks (the real exam's pass mark is 66%); (b) restore a cluster from an etcd snapshot and fix a broken kubelet within 20 minutes; and (c) upgrade a managed cluster one minor version under load with zero failed requests, showing the evidence.

## Industry reality

Managed Kubernetes is standard in Indian product companies: Zerodha moved services from VMs to Kubernetes on AWS from 2020 ([CNCF](https://www.cncf.io/case-studies/zerodha/)); Swiggy runs 10 clusters and reported Graviton nodes 10% cheaper than comparable x86 ([Swiggy Bytes](https://bytes.swiggy.com/how-swiggy-migrated-its-k8s-workload-to-graviton-d2643bbc7871)). At the top end, AWS reports Karpenter launching 100,000 EC2 instances in about 50 minutes in ultra-scale EKS testing ([AWS](https://aws.amazon.com/blogs/containers/under-the-hood-amazon-eks-ultra-scale-clusters/)). Kubernetes-related CNCF certifications (KCNA, KCSA, CKA, CKAD, CKS) remain the most recognised proof of hands-on skill.

Interview questions from this course:

1. **"A pod is stuck in `Pending`. Walk me through it."** Cover `kubectl describe` events, insufficient requests versus capacity, taints, affinity, topology spread, PVC zone binding, quotas, and node autoscaler behaviour.
2. **"What happens, step by step, when you run `kubectl apply` for a Deployment?"** Cover authentication, authorisation, admission (mutating, validating), etcd write, Deployment and ReplicaSet controllers, scheduler binding, kubelet, CRI, CNI, probes and Endpoints.
3. **"How would you upgrade a production cluster with no downtime?"** Cover deprecated API checks, control plane first, add-on compatibility, surge or blue/green node pools, PDBs, monitoring, and rollback limits.
4. **"How do pods get cloud credentials safely?"** Cover workload identity (IRSA, EKS Pod Identity, GKE and Azure workload identity), token projection, least-privilege roles, and why static keys in Secrets are a risk.
5. **"Ingress-NGINX is retired. What is your migration plan?"** Cover inventory of annotations, Gateway API concepts, choosing an implementation, `ingress2gateway`, behaviour differences, canary migration and rollback.

## Resources (free first)

- **Official:** [Kubernetes documentation](https://kubernetes.io/docs/home/), [Kubernetes releases](https://kubernetes.io/releases/), [Gateway API](https://gateway-api.sigs.k8s.io/), [Helm](https://helm.sh/docs/), [Kustomize](https://kubectl.docs.kubernetes.io/references/kustomize/), [Kubebuilder book](https://book.kubebuilder.io/), [Karpenter](https://karpenter.sh/docs/), [KEDA](https://keda.sh/docs/).
- **Hands-on:** [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way), [Killercoda](https://killercoda.com/) free scenarios, [EKS Best Practices Guides](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html), [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs), [AKS documentation](https://learn.microsoft.com/en-us/azure/aks/).
- **Exam:** [CKA curriculum and details](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/) (Kubernetes v1.35, 2 hours, two killer.sh sessions included).
- **Papers:** [Borg, Omega, and Kubernetes](https://queue.acm.org/detail.cfm?id=2898444) (ACM Queue, 2016); [Large-scale cluster management at Google with Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/) (EuroSys 2015).
- **Practising without a big bill:** do Chapters 1–9 and 11 on local clusters: [kind](https://kind.sigs.k8s.io/) (v0.33), [k3d](https://k3d.io/) (v5.9) or [minikube](https://minikube.sigs.k8s.io/) (v1.39), which need no cloud account. Use Google Cloud's Free Tier, which covers the cluster fee for one Autopilot or zonal cluster a month (nodes are still charged), for Chapter 10, and delete clusters and their load balancers and disks immediately after each session.
- **Paid, worth it:** *Kubernetes in Action*, 2nd edition (Marko Lukša, Manning).

## Sources

All checked 12 Oct 2026.
- [Kubernetes releases](https://kubernetes.io/releases/) (1.34–1.37 supported) and [Kubernetes v1.37 release](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/) (26 Aug 2026).
- [Sidecar containers stable in v1.33](https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/); [DRA GA in v1.34](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/); [in-place pod resize stable in v1.35](https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/).
- [Ingress-NGINX retirement](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/) (announced 11 Nov 2025) and [Ingress2Gateway 1.0](https://kubernetes.io/blog/2026/03/20/ingress2gateway-1-0-release/).
- [Gateway API v1.6](https://kubernetes.io/blog/2026/08/03/gateway-api-v1-6-release/) (released 30 Jun 2026).
- [Helm 4 released](https://helm.sh/blog/helm-4-released) (12 Nov 2025).
- [EKS 100,000 nodes](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-eks-100000-worker-nodes-per-cluster/) and [ultra-scale clusters deep dive](https://aws.amazon.com/blogs/containers/under-the-hood-amazon-eks-ultra-scale-clusters/).
- [InfoQ on AKS Automatic GA](https://www.infoq.com/news/2025/10/microsoft-kubernetes-automatic) (Oct 2025).
- [CKA exam page](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/).
- [Swiggy Graviton migration](https://bytes.swiggy.com/how-swiggy-migrated-its-k8s-workload-to-graviton-d2643bbc7871); [Disney+ Hotstar scaling, part 1](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef); [CNCF Zerodha case study](https://www.cncf.io/case-studies/zerodha/).
- [CNCF Kubernetes AI Conformance](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/) (11 Nov 2025).
- [Google Cloud Free Tier](https://docs.cloud.google.com/free/docs/free-cloud-features); tool versions from GitHub releases on 12 Oct 2026 (kind 0.33.0, k3d 5.9.0, minikube 1.39.0, Helm 4.3.0, Karpenter 1.15.0, KEDA 2.21.0).

_Last reviewed: 2026-10_
