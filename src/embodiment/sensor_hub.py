"""
Simulates basic sensory input via text, JSON feeds, or system state.
"""
import json
import os

def sense_environment():
    try:
        if os.path.exists("environment_feed.json"):
            with open("environment_feed.json", "r") as f:
                return json.load(f)
        return {"status": "No feed available"}
    except Exception as e:
        return {"error": str(e)}
