import json
from src.core.orchestrator import KasparroOrchestrator

if __name__ == "__main__":
    # Load the test data
    with open("data/input/product_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Fire it up
    app = KasparroOrchestrator()
    app.start_pipeline(data["raw_text"])