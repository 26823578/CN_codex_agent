# Prompts History (Skeleton: 20 entries simulating AI collaboration)

1. Prompt: Generate a basic Streamlit app structure for file upload and Q&A. → AI: Provided skeleton code for app.py.
2. Prompt: How to parse PDF, DOCX, TXT in Python? → AI: Suggested PyPDF2, python-docx, file.read().
3. Prompt: Implement sentence-based chunking with token limits using NLTK and tiktoken. → AI: Gave chunk_text function draft.
4. Prompt: Best way to use FAISS for RAG in Python? → AI: Recommended IndexFlatL2 for small scale.
5. Prompt: Create OpenAI embedding function. → AI: client.embeddings.create example.
6. Prompt: Design mode-specific system prompts for agent. → AI: Suggested templates for each mode.
7. Prompt: Add retrieval function with k=3. → AI: search and extract texts.
8. Prompt: Handle session state in Streamlit for vectorstore. → AI: Use st.session_state.
9. Prompt: Estimate tokens to avoid context overflow. → AI: tiktoken usage.
10. Prompt: Error handling for API calls. → AI: Try-except blocks (added manually).
11. Prompt: Test chunking function. → AI: Pytest example for chunk sizes.
12. Prompt: Test retrieval accuracy. → AI: Mock index test.
13. Prompt: Write README sections. → AI: Outline for design choices.
14. Prompt: Simulate commit log. → AI: Sample git-like logs.
15. Prompt: Agent instructions for sub-agents. → AI: Defined roles like 'chunker' and 'prompter'.
16. Prompt: Prompt examples for Q&A. → AI: 10 sample questions.
17. Prompt: Improve overlap in chunking. → AI: Reverse accumulate for overlap.
18. Prompt: Add progress spinner in UI. → AI: st.spinner.
19. Prompt: Modularize into files. → AI: Suggested app/ingest/utils/prompts split.
20. Prompt: Final refinements for modes. → AI: Tweaked humble_brag to be grounded.