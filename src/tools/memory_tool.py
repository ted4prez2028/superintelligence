from src.memory.vector_memory import save_to_memory, search_memory

def remember(text: str) -> str:
    save_to_memory(text)
    return "Stored in memory."

def recall(text: str) -> str:
    return search_memory(text)