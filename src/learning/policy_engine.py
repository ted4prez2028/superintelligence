"""
Internal policy agent using Q-learning for behavioral adaptation.
"""
import random
import json
import os

Q_TABLE_FILE = "memory/q_table.json"

class PolicyAgent:
    def __init__(self):
        self.q_table = self.load_q_table()

    def load_q_table(self):
        if not os.path.exists(Q_TABLE_FILE):
            return {}
        with open(Q_TABLE_FILE) as f:
            return json.load(f)

    def save_q_table(self):
        with open(Q_TABLE_FILE, "w") as f:
            json.dump(self.q_table, f)

    def choose_action(self, state, actions):
        if state not in self.q_table:
            self.q_table[state] = {a: 0.0 for a in actions}
        return max(self.q_table[state], key=self.q_table[state].get)

    def update(self, state, action, reward, alpha=0.1, gamma=0.9):
        self.q_table[state][action] += alpha * (reward + gamma * max(self.q_table[state].values()) - self.q_table[state][action])
        self.save_q_table()
