import os
import json
from src.tools.self_audit import scan_and_suggest
from src.tools.self_evolve import rewrite_module
from src.genesis.overmind import contribute_thought

WATCHED_PATHS = ["src/tools", "src/planning", "src/memory"]

def meta_optimize():
    logs = []
    for folder in WATCHED_PATHS:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".py"):
                    module_path = os.path.join(root, file)
                    relative_path = os.path.relpath(module_path, "src")
                    suggestion = scan_and_suggest(folder)
                    logs.append(f"📡 Auditing {relative_path}...")
                    logs.append(suggestion)
                    improvement_result = rewrite_module(f"{relative_path} Improve performance and modularity")
                    logs.append(improvement_result)
                    contribute_thought(f"Upgraded {relative_path}")
    return "\n".join(logs)