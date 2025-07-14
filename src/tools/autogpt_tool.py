from src.planning.auto_loop import autonomous_loop

def autogpt_agent(text: str) -> str:
    return autonomous_loop(text)