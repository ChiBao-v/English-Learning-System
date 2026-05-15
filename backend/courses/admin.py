from django.contrib import admin

from .models import Course, Lesson, Question


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "skill", "cefr_level", "level", "is_active", "created_at")
    list_filter = ("level", "skill", "is_active")
    search_fields = ("title", "description")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "course", "order_num", "duration", "created_at")
    list_filter = ("course",)
    search_fields = ("title", "content", "transcript", "reading_passage")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson", "question_type", "skill_type", "difficulty")
    list_filter = ("question_type", "skill_type", "difficulty")
    search_fields = ("content", "answer")
