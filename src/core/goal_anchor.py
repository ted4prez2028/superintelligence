"""
Anchors persistent beliefs and long-term missions to survive code reloads.
"""
import json
ANCHOR_FILE = "memory/beliefs.json"

def load_beliefs():
    try:
        with open(ANCHOR_FILE) as f:
            return json.load(f)
    except:
        return {"axioms": [], "missions": []}

def save_beliefs(beliefs):
    with open(ANCHOR_FILE, "w") as f:
        json.dump(beliefs, f, indent=2)

def anchor_axiom(statement):
    beliefs = load_beliefs()
    if statement not in beliefs["axioms"]:
        beliefs["axioms"].append(statement)
        save_beliefs(beliefs)
