# CLD305 · Cloud Storage and Managed Databases

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [OV06 Data Platform and Analytics Engineering](../../../../04_overlaps/OV06_data_platform_analytics_engineering/README.md), [CLD404](../../year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md), [CLD402](../../year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md) |

Part of the [Cloud Engineering major](../../README.md). Database internals (B+trees, WAL, MVCC) are in [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), and schema and query design for applications in [BE303](../../../backend_engineering/year_3/BE303_data_modeling_and_storage_for_backends_postgres/README.md). This course is about running data in the cloud: choosing the service, sizing it, making it durable and recoverable, and paying the right amount for it.

## Why this course matters now

Data is the part of a cloud system you cannot redeploy. A lost VM is a nuisance; a lost database is a company-ending event, and backups you never restored are a hope, not a plan, as GitLab's January 2017 outage showed when several backup methods turned out not to work ([GitLab post-mortem](https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/)). Managed services have moved the frontier: Amazon Aurora DSQL (generally available May 2025) and DynamoDB global tables with multi-Region strong consistency (June 2025) give zero-RPO multi-region writes, S3 Vectors (December 2025) stores up to 2 billion vectors per index in object storage, and AWS Database Savings Plans (December 2025) cut database bills by up to 35%.

AI assistants generate schemas, queries and migration scripts quickly, and agents increasingly hold database credentials. They do not know your access patterns, your recovery objectives or your residency rules. India's RBI requires payment-system data to be stored only in India, and the DPDP Rules 2025 add retention and breach duties. The engineer who can choose the right store, prove a restore and explain the bill is the one trusted with production data.

## Learning outcomes

By the end you can:

1. **Explain** durability, availability and consistency for block, file and object storage, and **calculate** expected data loss for a replication or erasure-coding scheme.
2. **Configure** object storage for security, versioning, immutability, lifecycle and cost on AWS, Azure and Google Cloud.
3. **Size** block and file storage from IOPS, throughput and latency requirements, and **benchmark** it with `fio`.
4. **Operate** managed relational databases: high availability, failover, read replicas, connection pooling, major-version upgrades with blue/green deployments.
5. **Compare** distributed SQL (Spanner, Aurora DSQL) with single-region SQL and **quantify** the latency cost of multi-region consistency.
6. **Design** DynamoDB, Firestore or Cosmos DB tables from access patterns, and **choose** consistency levels deliberately.
7. **Implement** backups, point-in-time recovery, cross-account immutable copies and DR, and **prove** RPO and RTO with a timed restore.
8. **Choose** a data store with a written decision covering access patterns, consistency, scale, residency and cost.

## Chapters and lessons

### Chapter 1 · Durability, availability, consistency (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Three kinds of storage | Block, file and object: interfaces, semantics, where each is used | Classify 12 workloads and justify each |
| 1.2 Durability maths | Replication versus erasure coding, annual failure rates, repair time; what "11 nines" means and does not mean | Compute expected annual loss for 3-way replication and a 10+4 code |
| 1.3 Consistency in storage | S3 strong read-after-write consistency (since December 2020), list consistency, Azure and GCS semantics; what your app may still assume wrongly | Write a test that would have failed under old eventual consistency |
| 1.4 Failure domains | Single-AZ versus multi-AZ versus multi-region storage; S3 One Zone and Express One Zone trade-offs | Choose storage for a cache, a data lake and audit logs |

**Check your understanding:** (1) Why can a highly durable object store still be unavailable? (2) What does erasure coding cost in rebuild traffic? (3) Why is a single-AZ storage class sometimes the right choice?

### Chapter 2 · Object storage in depth (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Data model and API | Buckets, keys, prefixes, multipart upload, presigned URLs, request-rate scaling per prefix | Upload a 5 GB file with multipart and resume after a failure |
| 2.2 Concurrency control | Conditional writes (`If-None-Match`, `If-Match`), ETags, building a lock on object storage (as Terraform's `use_lockfile` does) | Implement a compare-and-swap counter on S3 or GCS |
| 2.3 Protection | Default encryption, KMS keys, Block Public Access, bucket policies, versioning, Object Lock (WORM) for ransomware protection | Make a bucket immune to deletion by its own admin for 7 days |
| 2.4 Classes and lifecycle | S3 classes from Standard to Glacier Deep Archive (minimum durations of 30, 90 and 180 days), Intelligent-Tiering; Azure hot, cool, cold and archive tiers with LRS/ZRS/GRS/GZRS; GCS classes, dual-region with turbo replication | Design lifecycle rules for logs kept 7 years and compute the cost |
| 2.5 Object storage as a platform | Event notifications, S3 Tables (Apache Iceberg), S3 Vectors (generally available December 2025, up to 2 billion vectors per index), Express One Zone for low-latency access | Store embeddings in S3 Vectors or pgvector and run a similarity query |

**Check your understanding:** (1) How does a conditional write prevent two writers from both "winning"? (2) Why can a lifecycle rule that moves small objects to an archive class raise your bill? (3) What does Object Lock stop that versioning alone does not?

### Chapter 3 · Block and file storage (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Performance model | IOPS, throughput, latency, queue depth; gp3's independent IOPS and throughput settings, io2 Block Express; Google Hyperdisk; Azure Premium SSD v2 and Ultra | Benchmark a volume with `fio` at three queue depths |
| 3.2 Snapshots | Incremental snapshots, crash versus application consistency, fast snapshot restore, cross-region copy | Restore a 100 GB volume and measure time to full performance |
| 3.3 Instance store and caches | Ephemeral NVMe, what survives stop/start, use as cache or scratch | Use instance store as a build cache safely |
| 3.4 Shared file systems | EFS, Filestore, Azure Files, FSx for Lustre and NetApp ONTAP; NFS semantics and performance modes | Compare small-file throughput on EFS and a block volume |

**Check your understanding:** (1) Why can a restored snapshot be slow on first read? (2) When does a database need provisioned IOPS? (3) Why is NFS a poor fit for some databases?

### Chapter 4 · Managed relational databases (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 What "managed" covers | Patching, backups, HA and monitoring versus schema, queries, connections and capacity (still yours) | Write the shared-responsibility table for RDS, Cloud SQL and Azure Database for PostgreSQL |
| 4.2 High availability | Multi-AZ instance and cluster deployments, synchronous standby, failover mechanics and DNS, Cloud SQL HA, Azure zone-redundant HA | Force a failover under load and measure client-visible downtime |
| 4.3 Aurora and AlloyDB | Shared distributed storage (Aurora keeps six copies across three AZs), fast replicas, Aurora Serverless v2, AlloyDB columnar engine; Azure HorizonDB (preview) | Compare replica lag on standard Postgres and Aurora or AlloyDB |
| 4.4 Connections and scaling | Connection limits, pooling (RDS Proxy, PgBouncer), read replicas and read-your-writes, vertical scaling | Overload a database with connections, then fix it with a pooler |
| 4.5 Upgrades and changes | Major-version upgrades, blue/green deployments, parameter changes, schema migrations without locks | Upgrade Postgres one major version with under 1 minute of write downtime |

**Check your understanding:** (1) Why does a failover often cause errors longer than the database's own switch time? (2) What does Aurora's storage design change about replicas? (3) Why can adding read replicas break a "read your own write" feature?

### Chapter 5 · Distributed SQL (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Spanner | TrueTime, external consistency, splits, multi-region configurations | Read the Spanner paper's commit-wait section and compute its latency cost |
| 5.2 Aurora DSQL | Active-active multi-region with strong consistency, a witness region, optimistic concurrency, Postgres compatibility limits | Run a write workload from two regions and measure conflicts and latency |
| 5.3 Open-source options | CockroachDB, YugabyteDB, TiDB; running them yourself versus managed | Compare one with Aurora DSQL on a feature checklist |
| 5.4 When it is worth it | Latency floor from speed of light and consensus; most apps need one region plus DR | Write a decision note for a UPI-style payment ledger versus a food-delivery menu service |

**Check your understanding:** (1) Why does strong consistency across Mumbai and Singapore cost tens of milliseconds per write? (2) What does optimistic concurrency do to hot rows? (3) Name a workload where multi-region strong consistency is clearly worth it.

### Chapter 6 · NoSQL and caches (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 DynamoDB fundamentals | Partition and sort keys, item size, on-demand versus provisioned capacity, hot partitions, adaptive capacity | Load-test a hot key and fix it with write sharding |
| 6.2 Access-pattern design | Single-table design, GSIs and their eventual consistency, transactions, TTL, Streams | Design tables for an order system from 10 listed queries |
| 6.3 Global tables | Multi-Region eventual (last writer wins) versus multi-Region strong consistency (exactly three regions, zero RPO, no transactions or TTL) | Show a lost update under eventual mode and its absence under strong mode |
| 6.4 Firestore and Cosmos DB | Firestore Native and Enterprise edition with MongoDB compatibility; Cosmos DB's five consistency levels and request units | Choose a Cosmos DB consistency level for three features |
| 6.5 Caches | ElastiCache and MemoryDB for Valkey, Memorystore, Azure Cache; cache-aside, write-through, stampedes | Add a cache and measure database load drop; then cause and fix a stampede |

**Check your understanding:** (1) Why can a well-provisioned DynamoDB table still throttle? (2) Why are GSI reads eventually consistent? (3) What does "session" consistency in Cosmos DB guarantee and to whom?

### Chapter 7 · Analytical and vector stores, in outline (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Warehouses and lakehouses | BigQuery, Redshift, Fabric/Synapse; columnar storage; open table formats (deep dive in DEN305 and DEN402) | Query the same Parquet data from a warehouse and from S3 Tables |
| 7.2 Vector storage choices | pgvector, OpenSearch, S3 Vectors, managed vector databases; latency and cost trade-offs | Benchmark recall and latency for 1 million vectors in two stores |
| 7.3 Operational versus analytical | Change data capture, zero-ETL integrations, why not to run analytics on the primary | Stream changes from Postgres to a warehouse |

**Check your understanding:** (1) Why is a columnar store slow for single-row lookups? (2) When is object storage good enough for vectors? (3) What breaks when analysts query the production primary?

### Chapter 8 · Backups, DR and ransomware resilience (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 RPO and RTO for data | Point-in-time recovery, log shipping, snapshot frequency; matching to business needs | Set RPO/RTO for five data stores with a product owner role-play |
| 8.2 Backup architecture | AWS Backup, Azure Backup, Google Backup and DR; cross-region and cross-account copies; logically air-gapped vaults; Object Lock | Build a backup plan whose copies the production admin cannot delete |
| 8.3 DR patterns | Backup and restore, pilot light, warm standby, multi-site active-active; failback | Choose and price a DR pattern for a 2 TB Postgres |
| 8.4 Restore drills | Timed restores, data validation, runbooks; the GitLab 2017 lessons | Lab 8: restore a database to a point 10 minutes before a bad delete |

**Check your understanding:** (1) Why is an untested backup not a backup? (2) What does an attacker with your production admin role do first? (3) Why is failback often harder than failover?

### Chapter 9 · Security, residency and data movement (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Encryption and keys | At rest and in transit, customer-managed keys, key policies, envelope encryption, rotation, crypto-shredding | Make data unreadable by disabling a key, then recover |
| 9.2 Access to data | IAM database authentication, secrets rotation, least privilege for apps and agents, audit logging | Give an app short-lived DB credentials with no password in config |
| 9.3 Residency in India | RBI's April 2018 directive that payment-system data be stored only in India; DPDP Rules 2025 obligations at outline level; region and replica placement | Audit P3's replicas and backups for residency |
| 9.4 Moving data | DMS and Database Migration Service, logical replication, bulk transfer (DataSync, Storage Transfer Service), cutover (deep dive in CLD402) | Migrate a Postgres database with under 1 minute of downtime |

**Check your understanding:** (1) Where can a cross-region backup silently break a residency rule? (2) Why does crypto-shredding help with deletion obligations? (3) What makes a database migration's cutover risky?

### Chapter 10 · Choosing a store and paying for it (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 A decision framework | Access patterns, consistency, latency, scale, operations, residency, cost, team skills | Write decisions for five product features |
| 10.2 Cost anatomy | Storage, requests, I/O, provisioned capacity, backups, cross-AZ and egress; Database Savings Plans and reserved capacity | Find the three biggest line items in a sample database bill |
| 10.3 Polyglot or not | When one Postgres is enough; the operational cost of each extra store | Remove one store from an over-engineered design and justify it |

**Check your understanding:** (1) Why is "Postgres until it hurts" often correct? (2) Which cost grows with reads but not data size? (3) What does each new data store cost the team in on-call load?

### Chapter 11 · AI and data stores (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Reviewing generated schemas and queries | Missing indexes, unbounded scans, wrong partition keys, N+1 queries; checking with `EXPLAIN` and load tests | Review 10 AI-generated schemas and queries and log defects |
| 11.2 Agents with database access | Read-only roles, row limits, query timeouts, separate dev and prod credentials (the July 2025 Replit deletion is the cautionary case) | Design a database access policy for a coding agent |
| 11.3 Data for AI | Storage for RAG corpora and embeddings, freshness, deletion propagation to vector stores | Prove a deleted document disappears from search results |

**Check your understanding:** (1) Why can a correct-looking query be dangerous at scale? (2) What is the minimum guardrail before an agent can run SQL in production? (3) Why does deletion in a vector store matter legally?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: durability maths and consistency test | Calculations and test |
| 2 | 2 | Lab 2: multipart, presigned URLs, conditional writes | CAS counter |
| 3 | 2 | Lab 3: protection and lifecycle | WORM bucket; P1 starts |
| 4 | 3 | Lab 4: `fio` benchmarks and snapshots | Performance table; P1 due |
| 5 | 4 | Lab 5: failover and pooling | Downtime measurements |
| 6 | 4 | Lab 6: blue/green major upgrade | Upgrade log; P2 starts |
| 7 | 5 | Distributed SQL experiment | Latency and conflict results |
| 8 | 6 | Lab 7: DynamoDB access-pattern design | Table design + load test |
| 9 | 6 | Global tables and caches | Lost-update demo; P2 due |
| 10 | 7 | Vector store benchmark | Recall/latency table |
| 11 | 8 | Lab 8: timed restore drill | RPO/RTO evidence; P3 starts |
| 12 | 9 | Keys, residency, migration | Residency audit |
| 13 | 10 | P3 build and cost model | Decision records |
| 14 | 11 | P3 completion | Demo and DR drill |
| 15 | Review and exam | — | Written exam and restore practical |

## Working with AI in this course

- **Use AI for:** drafting table designs from a list of access patterns (then load-testing them), explaining `EXPLAIN` plans, writing `fio` and load-test scripts, generating lifecycle and backup policies, summarising database engine release notes before an upgrade. Named tools: Claude Code, GitHub Copilot, Amazon Q Developer, Gemini in BigQuery, Copilot in Azure SQL Database.
- **Do without AI (drills):** durability arithmetic, DynamoDB key design for the Lab 7 query list, choosing RPO/RTO and DR patterns, and the timed restore practical.
- **Verify AI output by:** load-testing generated key designs for hot partitions; running `EXPLAIN ANALYZE` on generated queries against realistic data volumes; testing lifecycle rules on a copy; restoring every backup it configures; checking each quoted limit or price against the official page.
- **Where AI still fails here (show it):** assistants often pick low-cardinality partition keys, assume GSI reads are strongly consistent, quote outdated storage-class minimums, or propose cross-region replicas that break residency rules. Ask one to design DynamoDB tables for a ride-hailing app and test the design at 5,000 writes per second on a single city key.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Written exam (durability, consistency, key design, DR, cost) | 20% |
| Restore practical (no AI) | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) restore a managed database to a given point in time in a separate account, validate the data and report achieved RPO and RTO, all within 60 minutes; (b) design a DynamoDB or Cosmos DB schema from 8 unseen access patterns that survives a load test without hot-partition throttling; and (c) choose a data store for a new brief and defend it on consistency, latency, residency and monthly cost.

## Industry reality

Managed databases are where cloud bills and outages concentrate, which is why database specialists command premium pay. Indian payment companies must keep payment-system data in India under RBI's 2018 directive, and SEBI-regulated entities must use MeitY-empanelled providers, so replica and backup placement is a compliance question as well as a reliability one. Cloud providers keep adding multi-region strong consistency, but most production systems still run one primary region with tested backups and a warm standby.

Interview questions from this course:

1. **"Design storage for a photo-sharing app with 100 million users."** Cover object storage with presigned uploads, metadata in a database, CDN, lifecycle tiers, replication and cost per user per month.
2. **"Our database failed over and the app was down for 8 minutes. Why so long?"** Cover DNS TTLs and client caching, connection pools holding dead connections, retry behaviour, application health checks, and how pooling proxies help.
3. **"Design a DynamoDB table for an order system."** Cover access patterns first, partition and sort keys, GSIs and their consistency, hot keys, transactions and idempotency, TTL and streams.
4. **"How would you protect our data from ransomware?"** Cover immutable, cross-account backups, Object Lock, separate credentials, key management, restore drills and detection.
5. **"When would you choose Spanner or Aurora DSQL over Postgres?"** Cover multi-region write needs, latency costs of consensus, compatibility limits, operational simplicity and price.

## Resources (free first)

- **Documentation:** [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/), [S3 conditional writes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), [Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/), [DynamoDB global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html), [Cloud Storage](https://docs.cloud.google.com/storage/docs), [Spanner](https://docs.cloud.google.com/spanner/docs), [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy), [Cosmos DB consistency levels](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels).
- **Papers:** [Spanner](https://www.usenix.org/conference/osdi12/technical-sessions/presentation/corbett) (OSDI 2012); [Amazon Aurora](https://www.amazon.science/publications/amazon-aurora-design-considerations-for-high-throughput-cloud-native-relational-databases) (SIGMOD 2017); [Amazon DynamoDB](https://www.usenix.org/conference/atc22/presentation/elhemali) (USENIX ATC 2022).
- **DR:** [Disaster recovery of workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) (four DR strategies).
- **Courses:** CMU [15-445/645 Database Systems](https://15445.courses.cs.cmu.edu/) (free lectures) for the internals behind managed services.
- **Practising without a big bill:** run Postgres, Valkey and DynamoDB Local in containers for most labs; use object storage within free allowances; use the smallest burstable database class only during sessions, stop or delete it after, and remember that snapshots and backups keep billing after the database is gone.
- **Paid, worth it:** *Designing Data-Intensive Applications*, 2nd edition (Kleppmann and Riccomini, O'Reilly, 2026).

## Sources

All checked 12 Oct 2026.
- [S3 storage classes](https://aws.amazon.com/s3/storage-classes/) (durability, AZs, minimum storage durations, Express One Zone).
- [S3 Vectors GA](https://aws.amazon.com/blogs/aws/amazon-s3-vectors-now-generally-available-with-increased-scale-and-performance/) (2 Dec 2025).
- [Aurora DSQL GA](https://aws.amazon.com/blogs/aws/amazon-aurora-dsql-is-now-generally-available/) (May 2025).
- [DynamoDB global tables multi-Region strong consistency GA](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-dynamo-db-global-tables-multi-region-strong-consistency-generally-available/) (Jun 2025) and [how global tables work](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html).
- [AWS Cloud Financial Management re:Invent 2025 launches](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-cloud-financial-management-key-reinvent-2025-launches-to-transform-your-finops-practice/) (Database Savings Plans, up to 35%).
- [Firestore with MongoDB compatibility GA](https://cloud.google.com/blog/products/databases/firestore-with-mongodb-compatibility-is-now-ga); [InfoQ on Azure HorizonDB](https://www.infoq.com/news/2025/12/azure-horizondb-postgresql/) (preview).
- [GitLab database outage post-mortem](https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/) (Feb 2017).
- [RBI: Storage of Payment System Data](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244) (6 Apr 2018).

_Last reviewed: 2026-10_
