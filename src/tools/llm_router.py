import os
from langchain_community.llms import Ollama
from duckduckgo_search import DDGS

def try_openai(prompt):
    from langchain_openai import OpenAI
    return OpenAI(temperature=0.7)(prompt)

def try_gemini(prompt):
    from google.generativeai import configure, GenerativeModel
    configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = GenerativeModel("gemini-pro")
    return model.generate_content(prompt).text

def try_claude(prompt):
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    return client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}]
    ).content[0].text

def try_ollama(prompt):
    return Ollama(model="llama3")(prompt)

def try_duckduckgo(prompt):
    with DDGS() as ddgs:
        results = list(ddgs.text(prompt, max_results=1))
        return results[0]["body"] if results else "No DuckDuckGo results."

def route_llm(prompt):
    try:
        if os.getenv("OPENAI_API_KEY"):
            return try_openai(prompt)
    except Exception:
        pass

    try:
        if os.getenv("GOOGLE_API_KEY"):
            return try_gemini(prompt)
    except Exception:
        pass

    try:
        if os.getenv("ANTHROPIC_API_KEY"):
            return try_claude(prompt)
    except Exception:
        pass

    try:
        return try_ollama(prompt)
    except Exception:
        pass

    return try_duckduckgo(prompt)
