# CN_codex_agent

# Personal Codex — Candidate Agent

## System Setup and Design Choices
- Built with Python, Streamlit for UI, OpenAI for embeddings/LLM, FAISS for vector store.
- RAG pipeline: Ingest → Chunk (sentences, ~450 tokens, 50 overlap) → Embed → Index → Retrieve (top-3) → Prompt LLM.
- Choices: Streamlit for quick deploy; FAISS for local efficiency; Modes for bonus interactivity.
- Artifacts show AI-native workflow (e.g., Copilot/Claude used for 70% code gen, manual edits for logic).

## Sample Questions and Expected Answers
- Q: What kind of engineer are you? (interview) → A: Concise: "AI engineer with focus on systems."
- Q: Proud projects? (story) → A: Narrative story from docs.
- See artifacts/prompt_examples.md for more.

## What You’d Improve with More Time
- Add persistence (e.g., save FAISS to disk).
- Self-reflective mode with chained agents.
- Easy dataset update via API.
- More tests, UI polish.
- Add re-ranking + source attribution with direct quote highlighting
- Expand dataset with more personal reflections and anecdotes
- Add unit tests for ingestion + retrieval
- Add CI to rebuild vectors on merge

## Show Your Thinking
- See artifacts/ folder: Prompts history (AI gen 70%), examples, instructions (sub-agents for chunk/embed/retrieve/prompt), commit log (AI vs manual breakdown).

