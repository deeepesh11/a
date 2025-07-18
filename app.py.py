from flask import Flask , request, render_template
from transformers import pipeline

app = Flask(_name_)

summarizer = pipeline('summarization', model="facebook/bart-large-cnn")


@app.route('/',methods=['GET','POST'])
def index():
  summary = ""
  if request.method == 'POST':
    input_text = request.form['input_text']
    if input_text:
      summary_output= summarizer(
          input_text,
          max_length=150,
          min_length=30,
          do_sample=False
      )
      summary = summary_output[0]['summary_text']
  return render_template('index.html', summary=summary)

if _name_ == '_main_':
    app.run(debug=True,port=5000)