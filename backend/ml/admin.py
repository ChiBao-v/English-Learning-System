from django.contrib import admin

from .models import MLModel, Recommendation, UserFeature


@admin.register(UserFeature)
class UserFeatureAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "avg_response_time",
        "accuracy_rate",
        "hint_usage",
        "predicted_level",
        "updated_at",
    )
    list_filter = ("predicted_level",)
    search_fields = ("user__email",)


@admin.register(MLModel)
class MLModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "version", "is_active", "created_at")
    list_filter = ("name", "is_active")
    search_fields = ("name", "version")


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "lesson", "score", "created_at")
    list_filter = ("lesson__course",)
    search_fields = ("user__email", "lesson__title", "reason")
