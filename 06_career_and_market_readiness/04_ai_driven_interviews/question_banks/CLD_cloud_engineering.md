# CLD · Cloud Engineering: interview question bank

| Role and market | Levels | Practise with | Score with |
|---|---|---|---|
| [CLD role page](../../01_market_map/roles/CLD_cloud_engineering.md) · [Cloud major](../../../03_majors/cloud_engineering/README.md) | NG → Mid → Sr | [Mock kit](../how_to_run_a_mock_with_any_llm.md) · [Day 5 simulation](../simulation_days.md#5-day-5-cloud-engineer--site-reliability-engineer-mid-level) | [Rubrics](../rubrics.md) |

Cloud interviews reward people who can reason from first principles (packets, permissions, state) through a provider's abstractions. Examples below use AWS names where a provider must be named; Azure and Google Cloud have equivalents, and interviewers accept answers in the provider you know if you map concepts correctly.

## 1. The typical loop

| Round | Duration | What it tests | AI policy you may meet | Mock brief |
|---|---|---|---|---|
| Screen / online assessment | 30–90 min | Linux, networking, one provider's core services; sometimes light DSA | Read the rules; usually AI-off | Kit 4.1 |
| Fundamentals deep dive | 45 min | IAM evaluation, VPC routing, DNS, TLS, Kubernetes internals | AI-off | Kit 4.1 with section 3 questions |
| Hands-on troubleshooting | 45–60 min | A broken environment or cluster | Sometimes documentation allowed; ask | Kit 4.9 |
| Infrastructure-as-code review | 30–45 min | A Terraform change, often with defects | Increasingly framed as reviewing AI-generated IaC | Kit 4.2 review variant |
| Cloud architecture design | 60 min | HA, landing zones, migrations, AI inference platforms, cost and failure modes | AI-off | Kit 4.3 |
| Behavioural | 45 min | Outages, cost overruns, disagreements on architecture | AI-off | Kit 4.11 |

## 2. How to use this bank

Answer aloud with a timer, then open the guide. For hands-on questions, reproduce them in a free-tier or local lab (for example a local Kubernetes cluster) and break things on purpose.

## 3. Questions

### Networking and identity fundamentals

**Q1 · NG · A VM in a private subnet calls an external API. Trace the packet out and back.**

<details><summary>Answer guide</summary>

- **Testing:** VPC routing mental model.
- **Strong answer:** DNS resolution via the VPC resolver; the subnet's route table sends `0.0.0.0/0` to a NAT gateway in a public subnet; the NAT gateway's route table sends traffic to the internet gateway; source address translated to the NAT's public IP; return traffic matched by connection tracking. Security groups (stateful) must allow egress; network ACLs (stateless) must allow both directions including ephemeral ports.
- **Common mistakes:** routing private subnets directly to the internet gateway; forgetting return-path ACL rules.
- **Follow-ups:** reach a cloud storage service without the NAT (gateway or interface endpoints, and their cost difference).
</details>

**Q2 · NG · You changed a DNS record an hour ago and some users still hit the old IP. Why?**

<details><summary>Answer guide</summary>

- **Testing:** DNS caching.
- **Strong answer:** resolvers and clients cache answers for the record's TTL (and some ignore it); the old TTL applies to caches populated before the change. Lower TTL well before a planned migration; keep the old target serving until traffic drains; check with `dig` against different resolvers. Also consider negative caching and application-level DNS caching (for example the JVM).
- **Common mistakes:** "DNS propagation takes 48 hours" as a fixed rule.
- **Follow-ups:** design a cut-over with zero downtime using weighted records.
</details>

**Q3 · Mid · How is an AWS API call authorised when identity policies, resource policies, permission boundaries and organisation SCPs all exist?**

<details><summary>Answer guide</summary>

- **Testing:** IAM policy evaluation logic.
- **Strong answer:** default deny; an explicit deny anywhere wins; organisation service control policies and permission boundaries set maximum permissions (they grant nothing on their own); an allow must come from an identity-based or resource-based policy; for cross-account access, both the caller's identity policy and the resource policy (or a role trust policy for assumed roles) must allow. Session policies further limit. Debug with the policy simulator and CloudTrail error details.
- **Common mistakes:** thinking an SCP grants permissions.
- **Follow-ups:** grant a CI pipeline in account A deploy rights in account B, least privilege.
</details>

**Q4 · Mid · Two services cannot connect after a network change. Your systematic checklist?**

<details><summary>Answer guide</summary>

- **Testing:** layered troubleshooting.
- **Strong answer:** layer by layer: DNS resolves to the expected address; routing (route tables, peering or transit routes in both directions); security groups on both sides; network ACLs including ephemeral ports; host firewall; the service listening on the right interface and port; TLS (certificate name, trust); then application-level errors. Use flow logs and reachability analysis tools; test from the source with `curl -v`, `nc`, `traceroute`.
- **Common mistakes:** jumping to the application before proving the network path.
- **Follow-ups:** overlapping CIDR ranges between two peered networks; options.
</details>

**Q5 · Mid · Where do you terminate TLS for a public web application, and why?**

<details><summary>Answer guide</summary>

- **Testing:** security and operations trade-offs.
- **Strong answer:** at the load balancer or CDN for central certificate management and offload; re-encrypt to backends when compliance or zero-trust requires encryption in transit inside the network; end-to-end (pass-through) when the backend must see the client certificate (mutual TLS). Automate certificate issuance and renewal; monitor expiry; enforce modern TLS versions.
- **Common mistakes:** plain HTTP inside the VPC by default without considering requirements.
- **Follow-ups:** an expired internal certificate caused an outage; how do you prevent it?
</details>

**Q6 · Mid · Block, file or object storage for: a database, shared home directories, user-uploaded images?**

<details><summary>Answer guide</summary>

- **Testing:** storage fundamentals.
- **Strong answer:** database: block storage (low-latency, attached to one instance, snapshots) or a managed database. Shared directories: a managed file system (NFS/SMB semantics, multiple clients). Images: object storage (durable, cheap, HTTP access, lifecycle tiers, CDN in front). Know consistency: Amazon S3 has provided strong read-after-write consistency since December 2020. Discuss cost per GB and per request.
- **Common mistakes:** object storage mounted as a file system for a database.
- **Follow-ups:** move rarely accessed images to a cheaper tier automatically.
</details>

### Infrastructure as code

**Q7 · Mid · `terraform plan` wants to destroy and recreate your production database. What do you do?**

<details><summary>Answer guide</summary>

- **Testing:** IaC safety.
- **Strong answer:** stop; read which attribute "forces replacement" (for example identifier, engine, subnet group, encryption setting); check whether the change is intended or drift; options: revert the change, use `moved` blocks for renamed resources, import or state operations, perform the change through a blue-green or snapshot-restore migration. Protect with `lifecycle { prevent_destroy = true }`, deletion protection on the resource, and plan review in CI.
- **Common mistakes:** `-auto-approve` in a pipeline for production.
- **Follow-ups:** how do you detect drift continuously?
</details>

**Q8 · Mid · Structure Terraform for three environments across several accounts.**

<details><summary>Answer guide</summary>

- **Testing:** IaC architecture.
- **Strong answer:** versioned reusable modules; a thin root configuration per environment and account (separate state per environment, remote state with locking); variables for differences, not copied code; pinned provider and module versions; small blast radius by splitting state by lifecycle (network, data, apps); CI pipeline with plan on pull request and apply after approval; policy-as-code checks.
- **Common mistakes:** one giant state for everything; workspaces used for strongly different environments without discipline.
- **Follow-ups:** sharing outputs between states safely.
</details>

**Q9 · Mid · Review this AI-generated Terraform.**

```hcl
resource "aws_s3_bucket" "reports" {
  bucket = "acme-reports"
}

resource "aws_s3_bucket_acl" "reports" {
  bucket = aws_s3_bucket.reports.id
  acl    = "public-read"
}

resource "aws_security_group_rule" "ssh" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.app.id
}

resource "aws_iam_role_policy" "app" {
  role   = aws_iam_role.app.id
  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [{ Effect = "Allow", Action = "*", Resource = "*" }]
  })
}
```

<details><summary>Answer guide</summary>

- **Testing:** security review of generated IaC.
- **Strong answer:** (1) A public-read ACL on a reports bucket exposes data; also, since April 2023 new buckets have ACLs disabled and Block Public Access on by default, so this resource would fail or require weakening account defaults. Keep it private and serve via signed URLs or a CDN with origin access control. Add encryption and versioning settings explicitly. (2) SSH open to the internet: remove; use a session manager or bastion with restricted sources. (3) `Action: *` on `Resource: *` is administrator access: scope to required actions and ARNs. Add policy-as-code checks in CI (for example Checkov or tfsec rules) so these fail automatically.
- **Common mistakes:** fixing only the most obvious one.
- **Follow-ups:** how do you find what permissions the app really needs (access analysis from logs)?
</details>

### Kubernetes

**Q10 · Mid · A pod is in `CrashLoopBackOff`. Debug it.**

<details><summary>Answer guide</summary>

- **Testing:** practical Kubernetes debugging.
- **Strong answer:** `kubectl describe pod` (events, exit code, last state, OOMKilled), `kubectl logs --previous`; check the image and command, config and secrets mounted, environment variables, liveness probe killing a slow-starting app (use a startup probe), dependency not reachable at start, resource limits. Reproduce the container locally with the same configuration.
- **Common mistakes:** deleting the pod repeatedly.
- **Follow-ups:** exit code 137 vs 1 vs 143.
</details>

**Q11 · Mid · After each deploy, users see 502s for about 30 seconds.**

<details><summary>Answer guide</summary>

- **Testing:** rollout mechanics.
- **Strong answer:** new pods receive traffic before ready (missing or weak readiness probes), old pods are killed while still in the load balancer's target list (no graceful shutdown, no `preStop` delay, short termination grace period), or load balancer health-check and deregistration delays mismatch. Fix readiness probes, handle SIGTERM (stop accepting, finish in-flight requests), add a short `preStop` sleep, align deregistration delay, set `maxUnavailable: 0` with surge.
- **Common mistakes:** adding retries at the client only.
- **Follow-ups:** long-lived WebSocket connections during deploys.
</details>

**Q12 · Mid · Explain requests, limits, CPU throttling and OOMKilled.**

<details><summary>Answer guide</summary>

- **Testing:** resource model.
- **Strong answer:** requests drive scheduling; limits cap usage. CPU over the limit is throttled (latency spikes, not kills); memory over the limit gets the container OOM-killed. QoS classes (Guaranteed, Burstable, BestEffort) affect eviction order. Many teams set memory limits equal to requests and avoid tight CPU limits for latency-sensitive services; base values on measured usage (vertical recommendations).
- **Common mistakes:** identical tiny limits copied across all services.
- **Follow-ups:** a JVM service gets OOM-killed while heap usage looks fine (non-heap memory, container-aware settings).
</details>

**Q13 · Sr · Make one Kubernetes cluster safe for ten teams.**

<details><summary>Answer guide</summary>

- **Testing:** multi-tenancy controls.
- **Strong answer:** namespace per team with RBAC (least privilege, no cluster-admin), resource quotas and limit ranges, default-deny network policies with explicit allows, Pod Security Standards (restricted profile) enforced by admission, image provenance and allowed registries, separate node pools for sensitive workloads, audit logging, cost allocation by labels. Know when a separate cluster is the right answer (hard isolation, compliance).
- **Common mistakes:** namespaces treated as a security boundary on their own.
- **Follow-ups:** a team needs a privileged DaemonSet; how do you decide?
</details>

### Architecture

**Q14 · Mid · Design a highly available web application with a relational database.**

<details><summary>Answer guide</summary>

- **Testing:** core cloud architecture.
- **Strong answer:** stateless app instances in an autoscaling group or orchestrator across at least two availability zones behind a load balancer; managed database with synchronous standby in another zone and automatic failover; read replicas if needed; backups with point-in-time recovery tested by restores; static assets on object storage plus CDN; health checks; define RTO and RPO and show how the design meets them; infrastructure as code; observability.
- **Common mistakes:** single-AZ database; never testing restores.
- **Follow-ups:** what happens to in-flight transactions during database failover?
</details>

**Q15 · Sr · Design a multi-account landing zone for a company moving to the cloud.**

<details><summary>Answer guide</summary>

- **Testing:** governance at scale.
- **Strong answer:** an organisation with organisational units (security, infrastructure, workloads by environment, sandbox); guardrails via SCPs (deny disabling logging, deny unapproved regions); centralised identity with single sign-on and role-based access; central log archive and security tooling accounts; a network hub (transit routing, inspection, shared DNS); account vending automated with baselines; tagging and cost allocation; break-glass access.
- **Common mistakes:** one account with many VPCs.
- **Follow-ups:** a team needs a region your SCP denies.
</details>

**Q16 · Sr · Migrate an on-premises application (VMs plus a commercial relational database) to the cloud.**

<details><summary>Answer guide</summary>

- **Testing:** migration planning.
- **Strong answer:** discovery (dependencies, traffic, licences, data size, compliance); choose per component among rehost, replatform, refactor, repurchase, retire, retain; pilot a low-risk component; data migration with change data capture to keep a replica in sync, then a short cut-over window; rollback plan; performance testing; cost model including licences; skills and runbooks for the operations team.
- **Common mistakes:** "lift and shift everything" without dependency mapping.
- **Follow-ups:** the database licence is not portable; options.
</details>

**Q17 · Sr · Active-active or active-passive across two regions?**

<details><summary>Answer guide</summary>

- **Testing:** multi-region trade-offs.
- **Strong answer:** active-passive: simpler, data replicated asynchronously, RPO > 0, failover time is the RTO, regular failover drills required. Active-active: lower RTO and latency for users near each region, but needs conflict handling or a globally consistent database, routing, and double capacity planning. Decide from business RTO/RPO, data consistency needs and cost. Avoid hidden single-region dependencies (identity, DNS, CI, secrets).
- **Common mistakes:** "active-active" while writes still go to one region's database.
- **Follow-ups:** split-brain prevention.
</details>

**Q18 · Mid · Serverless functions or containers for an image-processing pipeline triggered by uploads?**

<details><summary>Answer guide</summary>

- **Testing:** compute model selection.
- **Strong answer:** functions fit bursty, short, event-driven work (scale to zero, pay per use, managed scaling) within runtime, memory and duration limits; containers fit long or steady workloads, custom dependencies, GPUs, and predictable cost at high utilisation. Consider cold starts, concurrency limits, idempotency for retried events, and dead-letter queues. A hybrid is common.
- **Common mistakes:** ignoring retries producing duplicate outputs.
- **Follow-ups:** cost crossover estimate for 10 million images a day.
</details>

### Cost

**Q19 · Mid · The cloud bill rose 40% this month. Investigate.**

<details><summary>Answer guide</summary>

- **Testing:** FinOps practice.
- **Strong answer:** break down by service, account, region and tag; compare daily to find the start date; correlate with deploys. Usual suspects: NAT gateway data processing, cross-AZ or inter-region data transfer, logs ingestion, forgotten resources (unattached volumes, idle load balancers, old snapshots), autoscaling stuck high, a new managed service. Set budgets and anomaly alerts; enforce tagging.
- **Common mistakes:** buying reservations before finding the cause.
- **Follow-ups:** who owns cost in a team that does not see the bill?
</details>

**Q20 · Mid · Cut cost for a workload that is steady most of the day with evening peaks.**

<details><summary>Answer guide</summary>

- **Testing:** pricing models.
- **Strong answer:** right-size from utilisation data; commitments (savings plans or reserved capacity) for the steady baseline; on-demand or autoscaling for peaks; spot or preemptible capacity for stateless, interruption-tolerant parts with graceful handling; storage tiering and lifecycle rules; caching to reduce database size; measure cost per unit of business (per order).
- **Common mistakes:** spot for stateful databases.
- **Follow-ups:** how much should be committed, and how do you decide?
</details>

### Security

**Q21 · Mid · How should a service running in Kubernetes on a cloud get credentials to read a secret store and a bucket?**

<details><summary>Answer guide</summary>

- **Testing:** workload identity.
- **Strong answer:** no long-lived access keys in images, environment files or IaC. Use workload identity federation (the service account is mapped to a cloud role through an OIDC trust), scoped to the specific secret and bucket; secrets fetched at runtime or synced by a controller; rotation; audit logs of access.
- **Common mistakes:** a node-level role that every pod inherits.
- **Follow-ups:** CI pipelines deploying to the cloud without stored keys (OIDC from the CI provider).
</details>

**Q22 · Mid · You discover a storage bucket with customer exports has been publicly readable for a week. Respond.**

<details><summary>Answer guide</summary>

- **Testing:** defensive incident response in the cloud.
- **Strong answer:** contain first: block public access at bucket and account level; preserve evidence (configuration history, access logs, audit trail of who changed the policy and when); determine what was accessed and by whom from access logs; involve security, legal and privacy teams (breach notification duties depend on jurisdiction and data); rotate anything exposed; root cause (manual change, IaC default) and preventive controls (account-level block, policy-as-code, continuous configuration monitoring).
- **Common mistakes:** deleting the bucket (destroys evidence); fixing silently.
- **Follow-ups:** access logging was not enabled; what can you still determine?
</details>

### AI infrastructure and AI-era judgement

**Q23 · Sr · Design a GPU inference platform for several internal models.**

<details><summary>Answer guide</summary>

- **Testing:** AI-era infrastructure.
- **Strong answer:** model serving with a high-throughput inference server supporting continuous batching; autoscaling on queue depth or concurrency, not CPU; model loading time drives warm pools and scale-up policy; GPU sizing by model memory (weights plus key-value cache) and throughput; multi-tenancy with quotas and priority classes; cost per 1,000 tokens or per request as the key metric; observability (latency percentiles, tokens per second, GPU utilisation); capacity reservations vs on-demand; fallback to smaller models or external APIs.
- **Common mistakes:** autoscaling GPU nodes on CPU utilisation.
- **Follow-ups:** a new model needs twice the GPU memory; what changes?
</details>

**Q24 · Mid · CI fails with AccessDenied; the assistant suggests putting the root account's access keys in the CI secrets. Respond.**

<details><summary>Answer guide</summary>

- **Testing:** least-privilege judgement on AI suggestions.
- **Strong answer:** never use root credentials for automation; root keys should not exist. Read the AccessDenied message for the missing action and resource; grant that to a dedicated deploy role; let CI assume it through OIDC federation with conditions on repository and branch; no static keys. Explain why the assistant's fix "works" and why it is dangerous.
- **Common mistakes:** an admin role for CI "temporarily".
- **Follow-ups:** how do you stop a pull request from a fork from assuming the deploy role?
</details>

**Q25 · Mid · Serverless functions time out connecting to the database during traffic spikes.**

<details><summary>Answer guide</summary>

- **Testing:** connection management in elastic compute.
- **Strong answer:** each concurrent function instance opens connections; spikes exceed the database's connection limit. Fix with a connection proxy or pooler, reuse connections across invocations, cap function concurrency, use a data API or a database designed for many short connections, and move heavy writes to a queue.
- **Common mistakes:** increasing the database's max connections until memory runs out.
- **Follow-ups:** how do you load test this before launch?
</details>

### Behavioural

**Q26 · Mid · Tell me about a cost overrun or outage you caused or fixed.**

<details><summary>Answer guide</summary>

- **Testing:** ownership, learning.
- **Strong answer:** what happened with numbers (cost or downtime), how it was detected, your actions, root cause, the guardrail you added (budget alert, policy-as-code rule, runbook) and evidence that it worked later.
- **Common mistakes:** a story without a preventive change.
- **Follow-ups:** how did you communicate it to leadership?
</details>

## Sources

- AWS, *Amazon S3 now delivers strong read-after-write consistency* (Dec 2020): https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-s3-now-delivers-strong-read-after-write-consistency-automatically-for-all-applications/
- AWS, *Amazon S3 Block Public Access and ACLs disabled by default for new buckets* (applied from April 2023; checked October 2026): https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-s3-automatically-enable-block-public-access-disable-access-control-lists-buckets-april-2023/
- AWS IAM documentation, *Policy evaluation logic*: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html
- Kubernetes documentation (probes, resource management, Pod Security Standards): https://kubernetes.io/docs/
- Loop structure: [CLD role page](../../01_market_map/roles/CLD_cloud_engineering.md) and [Cloud major, section 8](../../../03_majors/cloud_engineering/README.md).

_Last reviewed: 2026-10_
