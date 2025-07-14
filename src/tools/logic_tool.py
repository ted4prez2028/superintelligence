from src.reasoning.prolog_solver import logic_infer

def logic_reason(text: str) -> str:
    return logic_infer(text)