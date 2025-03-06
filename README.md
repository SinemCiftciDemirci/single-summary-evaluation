# 📊 Single Summary Evaluation

This project evaluates and compares the quality of text summaries using the **ROUGE** and **BERTScore** metrics. It is particularly useful for objectively assessing and visualizing the performance of text summarization models.

---
🔗 Related Projects This project is part of a modular research framework for evaluating and improving fairy tale summarization models. Below are the related repositories:

| Children's Tale Summarizer - Flask App | The main Flask-based API that generates fairy tale summaries. (https://github.com/SinemCiftciDemirci/childrens-tale-summarizer-flask-app) |

| GPT Summarizer | Creates GPT-based fairy tale summaries. (https://github.com/SinemCiftciDemirci/gpt-summarizer) |

| Cosine Similarity Summarizer | Performs extractive summarization using cosine similarity. (https://github.com/SinemCiftciDemirci/cosine-similarity-summarizer) |

| Single Summary Evaluation | Measures the performance of a single summary using BERTScore and ROUGE score. (https://github.com/SinemCiftciDemirci/single-summary-evaluation) |

| Batch Summary Performance Evaluation | Compares model-generated summaries with GPT and Cosine-based reference summaries, calculating ROUGE and BERTScore collectively. (https://github.com/SinemCiftciDemirci/batch-summary-performance-evaluation) |

| Summary Performance Comparison | Creates visual performance comparisons from the Model_Performance.xlsx file produced in the Batch Summary Evaluation repo. (https://github.com/SinemCiftciDemirci/summary-performance-comparison) |

| Vision Model Test | Translates the generated summaries into English and creates three visuals: introduction, development, and conclusion. (https://github.com/SinemCiftciDemirci/vision-model-test) |

Each repository serves a unique role in evaluating or improving summarization models. You can use them individually or together for deeper analysis.

## 🚀 Features

- **Supports `.txt` and `.pdf` files** for input summaries.
- Calculates detailed metrics:
  - ✅ **ROUGE-1, ROUGE-2, ROUGE-L**
  - ✅ **BERTScore (Precision, Recall, F1-score)** optimized for Turkish
- Outputs results clearly in a DataFrame and visualizes them as a PNG file.

---

## 🗂️ Project Structure

```
summarization-model-performance/
├── model_performance.py
├── metrics/
│   └── your_summary.png
├── README.md

```

---

## 📌 Installation

Make sure to install required dependencies using `pip`:

```bash
pip install rouge
pip install bert-score
pip install transformers
pip install pandas matplotlib PyPDF2
```

---

## 🎯 Usage

1. **Run the script**

```bash
python model_performance.py
```

2. **Select files**

- A dialog box will prompt you to choose two files:
  - 📄 **Model-generated summary**
  - 📄 **Reference summary (e.g., GPT-generated, cos-similarity)**

3. **Review the results**

- A summary evaluation table will be displayed in the terminal.
- Visual results will be saved automatically in:

```
metrics/your_summary.png
```

---

## 🛠️ How It Works

The tool calculates the similarity and quality of summaries using two robust methods:

- **ROUGE Scores**: Measures overlap between the generated and reference summaries at unigram, bigram, and sentence levels.
- **BERTScore**: Measures semantic similarity using a transformer-based language model (`xlm-roberta-base`), ideal for Turkish texts.

Results are presented clearly and visually for easy interpretation.

---

## 🔍 Troubleshooting

- Ensure all required Python libraries are installed.
- Verify selected files are in `.txt` or `.pdf` format.
- Check terminal output for any detailed error messages.

---

## 📜 License

This project is open-source under the MIT License. Feel free to use, modify, and distribute.
