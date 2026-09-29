# Evaluation

This directory contains documentation and utilities for evaluating the
ArkTS code retrieval benchmark.

## Task

The benchmark evaluates **docstring-to-function retrieval**.

For each test example, a natural-language docstring is used as a query and
the corresponding ArkTS function is the relevant document.

The candidate collection contains all functions from the fixed test set.

## Evaluation procedure

1. Encode all test docstrings using the embedding model.
2. Encode all test functions using the same model.
3. Compute cosine similarity between every query and candidate function.
4. Rank candidate functions by similarity.
5. Determine the rank of the correct function.
6. Aggregate the ranks using the benchmark metrics.

Embeddings are normalized before similarity computation, so cosine
similarity is calculated as the dot product between normalized embeddings.

## Metrics

### Recall@1

The proportion of queries for which the correct function is ranked first.

### Recall@5

The proportion of queries for which the correct function appears among the
top five retrieved functions.

### Mean Reciprocal Rank (MRR)

The mean reciprocal rank of the correct function across all queries.

### NDCG@5

Normalized Discounted Cumulative Gain calculated at rank 5.

## Test set

All experiments use the same fixed test split containing **2,446 examples**.

The test set is not modified between experiments, allowing the results of
different training configurations to be compared directly.

## Reproducibility

The evaluation procedure is implemented in:

`experiments/fine_tuning/evaluate_embeddinggemma.py`

The same evaluation procedure is used for the zero-shot and fine-tuned
EmbeddingGemma experiments.
