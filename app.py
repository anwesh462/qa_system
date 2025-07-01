from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ''
    if request.method == 'POST':
        question = request.form['question']
        context = request.form['context']
        result = qa_pipeline(question=question, context=context)
        answer = result['answer']
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
