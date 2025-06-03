<div align="center">

<h1>❤️ LOVE: Benchmarking and Evaluating Text-to-Video Generation and Video-to-Text Interpretation</h1>

</div>

<div align="center">

<h3>💡 How to evaluate Text-to-Video Generation Models properly?</h3>

<a href="https://huggingface.co/datasets/anonymousdb/AIGVE-60K">
   <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-green" alt="Hugging Face Dataset Badge"/>
</a>

</div>

<p align="center">
  <img width="1000" alt="LOVE" src="https://github.com/user-attachments/assets/20901a3b-68e8-4b65-89b1-acbe38ae7165" />
</p>

<h3>If you find our database and code useful, please give a star :star: and citation :pencil:</h3>
---


## 🤗 AIGVE-60K Download

[![🤗 Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-green)](https://huggingface.co/datasets/anonymousdb/AIGVE-60K)

Download with CLI:

```bash
huggingface-cli download anonymousdb/AIGVE-60K --repo-type dataset --local-dir ./AIGVE-60K
```
</div>

<p align="center">
  <img width="1000" alt="LOVEe" src="https://github.com/user-attachments/assets/00a8e408-4480-4f93-9a24-d12db6b2d3da" />
</p>


## 🏆 T2V Generation Model Leaderboard 

This leaderboard presents the performance of 30 models on the **AIGVE-60K** benchmark, evaluating across three key dimensions:  
- 🎨 **Perceptual Quality** 
- 🔄 **Text-to-Video Correspondence**  
- ❓ **Task-specific Accuracy**

Final **Overall Rank** is computed by summing the individual ranks across these three dimensions.
The **top 3 models** are marked with 🥇🥈🥉. All model names are bolded for clarity.
| 🏆 Overall Rank | Model | 🎨 Perception MOS | 🔗 Rank | 🔄 Correspondence MOS | 🔗 Rank | ❓ Task-specific Accuracy (%) | 🔗 Rank |
|----------------|-------|--------------------|--------|------------------------|--------|--------------------|--------|
|              1 | 🥇 [Pixverse](https://pixverse.ai/)                                             |        63.81 |                 2 |            59.97 |                     2 |          91.33 |                   1 |
|              2 | 🥈 [Wanxiang](https://tongyi.aliyun.com/wanxiang/)                              |        60.54 |                 7 |            60.37 |                     1 |          90.33 |                   2 |
|              3 | 🥉 [Hailuo](https://hailuoai.video/)                                            |        60.58 |                 5 |            59.74 |                     3 |          87.67 |                   3 |
|              4 | [Jimeng](https://jimeng.jianying.com/)                                          |        65.25 |                 1 |            57.86 |                     6 |          81.33 |                   6 |
|              5 | [Sora](https://openai.com/research/video-generation-models-as-world-simulators) |        62.09 |                 4 |            59.68 |                     4 |          85.67 |                   5 |
|              6 | [Hunyuan](https://aivideo.hunyuan.tencent.com/)                                 |        58.81 |                 9 |            57.25 |                     7 |          79.67 |                   7 |
|              7 | [Vidu1.5](https://www.vidu.studio/zh)                                           |        54.56 |                15 |            58.25 |                     5 |          87    |                   4 |
|              8 | [Gen3](https://runwayml.com/research/introducing-gen-3-alpha)                   |        59.22 |                 8 |            55.72 |                     8 |          75.33 |                   9 |
|              9 | [Kling](https://klingai.io/)                                                    |        60.56 |                 6 |            55.57 |                     9 |          73.67 |                  11 |
|             10 | [Genmo](https://www.genmo.ai)                                                   |        57.66 |                11 |            53.78 |                    11 |          75.67 |                   8 |
|             11 | [ChatGLM](https://chatglm.cn/video?lang=zh)                                     |        56.39 |                13 |            53.98 |                    10 |          74    |                  10 |
|             12 | [Xunfei](https://typemovie.art/)                                                |        58.6  |                10 |            53.46 |                    12 |          66.33 |                  12 |
|             13 | [Pyramid](https://github.com/jy0205/Pyramid-Flow)                               |        63.67 |                 3 |            50.17 |                    16 |          50.17 |                  22 |
|             14 | [Wan2.1](https://github.com/FoundationVision/LlamaGen)                          |        57.27 |                12 |            52.33 |                    13 |          62.67 |                  16 |
|             15 | [Allegro](https://github.com/rhymes-ai/Allegro)                                 |        56.08 |                14 |            50.7  |                    15 |          63    |                  15 |
|             16 | [VideoCrafter2](https://github.com/AILab-CVC/VideoCrafter)                      |        48.11 |                19 |            51.07 |                    14 |          65.67 |                  13 |
|             17 | [CogVideo X1.5](https://github.com/THUDM/CogVideo)                              |        50.59 |                16 |            49.73 |                    17 |          64.67 |                  14 |
|             18 | [Animate](https://github.com/aigc-apps/EasyAnimate)                             |        50.48 |                17 |            49.3  |                    18 |          60.67 |                  17 |
|             19 | [Lavie](https://github.com/Vchitect/LaVie)                                      |        49.3  |                18 |            48.22 |                    19 |          55    |                  20 |
|             20 | [Hotshot-XL](https://github.com/hotshotco/Hotshot-XL)                           |        42.66 |                22 |            47.75 |                    20 |          57.67 |                  18 |
|             21 | [Latte](https://github.com/Vchitect/Latte)                                      |        43.81 |                21 |            46.73 |                    22 |          54.33 |                  21 |
|             22 | [VideoCrafter1](https://github.com/AILab-CVC/VideoCrafter)                      |        44.12 |                20 |            44.67 |                    24 |          46    |                  25 |
|             23 | [Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero)       |        40.53 |                24 |            44.89 |                    23 |          48.67 |                  23 |
|             24 | [NOVA](https://github.com/baaivision/NOVA)                                      |        41.18 |                23 |            47.18 |                    21 |          56    |                  19 |
|             25 | [ModelScope](https://github.com/modelscope/modelscope)                          |        38    |                26 |            43.73 |                    25 |          47.33 |                  24 |
|             26 | [Tune-A-Video](https://github.com/showlab/Tune-A-Video)                         |        35.41 |                27 |            42.69 |                    26 |          43    |                  26 |
|             27 | [LTX](https://github.com/Lightricks/LTX-Video)                                  |        40.11 |                25 |            41.28 |                    28 |          37    |                  28 |
|             28 | [LVDM](https://github.com/YingqingHe/LVDM)                                      |        33.84 |                28 |            42.2  |                    27 |          40.33 |                  27 |
|             29 | [ZeroScope](https://huggingface.co/cerspense/zeroscope_v2_XL)                   |        30.08 |                29 |            34.69 |                    29 |          22    |                  29 |
|             30 | [LWM](https://github.com/LargeWorldModel/LWM)                                   |        27.39 |                30 |            31.49 |                    30 |           9    |                  30 |


</div>

# ❤️ LOVE Metric -- <u>L</u>MM f<u>o</u>r <u>V</u>ideo <u>E</u>valuation
<p align="center">
  <img width="1000" alt="model" src="https://github.com/user-attachments/assets/67b09453-2a50-4869-9843-4b1d089c8cf9" />
</p>


## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/IntMeGroup/LOVE.git
```

Create and activate a conda environment:

```bash
conda create -n LOVE python=3.9 -y
conda activate LOVE
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install `flash-attn==2.3.6` (pre-built):

```bash
pip install flash-attn==2.3.6 --no-build-isolation
```

Or compile from source:

```bash
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention
git checkout v2.3.6
python setup.py install
```

---

## 🔧 Preparation

### 📁 Prepare dataset

```bash
huggingface-cli download anonymousdb/AIGVE-60K data.zip --repo-type dataset --local-dir ./
unzip data.zip -d ./data
```
### 📦 Prepare model weights

```bash
huggingface-cli download OpenGVLab/InternVL3-9B --local_dir OpenGVLab/InternVL3-9B
huggingface-cli download anonymousdb/LOVE-pretrain temporal.pth ./
```

---



## 🚀 Training


### 📈 Stage 1: Text-based quality training

```bash
sh shell/st1_train.sh
```

### 🎨 Stage 2: Fine-tune vision encoder and LLM with LoRA

```bash
sh shell/st2_train.sh
```

### ❓ Question-Answering (QA) Training

```bash
sh shell/train_qa.sh
```

---

## 🚀 Evaluation

### 📦 Download pretrained weights

```bash
huggingface-cli download anonymousdb/LOVE-Perception --local-dir ./weights/stage2/stage2_mos1
huggingface-cli download anonymousdb/LOVE-Correspondence --local-dir ./weights/stage2/stage2_mos2
huggingface-cli download anonymousdb/LOVE-QA --local-dir ./weights/qa
```

### 📈 Evaluate perception & correspondence scores

[![HF](https://img.shields.io/badge/%F0%9F%A4%97%20LOVE--Perception-orange)](https://huggingface.co/anonymousdb/LOVE-Perception)  
[![HF](https://img.shields.io/badge/%F0%9F%A4%97%20LOVE--Correspondence-green)](https://huggingface.co/anonymousdb/LOVE-Correspondence)

```bash
sh shell/eval_score.sh
```

### ❓ Evaluate question-answering

[![HF](https://img.shields.io/badge/%F0%9F%A4%97%20LOVE--QA-blue)](https://huggingface.co/anonymousdb/LOVE-QA)

```bash
sh shell/eval_qa.sh
```
# 🏆 V2T Interpretation Model Leaderboard 

This leaderboard presents the performance of 48 models on the **AIGVE-60K** benchmark, evaluating across three key dimensions:  
- 🎨 **Perception SRCC**: Spearman correlation of perceptual quality.
- 🔄 **Correspondence SRCC**: Spearman correlation of text-to-video alignment.
- ❓ **QA Accuracy**: Accuracy of question answering.
  
Final **Overall Rank** is computed by summing the individual ranks across these three dimensions.
The **top 3 models** are marked with 🥇🥈🥉. All model names are bolded for clarity.

## 🏆 V2T Instance-Level Performance Leaderboard

| 🏆 Rank | Method | Perception SRCC | 🔗 Rank | Correspondence SRCC | 🔗 Rank | QA Acc (%) | 🔗 Rank |
|--------|--------|------------------|--------|----------------------|--------|-------------|--------|
| 🥇 | **LOVE (Ours)** | 0.7932 | 1 | 0.7466 | 1 | 78.69 | 1 |
| 🥈 | **InternVL2.5 (38B)** | 0.6227 | 6 | 0.6470 | 5 | 75.81 | 3 |
| 🥉 | **Grok2 Vision** | 0.5628 | 11 | 0.6659 | 2 | 76.51 | 2 |
| 4 | **InternVL2.5 (72B)** | 0.5383 | 16 | 0.6612 | 4 | 75.18 | 4 |
| 5 |**InternVL3 (72B)** | 0.5441 | 13 | 0.6314 | 6 | 74.59 | 6 |
| 6 | **ChatGPT-4o** | 0.5263 | 18 | 0.6639 | 3 | 74.84 | 5 |
| 7 | **Gemini1.5-pro** | 0.4972 | 21 | 0.6095 | 8 | 73.38 | 9 |
| 7 | **InternVL3 (38B)** | 0.4950 | 22 | 0.5996 | 9 | 73.89 | 7 |
| 9 | **Llava-one-vision (72B)** | 0.5291 | 17 | 0.5702 | 12 | 73.31 | 10 |
| 10 | **Qwen2.5-VL (72B)** | 0.4245 | 26 | 0.6272 | 7 | 73.83 | 8 |
| 11 | **Claude3.5** | 0.4267 | 25 | 0.5827 | 11 | 73.20 | 11 |
| 12 | **Qwen2-VL (72B)** | 0.4628 | 24 | 0.5598 | 13 | 73.12 | 12 |
| 12 | **FGA-BLIP2** | 0.5181 | 19 | 0.5962 | 10 | 67.06 | 20 |
| 14 | **HPSv2** | 0.5415 | 14 | 0.4989 | 17 | 67.68 | 19 |
| 15 | **FAST-VQA** | 0.6391 | 5 | 0.3919 | 29 | 66.27 | 22 |
| 15 | **HOSA** | 0.6474 | 3 | 0.4153 | 24 | 64.34 | 29 |
| 17 | **ImageReward** | 0.4180 | 27 | 0.5076 | 16 | 68.33 | 18 |
| 18 | **QAC** | 0.5958 | 7 | 0.3948 | 27 | 64.40 | 28 |
| 19 | **NIQE** | 0.6536 | 2 | 0.4345 | 22 | 62.21 | 39 |
| 20 | **BRISQUE** | 0.5843 | 8 | 0.3806 | 30 | 64.67 | 26 |
| 21 | **AestheticScore** | 0.5524 | 12 | 0.3931 | 28 | 64.87 | 25 |
| 22 | **Qwen2-VL (7B)** | 0.3568 | 32 | 0.4498 | 21 | 71.56 | 13 |
| 23 | **Qwen2.5-VL (7B)** | 0.5410 | 15 | 0.5110 | 15 | 62.34 | 37 |
| 24 | **VideoLlama3 (8B)** | 0.3922 | 30 | 0.4228 | 23 | 70.16 | 16 |
| 25 | **DOVER** | 0.6414 | 4 | 0.3759 | 31 | 62.61 | 35 |
| 26 | **BMPRI** | 0.5741 | 9 | 0.3618 | 32 | 64.00 | 30 |
| 27 | **V-Aesthetic Quality** | 0.5031 | 20 | 0.4033 | 26 | 64.54 | 27 |
| 28 | **LLaVA-NeXT (8B)** | 0.4888 | 23 | 0.2847 | 36 | 70.21 | 15 |
| 29 | **InternVideo2.5 (8B)** | 0.1563 | 43 | 0.4978 | 18 | 70.64 | 14 |
| 30 | **InternVL2.5 (8B)** | 0.2799 | 38 | 0.4856 | 19 | 66.30 | 21 |
| 31 | **mPLUG-Owl3 (7B)** | 0.3532 | 34 | 0.5478 | 14 | 63.02 | 34 |
| 31 | **InternVL3 (9B)** | 0.2731 | 39 | 0.4768 | 20 | 65.82 | 23 |
| 33 | **SimpleVQA**| 0.5631 | 10 | 0.3474 | 33 | 60.78 | 42 |
| 34 | **PickScore** | 0.4026 | 29 | 0.4135 | 25 | 62.29 | 38 |
| 35 | **VideoLlava (7B)** | 0.1809 | 41 | 0.2005 | 41 | 68.46 | 17 |
| 36 | **V-Temporal Flickering** | 0.4076 | 28 | 0.1958 | 42 | 63.69 | 32 |
| 37 | **BLIPScore** | 0.1884 | 40 | 0.3163 | 34 | 63.93 | 31 |
| 38 | **BPRI** | 0.3558 | 33 | 0.2018 | 40 | 63.56 | 33 |
| 39 | **VSFA** | 0.3750 | 31 | 0.2438 | 37 | 57.09 | 46 |
| 40 | **CogAgent (18B)** | 0.1244 | 45 | 0.1190 | 46 | 65.32 | 24 |
| 41 | **V-Subject Consistency** | 0.3443 | 35 | 0.1647 | 45 | 62.52 | 36 |
| 42 | **BVQA** | 0.3089 | 36 | 0.2379 | 38 | 58.47 | 44 |
| 43 | **V-Overall Consistency** | 0.1559 | 44 | 0.3076 | 35 | 61.96 | 41 |
| 44 | **V-Imaging Quality** | 0.2810 | 37 | 0.1952 | 43 | 60.60 | 43 |
| 45 | **CLIPScore** | 0.0947 | 46 | 0.2290 | 39 | 58.27 | 45 |
| 46 | **VQAScore** | 0.1677 | 42 | 0.1763 | 44 | 52.97 | 47 |
| 47 | **Llama3.2-Vision (11B)** | 0.0940 | 47 | 0.0804 | 47 | 62.19 | 40 |
| 48 | **DeepseekVL2 (1B)** | 0.0121 | 48 | 0.0173 | 48 | 39.29 | 48 |

---
## 🏆 V2T Model-Level Performance Leaderboard

| 🏆 Rank | Method | Perception SRCC | 🔗 Rank | Correspondence SRCC | 🔗 Rank | QA Acc (%) | 🔗 Rank |
|--------|--------|------------------|--------|----------------------|--------|-------------|--------|
| 🥇 | **LOVE (Ours)** | 0.9324 | 1 | 0.9778 | 1 | 0.98 | 1 |
| 🥈 | **InternVL2.5 (38B)** | 0.9052 | 3 | 0.9586 | 2 | 0.95 | 6 |
| 🥉 | **InternVL3 (72B)** | 0.8923 | 7 | 0.9444 | 8 | 0.96 | 2 |
| 4 | **Grok2 Vision** | 0.8808 | 10 | 0.9546 | 4 | 0.95 | 5 |
| 5 | **InternVL2.5 (72B)** | 0.8843 | 9 | 0.9542 | 5 | 0.94 | 7 |
| 6 | **FGA-BLIP2** | 0.8954 | 5 | 0.9502 | 6 | 0.94 | 10 |
| 7 | **ChatGPT-4o** | 0.9048 | 4 | 0.9458 | 7 | 0.93 | 11 |
| 8 | **Gemini1.5-pro** | 0.8790 | 11 | 0.9430 | 10 | 0.95 | 4 |
| 9 | **VideoLlama3 (8B)** | 0.9073 | 2 | 0.9075 | 16 | 0.82 | 19 |
| 10 | **InternVL3 (38B)** | 0.8118 | 20 | 0.9439 | 9 | 0.94 | 9 |
| 11 | **Qwen2.5-VL (72B)** | 0.7762 | 28 | 0.9364 | 13 | 0.95 | 3 |
| 12 | **Qwen2-VL (72B)** | 0.8388 | 16 | 0.9271 | 15 | 0.91 | 14 |
| 13 | **FAST-VQA** | 0.8945 | 6 | 0.8376 | 20 | 0.81 | 20 |
| 14 | **LLaVA-NeXT (8B)** | 0.8785 | 12 | 0.8042 | 23 | 0.92 | 12 |
| 15 | **mPLUG-Owl3 (7B)** | 0.7962 | 24 | 0.9310 | 14 | 0.89 | 15 |
| 16 | **InternVL3 (9B)** | 0.8300 | 17 | 0.9373 | 12 | 0.77 | 25 |
| 17 | **Claude3.5** | 0.7602 | 30 | 0.8919 | 17 | 0.94 | 8 |
| 18 | **InternVL2.5 (8B)** | 0.7882 | 25 | 0.9390 | 11 | 0.81 | 21 |
| 19 | **Llava-one-vision (72B)** | 0.7829 | 27 | 0.8741 | 18 | 0.91 | 13 |
| 20 | **DOVER** | 0.8874 | 8 | 0.8038 | 24 | 0.77 | 26 |
| 21 | **ImageReward** | 0.8016 | 23 | 0.8549 | 19 | 0.86 | 17 |
| 22 | **InternVideo2.5 (8B)** | 0.3361 | 44 | 0.9560 | 3 | 0.84 | 18 |
| 23 | **NIQE** | 0.8412 | 15 | 0.7838 | 26 | 0.76 | 27 |
| 24 | **PickScore** | 0.8198 | 18 | 0.7775 | 28 | 0.78 | 22 |
| 25 | **HOSA** | 0.8456 | 14 | 0.7780 | 27 | 0.76 | 28 |
| 26 | **Qwen2.5-VL (7B)** | 0.8652 | 13 | 0.8167 | 22 | 0.67 | 36 |
| 27 | **Qwen2-VL (7B)** | 0.7085 | 33 | 0.7953 | 25 | 0.87 | 16 |
| 28 | **QAC** | 0.8100 | 21 | 0.7717 | 29 | 0.75 | 30 |
| 29 | **BRISQUE** | 0.8131 | 19 | 0.7615 | 30 | 0.74 | 31 |
| 30 | **HPSv2** | 0.7504 | 32 | 0.7522 | 31 | 0.78 | 23 |
| 31 | **CogAgent (18B)** | 0.4834 | 41 | 0.8198 | 21 | 0.78 | 24 |
| 32 | **SimpleVQA** | 0.8038 | 22 | 0.7273 | 33 | 0.69 | 34 |
| 33 | **BMPRI** | 0.7878 | 26 | 0.7321 | 32 | 0.70 | 33 |
| 34 | **V-Aesthetic Quality** | 0.7740 | 29 | 0.7273 | 33 | 0.70 | 32 |
| 35 | **AestheticScore** | 0.7566 | 31 | 0.7001 | 35 | 0.67 | 35 |
| 36 | **VideoLlava (7B)** | 0.6125 | 37 | 0.6406 | 36 | 0.75 | 29 |
| 37 | **V-Temporal Flickering** | 0.6396 | 34 | 0.5778 | 38 | 0.58 | 38 |
| 38 | **VSFA** | 0.6227 | 36 | 0.5858 | 37 | 0.52 | 39 |
| 39 | **BPRI** | 0.6356 | 35 | 0.5324 | 39 | 0.47 | 41 |
| 40 | **BVQA** | 0.5030 | 39 | 0.4674 | 41 | 0.48 | 40 |
| 41 | **V-Imaging Quality** | 0.5426 | 38 | 0.4986 | 40 | 0.44 | 43 |
| 42 | **V-Subject Consistency** | 0.4839 | 40 | 0.4416 | 42 | 0.45 | 42 |
| 43 | **Llama3.2-Vision (11B)** | 0.4483 | 42 | 0.2783 | 46 | 0.60 | 37 |
| 44 | **VQAScore** | 0.3437 | 43 | 0.3922 | 43 | 0.33 | 46 |
| 45 | **BLIPScore** | 0.2111 | 45 | 0.3451 | 44 | 0.38 | 44 |
| 46 | **V-Overall Consistency** | 0.1742 | 46 | 0.3201 | 45 | 0.34 | 45 |
| 47 | **CLIPScore** | 0.0300 | 48 | 0.1408 | 47 | 0.17 | 47 |
| 48 | **DeepseekVL2 (1B)** | 0.0607 | 47 | 0.0785 | 48 | 0.10 | 48 |


---
# 🎥 Text-to-Video (T2V) Generation Models

This section lists 30 representative T2V generation models, including both **commercial close-source models** and **open-source lab models**, with links to their official or GitHub pages.

---

## ♠️ Close-Source Commercial T2V Models

| Model | URL |
|-------|-----|
| **Pixverse** | [https://pixverse.ai/](https://pixverse.ai/) |
| **Wanxiang** | [https://tongyi.aliyun.com/wanxiang/](https://tongyi.aliyun.com/wanxiang/) |
| **Hailuo** | [https://hailuoai.video/](https://hailuoai.video/) |
| **Jimeng** | [https://jimeng.jianying.com/](https://jimeng.jianying.com/) |
| **Sora** | [https://openai.com/research/video-generation-models-as-world-simulators](https://openai.com/research/video-generation-models-as-world-simulators) |
| **Hunyuan** | [https://aivideo.hunyuan.tencent.com/](https://aivideo.hunyuan.tencent.com/) |
| **Vidu1.5** | [https://www.vidu.studio/zh](https://www.vidu.studio/zh) |
| **Gen3** | [https://runwayml.com/research/introducing-gen-3-alpha](https://runwayml.com/research/introducing-gen-3-alpha) |
| **Kling** | [https://klingai.io/](https://klingai.io/) |
| **Genmo** | [https://www.genmo.ai](https://www.genmo.ai) |
| **ChatGLM** | [https://chatglm.cn/video?lang=zh](https://chatglm.cn/video?lang=zh) |
| **Xunfei** | [https://typemovie.art/](https://typemovie.art/) |

---

## ❤️ Open-Source Lab T2V Models

| Model | URL |
|-------|-----|
| **Pyramid** | [https://github.com/jy0205/Pyramid-Flow](https://github.com/jy0205/Pyramid-Flow) |
| **Wan2.1** | [https://github.com/FoundationVision/LlamaGen](https://github.com/FoundationVision/LlamaGen) |
| **Allegro** | [https://github.com/rhymes-ai/Allegro](https://github.com/rhymes-ai/Allegro) |
| **VideoCrafter2** | [https://github.com/AILab-CVC/VideoCrafter](https://github.com/AILab-CVC/VideoCrafter) |
| **CogVideo X1.5** | [https://github.com/THUDM/CogVideo](https://github.com/THUDM/CogVideo) |
| **Animate** | [https://github.com/aigc-apps/EasyAnimate](https://github.com/aigc-apps/EasyAnimate) |
| **Lavie** | [https://github.com/Vchitect/LaVie](https://github.com/Vchitect/LaVie) |
| **Hotshot-XL** | [https://github.com/hotshotco/Hotshot-XL](https://github.com/hotshotco/Hotshot-XL) |
| **Latte** | [https://github.com/Vchitect/Latte](https://github.com/Vchitect/Latte) |
| **VideoCrafter1** | [https://github.com/AILab-CVC/VideoCrafter](https://github.com/AILab-CVC/VideoCrafter) |
| **Text2Video-Zero** | [https://github.com/Picsart-AI-Research/Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero) |
| **NOVA** | [https://github.com/baaivision/NOVA](https://github.com/baaivision/NOVA) |
| **ModelScope** | [https://github.com/modelscope/modelscope](https://github.com/modelscope/modelscope) |
| **Tune-A-Video** | [https://github.com/showlab/Tune-A-Video](https://github.com/showlab/Tune-A-Video) |
| **LTX** | [https://github.com/Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) |
| **LVDM** | [https://github.com/YingqingHe/LVDM](https://github.com/YingqingHe/LVDM) |
| **ZeroScope** | [https://huggingface.co/cerspense/zeroscope_v2_XL](https://huggingface.co/cerspense/zeroscope_v2_XL) |
| **LWM** | [https://github.com/LargeWorldModel/LWM](https://github.com/LargeWorldModel/LWM) |

---





# 📊 V2T Interpretation Model Collection

This repository provides a comprehensive list of ** Vision-to-Text (V2T) interpretation models**, covering conventional video quality assessment models, learning-based image-text alignment models, large multimodal models (LMMs), and proprietary foundation models. Each method is annotated with its category and accompanied by a corresponding GitHub or official URL.

---

## 🧭 Categories
- <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" alt="Hugging Face" width="22"/> Conventional VQA Metrics
- ♣️ Classical VQA Models  
- ❤️ Learning-based Scoring Models  
- ⭐ Large Multimodal Models (LMMs)  
- 🔺 Proprietary Foundation Models (Closed-source)

---
## <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" alt="Hugging Face" width="27"/> Conventional VQA Metrics
For
**BMPRI, BPRI, BRISQUE, HOSA, NIQE, QAC**
run:
```
videobench.m
```

## 📚 Model List and URLs

| Category | Method | URL |
|----------|--------|-----|
| ♣️ | **VSFA** | [GitHub](https://github.com/lidq92/VSFA) |
| ♣️ | **BVQA** | [GitHub](https://github.com/vztu/BVQA_Benchmark) |
| ♣️ | **SimpleVQA** | [GitHub](https://github.com/Raykshj/SimpleVQA) |
| ♣️ | **FAST-VQA** | [GitHub](https://github.com/VQAssessment/FAST-VQA-and-FasterVQA) |
| ♣️ | **DOVER** | [GitHub](https://github.com/VQAssessment/DOVER) |
| ❤️ | **CLIPScore** | [GitHub](https://github.com/jmhessel/clipscore) |
| ❤️ | **BLIPScore** | [GitHub](https://github.com/salesforce/BLIP) |
| ❤️ | **AestheticScore** | [GitHub](https://github.com/sorekdj60/AestheticScore) |
| ❤️ | **ImageReward** | [GitHub](https://github.com/THUDM/ImageReward) |
| ❤️ | **PickScore** | [GitHub](https://github.com/yuvalkirstain/PickScore) |
| ❤️ | **HPSv2** | [GitHub](https://github.com/tgxs002/HPSv2) |
| ❤️ | **VQAScore** | [GitHub](https://github.com/linzhiqiu/t2v_metrics) |
| ❤️ | **FGA-BLIP2** | [GitHub](https://github.com/DYEvaLab/EvalMuse) |
| ⭐ | **DeepSeek-VL2** | [GitHub](https://github.com/deepseek-ai/DeepSeek-V2) |
| ⭐ | **Video-LLaVA** | [GitHub](https://github.com/PKU-YuanGroup/Video-LLaVA) |
| ⭐ | **VideoLLaMA3** | [GitHub](https://github.com/DAMO-NLP-SG/VideoLLaMA3) |
| ⭐ | **mPLUG-OWL3** | [GitHub](https://github.com/X-PLUG/mPLUG-Owl) |
| ⭐ | **Qwen2.5-VL** | [GitHub](https://github.com/QwenLM/Qwen2.5-VL) |
| ⭐ | **LLaMA-3.2-Vision** | [HuggingFace](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision) |
| ⭐ | **CogAgent** | [GitHub](https://github.com/THUDM/CogAgent) |
| ⭐ | **LLaVA-NeXT** | [GitHub](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| ⭐ | **InternVideo2.5** | [GitHub](https://github.com/OpenGVLab/InternVideo) |
| ⭐ | **InternVL** | [GitHub](https://github.com/OpenGVLab/InternVL) |
| 🔺 | **Gemini 1.5 Pro** | [Official](https://gemini.google.com) |
| 🔺 | **Claude 3.5** | [Official](https://claude.ai) |
| 🔺 | **Grok2 Vision** | [Official](https://grok.com) |
| 🔺 | **ChatGPT-4o** | [Official](https://chatgpt.com) |

---
## ⚠️ Limitations and Broader Impact

The current rankings are based on data we obtained from randomly-selected professional annotators, and we do not intend to offend the developers of these excellent T2V and V2T models. Although our model shows promising scalability in evaluating AIGVs generated by new prompts and previously unseen T2V models, the effectiveness in real-world applications remains an open question.

We hope that our benchmark and dataset will contribute to the advancement of:
- 🎨 **T2V Generation**
- 📊 **T2V Evaluation**
- 🔁 **V2T Interpretation**


## ⭐ Acknowledgements

Thanks to the original authors of all the models listed here. This is a curated list intended to help researchers and developers in the **T2V generation**,**V2T interpretation** and **multimodal quality assessment** communities.



## 📌 TODO
- ✅ Release the training code 
- ✅ Release the evaluation code 
- ✅ Release the AIGVE-60K Database

