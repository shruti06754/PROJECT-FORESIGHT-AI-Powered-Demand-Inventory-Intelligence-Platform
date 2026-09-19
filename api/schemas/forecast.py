from pydantic import BaseModel
from typing import Any


class ForecastResponse(BaseModel):
    status: str
    rows: int
    data: list[dict[str, Any]]
