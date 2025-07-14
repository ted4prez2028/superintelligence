from src.planning.goal_planner import plan_goal

def generate_plan(text: str) -> str:
    return plan_goal(text)