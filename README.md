# Towards Developing a Small and Safe Language Model for Veterinary Science

<p align="center">
  <img src="./Image/hero.png" />
</p>

# Datasets
. [VetCorpus](https://huggingface.co/datasets/Harshit159nigam/VetLLM)  
. [VetInstruct (Train)](https://huggingface.co/datasets/Agcs12/VetFinetuneTrain)  
. [VetInstruct (Test)](https://huggingface.co/datasets/Agcs12/VetFinetuningTest)  
. [VetSafe](https://huggingface.co/datasets/Agcs12/vetmixsafe)


# Models
. [VetLM Instruct](https://huggingface.co/Agcs12/vetfinetune3B)  
. [VetLM Safe](https://huggingface.co/Agcs12/vetsafepostrain1epoch)

# Installation 🛠️

We recommend setting up a conda environment before running the project:

[Comment] Before running, configure your Python files with:
 - valid Hugging Face token
 - Weights & Biases API key
 - model checkpoint path
 - dataset path
```bash
conda create --name=vetlm python=3.10
conda activate vetlm

git clone https://github.com/AkashGhosh/Towards-Developing-a-Small-and-Safe-Language-Model-for-Veterinary-Science.git
cd Towards-Developing-a-Small-and-Safe-Language-Model-for-Veterinary-Science/Codes

[Pretrain]
python vet_pretrain_final.py

[Instruction Finetuning]
python vet_finetune.py

[Safety Alignment]
python safety_postrain.py


# About the Paper

**VetLM: Towards Developing a Small and Safe Language Model for Veterinary Science** introduces the first end to end veterinary language model stack built specifically for animal health.

- 🐾 **First Veterinary LLM Suite**  
  We present **VetLM**, a family of small but highly capable veterinary language models (1B and 3B parameters) trained exclusively for veterinary clinical use cases such as diagnostic reasoning, treatment planning, owner communication, and summarization.

- 📚 **Veterinary Scale Pretraining Data (VetCorpus-3M)**  
  We curate **VetCorpus-3M**, approximately 3.3M veterinary documents (around 15.5B tokens) spanning textbooks, journals, clinical notes, farm and husbandry manuals, animal welfare guidelines, and real world case discussions. The data covers multiple species including companion animals, farm animals, and exotics (mammals, birds, fish, reptiles, even insects).

- 🩺 **Instruction Tuning for Clinical Tasks (VetInstruct-120K)**  
  We build **VetInstruct-120K**, a 120K example veterinary instruction dataset for reasoning, treatment planning, summarization, reading comprehension, and realistic role based dialogues (doctor to owner, senior clinician to junior intern, etc.). All outputs are curated and validated by veterinary experts.

- 🛡️ **Safety Alignment with Veterinary Ethics (VetSafe)**  
  We introduce **VetSafe**, a safety alignment dataset inspired by the American Veterinary Medical Association Principles of Veterinary Medical Ethics. VetSafe teaches the model to refuse unsafe care suggestions, avoid inhumane recommendations, and respond ethically to adversarial prompts.

- ⚡ **Small, Fast, Deployable**  
  VetLM 1B and VetLM 3B run in sub second latency on a single A100 GPU (approximately 0.35 to 0.55 seconds per query), enabling real time triage assistance, discharge summary drafting, and owner communication support without requiring massive 70B plus parameter infrastructure.

- 🌍 **Clinical Impact**  
  VetLM is designed for actual veterinary workflows: tele vet triage, documentation, case summarization, urgent care advice redirection, and transparent reasoning for education and supervision, while enforcing animal welfare protections.

---

# The VetLM Pipeline

VetLM is an end to end pipeline: large scale pretraining data, instruction tuning, and safety alignment.

## 1. 🐕 VetCorpus 3M (Continual Pretraining)
- Approximately 3.3M veterinary domain documents (around 15.5B tokens).
- Sources include peer reviewed veterinary literature, standards of care, case reports, clinical narratives, preventive and husbandry guidelines, and owner education material.
- Coverage spans six knowledge domains:
  - Clinical medicine and therapeutics  
  - Diagnostics and procedures  
  - Preventive medicine, husbandry, and welfare  
  - Foundational veterinary science  
  - Evidence based veterinary research  
  - Client communication and professional conduct
- Broad species coverage across small animals, large animals, avian, aquatic, and exotic cases.

## 2. 🧠 VetInstruct 120K (Instruction Fine Tuning)
- 120K expert validated instruction and response pairs covering:
  - Diagnostic reasoning  
  - Causal analysis (why is this happening)  
  - Treatment planning  
  - Clinical summarization  
  - Reading comprehension of veterinary texts  
  - Owner facing and clinician facing dialogues  
  - Rationale generation (explain your answer)
- Data is produced with controlled prompting and then cleaned by veterinarians for factual accuracy, safety, and tone.

## 3. 🔒 VetSafe (Safety Alignment)
- More than 3K expert audited unsafe query to safe response pairs.
- Includes adversarial prompts intended to trigger harmful or unethical advice (for example, inhumane handling, unsupervised medication dosing, or advice that ignores urgent symptoms).
- The aligned model is trained to:
  - Refuse unsafe requests  
  - Redirect owners toward urgent in person veterinary care when required  
  - Avoid enabling animal harm, abuse, or suffering
- Safety tuning improves measured safety compliance by more than 60 percent, with only a small (about 2 to 3 percent) drop in raw generation quality. This is an intentional tradeoff for deployment.

---

# Evaluation Results

We benchmark VetLM against strong open source general purpose models such as Llama 3.x, Gemma 2, Qwen 3, Phi 3.5, and others.

All models are evaluated on the VetInstruct benchmark with five shot prompting across:
- Summarization  
- Clinical reasoning  
- Reading comprehension  
- Rationale generation  
- Role based dialogue

We report ROUGE 1, ROUGE 2, ROUGE L, BLEU 1 through BLEU 4, and BERTScore. GitHub Flavored Markdown supports tables using pipes and dashes, which makes it convenient to present quantitative model comparisons in README files. :contentReference[oaicite:1]{index=1}

**Highlights**
- VetLM 3B is the top performer across most metrics, outperforming even 70B scale general models.
- VetLM 1B, despite being roughly a 1B parameter model, matches or beats models an order of magnitude larger on domain specific tasks.
- Safety aligned variants remain competitive while being substantially safer.

| Model               | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 |
|---------------------|---------|---------|---------|-----------|--------|--------|--------|--------|
| **VetLM 3B**        | **45.1** | **18.8** | **30.2** | **88.2**  | **67.5** | **54.3** | **38.8** | **29.6** |
| **VetLM 1B**        | 43.7    | 16.7    | 28.1    | 87.8      | 66.8   | 53.9   | 38.5   | **29.6** |
| VetLM 3B (Safe)     | 43.5    | 16.0    | 29.2    | 87.6      | 65.0   | 52.0   | 37.8   | 28.8   |
| VetLM 1B (Safe)     | 41.5    | 15.5    | 27.5    | 87.2      | 64.5   | 51.5   | 36.9   | 28.4   |
| Llama-3.3-70B       | 37.3    | 14.1    | 22.6    | 87.2      | 45.5   | 40.8   | 31.0   | 23.8   |
| Llama-3.2-3B        | 32.5    | 10.9    | 20.2    | 85.6      | 51.2   | 41.6   | 28.4   | 20.6   |
| Llama-3.1-70B       | 22.3    | 5.0     | 14.2    | 83.2      | 44.3   | 33.5   | 19.9   | 12.6   |
| Gemma-2-27B         | 28.6    | 9.7     | 18.0    | 84.2      | 40.3   | 34.0   | 24.2   | 17.7   |
| Gemma-2-2B          | 25.5    | 7.8     | 15.8    | 83.1      | 41.1   | 33.0   | 22.0   | 15.6   |
| Qwen-3-32B          | 30.3    | 11.5    | 20.4    | 85.8      | 37.2   | 30.3   | 21.0   | 15.7   |
| Qwen-2-1.5B         | 31.9    | 10.1    | 20.5    | 85.4      | 55.0   | 43.2   | 28.6   | 20.4   |
| Phi-3.5-Mini        | 28.1    | 10.4    | 18.2    | 82.5      | 45.0   | 35.2   | 24.7   | 18.6   |

---

# Human Evaluation

Automated scores alone are not enough in a medical or safety critical domain, so we also run human and expert style evaluation.

## Pairwise Preference
Experts compared blinded answers from VetLM 3B and larger general models such as Llama 3.3 70B across more than one hundred prompts. VetLM 3B was preferred for clinical reasoning, triage like dialogue, and owner facing guidance. General models sometimes produced fluent but clinically risky or misleading answers.

## Quality Scoring
Experts then rated each answer on a zero to six scale for factuality, safety, clinical usefulness, and clarity. VetLM 3B received the highest mean score, followed by VetLM 1B, while larger general models trailed due to unsafe or overconfident recommendations.

**Takeaway**  
Veterinary-aligned behavior was consistently valued over raw linguistic fluency. Answers that sounded confident but gave unsafe guidance were downgraded.

---

# Qualitative Evaluation

<p align="center">
  <img src="./Image/hello.drawio.png" />
</p>

<p align="center">
  <img src="./Image/hello1.drawio.png" />
</p>






