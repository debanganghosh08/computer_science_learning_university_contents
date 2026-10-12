# CS215 · Labs and projects

Use one cloud provider for the whole course; the examples use AWS, but Google Cloud or Azure work with the same criteria. **Before any cloud lab, set a budget alarm** and tag everything you create, and destroy what you no longer need. Every lab that touches the cloud ends with `destroy` and a screenshot of an empty resource list. Labs 2, 6 and 7 are done without AI assistance.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Virtualization | Run a VM, measure boot time and memory overhead; summarize Firecracker's design choices | Measurements and a half-page summary | 3 h |
| 2 · Container from scratch | Isolate a process with `unshare` (PID, mount, network, UTS namespaces) and `chroot`; limit memory with cgroups v2 | Script, host-side `ps`/`ip` evidence, and an OOM-kill demonstration | 4 h |
| 3 · Dockerfile clinic | Take a provided 1 GB image to under 200 MB with multi-stage builds, a non-root user and no critical Trivy findings | Before-and-after sizes, scan reports, and the Dockerfile with comments | 4 h |
| 4 · CI/CD pipeline | GitHub Actions with lint, tests, a build-once artifact, caching, a scan gate, a canary deploy with automatic rollback, SHA-pinned actions and minimal `permissions:` | Workflow files, timings before and after caching, and a rollback demo log | 8 h |
| 5 · Core cloud services | Budget alarm first; the same API on a VM, a function and a serverless container; a static site on object storage with a CDN | A comparison table (cold start, p95 latency, cost estimate) and a teardown proof | 5 h |
| 6 · VPC and debugging | Two-AZ VPC, public and private subnets, NAT, load balancer; then fix three faults the instructor injects | Network diagram, rules, and a written debug log for each fault | 5 h |
| 7 · IAM | Keyless deployment from Actions via OIDC; reduce a wildcard policy to least privilege and prove the app still works | Trust policy, final policy, analyzer output, and a test run | 4 h |
| 8 · Infrastructure as code | The Lab 6 network and the Lab 5 app in Terraform or OpenTofu, with remote locked state, modules, `test`, Checkov and Infracost in PR checks | Repository, a PR that fails policy, a PR that passes, and a drift-detection demo | 10 h |
| 9 · Kubernetes | Run the app on kind or k3s with probes, requests and limits, an HPA and a rolling update; reproduce and fix a readiness-probe outage | Manifests, an autoscaling graph under load, and an outage note | 6 h |
| 10 · Observability | OpenTelemetry traces, Prometheus metrics, a Grafana RED dashboard, one SLO with a burn-rate alert | Dashboard export, alert rule, and an injected-failure alert timeline | 5 h |

## Projects

### P1 · Containerize, test and ship a three-tier app (L1, ~6 hours)

**Real-world inspiration:** the [Twelve-Factor App](https://12factor.net/) principles and Docker's [build best practices](https://docs.docker.com/build/building/best-practices/), which most container platforms assume.

**What to build:** an API, a PostgreSQL database and a small frontend, containerized with multi-stage builds, run locally with Compose, and built, tested, scanned and pushed to GitHub Container Registry by a CI workflow.

**Acceptance criteria:**
- **Image:** the API image is under 150 MB (or the size is justified), runs as non-root and has a health check.
- **Local start:** on a clean machine, `docker compose up` brings all services to healthy in under 60 seconds.
- **CI speed:** CI runs in under 10 minutes, with caching proven by before-and-after timings.
- **Scanning:** the final image has no critical Trivy findings, or each one is documented as accepted.
- **Workflow security:** every third-party action is pinned to a full commit SHA, and the workflow declares minimal `permissions:`.
- **Configuration:** comes only from environment variables, with no secrets in images or in the repository (a secret scan passes).

**Stretch goals:** multi-architecture images (amd64 and arm64); a signed image with Sigstore; integration tests that run against the Compose stack in CI.

**What it proves to an employer:** you can take an app from a laptop to a reproducible, scanned, automatically built artifact. That is the first task in almost every backend, DevOps and cloud role.

### P2 · A cloud service built entirely from code (L2, ~15 hours)

**Real-world inspiration:** platform teams expect every environment to be reproducible from code, with deployments that need no stored cloud keys. GitHub documents OIDC federation for exactly this ([GitHub docs](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)). The 2017 GitLab and 2022 Atlassian post-mortems show what manual, unrehearsed operations cost.

**What to build:** with Terraform or OpenTofu modules, provision:
- a VPC with public and private subnets;
- the P1 API on a VM or serverless container service;
- PostgreSQL in a private subnet (managed or self-run);
- an HTTPS load balancer;
- least-privilege IAM roles;
- a budget alarm.

Pull requests show `plan` output as a comment, and merging applies after a manual approval, authenticated by OIDC. Instrument the service with OpenTelemetry, build a dashboard, and define one SLO with an alert.

**Acceptance criteria:**
- **Rebuild from zero:** `destroy` followed by `apply` rebuilds everything from scratch in under 20 minutes, with zero console steps (screen recording).
- **No static credentials:** none exist anywhere. A secret scan of the repository and its CI history passes.
- **Policy and tagging:** Checkov shows no high-severity findings, or a written exception exists for each. Every resource is tagged with owner, environment and cost centre.
- **Cost:** the Infracost estimate fits inside your free tier or credits, and a test proves the budget alert fires at 50%.
- **Alerting:** the dashboard shows p95 latency and error rate. An injected failure triggers the SLO alert within 5 minutes.
- **README:** an architecture diagram and a "how to rebuild from nothing" section that a classmate follows successfully.

**Stretch goals:** a second environment from the same modules; `tofu test` or `terraform test` for module contracts; scheduled drift detection that opens an issue.

**What it proves to an employer:** you can run real infrastructure the way modern teams do (declaratively, keylessly, observably and within budget), not by clicking in a console.

### P3 · Flash-sale-ready platform with canaries, autoscaling and a game day (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Indian e-commerce sale days and ticket-booking openings bring sudden traffic spikes far above normal (*illustrative scenario*; design to the numbers below, not to any company's private figures). Regulated services in India must also respect data-location and log-retention rules: the RBI's [payment data directive](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244) and CERT-In's [180-day log rule](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf).

**What to build:**
- one or two containerized services on Kubernetes (managed with credits, or k3s on a VM);
- infrastructure entirely as code;
- delivery through a pipeline or GitOps (Argo CD) with canary releases and automated rollback driven by SLO burn;
- Horizontal Pod Autoscaling;
- OpenTelemetry, Prometheus and Grafana;
- a k6 or Locust load test;
- runbooks;
- a game day with a written post-mortem;
- a cost report with FinOps recommendations;
- a design-document section on data residency and log retention.

**Acceptance criteria:**
- **Load:** sustain 10× baseline request rate for 15 minutes with p95 latency under 300 ms and an error rate under 0.5%, with a graph showing autoscaling.
- **Bad release:** a deliberately faulty release is rolled back automatically within 10 minutes, with no human action, while user-facing errors stay under 1%.
- **Game day:** kill a node and fail the database primary (or simulate it), measure time to recover, and publish a blameless post-mortem with timeline, contributing factors and action items.
- **Logs:** retention matches your written policy, including a 180-day class for security-relevant logs, with its monthly cost calculated.
- **Rebuild:** the full environment is built from zero in under 45 minutes with no console clicks.
- **Cost:** reported per million requests, plus three optimizations with measured before-and-after savings.
- **Security:** no long-lived credentials; signed images verified before deploy; least-privilege service accounts.

**Stretch goals:** multi-AZ database failover; a scheduled chaos experiment; admission-control policies (OPA Gatekeeper or Kyverno); an AI-generated incident summary compared line by line with your own post-mortem, listing what it missed.

**What it proves to an employer:** you can run a production-shaped system end to end (deploy, scale, fail, recover, explain, and pay for it), with evidence. That is the core of cloud, DevOps and SRE roles.

## Feeds into

- [CLD301 Cloud Architecture](../../../03_majors/cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md), [CLD302 Infrastructure as Code](../../../03_majors/cloud_engineering/year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md), [CLD303 Containers and Kubernetes](../../../03_majors/cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md), [CLD304 Cloud Networking](../../../03_majors/cloud_engineering/year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md).
- [OPS301 CI/CD Engineering](../../../03_majors/devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md), [OPS303 Observability](../../../03_majors/devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md), [OPS304 Site Reliability Engineering](../../../03_majors/devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md), [OPS305 Configuration Management and GitOps](../../../03_majors/devops_sre_platform_engineering/year_3/OPS305_configuration_management_and_gitops/README.md).
- [CLD403 FinOps and Cloud Cost Engineering](../../../03_majors/cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md): Chapter 11 and P3's cost report.
- Overlaps: [OV01A Cloud Security Posture, Detection and Response](../../../04_overlaps/OV01_cloud_security/OV01A_cloud_security_posture_detection_and_response/README.md), [OV03A Software Supply Chain Security](../../../04_overlaps/OV03_devsecops/OV03A_software_supply_chain_security/README.md), [OV04A ML Platform Engineering](../../../04_overlaps/OV04_mlops_ml_platform/OV04A_ml_platform_engineering/README.md).
