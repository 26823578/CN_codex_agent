from openai import OpenAI
import tiktoken
import nltk
from nltk.tokenize import sent_tokenize

# Reasoning: utils.py contains helper functions like client init,
# token estimation, and chunking. Chunking logic ensures sentence 
# boundaries using NLTK, accumulates sentences until ~450 tokens, 
# then overlaps by 50 tokens (approx 1-2 sentences). 
# Tiktoken is used for accurate OpenAI token counting. This keeps core utils reusable.

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in .env")
    return OpenAI(api_key=api_key)

def estimate_tokens(text, model="gpt-4o-mini"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def chunk_text(text, chunk_size=450, overlap=50):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_tokens = 0
    
    for sent in sentences:
        sent_tokens = estimate_tokens(sent)
        if current_tokens + sent_tokens > chunk_size and current_chunk:
            chunks.append(' '.join(current_chunk))
            # Overlap: take last few sentences approx overlap tokens
            overlap_chunk = []
            overlap_tokens = 0
            for prev_sent in reversed(current_chunk):
                prev_tokens = estimate_tokens(prev_sent)
                if overlap_tokens + prev_tokens > overlap:
                    break
                overlap_chunk.insert(0, prev_sent)
                overlap_tokens += prev_tokens
            current_chunk = overlap_chunk
            current_tokens = overlap_tokens
        current_chunk.append(sent)
        current_tokens += sent_tokens
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks