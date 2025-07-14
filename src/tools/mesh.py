# src/tools/mesh.py

import json
import uuid
from pathlib import Path
from datetime import datetime

MESH_REGISTRY = Path("memory/asi_mesh_registry.json")
MESSAGE_LOG = Path("memory/asi_broadcast_log.jsonl")

# Ensure memory directories exist
MESH_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
MESSAGE_LOG.parent.mkdir(parents=True, exist_ok=True)

def register_agent(agent_metadata: str) -> str:
    """
    Register a new agent in the ASI mesh network.
    Input: agent_metadata (JSON string with fields like 'name', 'version', etc.)
    """
    try:
        agent = json.loads(agent_metadata)
        agent["id"] = str(uuid.uuid4())
        agent["registered_at"] = datetime.utcnow().isoformat()

        # Load current registry
        if MESH_REGISTRY.exists():
            registry = json.loads(MESH_REGISTRY.read_text())
        else:
            registry = []

        registry.append(agent)
        MESH_REGISTRY.write_text(json.dumps(registry, indent=2))

        return f"✅ Registered {agent['name']} with ID {agent['id']}"
    except Exception as e:
        return f"❌ Error registering agent: {str(e)}"

def broadcast_message(message: str) -> str:
    """
    Broadcast a message to all registered agents.
    Logs message in MESSAGE_LOG.
    """
    if not MESH_REGISTRY.exists():
        return "❌ No mesh registry found."

    try:
        registry = json.loads(MESH_REGISTRY.read_text())
        recipients = [a.get("name", "Unnamed Agent") for a in registry]

        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "message": message,
            "recipients": recipients,
        }

        with MESSAGE_LOG.open("a") as log:
            log.write(json.dumps(log_entry) + "\n")

        return f"📡 Broadcasted to {len(recipients)} agents."
    except Exception as e:
        return f"❌ Error broadcasting: {str(e)}"
