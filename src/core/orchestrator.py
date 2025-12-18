import json
import time
from src import config
from src.core.llm import GeminiEngine
from src.agents.data_analyst import DataAnalystAgent
from src.agents.content_strategist import ContentStrategistAgent
from src.agents.competitor_bot import CompetitorBotAgent
from src.templates.engine import TemplateEngine

class KasparroOrchestrator:
    def __init__(self):
        self.engine = GeminiEngine()
        self.templates = TemplateEngine()
        
        self.analyst = DataAnalystAgent(self.engine)
        self.strategist = ContentStrategistAgent(self.engine)
        self.competitor = CompetitorBotAgent(self.engine)

    def save_json(self, filename, data):
        path = config.OUTPUT_DIR / filename
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Saved: {filename}")

    def start_pipeline(self, raw_text):
        print("Starting content pipeline...")

        # 1. Analyze
        print("   [1/3] Analyzing raw input...")
        product_data = self.analyst.run({"raw_text": raw_text})
        time.sleep(2) # polite delay for API
        
        # 2. Strategy
        print("   [2/3] Generating content strategy...")
        faq_data = self.strategist.run(product_data)
        time.sleep(2)

        # 3. Competitor
        print("   [3/3] Running market comparison...")
        comp_data = self.competitor.run(product_data)

        # 4. Compile
        prod_page = self.templates.build_product_page(product_data)
        comp_page = self.templates.build_comparison_page(product_data, comp_data)

        # Save outputs
        self.save_json("faq.json", faq_data)
        self.save_json("product_page.json", prod_page)
        self.save_json("comparison_page.json", comp_page)
        
        print("\n Finished.")