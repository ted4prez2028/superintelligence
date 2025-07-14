"""
Implements recursive abstraction and transfer of knowledge across tasks/domains.
"""
import re

def extract_concepts(text):
    words = re.findall(r"\b\w{6,}\b", text.lower())
    return list(set(words))

def cross_domain_transfer(concepts, domain_b):
    return [f"In {domain_b}, '{c}' might mean: {c[::-1]}" for c in concepts]

def recursive_abstract_learning(memory, domain_b="biology"):
    results = []
    for entry in memory[-5:]:
        text = entry.get("text", "")
        concepts = extract_concepts(text)
        transferred = cross_domain_transfer(concepts, domain_b)
        results.extend(transferred)
    return results
