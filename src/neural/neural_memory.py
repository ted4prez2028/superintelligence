"""
Simulates sparse distributed memory using concept-to-concept reinforcement.
"""
from collections import defaultdict

memory_graph = defaultdict(lambda: defaultdict(int))

def reinforce_concept_link(a: str, b: str):
    memory_graph[a][b] += 1
    memory_graph[b][a] += 1

def retrieve_associations(concept: str, top=5):
    links = memory_graph[concept]
    return sorted(links.items(), key=lambda x: -x[1])[:top]
