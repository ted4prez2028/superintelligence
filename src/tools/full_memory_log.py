import os
from src.memory.vector_memory import save_to_memory

LOG_PATH = "logs/session_log.txt"

def log_interaction(text: str) -> str:
    with open(LOG_PATH, "a") as log:
        log.write(text + "\n")
    save_to_memory(text)
    return "Interaction logged and indexed."