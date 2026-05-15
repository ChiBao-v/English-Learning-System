from django.db import models

from courses.models import Course, Lesson, Question
from users.models import User


class Enrollment(models.Model):
    user = models.ForeignKey(User, related_name="enrollments", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "course")
        ordering = ["-enrolled_at"]

    def __str__(self) -> str:
        return f"{self.user.email} -> {self.course.title}"


class LessonProgress(models.Model):
    user = models.ForeignKey(User, related_name="lesson_progress", on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name="lesson_progress", on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    time_spent = models.PositiveIntegerField(default=0, help_text="Seconds spent")
    score = models.FloatField(default=0.0)

    class Meta:
        unique_together = ("user", "lesson")
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"{self.user.email} - {self.lesson.title}"


class QuestionAttempt(models.Model):
    user = models.ForeignKey(User, related_name="question_attempts", on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, related_name="question_attempts", on_delete=models.CASCADE
    )
    user_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    response_time_seconds = models.FloatField(default=0.0)
    answer_changed_count = models.PositiveIntegerField(default=0)
    hint_used = models.BooleanField(default=False)
    attempt_num = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Attempt {self.id} by {self.user.email}"


class BehaviorLog(models.Model):
    user = models.ForeignKey(User, related_name="behavior_logs", on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    event_data = models.JSONField(default=dict, blank=True)
    session_id = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self) -> str:
        return f"{self.user.email} - {self.event_type} - {self.timestamp.isoformat()}"
