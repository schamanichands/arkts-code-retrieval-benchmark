import argparse
import json
import os

import numpy as np
from datasets import load_dataset
from sentence_transformers import SentenceTransformer


def recall_at_k(ranks, k):
    return float(np.mean(ranks < k))


def mean_reciprocal_rank(ranks):
    return float(np.mean(1.0 / (ranks + 1)))


def ndcg_at_k(ranks, k):
    scores = []

    for rank in ranks:
        if rank < k:
            scores.append(1.0 / np.log2(rank + 2))
        else:
            scores.append(0.0)

    return float(np.mean(scores))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--model",
        default="google/embeddinggemma-300m",
    )

    parser.add_argument(
        "--dataset",
        default="hreyulog/arkts-code-docstring",
    )

    parser.add_argument(
        "--output",
        required=True,
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=32,
    )

    args = parser.parse_args()

    # Load dataset
    print("Loading dataset...")

    dataset = load_dataset(args.dataset)
    test_dataset = dataset["test"]

    docstrings = test_dataset["docstring"]
    functions = test_dataset["function"]

    print(f"Test examples: {len(test_dataset)}")

    # Load pretrained model
    print(f"Loading model: {args.model}")

    model = SentenceTransformer(
        args.model,
        device="cuda" if __import__("torch").cuda.is_available() else "cpu",
    )

    model.max_seq_length = 512

    # Encode queries
    print("Encoding docstrings...")

    query_embeddings = model.encode(
        docstrings,
        batch_size=args.batch_size,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    # Encode documents
    print("Encoding functions...")

    document_embeddings = model.encode(
        functions,
        batch_size=args.batch_size,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    # Validate embeddings
    if not np.isfinite(query_embeddings).all():
        raise ValueError("Invalid values detected in query embeddings")

    if not np.isfinite(document_embeddings).all():
        raise ValueError("Invalid values detected in document embeddings")

    # Cosine similarity
    print("Computing similarity matrix...")

    similarity = query_embeddings @ document_embeddings.T

    if not np.isfinite(similarity).all():
        raise ValueError("Invalid values detected in similarity matrix")

    # Ranking
    print("Computing rankings...")

    ranks = []

    for query_index in range(len(test_dataset)):
        ranking = np.argsort(-similarity[query_index])

        rank = int(
            np.where(ranking == query_index)[0][0]
        )

        ranks.append(rank)

    ranks = np.asarray(ranks)

    # Metrics
    metrics = {
        "recall@1": recall_at_k(ranks, 1),
        "recall@5": recall_at_k(ranks, 5),
        "mrr": mean_reciprocal_rank(ranks),
        "ndcg@5": ndcg_at_k(ranks, 5),
    }

    print("\nResults:")

    for name, value in metrics.items():
        print(f"{name}: {value:.6f}")

    # Save results
    result = {
        "model": args.model,
        "dataset": args.dataset,
        "test_size": len(test_dataset),
        "metrics": metrics,
    }

    output_dir = os.path.dirname(args.output)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\nResults saved to: {args.output}")


if __name__ == "__main__":
    main()
