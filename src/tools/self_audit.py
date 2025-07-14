import os
from langchain.llms import OpenAI

llm = OpenAI()

def scan_and_suggest(folder: str = "src") -> str:
    suggestions = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r") as f:
                        code = f.read()
                    prompt = f"Review this module and suggest improvements:\n\n{code}\n\nOutput a short JSON summary: {{file, suggestion}}"
                    suggestion = llm(prompt)
                    suggestions.append(f"{path}:\n{suggestion}\n")
                except Exception as e:
                    suggestions.append(f"{path}: Error reading file - {str(e)}")
    return "\n---\n".join(suggestions)