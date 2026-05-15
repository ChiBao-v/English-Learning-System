from django.contrib import admin

from .models import BehaviorLog, Enrollment, LessonProgress, QuestionAttempt


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "progress", "completed", "enrolled_at")
    list_filter = ("completed", "course")
    search_fields = ("user__email", "course__title")


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "lesson", "score", "time_spent", "completed_at")
    list_filter = ("lesson__course",)
    search_fields = ("user__email", "lesson__title")


@admin.register(QuestionAttempt)
class QuestionAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "question",
        "is_correct",
        "response_time_seconds",
        "answer_changed_count",
        "hint_used",
        "created_at",
    )
    list_filter = ("is_correct", "hint_used", "question__skill_type")
    search_fields = ("user__email", "question__content", "user_answer")


@admin.register(BehaviorLog)
class BehaviorLogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "event_type", "session_id", "timestamp")
    list_filter = ("event_type",)
    search_fields = ("user__email", "session_id")
