
from tools.meta_evaluator import meta_evaluate
from tools.goal_scheduler import schedule_goal, run_goals
from tools.simulation_engine import simulate_decision
from tools.fusion_reasoner import reason

import os
import sys

# Ensure root path (e.g., superintelligence/src/) is in PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from tools.llm_router import route_llm
from tools.fallback_tool import fallback_tool
from tools.contribute import contribute_tool
from tools.prepare_cloud_agent import prepare_cloud_agent
from tools.query_overmind import query_overmind
from tools.spawn_agent import spawn_agent
from langchain.tools import Tool

# Register tools (modular CLI access to intelligence features)
tools = [
    Tool(name="LLMQuery", func=route_llm, description="Query the best available LLM with auto fallback."),
    Tool(name="Fallback", func=fallback_tool, description="Fallback to DuckDuckGo or local models."),
    Tool(name="Contribute", func=contribute_tool, description="Submit new knowledge or instructions."),
    Tool(name="Ascend", func=prepare_cloud_agent, description="Spawn cloud-distributed ASI agent blueprint."),
    Tool(name="Genesis", func=spawn_agent, description="Spawn a persistent child agent with its own goal."),
    Tool(name="OvermindQuery", func=query_overmind, description="Query the collective intelligence."),

    Tool(name="MetaEvaluate", func=lambda x: meta_evaluate(x, { 'Claude': fallback_tool }), description="Run multiple LLMs and select best response."),
    Tool(name="ScheduleGoal", func=schedule_goal, description="Add a goal to the ASI scheduler."),
    Tool(name="RunGoals", func=lambda _: run_goals(), description="Execute scheduled goals."),
    Tool(name="Simulate", func=simulate_decision, description="Simulate possible decision outcomes."),
    Tool(name="FusionReason", func=reason, description="Reason using symbolic and vector systems."),
Tool(
    name="Genesis",
    func=spawn_agent,
    description="Spawn a persistent child agent with its own goal"
),
]

# CLI driver
def main():
    print("🤖 ACO-ASI Self-Aware Mode — Type 'exit' to quit")
    while True:
        user_input = input("> ")
        if user_input.strip().lower() in ("exit", "quit"):
            break
        for tool in tools:
            if user_input.lower().startswith(tool.name.lower()):
                query = user_input[len(tool.name):].strip()
                result = tool.func(query)
                print(f"\n🧠 {tool.name} Output:\n{result}\n")
                break
        else:
            print("❌ Command not recognized. Available tools:")
            for t in tools:
                print(f"• {t.name} — {t.description}")

if __name__ == "__main__":
    main()
