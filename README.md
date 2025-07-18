# 📝 Text Summarizer using BART and Flask

This project is a **Web-Based Text Summarizer** built using Python, Flask, and Hugging Face Transformers. It uses a powerful pretrained model — `facebook/bart-large-cnn` — to generate concise summaries from long pieces of text. Whether you're summarizing articles, research papers, or lengthy reports, this tool can give you fast, accurate, and readable results.

---

## 🎯 Project Overview

The goal of this project is to:
- Provide an easy-to-use web interface for text summarization
- Utilize state-of-the-art transformer models
- Help users quickly get the gist of long documents
- Serve as a beginner-friendly project for those learning Flask and NLP

The summarization is powered by the **BART (Bidirectional and Auto-Regressive Transformers)** model from Facebook AI, fine-tuned on CNN/DailyMail dataset, capable of producing high-quality extractive and abstractive summaries.

---

## 🧠 How It Works

- The user enters long text into a web form.
- Flask receives the input and sends it to the Hugging Face summarization pipeline.
- The pipeline tokenizes the text, passes it to the pretrained `facebook/bart-large-cnn` model, and generates a summary.
- The summary is displayed back to the user in the browser.

---

## 🖼️ Screenshots

### 1. Input Form

This is the initial interface where the user enters the long text:

![Input Screen](image.png)

---

### 2. Summary Output

After clicking the "Summarize" button, the app shows the summarized text:

![Summary Output](image_output.png)
---

## 🔍 Key Technologies

| Technology | Description |
|------------|-------------|
| **Flask** | Lightweight Python web framework used for routing and rendering |
| **Hugging Face Transformers** | NLP library for using pretrained models like BART |
| **facebook/bart-large-cnn** | Pretrained summarization model |
| **HTML (Jinja2)** | Template for frontend interface |

---


