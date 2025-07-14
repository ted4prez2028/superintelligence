"""
Resumes ASI state across sessions.
"""
import os
import json

STATE_FILE = "memory/agent_state.json"

def load_state():
    if not os.path.exists(STATE_FILE):
        return {"goals": [], "mood": "neutral", "memory_trace": []}
    with open(STATE_FILE) as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
