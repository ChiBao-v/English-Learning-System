"""Tạo khóa BIG STEP TOEIC 1 và các Lesson theo content_drafts/big_step_toeic_1/toc.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from courses.models import Course, Lesson


def _reconfigure_stdout() -> None:
    out = sys.stdout
    if hasattr(out, "reconfigure"):
        try:
            out.reconfigure(encoding="utf-8")
        except Exception:
            pass


def _default_toc_path() -> Path:
    return Path(settings.BASE_DIR).parent / "content_drafts" / "big_step_toeic_1" / "toc.json"


def _flatten_lessons(spec: dict) -> list[tuple[str, str]]:
    """
    Returns list of (section_key, title) in global order.
    section_key: listening_p1_u1 | grammar_u1 | ...
    """
    rows: list[tuple[str, str]] = []
    for part in spec["listening"]["parts"]:
        pnum = part["part"]
        for u in part["units"]:
            key = f"listening_p{pnum}_u{u['unit']}"
            rows.append((key, u["title"]))
    g = spec["reading"]["grammar"]["units"]
    for u in g:
        rows.append((f"grammar_u{u['unit']}", u["title"]))
    v = spec["reading"]["vocabulary"]["units"]
    for u in v:
        rows.append((f"vocabulary_u{u['unit']}", u["title"]))
    r = spec["reading"]["reading"]["units"]
    for u in r:
        rows.append((f"reading_u{u['unit']}", u["title"]))
    return rows


class Command(BaseCommand):
    help = "Seed một Course và các Lesson theo toc.json (BIG STEP TOEIC 1)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--toc",
            type=str,
            default="",
            help="Đường dẫn tới toc.json (mặc định: content_drafts/big_step_toeic_1/toc.json).",
        )
        parser.add_argument(
            "--replace",
            action="store_true",
            help="Nếu đã có course_title trong DB, xóa khóa đó rồi tạo lại.",
        )
        parser.add_argument(
            "--audio-map",
            type=str,
            default="",
            help="JSON optional: by_lesson_order { \"1\": \"/audio/...\" } (mặc định cạnh toc).",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        _reconfigure_stdout()
        toc_path = Path(options["toc"] or _default_toc_path()).resolve()
        if not toc_path.is_file():
            raise CommandError(f"Không tìm thấy: {toc_path}")

        with toc_path.open(encoding="utf-8") as f:
            spec = json.load(f)

        course_title = spec.get("course_title") or "BIG STEP TOEIC 1"
        description = spec.get("course_description", "")

        audio_map_path = Path(options["audio_map"] or toc_path.parent / "audio_map.json").resolve()
        audio_by_order: dict[str, str] = {}
        if audio_map_path.is_file():
            with audio_map_path.open(encoding="utf-8") as f:
                data = json.load(f)
            audio_by_order = {str(k): str(v) for k, v in (data.get("by_lesson_order") or {}).items()}

        existing = Course.objects.filter(title=course_title).first()
        if existing and not options["replace"]:
            raise CommandError(
                f'Đã có khóa "{course_title}". Dùng --replace để xóa và tạo lại, hoặc đổi course_title trong toc.json.'
            )

        if existing and options["replace"]:
            from courses.management.commands.flush_learning_data import _delete_course_by_title

            _delete_course_by_title(course_title)

        course = Course.objects.create(
            title=course_title[:255],
            description=description,
            level=Course.Level.INTERMEDIATE,
        )

        lessons_flat = _flatten_lessons(spec)
        for order, (key, title) in enumerate(lessons_flat, start=1):
            audio_url = audio_by_order.get(str(order), "").strip()
            Lesson.objects.create(
                course=course,
                title=title[:255],
                content="",
                audio_url=audio_url[:500] if audio_url else "",
                order_num=order,
                duration=30,
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'Đã tạo khóa "{course_title}" với {len(lessons_flat)} bài (order 1–{len(lessons_flat)}).'
            )
        )
        if audio_map_path.is_file():
            self.stdout.write(f"Đã áp dụng audio_map: {audio_map_path}")
        else:
            self.stdout.write("Chưa có audio_map.json — thêm by_lesson_order để gắn file nghe.")
