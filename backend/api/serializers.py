from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from courses.models import Course, Lesson, Question

from .course_display import level_label_vi, resolve_public_course_title
from learning.models import Enrollment, LessonProgress, QuestionAttempt
from ml.models import Recommendation

User = get_user_model()


class FlexibleTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Map username (or alternate identifier) to email before JWT authenticate."""

    def validate(self, attrs):
        identifier = attrs.get(self.username_field)
        if identifier:
            user = User.objects.filter(email__iexact=identifier).first()
            if user is None:
                user = User.objects.filter(username__iexact=identifier).first()
            if user is not None:
                attrs = {**attrs, self.username_field: user.email}
        return super().validate(attrs)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("id", "email", "username", "password", "first_name", "last_name")
        read_only_fields = ("id",)

    def create(self, validated_data):
        password = validated_data.pop("password")
        if not validated_data.get("username"):
            validated_data["username"] = validated_data["email"].split("@")[0]
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "role")


class CourseSerializer(serializers.ModelSerializer):
    level_label = serializers.SerializerMethodField()
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "description",
            "level",
            "level_label",
            "skill",
            "cefr_level",
            "thumbnail",
            "lesson_count",
            "is_active",
            "created_at",
            "updated_at",
            "external_id",
        )
        read_only_fields = ("id", "created_at", "updated_at")

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_level_label(self, obj):
        if getattr(obj, "cefr_level", None) and (obj.cefr_level or "").strip():
            band = obj.cefr_level.strip()
            base = level_label_vi(obj.level)
            return f"{band} ({base})"
        return level_label_vi(obj.level)


class PublicCourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    level_label = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("id", "title", "description", "level", "level_label", "skill", "cefr_level", "thumbnail", "lesson_count")

    def get_title(self, obj):
        return resolve_public_course_title(obj)

    def get_level_label(self, obj):
        if (getattr(obj, "cefr_level", None) or "").strip():
            band = obj.cefr_level.strip()
            base = level_label_vi(obj.level)
            return f"{band} ({base})"
        return level_label_vi(obj.level)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "id",
            "course",
            "title",
            "content",
            "transcript",
            "reading_passage",
            "audio_url",
            "order_num",
            "duration",
            "created_at",
        )
        read_only_fields = ("id", "created_at")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "lesson",
            "content",
            "question_type",
            "options",
            "answer",
            "difficulty",
            "hint",
            "skill_type",
            "audio_url",
            "image_url",
            "created_at",
        )
        read_only_fields = ("id", "created_at")


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ("id", "course", "enrolled_at", "progress", "completed")
        read_only_fields = ("id", "enrolled_at", "progress", "completed")


class LessonDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    course_skill = serializers.CharField(source="course.skill", read_only=True)
    course_cefr_level = serializers.CharField(source="course.cefr_level", read_only=True)
    course_title = serializers.CharField(source="course.title", read_only=True)

    class Meta:
        model = Lesson
        fields = (
            "id",
            "course",
            "title",
            "content",
            "transcript",
            "reading_passage",
            "audio_url",
            "order_num",
            "duration",
            "created_at",
            "questions",
            "course_skill",
            "course_cefr_level",
            "course_title",
        )


class SubmitAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    user_answer = serializers.CharField(max_length=255)
    response_time_seconds = serializers.FloatField(min_value=0)
    answer_changed_count = serializers.IntegerField(min_value=0, default=0)
    hint_used = serializers.BooleanField(default=False)
    attempt_num = serializers.IntegerField(min_value=1, default=1)


class CompleteLessonSerializer(serializers.Serializer):
    lesson_id = serializers.IntegerField()
    score = serializers.FloatField(min_value=0, max_value=100)
    time_spent = serializers.IntegerField(min_value=0)


class QuestionAttemptResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAttempt
        fields = (
            "id",
            "question",
            "user_answer",
            "is_correct",
            "response_time_seconds",
            "answer_changed_count",
            "hint_used",
            "attempt_num",
            "created_at",
        )


class LessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = (
            "id",
            "lesson",
            "started_at",
            "completed_at",
            "time_spent",
            "score",
        )


class RecommendationSerializer(serializers.ModelSerializer):
    lesson_title = serializers.CharField(source="lesson.title", read_only=True)
    course_id = serializers.IntegerField(source="lesson.course_id", read_only=True)
    course_title = serializers.CharField(source="lesson.course.title", read_only=True)

    class Meta:
        model = Recommendation
        fields = (
            "id",
            "lesson",
            "lesson_title",
            "course_id",
            "course_title",
            "score",
            "reason",
            "created_at",
        )
