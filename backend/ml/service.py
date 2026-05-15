from __future__ import annotations

import pandas as pd
from django.db.models import Avg, Case, FloatField, Value, When

from courses.models import Lesson
from learning.models import QuestionAttempt
from ml.models import Recommendation, UserFeature

from .features import _consistency_from_series
from .predictor import PredictionService


def build_feature_payload_for_user(user_id: int) -> dict:
    attempts = QuestionAttempt.objects.filter(user_id=user_id).values(
        "response_time_seconds",
        "is_correct",
        "hint_used",
        "answer_changed_count",
        "question__lesson_id",
    )
    attempts = list(attempts)
    if not attempts:
        return {
            "avg_response_time": 0.0,
            "accuracy_rate": 0.0,
            "hint_usage": 0.0,
            "answer_change_rate": 0.0,
            "consistency": 0.0,
            "total_attempts": 0.0,
            "unique_lessons": 0.0,
        }

    response_times = [float(item["response_time_seconds"]) for item in attempts]
    is_correct_values = [1.0 if item["is_correct"] else 0.0 for item in attempts]
    hint_values = [1.0 if item["hint_used"] else 0.0 for item in attempts]
    answer_change_values = [float(item["answer_changed_count"]) for item in attempts]
    lesson_ids = {int(item["question__lesson_id"]) for item in attempts if item["question__lesson_id"]}

    avg_response_time = sum(response_times) / len(response_times)
    accuracy_rate = sum(is_correct_values) / len(is_correct_values)
    hint_usage = sum(hint_values) / len(hint_values)
    answer_change_rate = sum(answer_change_values) / len(answer_change_values)
    consistency = _consistency_from_series(pd.Series(response_times))

    return {
        "avg_response_time": avg_response_time,
        "accuracy_rate": accuracy_rate,
        "hint_usage": hint_usage,
        "answer_change_rate": answer_change_rate,
        "consistency": consistency,
        "total_attempts": float(len(attempts)),
        "unique_lessons": float(len(lesson_ids)),
    }


def predict_user_level(user_id: int) -> dict:
    payload = build_feature_payload_for_user(user_id)
    predictor = PredictionService()
    prediction = predictor.predict_level(payload)
    return {"features": payload, "prediction": prediction}


def _extract_weak_skills(user_id: int) -> list[str]:
    skill_rows = (
        QuestionAttempt.objects.filter(user_id=user_id)
        .values("question__skill_type")
        .annotate(
            accuracy=Avg(
                Case(
                    When(is_correct=True, then=Value(1.0)),
                    default=Value(0.0),
                    output_field=FloatField(),
                )
            )
        )
        .order_by("accuracy")
    )
    weak = []
    for row in skill_rows:
        skill = row.get("question__skill_type")
        accuracy = float(row.get("accuracy") or 0.0)
        if skill and accuracy < 0.7:
            weak.append(skill)
    return weak


def _score_lesson(lesson, weak_skills: list[str], predicted_level: str) -> tuple[float, str]:
    level_score = 1.0 if lesson.course.level == predicted_level else 0.5
    skill_score = 1.0 if lesson.questions.filter(skill_type__in=weak_skills).exists() else 0.3
    recency_score = 0.4
    final_score = (0.5 * skill_score) + (0.3 * level_score) + (0.2 * recency_score)
    if skill_score >= 1.0:
        skills_vi = ", ".join(weak_skills[:2])
        reason = f"Luyện thêm kỹ năng đang thấp điểm: {skills_vi}"
    elif lesson.course.level == predicted_level:
        reason = "Bài học trong nhóm trình độ phù hợp tiến độ hiện tại của bạn"
    else:
        reason = "Gợi ý bài tiếp theo theo tiến độ học"
    return final_score, reason


def generate_recommendations_for_user(user_id: int, top_n: int = 5) -> dict:
    prediction_payload = predict_user_level(user_id)
    predicted_level = prediction_payload["prediction"]["predicted_level"]
    weak_skills = _extract_weak_skills(user_id)

    UserFeature.objects.update_or_create(
        user_id=user_id,
        defaults={
            "avg_response_time": prediction_payload["features"]["avg_response_time"],
            "accuracy_rate": prediction_payload["features"]["accuracy_rate"],
            "hint_usage": prediction_payload["features"]["hint_usage"],
            "consistency": prediction_payload["features"]["consistency"],
            "predicted_level": predicted_level,
        },
    )

    completed_lesson_ids = set(
        QuestionAttempt.objects.filter(user_id=user_id).values_list("question__lesson_id", flat=True)
    )
    candidate_lessons = (
        Lesson.objects.select_related("course")
        .prefetch_related("questions")
        .exclude(id__in=completed_lesson_ids)
        .filter(course__is_active=True)
    )
    if predicted_level and candidate_lessons.filter(course__level=predicted_level).exists():
        candidate_lessons = candidate_lessons.filter(course__level=predicted_level)

    scored = []
    for lesson in candidate_lessons.distinct():
        score, reason = _score_lesson(lesson, weak_skills, predicted_level)
        scored.append((lesson, score, reason))

    scored.sort(key=lambda item: item[1], reverse=True)
    top = scored[:top_n]

    Recommendation.objects.filter(user_id=user_id).delete()
    rec_rows = []
    for lesson, score, reason in top:
        rec_rows.append(
            Recommendation(
                user_id=user_id,
                lesson=lesson,
                score=round(float(score), 4),
                reason=reason,
            )
        )
    if rec_rows:
        Recommendation.objects.bulk_create(rec_rows)

    return {
        "predicted_level": predicted_level,
        "weak_skills": weak_skills,
        "recommendations": [
            {
                "lesson_id": rec.lesson_id,
                "lesson_title": rec.lesson.title,
                "course_id": rec.lesson.course_id,
                "course_title": rec.lesson.course.title,
                "score": rec.score,
                "reason": rec.reason,
            }
            for rec in Recommendation.objects.select_related("lesson__course").filter(user_id=user_id)[:top_n]
        ],
    }
