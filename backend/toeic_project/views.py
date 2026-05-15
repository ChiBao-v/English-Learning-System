"""Trang gốc: không phải SPA — chỉ thông báo API."""

from django.http import JsonResponse


def api_root(request):
    return JsonResponse(
        {
            "service": "TOEIC/E-learning API",
            "admin": "/admin/",
            "api": "/api/v1/",
            "hint": "Frontend dev: Ví dụ Vite tại http://127.0.0.1:5173",
        }
    )
