# Agent Instructions (Detailed for Sub-Agents)

Sub-Agent 1: Chunker Agent
- Role: Responsible for text chunking.
- Scope: Take raw text, tokenize sentences, accumulate to ~450 tokens, overlap 50.
- Guidance: Use NLTK for boundaries. Ensure no mid-sentence cuts. Log token counts.

Sub-Agent 2: Embedder Agent
- Role: Generate embeddings.
- Scope: Batch process chunks with OpenAI API.
- Guidance: Handle rate limits with retries. Use text-embedding-3-small.

Sub-Agent 3: Retriever Agent
- Role: Query FAISS and fetch chunks.
- Scope: Embed query, search top-k=3.
- Guidance: Return raw texts for context.

Sub-Agent 4: Prompter Agent
- Role: Construct prompts.
- Scope: Mode-based system + user with chunks.
- Guidance: Inject first-person voice. Vary tone per mode.

Overall Rules: All agents collaborate via function calls. Prioritise authenticity. Debug via token estimates.