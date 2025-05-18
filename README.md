# 

<div align="center">
   <h1>❤️LOVE：Benchmarking and Evaluating Text-to-Video Generation and Video-to-Text Interpretation</h1>
   <i>How to evaluate Text to Video Generation Model properly?</i>
   <div>
      <a href="https://huggingface.co/datasets/anonymousdb/AIGVE-60K"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-green"></a>
   </div>
</div>
<img width="1000" alt="LOVE" src="https://github.com/user-attachments/assets/20901a3b-68e8-4b65-89b1-acbe38ae7165" />


## <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face" width="27"/> AIGVE-60K Download
 <a href="https://huggingface.co/datasets/anonymousdb/AIGVE-60K"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-green"></a>
```
huggingface-cli download anonymousdb/AIGVE-60K --repo-type dataset --local-dir ./AIGVE-60K
```
## 🛠️ Installation

Clone this repository:
```
git clone https://github.com/IntMeGroup/LOVE.git
```
Create a conda virtual environment and activate it:
```
conda create -n LOVE python=3.9 -y
conda activate LOVE
```
Install dependencies using requirements.txt:
```
pip install -r requirements.txt
```
Install flash-attn==2.3.6
```
pip install flash-attn==2.3.6 --no-build-isolation
```
Alternatively you can compile from source:
```
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention
git checkout v2.3.6
python setup.py install
```

## 🌈 Training
Preparation
```
huggingface-cli download anonymousdb/AIGVE-60K/data --repo-type dataset --local-dir ./data
```

for stage1 training (Text-based quality levels)

```
sh shell/st1_train.sh
```
for stage2 training (Fine-tuning the vision encoder and LLM with LoRA)

```
sh shell/st2_train.sh
```

for quastion-answering training (QA)
```
sh shell/train_qa.sh
```

## 🌈 Evaluation
Download the pretrained weights
```
huggingface-cli download anonymousdb/LOVE-Perception --local-dir ./weights/stage2/stage2_mos1
huggingface-cli download anonymousdb/LOVE-Correspondence --local-dir ./weights/stage2/stage2_mos2
huggingface-cli download anonymousdb/LOVE-QA --local-dir ./weights/qa
```

for [perception](https://huggingface.co/anonymousdb/LOVE-Perception) and [correspondence](https://huggingface.co/anonymousdb/LOVE-Correspondence) score evaluation (Scores)

```
sh shell/eval_score.sh
```

for [quastion-answering](https://huggingface.co/anonymousdb/LOVE-QA) evaluation (QA)
```
sh shell/eval_qa.sh
```
## <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" alt="Hugging Face" width="27"/> Conventional VQA Metrics
For
**BMPRI, BPRI, BRISQUE, HOSA, NIQE, QAC**
run:
```
videobench.m
```
# 📊 V2T Interpretation Model Collection

This repository provides a comprehensive list of **30 Vision-to-Text (V2T) interpretation models**, covering traditional video quality assessment models, learning-based image-text alignment models, large multimodal models (LMMs), and proprietary foundation models. Each method is annotated with its category and accompanied by a corresponding GitHub or official URL.

---

## 🧭 Categories

- ♣️ Classical VQA Models  
- ❤️ Learning-based Scoring Models  
- ⭐ Large Multimodal Models (LMMs)  
- 🔺 Proprietary Foundation Models (Closed-source)

---

## 📚 Model List and URLs

| Category | Method | URL |
|----------|--------|-----|
| ♣️ | **VSFA** [[paper]](https://arxiv.org/abs/1908.02463) | [GitHub](https://github.com/lidq92/VSFA) |
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

## 📌 Citation Notice

If you use this list or part of the benchmark in your research, please consider citing the original papers listed above.

---

## 🔧 Contributions

If you'd like to contribute a new model, open an issue or submit a pull request with:

- Model name
- URL (GitHub or official site)
- Paper reference (if available)
- Category suggestion

---

## ⭐ Acknowledgements

Thanks to the original authors of all the models listed here. This is a curated list intended to help researchers and developers in the **V2T interpretation** and **multimodal quality assessment** communities.



## 📌 TODO
- ✅ Release the training code 
- ✅ Release the evaluation code 
- ✅ Release the AIGVE-60K Database

