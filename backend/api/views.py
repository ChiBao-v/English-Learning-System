from datetime import timedelta
from io import StringIO

from django.core.management import call_command
from django.core.management.base import CommandError
from django.db.models import Avg, Case, Count, FloatField, Sum, Value, When
from django.db.models.functions import TruncDate
from django.utils import timezone
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from courses.models import Course, Lesson, Question
from learning.models import BehaviorLog, Enrollment, LessonProgress, QuestionAttempt
from ml.models import MLModel, Recommendation, UserFeature
from ml.service import generate_recommendations_for_user
from users.models import User

from .permissions import IsAdminOrReadOnly, IsAdminRole, IsStaffMLRole
from .serializers import (
    CompleteLessonSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    LessonDetailSerializer,
    LessonProgressSerializer,
    LessonSerializer,
    PublicCourseSerializer,
    QuestionAttemptResultSerializer,
    QuestionSerializer,
    RecommendationSerializer,
    RegisterSerializer,
    SubmitAnswerSerializer,
    UserMeSerializer,
)


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer])
def api_root(request, format=None):
    """
    API Root — trang tổng quan toàn bộ endpoint.

    - Mở bằng trình duyệt (HTML)  → render templates/api_root.html (cards trực quan).
    - ?format=json hoặc API client → trả về dict URL thuần.

    Dùng TemplateHTMLRenderer với template RIÊNG nên KHÔNG ảnh hưởng tới
    browsable API của các endpoint khác (/courses/, /lessons/, ...).
    """
    endpoints = {
        'courses': reverse('course-list', request=request),
        'lessons': reverse('lesson-list', request=request),
        'questions': reverse('question-list', request=request),
        'public_courses': reverse('public-courses', request=request),
        'dashboard_student': reverse('dashboard-student', request=request),
        'dashboard_admin': reverse('dashboard-admin', request=request),
        'auth': {
            'register': reverse('auth-register', request=request),
            'login': reverse('auth-login', request=request),
            'refresh': reverse('auth-refresh', request=request),
            'me': reverse('auth-me', request=request),
            'change_password': reverse('auth-change-password', request=request),
            'update_profile': reverse('auth-update-profile', request=request),
        },
        'learning': {
            'enroll': reverse('learning-enroll', request=request),
            'submit_answer': reverse('learning-submit-answer', request=request),
            'complete_lesson': reverse('learning-complete-lesson', request=request),
        },
        'ml': {
            'model_status': reverse('ml-model-status', request=request),
            'feature_distribution': reverse('ml-feature-distribution', request=request),
            'retrain': reverse('ml-retrain', request=request),
        },
        'recommendations': reverse('recommendations', request=request),
    }
    if request.accepted_renderer.format == 'json':
        return Response(endpoints)
    return Response(endpoints, template_name='api_root.html')


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserMeSerializer(request.user)
        return Response(serializer.data)


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        user.first_name = request.data.get("first_name", user.first_name)
        user.last_name = request.data.get("last_name", user.last_name)
        user.username = request.data.get("username", user.username)
        user.save(update_fields=["first_name", "last_name", "username"])
        return Response(UserMeSerializer(user).data)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        old_password = request.data.get("old_password", "")
        new_password = request.data.get("new_password", "")
        if not old_password or not new_password:
            raise ValidationError({"detail": "old_password và new_password là bắt buộc."})
        if not request.user.check_password(old_password):
            raise ValidationError({"detail": "Mật khẩu hiện tại không đúng."})
        if len(new_password) < 8:
            raise ValidationError({"detail": "Mật khẩu mới phải có ít nhất 8 ký tự."})
        request.user.set_password(new_password)
        request.user.save()
        return Response({"detail": "Đổi mật khẩu thành công."})


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("id")
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related("course").all().order_by("course_id", "order_num")
    serializer_class = LessonSerializer
    permission_classes = [IsAdminOrReadOnly]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.select_related("lesson").all().order_by("lesson_id", "id")
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly]


class EnrollCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EnrollmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = serializer.validated_data["course"]
        enrollment, created = Enrollment.objects.get_or_create(
            user=request.user,
            course=course,
        )
        if not created:
            return Response(
                {"detail": "Already enrolled in this course."},
                status=status.HTTP_200_OK,
            )
        return Response(
            EnrollmentSerializer(enrollment).data,
            status=status.HTTP_201_CREATED,
        )


class LessonDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, lesson_id):
        lesson = Lesson.objects.select_related("course").prefetch_related("questions").filter(id=lesson_id).first()
        if not lesson:
            raise ValidationError({"lesson_id": "Lesson does not exist."})

        is_enrolled = Enrollment.objects.filter(
            user=request.user, course=lesson.course
        ).exists()
        if not is_enrolled:
            raise PermissionDenied("You must enroll in this course first.")

        progress, _ = LessonProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
            defaults={"started_at": timezone.now()},
        )
        if progress.started_at is None:
            progress.started_at = timezone.now()
            progress.save(update_fields=["started_at"])

        completed_ids = set(
            LessonProgress.objects.filter(
                user=request.user,
                lesson__course_id=lesson.course_id,
                completed_at__isnull=False,
            ).values_list("lesson_id", flat=True)
        )
        course_lessons = Lesson.objects.filter(course=lesson.course).order_by("order_num", "id")
        course_lessons_payload = [
            {
                "id": row.id,
                "title": row.title,
                "order_num": row.order_num,
                "completed": row.id in completed_ids,
            }
            for row in course_lessons
        ]

        return Response(
            {
                "lesson": LessonDetailSerializer(lesson).data,
                "progress": LessonProgressSerializer(progress).data,
                "course_lessons": course_lessons_payload,
            }
        )


class LessonQuestionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, lesson_id):
        lesson = Lesson.objects.select_related("course").prefetch_related("questions").filter(id=lesson_id).first()
        if not lesson:
            raise ValidationError({"lesson_id": "Lesson does not exist."})

        is_enrolled = Enrollment.objects.filter(
            user=request.user, course=lesson.course
        ).exists()
        if not is_enrolled:
            raise PermissionDenied("You must enroll in this course first.")

        questions = lesson.questions.all()
        return Response(QuestionSerializer(questions, many=True).data)


class SubmitAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SubmitAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        question = Question.objects.select_related("lesson", "lesson__course").filter(
            id=data["question_id"]
        ).first()
        if not question:
            raise ValidationError({"question_id": "Question does not exist."})

        is_enrolled = Enrollment.objects.filter(
            user=request.user, course=question.lesson.course
        ).exists()
        if not is_enrolled:
            raise PermissionDenied("You must enroll in this course first.")

        is_correct = data["user_answer"].strip().lower() == question.answer.strip().lower()
        attempt = QuestionAttempt.objects.create(
            user=request.user,
            question=question,
            user_answer=data["user_answer"],
            is_correct=is_correct,
            response_time_seconds=data["response_time_seconds"],
            answer_changed_count=data["answer_changed_count"],
            hint_used=data["hint_used"],
            attempt_num=data["attempt_num"],
        )

        progress, _ = LessonProgress.objects.get_or_create(
            user=request.user,
            lesson=question.lesson,
            defaults={"started_at": timezone.now()},
        )
        if progress.started_at is None:
            progress.started_at = timezone.now()
            progress.save(update_fields=["started_at"])

        BehaviorLog.objects.create(
            user=request.user,
            event_type="quiz_attempt",
            event_data={
                "question_id": question.id,
                "lesson_id": question.lesson_id,
                "course_id": question.lesson.course_id,
                "is_correct": is_correct,
                "response_time_seconds": data["response_time_seconds"],
                "answer_changed_count": data["answer_changed_count"],
                "hint_used": data["hint_used"],
                "attempt_num": data["attempt_num"],
            },
            session_id=request.headers.get("X-Session-ID", ""),
        )

        return Response(
            {
                "attempt": QuestionAttemptResultSerializer(attempt).data,
                "is_correct": is_correct,
            },
            status=status.HTTP_201_CREATED,
        )


class CompleteLessonView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CompleteLessonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        lesson = Lesson.objects.select_related("course").filter(id=data["lesson_id"]).first()
        if not lesson:
            raise ValidationError({"lesson_id": "Lesson does not exist."})

        is_enrolled = Enrollment.objects.filter(
            user=request.user, course=lesson.course
        ).exists()
        if not is_enrolled:
            raise PermissionDenied("You must enroll in this course first.")

        progress, _ = LessonProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
            defaults={"started_at": timezone.now()},
        )
        progress.score = data["score"]
        progress.time_spent = data["time_spent"]
        progress.completed_at = timezone.now()
        progress.save(update_fields=["score", "time_spent", "completed_at", "started_at"])

        course_lessons_count = Lesson.objects.filter(course=lesson.course).count()
        completed_lessons_count = LessonProgress.objects.filter(
            user=request.user,
            lesson__course=lesson.course,
            completed_at__isnull=False,
        ).count()
        progress_ratio = (
            (completed_lessons_count / course_lessons_count) if course_lessons_count > 0 else 0
        )
        Enrollment.objects.filter(user=request.user, course=lesson.course).update(
            progress=progress_ratio,
            completed=progress_ratio >= 1.0,
        )

        avg_score = (
            LessonProgress.objects.filter(
                user=request.user,
                lesson__course=lesson.course,
                completed_at__isnull=False,
            ).aggregate(avg=Avg("score"))["avg"]
            or 0
        )

        BehaviorLog.objects.create(
            user=request.user,
            event_type="lesson_completed",
            event_data={
                "lesson_id": lesson.id,
                "course_id": lesson.course_id,
                "score": data["score"],
                "time_spent": data["time_spent"],
                "course_progress": progress_ratio,
                "course_avg_score": avg_score,
            },
            session_id=request.headers.get("X-Session-ID", ""),
        )

        return Response(
            {
                "detail": "Lesson completed.",
                "progress": LessonProgressSerializer(progress).data,
                "course_progress": progress_ratio,
            }
        )


class RecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = generate_recommendations_for_user(request.user.id, top_n=5)
        queryset = Recommendation.objects.select_related("lesson__course").filter(user=request.user)[:5]
        return Response(
            {
                "predicted_level": result["predicted_level"],
                "weak_skills": result["weak_skills"],
                "recommendations": RecommendationSerializer(queryset, many=True).data,
            }
        )


class PublicCourseListView(generics.ListAPIView):
    """Khóa học công khai cho trang chủ (không cần đăng nhập)."""

    permission_classes = []
    serializer_class = PublicCourseSerializer

    def get_queryset(self):
        return (
            Course.objects.filter(is_active=True)
            .annotate(lesson_count=Count("lessons", distinct=True))
            .order_by("id")
        )


class StudentDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        enrollments = Enrollment.objects.filter(user=user).select_related("course")
        enrolled_count = enrollments.count()

        total_seconds = (
            LessonProgress.objects.filter(user=user).aggregate(s=Sum("time_spent"))["s"] or 0
        )

        attempts = QuestionAttempt.objects.filter(user=user)
        acc = attempts.aggregate(
            acc=Avg(
                Case(
                    When(is_correct=True, then=Value(1.0)),
                    default=Value(0.0),
                    output_field=FloatField(),
                )
            )
        )["acc"]
        accuracy_pct = round(float(acc or 0.0) * 100, 1)
        completed_lessons_count = LessonProgress.objects.filter(
            user=user, completed_at__isnull=False
        ).count()

        course_progress = [
            {
                "course_id": e.course_id,
                "title": e.course.title,
                "progress_pct": round(float(e.progress) * 100, 1),
            }
            for e in enrollments
        ]

        # Bài đầu tiên chưa hoàn thành theo thứ tự (để nút "Tiếp tục học").
        resume_lesson_by_course = {}
        for e in enrollments:
            cid = e.course_id
            lessons_qs = Lesson.objects.filter(course_id=cid).order_by("order_num", "id")
            done_ids = set(
                LessonProgress.objects.filter(
                    user=user,
                    lesson__course_id=cid,
                    completed_at__isnull=False,
                ).values_list("lesson_id", flat=True)
            )
            resume_id = None
            for les in lessons_qs:
                if les.id not in done_ids:
                    resume_id = les.id
                    break
            resume_lesson_by_course[cid] = resume_id

        completed_lesson_ids = LessonProgress.objects.filter(
            user=user,
            completed_at__isnull=False,
        ).values_list("lesson_id", flat=True)

        skill_rows = (
            attempts.filter(question__lesson_id__in=completed_lesson_ids)
            .values("question__skill_type")
            .annotate(
                acc=Avg(
                    Case(
                        When(is_correct=True, then=Value(1.0)),
                        default=Value(0.0),
                        output_field=FloatField(),
                    )
                )
            )
        )
        skill_pct = {}
        for row in skill_rows:
            st = row.get("question__skill_type") or "unknown"
            skill_pct[st] = round(float(row.get("acc") or 0.0) * 100, 1)

        return Response(
            {
                "kpis": {
                    "enrolled_courses": enrolled_count,
                    "total_study_seconds": int(total_seconds),
                    "accuracy_pct": accuracy_pct,
                    "completed_lessons": completed_lessons_count,
                },
                "course_progress": course_progress,
                "resume_lesson_by_course": resume_lesson_by_course,
                "skill_pct": skill_pct,
            }
        )


def _behavior_log_summary(log: BehaviorLog) -> str:
    if log.event_type == "lesson_completed":
        lid = (log.event_data or {}).get("lesson_id")
        return f"Hoàn thành bài học #{lid}" if lid is not None else "Hoàn thành bài học"
    if log.event_type == "quiz_attempt":
        return "Làm câu hỏi (quiz)"
    return log.event_type


class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsStaffMLRole]

    def get(self, request):
        now = timezone.now()
        week_start = now - timedelta(days=7)

        total_users = User.objects.count()
        total_courses = Course.objects.count()
        total_lessons = Lesson.objects.count()

        today = now.date()
        active_today = (
            BehaviorLog.objects.filter(timestamp__date=today)
            .values("user")
            .distinct()
            .count()
        )

        daily = (
            BehaviorLog.objects.filter(timestamp__gte=week_start)
            .annotate(day=TruncDate("timestamp"))
            .values("day")
            .annotate(count=Count("id"))
            .order_by("day")
        )
        activity_last_7_days = [
            {"day": row["day"].isoformat() if row["day"] else None, "count": row["count"]}
            for row in daily
        ]

        recent_logs = []
        for log in BehaviorLog.objects.select_related("user").order_by("-timestamp")[:10]:
            recent_logs.append(
                {
                    "user_email": log.user.email,
                    "event_type": log.event_type,
                    "timestamp": log.timestamp.isoformat(),
                    "summary": _behavior_log_summary(log),
                }
            )

        ml = MLModel.objects.filter(name="level_predictor", is_active=True).order_by("-created_at").first()
        ml_payload = None
        if ml:
            acc = ml.metrics.get("accuracy") if ml.metrics else None
            ml_payload = {
                "name": ml.name,
                "version": ml.version,
                "is_active": ml.is_active,
                "accuracy_pct": round(float(acc) * 100, 2) if acc is not None else None,
                "last_trained": ml.created_at.isoformat(),
            }

        return Response(
            {
                "overview": {
                    "total_users": total_users,
                    "total_courses": total_courses,
                    "total_lessons": total_lessons,
                    "active_today": active_today,
                },
                "activity_last_7_days": activity_last_7_days,
                "recent_logs": recent_logs,
                "ml_model": ml_payload,
            }
        )


class MLModelStatusView(APIView):
    """Trạng thái model active + lịch sử N version gần nhất — Admin / Data Scientist."""

    permission_classes = [IsAuthenticated, IsStaffMLRole]

    def get(self, request):
        active = (
            MLModel.objects.filter(name="level_predictor", is_active=True)
            .order_by("-created_at")
            .first()
        )
        active_payload = None
        if active:
            metrics = active.metrics or {}
            accuracy = metrics.get("accuracy")
            f1 = metrics.get("f1_macro")
            active_payload = {
                "id": active.id,
                "name": active.name,
                "version": active.version,
                "accuracy": float(accuracy) if accuracy is not None else None,
                "accuracy_pct": round(float(accuracy) * 100, 2) if accuracy is not None else None,
                "f1_macro": float(f1) if f1 is not None else None,
                "model_path": active.model_path,
                "is_active": active.is_active,
                "created_at": active.created_at.isoformat(),
            }

        history = [
            {
                "id": m.id,
                "version": m.version,
                "is_active": m.is_active,
                "accuracy": float((m.metrics or {}).get("accuracy") or 0.0) or None,
                "f1_macro": float((m.metrics or {}).get("f1_macro") or 0.0) or None,
                "created_at": m.created_at.isoformat(),
            }
            for m in MLModel.objects.filter(name="level_predictor").order_by("-created_at")[:10]
        ]

        return Response({"active": active_payload, "history": history})


class MLRetrainView(APIView):
    """Trigger retrain model qua management command `train_level_model` — Admin / DS."""

    permission_classes = [IsAuthenticated, IsStaffMLRole]

    def post(self, request):
        out = StringIO()
        try:
            call_command("train_level_model", stdout=out, stderr=out)
        except CommandError as exc:
            return Response(
                {"detail": str(exc), "log": out.getvalue()},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as exc:  # noqa: BLE001 — bao trùm để không 500 silent
            return Response(
                {"detail": f"Retrain failed: {exc}", "log": out.getvalue()},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        active = (
            MLModel.objects.filter(name="level_predictor", is_active=True)
            .order_by("-created_at")
            .first()
        )
        return Response(
            {
                "detail": "Retrain completed.",
                "log": out.getvalue(),
                "active_version": active.version if active else None,
                "metrics": active.metrics if active else {},
            },
            status=status.HTTP_201_CREATED,
        )


class MLFeatureDistributionView(APIView):
    """Thống kê phân phối feature đã lưu (UserFeature) — Data Scientist / Admin."""

    permission_classes = [IsAuthenticated, IsStaffMLRole]

    def get(self, request):
        qs = UserFeature.objects.all()
        n = qs.count()
        if not n:
            return Response(
                {
                    "user_feature_count": 0,
                    "predicted_level_counts": [],
                    "averages": {},
                }
            )

        averages = qs.aggregate(
            avg_response_time=Avg("avg_response_time"),
            avg_accuracy_rate=Avg("accuracy_rate"),
            avg_hint_usage=Avg("hint_usage"),
            avg_consistency=Avg("consistency"),
        )
        level_rows = (
            qs.values("predicted_level").annotate(count=Count("id")).order_by("predicted_level")
        )
        predicted_level_counts = [
            {"level": row["predicted_level"], "count": row["count"]} for row in level_rows
        ]

        return Response(
            {
                "user_feature_count": n,
                "predicted_level_counts": predicted_level_counts,
                "averages": {k: round(float(v or 0), 4) for k, v in averages.items()},
            }
        )
