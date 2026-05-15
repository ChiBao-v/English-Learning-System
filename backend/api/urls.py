from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import FlexibleTokenObtainPairSerializer
from .views import (
    AdminDashboardView,
    ChangePasswordView,
    CompleteLessonView,
    MLFeatureDistributionView,
    MLModelStatusView,
    MLRetrainView,
    CourseViewSet,
    EnrollCourseView,
    LessonDetailView,
    LessonQuestionsView,
    LessonViewSet,
    MeView,
    PublicCourseListView,
    QuestionViewSet,
    RecommendationView,
    RegisterView,
    StudentDashboardView,
    SubmitAnswerView,
    UpdateProfileView,
    api_root,
)

router = DefaultRouter()
router.register("courses", CourseViewSet, basename="course")
router.register("lessons", LessonViewSet, basename="lesson")
router.register("questions", QuestionViewSet, basename="question")

urlpatterns = [
    path("public/courses/", PublicCourseListView.as_view(), name="public-courses"),
    path("dashboard/student/", StudentDashboardView.as_view(), name="dashboard-student"),
    path("dashboard/admin/", AdminDashboardView.as_view(), name="dashboard-admin"),
    path("ml/feature-distribution/", MLFeatureDistributionView.as_view(), name="ml-feature-distribution"),
    path("ml/model-status/", MLModelStatusView.as_view(), name="ml-model-status"),
    path("ml/retrain/", MLRetrainView.as_view(), name="ml-retrain"),
    path("auth/register/", RegisterView.as_view(), name="auth-register"),
    path(
        "auth/login/",
        TokenObtainPairView.as_view(serializer_class=FlexibleTokenObtainPairSerializer),
        name="auth-login",
    ),
    path("auth/refresh/", TokenRefreshView.as_view(), name="auth-refresh"),
    path("auth/me/", MeView.as_view(), name="auth-me"),
    path("auth/change-password/", ChangePasswordView.as_view(), name="auth-change-password"),
    path("auth/update-profile/", UpdateProfileView.as_view(), name="auth-update-profile"),
    path("learning/enroll/", EnrollCourseView.as_view(), name="learning-enroll"),
    path(
        "learning/lessons/<int:lesson_id>/",
        LessonDetailView.as_view(),
        name="learning-lesson-detail",
    ),
    path(
        "learning/lessons/<int:lesson_id>/questions/",
        LessonQuestionsView.as_view(),
        name="learning-lesson-questions",
    ),
    path("learning/submit-answer/", SubmitAnswerView.as_view(), name="learning-submit-answer"),
    path(
        "learning/complete-lesson/",
        CompleteLessonView.as_view(),
        name="learning-complete-lesson",
    ),
    path("recommendations/", RecommendationView.as_view(), name="recommendations"),
    # api_root phải đứng TRƯỚC router: DefaultRouter cũng tạo một APIRootView ở
    # path("") nhưng chỉ liệt kê 3 viewset đã register. Đặt api_root trước để
    # /api/v1/ hiển thị danh sách ĐẦY ĐỦ endpoint (auth, learning, ml, ...).
    path("", api_root, name="api-root"),
    path("", include(router.urls)),
]
