from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import os

def contribute_tool(text: str, vectorstore_path="vectorstore_index") -> str:
    # Use HuggingFace for embeddings to avoid OpenAI dependency
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Load or create FAISS vectorstore
    if os.path.exists(vectorstore_path):
        vectorstore = FAISS.load_local(vectorstore_path, embeddings)
    else:
        vectorstore = FAISS.from_documents([], embeddings)

    # Wrap text in Document and add to vectorstore
    new_doc = Document(page_content=text)
    vectorstore.add_documents([new_doc])
    
    # Persist index
    vectorstore.save_local(vectorstore_path)

    return f"✅ Contributed {len(text.split())} words to knowledge index."
