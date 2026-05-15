from django.db import models


class Course(models.Model):
    class Level(models.TextChoices):
        BEGINNER = "beginner", "Beginner"
        INTERMEDIATE = "intermediate", "Intermediate"
        ADVANCED = "advanced", "Advanced"

    class Skill(models.TextChoices):
        GENERAL = "general", "General"
        LISTENING = "listening", "Listening"
        READING = "reading", "Reading"
        WRITING = "writing", "Writing"
        SPEAKING = "speaking", "Speaking"

    title = models.CharField(max_length=255)
    external_id = models.CharField(
        max_length=32,
        blank=True,
        default="",
        db_index=True,
        help_text="Mã khóa trong file fixture (vd: C01).",
    )
    description = models.TextField(blank=True)
    level = models.CharField(max_length=20, choices=Level.choices, default=Level.BEGINNER)
    skill = models.CharField(
        max_length=20,
        choices=Skill.choices,
        default=Skill.GENERAL,
        help_text="Kỹ năng chính của khóa (listening, reading, …).",
    )
    cefr_level = models.CharField(
        max_length=8,
        blank=True,
        default="",
        help_text="Band CEFR hiển thị: A1, A2, B1, B2, …",
    )
    thumbnail = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    transcript = models.TextField(
        blank=True,
        default="",
        help_text="Lời thoại/script audio (listening). Hiển thị trên trang bài tập, không phải trang tài liệu.",
    )
    reading_passage = models.TextField(
        blank=True,
        default="",
        help_text="Đoạn đọc chính (reading). Hiển thị trên trang bài tập; tab Tài-liệu chỉ preparation.",
    )
    audio_url = models.CharField(
        max_length=500,
        blank=True,
        default="",
        help_text="URL hoặc đường dẫn tương đối cho audio (text-only có thể để trống).",
    )
    order_num = models.PositiveIntegerField(default=1)
    duration = models.PositiveIntegerField(default=0, help_text="Duration in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["course_id", "order_num", "id"]
        unique_together = ("course", "order_num")

    def __str__(self) -> str:
        return f"{self.course.title} - {self.title}"


class Question(models.Model):
    class Type(models.TextChoices):
        MULTIPLE_CHOICE = "multiple_choice", "Multiple Choice"
        TRUE_FALSE = "true_false", "True/False"
        FILL_IN_BLANK = "fill_in_blank", "Fill In Blank"

    class SkillType(models.TextChoices):
        LISTENING = "listening", "Listening"
        READING = "reading", "Reading"
        GRAMMAR = "grammar", "Grammar"
        VOCABULARY = "vocabulary", "Vocabulary"
        WRITING = "writing", "Writing"
        SPEAKING = "speaking", "Speaking"

    lesson = models.ForeignKey(Lesson, related_name="questions", on_delete=models.CASCADE)
    content = models.TextField()
    question_type = models.CharField(
        max_length=20, choices=Type.choices, default=Type.MULTIPLE_CHOICE
    )
    options = models.JSONField(default=list, blank=True)
    answer = models.CharField(max_length=255)
    difficulty = models.PositiveSmallIntegerField(default=1)
    hint = models.TextField(blank=True)
    skill_type = models.CharField(
        max_length=20, choices=SkillType.choices, default=SkillType.READING
    )
    audio_url = models.CharField(
        max_length=500,
        blank=True,
        default="",
        help_text="Audio cho câu listening (không dùng thì để trống).",
    )
    image_url = models.CharField(
        max_length=500,
        blank=True,
        default="",
        help_text="Hình minh học (text-only có thể để trống).",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["lesson_id", "id"]

    def __str__(self) -> str:
        return f"Q{self.id} - Lesson {self.lesson_id}"
