"""Sinh course_C04_practical_office.json — Practical Office Communication B1."""

from __future__ import annotations

import json
from pathlib import Path

from c04_b1_office_lesson_builders import build_all_lessons

OUT = Path(__file__).resolve().parent / "course_C04_practical_office.json"


def main():
    data = {
        "course_id": "C04",
        "course_name": "Practical Office Communication (Intermediate B1)",
        "course_description": (
            "Giao tiếp công sở: small talk, email chuyên nghiệp, điện thoại, họp & ý kiến, modals & xin lỗi, "
            "cơ cấu công ty, báo cáo tiến độ (present perfect), lịch hẹn, thuyết trình, văn hóa làm việc từ xa."
        ),
        "course_level": "intermediate",
        "content_mode": "text_only",
        "expected_cohort_behavior": {
            "typical_response_time_sec_per_item": [10, 35],
            "typical_accuracy_band": [0.62, 0.86],
            "hint_usage_rate": [0.06, 0.25],
        },
        "lessons": build_all_lessons(),
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    nq = sum(len(x.get("quizzes") or []) for x in data["lessons"])
    print(f"Wrote {OUT.name}: {len(data['lessons'])} lessons, {nq} questions.")


if __name__ == "__main__":
    main()
