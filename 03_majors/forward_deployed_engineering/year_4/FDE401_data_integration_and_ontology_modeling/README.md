# FDE401 · Data Integration and Ontology Modeling

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [FDE301](../../year_3/FDE301_the_forward_deployed_engineer_role_mindset/README.md); assumes [FND115](../../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [FDE303](../../year_3/FDE303_rapid_integration_engineering_apis_legacy/README.md) | [FDE501](../../year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md), [FDE404](../FDE404_field_studio_three_simulated_customer/README.md), [OV06](../../../../04_overlaps/OV06_data_platform_analytics_engineering/) |

## Why this course matters now

Getting data out of systems (FDE303) is the easy half. The hard half is making it mean something: the same supplier spelled five ways across SAP, Tally and an Excel tracker; "customer" meaning a billing account in one system and a person in another; dates in three time zones; and no shared key. Palantir built its platform around this problem: its Ontology "sits on top of the digital assets integrated into the Palantir platform" and maps them to "real-world counterparts", with semantic elements (objects, properties, links) and kinetic elements (actions, functions) so that applications and AI work with business objects rather than raw tables. AI raises the stakes. An agent that answers "which suppliers are late?" is only as right as the definition of supplier, late and the joins underneath. Language models now draft schema mappings, suggest matches between records and generate data-quality rules quickly; they also merge two different people with similar names and invent relationships that are not in the data. This course teaches the durable methods: profiling, canonical models, probabilistic entity resolution, ontologies and knowledge graphs, domain standards, data quality contracts and governance, and how to ground AI systems in a model of the customer's business.

## Learning outcomes

By the end you can:

1. **Profile** an unfamiliar multi-source dataset and **report** quality problems with counts and examples.
2. **Design** a canonical data model and mapping specifications from several source systems, with versioning.
3. **Standardise** Indian and international identifiers, names, addresses and phone numbers, and **validate** formats such as GSTIN, PAN and IFSC.
4. **Implement** entity resolution with blocking and Fellegi–Sunter probabilistic matching (Splink), **choose** thresholds with clerical review, and **evaluate** with pairwise and cluster metrics.
5. **Model** a domain as an ontology (classes, properties, relations, constraints) using RDF/OWL/SHACL or a property graph, and **explain** when each is appropriate.
6. **Map** data to domain standards (HL7 FHIR, OMOP CDM, FIBO, GS1, LEI) and **justify** adopting or not adopting one.
7. **Define** data contracts and quality tests that run in pipelines, with quarantine and ownership.
8. **Ground** an AI assistant or agent in an ontology (typed objects, links and actions) and **measure** the effect on answer accuracy.
9. **Track** lineage and personal-data tags so that access policies and DPDP purpose limits can be enforced.

## Chapters and lessons

### Chapter 1 · Why integrated data is wrong (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Semantic heterogeneity | Same name, different meaning; different names, same meaning; units, currencies, fiscal years (April–March in India) | Find ten semantic conflicts between two illustrative ERP exports |
| 1.2 Identity problems | No shared keys; reused IDs; merged and split accounts; history | Diagram how one customer appears across four systems |
| 1.3 Time | Event time versus load time; time zones; slowly changing attributes | Fix a report that double-counts because of time-zone joins |
| 1.4 Cost of wrong joins | Fan-out joins, silent duplicates, revenue counted twice | Detect and fix a fan-out in a sales report |

**Check your understanding:** Why do integration bugs usually produce plausible numbers rather than errors? What is the first question to ask when two systems disagree about a customer count? Why does the Indian fiscal year matter to a global dashboard?

### Chapter 2 · Profiling messy data (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Profiling | Cardinality, null patterns, distributions, top values, format patterns; DuckDB SQL for profiling | Profile three public messy datasets and write a one-page report each |
| 2.2 Functional dependencies | Discovering keys and dependencies; violations as quality signals | Find candidate keys and three violated dependencies |
| 2.3 Outliers and sentinels | Placeholder values (`9999-12-31`, `NA`, `0`), test records in production | Build a sentinel detector and run it on all sources |
| 2.4 Profiling at scale | Sampling strategies; when a sample hides problems | Compare full-scan and sample profiles; report what the sample missed |

**Check your understanding:** Why profile before modelling? What does a column with exactly 1,000 distinct values in a million rows suggest? When is sampling dangerous?

### Chapter 3 · Canonical data models (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Canonical model pattern | A shared model between systems to avoid N×N mappings (Hohpe and Woolf); costs of over-generalising | Design a canonical "party, product, order, shipment, invoice" model for an illustrative distributor |
| 3.2 Mapping specifications | Source-to-target mappings with transformations, defaults and rejected values | Write mappings from three sources; review them with a classmate |
| 3.3 Operational versus analytical models | Normalised operational models, star schemas, wide tables for AI retrieval | Derive a star schema from your canonical model |
| 3.4 Versioning and evolution | Additive changes, deprecation, contracts with consumers | Plan a breaking change and its migration |

**Check your understanding:** When does a canonical model become a bottleneck? Why write mapping specs before code? What makes a change "breaking" for consumers?

### Chapter 4 · Standardisation and Indian identifiers (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Names | Transliteration variants (Mohammed, Mohammad, Md.), initials, honorifics, single-name records, script differences | Build a name normaliser and measure its effect on match rates |
| 4.2 Addresses | Free-text Indian addresses, landmarks, six-digit PIN codes, state and district names; geocoding limits | Parse 1,000 synthetic addresses; report unparseable patterns |
| 4.3 Identifiers with structure | GSTIN (15 characters: state code, PAN, entity number, check character), PAN (holder-type character), IFSC (bank code, branch code); validation versus verification | Write validators with tests; explain what each validation cannot prove |
| 4.4 Phones and emails | E.164 normalisation (+91), shared family numbers, role mailboxes | Normalise and flag shared contact points |
| 4.5 What not to store | Aadhaar numbers only where legally permitted and masked; minimising identifiers under DPDP purpose limits | Design a schema that matches records without storing raw sensitive identifiers (hashing with a secret key) |

**Check your understanding:** Why is a valid GSTIN format not proof that the business exists? How can normalisation increase false matches? Why hash identifiers with a secret key rather than a plain hash?

### Chapter 5 · Entity resolution I: blocking and comparison (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The problem | Deduplication versus record linkage; pairs explode as n²; precision versus recall costs | Estimate pair counts for 1 million records with and without blocking |
| 5.2 Blocking | Blocking keys, multiple blocking rules, sorted neighbourhood; measuring pairs completeness | Design blocking rules that keep 99% of true matches; measure reduction ratio |
| 5.3 Comparison functions | Exact, Jaro-Winkler, Levenshtein, token-based, phonetic (with care for Indian names), date and numeric tolerances | Compare five similarity measures on labelled name pairs |
| 5.4 Labelled data | Building a labelled pair set; clerical review guidelines; agreement | Label 300 pairs with a partner; compute agreement |

**Check your understanding:** Why does blocking trade recall for speed? Which similarity measure suits transposed first and last names? How many labelled pairs do you need to evaluate a matcher?

### Chapter 6 · Entity resolution II: probabilistic matching and evaluation (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Fellegi–Sunter | m and u probabilities, match weights, thresholds for match, possible match and non-match (Fellegi and Sunter, 1969) | Compute match weights by hand for five record pairs |
| 6.2 Splink | Expectation-maximisation training without labels, term-frequency adjustments, waterfall charts | Train a Splink model on synthetic supplier data; explain three decisions with waterfall charts |
| 6.3 Clustering | Transitivity, connected components, over-merging through chains; cluster-level review | Find and fix an over-merged cluster |
| 6.4 Evaluation | Pairwise precision and recall, cluster metrics, thresholds chosen by cost of each error type | Choose a threshold given that a false merge costs ten times a missed match |
| 6.5 Operating ER | Incremental resolution, stable IDs, human review queues, unmerge | Design a workflow for reviewing and unmerging entities |

**Check your understanding:** Why can a matcher with 99% pairwise precision still produce badly wrong clusters? How do term frequencies change the weight of a match on a common surname? Why must resolved IDs stay stable over time?

### Chapter 7 · Ontologies (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 What an ontology adds | Classes, properties, relations, constraints and meaning that applications share; versus a schema or a glossary | Model a hospital's patients, encounters, beds, staff and orders as classes and relations |
| 7.2 Semantic web standards | RDF triples, OWL 2 classes and properties, SHACL shapes for validation, SKOS for controlled vocabularies, schema.org | Encode your model in RDF/OWL; validate data with SHACL shapes |
| 7.3 Operational ontologies | Palantir's Ontology: object types, link types, action types and functions mapped onto datasets; actions with governance | Specify object, link and action types for a supply-chain use case in plain YAML |
| 7.4 Property graphs | Nodes, relationships and properties; Cypher queries; when a property graph is simpler than RDF | Load the same model into Neo4j; write five queries |
| 7.5 Modelling choices | Over-modelling, reification, time-varying relations, multiple classification | Review a classmate's ontology for three modelling errors |

**Check your understanding:** What can SHACL catch that a relational constraint cannot? Why do operational ontologies include actions, not only data? When does an ontology add cost without benefit?

### Chapter 8 · Domain standards (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Healthcare | HL7 FHIR resources (Patient, Encounter, Observation), OMOP Common Data Model for analytics; India's ABDM health data exchange | Map a synthetic hospital extract (Synthea) to FHIR resources |
| 8.2 Finance | FIBO concepts; Legal Entity Identifier (LEI); ISO 20022 message families (names only) | Map a counterparty table to LEI and FIBO concepts |
| 8.3 Supply chain | GS1 identifiers (GTIN for products, GLN for locations); UN/LOCODE | Normalise a product master with GTINs |
| 8.4 Adopt, adapt or ignore | Standards as vocabulary versus full compliance; cost and benefit | Write a one-page recommendation on adopting FHIR for a small clinic chain |

**Check your understanding:** Why do teams adopt a standard's vocabulary without its full complexity? What does LEI solve that a company name cannot? When is mapping to FHIR worth it for a customer?

### Chapter 9 · Data quality and contracts (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Quality dimensions | Completeness, validity, uniqueness, timeliness, consistency, accuracy; measurable rules for each | Write 20 rules across dimensions for your canonical model |
| 9.2 Tests in pipelines | Great Expectations, Soda Core and dbt tests; blocking versus warning checks; quarantine | Implement tests that block a bad load and quarantine rows |
| 9.3 Data contracts | Schema, semantics, quality and service levels agreed with producers (Open Data Contract Standard) | Write a contract for one source and test it |
| 9.4 Ownership | Producers own fixes; data stewards at the customer; escalation | Draft a RACI for data quality with the customer's teams |

**Check your understanding:** Why should a contract include semantics, not just schema? What happens when a quality check only warns? Who should fix a source-system data error, and how do you make it happen?

### Chapter 10 · Grounding AI in an ontology (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Typed tools | Agents that query objects and call actions instead of free SQL; fewer ways to be wrong | Expose three object types and one action as agent tools; compare with a text-to-SQL baseline on 40 questions |
| 10.2 Semantic layers | Metric definitions, join paths and descriptions as context for text-to-SQL | Add a semantic layer and measure the accuracy change |
| 10.3 Graph-based retrieval | GraphRAG (Edge et al., 2024): entity and community summaries; when graphs help retrieval | Compare vector retrieval and graph retrieval on 30 multi-hop questions |
| 10.4 LLM-assisted modelling | Drafting mappings, suggesting matches and rules; verifying with labelled data | Let an LLM propose 50 column mappings; measure precision against your mappings |
| 10.5 LLM-assisted entity resolution | LLMs as reviewers for "possible match" pairs; cost, consistency and bias | Use an LLM on 200 possible-match pairs; compare with human review |

**Check your understanding:** Why do typed object tools reduce agent errors compared with free SQL? Where does an LLM's match judgement fail on Indian names? How would you prove a semantic layer improved answers?

### Chapter 11 · Lineage, governance and personal data (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Lineage | Column- and dataset-level lineage; OpenLineage events | Emit lineage from your pipeline and trace one metric back to sources |
| 11.2 Personal-data tagging | Tagging fields by sensitivity; propagating tags through transformations | Tag your model and show tags surviving two transformations |
| 11.3 Access policies | Row-, column- and object-level access; purpose-based access for DPDP | Implement object-level access for two roles |
| 11.4 Deletion and correction | Rights requests across integrated systems; resolved entities | Execute a deletion request across sources and the resolved entity |

**Check your understanding:** Why does entity resolution complicate deletion requests? How does lineage help in an incident? What is purpose-based access and how would you enforce it?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Semantic conflicts and wrong joins | — |
| 2 | 2 | Lab 2 · Profiling report | — |
| 3 | 3 | Lab 3 · Canonical model and mappings | **P1 due** |
| 4 | 4 | Lab 4 · Normalisers and validators | — |
| 5 | 5 | Lab 5 · Blocking and labelled pairs | — |
| 6 | 6 | Lab 6 · Splink model and threshold choice | — |
| 7 | 7 | Lab 7 · Ontology in RDF/OWL/SHACL | Mid-term (AI off): ER and modelling |
| 8 | 7 | Lab 7 (cont.): property graph and operational ontology | — |
| 9 | 8 | Lab 8 · FHIR and GS1 mappings | **P2 due** |
| 10 | 9 | Lab 9 · Quality tests and contracts | — |
| 11 | 10 | Lab 10 · Typed tools versus text-to-SQL | — |
| 12 | 10 | Lab 10 (cont.): LLM-assisted mapping and ER | — |
| 13 | 11 | Lab 11 · Lineage, tags and deletion | — |
| 14 | Integration | P3 demonstration | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting mapping specifications and SHACL shapes, generating validators and test cases, writing Splink and DuckDB code, proposing candidate matches for review, summarising profiling output.
- **Do without AI (drills):** Fellegi–Sunter calculations by hand; ontology design on paper before tooling; threshold choice from an error-cost table; the mid-term and final.
- **Verify AI output by:** measuring every AI-proposed mapping or match against a labelled set; checking validators against known valid and invalid identifiers; running SHACL validation on generated shapes against deliberately broken data; reviewing every cluster an LLM proposes to merge.
- **Where AI still fails here (show it):** in Lab 10, record merges of different people with similar Indian names, invented relationships between entities, and plausible but wrong column mappings (for example, "date" mapped to the wrong date). Report error rates, not anecdotes.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (11) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 defence | 25% |

**Mastery gate.** You pass when you can, given four unfamiliar messy sources in one working day: (1) produce a canonical model with mapping specs and a profiling report; (2) resolve entities with a documented threshold, reporting pairwise precision and recall on a labelled sample (target ≥ 0.95 precision and ≥ 0.90 recall, or a written explanation of why not); (3) expose the result as typed objects to an AI assistant and show its accuracy on 20 business questions against a raw-table baseline.

## Industry reality

Palantir's platform documentation describes the Ontology as an operational layer with objects, links, actions and functions over integrated data. Probabilistic record linkage is used in government statistics and justice data; the UK Ministry of Justice publishes Splink as open source. Healthcare data exchange relies on HL7 FHIR internationally and in India's ABDM ecosystem; financial institutions use LEIs for counterparties; retailers and logistics firms use GS1 identifiers. Data contracts and in-pipeline quality tests are standard practice in modern data teams (see [DEN401](../../../data_engineering/year_4/DEN401_data_quality_observability_and_data_contracts/README.md)).

**Interview questions from this course**

1. *Merge supplier lists from three systems with no common key.* Strong answer: profiling; standardisation (names, GSTIN, addresses); blocking; probabilistic matching with labelled evaluation; threshold by error cost; clerical review; stable IDs; incremental updates.
2. *What is an ontology and why would an AI agent need one?* Strong answer: shared typed model of business objects, relations and permitted actions; agents call typed tools and actions instead of raw SQL; fewer ambiguous joins; governance and permissions attached to objects.
3. *Your dashboard shows revenue 12% higher than finance's number. Debug it.* Strong answer: checks definitions, time zones and fiscal calendars, fan-out joins, duplicates, currency, returns and cancellations; reconciles step by step; adds a test.
4. *How would you evaluate an entity resolution system?* Strong answer: labelled pairs including hard cases; pairwise and cluster metrics; threshold sensitivity; error-cost weighting; human review sample of merges; monitoring after launch.
5. *Should this hospital adopt FHIR for its integration?* Strong answer: depends on exchange partners, ABDM participation, available tooling and team skills; adopt the vocabulary first; map core resources; avoid full profile compliance unless needed.

## Resources (free first)

- **Ontology and graphs:** Palantir Ontology documentation — https://www.palantir.com/docs/foundry/ontology/overview/ ; W3C OWL 2 overview — https://www.w3.org/TR/owl2-overview/ ; SHACL — https://www.w3.org/TR/shacl/ ; SKOS — https://www.w3.org/TR/skos-reference/ ; schema.org — https://schema.org/ ; Neo4j GraphAcademy (free courses) — https://graphacademy.neo4j.com/ ; Microsoft GraphRAG — https://github.com/microsoft/graphrag
- **Entity resolution:** Splink — https://moj-analytical-services.github.io/splink/ ; Zingg — https://github.com/zinggAI/zingg ; Fellegi and Sunter, "A Theory for Record Linkage", *Journal of the American Statistical Association* 64 (1969)
- **Data quality and contracts:** Great Expectations — https://docs.greatexpectations.io/ ; Soda Core — https://github.com/sodadata/soda-core ; Open Data Contract Standard — https://bitol-io.github.io/open-data-contract-standard/ ; OpenLineage — https://openlineage.io/
- **Domain standards:** HL7 FHIR — https://hl7.org/fhir/ ; OMOP CDM — https://ohdsi.github.io/CommonDataModel/ ; FIBO — https://spec.edmcouncil.org/fibo/ ; GLEIF (LEI) — https://www.gleif.org/ ; GS1 standards — https://www.gs1.org/standards ; ABDM — https://abdm.gov.in/ ; Synthea synthetic patients — https://synthetichealth.github.io/synthea/
- **Tools:** DuckDB — https://duckdb.org/ ; Polars — https://pola.rs/
- **Paid, optional:** Peter Christen, *Data Matching* (Springer, 2012); Dean Allemang, James Hendler and Fabien Gandon, *Semantic Web for the Working Ontologist* (3rd ed., 2020).

## Sources

- Palantir, Ontology overview (documentation) — https://www.palantir.com/docs/foundry/ontology/overview/ (checked 2026-10)
- Fellegi and Sunter (1969), as above; Edge et al., "From Local to Global: A Graph RAG Approach to Query-Focused Summarization" (arXiv 2404.16130, 2024) — https://arxiv.org/abs/2404.16130 (checked 2026-10)
- UK Ministry of Justice, Splink documentation — https://moj-analytical-services.github.io/splink/ (checked 2026-10)
- Standards bodies' pages as listed under Resources (checked 2026-10)

_Last reviewed: 2026-10_
