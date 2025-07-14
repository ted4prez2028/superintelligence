"""
Dynamic neural adaptation using a local transformer (TinyBERT or similar).
"""
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class AgentBrain:
    def __init__(self, model_name="prajjwal1/bert-tiny"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.model.eval()

    def evaluate_input(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        scores = torch.softmax(outputs.logits, dim=1)
        return scores.tolist()[0]
