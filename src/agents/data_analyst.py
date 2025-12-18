from src.agents.base_agent import BaseAgent
from src.templates.schemas import ProductSchema

class DataAnalystAgent(BaseAgent):
    def run(self, data):
        self.log("Parsing raw product data...")
  
        prompt = f"""
        Extract structured data from this raw text. 
        IMPORTANT: Preserve specific details like concentrations (e.g., "10% Vitamin C", not just "Vitamin C").
        
        RAW TEXT:
        {data.get('raw_text', '')}
        """

        return self.engine.generate_json(prompt, schema=ProductSchema)