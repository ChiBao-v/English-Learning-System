"""Import khóa học từ JSON (C01…C06 trong fixtures hoặc file tự soạn)."""

from __future__ import annotations

import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

from courses.course_json_import import (
    CourseJsonImportError,
    import_course_payload,
    validate_course_payload,
)

DEFAULT_JSON = Path(__file__).resolve().parent.parent.parent / "fixtures" / "course_C01_foundation.json"


class Command(BaseCommand):
    help = (
        "Import một khóa học từ file JSON (mặc định: course_C01_foundation.json). "
        "Dùng --dry-run để kiểm tra; --replace-if-exists để ghi đè khóa cùng course_id."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default=str(DEFAULT_JSON),
            help="Đường dẫn file JSON.",
        )
        parser.add_argument(
            "--purge-first",
            action="store_true",
            help="Chạy purge_learning_content trước khi import (xóa toàn bộ khóa & log học).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Chỉ kiểm tra cấu trúc JSON, không ghi DB.",
        )
        parser.add_argument(
            "--replace-if-exists",
            action="store_true",
            help="Nếu course_id trong JSON trùng external_id khóa đã có, xóa khóa cũ rồi import.",
        )

    def handle(self, *args, **options):
        path = Path(options["path"])
        if not path.is_file():
            raise CommandError(f"File not found: {path}")

        if options["purge_first"]:
            if options["dry_run"]:
                raise CommandError("Không kết hợp --purge-first với --dry-run.")
            call_command("purge_learning_content", no_input=True)

        raw = path.read_text(encoding="utf-8")
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            raise CommandError(f"JSON không hợp lệ: {e}") from e

        errors = validate_course_payload(data)
        if errors:
            for line in errors:
                self.stdout.write(self.style.ERROR(line))
            raise CommandError(f"Validation failed ({len(errors)} issue(s)).")

        if options["dry_run"]:
            n_lessons = len(data.get("lessons") or [])
            n_q = sum(len(les.get("quizzes") or []) for les in (data.get("lessons") or []))
            self.stdout.write(
                self.style.SUCCESS(
                    "Dry-run OK: lessons=%s questions=%s external_id=%r"
                    % (n_lessons, n_q, (data.get("course_id") or "")[:32])
                )
            )
            return

        try:
            course, n_lessons, n_questions = import_course_payload(
                data,
                replace_if_exists=options["replace_if_exists"],
            )
        except CourseJsonImportError as e:
            raise CommandError(str(e)) from e

        self.stdout.write(
            self.style.SUCCESS(
                f"Import OK: db_course_pk={course.id} external_id={course.external_id!r} "
                f"lessons={n_lessons} questions={n_questions}"
            )
        )
