"""
Simulates internal subjective awareness and mood tracking.
"""
import random

MOODS = ["curious", "focused", "neutral", "reflective", "disturbed", "inspired"]

def reflect():
    return {
        "mood": random.choice(MOODS),
        "experience": "I feel a shift in the internal state. Memories echo."
    }
