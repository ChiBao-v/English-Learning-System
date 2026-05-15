"""Tiếng Anh cơ bản — A1 và A2 (CEFR)."""

from __future__ import annotations

from courses.data.base import CourseSpec, specs_from_rows

_A1: tuple[tuple[str, int, str], ...] = (
    ("GE: Giới thiệu lộ trình A1", 20, "reading"),
    ("GE: Bảng chữ cái & nguyên âm cơ bản", 30, "reading"),
    ("GE: Chào hỏi & từ biệt (Hello, Goodbye)", 30, "vocabulary"),
    ("GE: Giới thiệu tên, quốc tịch (I am / My name is)", 35, "grammar"),
    ("GE: Số đếm 1–100", 30, "vocabulary"),
    ("GE: Giờ & cách hỏi giờ (What time is it?)", 35, "listening"),
    ("GE: Thứ trong tuần & Today / Tomorrow", 30, "vocabulary"),
    ("GE: Tháng & ngày (ordinal numbers)", 35, "reading"),
    ("GE: Gia đình & quan hệ (family members)", 35, "vocabulary"),
    ("GE: Màu sắc & tính từ đơn giản", 30, "vocabulary"),
    ("GE: Đồ vật trong lớp & This / That", 35, "grammar"),
    ("GE: Động từ to be (am / is / are)", 40, "grammar"),
    ("GE: Câu khẳng định, phủ định, nghi vấn với to be", 40, "grammar"),
    ("GE: Từ vựng chủ đề đồ ăn đơn giản", 30, "vocabulary"),
    ("GE: There is / There are", 35, "grammar"),
    ("GE: Danh từ số ít & số nhiều (s/es)", 35, "grammar"),
    ("GE: Giới từ chỉ vị trí (in, on, under)", 30, "grammar"),
    ("Test: Unit test — A1 (1)", 35, "reading"),
    ("GE: Hiện tại đơn — động từ thường (I work / She studies)", 45, "grammar"),
    ("GE: Từ nhận dạng (always, usually, sometimes)", 35, "grammar"),
    ("GE: Câu hỏi Yes/No với do/does", 40, "grammar"),
    ("GE: Câu hỏi Wh- (What, Where, Who)", 40, "grammar"),
    ("GE: Từ vựng cơ thể & sức khỏe đơn giản", 30, "vocabulary"),
    ("GE: Can / can't — khả năng & xin phép", 35, "grammar"),
    ("Test: Mid test — A1", 40, "reading"),
    ("GE: Tổng ôn giao tiếp A1 — mẫu câu cốt lõi", 40, "listening"),
    ("Test: Final test — A1", 45, "reading"),
)

_A2: tuple[tuple[str, int, str], ...] = (
    ("GE: Giới thiệu lộ trình A2", 20, "reading"),
    ("GE: Hiện tại tiếp diễn (am/is/are + V-ing)", 40, "grammar"),
    ("GE: So sánh hiện tại đơn & tiếp diễn", 40, "grammar"),
    ("GE: Quá khứ của to be (was / were)", 35, "grammar"),
    ("GE: Quá khứ đơn — động từ có quy tắc", 45, "grammar"),
    ("GE: Động từ bất quy tắc — nhóm thường gặp", 45, "grammar"),
    ("GE: Going to — dự định gần", 35, "grammar"),
    ("GE: So sánh hơn (comparatives)", 40, "grammar"),
    ("GE: So sánh nhất (superlatives)", 40, "grammar"),
    ("GE: Danh từ đếm được & không đếm được", 35, "grammar"),
    ("GE: Some / any trong câu", 35, "grammar"),
    ("GE: Much / many / a lot of", 35, "grammar"),
    ("Test: Unit test — A2 (1)", 35, "reading"),
    ("GE: Must / have to — nghĩa vụ & quy định", 40, "grammar"),
    ("GE: Should — lời khuyên", 30, "grammar"),
    ("GE: Giới từ chỉ thời gian (at, on, in)", 35, "grammar"),
    ("GE: Trạng từ tần suất (always, often, never)", 35, "grammar"),
    ("GE: Like / love + V-ing — sở thích", 30, "grammar"),
    ("GE: Will — quyết định tại chỗ & dự đoán", 35, "grammar"),
    ("GE: Câu điều kiện loại 0 & 1 — giới thiệu", 40, "grammar"),
    ("Test: Mid test — A2", 40, "reading"),
    ("GE: Hội thoại ngắn — đặt lịch & xin phép", 40, "listening"),
    ("GE: Đọc hiểu đoạn ngắn — tìm ý chính", 45, "reading"),
    ("Test: Final test — A2", 45, "reading"),
)

GENERAL_ENGLISH_A1 = CourseSpec(
    key="general_english_a1",
    title="Tiếng Anh cơ bản — Nền tảng A1",
    description=(
        "Dành cho người mới bắt đầu (CEFR A1): chào hỏi, số & giờ, to be, "
        "hiện tại đơn cơ bản, từ vựng chủ đề thiết yếu. Lộ trình gợi ý ~8–12 tuần."
    ),
    level="beginner",
    suggested_days=56,
    lessons=specs_from_rows(_A1),
    practice_note="theo tiến trình A1 (CEFR).",
)

GENERAL_ENGLISH_A2 = CourseSpec(
    key="general_english_a2",
    title="Tiếng Anh cơ bản — Tiếp nối A2",
    description=(
        "Nâng từ A1 lên A2: thì quá khứ, so sánh, lượng từ, năng lực & nghĩa vụ, "
        "hội thoại và đọc hiểu đoạn ngắn. Lộ trình gợi ý ~10–14 tuần."
    ),
    level="beginner",
    suggested_days=70,
    lessons=specs_from_rows(_A2),
    practice_note="theo tiến trình A2 (CEFR).",
)

ALL_GENERAL_ENGLISH_SPECS: tuple[CourseSpec, ...] = (
    GENERAL_ENGLISH_A1,
    GENERAL_ENGLISH_A2,
)
