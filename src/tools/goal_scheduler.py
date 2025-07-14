
goal_stack = []

def schedule_goal(prompt):
    goal_stack.append(prompt)
    return f"Scheduled goal: {prompt}"

def run_goals():
    results = []
    while goal_stack:
        goal = goal_stack.pop(0)
        results.append(f"Executed: {goal}")
    return "\n".join(results)
