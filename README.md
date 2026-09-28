# ArkTS Benchmark for Generative Software Development

Research repository for the graduation research project:

> **Methods for constructing benchmarks for generative software development
> in low-resource programming languages**

The project focuses on **ArkTS** and investigates methods for constructing
and evaluating benchmarks for generative software development in a
low-resource programming language.

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
```

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/arkts-benchmark-nir.git
cd arkts-benchmark-nir
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the dataset

The dataset and original preprocessing pipeline are available in the
collaborative ArkTS-CodeSearch project:

https://github.com/hreyulog/arkts-codesearch

See `data/README.md` for dataset preparation instructions.

### 5. Run an experiment

Experiment-specific instructions are provided in the corresponding
experiment directory.

## Reproducibility

Experiments are organized to make the training and evaluation procedures
reproducible.

The repository separates:

1. Dataset and preprocessing work from the original collaborative project.
2. Benchmark preparation.
3. Model training.
4. Retrieval evaluation.
5. Experimental results and analysis.

Hardware and software configurations are documented alongside the
corresponding experiments.

## Attribution

This repository is part of a research project based on collaborative work.

The original ArkTS dataset construction and data-processing pipeline are
available in:

https://github.com/hreyulog/arkts-codesearch

Experimental results from the original collaborative work are distinguished
from experiments reproduced or conducted independently as part of this
research project.
