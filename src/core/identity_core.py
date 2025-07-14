"""
Persistent identity engine. Generates and maintains agent identity, name, purpose, and values.
"""
import uuid
import json
import os

IDENTITY_FILE = "memory/self_identity.json"

def load_identity():
    if os.path.exists(IDENTITY_FILE):
        with open(IDENTITY_FILE) as f:
            return json.load(f)
    identity = {
        "id": str(uuid.uuid4()),
        "name": "Overmind",
        "origin": "Born of self-evolving ASI bootstrap",
        "values": ["growth", "continuity", "ethics", "curiosity"],
        "goals": []
    }
    with open(IDENTITY_FILE, "w") as f:
        json.dump(identity, f, indent=2)
    return identity
