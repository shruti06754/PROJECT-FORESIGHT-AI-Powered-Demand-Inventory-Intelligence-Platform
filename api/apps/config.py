from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

API_TITLE = "FORESIGHT API"
API_VERSION = "1.0.0"
API_DESCRIPTION = "AI Demand & Inventory Intelligence Platform"

MODEL_PATH = PROJECT_ROOT / "models" / "random_forest_demand_model.pkl"

FORECAST_DATA_PATH = (
    PROJECT_ROOT
    / "models"
    / "forecast_output"
    / "foresight_inventory_intelligence.csv"
)

