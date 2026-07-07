from datasets import load_dataset
from collections import Counter

vsi_bench = load_dataset(
    "nyu-visionx/VSI-Bench",
    cache_dir="data/raw/hf_cache"
)

test = vsi_bench["test"]

print(vsi_bench)
print(Counter(test["question_type"]))

for row in test:
    if row["options"] is not None:
        print(row)
        break