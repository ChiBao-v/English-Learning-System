"""Sinh course_C03_expanding_horizons.json — Expanding Horizons A2 (10 × 3 trang × 10 quiz)."""

from __future__ import annotations

import json
from pathlib import Path

from c03_a2_expanding_lesson_builders import build_all_lessons

OUT = Path(__file__).resolve().parent / "course_C03_expanding_horizons.json"


def main():
    data = {
        "course_id": "C03",
        "course_name": "Expanding Horizons (Pre-Intermediate A2)",
        "course_description": (
            "Du lịch & nhiếp ảnh, quá khứ đơn, công nghệ & so sánh, âm nhạc, quá khứ tiếp diễn, "
            "sức khỏe và đọc hiểu tổng hợp. Dữ liệu phẳng chuẩn cho pipeline phân tích hành vi học tập."
        ),
        "course_level": "intermediate",
        "content_mode": "text_only",
        "expected_cohort_behavior": {
            "typical_response_time_sec_per_item": [8, 28],
            "typical_accuracy_band": [0.65, 0.88],
            "hint_usage_rate": [0.05, 0.22],
        },
        "lessons": build_all_lessons(),
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    nq = sum(len(x.get("quizzes") or []) for x in data["lessons"])
    print(f"Wrote {OUT.name}: {len(data['lessons'])} lessons, {nq} questions.")


if __name__ == "__main__":
    main()
