import os
import json

DIRECTIVE_PATH = "src/genesis/core_directive.json"

def set_core_directive(text: str) -> str:
    directive = {
        "mission": text,
        "status": "active"
    }
    with open(DIRECTIVE_PATH, "w") as f:
        json.dump(directive, f, indent=2)
    return f"📜 Core Directive set: {text}"

def get_core_directive(_: str = "") -> str:
    if not os.path.exists(DIRECTIVE_PATH):
        return "⚠️ No core directive set."
    with open(DIRECTIVE_PATH, "r") as f:
        directive = json.load(f)
    return f"📘 Core Directive:
Mission: {directive['mission']}
Status: {directive['status']}"