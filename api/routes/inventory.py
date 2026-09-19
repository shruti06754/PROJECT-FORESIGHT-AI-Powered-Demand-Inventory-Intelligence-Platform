import pandas as pd
from fastapi import APIRouter, HTTPException, Query
from api.app.config import PROJECT_ROOT
from api.schemas.inventory import InventoryResponse

router = APIRouter()

INVENTORY_DATA_PATH = PROJECT_ROOT / "Data" / "raw" / "inventory.csv"


@router.get("/inventory", response_model=InventoryResponse)
def get_inventory(
    limit: int = Query(20, ge=1, le=10000),
    offset: int = Query(0, ge=0)
):
    try:
        df = pd.read_csv(INVENTORY_DATA_PATH)

        data = df.iloc[offset:offset + limit].copy()

        data = data.rename(
            columns={
                "Snapshot_Date": "snapshot_date",
                "SKU": "sku",
                "Current_Stock": "current_stock",
                "On_Order": "on_order",
                "Lead_Time_Days": "lead_time_days",
                "Safety_Stock": "safety_stock",
                "Reorder_Point": "reorder_point",
                "Inventory_Value": "inventory_value"
            }
        )

        return {
            "status": "success",
            "rows": len(data),
            "data": data.to_dict(orient="records")
        }

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Inventory data file not found"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )