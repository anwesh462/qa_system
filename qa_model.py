from transformers import pipeline

# Load pretrained QA pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Test
context = "India gained independence from British rule on 15th August 1947."
question = "When did India become independent?"

result = qa_pipeline(question=question, context=context)
print(result['answer'])  # Output: 15th August 1947
