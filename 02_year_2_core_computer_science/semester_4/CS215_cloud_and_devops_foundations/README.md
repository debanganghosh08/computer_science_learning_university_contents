# CS215 · Cloud and DevOps Foundations

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 4 | 4 (≈ 120 hours) | L1 → L3 | [CS203](../../semester_3/CS203_operating_systems/README.md), [CS204](../../semester_3/CS204_computer_networks/README.md), [FND104](../../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) | [CLD301](../../../03_majors/cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md), [CLD302](../../../03_majors/cloud_engineering/year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md), [CLD303](../../../03_majors/cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md), [OPS301](../../../03_majors/devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md), [OPS303](../../../03_majors/devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md), [OPS304](../../../03_majors/devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md) |

Part of [Year 2 · Core Computer Science](../../README.md). It turns the OS and networking of [CS203](../../semester_3/CS203_operating_systems/README.md) and [CS204](../../semester_3/CS204_computer_networks/README.md) into running infrastructure, and gives [CS212](../CS212_distributed_systems_i/README.md)'s systems a place to live.

## Why this course matters now

Most software now ships as containers through automated pipelines onto rented infrastructure defined in code. The tools move fast:

- **Free tiers:** AWS reworked its free tier in July 2025 (new accounts get $100 in credits, up to $100 more for exploring services, and a 6-month free plan). Google Cloud offers $300 for 90 days plus an always-free `e2-micro` VM.
- **Infrastructure as code:** HashiCorp moved Terraform to the Business Source License in August 2023, and the community forked it as OpenTofu.
- **Kubernetes:** reached 1.37 in August 2026.

AI agents now write Dockerfiles, Terraform modules and pipeline YAML, and some open pull requests on their own (GitHub Copilot coding agent). The 2025 DORA report found that AI acts as an *amplifier*, magnifying an organization's existing strengths and weaknesses. A team that cannot read a `plan`, reason about IAM, or debug a VPC route will simply ship its mistakes faster. The costly failures are still human-scale. Capital One paid an $80 million penalty in 2020 after US regulators found it had not assessed risk properly before moving to the cloud. A compromised GitHub Action leaked CI secrets in March 2025. This course builds the judgement to prevent both.

## Learning outcomes

By the end you can:

1. **Explain** how hypervisors, microVMs and containers isolate workloads, and **build** a minimal container from Linux namespaces and cgroups.
2. **Write** production-grade Dockerfiles (multi-stage, non-root, small, scanned) and **run** multi-service environments with Compose.
3. **Build** CI/CD pipelines with tests, caching, scanning, immutable artifacts and progressive delivery, and **measure** them with the four DORA metrics.
4. **Deploy** an application on one cloud's core services (compute, storage, managed database, networking, DNS, CDN) using a free tier with budget alarms.
5. **Design** a VPC with public and private subnets, and **debug** connectivity layer by layer.
6. **Write** least-privilege IAM policies, use short-lived credentials (OIDC federation), and **audit** effective permissions.
7. **Provision** everything with Terraform or OpenTofu (modules, remote state, locking, tests, policy checks) and **review** a plan for risk.
8. **Run** a small Kubernetes workload with probes, limits and autoscaling.
9. **Instrument** a service with OpenTelemetry, **define** SLOs and alerts, and **write** a blameless post-mortem.
10. **Estimate and reduce** cloud cost, and **account for** Indian rules on data and log location.

## Chapters and lessons

### Chapter 1 · From servers to cloud (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Virtualization | Type 1 vs type 2 hypervisors, hardware virtualization (VT-x, AMD-V), KVM, paravirtual I/O | Run a VM with KVM/QEMU or VirtualBox and measure boot time and memory overhead |
| 1.2 MicroVMs | Firecracker (NSDI 2020): minimal device model for serverless density | Read the Firecracker paper's design section and list what it removed and why |
| 1.3 Service models | IaaS, PaaS, SaaS, FaaS, containers-as-a-service; regions and availability zones | Classify ten real services by model |
| 1.4 Shared responsibility | What the provider secures vs what you secure, by service model | Fill a responsibility matrix for a VM, a managed database and a function |

**Check your understanding:** (1) Why can a microVM start faster than a general-purpose VM? (2) In a managed database, who patches the OS, and who sets the firewall rules? (3) Why do providers expose availability zones to you instead of hiding them?

### Chapter 2 · Containers from first principles (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Namespaces | PID, mount, network, UTS, IPC, user namespaces | Build a "container" with `unshare` and `chroot`, then inspect it from the host |
| 2.2 cgroups v2 | CPU, memory and I/O limits; OOM behaviour | Limit a process to 100 MB and watch the OOM killer act |
| 2.3 Images and layers | OverlayFS, content-addressed layers, OCI image and runtime specs, `runc` | Unpack an OCI image by hand and list its layers |
| 2.4 Isolation strength | Shared kernel risk; gVisor and microVM sandboxes; rootless containers | Compare the attack surface of a container, gVisor and a microVM in a table |

**Check your understanding:** (1) Why is a container "just a process"? (2) Why can't a container run a different kernel? (3) When would you choose gVisor or Firecracker over plain containers?

### Chapter 3 · Docker in practice (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Dockerfiles that hold up | Layer caching, ordering, `.dockerignore`, multi-stage builds, distroless and slim bases | Shrink a Python API image by 80% and keep it working |
| 3.2 Secure images | Non-root users, read-only filesystems, no secrets in layers, scanning with Trivy | Scan, fix and rescan an image until no critical findings remain |
| 3.3 Compose for local environments | Services, networks, volumes, health checks, dependency ordering | Run API + PostgreSQL + Redis with one command |
| 3.4 The ecosystem | Docker Engine vs Docker Desktop (free for small businesses under 250 employees and $10M revenue, personal use and education), Podman, registries (GHCR) | Push a tagged image to GitHub Container Registry |

**Check your understanding:** (1) Why does putting `COPY . .` before installing dependencies slow every build? (2) Why is deleting a secret in a later layer not enough? (3) What does a health check give an orchestrator that a running process does not?

### Chapter 4 · CI/CD pipelines (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Continuous integration | Trunk-based development, fast tests, branch protection, required checks | Set up CI that runs lint, tests and build on every pull request |
| 4.2 GitHub Actions in depth | Workflows, jobs, runners, caching, matrices, artifacts; free for public repos, 2,000 minutes/month for private repos on the Free plan | Cut a pipeline's run time in half with caching and parallel jobs |
| 4.3 Delivery and deployment | Immutable artifacts, environment promotion, rolling, blue-green and canary deploys, feature flags, rollback | Implement a canary with automatic rollback on error rate |
| 4.4 Measuring delivery | DORA four keys: deployment frequency, lead time for changes, change failure rate, time to restore | Compute the four keys for your own repository's history |
| 4.5 Pipeline security | The March 2025 `tj-actions/changed-files` compromise; pin actions to commit SHAs; least-privilege `permissions:`; OIDC instead of stored cloud keys | Harden a workflow and prove no long-lived secret remains |

**Check your understanding:** (1) Why should the artifact you test be byte-for-byte the one you deploy? (2) Why does a canary need an automated rollback signal? (3) What can an attacker do with a CI token that has write access to the repository?

### Chapter 5 · One cloud's core services (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Account hygiene first | Root account lock-down, MFA, budgets and alerts, free-tier limits, tagging | Create a budget alarm at ₹500 or $5 before anything else |
| 5.2 Compute | VMs (EC2), serverless functions (Lambda), serverless containers; when to use each | Deploy the same API on a VM, a function and a container service; compare cold starts |
| 5.3 Storage and databases | Object storage (S3), block storage, managed PostgreSQL (RDS); durability vs availability; backups | Host a static site on object storage behind a CDN |
| 5.4 Messaging and DNS | Queues (SQS), pub/sub, DNS (Route 53), CDN caching | Decouple an image-resize job with a queue |
| 5.5 Mapping across providers | AWS, Google Cloud and Azure equivalents | Fill a three-provider mapping table for ten services |

**Check your understanding:** (1) Why set budget alarms before launching resources? (2) Why is object storage not a file system? (3) When is a queue better than a direct HTTP call?

### Chapter 6 · Cloud networking (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 VPC design | CIDR planning, public and private subnets, route tables, internet and NAT gateways | Design a two-AZ VPC with non-overlapping ranges for three environments |
| 6.2 Traffic control | Security groups vs network ACLs, stateful vs stateless rules | Write rules that allow only the load balancer to reach the app |
| 6.3 Load balancing and DNS | L4 vs L7 load balancers, health checks, TLS termination, DNS failover | Put an HTTPS load balancer in front of two instances |
| 6.4 Private connectivity and egress | VPC endpoints, peering, egress costs and NAT data charges | Replace NAT traffic to object storage with a VPC endpoint and estimate savings |

**Check your understanding:** (1) An instance in a private subnet cannot reach the internet: list the checks in order. (2) Why are security groups usually preferred over NACLs? (3) Why does data leaving the cloud often cost more than data entering it?

### Chapter 7 · Identity and access management (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Principals and policies | Users, roles, identity-based vs resource-based policies, explicit deny, evaluation logic | Work out effective permissions for five policy combinations by hand |
| 7.2 Temporary credentials | Roles, STS, instance and workload identities; why long-lived keys are a liability | Remove every access key from a project |
| 7.3 Federation for CI | OIDC trust from GitHub Actions to the cloud, scoped by repository and branch | Deploy from Actions with no stored cloud secrets |
| 7.4 Least privilege in practice | Access analyzers, policy simulators, permission boundaries, secrets managers | Tighten a `*` policy to the minimum actions and prove the app still works |

**Check your understanding:** (1) Why does an explicit deny beat any allow? (2) What should an OIDC trust policy pin, and what happens if it doesn't? (3) What did US regulators say Capital One failed to do before its cloud migration?

### Chapter 8 · Infrastructure as code (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Declarative infrastructure | Desired state, providers, resources, dependency graph, `plan`/`apply` | Write the Chapter 6 VPC in Terraform or OpenTofu |
| 8.2 State | State files, remote backends, locking, drift, `import`, secrets in state | Break and repair state on purpose; detect drift after a console change |
| 8.3 Modules and environments | Inputs, outputs, versioned modules, workspaces vs separate state per environment | Refactor into a reusable module used by dev and prod |
| 8.4 Testing and policy | `terraform test` / `tofu test`, Checkov and OPA policies, Infracost cost diffs in pull requests | Fail a PR that opens SSH to the world or raises cost by more than 20% |
| 8.5 Licences and ecosystem | Terraform's BSL 1.1 (2023) vs OpenTofu (open source, CNCF project); Pulumi and CDKs as alternatives | Write a half-page tool-choice record for a startup |

**Check your understanding:** (1) Why must state be locked? (2) What does a `plan` that says "must be replaced" mean for a database? (3) Why review `plan` output, not just the code diff?

### Chapter 9 · Kubernetes essentials (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Why orchestration | Scheduling, self-healing, service discovery; control plane, kubelet, etcd (Raft, from CS212) | Run a cluster with kind or k3s |
| 9.2 Core objects | Pods, Deployments, Services, Ingress, ConfigMaps, Secrets | Deploy the P1 app to the cluster |
| 9.3 Health and resources | Liveness, readiness and startup probes; requests and limits; QoS classes | Show a bad readiness probe causing an outage, then fix it |
| 9.4 Scaling and rollouts | Horizontal Pod Autoscaler, rolling updates, rollbacks | Load-test and watch the autoscaler react |

**Check your understanding:** (1) Why does a readiness probe protect users while a liveness probe protects the pod? (2) What happens to a pod that exceeds its memory limit? (3) Why does Kubernetes need etcd to be consistent?

### Chapter 10 · Observability and reliability (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Signals | Metrics, logs, traces; OpenTelemetry SDKs and collector; Prometheus 3.x; Grafana | Instrument the API with OpenTelemetry and view a trace |
| 10.2 What to measure | RED (rate, errors, duration) and USE (utilization, saturation, errors) methods | Build a RED dashboard for every service |
| 10.3 SLOs and alerting | SLIs, SLOs, error budgets, burn-rate alerts (Google SRE book and workbook) | Define one SLO and a multi-window burn-rate alert |
| 10.4 Incidents and post-mortems | On-call, blameless post-mortems; GitLab's January 2017 database incident, Atlassian's April 2022 outage, AWS's October 2025 event | Write a post-mortem of a failure you inject |
| 10.5 Logging rules in India | CERT-In: keep ICT logs for 180 days within India, sync clocks to NIC or NPL time | Design a log-retention policy and price it |

**Check your understanding:** (1) Why alert on symptoms (users' errors) instead of causes (CPU)? (2) How does an error budget change release decisions? (3) What made GitLab's 2017 backups fail when they were needed?

### Chapter 11 · Cost, data location and the cloud decision (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Pricing models | On-demand, savings plans and reservations, spot; storage tiers; egress and NAT charges | Price one architecture three ways with the AWS Pricing Calculator |
| 11.2 FinOps | Inform, optimize, operate (FinOps Foundation); tagging, showback, anomaly alerts | Tag every resource and produce a cost-by-team report |
| 11.3 Well-architected reviews | The AWS Well-Architected pillars, including cost optimization and sustainability | Run a lightweight review of your P2 deployment |
| 11.4 Data location | RBI's 2018 directive that payment system data be "stored in a system only in India"; DPDP Act duties; choosing regions | Write the region and data-residency section of a design doc for a payments start-up (illustrative) |
| 11.5 Cloud, colocation or both | When self-hosting wins; Zerodha's "common sense" scaling essay as a counterpoint | Write a one-page build-vs-rent analysis for a stated workload |

**Check your understanding:** (1) Why can a NAT gateway be the surprise line item on a bill? (2) When are spot instances the wrong choice? (3) What would change in your architecture if payment data must stay in India?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: VMs and microVM reading | Overhead measurements |
| 2 | 2 | Lab 2: container from scratch | `unshare` container, cgroup limit demo |
| 3 | 3 | Lab 3: Dockerfile clinic | Small, scanned, non-root image; P1 starts |
| 4 | 4 | Lab 4: CI | Pipeline with tests and caching |
| 5 | 4 | Lab 4: CD and hardening | Canary with rollback, hardened workflow; P1 due |
| 6 | 5 | Lab 5: cloud services | Budget alarm, three deploys compared |
| 7 | 6 | Lab 6: VPC | Working two-tier network, debug log |
| 8 | 7 | Lab 7: IAM | Keyless deploy, tightened policy; P2 starts |
| 9 | 8 | Lab 8: IaC | VPC and app as code |
| 10 | 8 | Lab 8: tests and policy | Failing-policy PR demo |
| 11 | 9 | Lab 9: Kubernetes | App on cluster with probes and HPA; P2 due |
| 12 | 10 | Lab 10: observability | Traces, dashboard, SLO alert; P3 design review |
| 13 | 11 | FinOps exercise | Cost report |
| 14 | — | P3 game day | P3 demo, post-mortem, cost report |
| 15 | Review and exam | — | Written exam, live debugging oral |

## Working with AI in this course

- **Use AI for:** drafting Dockerfiles, Terraform modules, Kubernetes manifests and workflow YAML; explaining unfamiliar cloud error messages and IAM policy JSON; summarizing logs and traces during debugging; drafting runbooks and post-mortems. Agentic tools now act directly: GitHub's Copilot coding agent opens pull requests, and HashiCorp's Terraform MCP server gives agents provider documentation. Treat their output as a junior colleague's pull request.
- **Do without AI (drills):** write a Dockerfile and a VPC module from documentation; work out effective IAM permissions by hand; debug a broken private-subnet route under time pressure; estimate a monthly bill on paper; read a 200-line `plan` and mark every risky change.
- **Verify AI output by:**
  - reviewing every `plan` line by line before `apply`;
  - running Checkov or OPA policies and container scans;
  - checking IAM with an access analyzer or policy simulator;
  - running Infracost diffs;
  - applying first in a throwaway account with a budget alarm.
  
  Never paste secrets, state files or customer data into a prompt.
- **Where AI still fails here:** DORA's 2025 research describes AI as an amplifier of existing practices rather than a fix for weak ones. Test it yourself: ask an assistant for "an S3 bucket and IAM policy for my app", then run Checkov and an access analyzer on the result and count the over-broad grants. Generated configuration that looks plausible but over-permissions, references non-existent arguments, or ignores cost is the failure to catch.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 30% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Written exam (networking, IAM evaluation, IaC state, cost) | 20% |
| Live debugging oral | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) rebuild the P2 environment from an empty account using only your code, in under 30 minutes, with no console clicks and no long-lived credentials; (b) fix three faults an examiner plants within 45 minutes (a broken route table, an over- or under-permissive IAM policy, and a failing readiness probe), explaining each diagnosis; and (c) explain a given month's cost report and propose savings with numbers.

## Industry reality

Cloud and DevOps work runs on the stack in this course:

- **Containers and Kubernetes:** Kubernetes 1.37 shipped in August 2026, and its control plane stores state in etcd.
- **Infrastructure as code:** Terraform 1.16 and OpenTofu 1.13 are both current releases.
- **Telemetry:** OpenTelemetry for instrumentation.
- **Delivery metrics:** DORA's metrics to measure delivery.

Public post-mortems from GitLab (2017), Atlassian (2022) and AWS (2025) are standard reading in operations teams. In India, the RBI's payment-data localisation rule and CERT-In's log rules shape region choice and retention design for fintech and any regulated service.

Interview questions from this course:

1. **"Containers vs VMs: what is the actual difference?"** Cover namespaces and cgroups vs hardware virtualization, the shared kernel and its security consequences, startup time and density, and when to sandbox (gVisor, Firecracker).
2. **"Design a CI/CD pipeline for a microservice."** Cover the stages (lint, unit, build once, scan, integration, deploy to staging, canary to production), immutable artifacts, automated rollback, OIDC credentials, SHA-pinned actions, and measuring with DORA metrics.
3. **"What is Terraform state and how do you manage it?"** Cover state's role in mapping config to real resources, remote backends with locking, drift detection, sensitive values in state, import, and splitting state by blast radius.
4. **"A service in a private subnet can't reach a dependency. Debug it."** Work layer by layer: DNS, route tables (NAT or endpoint), security groups in both directions, NACLs, the service's own listener, and verifying with reachability tools and flow logs.
5. **"The cloud bill doubled this month. What do you do?"** Cover breakdown by service and tag, egress and NAT charges, idle and orphaned resources, log volume, autoscaling misconfiguration, immediate containment, and prevention (budgets, anomaly alerts, Infracost in PRs).

## Resources (free first)

- **India course:** NPTEL [Cloud Computing](https://nptel.ac.in/courses/106105167) (Prof. Soumya Kanti Ghosh, IIT Kharagpur).
- **Books and guides:** [Google SRE books](https://sre.google/books/) (free online); [The Twelve-Factor App](https://12factor.net/); [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html); [FinOps Framework](https://www.finops.org/framework/); [DORA research](https://dora.dev/research/2025/dora-report/) and [four keys](https://dora.dev/guides/dora-metrics-four-keys/).
- **Documentation:** [Docker docs](https://docs.docker.com/) and [build best practices](https://docs.docker.com/build/building/best-practices/); [OCI image spec](https://github.com/opencontainers/image-spec) and [runtime spec](https://github.com/opencontainers/runtime-spec); [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html); [OverlayFS](https://www.kernel.org/doc/html/latest/filesystems/overlayfs.html); [Kubernetes docs](https://kubernetes.io/docs/home/); [OpenTofu docs](https://opentofu.org/docs/); [Terraform docs](https://developer.hashicorp.com/terraform/docs); [OpenTelemetry](https://opentelemetry.io/docs/); [Prometheus](https://prometheus.io/docs/introduction/overview/); [GitHub Actions security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) and [OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect); [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).
- **Papers:** [Firecracker (NSDI 2020)](https://www.usenix.org/conference/nsdi20/presentation/agache).
- **Free practice:** [Killercoda](https://killercoda.com/), [Play with Docker](https://labs.play-with-docker.com/), [kind](https://kind.sigs.k8s.io/), [k3s](https://k3s.io/), [LocalStack](https://localstack.cloud/), and provider free tiers ([AWS](https://aws.amazon.com/free/), [Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features), [Azure for Students](https://azure.microsoft.com/en-us/free/students), [Oracle Cloud Always Free](https://www.oracle.com/cloud/free/)).
- **Tools:** [Trivy](https://trivy.dev/), [Checkov](https://www.checkov.io/), [Infracost](https://www.infracost.io/), [k6](https://grafana.com/docs/k6/latest/), [Argo CD](https://argo-cd.readthedocs.io/).

## Sources

All checked 12 Oct 2026.
- [AWS Free Tier](https://aws.amazon.com/free/): $100 sign-up credit, up to $100 more, 6-month free plan.
- [Google Cloud free features](https://docs.cloud.google.com/free/docs/free-cloud-features): $300 for 90 days; `e2-micro` always free in three US regions.
- [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions): free for public repositories; 2,000 minutes/month on Free for private repositories.
- [Docker Desktop licence terms](https://docs.docker.com/subscription/desktop-license/).
- [HashiCorp adopts BSL](https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license) (10 Aug 2023); [OpenTofu at the CNCF](https://www.cncf.io/projects/opentofu/); [Linux Foundation OpenTofu announcement](https://www.linuxfoundation.org/press/announcing-opentofu).
- Release versions (Kubernetes 1.37 on 26 Aug 2026; Terraform 1.16; OpenTofu 1.13; Prometheus 3.15) from [endoflife.date](https://endoflife.date/) and [Kubernetes releases](https://kubernetes.io/releases/).
- [DORA 2025: State of AI-assisted Software Development](https://dora.dev/research/2025/dora-report/): "AI's primary role is as an amplifier".
- [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent); [HashiCorp Terraform MCP server](https://github.com/hashicorp/terraform-mcp-server).
- [OCC penalty against Capital One](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html) (6 Aug 2020).
- [CISA alert on tj-actions/changed-files](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) (Mar 2025).
- Post-mortems: [GitLab, January 2017](https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/); [Atlassian, April 2022](https://www.atlassian.com/engineering/post-incident-review-april-2022-outage); [AWS, October 2025](https://aws.amazon.com/message/101925/).
- [RBI: Storage of Payment System Data](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244) (6 Apr 2018).
- [CERT-In Directions](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) (28 Apr 2022).
- [Zerodha: Scaling with common sense](https://zerodha.tech/blog/scaling-with-common-sense/).

_Last reviewed: 2026-10_
