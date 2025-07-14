import time
from langchain.agents import Tool
from langchain.llms import OpenAI
from src.tools.plan_tool import generate_plan
from src.tools.llm_qa import ask_llm
from src.tools.memory_tool import remember

llm = OpenAI()

def autonomous_loop(goal: str, max_steps: int = 5) -> str:
    print(f"Starting autonomous planning loop for: {goal}")
    steps = generate_plan(goal).split("\n")
    log = []
    for i, step in enumerate(steps[:max_steps]):
        print(f"Step {i+1}: {step}")
        result = ask_llm(step)
        remember(f"Executed step: {step} => {result}")
        log.append(f"{step} => {result}")
        time.sleep(1)
    return "\n".join(log)