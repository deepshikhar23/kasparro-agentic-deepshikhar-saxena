from src.agents.base_agent import BaseAgent
from src.templates.schemas import CompetitorProduct

class CompetitorBotAgent(BaseAgent):
    def run(self, data):
        self.log("Scouting competition...")
        
        prompt = f"""
        Invent a realistic competitor product to compare against {data.get('name')}.
        It should be slightly inferior or offer a trade-off (e.g. cheaper but has alcohol).
        
        MAIN PRODUCT:
        Price: {data.get('price')}
        Ingredients: {data.get('ingredients')}
        
        Generate:
        - Name (Generic but realistic)
        - Price
        - Key Differentiator
        - Pros & Cons
        """

        return self.engine.generate_json(prompt, schema=CompetitorProduct)