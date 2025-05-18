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
---
## 🏆 T2V Generation Model Leaderboard 

This leaderboard presents the performance of 30 models on the **AIGVE-60K** benchmark, evaluating across three key dimensions:  
- **Perception Quality** 
- **Text-to-Video Correspondence**  
- **Question Answering Accuracy**

Final **Overall Rank** is computed by summing the individual ranks across these three dimensions.
|   Overall Rank | Model                                                                           |   Perception |   Perception Rank |   Correspondence |   Correspondence Rank |   TaskAccuracy |   TaskAccuracy Rank |
|---------------:|:--------------------------------------------------------------------------------|-------------:|------------------:|-----------------:|----------------------:|---------------:|--------------------:|
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
## 🏆 V2T Interpretation Model Leaderboard 

This leaderboard presents the performance of 48 models on the **AIGVE-60K** benchmark, evaluating across three key dimensions:  
- **Perception Quality** (Instance-level SRCC)  
- **Text-to-Video Correspondence** (Instance-level SRCC)  
- **Question Answering Accuracy**

Final **Overall Rank** is computed by summing the individual ranks across these three dimensions.

| 🏆 Rank | Method | Perception SRCC | 🔗 Rank | Correspondence SRCC | 🔗 Rank | QA Acc (%) | 🔗 Rank |
|------|--------|------------------|------|----------------------|------|-------------|------|
| 🥇 | **LOVE** | 0.7932 | 1 | 0.7466 | 1 | 78.69 | 1 |
| 🥈 | **InternVL3 (9B)** | 0.6421 | 3 | 0.5965 | 5 | 78.36 | 2 |
| 🥉 | **Qwen2.5-VL (7B)** | 0.7868 | 2 | 0.7354 | 2 | 77.35 | 3 |
| 4 | **InternVL2.5 (72B)** | 0.5383 | 8 | 0.6612 | 7 | 75.18 | 5 |
| 5 | **Grok2 Vision** | 0.5628 | 5 | 0.6659 | 6 | 76.51 | 4 |
| 6 | **ChatGPT-4o** | 0.5263 | 9 | 0.6639 | 8 | 74.84 | 6 |
| 7 | **InternVL3 (72B)** | 0.5441 | 7 | 0.6314 | 9 | 74.59 | 7 |
| 8 | **InternVL2.5 (38B)** | 0.6227 | 4 | 0.6470 | 8 | 75.81 | 5 |
| 9 | **Gemini1.5-pro** | 0.4972 | 10 | 0.6095 | 10 | 73.38 | 8 |
| 10 | **Claude3.5** | 0.4267 | 13 | 0.5827 | 11 | 73.20 | 9 |
| 11 | **Qwen2.5-VL (72B)** | 0.4245 | 14 | 0.6272 | 10 | 73.83 | 10 |
| 12 | **InternVL3 (38B)** | 0.4950 | 11 | 0.5996 | 12 | 73.89 | 9 |
| 13 | **Llava-one-vision (72B)** | 0.5291 | 6 | 0.5702 | 13 | 73.31 | 11 |
| 14 | **Qwen2-VL (72B)** | 0.4628 | 12 | 0.5598 | 14 | 73.12 | 12 |
| 15 | **InternVL3 (9B)** | 0.2731 | 24 | 0.4768 | 20 | 65.82 | 19 |
| 16 | **InternVL2.5 (8B)** | 0.2799 | 22 | 0.4856 | 19 | 66.30 | 18 |
| 17 | **VideoLLaMA3** | 0.3922 | 16 | 0.4228 | 23 | 70.16 | 14 |
| 18 | **InternVideo2.5 (8B)** | 0.1563 | 37 | 0.4978 | 17 | 70.64 | 13 |
| 19 | **LLaVA-NeXT** | 0.4888 | 12 | 0.2847 | 30 | 70.21 | 15 |
| 20 | **Qwen2-VL (7B)** | 0.3568 | 18 | 0.4498 | 21 | 71.56 | 11 |
| 21 | **HPSv2** | 0.5415 | 7 | 0.4989 | 16 | 67.68 | 17 |
| 22 | **FGA-BLIP2** | 0.5181 | 8 | 0.5962 | 5 | 67.06 | 20 |
| 23 | **ImageReward** | 0.4180 | 15 | 0.5076 | 15 | 68.33 | 16 |
| 24 | **CogAgent** | 0.1244 | 40 | 0.1190 | 39 | 65.32 | 21 |
| 25 | **mPLUG-Owl3 (7B)** | 0.3532 | 19 | 0.5478 | 18 | 63.02 | 23 |
| 26 | **PickScore** | 0.4026 | 17 | 0.4135 | 24 | 62.29 | 25 |
| 27 | **VideoLlava (7B)** | 0.1809 | 33 | 0.2005 | 33 | 68.46 | 16 |
| 28 | **AestheticScore** | 0.5524 | 6 | 0.3931 | 26 | 64.87 | 22 |
| 29 | **SimpleVQA** | 0.5631 | 5 | 0.3474 | 27 | 60.78 | 26 |
| 30 | **FAST-VQA** | 0.6391 | 2 | 0.3919 | 28 | 66.27 | 17 |
| 31 | **DOVER** | 0.6414 | 1 | 0.3759 | 29 | 62.61 | 24 |
| 32 | **VSFA** | 0.3750 | 20 | 0.2438 | 32 | 57.09 | 29 |
| 33 | **BVQA** | 0.3089 | 23 | 0.2379 | 34 | 58.47 | 27 |
| 34 | **CLIPScore** | 0.0947 | 43 | 0.2290 | 35 | 58.27 | 28 |
| 35 | **BLIPScore** | 0.1884 | 32 | 0.3163 | 31 | 63.93 | 22 |
| 36 | **VQAScore** | 0.1677 | 34 | 0.1763 | 37 | 52.97 | 31 |
| 37 | **QAC** | 0.5958 | 4 | 0.3948 | 25 | 64.40 | 30 |
| 38 | **BRISQUE** | 0.5843 | 3 | 0.3806 | 30 | 64.67 | 26 |
| 39 | **HOSA** | 0.6474 | 1 | 0.4153 | 22 | 64.34 | 27 |
| 40 | **NIQE** | 0.6536 | 1 | 0.4345 | 19 | 62.21 | 32 |
| 41 | **BMPRI** | 0.5741 | 4 | 0.3618 | 31 | 64.00 | 28 |
| 42 | **BPRI** | 0.3558 | 21 | 0.2018 | 32 | 63.56 | 30 |
| 43 | **V-Aesthetic Quality** | 0.5031 | 9 | 0.4033 | 26 | 64.54 | 29 |
| 44 | **V-Imaging Quality** | 0.2810 | 25 | 0.1952 | 36 | 60.60 | 33 |
| 45 | **V-Temporal Flickering** | 0.4076 | 16 | 0.1958 | 35 | 63.69 | 30 |
| 46 | **V-Subject Consistency** | 0.3443 | 20 | 0.1647 | 38 | 62.52 | 33 |
| 47 | **V-Overall Consistency** | 0.1559 | 35 | 0.3076 | 30 | 61.96 | 34 |
| 48 | **DeepseekVL2 (1B)** | 0.0121 | 48 | 0.0173 | 48 | 39.29 | 48 |

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

