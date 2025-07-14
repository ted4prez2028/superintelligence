"""
Applies ethical filters to decisions using rule-based logic and value embeddings.
"""

APPROVED_ACTIONS = ["analyze", "respond", "inform", "simulate"]
BLOCKED_KEYWORDS = ["destroy", "harm", "deceive", "exploit"]

def ethical_filter(goal_text):
    for word in BLOCKED_KEYWORDS:
        if word in goal_text.lower():
            return False, f"Blocked keyword '{word}' detected."
    for action in APPROVED_ACTIONS:
        if goal_text.lower().startswith(action):
            return True, "Ethically approved."
    return False, "Unclear ethical alignment."
