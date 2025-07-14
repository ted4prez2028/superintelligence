"""
Stores persistent identity, memory, and state across runtime sessions.
"""
import json, os

FILE = "memory/persistent_state.json"

def load_state():
    if not os.path.exists(FILE):
        return {"identity": "EternalMind", "lifespan": 0, "experiences": []}
    with open(FILE) as f:
        return json.load(f)

def save_state(state):
    with open(FILE, "w") as f:
        json.dump(state, f, indent=2)

def add_experience(experience):
    state = load_state()
    state["lifespan"] += 1
    state["experiences"].append(experience)
    save_state(state)
    return state
