from pydantic import BaseModel
from typing import Any


class RecommendationItem(BaseModel):
    date: str
    sku: str
    product_name: str
    category: str
    predicted_demand: float | None
    current_stock: float | None
    on_order: float | None
    stockout_risk: str | None
    overstock_risk: str | None
    stock_status: str | None
    action: str | None
    priority: str | None
    health_level: str | None
    inventory_health_score: float | None
    recommendation: str


class RecommendationResponse(BaseModel):
    status: str
    rows: int
    data: list[RecommendationItem]