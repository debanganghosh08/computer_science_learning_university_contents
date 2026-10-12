# CLD303 · Labs and projects

Most labs run on a local [kind](https://kind.sigs.k8s.io/) or [k3d](https://k3d.io/) cluster on your laptop (8 GB RAM is enough for three nodes). Labs that need a managed cluster say so; create those clusters with your CLD302 modules and delete them at the end of each session. The break-fix drills and mock exams are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Containers by hand, then properly | Isolate a process with `unshare` and cgroups v2; then build a multi-stage, non-root, multi-arch image, generate an SBOM and sign it with `cosign` | Shell transcript, image size before and after, `cosign verify` output, Trivy report | 5 h |
| 2 · Cluster from scratch | Kubernetes the Hard Way or `kubeadm` on three VMs (local VMs are fine) | Working cluster, certificate inventory and a diagram of every component and port | 8 h |
| 3 · Rollouts and disruption | Deployment with probes, requests, a PDB and a `preStop` hook; drain a node under load | Load-test output showing zero failed requests during drain and during a bad-image rollback | 4 h |
| 4 · Scheduling puzzles | Five prepared pods stuck in `Pending` (taints, affinity, spread, PVC zone, quota) | Root cause and fix for each, with the event line that revealed it | 3 h |
| 5 · Networking internals | Packet capture across nodes, Service and EndpointSlice inspection, a DNS `ndots` latency fix | Captures, before-and-after DNS latency and an explanation | 4 h |
| 6 · Gateway API migration | Migrate an Ingress-NGINX setup with rewrites and TLS to Gateway API using `ingress2gateway`; add a 90/10 canary | Diff of behaviour (status codes, headers) before and after, and canary traffic split measured | 5 h |
| 7 · Identity and admission | RBAC for a CI service account, workload identity to a cloud bucket (managed cluster), Pod Security `restricted`, a CEL ValidatingAdmissionPolicy | `kubectl auth can-i` matrix, keyless access proof, rejected privileged pod | 5 h |
| 8 · Storage and databases | Dynamic volumes, a zonal-volume failure reproduced and fixed, Velero backup/restore, CloudNativePG failover | Restore timing, failover timing, and data-loss check | 5 h |
| 9 · Write an operator | Kubebuilder operator for a `WebApp` CRD that creates and updates a Deployment, Service and HTTPRoute, with status conditions | Code, tests with envtest, and a demo of self-healing after manual deletion | 8 h |
| 10 · Break-fix drills (no AI) | 20 timed scenarios: broken kubelet, expired certificate, bad static-pod manifest, CNI down, wrong Service selector, NetworkPolicy block, etcd restore | Time per scenario and the fix; repeat until 80% are solved within 6 minutes each | 8 h |

## Projects

### P1 · Production-ready packaging of a real service (L1, ~6 hours)

**Real-world inspiration:** Kubernetes production checklists in the [EKS Best Practices Guides](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html) and GKE documentation: requests, probes, disruption budgets, non-root images.

**What to build:** take an open-source web service (or your own API from earlier courses) and ship it to a kind cluster with a signed multi-arch image, a Helm 4 chart with a values schema, Kustomize overlays for dev and prod, probes, resources, a PDB, an HPA, a NetworkPolicy and an HTTPRoute.

**Acceptance criteria:**
- Image under 150 MB, runs as non-root, zero critical CVEs in Trivy, signature verifies.
- `helm lint` and `kubeconform` pass for Kubernetes v1.37; the pod is admitted under Pod Security `restricted`.
- A rolling update under 200 requests per second produces zero non-2xx responses.
- **Cost ceiling:** US$0 (local only).

**Stretch goals:** chart published to an OCI registry; provenance attestation.

**What it proves to an employer:** you can hand any service to a platform team in a deployable, secure form.

### P2 · Autoscaling that is measured, not guessed (L2, ~15 hours)

**Real-world inspiration:** Disney+ Hotstar's engineers describe not trusting reactive autoscaling for live cricket and pre-scaling before big events ([Hotstar](https://blog.hotstar.com/hotstars-journey-from-ec2-to-containers-86ea4e4880fd)); AWS reports Karpenter launching 100,000 instances in about 50 minutes in ultra-scale tests ([AWS](https://aws.amazon.com/blogs/containers/under-the-hood-amazon-eks-ultra-scale-clusters/)). The traffic pattern is an *illustrative scenario*: a match-day spike from 2,000 to 40,000 requests per second within three minutes.

**What to build:** on a small managed cluster, an API and a queue worker with HPA on requests per second (Prometheus adapter or KEDA), KEDA on queue depth for the worker, VPA in recommendation mode, Karpenter (EKS or AKS) or Cluster Autoscaler (GKE) with a Spot-diversified pool, and a pre-scaling schedule for known events.

**Acceptance criteria:**
- A report with measured times for: pending pod to running on an existing node, new node to ready, and full scale-out from minimum to 10× replicas.
- Under a scaled-down version of the spike (for example 50 → 1,000 requests per second in 3 minutes), p99 latency stays below 500 ms with reactive scaling plus pre-scaling, and you show what happens without pre-scaling.
- Spot interruption of a node during load causes no failed requests (PDBs, graceful termination, diversification).
- Scale-in returns the cluster to its minimum within 15 minutes after load stops, without dropping in-flight queue messages.
- **Cost ceiling:** US$25; run load tests in short windows and delete the cluster after each session.

**Stretch goals:** in-place VPA resizing on the worker; a cost-per-1,000-requests comparison of on-demand and Spot node pools.

**What it proves to an employer:** you can make an elastic system that holds its latency target and prove it with numbers.

### P3 · A small internal platform with an upgrade and a game day (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- Hotstar's move away from two self-managed clusters that could not scale to its next concurrency target ([Hotstar](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef)).
- The retirement of Ingress-NGINX on 24 March 2026, which forced migrations across the industry ([Kubernetes](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)).
- Managed modes such as EKS Auto Mode, GKE Autopilot and AKS Automatic, which shift node operations to the provider.

**What to build:** with IaC, a managed cluster (on one provider) offering a "golden path" to other teams:
- your Lab 9 operator so a team creates a `WebApp` and gets a Deployment, Service, HTTPRoute, HPA, PDB and NetworkPolicy;
- workload identity, External Secrets, Pod Security `restricted` and admission policies;
- Gateway API ingress with TLS, CloudNativePG for a team database, Velero backups;
- a written runbook and an SLO for the platform API.

Then do two exercises:
1. a one-minor-version upgrade of control plane and nodes under load;
2. a game day: a classmate injects three faults without telling you which (examples: delete a CoreDNS pod set, break a NetworkPolicy, fill a node disk, expire a webhook certificate).

**Acceptance criteria:**
- A new team service goes from a 20-line `WebApp` manifest to serving HTTPS traffic in under 5 minutes.
- **Upgrade:** zero failed requests across the upgrade at 100 requests per second, with deprecated-API checks recorded before starting.
- **Game day:** all three faults detected and fixed within 60 minutes total, each with a short blameless post-incident note.
- **Restore:** Velero restores a deleted namespace including its database to a state no older than 15 minutes.
- **AI review:** an assistant-generated version of one platform component, with a table of every defect your checks caught.
- **Cost ceiling:** US$40 total.

**Stretch goals:** the same platform on a second provider using the same operator; DRA-based GPU request path (see CLD404); cost allocation per team using split cost allocation with Kubernetes labels or OpenCost.

**What it proves to an employer:** you can build, run, upgrade and debug Kubernetes for other engineers, which is the core of cloud infrastructure and platform roles.

## Feeds into

- [CLD403 FinOps and Cloud Cost Engineering](../../year_4/CLD403_finops_and_cloud_cost_engineering/README.md): Kubernetes cost allocation and rightsizing build on P2 and P3.
- [CLD404 AI Infrastructure in the Cloud](../../year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md): GPU node pools, DRA and gang scheduling.
- [OV02 Cloud-Native Backend](../../../../04_overlaps/OV02_cloud_native_backend/README.md): with BE301 and BE304.
- [OPS401 Platform Engineering](../../../devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md): P3 grows into an internal developer platform.
