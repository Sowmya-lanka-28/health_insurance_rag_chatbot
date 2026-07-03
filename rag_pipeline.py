import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

load_dotenv()


# Load and split documents
def load_documents():
    with open("policy_data.csv", "r", encoding="utf-8") as file:
        text = file.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )


    chunks = splitter.split_text(text)

    return chunks


# Create vector store
def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()

    vector_store = FAISS.from_texts(chunks, embeddings)

    return vector_store


# Ask question
def ask_question(vector_store, question):

    # Retrieve relevant docs
    docs = vector_store.similarity_search(question, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    # Insert variables into prompt
    prompt = f"""
You are a healthcare insurance assistant.

Use the following policy context to answer the question.

Context:
{context}

Question:
{question}

Give a short and clear answer.
"""

    response = llm.invoke(prompt)

    return response.content