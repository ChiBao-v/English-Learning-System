"""Sinh course_C01_foundation.json — Foundation English A1 (10 bài × 3 trang × 10 quiz)."""
from __future__ import annotations

import json
from pathlib import Path

from c01_a1_lesson_builders import build_all_lessons

OUT = Path(__file__).resolve().parent / "course_C01_foundation.json"


def main():
    data = {
        "course_id": "C01",
        "course_name": "Foundation English (Tiếng Anh Nền Tảng A1)",
        "course_description": (
            "Lộ trình A1: chào hỏi & giới thiệu, đại từ và to be, số & tuổi, phủ định & hỏi, "
            "quốc gia, câu hỏi Wh-, gia đình và đọc hiểu tổng hợp. Mỗi bài có tài liệu nhiều trang và 10 câu kiểm tra."
        ),
        "course_level": "beginner",
        "content_mode": "text_only",
        "expected_cohort_behavior": {
            "typical_response_time_sec_per_item": [5, 15],
            "typical_accuracy_band": [0.78, 0.95],
            "hint_usage_rate": [0.0, 0.12],
        },
        "lessons": build_all_lessons(),
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    nq = sum(len(x.get("quizzes") or []) for x in data["lessons"])
    print(f"Wrote {OUT.name}: {len(data['lessons'])} lessons, {nq} questions.")


if __name__ == "__main__":
    main()
