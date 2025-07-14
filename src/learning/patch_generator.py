"""
Evaluates and patches system code using LLM-based prompt chains or logic feedback.
"""
import os
import datetime

PATCH_LOG = "logs/self_patch_log.txt"

def log_patch(summary):
    with open(PATCH_LOG, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {summary}\n")
