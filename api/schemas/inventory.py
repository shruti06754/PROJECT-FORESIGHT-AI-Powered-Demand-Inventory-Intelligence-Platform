from pydantic import BaseModel
from typing import Any


class InventoryItem(BaseModel):
    snapshot_date: str
    sku: str
    current_stock: float | None
    on_order: float | None
    lead_time_days: float | None
    safety_stock: float | None
    reorder_point: float | None
    inventory_value: float | None


class InventoryResponse(BaseModel):
    status: str
    rows: int
    data: list[InventoryItem]