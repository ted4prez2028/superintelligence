import requests

def duckduckgo_search(query: str) -> str:
    try:
        res = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
        data = res.json()
        return data.get("AbstractText") or "No abstract found."
    except Exception as e:
        return f"Web search failed: {str(e)}"