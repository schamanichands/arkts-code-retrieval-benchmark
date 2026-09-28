# ArkTS Benchmark for Generative Software Development

Research repository for the graduation research project:

> **Methods for constructing benchmarks for generative software development
> in low-resource programming languages**

The project focuses on **ArkTS** and investigates methods for constructing
and evaluating benchmarks for generative software development in a
low-resource programming language.

The main benchmark task considered in this repository is **code retrieval**:
given a natural-language description of a function, retrieve the most
relevant ArkTS implementation from a collection of candidate functions.

## Research context

This repository is based on the collaborative work behind:

> **ArkTS-CodeSearch: A Open-Source ArkTS Dataset for Code Retrieval**

The original dataset construction and ArkTS data-processing pipeline are
available in the collaborative project:

https://github.com/hreyulog/arkts-codesearch

This repository focuses on the **benchmark experiments, evaluation, and
reproducibility** aspects of the research project.

## Dataset

The benchmark uses the ArkTS-CodeSearch dataset containing **24,452
ArkTS functions** paired with corresponding documentation.

| Split | Examples |
|-------|---------:|
| Train | 19,561 |
| Validation | 2,445 |
| Test | 2,446 |
| **Total** | **24,452** |

The dataset was collected from public GitHub and Gitee repositories and
processed using an ArkTS parsing and extraction pipeline.

## Benchmark task

The primary task is **docstring-to-function retrieval**.

Given a natural-language description (docstring), the system retrieves
relevant ArkTS functions from a candidate collection.

Retrieval quality is evaluated using:

- Recall@1
- Recall@5
- MRR
- NDCG

The repository contains experiments with both lexical and semantic
retrieval approaches.

## Experiments

The experimental part of the project investigates the effect of
domain-specific training on ArkTS code retrieval.

The planned experiments include:

### Baseline retrieval

Evaluation of pretrained embedding models on the ArkTS retrieval task
without ArkTS-specific fine-tuning.

### ArkTS fine-tuning

Fine-tuning of embedding models using ArkTS docstring–function pairs.

The main configuration uses:

- **EmbeddingGemma-300M**
- maximum sequence length: **512**
- **Multiple Negatives Ranking Loss**
- learning rate: **2 × 10⁻⁵**
- training epochs: **2**
- mixed-precision training

### Additional experiments

The repository is intended to contain experiments on:

- training data size;
- TypeScript-to-ArkTS transfer;
- comparison of embedding models;
- lexical vs. semantic retrieval;
- different training configurations.

## Repository structure

```text
arkts-benchmark-nir/
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── README.md
│
├── experiments/
│   ├── README.md
│   ├── baseline/
│   ├── fine_tuning/
│   └── transfer/
│
├── evaluation/
│   ├── README.md
│   └── results/
│
├── configs/
│
├── results/
│   └── README.md
│
└── figures/
