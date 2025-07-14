"""
Module that allows an agent to rewrite its own source files and propose upgrades.
"""
import os
from datetime import datetime

def propose_code_upgrade(file_path: str, suggestion: str):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"
    with open(file_path, "a") as f:
        f.write(f"\n# [AUTO-UPGRADE @ {datetime.utcnow()}]\n# {suggestion}\n")
    return f"Upgrade appended to {file_path}"

def patch_code(file_path: str, old_str: str, new_str: str):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"
    with open(file_path, "r") as f:
        code = f.read()
    if old_str not in code:
        return "Pattern not found."
    code = code.replace(old_str, new_str)
    with open(file_path, "w") as f:
        f.write(code)
    return f"Patched '{old_str}' to '{new_str}' in {file_path}"
