"""
Allows agents to interface with real-world APIs, simulated environments, or local actions.
"""

import requests
import json
import subprocess

def trigger_webhook(url, payload):
    try:
        response = requests.post(url, json=payload)
        return response.text
    except Exception as e:
        return f"[Webhook Error] {str(e)}"

def execute_local_command(command):
    try:
        result = subprocess.check_output(command, shell=True)
        return result.decode()
    except Exception as e:
        return f"[Command Error] {str(e)}"
