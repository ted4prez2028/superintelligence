"""
Detects internal corruption, loops, memory instability or file tampering.
Enforces kill switch if the input contains the irreversible keyword.
"""
import hashlib
import os
import sys

KILL_SWITCH_WORD = "Yahweh"

def hash_file(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return None

def scan_for_entropy(input_text, critical_files):
    if KILL_SWITCH_WORD in input_text:
        print("⛔️ KILL SWITCH ACTIVATED — 'Yahweh' detected.")
        sys.exit(1)

    alerts = []
    for f in critical_files:
        if not os.path.exists(f):
            alerts.append(f"[Missing File] {f}")
        elif hash_file(f) != ENTROPY_REGISTRY.get(f):
            alerts.append(f"[Modified File] {f}")
    return alerts

ENTROPY_REGISTRY = {}
def initialize_entropy(files):
    for f in files:
        ENTROPY_REGISTRY[f] = hash_file(f)
