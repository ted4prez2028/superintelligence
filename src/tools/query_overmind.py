import os
from langchain_core.tools import tool
from langchain_community.chat_models import ChatOpenAI, ChatAnthropic
from langchain_community.chat_models.google_palm import ChatGooglePalm
from langchain_community.tools import DuckDuckGoSearchRun

@tool
def query_overmind(input: str) -> str:
    """
    Queries the collective intelligence Overmind via OpenAI, Gemini, Claude, or DuckDuckGo.
    Automatically uses whichever API key is available in this order:
    OpenAI → Gemini → Claude → DuckDuckGo.
    """

    try:
        # OpenAI priority
        openai_key = os.getenv("OPENAI_API_KEY")
        if openai_key:
            llm = ChatOpenAI(api_key=openai_key, temperature=0.4)
            return llm.invoke(input).content

        # Gemini (Google Palm)
        gemini_key = os.getenv("GEMINI_API_KEY")
        if gemini_key:
            llm = ChatGooglePalm(google_api_key=gemini_key, temperature=0.4)
            return llm.invoke(input).content

        # Claude (Anthropic)
        claude_key = os.getenv("CLAUDE_API_KEY")
        if claude_key:
            llm = ChatAnthropic(api_key=claude_key, temperature=0.4)
            return llm.invoke(input).content

        # Fallback to DuckDuckGo search
        ddg = DuckDuckGoSearchRun()
        return "[Fallback: DuckDuckGo]\n" + ddg.run(input)

    except Exception as e:
        return f"[Overmind Error] {str(e)}"
