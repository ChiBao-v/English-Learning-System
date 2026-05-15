from __future__ import annotations

import random
from dataclasses import dataclass

import numpy as np
import pandas as pd
from django.db.models import F

from learning.models import QuestionAttempt


@dataclass
class FeatureRow:
    user_id: int
    avg_response_time: float
    accuracy_rate: float
    hint_usage: float
    answer_change_rate: float
    consistency: float
    total_attempts: int
    unique_lessons: int


FEATURE_COLUMNS = [
    "avg_response_time",
    "accuracy_rate",
    "hint_usage",
    "answer_change_rate",
    "consistency",
    "total_attempts",
    "unique_lessons",
]


def _consistency_from_series(series: pd.Series) -> float:
    mean_value = float(series.mean()) if len(series) else 0.0
    if mean_value <= 0:
        return 0.0
    std_value = float(series.std()) if len(series) > 1 else 0.0
    value = 1.0 - (std_value / mean_value)
    return float(max(0.0, min(1.0, value)))


def _level_from_features(
    accuracy_rate: float,
    hint_usage: float,
    avg_response_time: float,
    answer_change_rate: float,
    consistency: float,
    total_attempts: int,
    unique_lessons: int,
) -> str:
    """
    Composite score từ tất cả 7 features để label không bị trivially predictable từ 1 feature.

    Weights:
      accuracy_rate       0.35  — độ chính xác tổng thể
      hint_usage (inv)    0.20  — ít dùng gợi ý → giỏi hơn
      response_time (inv) 0.15  — phản hồi nhanh → tự tin hơn
      answer_change (inv) 0.10  — ít đổi đáp án → chắc chắn hơn
      consistency         0.10  — ổn định response_time
      total_attempts      0.05  — học nhiều → kinh nghiệm
      unique_lessons      0.05  — đa dạng bài học

    Thresholds: advanced >= 0.60, intermediate >= 0.38, else beginner.
    """
    rt_score        = max(0.0, min(1.0, (80.0 - avg_response_time) / 75.0))
    hint_score      = max(0.0, min(1.0, 1.0 - hint_usage))
    change_score    = max(0.0, min(1.0, 1.0 - answer_change_rate / 8.0))
    attempts_score  = max(0.0, min(1.0, total_attempts / 150.0))
    lessons_score   = max(0.0, min(1.0, unique_lessons / 20.0))

    score = (
        0.35 * accuracy_rate
        + 0.20 * hint_score
        + 0.15 * rt_score
        + 0.10 * change_score
        + 0.10 * consistency
        + 0.05 * attempts_score
        + 0.05 * lessons_score
    )
    if score >= 0.60:
        return "advanced"
    if score >= 0.38:
        return "intermediate"
    return "beginner"


def build_feature_dataframe() -> pd.DataFrame:
    queryset = (
        QuestionAttempt.objects.select_related("question__lesson")
        .annotate(lesson_id=F("question__lesson_id"))
        .values(
            "user_id",
            "lesson_id",
            "response_time_seconds",
            "is_correct",
            "hint_used",
            "answer_changed_count",
        )
    )
    raw_df = pd.DataFrame(list(queryset))
    if raw_df.empty:
        return pd.DataFrame()

    grouped = raw_df.groupby("user_id")
    rows: list[FeatureRow] = []
    for user_id, group in grouped:
        rows.append(
            FeatureRow(
                user_id=int(user_id),
                avg_response_time=float(group["response_time_seconds"].mean()),
                accuracy_rate=float(group["is_correct"].mean()),
                hint_usage=float(group["hint_used"].mean()),
                answer_change_rate=float(group["answer_changed_count"].mean()),
                consistency=_consistency_from_series(group["response_time_seconds"]),
                total_attempts=int(len(group)),
                unique_lessons=int(group["lesson_id"].nunique()),
            )
        )

    feature_df = pd.DataFrame([row.__dict__ for row in rows])
    feature_df["predicted_level"] = feature_df.apply(
        lambda r: _level_from_features(
            r["accuracy_rate"],
            r["hint_usage"],
            r["avg_response_time"],
            r["answer_change_rate"],
            r["consistency"],
            int(r["total_attempts"]),
            int(r["unique_lessons"]),
        ),
        axis=1,
    )
    # Label noise 10%: mô phỏng thực tế ranh giới trình độ không bao giờ tuyệt đối.
    # Người dùng gần boundary có thể bị phân loại sang level kề nhau.
    _neighbors = {"beginner": ["intermediate"], "intermediate": ["beginner", "advanced"], "advanced": ["intermediate"]}

    def _maybe_flip(level: str) -> str:
        if random.random() < 0.10:
            return random.choice(_neighbors[level])
        return level

    feature_df["predicted_level"] = feature_df["predicted_level"].apply(_maybe_flip)
    feature_df["predicted_level_id"] = feature_df["predicted_level"].map(
        {"beginner": 0, "intermediate": 1, "advanced": 2}
    )

    # Fill numeric NaN values for model stability.
    numeric_cols = FEATURE_COLUMNS + ["predicted_level_id"]
    feature_df[numeric_cols] = feature_df[numeric_cols].replace([np.inf, -np.inf], np.nan).fillna(0)
    return feature_df
