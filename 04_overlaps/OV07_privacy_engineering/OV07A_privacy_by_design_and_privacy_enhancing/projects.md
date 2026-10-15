# OV07A · Labs and projects

All labs use synthetic data you generate, public research datasets released for this purpose (for example the UCI Adult dataset, MNIST and CIFAR-10), or data the course provides. Attacks are run only against your own models and releases. No lab touches real personal data or a third party's system. Lab 3 and the exams are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Privacy requirements and LINDDUN | Turn three notice promises of an illustrative food-delivery app into requirements, acceptance tests and a LINDDUN model | Tests running in CI; data-flow diagram; top-10 threats with mitigations | 7 h |
| 2 · Linkage attack and ARX | Re-identify records in a "de-identified" synthetic health file by joining quasi-identifiers to a synthetic voter roll; then apply 5-anonymity and l-diversity with ARX and attack again | Re-identification rate before and after; one attack that still works and why | 5 h |
| 3 · Mechanisms from scratch (no AI) | Laplace, Gaussian and randomised response with sensitivity derivations | Code, proofs, and empirical noise histograms matching theory (Kolmogorov–Smirnov p > 0.05 over 10⁵ draws) | 5 h |
| 4 · OpenDP release with accounting | Rebuild Lab 3's release in OpenDP with user-level contribution bounds; account 30 queries under zCDP | Notebook; total ε at δ = 10⁻⁶; error table per query | 6 h |
| 5 · RAPPOR and shuffling | Toy RAPPOR client and decoder; simulate shuffle amplification | Top-10 recovery accuracy at n = 10⁵ and 10⁶; effective-ε plot | 5 h |
| 6 · Membership inference, DP-SGD and auditing | LiRA against your own CIFAR-10 classifier; retrain with Opacus at ε ∈ {1, 4, 8}; audit the DP run | TPR at 0.1% FPR for each model; accuracy vs ε with 3 seeds; empirical ε lower bound | 10 h |
| 7 · Federated learning with secure aggregation | FedAvg on 100 non-IID simulated clients with Flower; pairwise-mask secure aggregation; DP on updates | Accuracy curves; proof (test) that the server never sees an individual update; dropout handling | 8 h |
| 8 · MPC, PSI and homomorphic encryption | Three-party average with additive shares; DH-style PSI at 10⁵ rows; CKKS dot product; SD-JWT age check | Correctness tests; latency and bandwidth table; a note on what each party learns | 9 h |
| 9 · Attestation and clean-room rules | Write an attestation policy (key released only to a measured image) in a local simulator; write clean-room query rules | Policy file with tests; three queries your rules reject and why | 4 h |
| 10 · Synthetic data attacks | Generate synthetic data with CTGAN and MST; run linkage and membership attacks on both | Attack success vs utility for each generator | 5 h |

## Projects

### P1 · Re-identification audit and safe aggregate release (L1, ~6 hours)

**Real-world inspiration:** re-identification of the Netflix Prize ratings (Narayanan and Shmatikov, 2008) and of hashed NYC taxi medallions (2014); minimum-cell-size rules used by statistical agencies.

**What to build:** an audit tool that takes a tabular release and a list of quasi-identifiers, reports uniqueness and k for every equivalence class, simulates a linkage attack against a reference file you provide, and produces a safe aggregate table using suppression and generalisation.

**Acceptance criteria:**
- Reports the share of unique records for every combination of up to 4 quasi-identifiers on a 100,000-row synthetic dataset in under 60 s on a laptop.
- The linkage simulation re-identifies at least 80% of planted unique records in the "naive" release and reports the rate for the protected release.
- The protected release achieves k ≥ 5 and l ≥ 3 (distinct l-diversity) for the sensitive column, verified by an independent check script.
- A one-page memo states which attack the protected release still allows (for example background knowledge) and recommends whether differential privacy is needed.

**Stretch goals:** add t-closeness; compare your output with ARX on the same configuration.

**What it proves to an employer:** you can show, not assert, whether a dataset is safe to share.

### P2 · Differentially private analytics service with a budget ledger (L2, ~15 hours)

**Real-world inspiration:** the US Census Bureau's published privacy-loss budget for 2020; LinkedIn's DP analytics API (Rogers et al., 2020); NIST SP 800-226's privacy hazards.

**What to build:** an HTTP service over a synthetic events table (at least 10 million events, 500,000 users) that answers count, sum, mean and histogram queries with user-level differential privacy using OpenDP (or another audited library). It keeps a per-analyst and global budget ledger, bounds each user's contribution, and refuses queries that would exceed the budget.

**Acceptance criteria:**
- **Guarantee:** every answer is produced by library mechanisms; no hand-written noise sampler exists in the codebase (a CI check enforces this).
- **Accounting:** the ledger's total matches an independent recomputation with the library accountant to within 10⁻⁶; a query that would push total ε past the policy limit (default ε = 2 per quarter at δ = 10⁻⁷) is refused with a clear error.
- **Contribution bounding:** a test inserts a "heavy" user with 10,000 events and shows the answer changes by no more than the declared sensitivity.
- **Utility:** for counts with true value ≥ 1,000, median relative error ≤ 5% at the default budget, reported per query type.
- **Audit:** every answered query is logged with analyst, mechanism, parameters and ε spent; an auditor report regenerates the budget from logs alone.

**Stretch goals:** a zCDP-to-(ε, δ) conversion view for non-experts; a DP synthetic-data endpoint using MST; a red-team test showing a difference attack fails.

**What it proves to an employer:** you can put differential privacy into a real service with accounting that survives an audit.

### P3 · Privacy-preserving ML pipeline with an independent audit (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Gboard's federated and DP-trained models (Hard et al., 2018; Xu et al., 2023); membership-inference evaluation at low false-positive rates (Carlini et al., 2022); SISA unlearning (Bourtoule et al., 2021).

**What to build:** a pipeline that trains a text or image classifier for an illustrative multi-hospital scenario in three modes: centralised, centralised with DP-SGD, and federated (at least 20 simulated clients, non-IID) with secure aggregation and DP. Add canary-based memorisation tests, a LiRA membership-inference audit, an erasure path (SISA shards or documented retrain), and a model card with a privacy section.

**Acceptance criteria:**
- **Guarantees stated precisely:** unit of privacy, ε, δ, accountant and sampling assumptions in the model card, reproduced by a script.
- **Attack results:** LiRA true-positive rate at 0.1% false-positive rate reported for all three modes with 95% bootstrap intervals; the DP modes reduce it by at least 50% against the non-private baseline, or the report explains why not.
- **Memorisation:** planted canaries (100, each inserted 1, 5 and 25 times) show exposure falling in the DP modes, plotted against insertion count.
- **Utility:** accuracy for each mode over 3 seeds with intervals; the privacy-utility trade-off is plotted at ε ∈ {1, 4, 8}.
- **Erasure:** removing one client's or one record's data completes within a stated time, and a test shows the retrained model no longer contains that record's canary signal.
- **Review:** a LINDDUN model of the pipeline and a peer audit by another team; all "high" findings fixed or accepted with an owner.
- **AI-error log:** at least five documented cases of AI-generated privacy code that ran but was wrong, each with the test that caught it.

**Stretch goals:** a TEE-based variant with an attestation policy; DP synthetic data for an external research partner with a release memo.

**What it proves to an employer:** you can build ML on personal data with guarantees you can measure, explain and defend in a review.

## Feeds into

[OV07B](../OV07B_data_protection_law_for_engineers_in_practice/README.md) uses P2's ledger and P3's model card in its DPIA and breach exercises. [DEN404](../../../03_majors/data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) connects these PETs to platform lineage, masking and erasure. The OV07 capstone in the [overlap README](../README.md) combines all three, and P3 can seed a [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) thesis on privacy auditing.
