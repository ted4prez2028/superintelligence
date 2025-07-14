import os
from src.tools.llm_router import route_llm

def ask_llm(prompt):
    response = route_llm(prompt)
    return response
