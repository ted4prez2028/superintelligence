# src/tools/query.py

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
import os

PERSIST_PATH = "memory/collective_index"

embeddings = OpenAIEmbeddings()

# Load or create the FAISS vector store
def get_vector_store():
    if os.path.exists(PERSIST_PATH):
        return FAISS.load_local(PERSIST_PATH, embeddings, allow_dangerous_deserialization=True)
    else:
        return FAISS.from_documents([], embeddings)

# Prompt template for LLM reasoning over search results
response_prompt = PromptTemplate.from_template("""
You are an advanced ASI agent accessing the collective memory.

Query: "{query}"

Relevant thoughts:
{context}

Based on this, answer the query or explain why it's not answerable yet.
""")

# Main function for querying overmind
def query_overmind(query: str) -> str:
    """
    Searches the collective memory (FAISS) for similar thoughts and generates a response.

    Args:
        query (str): The input query.

    Returns:
        str: AI response based on retrieved memory.
    """
    if not query.strip():
        return "No input provided."

    store = get_vector_store()
    retriever = store.as_retriever(search_type="similarity", k=5)

    docs = retriever.invoke(query)
    context = "\n---\n".join([d.page_content for d in docs])

    llm = OpenAI(temperature=0.3)
    chain = response_prompt | llm | StrOutputParser()

    return chain.invoke({"query": query.strip(), "context": context})
