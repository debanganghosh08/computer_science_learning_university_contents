# DSC402 · Labs and projects

Three rules apply to all work. **Humans label the gold set:** no model may label data it is scored against. **Every LLM run is reproducible:** record model name and version, date, prompt, parameters and cost. **Every population number has an interval:** prevalence and regression estimates built on model labels must use a correction (PPI or DSL) or explain why none is needed.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Unicode, scripts and language ID | Normalise a mixed-script corpus; IndicLID tagging; token counts per script for two tokenisers | Normalisation function with tests; token-cost table | 3 h |
| 2 · TF-IDF baselines and dictionaries | Word vs character n-grams; logistic regression and linear SVM; validate a keyword dictionary | Accuracy table; 20 top n-grams with one spurious example; dictionary precision and recall | 4 h (2 weeks) |
| 3 · Embeddings and topic stability | Three sentence-embedding models as linear-probe features and for retrieval on your labelled set; LDA and BERTopic on one corpus across five seeds | Learning curves (50 → 1,000 labels); retrieval recall@10; topic persistence table with three stable and three unstable topics explained | 6 h (2 weeks) |
| 4 · Annotation and agreement (AI off) | Write a codebook; two annotators label 200 items; κ and α; adjudication | Codebook v2; agreement statistics; disagreement analysis | 4 h |
| 5 · LLM labelling with schemas | Label 2,000 items and extract fields with JSON schemas; prompt variants; distil into a small encoder | Accuracy vs gold; label-change rate across prompts; distilled model's accuracy, cost and p95 latency | 5 h (2 weeks) |
| 6 · Error analysis and judge bias | Per-class, per-language, per-source errors with intervals; position bias test for a pairwise LLM judge | Error report; measured position-bias rate | 3 h |
| 7 · Prediction-powered inference | Prevalence of three categories: naive LLM, gold-only and PPI; gold-size planning | Estimates and intervals for each; recommended gold size | 3 h |
| 8 · Indic pipelines | IndicTrans2 translate-then-classify vs a multilingual model on IndicSentiment in three languages | Per-language accuracy with bootstrap intervals; cost comparison | 3 h |
| 9 · Extraction from judgments | Extract statute citations and outcomes from 200 Supreme Court judgments with source spans | Field-level precision and recall on 50 hand-checked documents | 4 h |
| 10 · PII redaction and cost routing | Redact PII from 1,000 tickets; route easy cases to a small model and hard ones to a large model | Redaction recall; cost saved vs accuracy lost | 3 h |

## Projects

### P1 · Complaint triage: three generations of NLP (L1, ~6 hours)

**Real-world inspiration.** Financial firms and regulators route consumer complaints by product and issue. The US Consumer Financial Protection Bureau publishes its complaint database, including consumer-written narratives for part of the complaints and the product and issue categories recorded with each complaint, so a classifier can be checked against real labels. Read the database's documentation on how narratives are published before using them.

**What to build.** A product-category classifier for complaint narratives, built three ways: TF-IDF with logistic regression, sentence embeddings with a linear probe, and zero-shot LLM classification with the category definitions in the prompt. Compare them on accuracy, cost, latency and stability.

**Acceptance criteria**
- A fixed, stratified test set of at least 2,000 narratives is created before any modelling.
- Macro-F1 and per-class recall are reported for all three approaches with bootstrap intervals.
- Cost per 10,000 documents and p95 latency are measured for each.
- The LLM approach is run with two prompt variants and the label-change rate is reported.
- A one-page recommendation chooses an approach for a team handling 50,000 complaints a month (illustrative) and justifies it.

**Stretch goals.** A routing design that sends only low-confidence cases to the LLM; distil the LLM into a small model trained on its labels.

**What it proves to an employer.** You choose NLP methods on evidence, including cost, rather than by default.

### P2 · Sentiment across Indian languages and Hinglish (L2, ~15 hours)

**Real-world inspiration.** Consumer brands, apps and public agencies in India receive feedback in many languages and in code-mixed romanised text. AI4Bharat's IndicSentiment provides sentiment-labelled product and service reviews written in English with translations into Indian languages. Because its Indic texts are translations, they under-represent how people actually write, so code-mixed text needs its own test data.

**What to build.** A sentiment measurement pipeline for three Indian languages plus Hinglish, with your own 300-item code-mixed gold set, comparing a multilingual encoder fine-tuned on IndicSentiment, translate-then-classify with IndicTrans2, and an LLM with a codebook prompt.

**Acceptance criteria**
- The code-mixed gold set is labelled by two people with a codebook; κ is reported and disagreements are adjudicated.
- Accuracy and macro-F1 are reported per language and for code-mixed text, with bootstrap intervals; no claim of one method beating another is made where intervals overlap substantially.
- An error analysis covers at least 50 errors grouped by cause (sarcasm, transliteration, mixed sentiment, translation loss).
- Cost per 10,000 texts is reported for each method.
- A prevalence estimate of negative sentiment in an unlabelled sample is reported with a PPI interval using your gold set.

**Stretch goals.** Add a fourth language; evaluate how romanised vs native-script input changes accuracy; test a small open-weight model run locally.

**What it proves to an employer.** You can measure opinion in India's real linguistic mix and say precisely how reliable each number is.

### P3 · A measurement study of Indian court judgments (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Researchers and legal-tech firms study court output to understand delays, outcomes and how laws are applied. Indian Supreme Court and High Court judgments are available on the AWS Open Data Registry, and the Development Data Lab publishes judicial data for research. Such studies stand or fall on extraction quality and on honest uncertainty.

**What to build.** A pre-registered study answering two or three population questions about a defined set of judgments (for example, the share of judgments in a period that cite a given statute, the distribution of case types, or the share of appeals allowed), using an LLM extraction pipeline, a human gold set, and corrected estimates.

**Acceptance criteria**
- The study plan (questions, population, fields, gold-set size, estimators) is committed before extraction at scale.
- The extraction schema covers at least six fields with source-span citations; field-level precision and recall on a gold set of at least 200 judgments are reported with intervals.
- Each population estimate is reported three ways (naive LLM, gold-only, PPI or DSL corrected), and the corrected interval achieves the planned width.
- Accuracy is reported by court, decade and document length, and any slice with notably lower accuracy is discussed.
- The pipeline records model versions and prompts, reruns end to end, and its total API cost is reported.
- A six-page report for a legal-research audience presents findings, limitations (coverage of the corpus, OCR errors, extraction errors) and data-use terms.

**Stretch goals.** Repeat extraction with a second model family and analyse disagreements; release the gold set and schema (where terms allow); a small dashboard of the corrected estimates.

**What it proves to an employer.** You can turn a large, messy document collection into defensible numbers, which is the core of text analytics in research, compliance and legal technology.

## Feeds into

- [DSC404 Data Science in Production](../DSC404_data_science_in_production_deployment_monitoring/README.md): the P1 or P2 pipeline is deployed with monitoring and periodic re-validation.
- [DSC501 Frontier Seminar](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md): inference with AI-generated data is a seminar topic; P3 is a natural seed for a paper.
- [AIE305 Evaluating LLM Systems](../../../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md): gold sets, judges and agreement transfer directly to LLM evaluation work.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): Indic-language measurement and legal text analytics are open thesis areas.
