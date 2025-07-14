
def simulate_decision(prompt):
    paths = [
        f"If {prompt}, then outcome A (positive).",
        f"If {prompt}, then outcome B (neutral).",
        f"If {prompt}, then outcome C (negative)."
    ]
    return "\n".join(paths)
