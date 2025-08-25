import docx
import PyPDF2
from sentence_transformers import SentenceTransformer  # Wait, no: use OpenAI embeddings
from openai import OpenAI
import faiss
import numpy as np
import nltk
from utils import get_openai_client, chunk_text

nltk.download('punkt', quiet=True)

# Reasoning: ingest.py handles document parsing, chunking, embedding, and FAISS 
# index building. This modularises the RAG pipeline. We parse different file types: 
# PyPDF2 for PDFs, docx for Word, plain read for txt. Chunking uses NLTK for sentences,
#  targeting ~450 tokens with overlap. Embeddings are generated in batches for efficiency.
#  FAISS uses flat index for simplicity and small scale.

client = get_openai_client()

def ingest_documents(uploaded_files):
    texts = []
    for file in uploaded_files:
        if file.name.endswith('.pdf'):
            reader = PyPDF2.PdfReader(file)
            text = ''.join([page.extract_text() for page in reader.pages])
        elif file.name.endswith('.docx'):
            doc = docx.Document(file)
            text = '\n'.join([para.text for para in doc.paragraphs])
        elif file.name.endswith('.txt'):
            text = file.read().decode('utf-8')
        else:
            continue
        chunks = chunk_text(text, chunk_size=450, overlap=50)
        texts.extend(chunks)
    return texts

def build_faiss_index(texts):
    # Generate embeddings
    embeddings = []
    for text in texts:
        response = client.embeddings.create(input=text, model="text-embedding-3-small")
        embeddings.append(response.data[0].embedding)
    embeddings = np.array(embeddings).astype('float32')
    
    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return {'index': index, 'texts': texts}  # Store texts for retrieval

def retrieve_chunks(query, vectorstore, k=3):
    query_emb = client.embeddings.create(input=query, model="text-embedding-3-small").data[0].embedding
    query_emb = np.array([query_emb]).astype('float32')
    _, indices = vectorstore['index'].search(query_emb, k)
    return [vectorstore['texts'][i] for i in indices[0]]