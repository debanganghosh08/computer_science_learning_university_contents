# OV07A · Privacy by Design and Privacy-Enhancing Technologies

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [SEC305](../../../03_majors/cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md), [PRO301](../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md), [DEN301](../../../03_majors/data_engineering/year_3/DEN301_data_modeling_and_warehousing/README.md); co-requisite [DEN404](../../../03_majors/data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) (runs in semester 8, so this course is self-contained) | [OV07B](../OV07B_data_protection_law_for_engineers_in_practice/README.md), [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [RES502](../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) |

## Why this course matters now

Hashing a phone number is not anonymisation, and removing names is not de-identification: the Netflix Prize data (2008), the AOL search logs (2006) and the New York City taxi trips (2014) were all re-identified after "anonymisation". The US Census Bureau protected the 2020 census with differential privacy at a published privacy-loss budget of ε = 19.61, and Google, Apple, Microsoft and LinkedIn have described differentially private telemetry or analytics in papers. India's DPDP Rules, 2025 name encryption, obfuscation, masking and virtual tokens among the "reasonable security safeguards" every data fiduciary must apply. AI assistants now write differential-privacy code, detect personal data with tools such as Microsoft Presidio, and draft threat models; they also get sensitivity calculations wrong, add noise per event when the promise is per user, and call pseudonymous data anonymous. The skill that keeps its value is knowing exactly what a PET guarantees, measuring it, and refusing a design whose guarantee is weaker than the promise made to users.

## Learning outcomes

By the end you can:

1. **Threat-model** a data flow with LINDDUN and turn each threat into a design change, a control or an accepted risk with an owner.
2. **Re-identify** records in a "de-identified" dataset by linkage on quasi-identifiers (in a lab, on synthetic or public research data), and **explain** why k-anonymity, l-diversity and t-closeness each fail.
3. **Implement** the Laplace, Gaussian and randomised-response mechanisms, **prove** their privacy guarantee for a given sensitivity, and **compute** total privacy loss under composition with a library accountant.
4. **Design** a user-level differentially private analytics release with contribution bounding and a budget policy, and **measure** its error.
5. **Audit** a trained model for membership inference and **train** it with DP-SGD, reporting the privacy-utility trade-off with confidence intervals.
6. **Build** a federated learning pipeline with secure aggregation and **explain** what it does and does not hide.
7. **Choose** between secure multi-party computation, private set intersection, homomorphic encryption, trusted execution and data clean rooms for a stated problem, with cost and trust assumptions written down.
8. **Evaluate** a synthetic dataset for fidelity, utility and privacy, and **decide** whether it may leave the organisation.

## Chapters and lessons

### Chapter 1 · Privacy engineering foundations (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What privacy protects | Solove's taxonomy of privacy harms (2006); Nissenbaum's contextual integrity (2004): a flow is wrong when it breaks the norms of its context | Classify 10 product features by the harm they risk |
| 1.2 Privacy is not security | Confidentiality vs linkability, inference, purpose creep and loss of control; encryption solves the first, not the rest | Find three privacy failures in a system that passes a security audit |
| 1.3 Privacy by design | Cavoukian's seven principles and their critique (vague, hard to test); ISO/IEC 31700-1:2023; NIST Privacy Framework 1.0 and its 2025 draft update | Rewrite three principles as testable requirements |
| 1.4 Privacy requirements | Promises in notices → requirements → tests; "privacy acceptance tests" in CI | Write five acceptance tests for a ride-hailing app's location promise |

**Check your understanding:** Why can a fully encrypted system still violate contextual integrity? Give a requirement that is privacy-by-design in name only, and fix it. Which of Solove's harms does aggregation of public data cause?

### Chapter 2 · Threat modelling and minimisation architecture (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 LINDDUN | Linking, Identifying, Non-repudiation, Detecting, Data disclosure, Unawareness, Non-compliance; threat trees over data-flow diagrams | LINDDUN model of a food-delivery app's order flow |
| 2.2 LINDDUN with STRIDE | Running privacy and security threat models together ([SAR302](../../../03_majors/security_architecture/year_3/SAR302_threat_modeling/README.md)); scoring and prioritising | Merge both models; remove duplicates; rank the top 5 |
| 2.3 Minimisation patterns | Collect less, aggregate early, process on device, keep short retention, separate identifiers from content (split knowledge) | Redesign a fitness app so the server never sees raw GPS traces |
| 2.4 Rotating and scoped identifiers | Per-purpose pseudonyms; the Apple/Google Exposure Notification design (2020) with identifiers rotating every 10–20 minutes; masked Aadhaar showing only the last four digits | Implement per-purpose keyed pseudonyms; show that two purposes cannot join |
| 2.5 Privacy-preserving telemetry | Counting without user IDs, coarse timestamps, sampling, thresholds before upload | Re-design a crash-reporting pipeline; list the joins it no longer allows |

**Check your understanding:** A design stores hashed emails "so we cannot see them". Which LINDDUN categories still apply? When does on-device processing move the risk rather than remove it? Why do rotating identifiers need rotation of every linkable field, not just the ID?

### Chapter 3 · De-identification and its failures (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Identifiers and quasi-identifiers | ZIP code, gender and birth date identify about 87% of the 1990 US population (Sweeney, 2000); 15 demographic attributes re-identify 99.98% of Americans in a model (Rocher et al., 2019) | Measure uniqueness of attribute combinations in a census-style synthetic dataset |
| 3.2 Linkage and sparse data | Netflix Prize de-anonymisation (Narayanan and Shmatikov, 2008); AOL search logs (2006); NYC taxi trips with reversible MD5 hashes (2014) | Link a "de-identified" ratings file to a public profile file (lab data) |
| 3.3 k-anonymity and successors | Generalisation and suppression (Sweeney, 2002); l-diversity's homogeneity and background-knowledge attacks; t-closeness; the ARX tool | Make a dataset 5-anonymous with ARX; then break it with a homogeneity attack |
| 3.4 Pseudonymisation in law and practice | GDPR's distinction; EDPB Guidelines 01/2025 on pseudonymisation (adopted for consultation Jan 2025); the CJEU's *EDPS v SRB* (4 Sept 2025): pseudonymised data may be non-personal for a recipient who cannot reasonably re-identify | Write the re-identification-risk argument for one data share, both directions |
| 3.5 Detecting personal data | Pattern, checksum and model-based detectors (Presidio); Indian identifiers (Aadhaar Verhoeff check, PAN format, UPI IDs); false negatives in free text | Measure Presidio's recall on 500 hand-labelled support tickets |

**Check your understanding:** Why does adding more attributes to a release make k-anonymity collapse? A dataset is 10-anonymous but every record in one class has the same diagnosis: what leaked? What has to be true for pseudonymised data to be non-personal for its recipient after *EDPS v SRB*?

### Chapter 4 · Differential privacy I: the definition and basic mechanisms (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Why answers leak | Reconstruction attacks: enough noisy-but-too-accurate answers reveal the data (Dinur and Nissim, 2003); the Census Bureau's reconstruction of 2010 microdata as motivation | Reconstruct a 20-row secret table from subset-sum queries |
| 4.2 The definition | Neighbouring datasets, (ε, δ)-DP, the "plausible deniability" reading; event-level vs user-level | Explain ε = 0.1, 1 and 10 as odds ratios |
| 4.3 Laplace and Gaussian mechanisms | Global sensitivity; Laplace for ε-DP; Gaussian for (ε, δ); clamping inputs to bound sensitivity | Implement both; verify noise scale empirically |
| 4.4 Randomised response | Warner (1965) as the original local mechanism; unbiased estimation from noisy answers | Estimate a sensitive proportion from 10,000 simulated responses |
| 4.5 Properties | Post-processing immunity, group privacy, basic composition | Show that rounding and clipping after noise keep the guarantee |

**Check your understanding:** Why is sensitivity a property of the query and the data domain, not of the dataset you happen to hold? What goes wrong if you clamp values after computing the sum? Why does ε = 10 still mean something, and what?

### Chapter 5 · Differential privacy II: composition, accounting and real deployments (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Composition | Basic and advanced composition; Rényi DP (Mironov, 2017) and zero-concentrated DP (Bun and Steinke, 2016) for tight accounting | Compare total ε for 100 Gaussian queries under three accountants |
| 5.2 Budgets in a product | Per-user, per-period budgets; contribution bounding; who may spend budget; refusing queries | Design a budget policy for a dashboard with 40 metrics |
| 5.3 Libraries | OpenDP, Google's differential-privacy library and PipelineDP, Tumult Analytics; why not to hand-roll samplers (floating-point attacks, Mironov 2012) | Rebuild your Chapter 4 release in OpenDP; compare outputs |
| 5.4 Deployments | US Census 2020 (ε = 17.14 persons, 2.47 housing units, total 19.61 for redistricting data); LinkedIn's Audience Engagements API (2020); Microsoft Windows telemetry (2017); Google COVID-19 Community Mobility Reports (2020) | Write a one-page comparison: unit of privacy, ε, mechanism, published error |
| 5.5 Evaluating guarantees | NIST SP 800-226 (Mar 2025): the differential-privacy pyramid and privacy hazards | Audit a vendor's DP claim against the NIST hazards checklist |

**Check your understanding:** Two teams each spend ε = 1 on the same users. What is the guarantee now, and who should have known? Why did the Census Bureau's choice of ε provoke debate among data users and privacy researchers alike? What does "user-level" require the system to know?

### Chapter 6 · Local differential privacy and the shuffle model (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Local DP | Noise added on the device so the server never sees true values; error grows with √n relative to central DP | Compare error of central vs local DP counts at n = 10⁴, 10⁶ |
| 6.2 RAPPOR | Bloom filters plus two-stage randomised response in Chrome (Erlingsson et al., 2014) | Implement a toy RAPPOR; recover the top-10 strings |
| 6.3 Apple's deployment and its critique | Apple's count-mean sketch and per-day budgets ("Learning with Privacy at Scale", 2017); Tang et al. (2017) on how budgets add up over days | Compute a month's total loss under a stated per-day ε |
| 6.4 The shuffle model | Prochlo's encode–shuffle–analyse architecture (Bittau et al., 2017); amplification by shuffling (Erlingsson et al., 2019) | Simulate amplification and plot effective ε vs n |

**Check your understanding:** When is local DP the only acceptable option despite its error? Why does a per-day ε hide a larger yearly loss? What trust does the shuffle model move, and to whom?

### Chapter 7 · Privacy in machine learning (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Memorisation | Models store rare training examples; extraction from GPT-2 (Carlini et al., 2021); why duplication and rare strings matter | Measure exposure of planted "canary" strings in a small language model you train |
| 7.2 Membership inference | Shadow models (Shokri et al., 2017); LiRA and evaluating at low false-positive rates (Carlini et al., 2022) | Run LiRA against your own image classifier; report TPR at 0.1% FPR |
| 7.3 DP-SGD | Per-example clipping and Gaussian noise (Abadi et al., 2016); Opacus; choosing clip norm, noise multiplier, sampling rate | Train with DP-SGD at ε = 1, 4, 8; plot accuracy vs ε with 3 seeds each |
| 7.4 Auditing DP training | Empirical lower bounds on ε from attacks (Jagielski et al., 2020; Nasr et al., 2021); bugs that break guarantees | Audit your own DP-SGD run; compare the empirical bound with the claimed ε |
| 7.5 Unlearning and its limits | SISA training (Bourtoule et al., 2021); approximate unlearning; why erasure requests make retraining design a privacy question | Implement SISA with 5 shards; measure retraining cost for one deletion |
| 7.6 LLM systems | Personal data in prompts, logs, fine-tuning sets and retrieval indexes; redaction before embedding; access-controlled retrieval | Build a RAG index that excludes restricted-purpose documents and prove it with tests |

**Check your understanding:** Why is average-case attack accuracy the wrong way to report membership inference? DP-SGD at ε = 8 loses 2 points of accuracy: what other levers do you have before raising ε? Why does an erasure request touch the model, not only the database?

### Chapter 8 · Federated learning and federated analytics (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 FedAvg | Local training, weighted averaging, non-IID data and client drift (McMahan et al., 2017) | Run FedAvg with Flower on 100 simulated non-IID clients |
| 8.2 Production example | Gboard next-word prediction (Hard et al., 2018) and DP federated training of Gboard models (Google, 2022; Xu et al., 2023) | Write the threat model the Gboard papers assume |
| 8.3 Secure aggregation | The server sees only the sum (Bonawitz et al., 2017); dropouts; cost | Implement pairwise-masking secure aggregation for 20 clients |
| 8.4 What FL does not hide | Gradient inversion attacks exist (Zhu et al., 2019); model updates are personal data; FL plus DP as the defence | Show that DP noise on updates reduces reconstruction quality in your lab setup |
| 8.5 Federated analytics | Counting and histograms across devices without collecting raw data | Federated top-k query with thresholds and DP noise |

**Check your understanding:** Why is "the data never leaves the device" not a privacy guarantee on its own? What does secure aggregation protect against, and what does it not? When would you choose federated analytics over local DP?

### Chapter 9 · Cryptographic PETs (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Secret sharing and MPC | Additive secret sharing, Beaver triples, garbled circuits (intuition); the Boston Women's Workforce Council wage-gap study computed with MPC (Lapets et al., 2018) | Compute an average salary across 3 parties with additive shares |
| 9.2 Private set intersection | Matching customers without revealing non-matches; Google's Private Join and Compute (2019) | Implement Diffie–Hellman-style PSI on two hashed lists; measure time at 10⁵ rows |
| 9.3 Homomorphic encryption | BFV and CKKS; noise budgets; OpenFHE and Microsoft SEAL; Apple's use of homomorphic encryption for Enhanced Visual Search (2024) | Encrypted dot product with CKKS; measure latency and error |
| 9.4 Zero-knowledge proofs and selective disclosure | Proving "over 18" without revealing birth date; selective-disclosure credentials (IETF SD-JWT, ISO/IEC 18013-5 mobile driving licence); Aadhaar paperless offline e-KYC as a share-less design | Build a selective-disclosure age check with an SD-JWT library |
| 9.5 Costs and trust | Communication rounds, latency, key management, malicious vs semi-honest models | Cost table for the same task under MPC, HE and a trusted third party |

**Check your understanding:** In the wage-gap study, what did each employer have to trust? Why does CKKS give approximate answers, and when is that unacceptable? What can a verifier still learn from a zero-knowledge age proof?

### Chapter 10 · Trusted execution, confidential computing and clean rooms (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 TEEs | Intel SGX and TDX, AMD SEV-SNP, Arm CCA, NVIDIA confidential computing on GPUs; what the hardware root of trust covers | Draw the trust boundary of a confidential VM |
| 10.2 Attestation | Evidence, verifier and relying party (IETF RATS, RFC 9334); releasing keys only to measured code | Write an attestation policy that releases a key only to a specific image hash |
| 10.3 Limits | Side channels (Foreshadow, 2018), rollback, operator access to logs and debug paths | List the attacks your design assumes away |
| 10.4 Private AI inference | Apple's Private Cloud Compute (2024): stateless nodes, no privileged access, verifiable transparency | Compare PCC's claims with a normal cloud LLM API, claim by claim |
| 10.5 Data clean rooms | Aggregate-only joins between companies; analysis rules, minimum thresholds and DP noise; residual risks | Design a clean-room query policy for an advertiser and a retailer |

**Check your understanding:** What exactly does a remote attestation prove? Why are minimum-count thresholds alone insufficient in a clean room? Which of PCC's guarantees can an outside researcher check, and how?

### Chapter 11 · Synthetic data and privacy-preserving release (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Generators | Statistical (copulas), deep (CTGAN, Xu et al., 2019) and marginal-based (MST, AIM) generators; the SDV library | Generate synthetic tables with three methods |
| 11.2 Synthetic is not automatically anonymous | Stadler, Oprisanu and Troncoso (2022): synthetic data without DP can leak outliers; or loses utility when it protects them | Run a linkage and a membership attack on your non-DP synthetic data |
| 11.3 DP synthetic data | MST won the 2018 NIST differential privacy synthetic data challenge; utility at fixed ε | Compare MST and CTGAN on 10 downstream queries at ε = 1 |
| 11.4 The release decision | Fidelity, utility and privacy metrics; a release memo with residual risk | Write and defend a release memo for a hospital dataset (illustrative) |

**Check your understanding:** Why can a synthetic dataset protect the average person but expose the outlier? When is DP synthetic data a better choice than a DP query interface? What would you need to see before signing a vendor's "privacy-safe synthetic data" claim?

### Chapter 12 · Choosing PETs and running privacy reviews (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 A PET decision matrix | Who must not learn what; trust assumptions; accuracy needs; cost; maturity; regulator guidance (ICO PETs guidance, 2023; UN PET Guide for official statistics, 2023) | Fill the matrix for four business problems |
| 12.2 Privacy reviews | Review checklists, launch gates, risk acceptance, re-review triggers | Run a 45-minute review of another team's design |
| 12.3 Communicating guarantees | Explaining ε and residual risk to product managers, lawyers and users without overclaiming | Write a user-facing explanation and a lawyer-facing one for the same release |
| 12.4 Integration | Handing PET choices to DEN404's platform controls and OV07B's legal analysis | Present P3 and answer review questions |

**Check your understanding:** For "two banks want to find shared fraudsters", which PETs fit and what does each assume? What evidence would make you reopen an approved privacy review? How do you explain ε = 1 to a product manager in two sentences without lying?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Privacy requirements and LINDDUN | Requirements and tests for one promise |
| 2 | 2 | Lab 1 (cont.) | Threat model |
| 3 | 3 | Lab 2 · Linkage attack and ARX | **P1 due** |
| 4 | 4 | Lab 3 · Mechanisms from scratch (no AI) | Mechanism proofs |
| 5 | 5 | Lab 4 · OpenDP release with accounting | Budget policy |
| 6 | 6 | Lab 5 · RAPPOR and shuffling | — |
| 7 | 7 | Lab 6 · Membership inference | Mid-term (AI off) |
| 8 | 7 | Lab 6 (cont.) · DP-SGD and auditing | DP-SGD trade-off report |
| 9 | 8 | Lab 7 · Federated learning with secure aggregation | **P2 due** |
| 10 | 9 | Lab 8 · MPC and PSI | — |
| 11 | 9 | Lab 8 (cont.) · CKKS and selective disclosure | — |
| 12 | 10 | Lab 9 · Attestation policy and clean-room rules | Clean-room design |
| 13 | 11 | Lab 10 · Synthetic data attacks | Release memo |
| 14 | 12 | Peer privacy reviews | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** scaffolding experiments (data generators, plotting, Flower and Opacus boilerplate); explaining a proof step; drafting LINDDUN threat lists that you then prune and justify; translating a guarantee into plain language for a first draft. Claude, ChatGPT and Gemini handle these; Claude Code, GitHub Copilot or OpenAI Codex can wire up the lab harnesses.
- **Do without AI (drills):** sensitivity derivations and privacy proofs for every mechanism; composition arithmetic; the Lab 3 mechanisms; the mid-term and final. You cannot audit an accountant you cannot reproduce by hand.
- **Verify AI output by:** (1) recomputing sensitivity from the data domain, not from the sample; (2) checking that the unit of privacy (event or user) matches the promise; (3) comparing any hand-written noise sampler with a library's output distribution and replacing it with the library; (4) running an attack (linkage, membership inference, canary exposure) against the claimed protection; (5) checking every cited paper and guideline exists and says what is claimed.
- **Where AI still fails here (collect your own evidence):** in this course you keep a log of AI-generated privacy code that runs but is wrong. Classify each case: wrong sensitivity, missing contribution bounding, per-event instead of per-user noise, noise added before clamping, ε summed incorrectly, "anonymous" used for pseudonymous data. Your log is part of the P3 report.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, auto-graded where possible, short write-ups) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off): mechanisms, sensitivity, composition | 10% |
| Final exam (AI off) + oral defence of P3 | 30% |

**Mastery gate.** You pass when you can, with AI tools off: (1) given a query and a data domain, derive its sensitivity and the noise needed for a stated (ε, δ), and compute the total loss of a 20-query workload under zCDP; (2) given a dataset release, demonstrate a re-identification or membership attack, or argue with evidence why one is infeasible; (3) choose a PET for an unseen two-party data problem and state its trust assumptions and costs in one page that a reviewer accepts.

## Industry reality

Where this is used (all public): the US Census Bureau's 2020 Disclosure Avoidance System (TopDown algorithm); LinkedIn's differentially private Audience Engagements API (Rogers et al., 2020); Microsoft's private Windows telemetry (Ding, Kulkarni and Yekhanin, NeurIPS 2017); Chrome's RAPPOR (2014); Apple's local differential privacy (2017) and its homomorphic-encryption lookups (2024); Gboard's federated and DP-trained language models (2018–2023); Google's Private Join and Compute (2019); Apple's Private Cloud Compute (2024). In India, UIDAI requires Aadhaar numbers to sit in an Aadhaar Data Vault with only reference keys in business systems ([DEN404](../../../03_majors/data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) covers the platform side), and the DPDP Rules list masking, obfuscation and virtual tokens among required safeguards.

**Interview questions from this course**

1. *We hash user emails before sending them to our analytics vendor. Is that anonymous?* Strong answer: no; emails are enumerable or matchable by anyone with the same hash; it is pseudonymisation; propose a keyed hash with key held internally, or aggregate-only export, and name the residual linkage risk.
2. *Design a dashboard of "daily active users by city" with differential privacy.* Strong answer: defines user-level privacy, bounds each user's contribution, chooses a mechanism and budget per day, accounts for composition over the year, suppresses or thresholds tiny cities, reports expected error.
3. *How would you show that our model does not leak training data?* Strong answer: canary exposure and LiRA membership inference reported at low false-positive rates, compared with a DP-SGD baseline; explains why average accuracy hides the risk.
4. *Two hospitals want to train a model together without sharing records. Options?* Strong answer: federated learning with secure aggregation and DP; alternatively a TEE with attestation, or MPC for simple models; compares trust, cost, non-IID data and governance.
5. *A vendor sells "privacy-safe synthetic data". What do you ask?* Strong answer: whether it is differentially private and at what ε; attack evaluations (linkage, membership, outliers); utility on your queries; what happens to rare records; who holds the generator.

## Resources (free first)

- **Primary texts:** Dwork and Roth, *The Algorithmic Foundations of Differential Privacy* (free PDF) — https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf ; Near and Abuah, *Programming Differential Privacy* (free online book) — https://programming-dp.com/
- **Guidance:** NIST SP 800-226 — https://csrc.nist.gov/pubs/sp/800/226/final ; NIST Privacy Framework — https://www.nist.gov/privacy-framework ; LINDDUN — https://linddun.org/
- **Libraries and tools:** OpenDP — https://docs.opendp.org/ ; Opacus — https://opacus.ai/ ; Flower — https://flower.ai/docs/ ; OpenFHE — https://openfhe.org/ ; ARX — https://arx.deidentifier.org/ ; Microsoft Presidio — https://microsoft.github.io/presidio/ ; SDV — https://docs.sdv.dev/
- **Design references:** Apple Private Cloud Compute — https://security.apple.com/blog/private-cloud-compute/ ; Apple, Learning with Privacy at Scale — https://machinelearning.apple.com/research/learning-with-privacy-at-scale
- **Cryptography background:** Boneh and Shoup, *A Graduate Course in Applied Cryptography* (free draft) — https://toc.cryptobook.us/
- **Paid, optional:** none needed; the free texts above cover the course.

## Sources

All checked October 2026.

- Census Bureau, 2020 Census key parameters (9 Jun 2021): ε = 19.61 total; 17.14 persons, 2.47 housing units — https://www.census.gov/newsroom/press-releases/2021/2020-census-key-parameters.html
- NIST SP 800-226, *Guidelines for Evaluating Differential Privacy Guarantees* (Mar 2025) — https://csrc.nist.gov/pubs/sp/800/226/final
- Sweeney, "Simple Demographics Often Identify People Uniquely" (2000); Sweeney, "k-anonymity" (2002); Narayanan and Shmatikov, IEEE S&P 2008 — https://arxiv.org/abs/cs/0610105 ; Rocher, Hendrickx and de Montjoye, *Nature Communications* 10, 3069 (2019) — https://www.nature.com/articles/s41467-019-10933-3
- CJEU, *EDPS v SRB*, C-413/23 P (4 Sept 2025), summarised by Clifford Chance — https://www.cliffordchance.com/insights/resources/blogs/talking-tech/en/articles/2025/09/pseudonymized-data-after-edps-v-srb.html
- Dinur and Nissim, PODS 2003; Mironov, "Rényi Differential Privacy" (2017) — https://arxiv.org/abs/1702.07476 ; Bun and Steinke, zCDP (2016) — https://arxiv.org/abs/1605.02065
- Erlingsson, Pihur and Korolova, RAPPOR (CCS 2014) — https://arxiv.org/abs/1407.6981 ; Tang et al., Apple's DP implementation (2017) — https://arxiv.org/abs/1709.02753 ; Erlingsson et al., amplification by shuffling (2019) — https://arxiv.org/abs/1811.12469
- Rogers et al., LinkedIn Audience Engagements API (2020) — https://arxiv.org/abs/2002.05839 ; Ding, Kulkarni and Yekhanin, telemetry (NeurIPS 2017) — https://arxiv.org/abs/1712.01524 ; Aktay et al., Google mobility reports (2020) — https://arxiv.org/abs/2004.04145
- Abadi et al., DP-SGD (2016) — https://arxiv.org/abs/1607.00133 ; Shokri et al. (2017) — https://arxiv.org/abs/1610.05820 ; Carlini et al., LiRA (2022) — https://arxiv.org/abs/2112.03570 ; Carlini et al., extraction (2021) — https://arxiv.org/abs/2012.07805 ; Jagielski et al. (2020) — https://arxiv.org/abs/2006.07709 ; Bourtoule et al., SISA (2021) — https://arxiv.org/abs/1912.03817
- McMahan et al., FedAvg (2017) — https://arxiv.org/abs/1602.05629 ; Hard et al., Gboard (2018) — https://arxiv.org/abs/1811.03604 ; Bonawitz et al., secure aggregation (2017) — https://eprint.iacr.org/2017/281 ; Xu et al., Gboard with DP (2023) — https://arxiv.org/abs/2305.18465 ; Zhu, Liu and Han, gradient leakage (2019) — https://arxiv.org/abs/1906.08935
- Apple Machine Learning Research, "Combining Machine Learning and Homomorphic Encryption in the Apple Ecosystem" (Oct 2024) — https://machinelearning.apple.com/research/homomorphic-encryption ; Apple Security Research, Private Cloud Compute (Jun 2024) — https://security.apple.com/blog/private-cloud-compute/
- Stadler, Oprisanu and Troncoso, "Synthetic Data – Anonymisation Groundhog Day" (USENIX Security 2022) — https://arxiv.org/abs/2011.07018 ; McKenna, Miklau and Sheldon, MST (2021) — https://arxiv.org/abs/2108.04978
- IETF RFC 9334, Remote ATtestation procedureS (RATS) Architecture (Jan 2023) — https://www.rfc-editor.org/rfc/rfc9334
- DPDP Rules safeguards and UIDAI Aadhaar Data Vault: see the sources of [DEN404](../../../03_majors/data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md)

_Last reviewed: 2026-10_
