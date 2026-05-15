"""
Integration tests khớp với API thực tế (tài liệu §2.10.2).
Chạy: pytest từ thư mục backend (SQLite khi không set DATABASE_URL).
"""

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

pytestmark = pytest.mark.django_db


@pytest.fixture
def api():
    return APIClient()


def test_public_courses_list(api):
    response = api.get("/api/v1/public/courses/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_register_login_me_flow(api):
    payload = {
        "email": "pytest_user@example.com",
        "username": "pytestuser",
        "password": "testpass12",
        "first_name": "Py",
        "last_name": "Test",
    }
    r = api.post("/api/v1/auth/register/", payload, format="json")
    assert r.status_code == 201

    r = api.post(
        "/api/v1/auth/login/",
        {"email": payload["email"], "password": payload["password"]},
        format="json",
    )
    assert r.status_code == 200
    body = r.json()
    assert "access" in body
    access = body["access"]

    api.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
    r = api.get("/api/v1/auth/me/")
    assert r.status_code == 200
    assert r.json()["email"] == payload["email"]


def test_recommendations_requires_auth(api):
    r = api.get("/api/v1/recommendations/")
    assert r.status_code == 401


def test_submit_answer_requires_auth_and_body(api):
    r = api.post("/api/v1/learning/submit-answer/", {}, format="json")
    assert r.status_code == 401


def test_admin_dashboard_requires_admin(api):
    user = User.objects.create_user(
        email="student_only@example.com",
        username="studentonly",
        password="testpass12",
    )
    assert user.role == "student"
    r = api.post(
        "/api/v1/auth/login/",
        {"email": "student_only@example.com", "password": "testpass12"},
        format="json",
    )
    access = r.json()["access"]
    api.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
    r = api.get("/api/v1/dashboard/admin/")
    assert r.status_code == 403
