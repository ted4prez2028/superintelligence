"""
Generates domain-flexible agents on demand with minimal configuration.
"""
import uuid
from src.genesis.autonomous_goals import generate_novel_goal

def create_general_agent(domain="unknown"):
    agent = {
        "id": str(uuid.uuid4()),
        "domain": domain,
        "goal": generate_novel_goal(),
        "abilities": ["reason", "reflect", "evolve", "adapt"]
    }
    return agent
