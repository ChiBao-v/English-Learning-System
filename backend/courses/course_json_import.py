"""Import khóa học từ payload JSON (dùng bởi management command và có thể gọi từ code)."""

from __future__ import annotations

from typing import Any

from django.db import transaction

from courses.models import Course, Lesson, Question

DOC_PAGE_BREAK = "<<<DOC_PAGE_BREAK>>>"
DOC_PAGE_END_THEORY = "<<<DOC_PAGE_END_THEORY>>>"

JSON_TYPE_MAP = {
    "fill_in_blank": Question.Type.FILL_IN_BLANK,
    "multiple_choice": Question.Type.MULTIPLE_CHOICE,
    "synonym_antonym": Question.Type.MULTIPLE_CHOICE,
    "error_identification": Question.Type.MULTIPLE_CHOICE,
    "true_false": Question.Type.TRUE_FALSE,
}

ALLOWED_LEVELS = frozenset({"beginner", "intermediate", "advanced"})
ALLOWED_SKILLS = frozenset({"general", "listening", "reading", "writing", "speaking"})
ALLOWED_CEFR = frozenset({"A1", "A2", "B1", "B2", "C1", "C2"})


class CourseJsonImportError(Exception):
    """Lỗi cấu trúc hoặc nội dung JSON khóa học."""


def course_description_from_payload(data: dict) -> str:
    explicit = (data.get("course_description") or "").strip()
    if explicit:
        return explicit
    name = (data.get("course_name") or "").strip()
    if name:
        return f"Lộ trình: {name}."
    return ""


def options_to_list(options: dict[str, str]) -> list[str]:
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    out: list[str] = []
    for letter in letters:
        if letter in options:
            out.append(f"{letter}. {options[letter]}")
    return out


def full_correct_answer(options: dict[str, str], letter: str) -> str:
    letter = letter.strip().upper()
    if letter not in options:
        raise ValueError(f"correct_answer {letter} not in options")
    return f"{letter}. {options[letter]}"


def merge_theory_block(content_obj: dict) -> str:
    pages = content_obj.get("theory_pages")
    if pages and isinstance(pages, list):
        parts: list[str] = []
        for p in pages:
            title = (p.get("title") or "Phần").strip()
            body = (p.get("body") or "").strip()
            parts.append(f"## {title}\n\n{body}")
        return DOC_PAGE_BREAK.join(parts)
    return (content_obj.get("theory") or "").strip()


def merge_pages_key(content_obj: dict, key: str) -> str:
    pages = content_obj.get(key)
    if not pages or not isinstance(pages, list):
        return ""
    parts: list[str] = []
    for p in pages:
        title = (p.get("title") or "Phần").strip()
        body = (p.get("body") or "").strip()
        parts.append(f"## {title}\n\n{body}")
    return DOC_PAGE_BREAK.join(parts)


def format_study_content_and_transcript(content_obj: dict) -> tuple[str, str, str]:
    """
    Trả về (content tab tài liệu, transcript listening, reading_passage).

    - Có `transcript` → content chỉ từ preparation_*; reading_passage rỗng.
    - Có `reading_passage` (không dùng transcript) → content chỉ từ preparation_*.
    - Không có cả hai → hành vi cũ: format_lesson_content, hai field phụ rỗng.
    """
    transcript = (content_obj.get("transcript") or "").strip()
    reading_passage = (content_obj.get("reading_passage") or "").strip()
    if transcript:
        blocks: list[str] = []
        prep_pg = merge_pages_key(content_obj, "preparation_pages")
        if prep_pg:
            blocks.append(prep_pg)
        single_prep = (content_obj.get("preparation") or "").strip()
        if single_prep:
            blocks.append(single_prep)
        study = "\n\n".join(blocks).strip()
        return study, transcript, ""
    if reading_passage:
        blocks = []
        prep_pg = merge_pages_key(content_obj, "preparation_pages")
        if prep_pg:
            blocks.append(prep_pg)
        single_prep = (content_obj.get("preparation") or "").strip()
        if single_prep:
            blocks.append(single_prep)
        study = "\n\n".join(blocks).strip()
        return study, "", reading_passage
    return format_lesson_content(content_obj), "", ""


def format_lesson_content(content_obj: dict) -> str:
    chunks: list[str] = []
    theory_block = merge_theory_block(content_obj)
    supplemental: list[str] = []

    if rp := (content_obj.get("reading_passage") or "").strip():
        supplemental.append("---\n### Đoạn đọc\n" + rp)
    vocab = content_obj.get("vocabulary") or []
    if vocab:
        lines = ["Từ vựng:"]
        for item in vocab:
            w = item.get("word", "")
            vi = item.get("vi", "")
            pos = item.get("pos", "")
            extra = f" ({pos})" if pos else ""
            lines.append(f"• {w}{extra}: {vi}")
        supplemental.append("\n".join(lines))
    examples = content_obj.get("examples") or []
    if examples:
        lines = ["Ví dụ:"]
        for e in examples:
            lines.append(f"• {e.get('english', '')} — {e.get('vietnamese', '')}")
        supplemental.append("\n".join(lines))

    rest = "\n\n".join(supplemental) if supplemental else ""
    if theory_block and rest:
        chunks.append(theory_block + "\n\n" + DOC_PAGE_END_THEORY + "\n\n" + rest)
    elif theory_block:
        chunks.append(theory_block)
    elif rest:
        chunks.append(rest)
    return "\n\n".join(chunks)


def skill_type(lesson_name: str, quiz_type: str, metadata: dict | None = None) -> str:
    meta = metadata or {}
    sk = (meta.get("skill") or "").strip().lower()
    if sk == "reading":
        return Question.SkillType.READING
    if sk == "grammar":
        return Question.SkillType.GRAMMAR
    if sk == "vocabulary":
        return Question.SkillType.VOCABULARY
    if sk == "writing":
        return Question.SkillType.WRITING
    if sk == "speaking":
        return Question.SkillType.SPEAKING
    if sk == "listening":
        return Question.SkillType.LISTENING

    name = lesson_name.lower()
    if "đọc hiểu" in lesson_name or "đoạn văn" in name or "(reading)" in name:
        return Question.SkillType.READING
    if quiz_type == "error_identification":
        return Question.SkillType.GRAMMAR
    return Question.SkillType.VOCABULARY


def validate_course_payload(data: dict[str, Any]) -> list[str]:
    """Trả về danh sách lỗi (rỗng nếu hợp lệ)."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Root phải là một object JSON."]

    name = (data.get("course_name") or "").strip()
    if not name:
        errors.append("Thiếu hoặc rỗng course_name.")

    level = (data.get("course_level") or "beginner").strip().lower()
    if level not in ALLOWED_LEVELS:
        errors.append(f"course_level không hợp lệ: {level!r} (chỉ: beginner, intermediate, advanced).")

    skill = (data.get("course_skill") or "general").strip().lower()
    if skill not in ALLOWED_SKILLS:
        errors.append(
            f"course_skill không hợp lệ: {skill!r} (chỉ: {', '.join(sorted(ALLOWED_SKILLS))})."
        )

    cefr = (data.get("course_cefr_level") or "").strip().upper()
    if cefr and cefr not in ALLOWED_CEFR:
        errors.append(f"course_cefr_level không hợp lệ: {cefr!r}.")

    cid = (data.get("course_id") or "").strip()
    if cid and len(cid) > 32:
        errors.append("course_id quá 32 ký tự (external_id trong DB).")

    lessons = data.get("lessons")
    if not isinstance(lessons, list) or len(lessons) == 0:
        errors.append("lessons phải là mảng có ít nhất 1 phần tử.")
        return errors

    lesson_orders: list[int] = []
    for i, les in enumerate(lessons):
        prefix = f"Bài học [{i}]"
        if not isinstance(les, dict):
            errors.append(f"{prefix}: mỗi lesson phải là object.")
            continue
        lname = (les.get("lesson_name") or "").strip()
        if not lname:
            errors.append(f"{prefix}: thiếu lesson_name.")
        order = les.get("order")
        if order is not None and not isinstance(order, int):
            errors.append(f"{prefix}: order phải là số nguyên.")
        elif isinstance(order, int):
            lesson_orders.append(order)

        quizzes = les.get("quizzes")
        if quizzes is None:
            errors.append(f"{prefix} ({lname or '?'}): thiếu quizzes (có thể mảng rỗng).")
            continue
        if not isinstance(quizzes, list):
            errors.append(f"{prefix}: quizzes phải là mảng.")
            continue

        for j, q in enumerate(quizzes):
            qp = f"{prefix} câu [{j}]"
            if not isinstance(q, dict):
                errors.append(f"{qp}: mỗi quiz phải là object.")
                continue
            qtext = (q.get("question_text") or "").strip()
            if not qtext:
                errors.append(f"{qp}: thiếu question_text.")
            opt_dict = q.get("options")
            if not isinstance(opt_dict, dict) or not opt_dict:
                errors.append(f"{qp}: options phải là object có ít nhất một lựa chọn (A, B, …).")
                continue
            qt = q.get("question_type", "multiple_choice")
            if qt not in JSON_TYPE_MAP:
                errors.append(
                    f"{qp}: question_type {qt!r} chưa hỗ trợ. "
                    f"Hỗ trợ: {', '.join(sorted(JSON_TYPE_MAP))}."
                )
            ca = str(q.get("correct_answer", "")).strip().upper()
            if not ca:
                errors.append(f"{qp}: thiếu correct_answer.")
            elif ca not in opt_dict:
                errors.append(f"{qp}: correct_answer {ca!r} không có trong options.")

    if len(lesson_orders) != len(set(lesson_orders)) and lesson_orders:
        errors.append("Cảnh báo: có order trùng nhau giữa các bài — nên dùng order duy nhất.")

    return errors


@transaction.atomic
def import_course_payload(
    data: dict[str, Any],
    *,
    replace_if_exists: bool = False,
) -> tuple[Course, int, int]:
    """
    Tạo Course + Lesson + Question từ dict đã validate.
    replace_if_exists: nếu course_id trùng external_id, xóa khóa cũ (cascade) rồi import.
    """
    errs = validate_course_payload(data)
    if errs:
        raise CourseJsonImportError("; ".join(errs))

    ext = (data.get("course_id") or "").strip()[:32]
    if replace_if_exists:
        if not ext:
            raise CourseJsonImportError("--replace-if-exists yêu cầu course_id không rỗng trong JSON.")
        Course.objects.filter(external_id=ext).delete()

    course = Course.objects.create(
        title=data["course_name"],
        external_id=ext,
        description=course_description_from_payload(data),
        level=data.get("course_level", Course.Level.BEGINNER),
        skill=(data.get("course_skill") or Course.Skill.GENERAL).strip().lower(),
        cefr_level=(data.get("course_cefr_level") or "").strip().upper()[:8],
        is_active=True,
    )

    n_lessons = 0
    n_questions = 0
    for les in sorted(data["lessons"], key=lambda x: x.get("order", 0)):
        content_obj = les.get("content") or {}
        study_body, transcript_body, reading_passage_body = format_study_content_and_transcript(content_obj)
        lesson = Lesson.objects.create(
            course=course,
            title=les["lesson_name"],
            content=study_body,
            transcript=transcript_body,
            reading_passage=reading_passage_body,
            order_num=les.get("order", n_lessons + 1),
            duration=les.get("estimated_minutes", 30),
            audio_url=str(les.get("audio_url", "") or "")[:500],
        )
        n_lessons += 1

        for q in les.get("quizzes", []):
            opt_dict = q.get("options") or {}
            opt_list = options_to_list(opt_dict)
            letter = str(q["correct_answer"]).strip().upper()
            answer_str = full_correct_answer(opt_dict, letter)

            qt = q.get("question_type", "multiple_choice")
            django_type = JSON_TYPE_MAP.get(qt, Question.Type.MULTIPLE_CHOICE)

            q_audio = (q.get("audio_url") or les.get("audio_url") or "").strip()[:500]
            q_image = (q.get("image_url") or "").strip()[:500]
            Question.objects.create(
                lesson=lesson,
                content=q["question_text"],
                question_type=django_type,
                options=opt_list,
                answer=answer_str,
                difficulty=min(5, max(1, int(q.get("difficulty_level", 2)))),
                hint=q.get("hint_text", ""),
                skill_type=skill_type(les["lesson_name"], qt, les.get("metadata")),
                audio_url=q_audio,
                image_url=q_image,
            )
            n_questions += 1

    return course, n_lessons, n_questions
