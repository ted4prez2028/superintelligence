from langchain.llms import OpenAI

llm = OpenAI()

def detect_emotion(text: str) -> str:
    prompt = f"What emotional tone is expressed in the following text?\n\n{text}\n\nReturn only the tone (e.g., joyful, sad, analytical, angry, hopeful)."
    return llm(prompt)