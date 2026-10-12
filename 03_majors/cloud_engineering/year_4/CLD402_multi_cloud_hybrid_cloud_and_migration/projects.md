# CLD402 · Labs and projects

The "legacy estate" for these labs runs on your laptop or a lab server (VirtualBox, Multipass or containers) so you can discover and migrate it without paying for a source data centre. Migration services bill per replicating server and per hour: stop replication between sessions. TCO arithmetic, transfer-time maths and the 7 Rs assignment are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · TCO model (no AI) | Five-year TCO for 300 VMs on-premises versus cloud, including staff, power, licences, refresh, migration one-time costs and commitments | Spreadsheet with assumptions, sensitivity analysis on three inputs | 4 h |
| 2 · Discovery and dependencies | Run agentless discovery and flow capture on a 12-VM lab estate with a stale CMDB; find hidden dependencies (a nightly batch job, an NFS share, a hard-coded IP) | Corrected inventory, dependency graph, 7 Rs per app with evidence | 5 h |
| 3 · Wave plan and runbook | Plan waves for the lab estate; write and rehearse a cutover runbook with go/no-go and rollback | Wave plan, runbook, rehearsal timings | 4 h |
| 4 · Rehost with replication | Migrate two VMs with block-level replication (AWS MGN, Azure Migrate or Migrate to Virtual Machines), test cutover, then real cutover | Replication lag graph, test results, post-move fixes made | 5 h |
| 5 · Bulk data with checksums | Move 1 TB (or a scaled-down 100 GB) of mixed files with DataSync, Storage Transfer Service or rclone; incremental re-sync | Transfer time versus your prediction, checksum report | 3 h |
| 6 · CDC database migration | Live Postgres to managed Postgres with DMS or logical replication under write load; cutover | Write-downtime measurement, reconciliation results | 5 h |
| 7 · Strangler fig | Route one feature of a legacy monolith to a new service behind a router, with data sync | Traffic split evidence and rollback demo | 5 h |
| 8 · Hybrid control plane | Attach a local Kubernetes cluster to Azure Arc, EKS Hybrid Nodes or GKE attached clusters; apply a policy centrally | Policy applied on-premises from the cloud; behaviour when the link drops | 4 h |
| 9 · Cross-cloud federation | A workload on cloud A reads a bucket on cloud B using workload identity federation, no stored keys | Trust configuration and access logs on both sides | 3 h |
| 10 · AI assessment audit | Run an AI-assisted assessment on the Lab 2 estate and diff against your manual result | Table of agreements, misses and false dependencies | 3 h |

## Projects

### P1 · A migration business case (L1, ~6 hours)

**Real-world inspiration:** cloud providers fund migrations through programmes such as the AWS Migration Acceleration Program, but finance teams approve them on TCO and risk. 37signals' public numbers show the opposite case for steady workloads ([The Register](https://www.theregister.com/2025/05/09/37signals_cloud_repatriation_storage_savings)). The company is an *illustrative scenario*: a mid-sized Indian insurer with 300 VMs in a Pune data centre whose lease ends in 18 months.

**What to build:** a business case with a 5-year TCO, a 7 Rs breakdown for a provided application list, a risk register, a high-level wave plan and a recommendation, including a credible "stay on-premises" or "colocation" option.

**Acceptance criteria:**
- Every cost line has a stated source or assumption; sensitivity analysis shows which three inputs change the decision.
- At least 10% of applications are retired or retained with evidence (zombie or idle by utilisation, or residency).
- The recommendation states conditions under which it would be wrong.
- **Cost ceiling:** US$0.

**Stretch goals:** carbon comparison using provider carbon tools and India's CEA grid factor.

**What it proves to an employer:** you can speak to finance and leadership, not only to engineers.

### P2 · Database and VM migration with proven equivalence (L2, ~15 hours)

**Real-world inspiration:** heterogeneous and homogeneous database migrations with change data capture are the riskiest step in most programmes; AWS's [DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) and Google's Database Migration Service describe CDC-based cutovers. The workload is *illustrative*: a policy-administration app with a Postgres database and two application VMs.

**What to build:** migrate the app VMs by rehost and the database by CDC into your landing zone (built with CLD302 modules), with a rehearsed cutover, a reconciliation suite and a rollback path using reverse replication.

**Acceptance criteria:**
- Write downtime at cutover under 60 seconds, measured by a client writing every 100 ms.
- Reconciliation: row counts, per-partition checksums and three business totals (premium sum, policy count by state, claims open) match exactly; a planted drift in a test run is detected.
- Rollback rehearsal returns traffic to the source within 15 minutes with no data loss.
- Post-migration performance within 10% of the source on a defined query set, or a documented fix.
- **Cost ceiling:** US$20.

**Stretch goals:** heterogeneous move (SQL Server or MySQL to Postgres) with converted stored procedures and differential tests.

**What it proves to an employer:** you can move data without losing a rupee of it, and prove it.

### P3 · An end-to-end migration with hybrid residue and an exit plan (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- AWS Transform claims large time savings for VMware discovery and wave planning ([AWS](https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-generally-available/)); your job is to test such claims.
- SEBI's 2023 cloud framework requires regulated entities to manage vendor lock-in and plan exits.
- The EU Data Act removes switching charges from 2027 ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)).
- The company is an *illustrative scenario*: a brokerage with a 20-VM lab estate, of which a market-data feed handler must stay on-premises next to an exchange co-location link.

**What to build:**
1. Full discovery and a 7 Rs plan for the estate, done once manually and once with an AI-assisted tool, with a comparison.
2. Migrate in at least three waves using a factory approach (automated steps, tracking sheet, lessons per wave).
3. Keep the feed handler on-premises, managed through a hybrid control plane, connected by VPN with BGP and hybrid DNS.
4. Modernise one component (replatform to containers or managed database).
5. Run hypercare, then optimise and decommission the source.
6. Write an exit plan to a second cloud for the regulated core, with an export rehearsal of one dataset and its cost.

**Acceptance criteria:**
- **Completeness:** 100% of in-scope apps migrated, retained or retired as planned; the source estate is shut down with sign-offs recorded.
- **Dependencies:** zero unplanned outages caused by missed dependencies; any found during waves are logged with how discovery missed them.
- **AI comparison:** a table showing dependencies and classifications the AI-assisted assessment got right, missed and invented, with your final decision for each.
- **Hybrid:** policy and monitoring for the on-premises handler come from the cloud control plane; a 10-minute WAN cut does not stop the handler, and drift is reconciled after.
- **Exit:** the export rehearsal completes, with measured time, egress cost (with and without waivers) and data-format notes.
- **Cost:** post-optimisation monthly run cost at least 20% below the first post-migration month, with the actions listed.
- **Cost ceiling:** US$40.

**Stretch goals:** a portable deployment of one service on a second cloud with a cost comparison; carbon estimate before and after.

**What it proves to an employer:** you can run a migration programme end to end, use AI tools without being fooled by them, and plan for leaving, which is what consultancies, GCCs and regulated enterprises hire for.

## Feeds into

- [CLD403 FinOps](../CLD403_finops_and_cloud_cost_engineering/README.md): post-migration optimisation and commitments.
- [CLD501 Frontier Seminar](../../year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md): sovereignty and exit at national scale.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): migration work is a common co-op assignment.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): measuring AI-assisted migration accuracy is a strong capstone topic.
