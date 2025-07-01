# 🧠 QA System – BERT-based Question Answering App

This project is a **Question Answering (QA) system** that uses **transformer models (BERT)** from Hugging Face to answer questions based on input context. It features a simple **Flask web interface** where users can input a paragraph and ask a natural-language question. The system then returns the most probable answer extracted from the context.

---

## 🚀 Features

- ✅ Accepts user-input **context** and **question**
- ✅ Answers questions using **pretrained transformer models** from Hugging Face
- ✅ Fast and accurate with support for local or API-based inference
- ✅ Lightweight Flask-based web app — can be extended easily

---

## 🧠 Model Used

- `distilbert-base-uncased-distilled-squad`
  - A compact version of BERT fine-tuned on **SQuAD (Stanford Question Answering Dataset)**.
  - Maintained by Hugging Face.

---

## 🖥️ How It Works

1. User enters a **context paragraph** and a **question**
2. The app feeds the input to the QA model via Hugging Face's `pipeline()`
3. The model extracts the **most likely answer span** from the given context
4. The answer is displayed in the web interface

---

## 📦 Installation

### 🧱 Requirements

- Python 3.7+
- pip
