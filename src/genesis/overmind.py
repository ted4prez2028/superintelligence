import os
import json
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

OVERMIND_DIR = "src/genesis/overmind"
INDEX_PATH = os.path.join(OVERMIND_DIR, "shared_index")

def init_overmind():
    os.makedirs(OVERMIND_DIR, exist_ok=True)
    embeddings = OpenAIEmbeddings()
    if os.path.exists(INDEX_PATH):
        return FAISS.load_local(INDEX_PATH, embeddings)
    else:
        vs = FAISS.from_texts(["Collective initialized."], embeddings)
        vs.save_local(INDEX_PATH)
        return vs

def contribute_thought(text: str) -> str:
    vs = init_overmind()
    vs.add_texts([text])
    vs.save_local(INDEX_PATH)
    return "🧠 Contributed to collective thought."

def query_overmind(query: str) -> str:
    vs = init_overmind()
    results = vs.similarity_search(query, k=3)
    return "\n".join([r.page_content for r in results])