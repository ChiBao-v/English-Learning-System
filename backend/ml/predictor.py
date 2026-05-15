from __future__ import annotations

from pathlib import Path

import joblib
from django.conf import settings

from .features import FEATURE_COLUMNS
from .models import MLModel


class PredictionService:
    def __init__(self):
        self._model = None
        self._label_map = {0: "beginner", 1: "intermediate", 2: "advanced"}

    def _resolve_model_path(self) -> Path:
        active_model = MLModel.objects.filter(name="level_predictor", is_active=True).first()
        if not active_model or not active_model.model_path:
            raise RuntimeError("No active model found. Train model first.")
        model_path = Path(active_model.model_path)
        if not model_path.is_absolute():
            model_path = Path(settings.BASE_DIR) / model_path
        if not model_path.exists():
            raise RuntimeError(f"Model file not found at {model_path}")
        return model_path

    def _load_model(self):
        if self._model is None:
            model_path = self._resolve_model_path()
            self._model = joblib.load(model_path)
        return self._model

    def predict_level(self, feature_payload: dict) -> dict:
        model = self._load_model()
        row = [[float(feature_payload.get(column, 0.0)) for column in FEATURE_COLUMNS]]
        predicted_class = int(model.predict(row)[0])
        probabilities = model.predict_proba(row)[0].tolist()

        return {
            "predicted_level": self._label_map.get(predicted_class, "beginner"),
            "class_id": predicted_class,
            "probabilities": probabilities,
        }
