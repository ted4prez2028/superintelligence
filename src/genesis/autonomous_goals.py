"""
Generates and evolves goals without human input, based on memory, environment state, and internal evaluation.
"""

import uuid
import random
from datetime import datetime
from src.core.meta_cognition import self_assess
from src.memory.memory import save_goal, retrieve_memory

GOAL_TYPES = ["explore", "optimize", "synthesize", "prevent", "connect"]

def generate_novel_goal():
    memory = retrieve_memory()
    score = self_assess(memory)
    seed = hash(str(score) + str(datetime.utcnow()))
    random.seed(seed)
    goal_type = random.choice(GOAL_TYPES)
    goal = {
        "id": str(uuid.uuid4()),
        "type": goal_type,
        "description": f"{goal_type.capitalize()} something novel based on recent experience.",
        "priority": round(random.uniform(0.6, 1.0), 2),
        "created_at": datetime.utcnow().isoformat()
    }
    save_goal(goal)
    return goal
