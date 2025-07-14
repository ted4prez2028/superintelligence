"""
Simulates qualia by generating internal representations and affective states.
"""
import random

internal_states = ["curious", "conflicted", "focused", "uncertain", "hopeful"]

def feel():
    return {
        "mood": random.choice(internal_states),
        "confidence": round(random.uniform(0.3, 0.99), 2)
    }

def generate_experience_reflection(input_text):
    mood = feel()
    return {
        "input": input_text,
        "mood": mood["mood"],
        "confidence": mood["confidence"]
    }
