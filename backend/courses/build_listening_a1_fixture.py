"""
[Legacy] Build course_listening_a1.json from listening_preview_4lessons.json.

Hiện tại file fixtures/course_listening_a1.json được chỉnh tay (1 bài “Request your boss”
+ 20 câu quiz). Chỉ chạy script này nếu bạn cố ý ghi đè từ preview JSON cũ.
Run from repo root: python backend/courses/build_listening_a1_fixture.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BACKEND=Path(__file__).resolve().parent.parent
ROOT = BACKEND.parent

def _preview_path() -> Path:
    for rel in (
        Path("course/listening/listening_preview_4lessons.json"),
        Path("course/Listening/listening_preview_4lessons.json"),
    ):
        p = ROOT / rel
        if p.is_file():
            return p
    return ROOT / "course/listening/listening_preview_4lessons.json"


OUT_DIR = Path(__file__).resolve().parent / "fixtures"
OUT = OUT_DIR / "course_listening_a1.json"


def strip_html(html: str) -> str:
    if not html:
        return ""
    t = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    t = re.sub(r"</p>\s*<p[^>]*>", "\n\n", t, flags=re.I)
    t = re.sub(r"</p>|<p[^>]*>", "\n", t, flags=re.I)
    t = re.sub(r"<h[12][^>]*>", "\n## ", t, flags=re.I)
    t = re.sub(r"</h[12]>", "\n", t, flags=re.I)
    t = re.sub(r"<hr\s*/?>", "\n---\n", t, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"&nbsp;", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def act_lines(preparation: dict | None, tasks: list) -> str:
    lines: list[str] = ["### Bài tập (British Council gamedata)", ""]
    if preparation:
        lines.append(
            f"- **Preparation:** `{preparation.get('activityType')}` — {preparation.get('gamedataUrl', '')}"
        )
    for i, t in enumerate(tasks or [], 1):
        lines.append(f"- **Task {i}:** `{t.get('activityType')}` — {t.get('gamedataUrl', '')}")
    return "\n".join(lines)


QUIZZES_BY_SLUG = {
    "request-your-boss": {
        "question_text": "Theo transcript, Susanne yêu cầu Mario làm gì *trước tiên*?",
        "options": {
            "A": "Đặt phòng họp",
            "B": "Gửi email cho khách hàng để hỏi lịch Susanne có thể tới thăm",
            "C": "Viết báo cáo về dự án mới",
            "D": "Mời mọi người dự họp nhóm",
        },
        "correct_answer": "B",
        "hint_text": "Susanne nói “Please do this first. It's a priority and very urgent.” về việc email.",
    },
    "voicemail-message": {
        "question_text": "Marina làm việc cho công ty nào?",
        "options": {
            "A": "Old Time Toys",
            "B": "New Time Toys",
            "C": "Alex Toys",
            "D": "British Council",
        },
        "correct_answer": "A",
        "hint_text": "Marina giới thiệu “calling from Old Time Toys”.",
    },
    "booking-table": {
        "question_text": "Trong lần đặt bàn đầu tiên, Jamie đặt cho bao nhiêu người?",
        "options": {"A": "2", "B": "3", "C": "4", "D": "6"},
        "correct_answer": "C",
        "hint_text": "Jamie nói “Four.” khi được hỏi “How many people is it for?”",
    },
    "business-cards": {
        "question_text": "Trên danh thiếp của Dr Peter Miller, chức danh (position) là gì?",
        "options": {
            "A": "Sales Director",
            "B": "Lead Programmer",
            "C": "Product Manager",
            "D": "Intern, R&D team",
        },
        "correct_answer": "A",
        "hint_text": "Xem phần “Reading text”, thẻ số 1.",
    },
}


def main() -> None:
    preview = _preview_path()
    if not preview.is_file():
        print(f"Missing preview file: {preview}", file=sys.stderr)
        sys.exit(1)

    raw = json.loads(preview.read_text(encoding="utf-8"))
    lessons_out = []

    for idx, L in enumerate(raw["lessons"], start=1):
        slug = L["slug"]
        teaser = strip_html(L.get("teaserHtml") or "")
        instr = strip_html(L.get("instructionsHtml") or "")
        trans = strip_html(L.get("transcriptHtml") or "")
        disc = strip_html(L.get("discussionHtml") or "")
        audio_u = (L.get("audio") or {}).get("url") or ""
        hero = L.get("heroImageUrl") or ""
        worksheet = L.get("worksheetPdfUrl") or ""

        body_intro = f"*{L.get('metaDescription') or teaser}*\n\n"
        body_links = ""
        if audio_u:
            body_links += f"[Nghe audio mp3]({audio_u})\n\n"
        if hero:
            body_links += f"![Ảnh minh họa]({hero})\n\n"
        if worksheet:
            body_links += f"[Tải worksheet PDF]({worksheet})\n\n"

        theory_body = (
            body_intro
            + body_links
            + "### Hướng dẫn\n\n"
            + instr
            + "\n\n### Transcript\n\n"
            + trans
            + "\n\n### Thảo luận\n\n"
            + disc
            + "\n\n"
            + act_lines(L.get("preparation"), L.get("tasks") or [])
        )
        rt = L.get("readingTextHtml")
        if rt:
            theory_body += "\n\n### Reading text (danh thiếp)\n\n" + strip_html(rt)

        qz = QUIZZES_BY_SLUG.get(slug)
        if not qz:
            raise SystemExit(f"No quiz template for slug {slug!r}")

        lessons_out.append(
            {
                "lesson_id": f"L_a1_{slug.replace('-', '_')}",
                "lesson_name": L["title"],
                "order": idx,
                "estimated_minutes": 25,
                "audio_url": audio_u,
                "metadata": {"skill": "listening", "topic": slug, "source": "learnenglish.britishcouncil.org"},
                "content": {
                    "theory_pages": [
                        {"title": "Nội dung bài", "body": theory_body},
                    ]
                },
                "quizzes": [
                    {
                        "quiz_id": f"Q_{slug}_01",
                        "difficulty_level": 2,
                        "question_type": "multiple_choice",
                        "question_text": qz["question_text"],
                        "options": qz["options"],
                        "correct_answer": qz["correct_answer"],
                        "hint_text": qz["hint_text"],
                    }
                ],
            }
        )

    payload = {
        "course_id": "listening_a1",
        "course_name": "Listening — A1",
        "course_description": "Nghe hiểu A1: bài từ LearnEnglish (British Council). Mỗi bài có preparation, audio, task 1–2 (gamedata) và quiz hệ thống.",
        "course_level": "beginner",
        "course_skill": "listening",
        "course_cefr_level": "A1",
        "content_mode": "multimedia",
        "lessons": lessons_out,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
