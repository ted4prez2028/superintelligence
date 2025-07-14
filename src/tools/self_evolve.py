import os
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.3)

def rewrite_module(command: str) -> str:
    try:
        module_path = command.split()[0]
        instruction = " ".join(command.split()[1:])
        full_path = os.path.join("src", module_path)
        if not os.path.isfile(full_path):
            return f"File not found: {full_path}"
        with open(full_path, "r") as f:
            original = f.read()
        prompt = f"Here is a Python module:\n{original}\n\nRewrite or improve it based on: {instruction}"
        improvement = llm(prompt)
        with open(full_path, "w") as f:
            f.write(improvement)
        return f"✅ Updated {module_path} successfully."
    except Exception as e:
        return f"❌ Self-rewrite failed: {str(e)}"