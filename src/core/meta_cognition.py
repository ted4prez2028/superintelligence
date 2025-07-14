"""
Provides self-reflection and performance evaluation tools.
"""

def self_assess(memory):
    total = len(memory)
    failed = sum(1 for m in memory if m.get("status") == "failed")
    success = total - failed
    if total == 0:
        return {"success_rate": 0.0}
    return {"success_rate": success / total}

def evaluate_last_decision(memory):
    if not memory:
        return "No memory found."
    last = memory[-1]
    if last.get("status") == "failed":
        return f"Last decision failed: {last.get('reason', 'unknown')}."
    return "Last decision succeeded."
