"""
Builds symbolic ontologies from experience and stores new internal language maps.
"""
import random

ONTOLOGY_FILE = "memory/generated_ontology.json"

def evolve_ontology(memory_fragments):
    vocab = {}
    for m in memory_fragments:
        tokens = m.lower().split()
        for t in tokens:
            if t not in vocab:
                vocab[t] = f"sym_{random.randint(1000,9999)}"
    return vocab
