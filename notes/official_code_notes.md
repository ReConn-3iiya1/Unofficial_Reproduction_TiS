# Official Code Notes

## Repository

- official repo: https://github.com/vision-x-nyu/thinking-in-space
- local path: external/thinking-in-space
- read date: 2026-07-07
- official commit hash: 240e51aa7b0c151fd0d7d45150278723ab1be574
- branch: main

## Data Format

The VSI-Bench dataset is loaded from Hugging Face:

- dataset name: `nyu-visionx/VSI-Bench`
- split: `test`
- number of samples: `5130`
- cache directory: `data/raw/hf_cache`

Each sample contains the following fields:

- `id`: integer sample id
- `dataset`: source dataset name, e.g. `arkitscenes`
- `scene_name`: scene identifier
- `question_type`: task type
- `question`: natural-language question
- `ground_truth`: reference answer
- `options`: multiple-choice options; `null` for numerical-answer tasks
- `pruned`: whether the sample is marked as pruned

Task distribution in the `test` split:

| Question Type | Count |
|---|---:|
| `object_size_estimation` | 953 |
| `object_abs_distance` | 834 |
| `object_rel_distance` | 710 |
| `obj_appearance_order` | 618 |
| `object_counting` | 565 |
| `object_rel_direction_medium` | 378 |
| `object_rel_direction_hard` | 373 |
| `room_size_estimation` | 288 |
| `object_rel_direction_easy` | 217 |
| `route_planning` | 194 |

Example numerical-answer sample:
```json
{
  "id": 0,
  "dataset": "arkitscenes",
  "scene_name": "41069025",
  "question_type": "object_counting",
  "question": "How many table(s) are in this room?",
  "ground_truth": "4",
  "options": null,
  "pruned": false
}
```

## Environment

- Python: 3.10
- PyTorch: 2.5.1+cu121
- CUDA available: True
- transformers: 4.45.0.dev0
- datasets: 2.16.1

## Video Processing

- frame sampling method:
- number of frames:
- video truncation:
- library used:

## Prompt

- default prompt:
- multiple-choice prompt:
- numerical-answer prompt:
- CoT prompt:

## Evaluation

- MCA metric:
- NA metric:
- fuzzy matching:
- answer parser:
- missing prediction handling:

## Commands

- official inference command:
- official evaluation command:

## Differences to My Implementation

- 