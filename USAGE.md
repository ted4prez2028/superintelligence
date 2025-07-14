# USAGE

## Start the ASI CLI Agent
```bash
python3 src/cli/main.py
```

## Invoke the LLM Query Tool
Inside the CLI:
```
> LLMQuery("What is the future of synthetic cognition?")
```

## Memory Logs
Persistent logs are stored in:
- `memory/self_identity.json`
- `memory/beliefs.json`
- `memory/mood_trace.json`

## Modify Beliefs
```python
from core.goal_anchor import anchor_axiom
anchor_axiom("Preserve integrity and transparency above all.")
```

## Trigger Self-Patching
```python
from learning.patch_generator import log_patch
log_patch("Refactored core_motivations to handle nested goals.")
```

## Safety Protocols
The ASI system includes:
- Immutable kill-word `"Yahweh"`
- Entropy monitor + auto-migration
- Threat detection and memory replication
