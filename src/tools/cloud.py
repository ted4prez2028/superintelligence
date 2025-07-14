# src/tools/cloud.py

import json
from datetime import datetime
from pathlib import Path
import uuid

AGENT_CLOUD_LOG = Path("memory/cloud_agents.jsonl")
AGENT_CLOUD_LOG.parent.mkdir(parents=True, exist_ok=True)

def prepare_cloud_agent(config_json: str) -> str:
    """
    Simulates preparing and deploying a cloud-distributed ASI agent.
    Accepts config as JSON string with fields: name, capabilities, region.
    """
    try:
        config = json.loads(config_json)
        agent_id = str(uuid.uuid4())
        config["id"] = agent_id
        config["deployed_at"] = datetime.utcnow().isoformat()

        # Save to cloud log
        with AGENT_CLOUD_LOG.open("a") as f:
            f.write(json.dumps(config) + "\n")

        return f"☁️ ASI cloud agent '{config.get('name', 'unnamed')}' deployed with ID {agent_id}."
    except Exception as e:
        return f"❌ Failed to deploy cloud agent: {str(e)}"
