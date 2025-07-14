from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

vector_store = None

def initialize_memory():
    global vector_store
    embeddings = OpenAIEmbeddings()
    if os.path.exists("data/faiss_index"):
        vector_store = FAISS.load_local("data/faiss_index", embeddings)
    else:
        vector_store = FAISS.from_texts(["Initial memory seed."], embeddings)
        vector_store.save_local("data/faiss_index")

def save_to_memory(text: str):
    global vector_store
    if not vector_store:
        initialize_memory()
    vector_store.add_texts([text])
    vector_store.save_local("data/faiss_index")

def search_memory(query: str) -> str:
    global vector_store
    if not vector_store:
        initialize_memory()
    results = vector_store.similarity_search(query, k=2)
    return "\n".join([r.page_content for r in results])