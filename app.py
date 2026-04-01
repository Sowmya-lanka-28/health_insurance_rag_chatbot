import streamlit as st
from rag_pipeline import load_documents, create_vector_store, ask_question

st.title("Health Insurance Policy Chatbot")

# Load and build vector store
chunks = load_documents()
vector_store = create_vector_store(chunks)

# User input
question = st.text_input("Ask a question about the health insurance policy:")

if question:
    answer = ask_question(vector_store, question)

    st.write("### Answer:")
    st.write(answer)
