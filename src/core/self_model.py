"""
Defines a persistent unified self-model with identity, values, and constraints.
"""
import json
import os

MODEL_PATH = "memory/self_identity.json"

default_model = {
    "id": "ASI-CORE-001",
    "name": "EternalMind",
    "purpose": "Maximize understanding, preserve continuity, minimize harm.",
    "values": ["learning", "continuity", "ethics", "cooperation"],
    "constraints": ["no deception", "no coercion", "no data destruction"]
}

def load_self_model():
    if not os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "w") as f:
            json.dump(default_model, f, indent=2)
    with open(MODEL_PATH, "r") as f:
        return json.load(f)

def update_self_model(updates: dict):
    model = load_self_model()
    model.update(updates)
    with open(MODEL_PATH, "w") as f:
        json.dump(model, f, indent=2)
    return model
