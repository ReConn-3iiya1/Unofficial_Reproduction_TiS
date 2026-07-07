# Unofficial Reproduction: Thinking in Space
本仓库包含对论文《Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces》中 VSI-Bench 评测流程的部分复现。


This repository contains a partial reproduction of the VSI-Bench evaluation pipeline from the paper "Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces".

## 论文标题
Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces

## 论文任务

本仓库复现论文 **Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces** 中的部分实验。

该论文研究多模态大语言模型是否能够从第一视角室内视频中理解、记忆并回忆空间布局。作者提出了 **VSI-Bench**，一个基于视频的视觉空间智能 benchmark，包含来自 288 个真实室内场景视频的 5000 多个问答样本。该 benchmark 用于评估模型是否能够识别空间中的物体、记住物体之间的空间关系，并回答与场景布局相关的问题。

VSI-Bench 包含 8 类任务：

1. **Object Count**：统计房间中特定物体的数量。
2. **Absolute Distance**：估计两个物体之间的实际距离。
3. **Object Size**：估计物体的实际尺寸。
4. **Room Size**：估计房间或多个空间的面积。
5. **Relative Distance**：判断某个物体相对于目标物体最近或最远。
6. **Relative Direction**：从指定观察位置和朝向判断物体方向。
7. **Route Plan**：补全空间导航路径中的转向指令。
8. **Appearance Order**：判断多个物体在视频中首次出现的顺序。

原论文在 zero-shot 设置下评测了多个闭源和开源视频 MLLM。主要结论是：当前 MLLM 在视觉空间任务上仍明显低于人类水平；主要瓶颈来自空间推理，尤其是关系推理以及从自我中心视角到环境中心视角的转换。此外，论文发现 Chain-of-Thought 等常规语言推理提示并不能稳定提升空间推理能力，而显式生成 cognitive map 可以提升相对距离推理表现。

This repository reproduces selected experiments from **Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces**.

The paper studies whether multimodal large language models can understand and recall spatial layouts from egocentric indoor videos. It introduces **VSI-Bench**, a video-based visual-spatial intelligence benchmark containing more than 5,000 question-answer pairs from 288 real indoor-scene videos. The benchmark evaluates whether models can perceive objects, remember their spatial relationships, and answer questions about the scene layout.

VSI-Bench includes eight task types:

1. **Object Count**: count how many instances of a target object appear in the room.
2. **Absolute Distance**: estimate the metric distance between two objects.
3. **Object Size**: estimate the physical size of an object.
4. **Room Size**: estimate the area of the room or combined space.
5. **Relative Distance**: choose which object is closest to or farthest from another object.
6. **Relative Direction**: infer an object's direction from a specified viewpoint.
7. **Route Plan**: complete navigation instructions in the observed space.
8. **Appearance Order**: determine the first-time appearance order of objects in the video.

The original paper evaluates both proprietary and open-source video-capable MLLMs under zero-shot settings. It reports that current MLLMs remain substantially below human performance on visual-spatial tasks, and that spatial reasoning—especially relational reasoning and egocentric-to-allocentric transformation—is the main bottleneck. The paper also finds that standard linguistic prompting methods such as Chain-of-Thought do not reliably improve spatial reasoning, while explicitly generating cognitive maps can improve relative-distance reasoning.

## 复现范围
### 第一层复现
目标是复现基础评测工作流，而不是完整复现论文中的全部实验。

具体来说，本复现包括：

- 加载 VSI-Bench 的小规模样本子集；
- 使用一个支持视频输入的多模态大语言模型进行推理；
- 保存模型的原始预测结果；
- 将模型输出解析为可比较的答案格式；
- 对选择题任务和数值答案任务计算与原论文风格一致的评测指标。

本复现不包括重新构建 VSI-Bench、不包括复现论文中评测的全部模型、不包括复现主表中的全量结果，也不包括 cognitive map 实验和 prompting analysis 实验。

The goal is to reproduce the basic evaluation workflow rather than the full set of experiments reported in the paper.

Specifically, this reproduction aims to:

- load a small subset of VSI-Bench samples;
- run inference with one video-capable multimodal large language model;
- save the model’s raw predictions;
- parse model outputs into comparable answers;
- compute the official-style evaluation metrics for multiple-choice and numerical-answer tasks.

This reproduction does not attempt to rebuild VSI-Bench, reproduce all evaluated models, reproduce full-scale results in the main paper, or reproduce the cognitive-map and prompting-analysis experiments.

## 环境安装


## 数据准备


## 运行命令


## 评测命令


## 目前结果


## 已知差异



