"""Sinh course_C06_customer_service_fb.json — Customer Service & F&B B1."""

from __future__ import annotations

import json
from pathlib import Path

from c06_b1_csfb_lesson_builders import build_all_lessons

OUT = Path(__file__).resolve().parent / "course_C06_customer_service_fb.json"


def main():
    data = {
        "course_id": "C06",
        "course_name": "English for Customer Service & F&B (Intermediate B1)",
        "course_description": (
            "Đón khách & đặt bàn, gọi món & gợi ý, dị ứng & chế độ ăn, bán lẻ, thanh toán, "
            "xử lý khiếu nại, câu bị động lịch sự, đặt bàn qua điện thoại, chỉ đường & gợi ý địa phương, trả lời review online."
        ),
        "course_level": "intermediate",
        "content_mode": "text_only",
        "expected_cohort_behavior": {
            "typical_response_time_sec_per_item": [9, 36],
            "typical_accuracy_band": [0.58, 0.84],
            "hint_usage_rate": [0.07, 0.28],
        },
        "lessons": build_all_lessons(),
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    nq = sum(len(x.get("quizzes") or []) for x in data["lessons"])
    print(f"Wrote {OUT.name}: {len(data['lessons'])} lessons, {nq} questions.")


if __name__ == "__main__":
    main()
