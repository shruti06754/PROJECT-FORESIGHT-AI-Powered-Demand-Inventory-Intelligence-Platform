from fastapi import APIRouter, HTTPException, Query

from api.schemas.forecast import ForecastResponse
from api.services.forecast_service import forecast_service


router = APIRouter()


@router.get("/forecast", response_model=ForecastResponse)
def get_forecast(
    limit: int = Query(20, ge=1, le=10000),
    offset: int = Query(0, ge=0)
):
    try:
        df = forecast_service.generate_forecast()

        data = df.iloc[offset:offset + limit]

        return {
            "status": "success",
            "rows": len(data),
            "data": data.to_dict(orient="records")
        }

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Forecast file not found"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )