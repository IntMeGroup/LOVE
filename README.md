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

---

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

## 🧪 Evaluation

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

*Note: \textsuperscript{$\dag$} indicates representative values (e.g., resolution, frame rate) that are optional or variable depending on the use case.*



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


## ⭐ Acknowledgements

Thanks to the original authors of all the models listed here. This is a curated list intended to help researchers and developers in the **T2V generation**,**V2T interpretation** and **multimodal quality assessment** communities.



## 📌 TODO
- ✅ Release the training code 
- ✅ Release the evaluation code 
- ✅ Release the AIGVE-60K Database

