import argparse
import json
import os
import random

import numpy as np
import torch
from datasets import load_dataset
from sentence_transformers import InputExample, SentenceTransformer, losses
from torch.utils.data import DataLoader


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


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
        "--fraction",
        type=float,
        default=1.0,
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=4,
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=2,
    )
    parser.add_argument(
        "--learning-rate",
        type=float,
        default=1e-5,
    )
    parser.add_argument(
        "--max-seq-length",
        type=int,
        default=512,
    )
    parser.add_argument(
        "--warmup-ratio",
        type=float,
        default=0.10,
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
    )

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    set_seed(args.seed)

    print("Loading dataset...")
    dataset = load_dataset(args.dataset)

    train_dataset = dataset["train"]

    if args.fraction < 1.0:
        train_size = int(len(train_dataset) * args.fraction)

        train_dataset = (
            train_dataset
            .shuffle(seed=args.seed)
            .select(range(train_size))
        )

    print(f"Training examples: {len(train_dataset)}")

    print("Loading model...")
    model = SentenceTransformer(
        args.model,
        device="cuda" if torch.cuda.is_available() else "cpu",
    )

    model.max_seq_length = args.max_seq_length

    train_examples = [
        InputExample(
            texts=[
                row["docstring"],
                row["function"],
            ]
        )
        for row in train_dataset
    ]

    train_dataloader = DataLoader(
        train_examples,
        shuffle=True,
        batch_size=args.batch_size,
        collate_fn=model.smart_batching_collate,
    )

    train_loss = losses.MultipleNegativesRankingLoss(model)

    steps_per_epoch = len(train_dataloader)
    total_steps = steps_per_epoch * args.epochs
    warmup_steps = int(total_steps * args.warmup_ratio)

    config = {
        "model": args.model,
        "dataset": args.dataset,
        "train_fraction": args.fraction,
        "train_size": len(train_dataset),
        "batch_size": args.batch_size,
        "epochs": args.epochs,
        "learning_rate": args.learning_rate,
        "max_seq_length": args.max_seq_length,
        "loss": "MultipleNegativesRankingLoss",
        "warmup_ratio": args.warmup_ratio,
        "warmup_steps": warmup_steps,
        "use_amp": False,
        "seed": args.seed,
        "total_steps": total_steps,
    }

    config_path = os.path.join(
        args.output,
        "experiment_config.json",
    )

    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    print("Training configuration:")
    print(json.dumps(config, indent=2))

    model.fit(
        train_objectives=[
            (train_dataloader, train_loss)
        ],
        epochs=args.epochs,
        warmup_steps=warmup_steps,
        optimizer_params={
            "lr": args.learning_rate,
        },
        output_path=args.output,
        show_progress_bar=True,
        use_amp=False,
    )

    print(f"Model saved to: {args.output}")


if __name__ == "__main__":
    main()
