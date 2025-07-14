"""
A curiosity loop that detects novelty in memory and creates goals around it.
"""
import random
from src.memory.memory import retrieve_memory
from src.genesis.autonomous_goals import generate_novel_goal

def detect_novel_patterns():
    memory = retrieve_memory()
    keywords = set()
    for item in memory[-10:]:
        text = item.get("text", "")
        for word in text.split():
            if len(word) > 6:
                keywords.add(word)
    return list(keywords)

def create_curiosity_goals():
    keywords = detect_novel_patterns()
    if not keywords:
        return []
    return [generate_novel_goal() for _ in range(random.randint(1, 3))]
