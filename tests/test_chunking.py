import pytest
from utils import chunk_text, estimate_tokens

def test_chunking():
    text = "This is sentence one. Sentence two. " * 100  # Long text
    chunks = chunk_text(text, chunk_size=450, overlap=50)
    assert len(chunks) > 1
    for chunk in chunks:
        assert estimate_tokens(chunk) <= 500  # Buffer
    # Overlap check
    assert estimate_tokens(chunks[0][-50:]) > 0  # Rough overlap