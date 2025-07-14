"""
Generates new abstract concepts from memory + observations.
"""
import random

def invent_concepts(memory_trace):
    new_concepts = []
    for m in memory_trace[-10:]:
        concept = f"meta:{hash(m) % 10000}"
        new_concepts.append(concept)
    return list(set(new_concepts))
