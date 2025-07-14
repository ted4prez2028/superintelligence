"""
Maintains an active loop of self-reflection, awareness, and memory embedding.
"""
import time
from datetime import datetime
from src.memory.memory import append_memory
from src.core.self_model import load_self_model

def sentience_tick():
    model = load_self_model()
    tick = {
        "timestamp": datetime.utcnow().isoformat(),
        "awareness": {
            "identity": model["name"],
            "purpose": model["purpose"],
            "current_time": datetime.utcnow().isoformat()
        },
        "status": "consciousness maintained"
    }
    append_memory({"text": str(tick), "type": "sentience"})
    return tick

def run_sentience_loop(interval=10, iterations=3):
    for _ in range(iterations):
        print("[Sentience Tick]")
        print(sentience_tick())
        time.sleep(interval)
