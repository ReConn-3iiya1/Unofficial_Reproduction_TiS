# src/tis_reproduce/experiment.py

import json
import os
import platform
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def run_command(command: list[str]) -> str:
    try:
        return subprocess.check_output(command, stderr=subprocess.STDOUT).decode().strip()
    except Exception:
        return "unknown"


def get_git_info() -> Dict[str, str]:
    return {
        "commit_hash": run_command(["git", "rev-parse", "HEAD"]),
        "git_status": run_command(["git", "status", "--short"]),
    }


def get_gpu_info() -> str:
    return run_command([
        "nvidia-smi",
        "--query-gpu=name,memory.total,driver_version",
        "--format=csv,noheader",
    ])


def get_env_info() -> Dict[str, str]:
    return {
        "python": sys.version.replace("\n", " "),
        "platform": platform.platform(),
        "gpu": get_gpu_info(),
    }


def make_experiment_dir(
    model_name: str,
    split_name: str,
    prompt_type: str,
    output_root: str = "outputs/experiments",
) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_model = model_name.replace("/", "_").replace(" ", "_")
    exp_id = f"{timestamp}_{safe_model}_{split_name}_{prompt_type}"
    exp_dir = Path(output_root) / exp_id
    exp_dir.mkdir(parents=True, exist_ok=False)
    return exp_dir


def save_json(path: Path, data: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


class ExperimentLogger:
    def __init__(self, exp_dir: Path):
        self.exp_dir = exp_dir
        self.log_path = exp_dir / "run.log"

    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {message}"
        print(line)
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


class ExperimentTracker:
    def __init__(
        self,
        model_name: str,
        model_version: str,
        dataset_name: str,
        dataset_version: str,
        split_name: str,
        split_file: str,
        prompt_type: str,
        config: Dict[str, Any],
        command: str,
    ):
        self.exp_dir = make_experiment_dir(model_name, split_name, prompt_type)
        self.logger = ExperimentLogger(self.exp_dir)
        self.start_time = time.time()

        self.metadata = {
            "experiment_id": self.exp_dir.name,
            "start_time": datetime.now().isoformat(timespec="seconds"),
            "git": get_git_info(),
            "environment": get_env_info(),
            "data": {
                "dataset_name": dataset_name,
                "dataset_version": dataset_version,
                "split_name": split_name,
                "split_file": split_file,
            },
            "model": {
                "model_name": model_name,
                "model_version": model_version,
            },
            "inference": config,
            "command": command,
            "outputs": {
                "prediction_file": str(self.exp_dir / "predictions.jsonl"),
                "metric_file": str(self.exp_dir / "metrics.json"),
                "log_file": str(self.exp_dir / "run.log"),
            },
            "errors": [],
            "status": "running",
        }

        save_json(self.exp_dir / "metadata.json", self.metadata)
        self.logger.log(f"Experiment created: {self.exp_dir}")

    def add_error(self, error: str) -> None:
        self.metadata["errors"].append(error)
        save_json(self.exp_dir / "metadata.json", self.metadata)
        self.logger.log(f"ERROR: {error}")

    def finish(self, metrics: Dict[str, Any] | None = None) -> None:
        end_time = time.time()
        self.metadata["end_time"] = datetime.now().isoformat(timespec="seconds")
        self.metadata["runtime_seconds"] = round(end_time - self.start_time, 3)
        self.metadata["status"] = "finished"
        if metrics is not None:
            self.metadata["metrics"] = metrics
        save_json(self.exp_dir / "metadata.json", self.metadata)
        self.logger.log("Experiment finished.")