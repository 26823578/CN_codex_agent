import streamlit as st
from ingest import ingest_documents, build_faiss_index, retrieve_chunks
from prompts import get_system_prompt, get_user_prompt
from utils import get_openai_client, estimate_tokens
import os
import time

# Reasoning: app.py serves as the main entry point for the Streamlit UI. It handles file uploads, ingestion triggering, session state management 
# for the vector store, question input, mode selection, and response generation. 
# This separation keeps UI logic clean from ingestion and prompting. Streamlit's session state is used to persist
#  the FAISS index across interactions, avoiding re-ingestion on every query. 
# The mode switcher is implemented as a selectbox to match the bonus feature, altering the prompt accordingly.

from dotenv import load_dotenv
load_dotenv()

client = get_openai_client()

st.title("Welcome to your Personal Codex — Candidate Agent")

# Sidebar for file uploads and ingest button
with st.sidebar:
    st.header("Document Ingestion")
    uploaded_files = st.file_uploader("Upload your documents (CV, blogs, etc.)", accept_multiple_files=True, type=['pdf', 'docx', 'txt'])
    if st.button("Re-run Ingest") or 'vectorstore' not in st.session_state:
        if uploaded_files:
            with st.spinner("Ingesting documents..."):
                texts = ingest_documents(uploaded_files)
                st.session_state.vectorstore = build_faiss_index(texts)
                st.success("Ingestion complete!")
        else:
            st.warning("Please upload files first.")

# Main panel for Q&A
st.header("Ask a Question")
question = st.text_input("Enter your question:")
mode = st.selectbox("Response Mode", ["interview", "story", "fast", "humble_brag"])

if question and 'vectorstore' in st.session_state:
    with st.spinner("Generating response..."):
        # Retrieve relevant chunks
        chunks = retrieve_chunks(question, st.session_state.vectorstore)
        
        # Prepare prompt
        system_prompt = get_system_prompt(mode)
        user_prompt = get_user_prompt(question, chunks)
        
        # Estimate tokens to avoid overflow
        total_tokens = estimate_tokens(system_prompt + user_prompt)
        if total_tokens > 8000:  # Safety buffer for gpt-4o-mini
            st.error("Query too complex; try a simpler question.")
        else:
            # Call LLM
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            st.write(response.choices[0].message.content)