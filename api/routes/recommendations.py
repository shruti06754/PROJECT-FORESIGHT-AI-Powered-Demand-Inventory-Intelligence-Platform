import pandas as pd
from fastapi import APIRouter, HTTPException, Query
from api.app.config import PROJECT_ROOT
from api.schemas.recommendation import RecommendationResponse
from api.services.inventory_service import build_inventory_recommendation

router = APIRouter()

FORECAST_DATA_PATH = (
    PROJECT_ROOT
    / "models"
    / "forecast_output"
    / "foresight_inventory_intelligence.csv"
)


@router.get("/recommendations", response_model=RecommendationResponse)
def get_recommendations(
    limit: int = Query(20, ge=1, le=10000),
    offset: int = Query(0, ge=0)
):
    try:
        df = pd.read_csv(FORECAST_DATA_PATH)

        data = df.iloc[offset:offset + limit].copy()

        recommendations = [
            build_inventory_recommendation(row)
            for _, row in data.iterrows()
        ]

        return {
            "status": "success",
            "rows": len(recommendations),
            "data": recommendations
        }

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Forecast data file not found"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get(
    "/recommendations/{sku}",
    response_model=RecommendationResponse
)
def get_sku_recommendation(sku: str):
    try:
        df = pd.read_csv(FORECAST_DATA_PATH)

        data = df[
            df["SKU"].astype(str).str.upper() == sku.upper()
        ].copy()

        if data.empty:
            raise HTTPException(
                status_code=404,
                detail=f"SKU {sku} not found"
            )

        data["Date"] = pd.to_datetime(data["Date"])
        data = data.sort_values("Date").tail(1)

        recommendations = [
            build_inventory_recommendation(row)
            for _, row in data.iterrows()
        ]

        return {
            "status": "success",
            "sku": sku.upper(),
            "rows": len(recommendations),
            "data": recommendations
        }

    except HTTPException:
        raise

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Forecast data file not found"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )