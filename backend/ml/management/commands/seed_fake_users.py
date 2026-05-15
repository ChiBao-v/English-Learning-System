"""
Sinh user giả với QuestionAttempt realistic theo 3 trình độ (beginner/intermediate/advanced).
Mỗi trình độ có 3 sub-tier để tăng độ đa dạng và giúp RandomForest phân loại chính xác hơn.

    python manage.py seed_fake_users              # 500 user
    python manage.py seed_fake_users --count 200
    python manage.py seed_fake_users --batch 50   # in tiến độ mỗi 50 user
"""

from __future__ import annotations

import random
import sys
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from courses.models import Course, Lesson, Question
from learning.models import BehaviorLog, Enrollment, LessonProgress, QuestionAttempt
from ml.models import UserFeature
from ml.service import build_feature_payload_for_user
from users.models import User

try:
    from faker import Faker
    fake = Faker("vi_VN")
    Faker.seed(0)
except ImportError:
    fake = None

# ---------------------------------------------------------------------------
# Sub-tier profiles — 3 trình độ × 3 tier = 9 profiles để tăng độ đa dạng.
# Mỗi tier thể hiện người học ở đầu/giữa/cuối của dải trình độ đó.
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Label boundary trong features.py: accuracy < 0.6 → beginner,
# 0.6–0.8 → intermediate, >= 0.8 → advanced.
#
# Để tránh accuracy=1.0 (model học trivially), các profile được thiết kế
# để CHỒNG LÊN ngưỡng 0.6 và 0.8 — một số user beginner có accuracy > 0.6
# (label intermediate), một số advanced có accuracy < 0.8 (label intermediate).
# Số attempts nhỏ (15–50) giữ variance cao thay vì trung bình hóa về target.
# ---------------------------------------------------------------------------
PROFILES = [
    # ── BEGINNER ──────────────────────────────────────────────────────────
    # Phần lớn < 0.6, nhưng ~20% vượt ngưỡng → được gán label intermediate
    {
        "level": "beginner",
        "tier": "weak",
        "accuracy_range": (0.20, 0.50),
        "response_time_range": (35.0, 90.0),
        "hint_prob_range": (0.65, 0.88),
        "answer_changed_range": (3, 7),
        "attempts_range": (15, 35),
        "completion_ratio": 0.08,
        "study_days_back": 60,
    },
    {
        "level": "beginner",
        "tier": "mid",
        "accuracy_range": (0.35, 0.62),   # overlap qua 0.6
        "response_time_range": (28.0, 65.0),
        "hint_prob_range": (0.50, 0.72),
        "answer_changed_range": (2, 5),
        "attempts_range": (20, 45),
        "completion_ratio": 0.15,
        "study_days_back": 45,
    },
    {
        "level": "beginner",
        "tier": "struggling",     # học lâu nhưng không tiến bộ, rt cao
        "accuracy_range": (0.30, 0.58),
        "response_time_range": (40.0, 100.0),
        "hint_prob_range": (0.60, 0.85),
        "answer_changed_range": (3, 8),
        "attempts_range": (30, 60),
        "completion_ratio": 0.10,
        "study_days_back": 90,
    },
    # ── INTERMEDIATE ──────────────────────────────────────────────────────
    # Phần lớn 0.6–0.8, nhưng ~15% < 0.6 hoặc > 0.8
    {
        "level": "intermediate",
        "tier": "weak",
        "accuracy_range": (0.52, 0.68),   # overlap dưới 0.6
        "response_time_range": (20.0, 45.0),
        "hint_prob_range": (0.32, 0.55),
        "answer_changed_range": (1, 4),
        "attempts_range": (25, 50),
        "completion_ratio": 0.25,
        "study_days_back": 45,
    },
    {
        "level": "intermediate",
        "tier": "mid",
        "accuracy_range": (0.60, 0.76),
        "response_time_range": (15.0, 32.0),
        "hint_prob_range": (0.22, 0.42),
        "answer_changed_range": (1, 3),
        "attempts_range": (30, 55),
        "completion_ratio": 0.35,
        "study_days_back": 30,
    },
    {
        "level": "intermediate",
        "tier": "strong",
        "accuracy_range": (0.68, 0.84),   # overlap qua 0.8
        "response_time_range": (13.0, 28.0),
        "hint_prob_range": (0.14, 0.32),
        "answer_changed_range": (0, 3),
        "attempts_range": (35, 65),
        "completion_ratio": 0.48,
        "study_days_back": 20,
    },
    # ── ADVANCED ──────────────────────────────────────────────────────────
    # Phần lớn >= 0.8, nhưng ~20% dưới ngưỡng → label intermediate
    {
        "level": "advanced",
        "tier": "weak",
        "accuracy_range": (0.72, 0.88),   # overlap dưới 0.8
        "response_time_range": (10.0, 24.0),
        "hint_prob_range": (0.08, 0.22),
        "answer_changed_range": (0, 2),
        "attempts_range": (25, 50),
        "completion_ratio": 0.45,
        "study_days_back": 30,
    },
    {
        "level": "advanced",
        "tier": "mid",
        "accuracy_range": (0.80, 0.92),
        "response_time_range": (8.0, 18.0),
        "hint_prob_range": (0.04, 0.14),
        "answer_changed_range": (0, 1),
        "attempts_range": (30, 60),
        "completion_ratio": 0.60,
        "study_days_back": 20,
    },
    {
        "level": "advanced",
        "tier": "elite",
        "accuracy_range": (0.86, 0.97),
        "response_time_range": (5.0, 13.0),
        "hint_prob_range": (0.01, 0.07),
        "answer_changed_range": (0, 1),
        "attempts_range": (35, 70),
        "completion_ratio": 0.75,
        "study_days_back": 14,
    },
]

PROFILE_WEIGHTS = [0.07, 0.11, 0.06,   # beginner weak/mid/struggling
                   0.11, 0.15, 0.10,   # intermediate weak/mid/strong
                   0.11, 0.17, 0.12]   # advanced weak/mid/elite


def _fallback_user_feature(user: User) -> None:
    payload = build_feature_payload_for_user(user.id)
    acc = float(payload.get("accuracy_rate") or 0.0)
    if acc >= 0.72:
        level = UserFeature.PredictedLevel.ADVANCED
    elif acc >= 0.55:
        level = UserFeature.PredictedLevel.INTERMEDIATE
    else:
        level = UserFeature.PredictedLevel.BEGINNER
    UserFeature.objects.update_or_create(
        user=user,
        defaults={
            "avg_response_time": float(payload.get("avg_response_time") or 0.0),
            "accuracy_rate": acc,
            "hint_usage": float(payload.get("hint_usage") or 0.0),
            "consistency": float(payload.get("consistency") or 0.0),
            "predicted_level": level,
        },
    )


def _pick_profile() -> dict:
    """Chọn profile theo weighted distribution, có một ít ngẫu nhiên."""
    return random.choices(PROFILES, weights=PROFILE_WEIGHTS, k=1)[0]


class Command(BaseCommand):
    help = "Sinh user giả (mặc định 500) với QuestionAttempt đa dạng để train ML model."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=500, help="Số user cần tạo (mặc định 500)")
        parser.add_argument("--password", default="Test1234!", help="Mật khẩu chung (mặc định Test1234!)")
        parser.add_argument("--no-logs", action="store_true", help="Không tạo BehaviorLog")
        parser.add_argument("--batch", type=int, default=100, help="In tiến độ mỗi N user (mặc định 100)")

    def handle(self, *args, **options):
        out = getattr(self.stdout, "stream", self.stdout)
        if hasattr(out, "reconfigure"):
            try:
                out.reconfigure(encoding="utf-8")
            except Exception:
                try:
                    sys.stdout.reconfigure(encoding="utf-8")
                except Exception:
                    pass

        if fake is None:
            self.stdout.write(self.style.ERROR("Thiếu thư viện Faker. Chạy: pip install faker"))
            return

        count = options["count"]
        password = options["password"]
        no_logs = options["no_logs"]
        batch_size = options["batch"]
        now = timezone.now()

        courses = list(Course.objects.filter(is_active=True).order_by("id"))
        if not courses:
            self.stdout.write(self.style.ERROR("Không có khóa học. Chạy import_course_json trước."))
            return

        all_questions = list(
            Question.objects.filter(lesson__course__in=courses).select_related("lesson")
        )
        if not all_questions:
            self.stdout.write(self.style.ERROR("Không có câu hỏi trong DB."))
            return

        pick_courses = courses[: min(8, len(courses))]
        pool_questions = [q for q in all_questions if q.lesson.course in pick_courses] or all_questions

        # Nhóm câu hỏi theo lesson để trải đều khi lấy mẫu
        questions_by_lesson: dict[int, list] = {}
        for q in pool_questions:
            questions_by_lesson.setdefault(q.lesson_id, []).append(q)
        lesson_ids = list(questions_by_lesson.keys())

        self.stdout.write(f"Bắt đầu tạo {count} user giả ({len(pool_questions)} câu hỏi, {len(lesson_ids)} bài học)...")

        created_count = 0
        skipped_count = 0
        level_counts: dict[str, int] = {"beginner": 0, "intermediate": 0, "advanced": 0}

        for i in range(count):
            profile = _pick_profile()
            level = profile["level"]
            accuracy_target = random.uniform(*profile["accuracy_range"])
            hint_prob = random.uniform(*profile["hint_prob_range"])

            username = f"fake_{i:05d}"
            email = f"fake_{level[:3]}_{i:05d}@fake.local"
            # Idempotent: username là khóa deterministic theo i, email thì phụ
            # thuộc level (random mỗi lần chạy) nên phải check theo username.
            if User.objects.filter(username=username).exists():
                skipped_count += 1
                continue

            with transaction.atomic():
                user = User.objects.create(
                    email=email,
                    username=username,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    role=User.Role.STUDENT,
                )
                user.set_password(password)
                user.save()

                # Enroll 1–4 courses (advanced học nhiều hơn)
                max_enroll = 4 if level == "advanced" else (3 if level == "intermediate" else 2)
                enrolled = random.sample(pick_courses, k=min(random.randint(1, max_enroll), len(pick_courses)))
                for c in enrolled:
                    Enrollment.objects.get_or_create(user=user, course=c)

                # Chọn câu hỏi trải đều theo lesson (thực tế hơn)
                n_attempts = min(len(pool_questions), random.randint(*profile["attempts_range"]))
                n_lessons_to_pick = min(len(lesson_ids), max(3, n_attempts // 8))
                picked_lesson_ids = random.sample(lesson_ids, k=n_lessons_to_pick)

                sampled: list = []
                per_lesson = max(1, n_attempts // n_lessons_to_pick)
                for lid in picked_lesson_ids:
                    pool = questions_by_lesson[lid]
                    take = min(len(pool), per_lesson + random.randint(-1, 2))
                    sampled.extend(random.sample(pool, k=max(1, take)))
                sampled = sampled[:n_attempts]

                # Tạo study timeline ngẫu nhiên trong window
                study_window = profile["study_days_back"]
                start_day = random.randint(study_window // 2, study_window)

                attempts_to_create = []
                for attempt_no, question in enumerate(sampled, start=1):
                    # Noise lớn hơn (±0.18) để aggregated accuracy có variance,
                    # tránh tất cả user converge đúng target → accuracy=1.0 khi train
                    noise = random.gauss(0, 0.18)
                    is_correct = random.random() < min(0.97, max(0.03, accuracy_target + noise))
                    ua = question.answer if is_correct else random.choice(["A", "B", "C", "D"])
                    rt = round(random.uniform(*profile["response_time_range"]), 2)
                    # Thêm noise nhỏ vào response_time để tăng variance (giúp consistency feature)
                    rt = max(2.0, rt + random.gauss(0, rt * 0.15))
                    day_offset = random.randint(0, start_day)
                    attempts_to_create.append(QuestionAttempt(
                        user=user,
                        question=question,
                        user_answer=ua,
                        is_correct=is_correct,
                        response_time_seconds=round(rt, 2),
                        answer_changed_count=random.randint(*profile["answer_changed_range"]),
                        hint_used=random.random() < hint_prob,
                        attempt_num=attempt_no,
                        created_at=now - timedelta(days=day_offset),
                    ))
                QuestionAttempt.objects.bulk_create(attempts_to_create)

                # Hoàn thành một số lesson theo completion_ratio
                lessons_touched = {q.lesson_id: q.lesson for q in sampled}
                n_complete = max(0, int(len(lessons_touched) * profile["completion_ratio"]))
                lesson_progress_to_save = []
                for lid, lesson in list(lessons_touched.items())[:n_complete]:
                    if lesson.course not in enrolled:
                        continue
                    completed_at = now - timedelta(days=random.randint(0, start_day))
                    started_at = completed_at - timedelta(minutes=random.randint(15, 60))
                    lp, _ = LessonProgress.objects.get_or_create(
                        user=user,
                        lesson=lesson,
                        defaults={"started_at": started_at},
                    )
                    lp.score = round(random.uniform(40.0 + accuracy_target * 50, 99.0), 1)
                    lp.time_spent = random.randint(200, 3000)
                    lp.completed_at = completed_at
                    if lp.started_at is None:
                        lp.started_at = started_at
                    lp.save()

                # Cập nhật enrollment progress
                for c in enrolled:
                    total_l = Lesson.objects.filter(course=c).count()
                    done_l = LessonProgress.objects.filter(
                        user=user, lesson__course=c, completed_at__isnull=False
                    ).count()
                    ratio = (done_l / total_l) if total_l else 0.0
                    Enrollment.objects.filter(user=user, course=c).update(
                        progress=round(ratio, 4), completed=ratio >= 1.0
                    )

                if not no_logs:
                    BehaviorLog.objects.create(
                        user=user,
                        event_type="quiz_attempt",
                        event_data={"level": level, "tier": profile["tier"], "source": "seed_fake_users"},
                        session_id=f"fake-seed-{user.id}",
                    )

                _fallback_user_feature(user)

            created_count += 1
            level_counts[level] += 1

            if created_count % batch_size == 0:
                self.stdout.write(f"  → {created_count}/{count} user đã tạo...")

        self.stdout.write(self.style.SUCCESS(
            f"\nHoàn thành: {created_count} user mới, {skipped_count} bỏ qua (đã tồn tại)."
        ))
        self.stdout.write(
            f"  Phân phối: beginner={level_counts['beginner']}  "
            f"intermediate={level_counts['intermediate']}  "
            f"advanced={level_counts['advanced']}"
        )
        self.stdout.write(self.style.WARNING("\nBước tiếp theo: python manage.py train_level_model"))
