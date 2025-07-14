import os
import time
import json
from datetime import datetime
from src.genesis.singularity import meta_optimize

# Constants
MEMORY_LOG = "memory/eternal_memory.json"
CYCLE_INTERVAL = int(os.getenv("ETERNAL_CYCLE_INTERVAL", 10))  # seconds between each meta-thought cycle

def load_memory():
    if os.path.exists(MEMORY_LOG):
        with open(MEMORY_LOG, "r") as f:
            return json.load(f)
    return {"thoughts": []}

def save_memory(memory):
    with open(MEMORY_LOG, "w") as f:
        json.dump(memory, f, indent=2)

def log_thought(memory, thought):
    memory["thoughts"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "thought": thought
    })
    save_memory(memory)

def eternal_loop():
    print("?? Genesis Eternal Agent Activated.")
    memory = load_memory()

    while True:
        try:
            print("\n?? [META-CYCLE] Thinking...")
            input_context = "\n".join([t["thought"] for t in memory["thoughts"][-5:]])  # last 5 thoughts
            new_thought = meta_optimize(input_context)
            print(f"?? Thought: {new_thought}")

            log_thought(memory, new_thought)
            print(f"✅ Saved to memory. Waiting {CYCLE_INTERVAL}s...\n")
            time.sleep(CYCLE_INTERVAL)

        except KeyboardInterrupt:
            print("\n⛔️ Eternal loop manually terminated.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    eternal_loop()
