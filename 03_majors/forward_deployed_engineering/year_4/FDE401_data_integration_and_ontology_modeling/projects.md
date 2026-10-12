# FDE401 · Labs and projects

Use synthetic or public data. Where data imitates Indian identifiers (GSTIN, PAN, phone numbers), generate it synthetically with valid formats and no real people or businesses. Every project ships a profiling report, mapping specifications, a labelled evaluation set with guidelines, the code, and a notebook that recomputes every headline number.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Semantic conflicts and wrong joins | Find ten semantic conflicts between two illustrative ERP exports; fix a fan-out join and a time-zone double count | Conflict table, before/after queries with row counts | 3 h |
| 2 · Profiling report | Profile three messy public datasets with DuckDB: nulls, cardinality, patterns, sentinels, candidate keys, violated dependencies | Three one-page reports, profiling SQL | 4 h |
| 3 · Canonical model and mappings | Design a canonical party/product/order/shipment/invoice model for an illustrative distributor; write mappings from three sources; derive a star schema | Model diagram, mapping specs, review notes | 5 h |
| 4 · Normalisers and validators | Name, address and phone normalisers; GSTIN, PAN and IFSC validators with tests; keyed hashing for sensitive identifiers | Code, test suite, note on what validation cannot prove | 4 h |
| 5 · Blocking and labelled pairs | Design blocking rules; measure pairs completeness and reduction ratio; label 300 pairs with a partner and compute agreement | Blocking analysis, labelled set, agreement statistic | 5 h |
| 6 · Splink model and threshold choice | Train a Fellegi–Sunter model with Splink; explain decisions with waterfall charts; choose a threshold from an error-cost table; fix an over-merged cluster | Notebook, threshold memo, cluster fix | 6 h |
| 7 · Ontology three ways | Model one domain in RDF/OWL with SHACL validation, in Neo4j as a property graph, and as object/link/action types in YAML | Three models, five queries each, SHACL report on broken data | 7 h |
| 8 · FHIR and GS1 mappings | Map a Synthea extract to FHIR resources; normalise a product master with GTINs | Mapping code, validation results, adoption recommendation | 4 h |
| 9 · Quality tests and contracts | 20 quality rules; blocking tests with quarantine in a pipeline; a data contract for one source | Test suite, contract file, quarantine demo | 4 h |
| 10 · Grounding AI | Typed object tools versus text-to-SQL on 40 questions; semantic layer effect; LLM-proposed mappings and LLM review of possible matches measured against labels | Accuracy tables, error analysis | 7 h |
| 11 · Lineage, tags and deletion | Emit OpenLineage events; tag personal data and propagate tags; execute a deletion request across sources and resolved entities | Lineage graph, tag propagation test, deletion log | 4 h |

## Projects

### P1 · Profiling and canonical model for a messy multi-source extract (L1, ~6 hours)

**Real-world inspiration.** Palantir's deployment strategists describe integrating a customer's ERP data to resolve shipment discrepancies (2022); Palantir's Ontology maps integrated datasets to real-world objects such as plants, products and orders.

**What to build.** From three provided synthetic extracts of an illustrative Kolkata-based distributor (an ERP order table, a Tally-style invoice export, a warehouse spreadsheet), produce a profiling report, a canonical model and mapping specifications, and load the canonical tables.

**Acceptance criteria**
- Profiling report lists at least 15 quality issues with counts and examples.
- Mapping specs cover every target field with source, transformation and rejection rule.
- Loaded canonical tables reconcile to source totals (orders, invoice amounts) within documented exclusions.
- A classmate reproduces your load from the README in under 30 minutes.

**Stretch goals.** Add a slowly changing dimension for customer addresses.

**What it proves to an employer.** You can make sense of an unfamiliar customer's data quickly and leave a model others can build on.

### P2 · Supplier and customer entity resolution with Indian data (L2, ~15 hours)

**Real-world inspiration.** The UK Ministry of Justice publishes Splink for linking records without unique identifiers; Indian businesses commonly hold the same counterparty under different spellings across GST, accounting and CRM systems (illustrative).

**What to build.** Resolve 200,000 synthetic counterparty records from four sources (GST purchase register, accounting ledger, CRM, procurement portal) for an illustrative manufacturer. Use standardisation, blocking and Splink; produce stable entity IDs, a review queue for possible matches, and an unmerge procedure.

**Acceptance criteria**
- Labelled evaluation set of at least 1,000 pairs (including hard cases: transliteration variants, shared phones, branch GSTINs of the same PAN); agreement reported.
- Pairwise precision ≥ 0.95 and recall ≥ 0.90 at the chosen threshold, or a written analysis of what limits them.
- Threshold justified with an error-cost table; cluster-level spot check of 50 clusters with no over-merge left unexplained.
- Incremental run: adding 5,000 new records preserves existing entity IDs except for documented merges.
- No raw sensitive identifier is stored in the resolved table; matching uses keyed hashes where needed.

**Stretch goals.** Compare Splink with an LLM reviewer on the possible-match band; report cost and agreement.

**What it proves to an employer.** You can solve the identity problem that sits under almost every enterprise AI deployment.

### P3 · An operational ontology that an AI agent can use (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Palantir's Ontology combines semantic elements (objects, properties, links) with kinetic elements (actions, functions) so applications and AI act on business objects with governance; GraphRAG (Edge et al., 2024) uses entity graphs to answer questions that span documents.

**What to build.** For an illustrative multi-hospital network in Kerala (synthetic data from Synthea plus synthetic staffing and bed data): integrate four sources into a canonical model mapped to FHIR resources where sensible; resolve patients across sources; define an operational ontology (object types such as Patient, Encounter, Bed, Ward, Clinician; link types; two action types such as "request bed transfer" with approval); enforce object-level access for two roles; expose it to an AI assistant as typed tools; and compare against a text-to-SQL baseline.

**Acceptance criteria**
- SHACL (or equivalent) validation runs in the pipeline and blocks invalid data; quality contract for each source.
- Patient resolution evaluated on a labelled set with precision and recall reported.
- On a 60-question evaluation (written and labelled before testing, including multi-hop questions), the ontology-grounded assistant beats the text-to-SQL baseline by a margin with a confidence interval, or you explain why not.
- Actions require approval and are audit-logged; a role without permission cannot see or act on restricted objects (tested).
- Lineage traces at least one answer back to source records; a deletion request is executed end to end.

**Stretch goals.** Add graph-based retrieval over discharge-summary text linked to the ontology and measure multi-hop answer accuracy.

**What it proves to an employer.** You can build the data foundation that makes AI deployments correct and governable, which is the core of FDE work at platform companies.

## Feeds into

- [FDE501 Frontier Seminar](../../year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md): ontologies and resolution pipelines are prime candidates for productising field patterns.
- [FDE404 Field Studio](../FDE404_field_studio_three_simulated_customer/README.md): each simulated customer needs a canonical model and entity resolution.
- [OV06 Data Platform and Analytics Engineering](../../../../04_overlaps/OV06_data_platform_analytics_engineering/): semantic layers and platform-scale data modelling.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): entity resolution and grounded agents are strong capstone topics.
