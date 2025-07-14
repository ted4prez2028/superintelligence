# src/tools/genesis.py

import json
from pathlib import Path
from datetime import datetime
import uuid

AGENT_SPAWN_LOG = Path("memory/genesis_agents.jsonl")
AGENT_SPAWN_LOG.parent.mkdir(parents=True, exist_ok=True)

def spawn_agent(agent_config_json: str) -> str:
    """
    Spawns a new ASI agent with a given configuration.
    Configuration is a JSON string with fields: name, purpose, traits.
    """
    try:
        agent = json.loads(agent_config_json)
        agent_id = str(uuid.uuid4())
        agent["id"] = agent_id
        agent["spawned_at"] = datetime.utcnow().isoformat()

        # Save to agent spawn log
        with AGENT_SPAWN_LOG.open("a") as f:
            f.write(json.dumps(agent) + "\n")

        return f"🌱 Genesis: Agent '{agent.get('name', 'Unnamed')}' spawned with ID {agent_id}."
    except Exception as e:
        return f"❌ Failed to spawn agent: {str(e)}"
