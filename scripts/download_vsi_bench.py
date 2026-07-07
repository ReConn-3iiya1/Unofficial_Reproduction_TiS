from datasets import load_dataset

vsi_bench = load_dataset(
    "nyu-visionx/VSI-Bench",
    cache_dir="data/raw/hf_cache"
)

print(vsi_bench)
print(vsi_bench.keys())
print(vsi_bench[list(vsi_bench.keys())[0]][0])