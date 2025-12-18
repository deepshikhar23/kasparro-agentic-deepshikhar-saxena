from src.core.llm import GeminiEngine

class BaseAgent:
    def __init__(self, engine):
        self.engine = engine

    def run(self, data):
        raise NotImplementedError("Subclasses must implement run()")

    def log(self, msg):
        print(f"[{self.__class__.__name__}] {msg}")