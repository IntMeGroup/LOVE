# 

<div align="center">
   <h1>❤️LOVE：Benchmarking and Evaluating Text-to-Video Generation and Video-to-Text Interpretation</h1>
   <i>How to evaluate Text to Video Generation Model properly?</i>
   <div>
      <a href="https://huggingface.co/datasets/anonymousdb/AIGVE-60K"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-green"></a>
   </div>
</div>
<img width="1000" alt="LOVE" src="https://github.com/user-attachments/assets/20901a3b-68e8-4b65-89b1-acbe38ae7165" />


## ![Hugging Face](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)AIGVE-60K Download
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


## 📌 TODO
- ✅ Release the training code 
- ✅ Release the evaluation code 
- ✅ Release the AIGVE-60K Database

