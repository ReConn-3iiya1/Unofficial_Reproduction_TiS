# scripts/run_model.py

import argparse
import json
import traceback
from pathlib import Path

from vsi_reproduce.experiment import ExperimentTracker


def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def model_generate(sample):
    # TODO: 替换成你的真实模型推理代码
    return "A"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--split_file", required=True)
    parser.add_argument("--split_name", default="tiny")
    parser.add_argument("--dataset_version", default="official")
    parser.add_argument("--model_name", required=True)
    parser.add_argument("--model_version", required=True)
    parser.add_argument("--prompt_type", default="default")
    parser.add_argument("--num_frames", type=int, default=32)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max_new_tokens", type=int, default=128)
    parser.add_argument("--batch_size", type=int, default=1)
    args = parser.parse_args()

    config = {
        "batch_size": args.batch_size,
        "frame_sampling_method": "uniform",
        "num_frames": args.num_frames,
        "prompt_type": args.prompt_type,
        "temperature": args.temperature,
        "max_new_tokens": args.max_new_tokens,
        "decoding_method": "greedy" if args.temperature == 0 else "sampling",
    }

    tracker = ExperimentTracker(
        model_name=args.model_name,
        model_version=args.model_version,
        dataset_name="VSI-Bench",
        dataset_version=args.dataset_version,
        split_name=args.split_name,
        split_file=args.split_file,
        prompt_type=args.prompt_type,
        config=config,
        command=" ".join(["python", "scripts/run_model.py"]),
    )

    samples = load_jsonl(args.split_file)
    predictions = []

    for idx, sample in enumerate(samples):
        try:
            tracker.logger.log(f"Running sample {idx + 1}/{len(samples)}: {sample.get('sample_id')}")
            raw_prediction = model_generate(sample)

            predictions.append({
                "sample_id": sample.get("sample_id"),
                "task": sample.get("task"),
                "question": sample.get("question"),
                "gt_answer": sample.get("answer"),
                "raw_prediction": raw_prediction,
                "model": args.model_name,
                "prompt_type": args.prompt_type,
                "num_frames": args.num_frames,
            })

        except Exception as e:
            error_text = traceback.format_exc()
            tracker.add_error(error_text)

            predictions.append({
                "sample_id": sample.get("sample_id"),
                "task": sample.get("task"),
                "question": sample.get("question"),
                "gt_answer": sample.get("answer"),
                "raw_prediction": None,
                "error": str(e),
                "model": args.model_name,
            })

    pred_path = Path(tracker.metadata["outputs"]["prediction_file"])
    write_jsonl(pred_path, predictions)

    tracker.finish(metrics=None)
    print(f"Experiment directory: {tracker.exp_dir}")


if __name__ == "__main__":
    main()