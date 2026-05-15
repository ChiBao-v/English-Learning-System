"""Sinh course_C02_daily_life.json — Daily Life & Surroundings A1+ (10 × 3 trang × 10 quiz)."""

from __future__ import annotations

import json
from pathlib import Path

from c02_daily_life_lesson_builders import build_all_lessons

OUT = Path(__file__).resolve().parent / "course_C02_daily_life.json"


def main():
    data = {
        "course_id": "C02",
        "course_name": "Daily Life & Surroundings (Tiếng Anh Đời sống A1+)",
        "course_description": (
            "Mở rộng vốn từ đời sống, giao thông, thực phẩm; thì hiện tại đơn, giới từ thời gian/địa điểm, "
            "some/any, trạng từ tần suất và đọc hiểu tổng hợp. Mỗi bài có tài liệu nhiều trang và 10 câu kiểm tra."
        ),
        "course_level": "beginner",
        "content_mode": "text_only",
        "expected_cohort_behavior": {
            "typical_response_time_sec_per_item": [6, 18],
            "typical_accuracy_band": [0.72, 0.92],
            "hint_usage_rate": [0.0, 0.15],
        },
        "lessons": build_all_lessons(),
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    nq = sum(len(x.get("quizzes") or []) for x in data["lessons"])
    print(f"Wrote {OUT.name}: {len(data['lessons'])} lessons, {nq} questions.")


if __name__ == "__main__":
    main()
