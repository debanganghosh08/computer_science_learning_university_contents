# DSC402 · NLP and Text Analytics with LLMs

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [DSC302](../../year_3/DSC302_applied_machine_learning_for_data_scientists/README.md) (uses [DSC301](../../year_3/DSC301_statistical_inference_and_modeling/README.md) and [DSC305](../../year_3/DSC305_feature_engineering_and_model_evaluation/README.md)) | [DSC404](../DSC404_data_science_in_production_deployment_monitoring/README.md), [DSC501](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md), [AIE305](../../../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Data Science major](../../README.md). This course treats text as data for measurement and decisions: what share of complaints are about fraud, which issues are rising, what courts decide and why. Building LLM applications and agents is the AI Engineering major's subject ([AIE303](../../../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md)); transformer internals are in the Deep Learning major ([DLR303](../../../deep_learning/year_3/DLR303_sequence_models_and_transformers/README.md)).

## Why this course matters now

Large language models changed text analytics from a modelling problem into a measurement problem. Zero-shot ChatGPT labels beat crowd workers by about 25 percentage points on average across four annotation datasets, at under $0.003 per label (Gilardi et al., 2023), so many teams now label millions of documents with an LLM instead of training a custom classifier. The risk moved downstream: a classifier that is 90% accurate can still bias a prevalence estimate or a regression coefficient if its errors are correlated with what you study. Prediction-powered inference (Angelopoulos et al., *Science*, 2023) and design-based supervised learning (Egami et al., 2023) show how a small, carefully labelled sample restores valid confidence intervals. India adds scale and diversity: the Eighth Schedule lists 22 languages, AI4Bharat's IndicTrans2 translates among all of them, and code-mixed text such as Hinglish is the norm in reviews and social media. The skill that stays human is designing the measurement: the codebook, the gold set, the agreement study, the error analysis by language and group, and the statistical correction that turns noisy labels into a number a policy or product team can trust.

## Learning outcomes

By the end you can:

1. **Design** a text-measurement study: construct, codebook, sampling frame, gold set and validation plan.
2. **Normalise and process** text in Indic scripts and code-mixed language (Unicode normalisation, language identification, transliteration).
3. **Build** classical baselines (TF-IDF with linear models) and **compare** them with embedding and LLM approaches on accuracy, cost, latency and stability.
4. **Use** embeddings for similarity, clustering and topic discovery (BERTopic), and **evaluate** topics for stability and human interpretability.
5. **Run** an annotation study with inter-annotator agreement (Cohen's κ, Krippendorff's α) and adjudication.
6. **Label and extract** with LLMs using structured outputs, and **validate** them against gold data by class, language and source.
7. **Estimate** population quantities from LLM labels with valid uncertainty (prediction-powered inference, design-based supervised learning).
8. **Build** multilingual pipelines with Indic resources and **measure** performance per language.
9. **Operate** text analytics responsibly: PII redaction, cost control, drift across model versions and bias audits.

## Chapters and lessons

### Chapter 1 · Text as data and measurement (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Constructs and measures | What you want to know vs what the text shows; validity and reliability | Define "customer frustration" operationally in three ways and critique each |
| 1.2 Corpus construction | Sampling frames, selection bias in scraped data, time coverage, licences and terms | Document the sampling frame of a complaints corpus |
| 1.3 Tasks | Classification, extraction, clustering, scaling, retrieval; which one answers the question | Map ten business questions to text tasks |
| 1.4 Ethics and consent | Public vs personal text, re-identification, DPDP purpose limitation | Write a data-use note for a social-media study |

**Check your understanding:** (1) Why can a perfectly accurate classifier still measure the wrong thing? (2) How does scraping only one platform bias prevalence estimates? (3) What makes a text field "personal data" under India's DPDP Act?

### Chapter 2 · Text processing for many scripts (weeks 1–2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Unicode and normalisation | Code points, NFC/NFKC, zero-width joiners in Indic scripts | Find visually identical strings that compare unequal |
| 2.2 Tokenisation | Words, subwords (BPE, SentencePiece), token counts and LLM cost across scripts | Compare token counts for the same sentence in English, Hindi and Tamil |
| 2.3 Language ID and code-mixing | IndicLID for Indic languages and romanised text; mixed-script sentences | Tag 500 social-media posts by language and script |
| 2.4 Transliteration | Romanised Hindi and other languages; IndicXlit | Transliterate romanised reviews and measure the effect on a classifier |

**Check your understanding:** (1) Why can the same review cost twice as many tokens in one script as another? (2) What breaks if you lowercase or strip accents blindly in Indic text? (3) How should "acha tha but delivery late" be labelled for language?

### Chapter 3 · Classical text models (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Bag of words and TF-IDF | Vocabulary, n-grams, character n-grams for noisy text | Build a complaint classifier in 30 lines |
| 3.2 Linear models for text | Logistic regression and linear SVMs; reading coefficients | List the 20 most predictive n-grams and find a spurious one |
| 3.3 Dictionaries and rules | Keyword lists, regular expressions, their precision and recall | Validate a fraud-keyword dictionary against labels |
| 3.4 Why baselines matter | Cost, latency and stability vs LLMs | Benchmark TF-IDF + logistic regression vs an LLM on cost per 10,000 documents |

**Check your understanding:** (1) Why do character n-grams help on misspelt, code-mixed text? (2) What does a dictionary's high precision but low recall do to a prevalence estimate? (3) When would you ship TF-IDF instead of an LLM?

### Chapter 4 · Embeddings (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 From word vectors to sentence embeddings | Distributional semantics; contrastive sentence encoders | Retrieve near-duplicate complaints by cosine similarity |
| 4.2 Choosing an embedding model | MTEB, multilingual models, domain fit, dimension and cost | Compare three models on your own retrieval set, not only the leaderboard |
| 4.3 Embeddings as features | Linear probes, few-shot classification (SetFit), clustering | Train a linear probe with 50, 200 and 1,000 labels |
| 4.4 Embedding drift | Changing models changes vectors; re-indexing and version pinning | Measure how cluster assignments change across two embedding models |

**Check your understanding:** (1) Why can the MTEB leader underperform on your domain? (2) What happens to an index when you upgrade the embedding model? (3) When is a linear probe on embeddings enough?

### Chapter 5 · Topic modelling and discovery (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 LDA | Generative story, priors, choosing the number of topics | Fit LDA on parliamentary questions or news headlines |
| 5.2 BERTopic | Embeddings + UMAP + HDBSCAN + class-based TF-IDF; LLM topic labels | Fit BERTopic on the same corpus and compare |
| 5.3 Evaluating topics | Coherence metrics vs human judgement; stability across seeds and samples | Run five seeds and report which topics persist |
| 5.4 Topics over time | Dynamic topics, emerging issues, alerting | Detect a rising complaint theme month by month |

**Check your understanding:** (1) Why is a single topic-model run weak evidence? (2) What does an LLM-written topic label hide? (3) How would you validate that a "new" topic is not a model artefact?

### Chapter 6 · Annotation design and agreement (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Codebooks | Definitions, decision rules, examples and counter-examples, edge cases | Write a codebook for five complaint categories |
| 6.2 Agreement | Percent agreement vs Cohen's κ vs Krippendorff's α; prevalence effects | Two annotators label 200 items; compute κ and discuss disagreements |
| 6.3 Adjudication and gold sets | Resolving disagreements, gold-set size for a target precision | Build a 300-item adjudicated gold set |
| 6.4 Sampling what to label | Random, stratified and active sampling; how sampling affects later estimates | Plan a labelling budget for a rare category |
| 6.5 Annotation tools | Label Studio-style tools and AI4Bharat's Shoonya platform; annotator welfare and pay | Set up a labelling project and export with provenance |

**Check your understanding:** (1) Why can κ be low when agreement is 95%? (2) How large must a gold set be to estimate 3% prevalence within ±1 point? (3) Why does active sampling complicate prevalence estimation?

### Chapter 7 · LLMs for labelling and extraction (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Zero- and few-shot classification | Prompting with the codebook, label definitions, example selection | Label 2,000 complaints with an LLM using your codebook |
| 7.2 Structured outputs | JSON schemas, enumerations, nulls for "not stated"; refusing to guess | Extract seven fields from 500 documents into a validated schema |
| 7.3 Confidence and abstention | Self-reported confidence vs log-probabilities vs agreement across prompts or models | Compare three confidence signals against gold accuracy |
| 7.4 Sensitivity and reproducibility | Prompt wording, example order, temperature, model version | Measure label changes across five prompt variants |
| 7.5 Distillation | Training a small classifier on LLM labels for cost and latency | Distil the LLM into a fine-tuned small encoder and compare |

**Check your understanding:** (1) Why should "not stated" be an allowed output? (2) What does it mean if labels change across prompt wordings? (3) When is distillation worth the effort?

### Chapter 8 · Validating LLM outputs (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Accuracy against gold | Per-class precision and recall, confusion matrices, κ between LLM and humans | Full error analysis of the Chapter 7 labels |
| 8.2 Errors that matter | Errors correlated with language, source, length or group | Show accuracy by language and source with intervals |
| 8.3 LLM-as-judge | Using models to grade outputs; position, verbosity and self-preference biases (Zheng et al., 2023) | Measure position bias in a pairwise judge |
| 8.4 Contamination and version drift | Benchmarks seen in training; silent model updates | Re-run labels after a model version change and quantify the shift |

**Check your understanding:** (1) Why is overall accuracy not enough for a measurement study? (2) How would you detect that an LLM judge prefers longer answers? (3) What must you record so a labelling run can be reproduced?

### Chapter 9 · Statistical inference with model-generated labels (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Measurement error | How misclassification biases prevalence and regression estimates | Simulate bias from a 90%-accurate classifier with correlated errors |
| 9.2 Prediction-powered inference | Combining many model labels with a small gold sample for valid intervals (Angelopoulos et al., 2023) | Estimate complaint-category prevalence with PPI and compare with naive and gold-only |
| 9.3 Design-based supervised learning | Using LLM surrogates in downstream regressions (Egami et al., 2023) | Estimate a regression coefficient with and without correction |
| 9.4 Planning the gold sample | Trade-off between gold size and interval width | Choose the gold size that meets a ±2 point target |

**Check your understanding:** (1) Why does a more accurate model shrink a PPI interval? (2) What assumption about the gold sample does PPI need? (3) When is the naive estimate from LLM labels acceptable?

### Chapter 10 · Multilingual and Indic NLP (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Indic resources | AI4Bharat's IndicNLP catalog, IndicBERT v2 and IndicXTREME, IndicTrans2 (22 scheduled languages), the MILU benchmark; government platform Bhashini | Inventory resources for three languages you will use |
| 10.2 Translate-then-analyse vs native models | Error propagation through translation; cost; meaning loss | Compare translate-then-classify with a multilingual classifier on IndicSentiment |
| 10.3 Low-resource evaluation | Small test sets, intervals, per-language reporting | Report accuracy per language with bootstrap intervals |
| 10.4 Bias in Indian contexts | Caste, religion, region and gender stereotypes in models; the Indic-Bias benchmark | Probe a model for one stereotype category and report the method's limits |

**Check your understanding:** (1) When is translating to English first a reasonable choice? (2) Why can a language with 200 test items not support a fine-grained ranking? (3) What would make a bias probe misleading?

### Chapter 11 · Information extraction and document analytics (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 NER and relation extraction | Entities, relations, normalisation to IDs (statutes, places, companies) | Extract statutes cited in 200 judgments and normalise them |
| 11.2 PDFs, OCR and tables | Scanned government documents, layout, table extraction, OCR errors in Indic scripts | Extract a table from 50 scanned PDFs and measure cell accuracy |
| 11.3 Retrieval for analytics | Embedding search to find relevant documents before labelling; recall of retrieval (see AIE303) | Measure retrieval recall before extraction |
| 11.4 Long documents | Chunking, map-reduce extraction, citation of source spans | Extract fields with source-span citations and verify 50 by hand |

**Check your understanding:** (1) Why must extracted values point to source spans? (2) How does retrieval recall cap your extraction recall? (3) What OCR errors are common in Devanagari text?

### Chapter 12 · Text analytics in production, and ethics (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Pipelines and monitoring | Label distribution drift, language mix drift, cost dashboards, periodic re-validation | Design a monthly re-validation plan |
| 12.2 Cost and latency | Batch APIs, caching, small models for easy cases, routing hard cases to large models | Cut labelling cost by 70% with a router and measure accuracy loss |
| 12.3 Privacy | PII detection and redaction, data minimisation, retention; DPDP Rules 2025 timelines | Redact PII from 1,000 tickets and measure recall on a hand-checked set |
| 12.4 Reporting text findings | Prevalence with intervals, examples with consent, limitations | Write the P3 report's findings section |

**Check your understanding:** (1) What triggers a re-validation of an LLM labelling pipeline? (2) Which documents should go to the expensive model? (3) What can never be quoted verbatim in a public report?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1–2 | Lab 1 · Unicode, scripts and language ID | Measurement plan draft |
| 2 | 2–3 | Lab 2 · TF-IDF baselines | — |
| 3 | 3 | Lab 2 (cont.): dictionaries | — |
| 4 | 4 | Lab 3 · Embedding bake-off | **P1 due** |
| 5 | 5 | Lab 3 (cont.): Topic stability | — |
| 6 | 6 | Lab 4 · Annotation and agreement | Codebook |
| 7 | 7 | Lab 5 · LLM labelling with schemas | Mid-term (AI off) |
| 8 | 7 | Lab 5 (cont.): distillation | — |
| 9 | 8 | Lab 6 · Error analysis and judge bias | — |
| 10 | 9 | Lab 7 · Prediction-powered inference | **P2 due** |
| 11 | 10 | Lab 8 · Indic pipelines | — |
| 12 | 11 | Lab 9 · Extraction from judgments | P3 checkpoint |
| 13 | 12 | Lab 10 · PII redaction and cost routing | — |
| 14 | 12 | Report clinic | **P3 due** |
| 15 | Review | Measurement defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** labelling and extraction at scale (Claude, GPT-family, Gemini and open-weight models through their APIs); drafting codebook examples; generating regex and parsing code; translating with IndicTrans2; summarising topic clusters. Claude Code and GitHub Copilot speed up pipeline code.
- **Do without AI (drills):** writing the codebook and decision rules; labelling the gold set yourself (models must never label the gold data they are scored against); computing κ and interpreting it; designing the gold-sample size; the error analysis write-up. The mid-term and final are AI-off.
- **Verify AI output by:** (1) a held-out human gold set with per-class, per-language metrics and intervals; (2) prompt-variant and model-version stability checks; (3) source-span citations for every extracted field, with a random sample checked by hand; (4) PPI or DSL corrections for any population estimate; (5) recording model name, version, date, prompt and parameters for every run.
- **Where AI still fails here:** LLM judges show measurable position and verbosity biases (Zheng et al., 2023), and model labels can be accurate on average while their errors correlate with language or source, which biases downstream estimates. In Labs 6 and 8 you will measure both on your own data, including accuracy differences between English, Hindi and code-mixed text.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + measurement defence of P3 | 25% |

**Mastery gate.** You pass when you can: (1) given a new corpus and question, produce in one day a codebook, a gold-set plan, an LLM labelling pipeline and a prevalence estimate with a valid confidence interval; (2) show accuracy by language and source with intervals, and explain how errors could bias the estimate; (3) AI off, compute and interpret κ, size a gold sample, and critique a text-analytics report for measurement errors.

## Industry reality

Customer-support analytics, trust-and-safety, compliance monitoring, market research and policy research all now use LLMs to label text at scale, and the methodological literature on correcting LLM-label bias is growing fast (Angelopoulos et al., 2023; Egami et al., 2023). Indian-language technology has public infrastructure: AI4Bharat's open models and datasets (IndicTrans2, IndicBERT, IndicXlit, IndicLID, MILU) and the government's Bhashini platform. Public text corpora for practice include the US Consumer Financial Protection Bureau's complaint database and Indian Supreme Court and High Court judgments on the AWS Open Data Registry.

**Interview questions from this course**

1. *Classify 10 million support tickets into 30 categories. LLM or classifier?* Strong answer: starts with a codebook and gold set; benchmarks TF-IDF, embeddings + probe and LLM on accuracy, cost and latency; often uses the LLM to label and a distilled model to serve; plans monitoring and re-validation.
2. *The LLM labels are 92% accurate. Can we report "18% of tickets mention fraud"?* Strong answer: only with a correction; explains how correlated errors bias prevalence; uses PPI or a calibration on the gold set; reports an interval and per-segment accuracy.
3. *How do you validate an extraction pipeline on legal documents?* Strong answer: field-level gold set, exact and normalised matching, source-span citations, retrieval recall, per-court and per-language breakdowns, error taxonomy and human review of uncertain cases.
4. *Our reviews are in Hindi, English and Hinglish. How do you analyse sentiment?* Strong answer: language ID and transliteration, comparison of translate-then-classify vs multilingual models, per-language evaluation with intervals, code-mixed test items, and a decision based on the weakest language.
5. *Topic modelling shows a new complaint theme. Do you alert the business?* Strong answer: checks stability across seeds and samples, reads examples, validates with a quick labelling of a sample, quantifies growth with intervals, and frames it as a hypothesis until validated.

## Resources (free first)

- **Texts:** Jurafsky and Martin, *Speech and Language Processing*, 3rd ed. draft — https://web.stanford.edu/~jurafsky/slp3/ ; Hugging Face LLM Course — https://huggingface.co/learn/llm-course
- **Indic resources:** AI4Bharat — https://ai4bharat.iitm.ac.in/ ; IndicNLP catalog — https://github.com/AI4Bharat/indicnlp_catalog ; IndicTrans2 — https://github.com/AI4Bharat/IndicTrans2 ; IndicBERT v2 and IndicXTREME — https://github.com/AI4Bharat/IndicBERT ; IndicXlit — https://github.com/AI4Bharat/IndicXlit ; IndicLID — https://github.com/AI4Bharat/IndicLID ; MILU — https://github.com/AI4Bharat/MILU ; Indic-Bias — https://github.com/AI4Bharat/indic-bias ; Shoonya — https://github.com/AI4Bharat/Shoonya ; Bhashini — https://bhashini.gov.in/
- **Tools:** Sentence-Transformers — https://sbert.net/ ; MTEB leaderboard — https://huggingface.co/spaces/mteb/leaderboard ; BERTopic — https://maartengr.github.io/BERTopic/
- **Papers:** Gilardi et al. — https://doi.org/10.1073/pnas.2305016120 ; Angelopoulos et al., prediction-powered inference — https://arxiv.org/abs/2301.09633 ; Egami et al., design-based supervised learning — https://arxiv.org/abs/2306.04746 ; Zheng et al., LLM-as-a-judge — https://arxiv.org/abs/2306.05685
- **Data:** IndicSentiment — https://huggingface.co/datasets/ai4bharat/IndicSentiment ; CFPB Consumer Complaint Database — https://www.consumerfinance.gov/data-research/consumer-complaints/ ; Indian Supreme Court judgments (AWS Open Data) — https://registry.opendata.aws/indian-supreme-court-judgments/ ; Indian High Court judgments (AWS Open Data) — https://registry.opendata.aws/indian-high-court-judgments/ ; Development Data Lab judicial data — https://www.devdatalab.org/judicial-data
- **Paid, optional:** Grimmer, Roberts and Stewart, *Text as Data* (Princeton University Press, 2022), the standard text on measurement with text.

## Sources

- Gilardi, Alizadeh and Kubli, PNAS (2023) — https://doi.org/10.1073/pnas.2305016120 (checked 2026-10)
- Angelopoulos et al., "Prediction-powered inference", *Science* (2023) — https://doi.org/10.1126/science.adi6000 (checked 2026-10)
- Egami et al., "Using Imperfect Surrogates for Downstream Inference" (arXiv 2306.04746, 2023) — https://arxiv.org/abs/2306.04746 (checked 2026-10)
- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (arXiv 2306.05685, 2023) — https://arxiv.org/abs/2306.05685 (checked 2026-10)
- AI4Bharat GitHub organisation (IndicTrans2: "Translation models for 22 scheduled languages of India"; IndicXlit; IndicLID; MILU; Indic-Bias; Shoonya), repository descriptions as of 12 Oct 2026 — https://github.com/AI4Bharat (checked 2026-10)
- Sentence-Transformers 6.1 (PyPI, Sep 2026) — https://pypi.org/project/sentence-transformers/ (checked 2026-10)
- Press Information Bureau, DPDP Rules notified (Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 (checked 2026-10)

_Last reviewed: 2026-10_
