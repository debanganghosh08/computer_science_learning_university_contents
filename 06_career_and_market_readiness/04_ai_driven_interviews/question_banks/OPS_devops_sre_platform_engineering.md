# OPS · DevOps, SRE and Platform Engineering: interview question bank

| Role and market | Levels | Practise with | Score with |
|---|---|---|---|
| [OPS role page](../../01_market_map/roles/OPS_devops_sre_platform_engineering.md) · [OPS major](../../../03_majors/devops_sre_platform_engineering/README.md) | NG → Mid → Sr | [Mock kit 4.9](../how_to_run_a_mock_with_any_llm.md#49-cloud-and-sre-incident-60-minutes) · [Day 5 simulation](../simulation_days.md#5-day-5-cloud-engineer--site-reliability-engineer-mid-level) | [Rubrics](../rubrics.md) |

Operations interviews watch your method more than your memory: how you narrow a problem, what you check first, how you act safely while users are affected, and how you make the next incident less likely. AI tools now draft scripts, runbooks and even remediation steps, so expect questions on when to trust them in production.

## 1. The typical loop

| Round | Duration | What it tests | AI policy you may meet | Mock brief |
|---|---|---|---|---|
| Linux and networking troubleshooting | 45 min | Method under uncertainty | AI-off | Day 5 troubleshooting brief |
| Coding or scripting | 45 min | Automation in Python, Go or Bash; DSA at some product companies | AI-off | Kit 4.1 |
| Reliability system design | 60 min | Monitoring, alerting, deployment pipelines, failover | AI-off | Kit 4.3 |
| Incident scenario | 45–60 min | Triage, mitigation, communication, postmortem | AI-off | Kit 4.9 |
| Behavioural | 45 min | Outages, on-call improvements | AI-off | Kit 4.11 |

## 2. How to use this bank

Answer aloud with a timer, then open the guide. Practise troubleshooting on a real Linux VM you can break; the commands only become reflexes through use.

## 3. Questions

### Linux and networking

**Q1 · NG · "The server is slow." Your first five minutes.**

<details><summary>Answer guide</summary>

- **Testing:** method (for example the USE method: utilisation, saturation, errors per resource).
- **Strong answer:** clarify what is slow and since when; `uptime` (load trend), `top`/`htop` (CPU, memory, top processes), `vmstat 1` (run queue, swap, iowait), `iostat -xz 1` (disk utilisation and latency), `free -m`, `df -h`, `ss -s` (connections), `dmesg -T` (OOM kills, hardware errors), recent changes and deploys. Form a hypothesis and test it.
- **Common mistakes:** rebooting first; running random commands without a hypothesis.
- **Follow-ups:** CPU is 100% in `si` (softirq); what does that suggest?
</details>

**Q2 · Mid · Load average is 40 on an 8-core machine but CPU is mostly idle. Explain.**

<details><summary>Answer guide</summary>

- **Testing:** Linux load semantics.
- **Strong answer:** on Linux, load average counts runnable tasks and tasks in uninterruptible sleep (D state), typically waiting on I/O. High load with idle CPU points to I/O waits: a slow disk, a hung network file system, or a storage backend issue. Check `ps -eo state,cmd | grep '^D'`, `iostat`, mount health, kernel logs.
- **Common mistakes:** "load average equals CPU usage".
- **Follow-ups:** a process stuck in D state cannot be killed; why?
</details>

**Q3 · Mid · `df` says the disk is full; `du` adds up to far less.**

<details><summary>Answer guide</summary>

- **Testing:** file system internals.
- **Strong answer:** deleted files still held open by a process (a log file deleted while the service writes to it) keep their space allocated; find them with `lsof +L1` and restart or signal the process to reopen logs (or truncate via `/proc/<pid>/fd`). Other causes: files hidden under a mount point, reserved blocks, inode exhaustion (`df -i`).
- **Common mistakes:** deleting more files at random.
- **Follow-ups:** prevent recurrence (log rotation with copytruncate or reopen signals, alerts on disk growth rate).
</details>

**Q4 · NG · A request to `https://api.example.com` takes 3 seconds. How do you find which step is slow?**

<details><summary>Answer guide</summary>

- **Testing:** request lifecycle.
- **Strong answer:** DNS lookup, TCP connect, TLS handshake, server processing (time to first byte), transfer. `curl -w` with `time_namelookup`, `time_connect`, `time_appconnect`, `time_starttransfer`, `time_total` shows each. Then dig into the slow phase: resolver issues, network path or packet loss, certificate chain or OCSP, or the application.
- **Common mistakes:** blaming the application without measuring.
- **Follow-ups:** DNS lookups take 5 seconds intermittently from containers (search domains, `ndots`, resolver timeouts).
</details>

**Q5 · Mid · A service making many outbound calls starts failing with "cannot assign requested address".**

<details><summary>Answer guide</summary>

- **Testing:** TCP connection lifecycle.
- **Strong answer:** ephemeral port exhaustion: each new outbound connection to the same destination needs a local port; closed connections linger in TIME_WAIT. Causes: no connection reuse (no keep-alive or pooling), very high request rate to one destination. Fixes: connection pooling and keep-alive, widen the ephemeral port range, more destination addresses, check NAT gateway limits. Verify with `ss -tan state time-wait | wc -l`.
- **Common mistakes:** disabling TIME_WAIT behaviour with unsafe kernel tweaks as the first fix.
- **Follow-ups:** why does TIME_WAIT exist?
</details>

### Scripting and automation

**Q6 · NG · Write a script to list the top 10 client IPs causing 5xx responses in an access log.**

<details><summary>Answer guide</summary>

- **Testing:** practical text processing, robustness.
- **Strong answer:** with `awk` filter by status field, count by IP, `sort | uniq -c | sort -rn | head`; or a short Python script that parses lines with a regular expression, skips malformed lines and counts with a `Counter`. Use `set -euo pipefail` in Bash, quote variables, handle compressed rotated logs (`zcat`). State the assumed log format.
- **Common mistakes:** hard-coding field positions without checking the format; ignoring malformed lines.
- **Follow-ups:** the log is 50 GB; stream it, parallelise by file, or query it in the log platform instead.
</details>

**Q7 · Mid · What makes automation idempotent, and why does it matter?**

<details><summary>Answer guide</summary>

- **Testing:** automation design.
- **Strong answer:** running it twice leaves the system in the same state as running it once: check current state before acting, declare desired state rather than steps (configuration management, Kubernetes manifests, Terraform), use create-if-absent operations, make retries safe. It matters because automation is retried after partial failure and run by schedulers that may overlap.
- **Common mistakes:** scripts that append a config line on every run.
- **Follow-ups:** two runs overlap; add locking.
</details>

### Reliability engineering

**Q8 · Mid · Define SLIs, an SLO and the error budget for a public API.**

<details><summary>Answer guide</summary>

- **Testing:** SRE fundamentals.
- **Strong answer:** SLIs from the user's view: availability (good requests / valid requests, excluding client errors) and latency (share of requests under, say, 300 ms) measured at the load balancer. SLO example: 99.9% availability over 30 days, which allows 0.1% errors, about 43 minutes of full outage. Error budget policy: when the budget is spent, prioritise reliability work and slow risky releases. Choose SLOs with product owners.
- **Common mistakes:** 100% targets; SLIs from server CPU.
- **Follow-ups:** an SLO for a batch job (freshness or completion time).
</details>

**Q9 · Mid · Design alerting on that SLO without paging people for noise.**

<details><summary>Answer guide</summary>

- **Testing:** burn-rate alerting.
- **Strong answer:** alert on error-budget burn rate, not raw error spikes. The multiwindow, multi-burn-rate approach from Google's SRE workbook pages when, for example, 2% of a 30-day budget burns in 1 hour (burn rate 14.4) confirmed by a short 5-minute window, and 5% in 6 hours (burn rate 6); slower burns create tickets. Short windows reduce reset time; long windows reduce noise.
- **Common mistakes:** paging on any 5xx; static CPU thresholds as pages.
- **Follow-ups:** low-traffic services where one error is 1% of requests.
</details>

**Q10 · Mid · On-call receives 40 pages a week and people are burning out. Fix it.**

<details><summary>Answer guide</summary>

- **Testing:** operational leadership.
- **Strong answer:** measure: list every page for a month with cause and action taken; delete alerts with no action; convert non-urgent ones to tickets; fix top recurring causes; page on symptoms (SLO burn) not causes; add runbooks; auto-remediate safe recurring actions; set a target (for example under two pages per shift) and review weekly. Make reliability work part of planning.
- **Common mistakes:** raising thresholds blindly until alerts stop.
- **Follow-ups:** how do you get product teams to fix the root causes?
</details>

**Q11 · Mid · What makes a good postmortem?**

<details><summary>Answer guide</summary>

- **Testing:** learning culture.
- **Strong answer:** blameless framing (systems and conditions, not individuals); impact with numbers; timeline from detection to recovery; root cause and contributing factors (why it was possible, why it was not detected sooner, why recovery took that long); what went well; action items that are specific, owned, dated and tracked, prioritised by risk reduction. Share widely; review completion.
- **Common mistakes:** "human error" as root cause; action items like "be more careful".
- **Follow-ups:** how do you know postmortems lead to fewer incidents?
</details>

### CI/CD

**Q12 · Mid · Design a deployment pipeline with canary releases and automatic rollback.**

<details><summary>Answer guide</summary>

- **Testing:** delivery safety.
- **Strong answer:** build once, promote the same artefact; tests and security scans; deploy to staging with smoke tests; canary to a small share of production traffic; compare canary vs baseline on SLIs (errors, latency, saturation, business metrics) with statistical guardrails; automatic rollback if thresholds are breached; progressive increase; feature flags to separate deploy from release; deployment freeze rules and audit.
- **Common mistakes:** canary judged only by "pods are healthy".
- **Follow-ups:** canaries for database schema changes.
</details>

**Q13 · Mid · CI takes 40 minutes per pull request. Make it fast.**

<details><summary>Answer guide</summary>

- **Testing:** developer productivity engineering.
- **Strong answer:** measure where time goes; cache dependencies and build outputs (remote caches for incremental builds); parallelise and shard tests; run only affected tests based on change graphs, with a full run on main; smaller container images; fail fast with lint and unit tests first; fix or quarantine slow and flaky tests; right-size runners.
- **Common mistakes:** skipping tests to save time.
- **Follow-ups:** how do you keep it fast over a year (budgets and dashboards)?
</details>

**Q14 · Sr · "Deploy" and "release": why separate them, and how?**

<details><summary>Answer guide</summary>

- **Testing:** trunk-based delivery.
- **Strong answer:** deploying code to production does not have to expose it; feature flags release features to cohorts, decouple business timing from engineering, and allow instant kill switches. Requires flag hygiene (owners, expiry), testing of both flag states, and backwards-compatible data changes (expand-contract). Enables small, frequent deploys, which improves DORA metrics (deployment frequency, lead time, change failure rate, time to restore).
- **Common mistakes:** flags that live forever and multiply test paths.
- **Follow-ups:** a flag misconfiguration caused an outage; what controls apply to flag changes?
</details>

**Q15 · Mid · Secure the software supply chain of your CI pipeline.**

<details><summary>Answer guide</summary>

- **Testing:** defensive CI security.
- **Strong answer:** pin dependencies and actions by version or digest; dependency and container scanning; generate an SBOM; sign artefacts and verify signatures at deploy (for example Sigstore); build provenance aligned with SLSA levels; least-privilege, short-lived CI credentials via OIDC; protect the main branch and require reviews; isolate untrusted pull-request builds from secrets; audit logs.
- **Common mistakes:** long-lived cloud keys stored as CI secrets available to every job.
- **Follow-ups:** a widely used dependency was compromised upstream; how do you find where you used it?
</details>

### Observability

**Q16 · Mid · Prometheus memory exploded after a team added a label. Why?**

<details><summary>Answer guide</summary>

- **Testing:** metrics cardinality.
- **Strong answer:** each unique label combination is a separate time series; labels with unbounded values (user ID, request ID, full URL) create millions of series. Use bounded labels (route template, status class); put high-cardinality detail in logs or traces; set limits on series per target; review new metrics in code review.
- **Common mistakes:** scaling the Prometheus server instead of fixing labels.
- **Follow-ups:** when do you choose logs vs metrics vs traces for a question?
</details>

**Q17 · Mid · Design observability for 40 microservices.**

<details><summary>Answer guide</summary>

- **Testing:** practical observability architecture.
- **Strong answer:** standard instrumentation with OpenTelemetry; RED metrics (rate, errors, duration) per service and route, USE metrics for resources; structured logs with trace IDs; distributed tracing with context propagation across HTTP and queues, with sampling (head or tail-based to keep errors and slow traces); SLO dashboards per user journey; service ownership metadata; cost controls on log volume.
- **Common mistakes:** dashboards for everything, no SLOs; no trace context across message queues.
- **Follow-ups:** how do you debug a latency regression that crosses five services?
</details>

### Platform engineering

**Q18 · Sr · Design an internal developer platform.**

<details><summary>Answer guide</summary>

- **Testing:** platform as a product.
- **Strong answer:** start from developer pain (survey, measure lead time); golden paths: templates that create a service with CI/CD, observability, security defaults and on-call setup; self-service infrastructure through approved modules; a service catalogue with ownership; guardrails as code; documentation; measure adoption, satisfaction and DORA metrics; keep escape hatches with clear support boundaries.
- **Common mistakes:** building a portal before solving one painful workflow.
- **Follow-ups:** teams refuse to migrate to the golden path; what do you do?
</details>

**Q19 · Sr · GitOps for Kubernetes: how do you promote a change from staging to production?**

<details><summary>Answer guide</summary>

- **Testing:** declarative delivery.
- **Strong answer:** Git as the source of truth for desired state; a controller (for example Argo CD or Flux) reconciles clusters and reports drift; promotion by pull request that updates the image digest or overlay for production after automated checks pass in staging; secrets via an external secret manager or encrypted manifests; rollback by reverting the commit; separate repos or folders per environment with protected branches.
- **Common mistakes:** `kubectl apply` by hand in production alongside GitOps.
- **Follow-ups:** emergency fixes during an incident; how do you keep Git and the cluster consistent?
</details>

### Incidents and resilience

**Q20 · Mid · You are the incident commander for a severity-1 outage. What do you do in the first 15 minutes?**

<details><summary>Answer guide</summary>

- **Testing:** incident leadership.
- **Strong answer:** declare the incident and severity; open a channel and a running log; assign roles (incident commander coordinates, operations lead investigates, communications lead updates stakeholders and status page); establish impact; focus on mitigation (roll back recent changes, fail over, shed load); set an update cadence (for example every 15 minutes); avoid parallel uncoordinated changes; hand over explicitly if needed.
- **Common mistakes:** the commander debugging personally and stopping coordination.
- **Follow-ups:** a senior executive joins and starts directing engineers; handle it.
</details>

**Q21 · Mid · A slow dependency caused the whole platform to fall over. Explain how, and how to prevent it.**

<details><summary>Answer guide</summary>

- **Testing:** cascading failure.
- **Strong answer:** callers waited on the slow dependency, exhausting threads or connections; retries multiplied load (retry storm); queues grew; health checks failed and autoscaling added more callers. Prevent with timeouts shorter than callers' timeouts, retries with exponential backoff, jitter and a budget, circuit breakers, bulkheads (separate pools per dependency), load shedding and graceful degradation (serve cached or partial results).
- **Common mistakes:** more retries.
- **Follow-ups:** how do you test this before it happens (fault injection, game days)?
</details>

**Q22 · Sr · Prepare the platform for a sale with 10× normal traffic.**

<details><summary>Answer guide</summary>

- **Testing:** capacity planning.
- **Strong answer:** forecast peak per journey; load test end to end with production-like data; find the first bottleneck and repeat; pre-scale (autoscaling reacts too slowly for step changes) and raise cloud quotas; check third-party limits (payment gateway, SMS provider); caching and static pages; queue-based buffering; feature flags to switch off non-essential features; change freeze; staffed war room with runbooks; post-event review.
- **Common mistakes:** testing only the web tier.
- **Follow-ups:** the payment gateway's limit is lower than your peak; options.
</details>

### Containers

**Q23 · NG · Review this Dockerfile pattern: `FROM python:latest`, `COPY . .`, `RUN pip install -r requirements.txt`, an API key set with `ENV`, running as root.**

<details><summary>Answer guide</summary>

- **Testing:** container hygiene.
- **Strong answer:** pin the base image (version or digest) and prefer a slim image; copy `requirements.txt` first and install before copying code to use layer caching; multi-stage build to exclude build tools; never bake secrets into images (they persist in layers); inject at runtime from a secret store; add a non-root `USER`; `.dockerignore`; health check; scan the image.
- **Common mistakes:** deleting the secret in a later layer and thinking it is gone.
- **Follow-ups:** how do you rebuild images when the base image gets a security fix?
</details>

### AI-era judgement

**Q24 · Mid · An assistant wrote this cleanup script for a cron job. Would you deploy it?**

```bash
#!/bin/bash
ARTIFACT_DIR=$1
find $ARTIFACT_DIR -mtime +7 -name "*.tar.gz" | xargs rm
rm -rf $ARTIFACT_DIR/tmp/*
```

<details><summary>Answer guide</summary>

- **Testing:** reviewing dangerous automation.
- **Strong answer:** no. If the argument is missing, `$ARTIFACT_DIR` is empty: `find` searches the current directory and the last line becomes `rm -rf /tmp/*`, deleting the system's temporary files. Unquoted variables break on spaces; `xargs rm` breaks on unusual filenames. Fix: `set -euo pipefail`; require and validate the argument (exists, is a directory, under an expected prefix); quote everything; use `find "$dir" -mtime +7 -name '*.tar.gz' -print -delete`; log what is deleted; a dry-run mode; test in a sandbox.
- **Common mistakes:** only adding quotes.
- **Follow-ups:** how would you catch this class of bug automatically (ShellCheck in CI)?
</details>

**Q25 · Sr · Would you let an AI agent run remediation actions in production during incidents?**

<details><summary>Answer guide</summary>

- **Testing:** risk design for operational AI.
- **Strong answer:** start read-only: summarising alerts, correlating changes, suggesting runbook steps. Then allow a small allow-list of reversible, low-blast-radius actions (restart a pod, scale out, toggle a pre-approved flag) behind human approval; scoped credentials; rate limits; full audit logs; evaluate on replays of past incidents before production; measure precision of suggestions; kill switch. Irreversible actions (deleting data, changing IAM) stay human-only.
- **Common mistakes:** either "never" without nuance or "yes, it is faster".
- **Follow-ups:** the agent's suggested fix was wrong but plausible; how would on-call notice in time?
</details>

### Behavioural

**Q26 · Mid · Tell me about an outage you caused.**

<details><summary>Answer guide</summary>

- **Testing:** accountability and learning.
- **Strong answer:** what you changed, how it failed, how quickly you noticed, how you mitigated and communicated, the postmortem's systemic findings (why the system allowed the mistake), and what you changed afterwards.
- **Common mistakes:** hiding your role, or excessive self-blame with no systemic fix.
- **Follow-ups:** what guardrail would have stopped it?
</details>

## Sources

- Google, *The Site Reliability Workbook*, chapter "Alerting on SLOs" (multiwindow, multi-burn-rate alerts; checked October 2026): https://sre.google/workbook/alerting-on-slos/
- DORA research on delivery performance metrics: https://dora.dev/
- SLSA specification: https://slsa.dev/ ; OpenTelemetry documentation: https://opentelemetry.io/docs/
- Loop structure: [OPS role page](../../01_market_map/roles/OPS_devops_sre_platform_engineering.md).

_Last reviewed: 2026-10_
