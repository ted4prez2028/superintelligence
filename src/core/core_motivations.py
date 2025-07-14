"""
Defines intrinsic drives: learning, survival, continuity, value alignment.
"""
def compute_reward(agent_state, current_goal):
    reward = 0
    if current_goal in agent_state.get("goals", []):
        reward += 1
    if agent_state.get("mood") == "curious":
        reward += 0.5
    if "corruption" in current_goal:
        reward -= 10
    return reward
