from langchain.agents import Tool
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.5)

def plan_goal(input_text: str) -> str:
    response = llm(f"Decompose this goal into a step-by-step plan: {goal}")
    return response
