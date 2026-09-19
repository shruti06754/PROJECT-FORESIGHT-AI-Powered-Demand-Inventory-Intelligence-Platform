from fastapi import FastAPI
from api.app.config import API_TITLE, API_VERSION, API_DESCRIPTION
from api.routes.health import router as health_router
from api.routes.forecast import router as forecast_router
from api.routes.inventory import router as inventory_router
from api.routes.recommendations import router as recommendations_router

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description=API_DESCRIPTION
)


@app.get("/")
def root():
    return {
        "message": "FORESIGHT API is running",
        "docs": "/docs",
        "health": "/health"
    }


app.include_router(health_router)
app.include_router(forecast_router)
app.include_router(inventory_router)
app.include_router(recommendations_router)
