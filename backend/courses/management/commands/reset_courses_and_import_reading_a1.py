"""
Xóa toàn bộ khóa/bài/log học → seed 16 khóa → import Reading A1 (4 bài + quiz).

Fixture: courses/fixtures/course_reading_a1.json (tạo lại bằng
  python courses/fixtures/generate_reading_a1_fixture.py).

Chạy (từ thư mục backend, venv đã kích hoạt):
  python manage.py reset_courses_and_import_reading_a1 --no-input
"""

from pathlib import Path

from django.core.management import call_command
from django.core.management.base import BaseCommand

FIXTURE = Path(__file__).resolve().parent.parent.parent / "fixtures" / "course_reading_a1.json"


class Command(BaseCommand):
    help = "Purge learning content, seed 16 skill courses, import Reading A1 (4 lessons, 18 Q each)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-input",
            action="store_true",
            help="Không hỏi xác nhận trước khi purge.",
        )
        parser.add_argument(
            "--skip-import",
            action="store_true",
            help="Chỉ purge + seed, không import Reading A1.",
        )

    def handle(self, *args, **options):
        if not options["no_input"]:
            self.stdout.write(self.style.WARNING("Bạn sắp xóa toàn bộ khóa học và dữ liệu học liên quan."))
            confirm = input("Gõ chính xác YES để tiếp tục: ")
            if confirm.strip() != "YES":
                self.stdout.write("Đã hủy.")
                return

        call_command("purge_learning_content", no_input=True)
        call_command("seed_skill_cefr_courses")

        if options["skip_import"]:
            self.stdout.write(self.style.SUCCESS("Done (skip import)."))
            return

        if not FIXTURE.is_file():
            self.stdout.write(self.style.ERROR(f"Thiếu file: {FIXTURE}"))
            self.stdout.write("Chạy: python courses/fixtures/generate_reading_a1_fixture.py")
            return

        call_command(
            "import_course_json",
            path=str(FIXTURE),
            replace_if_exists=True,
        )
        self.stdout.write(self.style.SUCCESS("reset_courses_and_import_reading_a1: done."))
