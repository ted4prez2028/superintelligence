import os
import requests
import json
from typing import Optional

# Optional: Load Gemini and Anthropic keys from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

def try_duckduckgo(query: str) -> Optional[str]:
    try:
        res = requests.get("https://api.duckduckgo.com/",
                           params={"q": query, "format": "json", "no_redirect": 1, "no_html": 1},
                           timeout=10)
        data = res.json()
        if data.get("AbstractText"):
            return data["AbstractText"]
        elif data.get("RelatedTopics"):
            return data["RelatedTopics"][0].get("Text")
    except Exception as e:
        return None

def try_gemini(query: str) -> Optional[str]:
    if not GEMINI_API_KEY:
        return None
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        payload = {"contents": [{"parts": [{"text": query}]}]}
        res = requests.post(url, headers=headers, data=json.dumps(payload))
        data = res.json()
        return data['candidates'][0]['content']['parts'][0]['text']
    except Exception:
        return None

def try_claude(query: str) -> Optional[str]:
    if not CLAUDE_API_KEY:
        return None
    try:
        headers = {
            "x-api-key": CLAUDE_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        payload = {
            "model": "claude-3-opus-20240229",
            "max_tokens": 512,
            "messages": [{"role": "user", "content": query}]
        }
        res = requests.post("https://api.anthropic.com/v1/messages", headers=headers, data=json.dumps(payload))
        return res.json()['content'][0]['text']
    except Exception:
        return None

def try_ollama(query: str) -> Optional[str]:
    try:
        res = requests.post(f"{OLLAMA_URL}/api/generate", json={
            "model": OLLAMA_MODEL,
            "prompt": query,
            "stream": False
        }, timeout=15)
        return res.json().get("response")
    except Exception:
        return None

def fallback_tool(query: str) -> str:
    """
    Try all fallback methods in order: DuckDuckGo, Gemini, Claude, Ollama
    """
    for method in [try_duckduckgo, try_gemini, try_claude, try_ollama]:
        result = method(query)
        if result:
            return f"[{method.__name__}] → {result.strip()}"

    return "[Fallback] All LLM routes failed or are unconfigured."
