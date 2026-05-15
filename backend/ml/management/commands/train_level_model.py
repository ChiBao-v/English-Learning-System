from __future__ import annotations

from datetime import datetime
from pathlib import Path

import joblib
import mlflow
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

from ml.features import FEATURE_COLUMNS, build_feature_dataframe
from ml.models import MLModel, UserFeature


class Command(BaseCommand):
    help = "Train level prediction model from question attempts."

    def handle(self, *args, **options):
        feature_df = build_feature_dataframe()
        if feature_df.empty or len(feature_df) < 6:
            raise CommandError("Not enough training data. Need at least 6 users with attempts.")

        X = feature_df[FEATURE_COLUMNS]
        y = feature_df["predicted_level_id"]

        stratify_target = y if len(y.unique()) > 1 else None
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.3,
                random_state=42,
                stratify=stratify_target,
            )
        except ValueError:
            # Fallback when a class has too few samples for stratified split.
            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.3,
                random_state=42,
                stratify=None,
            )

        model = RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            random_state=42,
        )
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = float(accuracy_score(y_test, y_pred))
        f1 = float(f1_score(y_test, y_pred, average="macro"))

        mlflow_tracking_uri = getattr(settings, "MLFLOW_TRACKING_URI", None) or (
            Path(settings.BASE_DIR) / "ml_artifacts" / "mlruns"
        ).as_uri()
        if not mlflow_tracking_uri.startswith("http"):
            # Convert file:///D:/... → Path để mkdir
            from urllib.request import url2pathname
            from urllib.parse import urlparse
            local_path = Path(url2pathname(urlparse(mlflow_tracking_uri).path))
            local_path.mkdir(parents=True, exist_ok=True)
        mlflow.set_tracking_uri(mlflow_tracking_uri)
        mlflow.set_experiment("toeic_level_prediction")

        version = datetime.now().strftime("%Y%m%d%H%M%S")
        model_dir = Path(settings.BASE_DIR) / "ml_artifacts"
        model_dir.mkdir(parents=True, exist_ok=True)
        model_path = model_dir / f"level_predictor_{version}.joblib"
        joblib.dump(model, model_path)

        with mlflow.start_run(run_name=f"level_predictor_{version}"):
            mlflow.log_param("n_estimators", 200)
            mlflow.log_param("max_depth", 8)
            mlflow.log_param("feature_count", len(FEATURE_COLUMNS))
            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("f1_macro", f1)
            mlflow.log_artifact(str(model_path))

        MLModel.objects.filter(name="level_predictor", is_active=True).update(is_active=False)
        model_record = MLModel.objects.create(
            name="level_predictor",
            version=version,
            metrics={"accuracy": accuracy, "f1_macro": f1},
            model_path=str(model_path),
            is_active=True,
        )

        for _, row in feature_df.iterrows():
            UserFeature.objects.update_or_create(
                user_id=int(row["user_id"]),
                defaults={
                    "avg_response_time": float(row["avg_response_time"]),
                    "accuracy_rate": float(row["accuracy_rate"]),
                    "hint_usage": float(row["hint_usage"]),
                    "consistency": float(row["consistency"]),
                    "predicted_level": str(row["predicted_level"]),
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Training completed. Model version={model_record.version}, accuracy={accuracy:.4f}, f1={f1:.4f}"
            )
        )
