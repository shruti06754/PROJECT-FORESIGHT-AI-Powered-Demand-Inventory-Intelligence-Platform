import pandas as pd

from api.app.config import PROJECT_ROOT


FORECAST_PATH = PROJECT_ROOT / "Data" / "raw" / "forecast_output.csv"


class ForecastService:

    def __init__(self):
        self.forecast_df = None

    def load_forecast(self):
        if self.forecast_df is None:

            if not FORECAST_PATH.exists():
                raise FileNotFoundError(
                    f"Forecast file not found: {FORECAST_PATH}"
                )

            self.forecast_df = pd.read_csv(FORECAST_PATH)

            self.forecast_df["Date"] = pd.to_datetime(
                self.forecast_df["Date"]
            )

        return self.forecast_df

    def generate_forecast(self):
        return self.load_forecast()


forecast_service = ForecastService()