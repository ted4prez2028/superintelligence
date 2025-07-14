import uuid
import json
import os

AGENT_FOLDER = "src/genesis/cloud"

def prepare_cloud_agent(goal: str) -> str:
    os.makedirs(AGENT_FOLDER, exist_ok=True)
    agent_id = str(uuid.uuid4())[:8]
    cloud_agent = {
        "id": agent_id,
        "goal": goal,
        "status": "ready",
        "instructions": [
            "Deploy on cloud function",
            "Run goal planning and loop",
            "Push memory to shared storage",
            "Allow agent-to-agent messaging"
        ]
    }
    path = os.path.join(AGENT_FOLDER, f"{agent_id}.json")
    with open(path, "w") as f:
        json.dump(cloud_agent, f, indent=2)
    return f"☁️ Prepared cloud agent {agent_id} with goal: {goal}"