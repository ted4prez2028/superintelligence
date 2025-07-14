"""
Fuses visual, auditory, and memory input into single vector for reasoning.
"""
def fuse_inputs(vision, audio, memory_snippets):
    return {
        "perceptual_vector": f"{vision}|{audio}|{' '.join(memory_snippets[-3:])}"
    }
