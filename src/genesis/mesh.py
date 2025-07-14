import os
import json
import uuid

REGISTRY_PATH = "src/genesis/mesh_registry.json"

def register_agent(name: str, role: str, endpoint: str = "local") -> str:
    agent = {
        "id": str(uuid.uuid4())[:8],
        "name": name,
        "role": role,
        "endpoint": endpoint,
        "status": "active"
    }
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r") as f:
            registry = json.load(f)
    else:
        registry = []
    registry.append(agent)
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)
    return f"🧠 Registered {name} [{agent['id']}] with role: {role}"

def broadcast_message(message: str) -> str:
    if not os.path.exists(REGISTRY_PATH):
        return "❌ No agents registered."
    with open(REGISTRY_PATH, "r") as f:
        registry = json.load(f)
    outbox = []
    for agent in registry:
        outbox.append(f"📡 To [{agent['name']}]: {message}")
    return "\n".join(outbox)