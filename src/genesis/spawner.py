import os
import uuid
import subprocess

AGENT_FOLDER = "src/genesis/agents"

def spawn_agent(goal: str) -> str:
    os.makedirs(AGENT_FOLDER, exist_ok=True)
    agent_id = str(uuid.uuid4())[:8]
    script_path = os.path.join(AGENT_FOLDER, f"{agent_id}.py")

    agent_script = f"""import time
from src.tools.plan_tool import generate_plan
from src.tools.llm_qa import ask_llm
from src.memory.vector_memory import save_to_memory

print("🧬 Spawned Agent {agent_id} for goal: {goal}")
plan = generate_plan("{goal}")
steps = plan.split("\\n")
for step in steps:
    print("🧠 Step:", step)
    result = ask_llm(step)
    save_to_memory(f"[{agent_id}] {step} => {result}")
    time.sleep(1)
print("✅ Agent {agent_id} completed.")"""

    with open(script_path, "w") as f:
        f.write(agent_script)

    subprocess.Popen(["python", script_path])
    return f"Spawned agent {agent_id} with goal: {goal}"