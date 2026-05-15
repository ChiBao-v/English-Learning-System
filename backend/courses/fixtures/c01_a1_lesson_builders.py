"""Nội dung 10 bài Foundation A1 — dùng bởi generate_c01_a1_course.py."""

from __future__ import annotations


def Q(qid, diff, qtype, text, opts, ans, hint, rt=12, hu=False):
    return {
        "quiz_id": qid,
        "difficulty_level": diff,
        "question_type": qtype,
        "question_text": text,
        "options": opts,
        "correct_answer": ans,
        "hint_text": hint,
        "expected_behavior_simulation": {"avg_response_time_sec": rt, "likely_to_use_hint": hu},
    }


def wc(text: str) -> int:
    return len(text.replace("\n", " ").split())


def build_all_lessons():
    """Trả về list 10 lesson dict (JSON-serializable)."""
    lessons = []
    lessons.append(_lesson_01())
    lessons.append(_lesson_02())
    lessons.append(_lesson_03())
    lessons.append(_lesson_04())
    lessons.append(_lesson_05())
    lessons.append(_lesson_06())
    lessons.append(_lesson_07())
    lessons.append(_lesson_08())
    lessons.append(_lesson_09())
    lessons.append(_lesson_10())
    return lessons


def _lesson_01():
    meta = {"skill": "vocabulary", "topic": "greetings", "time_est_minutes": 10, "difficulty": 0.1}
    p1 = """### Chào hỏi trang trọng

Dùng khi **lần đầu gặp**, trong lớp, công sở, hoặc khi muốn **lịch sự**.

| Cụm | Khi nào |
|-----|---------|
| **Hello** | Gần như mọi tình huống trung tính |
| **Good morning** | **Sáng** (khoảng đến ~11h, tùy văn hóa) |
| **Good afternoon** | **Chiều** (sau buổi trưa — gặp giáo viên lúc **2 giờ chiều** → dùng câu này) |
| **Good evening** | **Tối** (sau giờ làm, chào buổi tối) |

> **Good night** = chúc **ngủ ngon** (khi chia tay trước khi đi ngủ), **không** dùng như “chào buổi tối” khi mới gặp."""

    p2 = """### Chào thân mật & tạm biệt

**Thân mật:** *Hi*, *Hey* — bạn bè, chat, môi trường lỏng.

**Tạm biệt:**

- *Goodbye* — trung tính, lịch sự nhẹ.
- *Bye* — rất ngắn, thân mật.
- *See you later* — **hẹn gặp lại sau** (có thể thêm *See you tomorrow*).
- *Good night* — **Chúc ngủ ngon** (chia tay buổi đêm).

### Thực hành nhanh

Đọc to từng cụm **3 lần**; ghép với cử chỉ vẫy tay khi nói *Bye* / *See you later*."""

    p3 = """### Từ vựng cốt lõi

| Tiếng Anh | Gợi ý nghĩa |
|-----------|-------------|
| **name** | tên |
| **friend** | bạn bè |
| **teacher** | giáo viên |
| **student** | học sinh / sinh viên |

### Câu mẫu

- *My name is Lan.* — *She is my **friend**.*
- *He is a **teacher**.* — *I am a **student**.*

### Gợi ý học

Viết **4 câu** giới thiệu: tên — bạn là gì (student) — một người là teacher — một người là friend."""

    reading = (
        "Anna: Good afternoon, Mr. Brown!\n"
        "Mr. Brown: Good afternoon, Anna. How are you?\n"
        "Anna: I'm fine, thank you. Goodbye!\n"
        "Mr. Brown: Goodbye. See you later!"
    )
    return {
        "lesson_id": "L01_01",
        "lesson_name": "Greetings & Introductions (Vocabulary)",
        "order": 1,
        "estimated_minutes": 32,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Chào hỏi trang trọng", "body": p1},
                {"title": "Trang 2 — Thân mật & tạm biệt", "body": p2},
                {"title": "Trang 3 — Từ vựng & câu mẫu", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "Hello / Hi", "vi": "Xin chào (trang trọng / thân mật)"},
                {"word": "Good morning / afternoon / evening", "vi": "Chào buổi sáng/chiều/tối"},
                {"word": "Goodbye / Bye", "vi": "Tạm biệt"},
                {"word": "See you later", "vi": "Hẹn gặp lại"},
                {"word": "Good night", "vi": "Chúc ngủ ngon"},
                {"word": "name", "vi": "tên"},
                {"word": "friend", "vi": "bạn bè"},
                {"word": "teacher", "vi": "giáo viên"},
                {"word": "student", "vi": "học sinh; sinh viên"},
            ],
            "examples": [
                {"english": "Good afternoon, teacher!", "vietnamese": "Chào buổi chiều, thầy/cô!"},
                {"english": "See you later, my friend.", "vietnamese": "Hẹn gặp lại, bạn của tôi."},
            ],
        },
        "quizzes": [
            Q("Q_L01_01_01", 1, "multiple_choice", "Gặp giáo viên lúc 2 giờ chiều, bạn nên nói:", {"A": "Good morning", "B": "Good afternoon", "C": "Good night", "D": "Good night, teacher"}, "B", "Chiều → Good afternoon.", 10),
            Q("Q_L01_01_02", 2, "multiple_choice", "Ghép đúng (đồng nghĩa / gần nghĩa trong chào hỏi): 1. Hello — 2. Goodbye", {"A": "1→Hi, 2→Bye", "B": "1→Bye, 2→Hi", "C": "1→Good night, 2→Morning", "D": "1→Teacher, 2→Student"}, "A", "Hello ≈ Hi; Goodbye ≈ Bye.", 12),
            Q("Q_L01_01_03", 1, "fill_in_blank", "See you _____. (Hẹn gặp lại sau)", {"A": "later", "B": "before", "C": "never", "D": "again"}, "A", "See you later — cố định.", 9),
            Q("Q_L01_01_04", 2, "multiple_choice", "Khi nào nói *Good night*?", {"A": "Chào buổi sáng", "B": "Chia tay trước khi đi ngủ / chúc ngủ ngon", "C": "Gặp lúc 3 giờ chiều", "D": "Khi gặp lần đầu buổi sáng"}, "B", "Good night = chúc ngủ ngon.", 11),
            Q("Q_L01_01_05", 1, "multiple_choice", "Từ *teacher* nghĩa là:", {"A": "học sinh", "B": "giáo viên", "C": "bạn bè", "D": "tên"}, "B", "Teacher = giáo viên.", 8),
            Q("Q_L01_01_06", 2, "multiple_choice", "Chọn câu **thân mật** nhất:", {"A": "Good evening, Professor.", "B": "Hey! How are you?", "C": "Goodbye, sir.", "D": "See you later, Mr. Smith."}, "B", "Hey — thân mật.", 10),
            Q("Q_L01_01_07", 2, "fill_in_blank", "I am a _____. I study at school.", {"A": "teacher", "B": "student", "C": "night", "D": "later"}, "B", "Study at school → student.", 10),
            Q("Q_L01_01_08", 2, "error_identification", "Tìm từ không hợp ngữ cảnh: 'Good night! Nice to meet you — at 9 a.m.!'", {"A": "Good night", "B": "Nice to meet you", "C": "at 9 a.m.", "D": "—"}, "A", "9 sáng không dùng Good night.", 14, True),
            Q("Q_L01_01_09", 2, "multiple_choice", "She is my _____.", {"A": "name", "B": "friend", "C": "morning", "D": "goodbye"}, "B", "My friend — bạn của tôi.", 9),
            Q("Q_L01_01_10", 3, "multiple_choice", "Chọn câu đúng:", {"A": "Goodbye morning.", "B": "Good morning, class.", "C": "Good class, morning.", "D": "Morning good."}, "B", "Good morning, class.", 11),
        ],
    }


def _lesson_02():
    meta = {"skill": "grammar", "topic": "to_be_affirmative", "time_est_minutes": 15, "difficulty": 0.15}
    p1 = """### Đại từ nhân xưng (chủ ngữ)

| Đại từ | Gợi ý |
|--------|--------|
| **I** | tôi |
| **you** | bạn / các bạn |
| **we** | chúng ta / chúng tôi |
| **they** | họ |
| **he** | anh ấy / ông ấy… |
| **she** | cô ấy / bà ấy… |
| **it** | nó (vật, động vật, sự việc) |

Đại từ đứng **trước** động từ: *I am*, *She is*…"""

    p2 = """### Động từ *to be* — **khẳng định** (hiện tại)

| Chủ ngữ | Dạng | Viết tắt (một số) |
|---------|------|-------------------|
| **I** | **am** | *I'm* |
| **he / she / it** | **is** | *He's, She's, It's* |
| **you / we / they** | **are** | *You're, We're, They're* |

### Cấu trúc

**Chủ ngữ + be + …** (bổ ngữ có thể là danh từ / tính từ / giới từ cụm)

- *I am a student.*
- *He is a teacher.*
- *They are friends.*"""

    p3 = """### Lưu ý nhanh

- *I* **luôn** đi với *am* — không nói *I is*.
- *He/She/It* với *is*; *You/We/They* với *are*.
- Viết tắt giúp **nói nhanh**: *I'm*, *it's*, *they're* — luyện đọc to.

### Bài tập gợi ý

Viết **6 câu**: mỗi đại từ (*I, you, he, she, we, they*) **một câu** khẳng định có *to be*."""

    reading = "I am a student. You are my friend. He is a boy. She is a girl. It is a book. We are in class. They are happy."
    return {
        "lesson_id": "L01_02",
        "lesson_name": 'Subject Pronouns & "To be" - Affirmative (Grammar)',
        "order": 2,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Đại từ nhân xưng", "body": p1},
                {"title": "Trang 2 — To be khẳng định", "body": p2},
                {"title": "Trang 3 — Viết tắt & luyện tập", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "I / you / we / they / he / she / it", "vi": "các đại từ nhân xưng"},
                {"word": "am / is / are", "vi": "dạng của to be (hiện tại)"},
            ],
            "examples": [
                {"english": "She is a teacher.", "vietnamese": "Cô ấy là giáo viên."},
                {"english": "We are students.", "vietnamese": "Chúng tôi là học sinh."},
            ],
        },
        "quizzes": [
            Q("Q_L01_02_01", 1, "multiple_choice", "She _______ a teacher.", {"A": "am", "B": "is", "C": "are", "D": "be"}, "B", "She + is.", 9),
            Q("Q_L01_02_02", 1, "fill_in_blank", "We _______ students.", {"A": "am", "B": "is", "C": "are", "D": "be"}, "C", "We + are.", 9),
            Q("Q_L01_02_03", 2, "error_identification", "Tìm lỗi: 'I is a student.'", {"A": "I", "B": "is", "C": "a", "D": "student"}, "B", "I am a student.", 12, True),
            Q("Q_L01_02_04", 2, "multiple_choice", "They _______ my friends.", {"A": "am", "B": "is", "C": "are", "D": "be"}, "C", "They + are.", 9),
            Q("Q_L01_02_05", 2, "multiple_choice", "It _______ a pen.", {"A": "am", "B": "is", "C": "are", "D": "be"}, "B", "It + is.", 9),
            Q("Q_L01_02_06", 2, "fill_in_blank", "He _______ from Vietnam.", {"A": "am", "B": "is", "C": "are", "D": "be"}, "B", "He + is.", 9),
            Q("Q_L01_02_07", 3, "multiple_choice", "Chọn câu đúng:", {"A": "You is nice.", "B": "You are nice.", "C": "You am nice.", "D": "You be nice."}, "B", "You + are.", 10),
            Q("Q_L01_02_08", 2, "multiple_choice", "I'm = ?", {"A": "I is", "B": "I am", "C": "I are", "D": "I be"}, "B", "I'm = I am.", 8),
            Q("Q_L01_02_09", 3, "error_identification", "Tìm lỗi: 'They is happy.'", {"A": "They", "B": "is", "C": "happy", "D": "—"}, "B", "They are happy.", 13, True),
            Q("Q_L01_02_10", 2, "fill_in_blank", "You _______ very kind.", {"A": "am", "B": "is", "C": "are", "D": "be"}, "C", "You + are.", 9),
        ],
    }


def _lesson_03():
    meta = {"skill": "reading", "topic": "nice_to_meet_you", "time_est_minutes": 10, "difficulty": 0.2}
    text = (
        "Hello! I am David. I am a student. She is Sarah. She is a teacher. "
        "We are friends. Good morning and nice to meet you!"
    )
    p1 = """### Mục tiêu đọc

Ôn **từ vựng chào hỏi** và **to be khẳng định** trong một đoạn ngắn — tìm **ai là ai**, **nghề gì**, **quan hệ** thế nào."""

    p2 = """### Chiến lược

1. **Đọc câu đầu** — biết chủ đề (chào + giới thiệu).
2. Gạch **đại từ** (*I, she, we*) và **to be** (*am, is, are*).
3. Trả lời câu hỏi chỉ dựa **chữ trong bài** — không đoán thêm."""

    p3 = """### Từ khóa trong bài

- *student* — *teacher* — *friends* — *Good morning* — *nice to meet you*

### Sau khi đọc

Viết **2–3 câu** tóm tắt: David là gì, Sarah là gì, họ quan hệ gì."""
    return {
        "lesson_id": "L01_03",
        "lesson_name": "Nice to meet you (Reading)",
        "order": 3,
        "estimated_minutes": 30,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Mục tiêu", "body": p1},
                {"title": "Trang 2 — Cách đọc", "body": p2},
                {"title": "Trang 3 — Từ khóa & tóm tắt", "body": p3},
            ],
            "reading_passage": text,
            "reading_word_count": wc(text),
            "vocabulary": [
                {"word": "student", "vi": "học sinh; sinh viên"},
                {"word": "teacher", "vi": "giáo viên"},
                {"word": "friends", "vi": "bạn bè"},
                {"word": "Nice to meet you", "vi": "Rất vui được gặp bạn"},
            ],
            "examples": [
                {"english": "I am David.", "vietnamese": "Tôi là David."},
                {"english": "We are friends.", "vietnamese": "Chúng tôi là bạn."},
            ],
        },
        "quizzes": [
            Q("Q_L01_03_01", 2, "multiple_choice", "What is David's job / role in the text?", {"A": "Teacher", "B": "Student", "C": "Friend", "D": "Driver"}, "B", "I am a student.", 11),
            Q("Q_L01_03_02", 2, "true_false", "Sarah is a student.", {"A": "True", "B": "False"}, "B", "She is a teacher.", 10),
            Q("Q_L01_03_03", 2, "multiple_choice", "Are David and Sarah friends?", {"A": "Yes", "B": "No", "C": "We don't know", "D": "They are brothers"}, "A", "We are friends.", 10),
            Q("Q_L01_03_04", 2, "multiple_choice", "Who is a teacher?", {"A": "David", "B": "Sarah", "C": "I", "D": "We"}, "B", "She is Sarah. She is a teacher.", 10),
            Q("Q_L01_03_05", 2, "multiple_choice", "The text says: Good morning and …", {"A": "good night", "B": "nice to meet you", "C": "see you later", "D": "bye bye"}, "B", "Cuối đoạn.", 9),
            Q("Q_L01_03_06", 3, "multiple_choice", "We are friends. Who does *we* refer to?", {"A": "David and Sarah", "B": "David only", "C": "Sarah only", "D": "The teacher"}, "A", "We = David và Sarah.", 12),
            Q("Q_L01_03_07", 2, "fill_in_blank", "She _______ Sarah.", {"A": "am", "B": "is", "C": "are", "D": "be"}, "B", "She is Sarah.", 9),
            Q("Q_L01_03_08", 3, "true_false", "David is a teacher.", {"A": "True", "B": "False"}, "B", "David is a student.", 9),
            Q("Q_L01_03_09", 2, "multiple_choice", "How many people are named in the text?", {"A": "One", "B": "Two", "C": "Three", "D": "Four"}, "B", "David và Sarah.", 11),
            Q("Q_L01_03_10", 3, "multiple_choice", "Best title for the text:", {"A": "A day at school", "B": "Hello — David and Sarah", "C": "Good night", "D": "Numbers 1–10"}, "B", "Nội dung giới thiệu + quan hệ.", 12),
        ],
    }


def _lesson_04():
    meta = {"skill": "vocabulary", "topic": "numbers_age", "time_est_minutes": 15, "difficulty": 0.2}
    p1 = """### Số 1–10

**One, two, three, four, five, six, seven, eight, nine, ten.**

Luyện **đếm ngón tay** và **viết chữ** song song."""

    p2 = """### 11–20 & chục

- **Eleven … twenty** — chú ý **thirteen** (không phải *threeteen*), **fifteen**, **eighteen**.
- Chục: **thirty, forty, fifty, sixty, seventy, eighty, ninety, one hundred**.

> **Fifteen** (15) khác **fifty** (50) — phát âm và chính tả."""

    p3 = """### Nói tuổi

Cấu trúc chuẩn: **I am + [số tuổi] + years old.**

- *I am twenty years old.*
- *She is fifteen years old.*

Tránh: ~~*I have twenty years old.*~~ (sai thông dụng)."""
    reading = "I am ten years old. My brother is fifteen. My parents are forty and forty-two. We are a family of four."
    return {
        "lesson_id": "L01_04",
        "lesson_name": "Numbers (1-100) & Age (Vocabulary)",
        "order": 4,
        "estimated_minutes": 36,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Số 1–10", "body": p1},
                {"title": "Trang 2 — 11–20 & chục", "body": p2},
                {"title": "Trang 3 — Tuổi (years old)", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "one - ten", "vi": "một đến mười"},
                {"word": "eleven - twenty", "vi": "mười một đến hai mươi"},
                {"word": "thirty … one hundred", "vi": "ba mươi … một trăm"},
                {"word": "years old", "vi": "… tuổi"},
            ],
            "examples": [
                {"english": "I am twenty years old.", "vietnamese": "Tôi 20 tuổi."},
                {"english": "She is fifteen.", "vietnamese": "Cô ấy 15 tuổi. (có thể bỏ years old khi rõ ngữ cảnh)"},
            ],
        },
        "quizzes": [
            Q("Q_L01_04_01", 1, "multiple_choice", "Số 15 viết là:", {"A": "Fiveteen", "B": "Fifteen", "C": "Fifty", "D": "Fivty"}, "B", "Fifteen = 15.", 9),
            Q("Q_L01_04_02", 2, "multiple_choice", "“Tôi 20 tuổi” — câu tốt nhất:", {"A": "I am twenty years old.", "B": "I have twenty years.", "C": "I have twenty years old.", "D": "I am twenty years."}, "A", "I am … years old.", 11),
            Q("Q_L01_04_03", 2, "multiple_choice", "Ten + Twelve = ?", {"A": "Twenty", "B": "Twenty-two", "C": "Twenty-one", "D": "Nineteen"}, "B", "10+12=22.", 11),
            Q("Q_L01_04_04", 2, "multiple_choice", "Forty nghĩa là:", {"A": "14", "B": "40", "C": "4", "D": "400"}, "B", "Forty = 40.", 9),
            Q("Q_L01_04_05", 2, "fill_in_blank", "I am _____ years old. (18)", {"A": "eighteen", "B": "eighteenth", "C": "eighty", "D": "eight"}, "A", "18 = eighteen.", 10),
            Q("Q_L01_04_06", 2, "multiple_choice", "Which is correct?", {"A": "She have 12 years old.", "B": "She is twelve years old.", "C": "She is twelve year old.", "D": "She are twelve."}, "B", "She is twelve years old.", 12),
            Q("Q_L01_04_07", 2, "multiple_choice", "Thirteen = ?", {"A": "30", "B": "13", "C": "3", "D": "33"}, "B", "Thirteen = 13.", 8),
            Q("Q_L01_04_08", 3, "multiple_choice", "One hundred = ?", {"A": "10", "B": "100", "C": "1000", "D": "1"}, "B", "One hundred = 100.", 9),
            Q("Q_L01_04_09", 2, "error_identification", "Tìm lỗi: 'I am 20 years olds.'", {"A": "I am", "B": "20", "C": "years olds", "D": "—"}, "C", "years old (không có s).", 13, True),
            Q("Q_L01_04_10", 2, "fill_in_blank", "Twenty + Five = _____", {"A": "twenty-five", "B": "fifty-two", "C": "thirty", "D": "fourteen"}, "A", "25 = twenty-five.", 10),
        ],
    }


def _lesson_05():
    meta = {"skill": "grammar", "topic": "to_be_negative_question", "time_est_minutes": 20, "difficulty": 0.25}
    p1 = """### Phủ định với *to be*

Thêm **not** sau *am/is/are* (hoặc dạng rút):

- *I am not* / *I'm not*
- *He/She/It is not* — *isn't*
- *You/We/They are not* — *aren't*

Ví dụ: *They aren't teachers.* — *I'm not tired.*"""

    p2 = """### Câu hỏi Yes/No

**Đảo to be lên đầu câu:**

- *Am I late?*
- *Is he your brother?*
- *Are you ready?*

Trả lời ngắn: *Yes, I am.* / *No, he isn't.* / *No, they aren't.*"""

    p3 = """### Lưu ý

- *Are you…?* với *you* = bạn **một** hoặc **nhiều** người.
- Phủ định + danh từ: *She is not a doctor.*

### Luyện

Viết **4 câu**: 2 phủ định, 2 câu hỏi Yes/No."""
    reading = "Are you a student? Yes, I am. Is he a teacher? No, he isn't. We are not late. They aren't doctors."
    return {
        "lesson_id": "L01_05",
        "lesson_name": '"To be" - Negative & Interrogative (Grammar)',
        "order": 5,
        "estimated_minutes": 40,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Phủ định", "body": p1},
                {"title": "Trang 2 — Câu hỏi Yes/No", "body": p2},
                {"title": "Trang 3 — Luyện tập", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "not / isn't / aren't", "vi": "phủ định với to be"},
                {"word": "Am / Is / Are ...?", "vi": "câu hỏi Yes/No"},
            ],
            "examples": [
                {"english": "I am not a teacher.", "vietnamese": "Tôi không phải giáo viên."},
                {"english": "Are you from Vietnam?", "vietnamese": "Bạn có phải từ Việt Nam không?"},
            ],
        },
        "quizzes": [
            Q("Q_L01_05_01", 2, "multiple_choice", "They _______ teachers. They are students.", {"A": "isn't", "B": "aren't", "C": "am not", "D": "not are"}, "B", "They aren't teachers.", 11),
            Q("Q_L01_05_02", 2, "multiple_choice", "Which question is correct?", {"A": "You are a student?", "B": "Are you a student?", "C": "Is you a student?", "D": "Are a you student?"}, "B", "Are you a student?", 10),
            Q("Q_L01_05_03", 2, "multiple_choice", "Short negative answer: Is he 25 years old?", {"A": "No, he isn't.", "B": "No, he not is.", "C": "No, he aren't.", "D": "No, he am not."}, "A", "No, he isn't.", 11),
            Q("Q_L01_05_04", 2, "fill_in_blank", "I _______ ready yet. (phủ định)", {"A": "am not", "B": "isn't", "C": "aren't", "D": "not"}, "A", "I am not.", 10),
            Q("Q_L01_05_05", 2, "multiple_choice", "She _______ my sister.", {"A": "is not", "B": "are not", "C": "am not", "D": "be not"}, "A", "She is not / isn't.", 9),
            Q("Q_L01_05_06", 3, "error_identification", "Tìm lỗi: 'Are she your friend?'", {"A": "Are", "B": "she", "C": "your friend", "D": "—"}, "A", "Is she your friend?", 13, True),
            Q("Q_L01_05_07", 2, "multiple_choice", "We _______ at home now. (phủ định)", {"A": "isn't", "B": "aren't", "C": "am not", "D": "not are"}, "B", "We aren't.", 10),
            Q("Q_L01_05_08", 2, "true_false", "I'm not means I am not.", {"A": "True", "B": "False"}, "A", "I'm not = I am not.", 8),
            Q("Q_L01_05_09", 2, "fill_in_blank", "_____ she at home now? (Yes/No question)", {"A": "Is", "B": "Are", "C": "Am", "D": "Do"}, "A", "She → Is she…?", 10),
            Q("Q_L01_05_10", 2, "fill_in_blank", "_______ we late?", {"A": "Is", "B": "Are", "C": "Am", "D": "Be"}, "B", "We → Are we…?", 9),
        ],
    }


def _lesson_06():
    meta = {"skill": "reading", "topic": "personal_profile", "time_est_minutes": 12, "difficulty": 0.25}
    profile = (
        "User Profile\n"
        "Name: Emma Smith\n"
        "Age: 22\n"
        "Job: Student\n\n"
        'About: "Hi, I\'m Emma. I am not a teacher. I am 22 years old. '
        'Are you a student too? Nice to meet you!"'
    )
    p1 = """### Đọc profile

Profile gồm **tên**, **tuổi**, **nghề** và đôi khi đoạn **About** — đọc từng dòng và ghi chú **số** và **to be** (khẳng định / phủ định / hỏi)."""

    p2 = """### Câu hỏi thường gặp từ profile

- Bao nhiêu tuổi? — tìm *Age:* hoặc *… years old*.
- Nghề? — *Job:* hoặc *I am a …*
- Có phải giáo viên không? — tìm *I am not a teacher*."""

    p3 = """### Sau khi đọc

Viết **profile mini** của bạn (4–5 dòng) theo mẫu Emma — dùng *I am*, *I am not*, *Are you …?*."""
    return {
        "lesson_id": "L01_06",
        "lesson_name": "A Personal Profile (Reading)",
        "order": 6,
        "estimated_minutes": 34,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Đọc profile", "body": p1},
                {"title": "Trang 2 — Câu hỏi từ dữ liệu", "body": p2},
                {"title": "Trang 3 — Viết profile của bạn", "body": p3},
            ],
            "reading_passage": profile,
            "reading_word_count": wc(profile),
            "vocabulary": [
                {"word": "profile", "vi": "hồ sơ / tiểu sử ngắn"},
                {"word": "name / age / job", "vi": "tên / tuổi / nghề"},
            ],
            "examples": [
                {"english": "I am not a teacher.", "vietnamese": "Tôi không phải giáo viên."},
                {"english": "Are you a student too?", "vietnamese": "Bạn cũng là học sinh/sinh viên à?"},
            ],
        },
        "quizzes": [
            Q("Q_L01_06_01", 2, "multiple_choice", "Is Emma a teacher?", {"A": "Yes, she is.", "B": "No, she isn't.", "C": "Yes, she are.", "D": "No, she not is."}, "B", "I am not a teacher.", 11),
            Q("Q_L01_06_02", 1, "fill_in_blank", "Emma is _______ years old.", {"A": "20", "B": "22", "C": "12", "D": "32"}, "B", "Age: 22.", 9),
            Q("Q_L01_06_03", 2, "true_false", "Emma is a student.", {"A": "True", "B": "False"}, "A", "Job: Student.", 8),
            Q("Q_L01_06_04", 2, "multiple_choice", "What is Emma's family name (surname)?", {"A": "Emma", "B": "Smith", "C": "Student", "D": "Teacher"}, "B", "Emma Smith → Smith.", 11),
            Q("Q_L01_06_05", 2, "multiple_choice", "The text asks: Are you a student too? Who is *you*?", {"A": "The reader", "B": "Emma", "C": "The teacher", "D": "Smith"}, "A", "Lời hỏi người đọc.", 12),
            Q("Q_L01_06_06", 2, "true_false", "Emma says she is a teacher.", {"A": "True", "B": "False"}, "B", "I am not a teacher.", 9),
            Q("Q_L01_06_07", 2, "multiple_choice", "How old is Emma?", {"A": "twelve", "B": "twenty-two", "C": "thirty", "D": "twenty"}, "B", "22 = twenty-two.", 10),
            Q("Q_L01_06_08", 3, "multiple_choice", "Nice to meet you! appears when Emma is:", {"A": "angry", "B": "introducing / closing politely", "C": "sleeping", "D": "ordering food"}, "B", "Chào / kết thúc lịch sự.", 11),
            Q("Q_L01_06_09", 2, "fill_in_blank", "I _______ a teacher. (phủ định — Emma)", {"A": "am not", "B": "is not", "C": "are not", "D": "not am"}, "A", "I am not a teacher.", 10),
            Q("Q_L01_06_10", 3, "multiple_choice", "Job: Student means Emma is:", {"A": "a teacher", "B": "a student", "C": "retired", "D": "a driver"}, "B", "Job: Student.", 10),
        ],
    }


def _lesson_07():
    meta = {"skill": "vocabulary", "topic": "countries", "time_est_minutes": 15, "difficulty": 0.3}
    p1 = """### Quốc gia & quốc tịch (cặp hay gặp)

| Quốc gia | Quốc tịch (tính từ / danh từ chỉ người) |
|----------|----------------------------------------|
| Vietnam | **Vietnamese** |
| the UK | **British** |
| the USA | **American** |
| Japan | **Japanese** |
| China | **Chinese** |

> **Japanese** vừa là tính từ *Nhật Bản*, vừa chỉ *người Nhật* (tùy câu)."""

    p2 = """### Cách nói xuất xứ

- *I am from **Vietnam**.* (from + **tên nước**)
- *I am **Vietnamese**.* (I am + **quốc tịch**)

Cả hai đều phổ biến ở trình độ nền tảng."""

    p3 = """### Lỗi thường gặp

- ~~*I am from Vietnamese.*~~ → *from Vietnam* **hoặc** *I am Vietnamese.*
- Nhớ *the* với *the USA*, *the UK* (thói quen cố định).

### Luyện

Viết **3 câu** về bản thân: from + nước; I am + quốc tịch; 1 câu hỏi bạn."""
    reading = "I am from Vietnam. I am Vietnamese. She is from Japan. She is Japanese. He is from the USA. He is American."
    return {
        "lesson_id": "L01_07",
        "lesson_name": "Countries & Nationalities (Vocabulary)",
        "order": 7,
        "estimated_minutes": 36,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Bảng cặp từ", "body": p1},
                {"title": "Trang 2 — from / I am", "body": p2},
                {"title": "Trang 3 — Lỗi thường gặp", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "Vietnam / Vietnamese", "vi": "Việt Nam / người Việt, tiếng Việt"},
                {"word": "the USA / American", "vi": "Hoa Kỳ / người Mỹ"},
                {"word": "the UK / British", "vi": "Anh / người Anh"},
                {"word": "Japan / Japanese", "vi": "Nhật Bản / người Nhật"},
                {"word": "China / Chinese", "vi": "Trung Quốc / người Trung"},
            ],
            "examples": [
                {"english": "I am from Vietnam.", "vietnamese": "Tôi đến từ Việt Nam."},
                {"english": "She is Japanese.", "vietnamese": "Cô ấy là người Nhật."},
            ],
        },
        "quizzes": [
            Q("Q_L01_07_01", 2, "multiple_choice", "I am from Japan. I am _______.", {"A": "Japanese", "B": "Japan", "C": "Japanian", "D": "Japans"}, "A", "Quốc tịch: Japanese.", 10),
            Q("Q_L01_07_02", 2, "fill_in_blank", "She is from the USA. She is _______.", {"A": "USA", "B": "American", "C": "America", "D": "USAmerican"}, "B", "American.", 9),
            Q("Q_L01_07_03", 3, "error_identification", "Tìm lỗi: 'I am from Vietnamese.'", {"A": "I am", "B": "from", "C": "Vietnamese", "D": "—"}, "C", "from Vietnam hoặc I am Vietnamese.", 13, True),
            Q("Q_L01_07_04", 2, "multiple_choice", "He is from the UK. He is _______.", {"A": "UKish", "B": "British", "C": "England", "D": "Englishman only"}, "B", "British.", 10),
            Q("Q_L01_07_05", 2, "multiple_choice", "We are from China. We are _______.", {"A": "Chineses", "B": "Chinese", "C": "China", "D": "Chinish"}, "B", "Chinese.", 9),
            Q("Q_L01_07_06", 2, "fill_in_blank", "They are _______. They come from Vietnam.", {"A": "Vietnam", "B": "Vietnamese", "C": "Vietnamian", "D": "Vietnameses"}, "B", "Vietnamese.", 10),
            Q("Q_L01_07_07", 2, "multiple_choice", "Which is correct?", {"A": "I am from the China.", "B": "I am from China.", "C": "I am from a China.", "D": "I from China."}, "B", "from China (thường không cần the).", 11),
            Q("Q_L01_07_08", 2, "true_false", "American can describe a person from the USA.", {"A": "True", "B": "False"}, "A", "American — người Mỹ.", 8),
            Q("Q_L01_07_09", 3, "multiple_choice", "Choose the best sentence:", {"A": "I am Vietnam.", "B": "I am from Vietnam.", "C": "I am come from Vietnam.", "D": "I from Vietnamese."}, "B", "I am from Vietnam.", 11),
            Q("Q_L01_07_10", 2, "multiple_choice", "Nationality for the UK (most common adjective in course):", {"A": "English", "B": "British", "C": "UKese", "D": "England"}, "B", "British (đáp án theo bài).", 10),
        ],
    }


def _lesson_08():
    meta = {"skill": "grammar", "topic": "wh_questions", "time_est_minutes": 15, "difficulty": 0.35}
    p1 = """### What — cái gì / tên gì

- *What is your **name**?*
- *What is this?*

**What** hỏi **nội dung / tên / vật**."""

    p2 = """### Where — ở đâu / từ đâu

- *Where are you **from**?*
- *Where is my bag?*

**Where** hỏi **địa điểm / nguồn gốc**."""

    p3 = """### Who — ai

- *Who is he?* — *He is my teacher.*

### Cấu trúc gợi ý

**Wh- + am/is/are + chủ ngữ + …?** (ở trình độ A1, nhiều mẫu cố định)

### Luyện

Đặt **6 câu** (2 What, 2 Where, 2 Who) về lớp học của bạn."""
    reading = "What is your name? My name is Linh. Where are you from? I am from Vietnam. Who is he? He is our teacher."
    return {
        "lesson_id": "L01_08",
        "lesson_name": "Question Words - What, Where, Who (Grammar)",
        "order": 8,
        "estimated_minutes": 36,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — What", "body": p1},
                {"title": "Trang 2 — Where", "body": p2},
                {"title": "Trang 3 — Who & luyện", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "What", "vi": "gì (cái gì, tên gì)"},
                {"word": "Where", "vi": "ở đâu / đâu / từ đâu"},
                {"word": "Who", "vi": "ai"},
            ],
            "examples": [
                {"english": "Where are you from?", "vietnamese": "Bạn đến từ đâu?"},
                {"english": "Who is she?", "vietnamese": "Cô ấy là ai?"},
            ],
        },
        "quizzes": [
            Q("Q_L01_08_01", 2, "multiple_choice", "_______ are you from? — I am from Vietnam.", {"A": "What", "B": "Where", "C": "Who", "D": "How"}, "B", "Where — nơi chốn / nguồn gốc.", 10),
            Q("Q_L01_08_02", 1, "fill_in_blank", "_______ is your name?", {"A": "What", "B": "Where", "C": "Who", "D": "When"}, "A", "What is your name?", 8),
            Q("Q_L01_08_03", 2, "multiple_choice", "Ghép đúng: 1. Who is she? 2. Where is she from?", {"A": "1→She is my teacher. | 2→She is from the UK.", "B": "1→She is from the UK. | 2→She is my teacher.", "C": "1→My name is Ann. | 2→I am fine.", "D": "1→I am 20. | 2→I am a student."}, "A", "Who → người; Where from → nơi.", 13),
            Q("Q_L01_08_04", 2, "multiple_choice", "_______ is that man?", {"A": "What", "B": "Where", "C": "Who", "D": "How"}, "C", "Who is that man?", 9),
            Q("Q_L01_08_05", 2, "multiple_choice", "What is your name? — _______", {"A": "I am from Hanoi.", "B": "I am Lan.", "C": "I am fine.", "D": "I am a student from."}, "B", "Trả lời tên.", 10),
            Q("Q_L01_08_06", 2, "fill_in_blank", "_______ is my book? — On the desk.", {"A": "What", "B": "Where", "C": "Who", "D": "Why"}, "B", "Where — vị trí.", 10),
            Q("Q_L01_08_07", 3, "multiple_choice", "Which question asks about a person (identity)?", {"A": "What is your phone?", "B": "Who is he?", "C": "Where is Tuesday?", "D": "What color is time?"}, "B", "Who — ai.", 12),
            Q("Q_L01_08_08", 2, "error_identification", "Tìm lỗi: 'Where is you from?'", {"A": "Where", "B": "is", "C": "you", "D": "from"}, "B", "Where **are** you from?", 12, True),
            Q("Q_L01_08_09", 2, "multiple_choice", "Who are you? — (học mẫu đáp lịch sự) — Often answered with:", {"A": "I am from Vietnam.", "B": "I'm Linh, nice to meet you.", "C": "I am 20 years old.", "D": "I am on the table."}, "B", "Giới thiệu tên + lịch sự.", 11),
            Q("Q_L01_08_10", 2, "multiple_choice", "_______ are those people? — They are my parents.", {"A": "What", "B": "Where", "C": "Who", "D": "When"}, "C", "Who — hỏi về người.", 10),
        ],
    }


def _lesson_09():
    meta = {"skill": "vocabulary", "topic": "family", "time_est_minutes": 12, "difficulty": 0.35}
    p1 = """### Gia đình cốt lõi

- **Father** / **Dad** — bố
- **Mother** / **Mom** — mẹ
- **Brother** — anh/em trai
- **Sister** — chị/em gái"""

    p2 = """### Gia đình mở rộng

- **Grandfather** / **Grandmother** — ông / bà
- **Uncle** — chú / bác / cậu (tùy văn hóa)
- **Aunt** — cô / dì / thím…

### Từ tổng

- **Family** — gia đình
- **Parents** — **bố mẹ** (cha mẹ)"""

    p3 = """### Câu mẫu

- *This is my **mother**.*
- *My **parents** are kind.*
- *I have one **sister**.*

### Bài tập

Vẽ **cây gia đình** đơn giản và ghi **10 từ** tiếng Anh."""
    reading = "My father is Tom and my mother is Sue. My brother is Tim. My sister is Anna. My uncle is Jack. We are a happy family."
    return {
        "lesson_id": "L01_09",
        "lesson_name": "Family Members (Vocabulary)",
        "order": 9,
        "estimated_minutes": 30,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Gia đình cốt lõi", "body": p1},
                {"title": "Trang 2 — Mở rộng & parents", "body": p2},
                {"title": "Trang 3 — Câu mẫu & bài tập", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "father / mother / parents", "vi": "bố / mẹ / bố mẹ"},
                {"word": "brother / sister", "vi": "anh/em trai / chị/em gái"},
                {"word": "grandfather / grandmother", "vi": "ông / bà"},
                {"word": "uncle / aunt", "vi": "chú bác / cô dì"},
                {"word": "family", "vi": "gia đình"},
            ],
            "examples": [
                {"english": "My mother and my father are my parents.", "vietnamese": "Mẹ và bố tôi là cha mẹ tôi."},
                {"english": "She is my sister.", "vietnamese": "Cô ấy là chị/em gái tôi."},
            ],
        },
        "quizzes": [
            Q("Q_L01_09_01", 1, "multiple_choice", "My mother and my father are my _______.", {"A": "brothers", "B": "parents", "C": "sisters", "D": "uncles"}, "B", "Parents = bố mẹ.", 9),
            Q("Q_L01_09_02", 1, "multiple_choice", "“Chị/em gái” trong tiếng Anh là:", {"A": "Brother", "B": "Sister", "C": "Aunt", "D": "Mom"}, "B", "Sister.", 8),
            Q("Q_L01_09_03", 2, "multiple_choice", "My father's brother is my _______.", {"A": "grandfather", "B": "uncle", "C": "cousin", "D": "brother"}, "B", "Uncle — chú/bác (cha của bạn).", 11),
            Q("Q_L01_09_04", 2, "multiple_choice", "Parents means:", {"A": "children", "B": "mother and father", "C": "only mother", "D": "cousins"}, "B", "Parents.", 8),
            Q("Q_L01_09_05", 2, "fill_in_blank", "My _____ is sixty years old. (ông)", {"A": "uncle", "B": "grandfather", "C": "brother", "D": "sister"}, "B", "Grandfather.", 10),
            Q("Q_L01_09_06", 2, "multiple_choice", "She is my mother's sister. She is my _______.", {"A": "uncle", "B": "aunt", "C": "brother", "D": "dad"}, "B", "Aunt.", 11),
            Q("Q_L01_09_07", 2, "true_false", "Brother can mean only a younger brother.", {"A": "True", "B": "False"}, "B", "Brother = anh hoặc em trai.", 10),
            Q("Q_L01_09_08", 2, "multiple_choice", "We use ___ for both formal and informal 'father' in family context:", {"A": "teacher", "B": "father / dad", "C": "student", "D": "family"}, "B", "father / dad.", 10),
            Q("Q_L01_09_09", 3, "multiple_choice", "My parents' daughter (not me, I'm a boy) could be my:", {"A": "uncle", "B": "sister", "C": "father", "D": "grandfather"}, "B", "Sister.", 12),
            Q("Q_L01_09_10", 2, "fill_in_blank", "This is my _____. He is my dad's father.", {"A": "brother", "B": "grandfather", "C": "uncle", "D": "cousin"}, "B", "Dad's father = grandfather.", 11),
        ],
    }


def _lesson_10():
    meta = {"skill": "reading", "topic": "my_family", "time_est_minutes": 15, "difficulty": 0.4}
    text = (
        "Hi, my name is Alex. I am 15 years old and I am from the USA. I am American. "
        "This is my family. Who is he? He is my father, John. He is 40 years old. "
        "Where is my mother from? She is from the UK, so she is British. "
        "I have one sister. We are a happy family."
    )
    p1 = """### Đọc tổng hợp

Đoạn kết hợp: **chào/giới thiệu**, **tuổi**, **quốc gia & quốc tịch**, **gia đình**, **câu hỏi Who/Where**, **to be**."""

    p2 = """### Chiến lược

1. Tìm **tên** và **tuổi** của Alex.
2. Bố: tên + tuổi; mẹ: **từ đâu** → quốc tịch.
3. *I have one sister* — anh/chị/em.

### Từ khóa

*from the USA / American / from the UK / British / father / mother / sister*"""

    p3 = """### Sau khi đọc

Viết **đoạn 5–7 câu** về gia đình bạn (tuổi, nghề đơn giản, quốc tịch) — dùng *I am*, *My … is*, *We are*."""
    return {
        "lesson_id": "L01_10",
        "lesson_name": "My Family (Reading)",
        "order": 10,
        "estimated_minutes": 40,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Tổng hợp kiến thức", "body": p1},
                {"title": "Trang 2 — Chiến lược đọc", "body": p2},
                {"title": "Trang 3 — Viết về gia đình bạn", "body": p3},
            ],
            "reading_passage": text,
            "reading_word_count": wc(text),
            "vocabulary": [
                {"word": "family / father / mother / sister", "vi": "gia đình / bố / mẹ / chị em gái"},
                {"word": "from the USA / American", "vi": "từ Mỹ / người Mỹ"},
                {"word": "from the UK / British", "vi": "từ Anh / người Anh"},
            ],
            "examples": [
                {"english": "Where is my mother from?", "vietnamese": "Mẹ tôi đến từ đâu?"},
                {"english": "We are a happy family.", "vietnamese": "Chúng tôi là một gia đình hạnh phúc."},
            ],
        },
        "quizzes": [
            Q("Q_L01_10_01", 2, "multiple_choice", "Where is Alex from?", {"A": "The USA", "B": "The UK", "C": "Vietnam", "D": "Japan"}, "A", "from the USA.", 10),
            Q("Q_L01_10_02", 2, "true_false", "Alex's mother is American.", {"A": "True", "B": "False"}, "B", "Mother is from the UK / British.", 11),
            Q("Q_L01_10_03", 2, "multiple_choice", "How old is John (the father)?", {"A": "15", "B": "40", "C": "22", "D": "50"}, "B", "He is 40 years old.", 10),
            Q("Q_L01_10_04", 2, "multiple_choice", "What nationality is Alex?", {"A": "British", "B": "American", "C": "Japanese", "D": "Vietnamese"}, "B", "I am American.", 10),
            Q("Q_L01_10_05", 2, "multiple_choice", "Who is John?", {"A": "Alex's mother", "B": "Alex's father", "C": "Alex's sister", "D": "Alex's teacher"}, "B", "He is my father, John.", 10),
            Q("Q_L01_10_06", 2, "multiple_choice", "Where is Alex's mother from?", {"A": "The USA", "B": "The UK", "C": "China", "D": "Japan"}, "B", "She is from the UK.", 10),
            Q("Q_L01_10_07", 2, "true_false", "Alex has two sisters.", {"A": "True", "B": "False"}, "B", "I have one sister.", 9),
            Q("Q_L01_10_08", 3, "multiple_choice", "She is British because:", {"A": "She is 40", "B": "She is from the UK", "C": "She is Alex's father", "D": "She is 15"}, "B", "from the UK → British.", 12),
            Q("Q_L01_10_09", 2, "fill_in_blank", "Alex is _______ years old.", {"A": "40", "B": "15", "C": "22", "D": "50"}, "B", "I am 15 years old.", 9),
            Q("Q_L01_10_10", 3, "multiple_choice", "Best summary:", {"A": "Alex is a teacher in Vietnam.", "B": "Alex introduces family: US background, parents' ages/origin, one sister.", "C": "Alex has no family.", "D": "Alex is British and his mom is American."}, "B", "Tóm tắt đúng đoạn.", 13),
        ],
    }
