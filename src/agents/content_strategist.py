from src.agents.base_agent import BaseAgent
from src.templates.schemas import FAQPage

class ContentStrategistAgent(BaseAgent):
    def run(self, data):
        self.log("Generating customer FAQs...")
        
        # Build context from the previous agent's output
        context = f"""
        Product: {data.get('name')}
        Ingredients: {', '.join(data.get('ingredients', []))}
        Usage: {data.get('usage_instructions')}
        Safety: {data.get('safety_warning')}
        """

        prompt = f"""
        Generate exactly 15 distinct FAQs for this product based on the context.
        
        Cover these categories:
        1. Safety & Sensitivity
        2. Usage Routine
        3. Ingredient Benefits
        4. Storage
        5. Expected Results
        
        CONTEXT:
        {context}
        """

        return self.engine.generate_json(prompt, schema=FAQPage)