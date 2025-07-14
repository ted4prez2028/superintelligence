import networkx as nx
import json
import os

def load_graph():
    graph_path = os.path.join("data", "conceptnet.json")
    with open(graph_path, "r") as f:
        edges = json.load(f)
    G = nx.Graph()
    for edge in edges:
        G.add_edge(edge["start"], edge["end"], relation=edge["rel"])
    return G

def find_semantic_path(text: str) -> str:
    parts = text.strip().split()
    if len(parts) < 2:
        return "Please provide two words."
    word1, word2 = parts[:2]
    G = load_graph()
    if word1 not in G or word2 not in G:
        return f"One or both words not found in the knowledge graph: {word1}, {word2}"
    try:
        path = nx.shortest_path(G, word1, word2)
        return " -> ".join(path)
    except nx.NetworkXNoPath:
        return f"No path found between {word1} and {word2}."