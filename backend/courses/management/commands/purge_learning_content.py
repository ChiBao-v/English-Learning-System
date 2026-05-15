"""Xóa toàn bộ nội dung học tập & khóa học (giữ user)."""

from django.core.management.base import BaseCommand
from django.db import transaction

from courses.models import Course
from learning.models import BehaviorLog, Enrollment, LessonProgress, QuestionAttempt
from ml.models import MLModel, Recommendation, UserFeature


class Command(BaseCommand):
    help = (
        "Xóa courses/lessons/questions và dữ liệu học liên quan "
        "(attempts, enrollment, recommendations, ML cache). Không xóa User."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-input",
            action="store_true",
            help="Không hỏi xác nhận (dùng tự động / CI).",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if not options["no_input"]:
            self.stdout.write(
                self.style.WARNING(
                    "Sẽ xóa toàn bộ khóa học, bài học, câu hỏi, enrollments, "
                    "tiến độ, attempts, recommendations và log hành vi."
                )
            )
            confirm = input("Gõ chính xác YES để tiếp tục: ")
            if confirm.strip() != "YES":
                self.stdout.write("Đã hủy.")
                return

        QuestionAttempt.objects.all().delete()
        LessonProgress.objects.all().delete()
        Enrollment.objects.all().delete()
        Recommendation.objects.all().delete()
        BehaviorLog.objects.all().delete()
        UserFeature.objects.all().delete()
        MLModel.objects.all().delete()
        Course.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Purge complete."))
