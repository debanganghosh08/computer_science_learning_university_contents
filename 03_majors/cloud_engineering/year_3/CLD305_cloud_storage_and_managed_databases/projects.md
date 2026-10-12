# CLD305 · Labs and projects

Use containers locally (Postgres, Valkey, DynamoDB Local, MinIO for S3-compatible tests) wherever a lab says "local". For cloud labs, use the smallest instance classes, delete databases at the end of each session, and remember to delete snapshots and backup copies too. Lab 8 and the key-design part of Lab 7 are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Durability and consistency | Compute expected annual loss for replication and erasure-coding schemes; write a read-after-write and list-after-write test against S3 or GCS | Calculations and test output | 3 h |
| 2 · Object storage mechanics | Multipart upload with resume, presigned upload URL with size limits, a compare-and-swap counter using conditional writes | Code and a demonstration of a rejected conflicting write | 4 h |
| 3 · Protection and lifecycle | Block Public Access, KMS encryption, versioning, Object Lock in compliance mode for 1 day, lifecycle to colder classes | Proof that even the account admin cannot delete a locked object; lifecycle cost model for 7-year log retention | 4 h |
| 4 · Block storage performance | `fio` random-read and sequential-write tests on gp3 (or Hyperdisk / Premium SSD v2) at three IOPS settings; snapshot restore timing | Performance table, cost per 1,000 IOPS, first-read latency after restore | 4 h |
| 5 · Managed Postgres HA | Multi-AZ Postgres under load: forced failover, client-visible downtime with and without a pooling proxy, read replica lag | Timeline graphs and a list of client-side fixes | 5 h |
| 6 · Zero-downtime major upgrade | Blue/green deployment (or logical replication) to upgrade Postgres one major version | Write downtime measured, rollback plan, and checklist | 4 h |
| 7 · DynamoDB from access patterns | Design tables for 10 queries of an order system (no AI for the design), then load-test a hot key and fix it | Key design with justification, throttling graphs before and after | 6 h |
| 8 · Timed restore drill (no AI) | Delete rows by "mistake", then restore to 10 minutes before into a separate account and reconcile | Achieved RPO and RTO, data-validation queries and runbook | 4 h |
| 9 · Global tables and consistency | Show a lost update with multi-Region eventual consistency; repeat with multi-Region strong consistency and measure write latency | Both histories and the latency comparison | 3 h |
| 10 · Vector storage benchmark | 1 million embeddings in pgvector and S3 Vectors (or OpenSearch); measure recall@10, p95 latency and monthly cost | Benchmark table and a recommendation | 4 h |

## Projects

### P1 · An immutable, cheap audit-log store (L1, ~6 hours)

**Real-world inspiration:** CERT-In's April 2022 directions require organisations in India to keep system logs for a rolling 180 days, and SEBI's cloud framework requires regulated entities to retain ownership of their logs. Object Lock and lifecycle policies are how cloud teams make logs tamper-proof and affordable.

**What to build:** a log bucket in an India region that receives logs from two sources, with KMS encryption, Object Lock retention of 180 days, a lifecycle to colder classes after 30 days, a cross-account replica in the second India region, and a query path (Athena, BigQuery external tables or similar).

**Acceptance criteria:**
- A delete attempt by the bucket owner's admin role fails during retention; show the error.
- Replicated objects appear in the second region within 15 minutes; replica stays in India.
- A query over one day of logs returns in under 30 seconds.
- A cost model for 1 TB per month over 7 years, by storage class.
- **Cost ceiling:** US$3 (use small data volumes and a 1-day retention for the actual test).

**Stretch goals:** log-integrity digests; Intelligent-Tiering versus explicit lifecycle comparison.

**What it proves to an employer:** you can make compliance-grade storage that cannot be quietly erased.

### P2 · Database high availability you can measure (L2, ~15 hours)

**Real-world inspiration:** managed database failovers are fast on paper but clients often see much longer outages because of DNS caching and stale connections; AWS's [RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) and similar poolers exist for this. The application is an *illustrative scenario*: a grocery-delivery order service with a 2-second checkout budget.

**What to build:** an order API on managed Postgres (RDS, Aurora, Cloud SQL, AlloyDB or Azure Database for PostgreSQL) with Multi-AZ HA, a pooling proxy, a read replica for order history, retry logic with idempotency keys, and dashboards for client-side errors and latency.

**Acceptance criteria:**
- During three forced failovers at 200 requests per second, no order is lost or duplicated, and client-visible errors last under 30 seconds per failover.
- Order-history reads go to the replica, but a user always sees their own new order immediately (read-your-writes solved and explained).
- A blue/green major-version upgrade completes with under 60 seconds of write unavailability.
- A written comparison of measured failover behaviour with and without the pooler.
- **Cost ceiling:** US$20; stop or delete instances between sessions.

**Stretch goals:** the same tests on Aurora DSQL or Spanner with two regions; measure write latency and conflict rates.

**What it proves to an employer:** you understand failover from the client's side, which is where real outages happen.

### P3 · A data platform for a regulated app, with a proven DR plan (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- RBI requires payment-system data to be stored only in India ([RBI, 2018](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244)).
- GitLab's 2017 outage showed backups that had never been restored ([GitLab](https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/)).
- Multi-region strong consistency became available in DynamoDB and Aurora DSQL in 2025.
- The company is an *illustrative scenario*: a UPI-linked wallet with a transaction ledger, user profiles, KYC documents, a search index and a support chatbot over policy documents.

**What to build:** a polyglot data layer chosen with written decision records:
- a relational ledger with HA, point-in-time recovery and idempotent writes;
- a key-value store for sessions and rate limits;
- encrypted object storage with Object Lock for KYC documents;
- a vector store for the chatbot's documents, with deletion propagation;
- backups copied to a separate, locked-down account in a second India region;
- a DR runbook for losing the primary region.

**Acceptance criteria:**
- **Residency:** every primary, replica, backup and log location is in India; an automated check fails the build otherwise.
- **DR drill:** simulate loss of the primary region and restore service from the second region. The ledger achieves RPO ≤ 5 minutes and RTO ≤ 60 minutes, measured, with zero duplicated or missing ledger entries after reconciliation.
- **Ransomware drill:** with the production admin role "compromised", show that backups and KYC objects cannot be deleted or overwritten.
- **Deletion:** deleting a user removes their profile, documents and embeddings, and a search no longer returns their data; produce an audit record.
- **Cost:** a monthly cost model at 1 million users, with the three biggest line items and one concrete optimisation each.
- **AI review:** a table of defects found in an AI-generated version of the schema and backup plan.
- **Cost ceiling:** US$40 total.

**Stretch goals:** a warm standby using multi-Region strong consistency and a cost comparison against backup-and-restore; crypto-shredding with per-user keys.

**What it proves to an employer:** you can design, protect and recover data under Indian regulation, the work behind cloud database engineer and data platform roles.

## Feeds into

- [OV06 Data Platform and Analytics Engineering](../../../../04_overlaps/OV06_data_platform_analytics_engineering/README.md): with DEN305 and DAN304.
- [CLD404 AI Infrastructure in the Cloud](../../year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md): storage for training datasets, checkpoints and vector search.
- [CLD402 Multi-Cloud, Hybrid Cloud and Migration](../../year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md): database migration at scale.
- [CLD403 FinOps](../../year_4/CLD403_finops_and_cloud_cost_engineering/README.md): storage and database cost optimisation.
