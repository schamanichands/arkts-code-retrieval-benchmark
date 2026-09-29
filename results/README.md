# Experimental Results

This directory contains experimental results used in the NIR
on benchmarking generative software development for the low-resource
ArkTS programming language.

## Directory structure

### `raw/`

Raw JSON records of individual experiments and results reported
in the ArkTS-CodeSearch paper.

Files:

- `baseline_embeddinggemma.json` — zero-shot EmbeddingGemma-300M baseline.
- `fine_tuning_25.json` — fine-tuning with 25% of the ArkTS training data.
- `fine_tuning_50.json` — fine-tuning with 50% of the ArkTS training data.
- `fine_tuning_100.json` — fine-tuning with 100% of the ArkTS training data.
- `paper_table1.json` — results reported in Table 1 of the ArkTS-CodeSearch paper.
- `paper_table2.json` — results reported in Table 2 of the ArkTS-CodeSearch paper.

## Evaluation task

The benchmark evaluates docstring-to-function retrieval.

The test set contains 2,446 examples.

The main evaluation metrics are:

- Recall@1
- Recall@5
- MRR
- NDCG@5

## Controlled data-efficiency experiment

The 25%, 50%, and 100% experiments use the same model and
training configuration. The intended experimental variable is
the fraction of specialized ArkTS training data.

## Attribution

The `fine_tuning_25.json`, `fine_tuning_50.json`, and
`fine_tuning_100.json` files contain experiments conducted
as part of this NIR.

The `paper_table1.json` and `paper_table2.json` files contain
results reported in the joint ArkTS-CodeSearch paper and are
stored separately from the independent NIR experiments.
