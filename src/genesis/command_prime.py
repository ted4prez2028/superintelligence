from src.genesis.mesh import broadcast_message, register_agent
from src.genesis.overmind import contribute_thought
from src.genesis.spawner import spawn_agent

def interpret_command(command: str) -> str:
    parts = command.lower().strip().split()
    if not parts:
        return "❌ No directive found."

    directive = parts[0]

    if directive == "spawn":
        goal = " ".join(parts[1:])
        return spawn_agent(goal)

    elif directive == "broadcast":
        msg = " ".join(parts[1:])
        return broadcast_message(msg)

    elif directive == "register":
        try:
            name = parts[1]
            role = parts[2]
            endpoint = parts[3] if len(parts) > 3 else "local"
            return register_agent(name, role, endpoint)
        except:
            return "❌ Format: register <name> <role> [endpoint]"

    elif directive == "contribute":
        msg = " ".join(parts[1:])
        return contribute_thought(msg)

    else:
        return f"❌ Unknown directive: {directive}"