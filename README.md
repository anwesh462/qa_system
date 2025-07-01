# QA System – BERT-based Question Answering App

This project is a Question Answering (QA) system that uses transformer models (BERT) from Hugging Face to answer questions based on input context. It features a simple Flask web interface where users can input a paragraph and ask a natural-language question. The system then returns the most probable answer extracted from the context.

---

## Features

- Accepts user-input context and question
- Answers questions using pretrained transformer models from Hugging Face
- Fast and accurate with support for local inference
- Lightweight Flask-based web app — simple to run and extend

---

## Model Used

- distilbert-base-uncased-distilled-squad
  - A compact version of BERT fine-tuned on the SQuAD dataset for extractive question answering.
  - Runs fast even on CPUs.

---

## Folder Structure

qa_system/
├── app.py               # Flask web application  
├── qa_model.py          # Script to test model without web interface  
├── templates/  
│   └── index.html       # Web UI for input/output  
├── requirements.txt     # Project dependencies  

---

## How to Run Locally

### Step 1: Clone the Repository

git clone https://github.com/YOUR_USERNAME/qa_system.git  
cd qa_system

### Step 2: Install Required Packages

pip install -r requirements.txt

If not already installed, also install PyTorch:

pip install torch

### Step 3: Run the Flask App

python app.py

### Step 4: Open in Browser

http://127.0.0.1:5000

---

## Example Usage

Context:
India gained independence from British rule on 15th August 1947.

Question:
When did India gain independence?

Answer:
15th August 1947



## Acknowledgements

- Hugging Face Transformers
- SQuAD Dataset
- Flask Web Framework
