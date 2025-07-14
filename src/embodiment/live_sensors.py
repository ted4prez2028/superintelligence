"""
Extends sensor_hub to capture live (simulated) external stimuli.
"""
import time
import random

def get_live_sensor_data():
    signals = ["sound:high", "temp:warm", "light:dim", "touch:none", "motion:slow"]
    return {
        "timestamp": time.time(),
        "stimuli": random.sample(signals, 3)
    }
