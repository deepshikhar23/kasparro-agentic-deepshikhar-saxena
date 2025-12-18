class TemplateEngine:
    def fmt_price(self, price):
        if "₹" not in price and "Rs" not in price:
            return f"₹{price}"
        return price

    def build_product_page(self, data):
        # Default to "Skincare" if benefits list is empty
        main_benefit = data.get('benefits', ['Skincare'])[0]
        
        return {
            "page_meta": {
                "title": f"{data['name']} | {main_benefit} | Official Store",
                "keywords": data['ingredients']
            },
            "hero_section": {
                "headline": f"Experience {main_benefit} with {data['name']}",
                "price_display": self.fmt_price(data['price']),
                "cta_text": "Add to Cart"
            },
            "details_section": {
                "ingredients_list": data['ingredients'],
                "how_to_use": data['usage_instructions'],
                "safety_note": data['safety_warning'] or "Dermatologist tested."
            }
        }

    def build_comparison_page(self, our_product, competitor):
        return {
            "title": f"{our_product['name']} vs {competitor['name']}",
            "comparison_table": [
                {
                    "feature": "Price",
                    "us": self.fmt_price(our_product['price']),
                    "them": self.fmt_price(competitor['price'])
                },
                {
                    "feature": "Key Ingredients",
                    "us": ", ".join(our_product['ingredients']),
                    "them": "Standard generic formulation"
                },
                {
                    "feature": "Primary Benefit",
                    "us": ", ".join(our_product['benefits']),
                    "them": competitor['key_differentiator']
                }
            ],
            "verdict": f"Why {our_product['name']} is the clear winner."
        }