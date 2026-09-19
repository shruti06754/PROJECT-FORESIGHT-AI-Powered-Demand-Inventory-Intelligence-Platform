import joblib
from api.app.config import MODEL_PATH


class ModelService:
    def __init__(self):
        self.model = None

    def load_model(self):
        if self.model is None:
            self.model = joblib.load(MODEL_PATH)

        return self.model

    def get_model(self):
        return self.load_model()


model_service = ModelService()