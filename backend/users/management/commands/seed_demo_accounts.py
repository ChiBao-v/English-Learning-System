"""
Tạo học viên demo có tên + mật khẩu cố định, gắn dữ liệu sử dụng thật (đăng ký khóa,
làm câu hỏi, tiến độ bài, behavior log, UserFeature / gợi ý khi có model).

Chạy sau import_course_json (hoặc khi DB đã có khóa học + câu hỏi).
"""

from __future__ import annotations

import random
import sys
from datetime import timedelta

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from courses.models import Course, Lesson, Question
from learning.models import BehaviorLog, Enrollment, LessonProgress, QuestionAttempt
from ml.models import UserFeature
from ml.service import build_feature_payload_for_user, generate_recommendations_for_user
from users.models import User

# Đăng nhập SPA: email + mật khẩu (role student)
DEMO_STUDENTS = [
    ("nguyen.van.minh@demo.local", "minhnv", "Nguyễn Văn", "Minh"),
    ("tran.thi.huong@demo.local", "huongtt", "Trần Thị", "Hương"),
    ("le.quoc.anh@demo.local", "anhlq", "Lê Quốc", "Anh"),
    ("pham.thi.mai@demo.local", "maipt", "Phạm Thị", "Mai"),
    ("hoang.duc.tien@demo.local", "tienhd", "Hoàng Đức", "Tiến"),
    ("vo.thi.lan@demo.local", "lanvt", "Võ Thị", "Lan"),
    ("dang.minh.khoi@demo.local", "khoidm", "Đặng Minh", "Khôi"),
    ("bui.thi.ngoc@demo.local", "ngocbt", "Bùi Thị", "Ngọc"),
]


def _ensure_min_courses() -> list[Course]:
    """Nếu DB chưa có khóa học, tạo tối thiểu để demo."""
    if Course.objects.exists():
        return list(Course.objects.filter(is_active=True).order_by("id"))

    courses_data = [
        (
            "Demo — Tiếng Anh giao tiếp (A1–A2)",
            "beginner",
            "Khóa mẫu: chào hỏi, giới thiệu, đặt câu hỏi đơn giản.",
        ),
        (
            "Demo — TOEIC Listening nền tảng",
            "intermediate",
            "Khóa mẫu: mô tả tranh, hội thoại ngắn, câu hỏi lựa chọn.",
        ),
    ]
    created: list[Course] = []
    for title, level, desc in courses_data:
        c = Course.objects.create(title=title, description=desc, level=level, is_active=True)
        created.append(c)
        for order in range(1, 4):
            lesson = Lesson.objects.create(
                course=c,
                order_num=order,
                title=f"Unit {order}: Thực hành {title[:24]}",
                content="Nội dung bài học demo — đọc nghe và làm bài trắc nghiệm.",
                duration=20 + order * 5,
            )
            for q in range(1, 5):
                skill = ["listening", "reading", "grammar", "vocabulary"][(order + q) % 4]
                Question.objects.create(
                    lesson=lesson,
                    content=f"[{skill.upper()}] Chọn đáp án đúng (Unit {order}, Q{q})",
                    question_type=Question.Type.MULTIPLE_CHOICE,
                    options=[
                        "A. Đáp án phù hợp ngữ cảnh",
                        "B. Đáp án trung tính",
                        "C. Đáp án gây nhiễu",
                        "D. Đáp án sai phổ biến",
                    ],
                    answer="A",
                    difficulty=min(5, q),
                    hint="Chú ý từ khóa trong câu.",
                    skill_type=skill,
                )
    return created


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


class Command(BaseCommand):
    help = "Tạo/cập nhật học viên demo có tên, mật khẩu cố định và dữ liệu sử dụng sản phẩm."

    def add_arguments(self, parser):
        parser.add_argument(
            "--password",
            default="Demo123!",
            help="Mật khẩu chung cho các tài khoản học viên demo (mặc định: Demo123!)",
        )
        parser.add_argument(
            "--no-logs",
            action="store_true",
            help="Không tạo BehaviorLog (nhanh hơn).",
        )
        parser.add_argument("--ds-email", default="ds@demo.local")
        parser.add_argument("--ds-username", default="datascientist")
        parser.add_argument("--ds-password", default="ds123456")
        parser.add_argument("--skip-ds", action="store_true", help="Không tạo/cập nhật tài khoản Data Scientist.")

    @transaction.atomic
    def handle(self, *args, **options):
        # Tránh UnicodeEncodeError trên Windows (console cp1252).
        out = getattr(self.stdout, "stream", self.stdout)
        if hasattr(out, "reconfigure"):
            try:
                out.reconfigure(encoding="utf-8")
            except Exception:
                try:
                    sys.stdout.reconfigure(encoding="utf-8")
                except Exception:
                    pass

        password = options["password"]
        no_logs = options["no_logs"]

        courses = _ensure_min_courses()
        if not courses:
            self.stdout.write(self.style.ERROR("Không có khóa học — kiểm tra DB."))
            return

        # Ưu tiên vài khóa đầu để mọi môi trường đều có dữ liệu
        pick_courses = courses[: min(6, len(courses))]
        all_questions = list(
            Question.objects.filter(lesson__course__in=pick_courses).select_related("lesson")
        )
        if not all_questions:
            self.stdout.write(
                self.style.ERROR(
                    "Không có câu hỏi trong các khóa học. Chạy import_course_json trước hoặc để lệnh tự tạo khóa tối thiểu (DB trống)."
                )
            )
            return

        lines_out = []
        now = timezone.now()

        for email, username, first_name, last_name in DEMO_STUDENTS:
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    "username": username,
                    "first_name": first_name,
                    "last_name": last_name,
                    "role": User.Role.STUDENT,
                },
            )
            if not created:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.role = User.Role.STUDENT
            user.set_password(password)
            user.save()

            # Đăng ký 2–3 khóa
            enrolled = random.sample(pick_courses, k=min(3, len(pick_courses)))
            for c in enrolled:
                Enrollment.objects.get_or_create(user=user, course=c)

            # Làm bài: 30–90 câu tùy sẵn có
            n_attempts = min(len(all_questions), random.randint(35, 90))
            if n_attempts < 10 and all_questions:
                n_attempts = min(len(all_questions), 10)
            sampled = random.sample(all_questions, k=n_attempts) if all_questions else []

            # Độ khác nhau giữa các user (một số giỏi hơn)
            idx = DEMO_STUDENTS.index((email, username, first_name, last_name))
            acc_bias = 0.55 + (idx % 5) * 0.06

            for attempt_no, question in enumerate(sampled, start=1):
                is_correct = random.random() < min(0.92, acc_bias + random.uniform(-0.12, 0.12))
                ua = question.answer if is_correct else random.choice(["A", "B", "C", "D"])
                QuestionAttempt.objects.create(
                    user=user,
                    question=question,
                    user_answer=ua,
                    is_correct=is_correct,
                    response_time_seconds=round(random.uniform(8.0, 55.0), 2),
                    answer_changed_count=random.randint(0, 2),
                    hint_used=random.random() < 0.28,
                    attempt_num=attempt_no,
                )

            # Tiến độ: hoàn thành một vài bài
            lessons_touched = {q.lesson_id for q in sampled}
            for lid in list(lessons_touched)[: max(1, len(lessons_touched) // 3)]:
                lesson = Lesson.objects.get(pk=lid)
                lp, _ = LessonProgress.objects.get_or_create(
                    user=user,
                    lesson=lesson,
                    defaults={"started_at": now - timedelta(days=random.randint(1, 14))},
                )
                lp.score = round(random.uniform(65.0, 98.0), 1)
                lp.time_spent = random.randint(300, 2400)
                lp.completed_at = now - timedelta(hours=random.randint(1, 72))
                if lp.started_at is None:
                    lp.started_at = lp.completed_at - timedelta(minutes=30)
                lp.save()

            # Cập nhật progress enrollment theo khóa
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
                    event_data={"note": "seed_demo_accounts", "email": email},
                    session_id=f"seed-{user.id}",
                )
                BehaviorLog.objects.create(
                    user=user,
                    event_type="lesson_completed",
                    event_data={"note": "seed_demo_accounts", "email": email},
                    session_id=f"seed-{user.id}",
                )

            try:
                generate_recommendations_for_user(user.id, top_n=5)
            except Exception:
                _fallback_user_feature(user)

            lines_out.append(f"  • {email}  /  {password}  ({first_name} {last_name})")

        self.stdout.write(self.style.SUCCESS("\n=== Học viên demo (đăng nhập bằng email) ==="))
        for line in lines_out:
            self.stdout.write(line)
        self.stdout.write(
            self.style.WARNING(
                "\n(Tài khoản bulk student001@… / student123 không còn được seed tự động; dùng các email demo ở trên.)"
            )
        )

        ds_email = options["ds_email"]
        ds_password = options["ds_password"]
        if not options["skip_ds"]:
            call_command(
                "ensure_data_scientist",
                email=ds_email,
                username=options["ds_username"],
                password=ds_password,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"\n=== Data Scientist ===\n  • {ds_email}  /  {ds_password}  (vào /admin — Tổng quan và ML)\n"
                )
            )

        self.stdout.write(self.style.SUCCESS("\nXong. Đã đồng bộ UserFeature / gợi ý (hoặc fallback khi chưa train model)."))
