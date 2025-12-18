from typing import List, Optional
from pydantic import BaseModel, Field

# 1. Product Data Model
class ProductSchema(BaseModel):
    name: str = Field(description="Name of the product")
    price: str = Field(description="Price (e.g. $25)")
    skin_type: List[str] = Field(description="Best for these skin types")
    ingredients: List[str] = Field(description="Active ingredients list")
    benefits: List[str] = Field(description="Main selling points")
    usage_instructions: str = Field(description="Step-by-step usage")
    safety_warning: Optional[str] = Field(description="Warnings or caution notes")

# 2. FAQ Output
class FAQItem(BaseModel):
    category: str
    question: str
    answer: str

class FAQPage(BaseModel):
    faqs: List[FAQItem]

# 3. Competitor Analysis
class CompetitorProduct(BaseModel):
    name: str
    price: str
    key_differentiator: str
    pros: List[str]
    cons: List[str]