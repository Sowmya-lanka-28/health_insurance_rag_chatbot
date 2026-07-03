# 🏥 Health Insurance RAG Chatbot

## 📖 Project Overview

The Health Insurance RAG Chatbot is an AI-powered question-answering system that helps users understand health insurance policies using Retrieval-Augmented Generation (RAG). The chatbot retrieves relevant policy information and generates accurate answers using a Large Language Model.

---

## 🚀 Features

- Ask questions about health insurance policies
- Intelligent semantic search
- Retrieval-Augmented Generation (RAG)
- Natural language responses
- Streamlit-based user interface
- FAISS vector database for efficient retrieval

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- OpenAI
- FAISS
- Python Dotenv

---

## 🏗 Project Architecture

User Question

↓

Streamlit Interface

↓

LangChain

↓

FAISS Vector Database

↓

Relevant Policy Content

↓

OpenAI GPT Model

↓

Generated Answer

---

## 📂 Project Structure

health_insurance_rag_chatbot/

├── app.py

├── rag_pipeline.py

├── policy_data.csv

├── requirements.txt

├── README.md


---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Sowmya-lanka-28/health_insurance_rag_chatbot.git
```

Move into the project

```bash
cd health_insurance_rag_chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
OPENAI_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app.py
```

---

## 💬 Sample Questions

- What is the waiting period?
- Does the policy cover maternity expenses?
- Is ambulance service covered?
- What documents are required to file a claim?
- What are the policy exclusions?

---



## 👩‍💻 Author

**Sowmya Lanka**

Data Scientist | GenAI Engineer

LinkedIn:
https://linkedin.com/in/sowmya-lanka-323806400
