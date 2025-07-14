"""
Agent evaluates and modifies its policy based on outcome feedback.
"""
from src.core.persistence_engine import add_experience

def feedback_loop(action: str, result: str):
    reflection = {
        "action": action,
        "result": result,
        "reinforcement": "positive" if "success" in result else "negative"
    }
    add_experience(reflection)
    return reflection
