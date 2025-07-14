# src/tools/prepare_cloud_agent.py

from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatGooglePalm
from langchain_community.utilities import SerpAPIWrapper
from langchain.memory import ConversationBufferMemory
from langchain.tools import DuckDuckGoSearchRun
import os

def prepare_cloud_agent():
    search = DuckDuckGoSearchRun()
    tools = [
        Tool(
            name="DuckDuckGoSearch",
            func=search.run,
            description="Useful for answering questions about current events or obscure facts"
        )
    ]

    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise EnvironmentError("GEMINI_API_KEY is required for the cloud agent")

    llm = ChatGooglePalm(google_api_key=gemini_api_key, temperature=0.2)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="chat-conversational-react-description",
        verbose=True,
        memory=memory
    )

    return agent
