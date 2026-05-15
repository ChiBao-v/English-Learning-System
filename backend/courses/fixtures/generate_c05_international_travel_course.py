"""Sinh course_C05_international_travel.json — English for International Travel B1."""

from __future__ import annotations

import json
from pathlib import Path

from c05_b1_travel_lesson_builders import build_all_lessons

OUT = Path(__file__).resolve().parent / "course_C05_international_travel.json"


def main():
    data = {
        "course_id": "C05",
        "course_name": "English for International Travel (Intermediate B1)",
        "course_description": (
            "Sân bay & an ninh, nhập cảnh & hải quan, khách sạn, giao thông, nhà hàng, tham quan & chụp ảnh, "
            "mua sắm, khẩn cấp, kết bạn trên đường, đọc/viết review du lịch."
        ),
        "course_level": "intermediate",
        "content_mode": "text_only",
        "expected_cohort_behavior": {
            "typical_response_time_sec_per_item": [8, 32],
            "typical_accuracy_band": [0.60, 0.85],
            "hint_usage_rate": [0.05, 0.26],
        },
        "lessons": build_all_lessons(),
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    nq = sum(len(x.get("quizzes") or []) for x in data["lessons"])
    print(f"Wrote {OUT.name}: {len(data['lessons'])} lessons, {nq} questions.")


if __name__ == "__main__":
    main()
