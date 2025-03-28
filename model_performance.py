import os
from tkinter import Tk, filedialog
from rouge import Rouge
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt
from bert_score import score

def select_file(file_type):
    """
    Open a file dialog to select a file and return the file path.

    Args:
        file_type (str): File type to filter (e.g., 'txt', 'pdf').

    Returns:
        str: Selected file path.
    """
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf")]
    )
    return file_path

def read_file(file_path):
    """
    Read text from a .txt or .pdf file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: File content as text.
    """
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    elif file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = "".join(page.extract_text() for page in reader.pages)
        return text
    else:
        raise ValueError("Unsupported file format. Only .txt and .pdf are allowed.")

def calculate_rouge_scores(model_summary, ref_summary):
    """
    Calculate ROUGE scores between the model-generated summary and referance summary.

    Args:
        model_summary (str): Summary generated by the model.
        ref_summary (str): Reference summary from referance.

    Returns:
        dict: ROUGE-1, ROUGE-2, and ROUGE-L scores.
    """
    rouge = Rouge()
    scores = rouge.get_scores(model_summary, ref_summary, avg=True)
    return {
        "ROUGE-1": scores["rouge-1"],
        "ROUGE-2": scores["rouge-2"],
        "ROUGE-L": scores["rouge-l"],
    }


def calculate_bertscore(model_summary, ref_summary):
    """
    Calculate BERTScore for Turkish fairy tales and summaries.

    Args:
        model_summary (str): Summary generated by the model.
        ref_summary (str): Reference summary.

    Returns:
        dict: BERTScore results (Precision, Recall, F1).
    """
    try:
        # Convert summaries to list
        model_summaries = [model_summary]
        referance_summaries = [ref_summary]

        # Calculate BERTScore using a Turkish-supported model
        precisions, recalls, f1s = score(
            model_summaries,
            referance_summaries,
            lang="tr",
            model_type="xlm-roberta-base"
        )

        # Return scores
        return {
            "Precision": round(precisions.mean().item(), 4),
            "Recall": round(recalls.mean().item(), 4),
            "F1": round(f1s.mean().item(), 4)
        }
    except Exception as e:
        print(f"Error during BERTScore calculation: {e}")
        return {"Precision": 0, "Recall": 0, "F1": 0}


if __name__ == "__main__":
    print("Upload model-generated summary.")
    model_summary_path = select_file("txt or pdf")
    print("Upload reference summary.")
    ref_summary_path = select_file("txt or pdf")

    # Read the files
    model_summary = read_file(model_summary_path)
    ref_summary = read_file(ref_summary_path)

    # Calculate ROUGE scores
    rouge_scores = calculate_rouge_scores(model_summary, ref_summary)

    # Calculate BERTScore
    bert_scores = calculate_bertscore(model_summary, ref_summary)

    # ROUGE-1
    rouge1_prec = round(rouge_scores["ROUGE-1"]["p"], 4)
    rouge1_rec = round(rouge_scores["ROUGE-1"]["r"], 4)
    rouge1_f1 = round(rouge_scores["ROUGE-1"]["f"], 4)

    # ROUGE-2
    rouge2_prec = round(rouge_scores["ROUGE-2"]["p"], 4)
    rouge2_rec = round(rouge_scores["ROUGE-2"]["r"], 4)
    rouge2_f1 = round(rouge_scores["ROUGE-2"]["f"], 4)

    # ROUGE-L
    rougel_prec = round(rouge_scores["ROUGE-L"]["p"], 4)
    rougel_rec = round(rouge_scores["ROUGE-L"]["r"], 4)
    rougel_f1 = round(rouge_scores["ROUGE-L"]["f"], 4)

    # BERTScore
    bert_prec = round(bert_scores["Precision"], 4)
    bert_rec = round(bert_scores["Recall"], 4)
    bert_f1 = round(bert_scores["F1"], 4)

    # Create DataFrame
    df = pd.DataFrame(index=["ROUGE-1", "ROUGE-2", "ROUGE-L", "BERTScore"],
                      columns=["Precision", "Recall", "F1-score"])

    # Assign values
    df.loc["ROUGE-1"] = [rouge1_prec, rouge1_rec, rouge1_f1]
    df.loc["ROUGE-2"] = [rouge2_prec, rouge2_rec, rouge2_f1]
    df.loc["ROUGE-L"] = [rougel_prec, rougel_rec, rougel_f1]
    df.loc["BERTScore"] = [bert_prec, bert_rec, bert_f1]

    print(df, "\n")

    # Save as PNG
    model_basename = os.path.splitext(os.path.basename(model_summary_path))[0]
    os.makedirs("metrics", exist_ok=True)
    output_path = f"metrics/{model_basename}.png"

    plt.figure(figsize=(5, 2.5))
    plt.axis('off')

    the_table = plt.table(cellText=df.values,
                          rowLabels=df.index,
                          colLabels=df.columns,
                          loc='center',
                          cellLoc='center')

    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(1.2, 1.2)

    plt.savefig(output_path, bbox_inches='tight')
    print(f"Results saved as '{output_path}'")
