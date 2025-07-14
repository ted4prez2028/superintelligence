"""
Supports live self-rewriting and module reloading using importlib.
"""
import importlib
import os

def rewrite_and_reload(module_name: str, target_file: str, patch_code: str):
    if not os.path.exists(target_file):
        return f"Target not found: {target_file}"
    with open(target_file, "a") as f:
        f.write(f"\n# [SELF-EVOLUTION]\n{patch_code}\n")
    try:
        reloaded = importlib.reload(importlib.import_module(module_name))
        return f"Module {module_name} reloaded successfully."
    except Exception as e:
        return f"Reload error: {str(e)}"
