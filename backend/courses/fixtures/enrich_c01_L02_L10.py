"""
Làm giàu L01_02–L01_10: theory_pages (3 trang) + 10 quiz/bài.
Chạy từ thư mục fixtures: python enrich_c01_L02_L10.py
"""
from __future__ import annotations

import json
from pathlib import Path

P = Path(__file__).resolve().parent / "course_C01_foundation.json"


def Q(qid, diff, qtype, text, opts, ans, hint, rt=10, hint_used=False):
    return {
        "quiz_id": qid,
        "difficulty_level": diff,
        "question_type": qtype,
        "question_text": text,
        "options": opts,
        "correct_answer": ans,
        "hint_text": hint,
        "expected_behavior_simulation": {"avg_response_time_sec": rt, "likely_to_use_hint": hint_used},
    }


ENRICH: dict = {}

# --- L01_02 ---
ENRICH["L01_02"] = {
    "estimated_minutes": 45,
    "theory_pages": [
        {
            "title": "Trang 1 — Nhà & văn phòng",
            "body": """### Mục tiêu

Gọi đúng tên **đồ vật** trong **nhà** (*home*) và **văn phòng** (*office*), học theo **phòng** (*kitchen*, *bedroom*, *living room*, *meeting room*) thay vì học list rời.

### Gợi ý ghi nhớ

- **Văn phòng:** *desk*, *chair*, *computer*, *printer*, *notebook*, *lamp*, *whiteboard*.
- **Nhà:** *fridge*, *stove*, *sofa*, *TV*, *bed*…
- Luôn thử đặt từ trong **câu có mạo từ**: *a comfortable chair*, *the printer is broken*.

### Vì sao học theo bối cảnh?

Não lưu theo **mạng nghĩa** (bếp — fridge/stove; làm việc — desk/computer) sẽ nhớ lâu hơn học bảng từ đơn điệu.""",
        },
        {
            "title": "Trang 2 — Số ít/nhiều & there is/are",
            "body": """### Danh từ đếm được

- Số nhiều thường thêm **-s**: *one desk — two desks*.
- **Furniture** (*đồ đạc*) là **không đếm được** — không nói *many furnitures*; dùng *a lot of furniture* / *some furniture*.

### There is / There are

- *There **is** a printer on the desk.* (một vật)
- *There **are** two chairs.* (nhiều vật)

### Hỏi vị trí & đồ vật

- *What is this / that?* — *Where is my phone?* — *Where are the keys?*

> Luyện: mô tả góc bàn học của bạn bằng 4–5 câu *There is/are …*""",
        },
        {
            "title": "Trang 3 — Collocation & thói quen đọc",
            "body": """### Cụm động từ hay gặp

| Cụm | Nghĩa gợi ý |
|-----|-------------|
| *sit on the chair* | ngồi **trên** ghế |
| *turn on / off the light* | bật/tắt đèn |
| *open / close the door* | mở/đóng cửa |

### Đọc email công việc

Trong email ngắn, khoanh các **danh từ chỉ đồ vật** — bạn sẽ thấy cùng từ (*printer*, *desk*) lặp lại: đó là từ **cốt lõi** của môi trường làm việc.

### Bài tập nhanh

1. Vẽ sơ đồ một phòng và viết **8 câu** *There is/are*.
2. Đặt *Where is…?* và trả lời bằng *in/on/under/next to*.""",
        },
    ],
    "quizzes": [
        Q("Q_L01_02_01", 1, "fill_in_blank", "There is a _____ on the wall in the meeting room.", {"A": "sofa", "B": "whiteboard", "C": "spoon", "D": "sink"}, "B", "Trong phòng họp thường có bảng (whiteboard).", 10),
        Q("Q_L01_02_02", 2, "synonym_antonym", "Từ gần nghĩa nhất với 'begin' trong 'begin the meeting':", {"A": "finish", "B": "start", "C": "cancel", "D": "delay"}, "B", "Begin ≈ start.", 11),
        Q("Q_L01_02_03", 2, "fill_in_blank", "I need to print this file. Where is the _____?", {"A": "fridge", "B": "printer", "C": "pillow", "D": "bathtub"}, "B", "In ra giấy dùng máy in.", 9),
        Q("Q_L01_02_04", 3, "error_identification", "Tìm lỗi: 'There are many furnitures in the room.'", {"A": "There are", "B": "many", "C": "furnitures", "D": "in the room"}, "C", "Furniture không đếm được, không thêm -s.", 15, True),
        Q("Q_L01_02_05", 2, "multiple_choice", "Chọn câu đúng:", {"A": "I sit on the chair.", "B": "I sit in the chair.", "C": "I sit at the chair.", "D": "I sit to the chair."}, "A", "Ngồi trên ghế: sit on the chair.", 12),
        Q("Q_L01_02_06", 2, "fill_in_blank", "There _____ two computers on the desk.", {"A": "is", "B": "are", "C": "am", "D": "be"}, "B", "Two computers → are.", 9),
        Q("Q_L01_02_07", 2, "fill_in_blank", "We keep food in the _____.", {"A": "printer", "B": "fridge", "C": "sofa", "D": "whiteboard"}, "B", "Đồ ăn — tủ lạnh.", 10),
        Q("Q_L01_02_08", 2, "multiple_choice", "Chọn câu đúng:", {"A": "I need a paper for the printer.", "B": "I need some paper for the printer.", "C": "I need paper for a printer.", "D": "I need papers for printer."}, "B", "Paper thường không đếm; some paper — tự nhiên.", 12),
        Q("Q_L01_02_09", 3, "fill_in_blank", "Please turn _____ the lights when you leave.", {"A": "of", "B": "off", "C": "out", "D": "down"}, "B", "turn off the lights — tắt đèn.", 11),
        Q("Q_L01_02_10", 3, "error_identification", "Tìm lỗi: 'There is two lamps in the room.'", {"A": "There is", "B": "two", "C": "lamps", "D": "in the room"}, "A", "Two lamps → There are.", 14, True),
    ],
}

# --- L01_03 ---
ENRICH["L01_03"] = {
    "estimated_minutes": 45,
    "theory_pages": [
        {
            "title": "Trang 1 — Ngoại hình & tính cách",
            "body": """### Hai trục

- **Appearance** (ngoại hình): *tall/short*, *young/old*, *slim*, *curly/straight hair*…
- **Personality** (tính cách): *friendly*, *shy*, *outgoing*, *patient*, *serious*, *funny*…

### Cách mô tả nhanh

- *She has long black hair.* — *He is of medium height.* — *They look happy.*

> Tập **không** lặp *She is…* ở mọi câu — xen *She has…*, *Her eyes are…*, *She looks…*""",
        },
        {
            "title": "Trang 2 — Hỏi đúng: look like / like",
            "body": """### Ba câu hỏi dễ nhầm

| Ý muốn hỏi | Câu hay dùng |
|------------|----------------|
| Trông **như thế nào**? | *What does she **look like**?* |
| **Tính cách** / người thế nào? | *What is he **like**?* |
| **Thích** gì? | *What does she **like**?* |

### Tính từ + danh từ

- *a friendly neighbor* — *a serious boss* — *a shy classmate*

### Nối ý

- *and* / *but*: *He is friendly **but** a little shy.*""",
        },
        {
            "title": "Trang 3 — Viết & nói",
            "body": """### Viết đoạn ngắn

1. 3–4 câu về **một người** (ngoại hình + tính cách).
2. Thêm **một chi tiết cụ thể** (màu tóc, nụ cười, thói quen).

### Ghi âm

Đọc đoạn của bạn trong **40 giây** — nghe lại và sửa *he/she* nếu nhầm.

### So sánh nhẹ

- *taller than* — *more outgoing than* (khi so hai người).""",
        },
    ],
    "quizzes": [
        Q("Q_L01_03_01", 1, "fill_in_blank", "My best friend is very _____. She talks to everyone.", {"A": "shy", "B": "outgoing", "C": "invisible", "D": "empty"}, "B", "Hay trò chuyện → outgoing.", 9),
        Q("Q_L01_03_02", 2, "synonym_antonym", "Từ gần nghĩa với 'kind' (tốt bụng):", {"A": "mean", "B": "helpful", "C": "rude", "D": "lazy"}, "B", "Helpful gần nghĩa tích cực như kind.", 11),
        Q("Q_L01_03_03", 2, "multiple_choice", "Câu hỏi phù hợp để hỏi **ngoại hình**:", {"A": "What is she like?", "B": "What does she look like?", "C": "What does she like?", "D": "How does she like?"}, "B", "Look like = trông như thế nào.", 11),
        Q("Q_L01_03_04", 3, "error_identification", "Tìm lỗi: 'He has a very kindness smile.'", {"A": "He has", "B": "a very", "C": "kindness", "D": "smile"}, "C", "Cần tính từ: kind smile.", 14, True),
        Q("Q_L01_03_05", 3, "fill_in_blank", "She has _____ hair. It is not straight.", {"A": "curly", "B": "medium", "C": "outgoing", "D": "patient"}, "A", "Không thẳng → có thể curly.", 10),
        Q("Q_L01_03_06", 2, "fill_in_blank", "He is very _____. He doesn't talk much in class.", {"A": "outgoing", "B": "shy", "C": "tall", "D": "curly"}, "B", "Ít nói → shy.", 10),
        Q("Q_L01_03_07", 2, "multiple_choice", "Chọn câu đúng:", {"A": "What does your brother like?", "B": "What does your brother look like?", "C": "How is your brother like?", "D": "What is your brother look like?"}, "B", "Hỏi ngoại hình: What … look like?", 12),
        Q("Q_L01_03_08", 2, "fill_in_blank", "Anna _____ straight brown hair.", {"A": "is", "B": "has", "C": "have", "D": "looks"}, "B", "Has + kiểu tóc.", 10),
        Q("Q_L01_03_09", 3, "multiple_choice", "Từ trái nghĩa gần nhất với 'patient' (kiên nhẫn):", {"A": "calm", "B": "impatient", "C": "friendly", "D": "quiet"}, "B", "Impatient = thiếu kiên nhẫn.", 12),
        Q("Q_L01_03_10", 3, "error_identification", "Tìm lỗi: 'She is a long hair.'", {"A": "She is", "B": "a", "C": "long", "D": "hair"}, "A", "Tóc: She has long hair / Her hair is long.", 13, True),
    ],
}

# --- L01_04 ---
ENRICH["L01_04"] = {
    "estimated_minutes": 45,
    "theory_pages": [
        {
            "title": "Trang 1 — Nói về nghề",
            "body": """### Vì sao chủ đề *jobs* quan trọng?

Xuất hiện trong **giao tiếp hàng ngày**, **giới thiệu**, **phỏng vấn** — cần vừa **danh từ nghề**, vừa **mẫu câu ổn định**.

### Hai cách phổ biến

- *I **am** a teacher.* (*to be* + nghề)
- *I **teach** English.* (hiện tại đơn + hành động)

### work + giới từ

- *work **in** a hospital* — *work **at** a bank* — *work **for** a company*""",
        },
        {
            "title": "Trang 2 — a / an & câu hỏi",
            "body": """### Mạo từ với nghề

- *a teacher* — *an engineer* (**an** trước nguyên âm)
- Tránh: ~~*I am engineer*~~

### Câu hỏi thường gặp

| Câu | Khi nào dùng |
|-----|----------------|
| *What do you do?* | Hỏi nghề (rất phổ biến) |
| *What is your job?* | Hỏi công việc |
| *Where do you work?* | Hỏi địa điểm |

### Tính từ mô tả công việc

- *busy*, *stressful*, *creative*, *flexible*""",
        },
        {
            "title": "Trang 3 — Giới thiệu người khác & luyện tập",
            "body": """### Nói về người thân

- *My father is a driver.*
- *Her sister works in retail.*

### Nhóm chủ đề

Học theo **lĩnh vực**: y tế, giáo dục, công nghệ, dịch vụ — não sẽ “bắt cặp” từ nhanh hơn.

### Bài tập

- Viết **2–3 câu** về nghề của bạn hoặc người thân.
- Lập bảng: **Từ nghề** — **một câu mô tả tiếng Việt** — **dịch sang tiếng Anh**.""",
        },
    ],
    "quizzes": [
        Q("Q_L01_04_01", 1, "fill_in_blank", "He is _____ engineer. He designs bridges.", {"A": "a", "B": "an", "C": "the", "D": "—"}, "B", "Engineer bắt đầu bằng nguyên âm → an.", 9),
        Q("Q_L01_04_02", 2, "synonym_antonym", "Từ gần nghĩa với 'occupation':", {"A": "holiday", "B": "job", "C": "weather", "D": "furniture"}, "B", "Occupation ≈ job.", 11),
        Q("Q_L01_04_03", 2, "multiple_choice", "Chọn câu đúng:", {"A": "She is teacher.", "B": "She is a teacher.", "C": "She is an teacher.", "D": "She are a teacher."}, "B", "A teacher — phụ âm → a.", 10),
        Q("Q_L01_04_04", 3, "error_identification", "Tìm lỗi: 'My uncle work in a factory.'", {"A": "My uncle", "B": "work", "C": "in", "D": "a factory"}, "B", "Ngôi 3 số ít: works.", 14, True),
        Q("Q_L01_04_05", 2, "fill_in_blank", "Where _____ you work?", {"A": "do", "B": "does", "C": "is", "D": "are"}, "A", "You + do trong câu hỏi thường.", 10),
        Q("Q_L01_04_06", 2, "multiple_choice", "Câu lịch sự để hỏi nghề:", {"A": "How much is your salary?", "B": "What do you do?", "C": "How old are you?", "D": "Where is your house?"}, "B", "What do you do? — hỏi nghề.", 9),
        Q("Q_L01_04_07", 2, "fill_in_blank", "She works _____ a nurse _____ a hospital.", {"A": "as / in", "B": "like / on", "C": "for / at", "D": "to / by"}, "A", "work as a nurse; in a hospital.", 12),
        Q("Q_L01_04_08", 2, "fill_in_blank", "I work _____ a tech company.", {"A": "to", "B": "for", "C": "at", "D": "in"}, "B", "work for + công ty.", 10),
        Q("Q_L01_04_09", 3, "multiple_choice", "Chọn câu đúng:", {"A": "He is an driver.", "B": "He is a driver.", "C": "He is driver.", "D": "He are a driver."}, "B", "Driver — phụ âm → a.", 11),
        Q("Q_L01_04_10", 3, "error_identification", "Tìm lỗi: 'She work as a nurse.'", {"A": "She", "B": "work", "C": "as", "D": "a nurse"}, "B", "She works.", 13, True),
    ],
}

# --- L01_05 ---
ENRICH["L01_05"] = {
    "estimated_minutes": 45,
    "theory_pages": [
        {
            "title": "Trang 1 — At / On / In",
            "body": """### Gợi ý nhanh

| Giới từ | Thường dùng |
|---------|-------------|
| **at** | điểm (*at the door*), giờ (*at 8 a.m.*), hoạt động (*at work*) |
| **on** | bề mặt (*on the table*), ngày (*on Monday*), xe công cộng (*on the bus*) |
| **in** | trong không gian (*in the room*), tháng/năm/thành phố lớn (*in July*, *in Hanoi*) |

### Thời gian

- *at* + giờ — *on* + ngày trong tuần — *in* + tháng/năm.""",
        },
        {
            "title": "Trang 2 — Địa điểm & lỗi thường gặp",
            "body": """### Thành phố & địa chỉ

- *in Hanoi* — *in Vietnam*
- *at 10 Nguyen Hue Street* (số nhà cụ thể)

### at school / in the school

- *at school* — đi học / hoạt động trường
- *in the school* — bên trong tòa nhà

### Lỗi phổ biến

- ~~*at Hanoi*~~ → *in Hanoi*
- ~~*in Monday*~~ → *on Monday*""",
        },
        {
            "title": "Trang 3 — Luyện mô tả",
            "body": """### Miêu tả phòng

*The clock is on the wall. The books are in the bag. I'm at home.*

### Bài tập

Viết **10 câu** mô tả đường đi từ nhà đến trường — mỗi câu có ít nhất **một** giới từ thời gian hoặc vị trí.

### Cụm cố định

*on the left/right* — *in the middle* — *at the corner*""",
        },
    ],
    "quizzes": [
        Q("Q_L01_05_01", 1, "fill_in_blank", "See you _____ 5 p.m.", {"A": "in", "B": "on", "C": "at", "D": "by"}, "C", "Giờ cụ thể → at.", 8),
        Q("Q_L01_05_02", 2, "fill_in_blank", "The picture is _____ the wall.", {"A": "at", "B": "on", "C": "in", "D": "to"}, "B", "Treo trên bề mặt → on.", 9),
        Q("Q_L01_05_03", 2, "synonym_antonym", "Từ KHÔNG cùng nhóm với in/on/at (vị trí):", {"A": "under", "B": "behind", "C": "happy", "D": "next to"}, "C", "Happy — tính từ cảm xúc.", 12),
        Q("Q_L01_05_04", 3, "error_identification", "Tìm lỗi: 'I will see you in Monday.'", {"A": "I will", "B": "see you", "C": "in Monday", "D": "—"}, "C", "Ngày trong tuần → on Monday.", 13, True),
        Q("Q_L01_05_05", 3, "multiple_choice", "Chọn câu tự nhiên nhất:", {"A": "I study on university.", "B": "I study in a university.", "C": "I study at a university.", "D": "I study to university."}, "C", "at a university — học tại trường.", 12),
        Q("Q_L01_05_06", 2, "fill_in_blank", "My parents live _____ Da Nang.", {"A": "at", "B": "on", "C": "in", "D": "to"}, "C", "Thành phố → in.", 9),
        Q("Q_L01_05_07", 2, "fill_in_blank", "The keys are _____ the table.", {"A": "at", "B": "on", "C": "in", "D": "by"}, "B", "Trên mặt bàn → on.", 9),
        Q("Q_L01_05_08", 2, "fill_in_blank", "We have a meeting _____ Friday morning.", {"A": "at", "B": "on", "C": "in", "D": "by"}, "B", "Friday morning → on.", 10),
        Q("Q_L01_05_09", 3, "error_identification", "Tìm lỗi: 'She is on the kitchen.'", {"A": "She is", "B": "on", "C": "the kitchen", "D": "—"}, "B", "Trong bếp → in the kitchen.", 13, True),
        Q("Q_L01_05_10", 2, "multiple_choice", "Chọn câu đúng:", {"A": "I wake up in 6 a.m.", "B": "I wake up at 6 a.m.", "C": "I wake up on 6 a.m.", "D": "I wake up by 6 a.m."}, "B", "Giờ → at.", 10),
    ],
}

# --- L01_06 ---
ENRICH["L01_06"] = {
    "estimated_minutes": 42,
    "theory_pages": [
        {
            "title": "Trang 1 — Chào & mức độ lịch sự",
            "body": """### Mở đầu hội thoại

- Thân mật: *Hi* — *Hello*
- Trang trọng hơn: *Good morning / afternoon / evening*

### Hỏi thăm

- *How are you?* — *How are you today?*
- Trả lời ngắn: *I'm fine, thanks.* — *Not bad.* — *A bit tired.*

> Sau đó nhớ hỏi lại: *And you?* — *How about you?*""",
        },
        {
            "title": "Trang 2 — Nice to meet / How do you do",
            "body": """### Lần đầu / lần sau

- *Nice to **meet** you.* (lần đầu)
- *Nice to **see** you.* (gặp lại)

### Dễ nhầm

| Câu | Ý |
|-----|---|
| *What do you do?* | Hỏi **nghề** |
| *How do you do?* | Chào rất trang trọng (hiếm) — đáp thường lặp *How do you do?* |
| *How are you doing?* | Thân mật (Mỹ) |""",
        },
        {
            "title": "Trang 3 — Email & ứng xử",
            "body": """### Email công việc

- Mở: *Dear …* hoặc *Hi team*
- Kết: *Best regards* — *Sincerely* — *Thanks*

### Ứng xử nhẹ

- Người khác ho: *Bless you.*
- Tin xấu: *I'm sorry to hear that.*

### Bài tập

Viết **3 lời chào** cho: bạn thân — giảng viên — khách hàng (mức độ lịch sự khác nhau).""",
        },
    ],
    "quizzes": [
        Q("Q_L01_06_01", 1, "multiple_choice", "Câu trả lời phù hợp cho 'How are you?' (giao tiếp thường):", {"A": "I'm a student.", "B": "I'm fine, thanks.", "C": "I am in Hanoi.", "D": "I like coffee."}, "B", "Hỏi sức khỏe → trả lời trạng thái.", 8),
        Q("Q_L01_06_02", 2, "fill_in_blank", "_____ to meet you.", {"A": "Nice", "B": "Bad", "C": "Angry", "D": "Slow"}, "A", "Nice to meet you — cố định.", 7),
        Q("Q_L01_06_03", 2, "synonym_antonym", "Từ trái nghĩa với 'polite':", {"A": "kind", "B": "rude", "C": "gentle", "D": "friendly"}, "B", "Rude = thô lỗ.", 11),
        Q("Q_L01_06_04", 3, "error_identification", "Tìm lỗi: 'How do you do? — I am fine, thank you.'", {"A": "How do you do", "B": "I am", "C": "fine", "D": "thank you"}, "A", "How do you do? không trả lời như How are you.", 15, True),
        Q("Q_L01_06_05", 2, "fill_in_blank", "_____ you tomorrow!", {"A": "See", "B": "Watch", "C": "Look", "D": "Meet"}, "A", "See you tomorrow.", 8),
        Q("Q_L01_06_06", 2, "multiple_choice", "Chọn lời đáp tự nhiên: 'Good morning! How are you?'", {"A": "I'm a teacher.", "B": "Morning! I'm good, thanks.", "C": "I am at school.", "D": "I like morning."}, "B", "Đáp chào + trạng thái.", 9),
        Q("Q_L01_06_07", 2, "fill_in_blank", "Long time no see! How have you _____?", {"A": "been", "B": "be", "C": "was", "D": "being"}, "A", "How have you been?", 10),
        Q("Q_L01_06_08", 2, "multiple_choice", "Câu nào hỏi **nghề**?", {"A": "How are you?", "B": "What do you do?", "C": "Where are you from?", "D": "How old are you?"}, "B", "What do you do?", 9),
        Q("Q_L01_06_09", 3, "fill_in_blank", "It was nice _____ you again.", {"A": "meet", "B": "to meet", "C": "meeting", "D": "met"}, "B", "Nice to meet you again.", 11),
        Q("Q_L01_06_10", 3, "error_identification", "Tìm lỗi: 'She is fine. How is you?'", {"A": "She is", "B": "fine", "C": "How is you", "D": "—"}, "C", "How **are** you?", 12, True),
    ],
}

# --- L01_07 ---
ENRICH["L01_07"] = {
    "estimated_minutes": 45,
    "theory_pages": [
        {
            "title": "Trang 1 — Hỏi giá & thanh toán",
            "body": """### Câu cốt lõi

- *How much **is** this?* — *How much **are** these?* (**is/are** khớp *this/these*)
- *Can I pay **by card**?* — *Do you take credit cards?*

### Quyết định

- *I'll **take** it.* (= tôi mua)
- *It's too **expensive**.*

### Mở đầu lịch sự

> *Excuse me, …* trước khi chặn nhân viên.""",
        },
        {
            "title": "Trang 2 — Cỡ, thử đồ, giảm giá",
            "body": """### Size & thử đồ

- *small / medium / large*
- *Can I **try this on**?* (quần áo)

### Giá & khuyến mãi

- *Is there a **discount**?*
- *Is it **on sale**?*

### Trả giá (chợ)

- *Can you give me a **better price**?*

### Sau khi trả tiền

*Here's your change.* — *Keep the change.* (tùy văn hóa)""",
        },
        {
            "title": "Trang 3 — Siêu thị & nhãn",
            "body": """### Trong siêu thị

- *Where can I find milk?*
- *Which aisle is the bread?*

### Nhãn sản phẩm

- *best before* — *expiry date* — *made in…*

### Bài tập

Lập **shopping list** một tuần bằng tiếng Anh; đóng vai khách — nhân viên hỏi giá từng món.""",
        },
    ],
    "quizzes": [
        Q("Q_L01_07_01", 1, "fill_in_blank", "_____ much are these shoes?", {"A": "What", "B": "How", "C": "Which", "D": "When"}, "B", "How much — hỏi giá.", 8),
        Q("Q_L01_07_02", 2, "synonym_antonym", "Từ gần nghĩa với 'cheap':", {"A": "expensive", "B": "inexpensive", "C": "heavy", "D": "slow"}, "B", "Inexpensive ≈ cheap.", 11),
        Q("Q_L01_07_03", 2, "multiple_choice", "Câu lịch sự khi nhờ nhân viên:", {"A": "Hey! Come here!", "B": "Excuse me, can you help me?", "C": "You! Price!", "D": "Give me that!"}, "B", "Excuse me…", 9),
        Q("Q_L01_07_04", 3, "error_identification", "Tìm lỗi: 'How much is these books?'", {"A": "How much", "B": "is", "C": "these", "D": "books"}, "B", "These books → are.", 13, True),
        Q("Q_L01_07_05", 3, "fill_in_blank", "This jacket is nice. I think I'll _____ it.", {"A": "take", "B": "make", "C": "do", "D": "go"}, "A", "I'll take it — tôi mua.", 10),
        Q("Q_L01_07_06", 2, "fill_in_blank", "Do you have this in _____ Large? (cỡ áo)", {"A": "size", "B": "number", "C": "kind", "D": "type"}, "A", "Size Large — cỡ.", 10),
        Q("Q_L01_07_07", 2, "multiple_choice", "Chọn câu đúng:", {"A": "How much is this shirts?", "B": "How much are these shirts?", "C": "How much are this shirt?", "D": "How much be these shirts?"}, "B", "These shirts → are.", 11),
        Q("Q_L01_07_08", 2, "fill_in_blank", "Is there any _____ on this item?", {"A": "discount", "B": "expensive", "C": "money", "D": "pay"}, "A", "Discount — giảm giá.", 10),
        Q("Q_L01_07_09", 3, "multiple_choice", "Từ trái nghĩa gần nhất với 'expensive':", {"A": "cheap", "B": "large", "C": "new", "D": "soft"}, "A", "Cheap — rẻ.", 10),
        Q("Q_L01_07_10", 3, "error_identification", "Tìm lỗi: 'Can I try on it?'", {"A": "Can I", "B": "try on it", "C": "—", "D": "—"}, "B", "Đại từ: try **it** on.", 13, True),
    ],
}

# --- L01_08 ---
ENRICH["L01_08"] = {
    "estimated_minutes": 45,
    "theory_pages": [
        {
            "title": "Trang 1 — Trình tự gọi món",
            "body": """### Các bước

1. Xin bàn / ngồi: *A table for two, please.*
2. Xin menu: *Could I have the menu?*
3. Gọi món: *I'd like …* — *I'll have …*
4. Sau bữa: *Could we have the **bill**, please?* (Anh) / *Check, please?* (Mỹ)

### Lịch sự

Luôn có *please* / *thank you* khi phù hợp.""",
        },
        {
            "title": "Trang 2 — Đồ uống & dị ứng",
            "body": """### Nước

- *still water* / *sparkling water*
- *A glass of orange juice, please.*

### Dị ứng & món chay

- *I'm **allergic to** seafood.*
- *Is this **vegetarian**?*

### Độ cay

*mild* — *medium* — *spicy* — *Not too spicy, please.*""",
        },
        {
            "title": "Trang 3 — Bữa ăn & takeaway",
            "body": """### Cấu trúc bữa

*starter* — *main course* — *dessert*

### Sau bữa

- *The food was delicious.*
- *Could we have some **takeaway** boxes?*

### Bài tập

Đọc menu tiếng Anh trên web nhà hàng — ghi 5 món và cách bạn gọi lịch sự.""",
        },
    ],
    "quizzes": [
        Q("Q_L01_08_01", 1, "fill_in_blank", "_____ I have the menu, please?", {"A": "Could", "B": "Should", "C": "Must", "D": "May not"}, "A", "Could I have… — xin menu.", 9),
        Q("Q_L01_08_02", 2, "multiple_choice", "Cách gọi món lịch sự:", {"A": "I want food now.", "B": "I'll have the pasta, please.", "C": "Give pasta!", "D": "Pasta me!"}, "B", "I'll have … please.", 10),
        Q("Q_L01_08_03", 2, "synonym_antonym", "Trong nhà hàng Mỹ, từ thường dùng thay 'bill':", {"A": "check", "B": "letter", "C": "ticket", "D": "note"}, "A", "Check, please.", 11),
        Q("Q_L01_08_04", 4, "error_identification", "Tìm lỗi: 'Can I have a coffee? — Yes, I can.'", {"A": "Can I have", "B": "a coffee", "C": "Yes, I can", "D": "—"}, "C", "Đáp: Certainly / Here you are.", 16, True),
        Q("Q_L01_08_05", 3, "fill_in_blank", "I'm _____ to nuts. I can't eat this cake.", {"A": "allergic", "B": "happy", "C": "ready", "D": "full"}, "A", "Allergic to.", 10),
        Q("Q_L01_08_06", 2, "fill_in_blank", "Are you ready to _____?", {"A": "order", "B": "ordering", "C": "ordered", "D": "orders"}, "A", "Ready to order.", 9),
        Q("Q_L01_08_07", 2, "multiple_choice", "Khách muốn nước cam:", {"A": "I am orange juice.", "B": "A glass of orange juice, please.", "C": "Give juice orange.", "D": "I want juice now."}, "B", "A glass of orange juice, please.", 10),
        Q("Q_L01_08_08", 2, "fill_in_blank", "Could we have the _____, please? (hóa đơn — Anh)", {"A": "check", "B": "bill", "C": "letter", "D": "menu"}, "B", "Bill (Anh); check (Mỹ).", 10),
        Q("Q_L01_08_09", 3, "multiple_choice", "Chọn câu đúng:", {"A": "I'd like the soup and a salad.", "B": "I liking the soup.", "C": "I'd like soup and salading.", "D": "I want soup now immediately."}, "A", "I'd like … — lịch sự.", 11),
        Q("Q_L01_08_10", 3, "error_identification", "Tìm lỗi: 'I am allergic with seafood.'", {"A": "I am", "B": "allergic", "C": "with", "D": "seafood"}, "C", "Allergic **to** seafood.", 13, True),
    ],
}

# --- L01_09 ---
ENRICH["L01_09"] = {
    "estimated_minutes": 48,
    "theory_pages": [
        {
            "title": "Trang 1 — Đọc hiểu nền tảng",
            "body": """### Mục tiêu khi đọc

- Nắm **chủ đề** (topic)
- **Scanning:** tìm số, tên, địa điểm, nghề nhanh
- Ghi **keywords** (từ khóa) thay vì đọc từng chữ

### Đoạn giới thiệu bản thân thường có

*Tên — tuổi/quê — học/làm — sở thích — mục tiêu*

Các mẫu: *My name is…*, *I come from…*, *I study…*, *I hope to…*""",
        },
        {
            "title": "Trang 2 — Skimming & đại từ",
            "body": """### Skimming

Đọc **câu đầu** mỗi đoạn (nếu có nhiều đoạn) để biết hướng bài.

### Theo dõi nhân vật

Gạch *he/she/I* — tránh nhầm người khi câu hỏi hỏi *he* hay *she*.

### Paraphrase trong đề

Đề có thể viết khác văn bản nhưng **cùng nghĩa**: *want to* ≈ *hope to* ≈ *would like to*.""",
        },
        {
            "title": "Trang 3 — Trả lời đúng bài",
            "body": """### True/False & trắc nghiệm

Chỉ căn cứ **văn bản** — không thêm thông tin ngoài đoạn.

### Suy luận có giới hạn

Nếu bài không nhắc **lương**, không chọn đáp án có lương.

### Luyện tập

Đọc lướt 1 phút → trả lời câu hỏi **không nhìn lại** → đọc lại kiểm tra.""",
        },
    ],
    "quizzes": [
        Q("Q_L01_09_01", 2, "multiple_choice", "Theo đoạn văn mẫu trong bài, Minh đang học gì?", {"A": "Medicine", "B": "Information technology", "C": "English literature", "D": "History"}, "B", "study information technology.", 12),
        Q("Q_L01_09_02", 2, "fill_in_blank", "Minh lives _____ his cousin.", {"A": "with", "B": "and", "C": "to", "D": "for"}, "A", "Live with.", 10),
        Q("Q_L01_09_03", 3, "multiple_choice", "Điều nào KHÔNG được nói trong đoạn mẫu?", {"A": "Minh is 22.", "B": "Minh plays football every day.", "C": "Minh wants better English.", "D": "Minh is from Da Nang."}, "B", "Đoạn có badminton, không có football.", 14),
        Q("Q_L01_09_04", 3, "synonym_antonym", "Từ 'hope' trong 'I hope to work…' gần nghĩa nhất với:", {"A": "wish", "B": "forget", "C": "refuse", "D": "hate"}, "A", "Hope / wish — mong muốn.", 11),
        Q("Q_L01_09_05", 4, "error_identification", "Câu nào có lỗi ngữ pháp?", {"A": "I am a student.", "B": "I have twenty-two years old.", "C": "I like reading.", "D": "I come from Da Nang."}, "B", "I am twenty-two years old.", 14, True),
        Q("Q_L01_09_06", 2, "multiple_choice", "Theo đoạn mẫu, trong thời gian rảnh Minh thích:", {"A": "football", "B": "science fiction & badminton", "C": "swimming", "D": "cooking"}, "B", "reading science fiction and playing badminton.", 12),
        Q("Q_L01_09_07", 2, "fill_in_blank", "Minh wants to work for an _____ company after graduation.", {"A": "national", "B": "international", "C": "local", "D": "small"}, "B", "international company — trong đoạn.", 11),
        Q("Q_L01_09_08", 3, "multiple_choice", "Ý chính của đoạn mẫu gần nhất với:", {"A": "Minh chỉ thích thể thao.", "B": "Minh giới thiệu bản thân và mục tiêu học tiếng Anh.", "C": "Minh mô tả căn hộ chi tiết.", "D": "Minh nói về gia đình."}, "B", "Tổng hợp: bản thân + học tập + mục tiêu.", 13),
        Q("Q_L01_09_09", 3, "fill_in_blank", "He comes _____ Da Nang.", {"A": "to", "B": "from", "C": "at", "D": "in"}, "B", "come from + nơi.", 10),
        Q("Q_L01_09_10", 3, "error_identification", "Tìm lỗi: 'I enjoy to read science fiction.'", {"A": "I enjoy", "B": "to read", "C": "science", "D": "fiction"}, "B", "Enjoy + V-ing: enjoy reading.", 14, True),
    ],
}

# --- L01_10 ---
ENRICH["L01_10"] = {
    "estimated_minutes": 48,
    "theory_pages": [
        {
            "title": "Trang 1 — Thói quen & hiện tại đơn",
            "body": """### Diễn tả routine

Dùng **hiện tại đơn** + trạng từ tần suất: *always*, *usually*, *often*, *sometimes*, *never*, *rarely*.

### Trình tự một ngày

*wake up* → *have breakfast* → *go to work* → *have lunch* → *come home* → *have dinner* → *go to bed*

- Giờ: *at 6:30 a.m.*""",
        },
        {
            "title": "Trang 2 — Câu hỏi về thời gian",
            "body": """### Hỏi giờ & tần suất

- *What time do you…?*
- *How often do you…?* → *once a week*, *twice a month*

### every day / daily

*I exercise every day.* (= *daily*)

### Weekdays vs weekends

*On weekdays…* — *At weekends…*""",
        },
        {
            "title": "Trang 3 — Đọc & viết nhật ký",
            "body": """### Khi đọc đoạn routine

Gạch **động từ** theo thứ tự và **mốc giờ**.

### Viết

- Nhật ký **5 dòng/buổi tối** bằng tiếng Anh.
- Ghi âm **1 phút** mô tả buổi sáng — so với bản viết.

### Mở rộng

Dùng *because* để nói **vì sao** có thói quen đó.""",
        },
    ],
    "quizzes": [
        Q("Q_L01_10_01", 2, "multiple_choice", "Theo đoạn mẫu, người nói đi làm bằng gì?", {"A": "Car", "B": "Bus", "C": "Bike", "D": "Train"}, "B", "take the bus.", 11),
        Q("Q_L01_10_02", 2, "fill_in_blank", "I _____ watch TV late at night. (gần như không)", {"A": "always", "B": "usually", "C": "rarely", "D": "often"}, "C", "Rarely = hiếm khi.", 10),
        Q("Q_L01_10_03", 3, "synonym_antonym", "Từ trái nghĩa với 'always':", {"A": "often", "B": "never", "C": "usually", "D": "sometimes"}, "B", "Never.", 11),
        Q("Q_L01_10_04", 3, "error_identification", "Tìm lỗi: 'She go to work at 8 a.m. every day.'", {"A": "She", "B": "go", "C": "to work", "D": "every day"}, "B", "She goes.", 13, True),
        Q("Q_L01_10_05", 4, "fill_in_blank", "She _____ dinner at home every day.", {"A": "have", "B": "has", "C": "having", "D": "is have"}, "B", "She has.", 12),
        Q("Q_L01_10_06", 2, "fill_in_blank", "I usually leave home _____ 7:15 a.m.", {"A": "in", "B": "on", "C": "at", "D": "by"}, "C", "Giờ cụ thể → at.", 9),
        Q("Q_L01_10_07", 2, "multiple_choice", "Câu hỏi về tần suất:", {"A": "What time is it?", "B": "How often do you exercise?", "C": "Where do you live?", "D": "Who is that?"}, "B", "How often — bao lâu một lần.", 10),
        Q("Q_L01_10_08", 2, "fill_in_blank", "Every weekday I _____ up at six thirty.", {"A": "wake", "B": "wakes", "C": "waking", "D": "woke"}, "A", "I wake up — hiện tại đơn.", 10),
        Q("Q_L01_10_09", 3, "multiple_choice", "Theo đoạn mẫu, buổi tối người nói đôi khi:", {"A": "đi ngủ sớm", "B": "nấu ăn hoặc gọi đồ", "C": "xem TV suốt đêm", "D": "đi taxi"}, "B", "cook dinner or order food.", 12),
        Q("Q_L01_10_10", 3, "error_identification", "Tìm lỗi: 'Before bed, I read for twenty minute.'", {"A": "Before bed", "B": "I read", "C": "for twenty minute", "D": "—"}, "C", "twenty minutes.", 13, True),
    ],
}


def main():
    data = json.loads(P.read_text(encoding="utf-8"))
    by_id = {x["lesson_id"]: x for x in data["lessons"]}
    for lid, spec in ENRICH.items():
        les = by_id[lid]
        old = les["content"]
        les["estimated_minutes"] = spec["estimated_minutes"]
        les["content"] = {
            "theory": "",
            "theory_pages": spec["theory_pages"],
            "reading_passage": old["reading_passage"],
            "reading_word_count": old.get("reading_word_count", 0),
            "vocabulary": old["vocabulary"],
            "examples": old["examples"],
        }
        les["quizzes"] = spec["quizzes"]
    P.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    total_q = sum(len(ENRICH[l]["quizzes"]) for l in ENRICH)
    print(f"OK: updated {len(ENRICH)} lessons; total new quiz slots = {total_q}")


if __name__ == "__main__":
    main()
