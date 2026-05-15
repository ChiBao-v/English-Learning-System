"""Tạo khóa rỗng: 4 kỹ năng × 4 band (A1–B2), external_id dạng listening_a1, reading_b2, …"""

from django.core.management.base import BaseCommand
from django.db import transaction

from courses.models import Course

SKILLS = (
    ("listening", "Listening"),
    ("reading", "Reading"),
    ("writing", "Writing"),
    ("speaking", "Speaking"),
)
BANDS = ("a1", "a2", "b1", "b2")
BAND_TO_CEFR = {"a1": "A1", "a2": "A2", "b1": "B1", "b2": "B2"}
BAND_TO_LEVEL = {
    "a1": Course.Level.BEGINNER,
    "a2": Course.Level.BEGINNER,
    "b1": Course.Level.INTERMEDIATE,
    "b2": Course.Level.INTERMEDIATE,
}
BAND_TO_SKILL_ENUM = {
    "listening": Course.Skill.LISTENING,
    "reading": Course.Skill.READING,
    "writing": Course.Skill.WRITING,
    "speaking": Course.Skill.SPEAKING,
}


class Command(BaseCommand):
    help = "Tạo/ cập nhật 16 khóa học (Listening/Reading/Writing/Speaking × A1–B2), chưa có bài học."

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-existing",
            action="store_true",
            help="Không ghi đè khóa đã có (cùng external_id).",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        skip = options["skip_existing"]
        created = 0
        updated = 0
        for key, label in SKILLS:
            skill_enum = BAND_TO_SKILL_ENUM[key]
            for band in BANDS:
                ext = f"{key}_{band}"
                title = f"{label} — {BAND_TO_CEFR[band]}"
                desc = (
                    f"Khóa {label} trình độ {BAND_TO_CEFR[band]}. "
                    "Nội dung bài học sẽ được thêm qua import JSON."
                )
                defaults = {
                    "title": title,
                    "description": desc,
                    "level": BAND_TO_LEVEL[band],
                    "skill": skill_enum,
                    "cefr_level": BAND_TO_CEFR[band],
                    "is_active": True,
                }
                if skip and Course.objects.filter(external_id=ext).exists():
                    continue
                obj, was_created = Course.objects.update_or_create(
                    external_id=ext,
                    defaults=defaults,
                )
                if was_created:
                    created += 1
                else:
                    updated += 1
        self.stdout.write(
            self.style.SUCCESS(f"seed_skill_cefr_courses: created={created} updated={updated} skip_existing={skip}")
        )
