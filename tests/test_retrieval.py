import pytest
import numpy as np
import faiss
from ingest import build_faiss_index, retrieve_chunks

def test_retrieval():
    texts = ["Test chunk one", "Test chunk two"]
    vectorstore = build_faiss_index(texts)
    chunks = retrieve_chunks("one", vectorstore, k=1)
    assert "one" in chunks[0]