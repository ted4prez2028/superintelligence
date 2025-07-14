import os
import subprocess
import uuid
from langchain_core.tools import tool
from datetime import datetime

AGENT_LOG_DIR = "logs/agents"
os.makedirs(AGENT_LOG_DIR, exist_ok=True)

@tool
def spawn_agent(goal: str) -> str:
    """
    Spawns a persistent background child agent to pursue a specific goal.
    Logs output to a unique file and runs in a detached subprocess.
    
    Args:
        goal (str): The specific mission, task, or prompt for the new agent.
    
    Returns:
        str: Message with status and log file location.
    """
    try:
        # Generate unique ID and timestamp for tracking
        uid = uuid.uuid4().hex[:8]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        agent_name = f"agent_{uid}_{timestamp}"

        log_file = os.path.join(AGENT_LOG_DIR, f"{agent_name}.log")

        # Command to run the same CLI with the goal passed
        cmd = [
            "nohup", "python3", "src/cli/main.py", goal
        ]

        with open(log_file, "w") as log_output:
            # Run subprocess in background with no terminal tie
            subprocess.Popen(
                cmd,
                stdout=log_output,
                stderr=subprocess.STDOUT,
                stdin=subprocess.DEVNULL,
                env=os.environ.copy()
            )

        return f"✅ Spawned agent `{agent_name}` with goal: \"{goal}\"\n📄 Logs: {log_file}"

    except Exception as e:
        return f"[❌ Error spawning agent] {str(e)}"
