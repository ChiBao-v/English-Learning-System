"""Hiển thị khóa học công khai: chuẩn hoá tên/ cấp độ cho API."""

from __future__ import annotations

import re

# Khóa C01 — tên đầy đủ (tránh card trang chủ còn nhãn band TOEIC cũ trong DB)
CANONICAL_COURSE_TITLES = {
    "C01": "Foundation English — Tiếng Anh Nền Tảng (A1)",
    "C02": "Daily Life & Surroundings — Đời sống & Môi trường (A1+)",
    "C03": "Expanding Horizons — Mở rộng địa hình (Pre-Intermediate A2)",
    "C04": "Practical Office Communication — Giao tiếp công sở (Intermediate B1)",
    "C05": "English for International Travel — Tiếng Anh du lịch quốc tế (B1)",
    "C06": "Customer Service & F&B — Dịch vụ khách hàng & Nhà hàng (B1)",
}

LEVEL_LABEL_VI = {
    "beginner": "Cơ bản",
    "intermediate": "Trung cấp",
    "advanced": "Nâng cao",
}


def resolve_public_course_title(course) -> str:
    """Ưu tiên tên chuẩn theo mã khóa; sửa legacy chỉ hiển thị band TOEIC."""
    ext = getattr(course, "external_id", None) or ""
    ext = ext.strip()
    if ext in CANONICAL_COURSE_TITLES:
        return CANONICAL_COURSE_TITLES[ext]
    raw = (course.title or "").strip()
    if re.match(r"^TOEIC\s*\d+\+?\s*$", raw, re.IGNORECASE):
        return CANONICAL_COURSE_TITLES.get("C01", raw)
    return raw


def level_label_vi(level: str) -> str:
    return LEVEL_LABEL_VI.get(level or "", level or "")
