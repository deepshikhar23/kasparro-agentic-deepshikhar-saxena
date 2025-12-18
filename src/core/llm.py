import json
import time
import google.generativeai as genai
from google.api_core import exceptions
from src import config

class GeminiEngine:
    def __init__(self):
        genai.configure(api_key=config.API_KEY)
        self.model = genai.GenerativeModel(
            model_name=config.MODEL_NAME,
            generation_config=config.GENERATION_CONFIG
        )

    def generate(self, prompt, schema=None):
        for i in range(3):
            try:
                if schema:
                    response = self.model.generate_content(
                        prompt,
                        generation_config=genai.GenerationConfig(
                            response_mime_type="application/json",
                            response_schema=schema
                        )
                    )
                else:
                    response = self.model.generate_content(prompt)
                
                return response.text

            except Exception as e:
                print(f"API hit a snag: {e}. Retrying in {2 * (i + 1)}s...")
                time.sleep(2 * (i + 1))
        
        raise Exception("API keeps failing. Check quota or connection.")

    def generate_json(self, prompt, schema=None):
        res = self.generate(prompt, schema)
        return json.loads(res)