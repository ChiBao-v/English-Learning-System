from django.db import models

from courses.models import Lesson
from users.models import User


class UserFeature(models.Model):
    class PredictedLevel(models.TextChoices):
        BEGINNER = "beginner", "Beginner"
        INTERMEDIATE = "intermediate", "Intermediate"
        ADVANCED = "advanced", "Advanced"

    user = models.OneToOneField(User, related_name="feature", on_delete=models.CASCADE)
    avg_response_time = models.FloatField(default=0.0)
    accuracy_rate = models.FloatField(default=0.0)
    hint_usage = models.FloatField(default=0.0)
    consistency = models.FloatField(default=0.0)
    predicted_level = models.CharField(
        max_length=20, choices=PredictedLevel.choices, default=PredictedLevel.BEGINNER
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Feature({self.user.email})"


class MLModel(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    metrics = models.JSONField(default=dict, blank=True)
    model_path = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("name", "version")

    def __str__(self) -> str:
        return f"{self.name}:{self.version}"


class Recommendation(models.Model):
    user = models.ForeignKey(
        User, related_name="recommendations", on_delete=models.CASCADE
    )
    lesson = models.ForeignKey(
        Lesson, related_name="recommendations", on_delete=models.CASCADE
    )
    score = models.FloatField(default=0.0)
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-score", "-created_at"]

    def __str__(self) -> str:
        return f"Rec(user={self.user_id}, lesson={self.lesson_id}, score={self.score})"
