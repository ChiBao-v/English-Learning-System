"""Khóa C02 — Daily Life & Surroundings (A1+): 10 bài × 3 trang × 10 quiz."""

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
    return [
        _lesson_01(),
        _lesson_02(),
        _lesson_03(),
        _lesson_04(),
        _lesson_05(),
        _lesson_06(),
        _lesson_07(),
        _lesson_08(),
        _lesson_09(),
        _lesson_10(),
    ]


def _lesson_01():
    meta = {"skill": "vocabulary", "topic": "routines_time", "time_est_minutes": 25, "difficulty": 0.3}
    p1 = """### Morning routines & telling time

**Hoạt động buổi sáng**

| Cụm | Nghĩa |
|-----|--------|
| **Wake up** | thức dậy |
| **Get up** | ra khỏi giường |
| **Brush teeth** | đánh răng |
| **Wash face** | rửa mặt |
| **Have breakfast** | ăn sáng |

**Giờ giấc**

- Giờ tròn: số + **o'clock** → *6:00* = *Six o'clock*.
- Nửa giờ: **Half past** + số giờ → *6:30* = *Half past six*.

**Ngữ cảnh:** *I wake up at six o'clock.*"""

    p2 = """### Work & afternoon routines

**Hoạt động**

| Cụm | Nghĩa |
|-----|--------|
| **Go to work / school** | đi làm / đi học |
| **Start work** | bắt đầu làm |
| **Have lunch** | ăn trưa |
| **Finish work** | tan làm |

**Thời gian trong ngày**

- *In the morning* — buổi sáng  
- *At noon* — khoảng 12 giờ trưa  
- *In the afternoon* — buổi chiều  

**Ngữ cảnh:** *I go to work at eight o'clock in the morning.*"""

    p3 = """### Evening routines & sleep

**Hoạt động**

- *Go home* — về nhà  
- *Take a shower* — tắm  
- *Have dinner* — ăn tối  
- *Relax* — thư giãn  
- *Watch TV* — xem TV  
- *Go to bed* — đi ngủ  

**Thời gian:** *In the evening* (buổi tối), *At night* (đêm).

**Ngữ cảnh:** *I take a shower and go to bed at ten o'clock.*

### Gợi ý

Viết **một đoạn 4–5 câu** về một ngày của bạn, dùng ít nhất **3 cụm** trong bài."""

    reading = (
        "My name is Lin. I wake up at six o'clock. I brush my teeth and have breakfast. "
        "I go to work at half past seven in the morning. After work, I go home and relax. "
        "In the evening, I watch TV. I go to bed at ten o'clock at night."
    )
    return {
        "lesson_id": "L02_01",
        "lesson_name": "Daily Routines & Time (Vocabulary)",
        "order": 1,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Morning routines & telling time", "body": p1},
                {"title": "Trang 2 — Work & afternoon routines", "body": p2},
                {"title": "Trang 3 — Evening & sleep", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "wake up / get up", "vi": "thức dậy / ra khỏi giường"},
                {"word": "brush teeth / wash face", "vi": "đánh răng / rửa mặt"},
                {"word": "have breakfast / lunch / dinner", "vi": "ăn sáng / trưa / tối"},
                {"word": "o'clock / half past", "vi": "giờ tròn / rưỡi (half past six)"},
                {"word": "in the morning / afternoon / evening", "vi": "buổi sáng/chiều/tối"},
                {"word": "at noon / at night", "vi": "buổi trưa (12h) / ban đêm"},
                {"word": "go home / go to bed", "vi": "về nhà / đi ngủ"},
            ],
            "examples": [
                {"english": "I wake up at six o'clock.", "vietnamese": "Tôi thức dậy lúc 6 giờ."},
                {"english": "After work, I go home and relax.", "vietnamese": "Sau giờ làm, tôi về nhà và thư giãn."},
            ],
        },
        "quizzes": [
            Q("Q_L02_01_01", 2, "multiple_choice", "Hành động “đánh răng” là:", {"A": "Wash face", "B": "Brush teeth", "C": "Have breakfast", "D": "Get up"}, "B", "Brush teeth = đánh răng.", 10),
            Q("Q_L02_01_02", 2, "multiple_choice", "07:30 đọc là:", {"A": "Seven o'clock", "B": "Half past seven", "C": "Eight thirty", "D": "Half to eight"}, "B", "7:30 = half past seven.", 11),
            Q("Q_L02_01_03", 2, "fill_in_blank", "After work, I go _____ and relax.", {"A": "home", "B": "house", "C": "to home", "D": "homework"}, "A", "Go home — cố định (không to).", 10),
            Q("Q_L02_01_04", 3, "multiple_choice", "Ghép đúng: 1. Have lunch — 2. Have dinner", {"A": "1→At noon, 2→In the evening", "B": "1→In the evening, 2→At noon", "C": "1→At night, 2→At noon", "D": "1→In the morning, 2→At noon"}, "A", "Lunch ~ noon; dinner ~ evening.", 14),
            Q("Q_L02_01_05", 2, "error_identification", "Sửa lỗi: “I eat breakfast at night.”", {"A": "eat", "B": "breakfast", "C": "night", "D": "I"}, "C", "Breakfast → in the morning (đổi night → morning).", 12, True),
            Q("Q_L02_01_06", 2, "multiple_choice", "I go to sleep _____ ten o'clock.", {"A": "in", "B": "on", "C": "at", "D": "by"}, "C", "Giờ cụ thể → at.", 9),
            Q("Q_L02_01_07", 1, "true_false", "“Go home” means going to the office.", {"A": "True", "B": "False"}, "B", "Go home = về nhà.", 8),
            Q("Q_L02_01_08", 2, "multiple_choice", "“Tôi đi ngủ lúc 10h.” — Chọn câu đúng:", {"A": "I go to bed at ten o'clock.", "B": "I go to the bed at ten.", "C": "I sleep to bed at ten.", "D": "I go bed at ten o'clock."}, "A", "Go to bed at + giờ.", 12),
            Q("Q_L02_01_09", 3, "multiple_choice", "Thứ tự logic buổi sáng đúng nhất:", {"A": "Wake up → Get up → Have breakfast", "B": "Have breakfast → Wake up → Get up", "C": "Get up → Have breakfast → Wake up", "D": "Wake up → Have breakfast → Get up"}, "A", "Thức dậy → ra khỏi giường → ăn sáng.", 13),
            Q("Q_L02_01_10", 2, "fill_in_blank", "I watch _____ in the evening.", {"A": "TV", "B": "radio", "C": "homework", "D": "breakfast"}, "A", "Watch TV.", 9),
        ],
    }


def _lesson_02():
    meta = {"skill": "grammar", "topic": "present_simple", "time_est_minutes": 30, "difficulty": 0.35}
    p1 = """### Present Simple — **khẳng định**

**Chủ ngữ + động từ**

- *I / You / We / They + V (nguyên mẫu)* → *I work*, *They play*.
- *He / She / It + V-s / es* → *He works*, *She plays*.

**Thêm -s / -es**

- Thêm **-es** khi tận cùng *o, s, z, ch, x, sh*: *go → goes*, *watch → watches*.
- Phụ âm + *y* → *-ies*: *study → studies*."""

    p2 = """### Present Simple — **phủ định**

Dùng trợ động từ **do / does + not**. Động từ chính **luôn nguyên mẫu**.

- *I / You / We / They + don't + V* → *I don't eat meat.*
- *He / She / It + doesn't + V* → *She doesn't like coffee.*"""

    p3 = """### Present Simple — **nghi vấn**

Đảo **Do / Does** lên trước chủ ngữ. Động từ chính **nguyên mẫu**.

- *Do + I/you/we/they + V?* → *Do you work?* — *Yes, I do. / No, I don't.*
- *Does + he/she/it + V?* → *Does she study?* — *Yes, she does. / No, she doesn't.*

### Lưu ý

Không nói *Does she studies?* — sau *does* chỉ còn *study*."""

    reading = (
        "Tom works in a cafe. He starts work at 8:00. He doesn't work on Sundays. "
        "Do you like coffee? He drinks coffee every morning. His sister studies English. "
        "She doesn't watch TV often."
    )
    return {
        "lesson_id": "L02_02",
        "lesson_name": "Present Simple - Action Verbs (Grammar)",
        "order": 2,
        "estimated_minutes": 40,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Affirmative", "body": p1},
                {"title": "Trang 2 — Negative", "body": p2},
                {"title": "Trang 3 — Questions", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "work / play / study / watch", "vi": "động từ thường (chú ý -s/-es)"},
                {"word": "don't / doesn't", "vi": "phủ định với do/does"},
            ],
            "examples": [
                {"english": "She watches TV every day.", "vietnamese": "Cô ấy xem TV mỗi ngày."},
                {"english": "They don't live here.", "vietnamese": "Họ không sống ở đây."},
            ],
        },
        "quizzes": [
            Q("Q_L02_02_01", 2, "multiple_choice", "She _____ music every day.", {"A": "listen", "B": "listens", "C": "listening", "D": "listening to"}, "B", "She + listens.", 10),
            Q("Q_L02_02_02", 2, "fill_in_blank", "He (watch) _____ TV every day.", {"A": "watch", "B": "watches", "C": "watching", "D": "watched"}, "B", "He watches — thêm -es.", 10),
            Q("Q_L02_02_03", 2, "multiple_choice", "We _____ work on weekends.", {"A": "aren't", "B": "doesn't", "C": "don't", "D": "isn't"}, "C", "We don't + V.", 11),
            Q("Q_L02_02_04", 2, "error_identification", "Tìm lỗi: “He doesn't goes to school.”", {"A": "doesn't", "B": "goes", "C": "to", "D": "school"}, "B", "doesn't go (không goes).", 12, True),
            Q("Q_L02_02_05", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "Does he like pizza?", "B": "He does like pizza?", "C": "Like he does pizza?", "D": "Does like he pizza?"}, "A", "Does + he + like + …?", 11),
            Q("Q_L02_02_06", 2, "multiple_choice", "_____ they play tennis?", {"A": "Does", "B": "Do", "C": "Are", "D": "Is"}, "B", "They → Do.", 9),
            Q("Q_L02_02_07", 2, "fill_in_blank", "I (study) _____ English on Mondays.", {"A": "study", "B": "studies", "C": "studying", "D": "studied"}, "A", "I + study (nguyên mẫu).", 9),
            Q("Q_L02_02_08", 2, "fill_in_blank", "Does it rain? — No, it _____.", {"A": "doesn't", "B": "don't", "C": "isn't", "D": "not"}, "A", "It + doesn't.", 10),
            Q("Q_L02_02_09", 2, "multiple_choice", "“Cô ấy không đi làm.” — Chọn câu đúng:", {"A": "She doesn't go to work.", "B": "She don't go to work.", "C": "She not go to work.", "D": "She doesn't goes to work."}, "A", "She doesn't + go.", 11),
            Q("Q_L02_02_10", 3, "multiple_choice", "Ghép: 1. He — 2. You", {"A": "1→doesn't, 2→don't", "B": "1→don't, 2→doesn't", "C": "1→don't, 2→don't", "D": "1→doesn't, 2→doesn't"}, "A", "He doesn't; You don't.", 13),
        ],
    }


def _lesson_03():
    meta = {"skill": "reading", "topic": "routine_application", "time_est_minutes": 25, "difficulty": 0.4}
    text = (
        "Mark is a software engineer. First, he wakes up at 6:00. He doesn't have a big breakfast. "
        "He drinks coffee. Then, he goes to work at half past seven. His company is big. "
        "He works from 8:00 to 5:00. He has lunch at noon. In the evening, Mark doesn't work. "
        "He relaxes. He exercises, takes a shower, and has dinner. Finally, he goes to bed at 11:00."
    )
    p1 = """### Pre-reading — từ khóa & liên từ

**Từ vựng**

- *Software engineer* — kỹ sư phần mềm  
- *Busy* — bận rộn  
- *Relax* — thư giãn  
- *Company* — công ty  

**Liên từ trình tự:** *First* (đầu tiên), *Then / After that* (sau đó), *Finally* (cuối cùng)."""

    p2 = """### Reading text

Đọc đoạn về **một ngày của Mark** — chú ý **giờ giấc** và **thứ tự** (*First → Then → Finally*)."""

    p3 = """### Post-reading — phân tích

- Động từ *-s*: *wakes*, *goes*, *works*, *relaxes*, *exercises*…  
- Phủ định: *doesn't have*, *doesn't work*.  
- **Scanning:** đọc câu hỏi trước → tìm từ khóa (*lunch* → *at noon*)."""

    return {
        "lesson_id": "L02_03",
        "lesson_name": "A Day in the Life (Reading)",
        "order": 3,
        "estimated_minutes": 38,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Pre-reading", "body": p1},
                {"title": "Trang 2 — Bài đọc", "body": p2},
                {"title": "Trang 3 — Post-reading", "body": p3},
            ],
            "reading_passage": text,
            "reading_word_count": wc(text),
            "vocabulary": [
                {"word": "software engineer", "vi": "kỹ sư phần mềm"},
                {"word": "company", "vi": "công ty"},
                {"word": "First / Then / Finally", "vi": "trình tự"},
            ],
            "examples": [
                {"english": "He has lunch at noon.", "vietnamese": "Anh ấy ăn trưa lúc buổi trưa."},
            ],
        },
        "quizzes": [
            Q("Q_L02_03_01", 1, "multiple_choice", "What is Mark's job?", {"A": "Doctor", "B": "Software engineer", "C": "Teacher", "D": "Driver"}, "B", "Đầu đoạn: software engineer.", 9),
            Q("Q_L02_03_02", 1, "true_false", "Mark has a big breakfast.", {"A": "True", "B": "False"}, "B", "He doesn't have a big breakfast.", 8),
            Q("Q_L02_03_03", 2, "fill_in_blank", "Mark drinks _____ for breakfast.", {"A": "coffee", "B": "tea", "C": "milk", "D": "water"}, "A", "He drinks coffee.", 9),
            Q("Q_L02_03_04", 2, "multiple_choice", "What time does he go to work?", {"A": "7:00", "B": "7:30", "C": "8:00", "D": "6:00"}, "B", "Half past seven = 7:30.", 11),
            Q("Q_L02_03_05", 2, "multiple_choice", "Trái nghĩa gần nghĩa với “work” (trong bài tối):", {"A": "relax", "B": "exercise", "C": "sleep", "D": "eat"}, "A", "Tối: doesn't work — relaxes.", 12),
            Q("Q_L02_03_06", 2, "fill_in_blank", "When does he have lunch? — _____", {"A": "At noon", "B": "At night", "C": "In the evening", "D": "At 11:00"}, "A", "He has lunch at noon.", 10),
            Q("Q_L02_03_07", 2, "multiple_choice", "What happens after he exercises?", {"A": "He goes to bed", "B": "He takes a shower", "C": "He drinks coffee", "D": "He goes to work"}, "B", "exercises → takes a shower → has dinner.", 12),
            Q("Q_L02_03_08", 2, "true_false", "He works in the evening.", {"A": "True", "B": "False"}, "B", "In the evening, Mark doesn't work.", 9),
            Q("Q_L02_03_09", 2, "multiple_choice", "“His company…” — *His* chỉ:", {"A": "the coffee", "B": "Mark's", "C": "the train", "D": "breakfast"}, "B", "His = của Mark.", 10),
            Q("Q_L02_03_10", 2, "fill_in_blank", "The text is mainly about Mark's _____.", {"A": "daily routine", "B": "company only", "C": "coffee", "D": "breakfast only"}, "A", "Main idea: một ngày / routine.", 11),
        ],
    }


def _lesson_04():
    meta = {"skill": "vocabulary", "topic": "town_transport", "time_est_minutes": 25, "difficulty": 0.4}
    p1 = """### Public places

| Địa điểm | Nghĩa |
|----------|--------|
| **Hospital** | bệnh viện |
| **School** | trường |
| **Bank** | ngân hàng |
| **Supermarket** | siêu thị |
| **Park** | công viên |
| **Restaurant** | nhà hàng |

**Ngữ cảnh:** *I buy food at the supermarket.*"""

    p2 = """### Transportation

| Từ | Nghĩa |
|----|--------|
| **Car / bus / train** | ô tô / xe buýt / tàu |
| **Motorbike / bicycle (bike)** | xe máy / xe đạp |
| **Walk** | đi bộ |

**By + phương tiện:** *go by car*, *go by bus*.  
**Ngoại lệ:** *on foot* = đi bộ (không nói *by foot*)."""

    p3 = """### Asking for locations

- *Where is the + địa điểm?* — *Where is the bank?*
- Chỉ đường cơ bản: *It's here.* / *It's there.* / *It's near …*

### Thực hành

Đặt **3 câu Where is…?** về nơi trong thị trấn tưởng tượng."""

    reading = (
        "I need money. Where is the bank? It is near the supermarket. "
        "I go to school by bus. My father goes to work by car. Sometimes I walk to the park on foot."
    )
    return {
        "lesson_id": "L02_04",
        "lesson_name": "Places in Town & Transport (Vocabulary)",
        "order": 4,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Public places", "body": p1},
                {"title": "Trang 2 — Transportation", "body": p2},
                {"title": "Trang 3 — Asking where", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "hospital / bank / supermarket", "vi": "bệnh viện / ngân hàng / siêu thị"},
                {"word": "by bus / by car / on foot", "vi": "đi bằng… / đi bộ"},
            ],
            "examples": [
                {"english": "I go to work by bus.", "vietnamese": "Tôi đi làm bằng xe buýt."},
            ],
        },
        "quizzes": [
            Q("Q_L02_04_01", 1, "multiple_choice", "You keep money in a _____.", {"A": "School", "B": "Bank", "C": "Park", "D": "Restaurant"}, "B", "Bank = ngân hàng.", 8),
            Q("Q_L02_04_02", 2, "multiple_choice", "I go to work _____ bus.", {"A": "in", "B": "by", "C": "on", "D": "at"}, "B", "By bus.", 9),
            Q("Q_L02_04_03", 2, "fill_in_blank", "Doctors work in a _____.", {"A": "hospital", "B": "bank", "C": "park", "D": "restaurant"}, "A", "Hospital.", 9),
            Q("Q_L02_04_04", 3, "multiple_choice", "Ghép: 1. Buy food — 2. Eat a meal", {"A": "1→Supermarket, 2→Restaurant", "B": "1→Restaurant, 2→Supermarket", "C": "1→School, 2→Bank", "D": "1→Park, 2→Hospital"}, "A", "Mua đồ ăn ở siêu thị; ăn ở nhà hàng.", 13),
            Q("Q_L02_04_05", 2, "error_identification", "Sửa: “I go to school by foot.”", {"A": "go", "B": "school", "C": "by", "D": "foot"}, "C", "On foot (không by foot).", 11, True),
            Q("Q_L02_04_06", 2, "multiple_choice", "Where _____ the park?", {"A": "is", "B": "are", "C": "am", "D": "be"}, "A", "The park → is.", 9),
            Q("Q_L02_04_07", 1, "true_false", "You can take a train at the bank.", {"A": "True", "B": "False"}, "B", "Ga/tàu không ở ngân hàng.", 8),
            Q("Q_L02_04_08", 2, "multiple_choice", "“Tôi đi xe máy đến trường.”", {"A": "I go to school by motorbike.", "B": "I go to school with motorbike.", "C": "I go school by motorbike.", "D": "I by motorbike to school."}, "A", "By motorbike.", 11),
            Q("Q_L02_04_09", 2, "fill_in_blank", "The opposite of “here” in basic directions is _____.", {"A": "there", "B": "near", "C": "where", "D": "everywhere"}, "A", "Here / there.", 9),
            Q("Q_L02_04_10", 2, "fill_in_blank", "A place with trees and grass is often a _____.", {"A": "park", "B": "bank", "C": "hospital", "D": "supermarket"}, "A", "Park.", 9),
        ],
    }


def _lesson_05():
    meta = {"skill": "grammar", "topic": "prepositions_in_on_at", "time_est_minutes": 30, "difficulty": 0.45}
    p1 = """### Prepositions of time — **in, on, at**

- **IN:** tháng (*in May*), năm (*in 2024*), mùa (*in summer*), *in the morning/afternoon/evening*.
- **ON:** ngày trong tuần (*on Monday*), ngày cụ thể (*on May 1st*).
- **AT:** giờ (*at 7 o'clock*), *at noon*, *at night*."""

    p2 = """### Prepositions of place — **in, on, at**

- **IN:** quốc gia/thành phố (*in Vietnam*), trong phòng (*in the room*).
- **ON:** trên bề mặt (*on the table*), tên đường (*on Baker Street*).
- **AT:** điểm cụ thể (*at 123 Baker Street*), *at school*, *at home*, *at work*."""

    p3 = """### Dễ nhầm

- *In the hospital* (bên trong tòa nhà) vs *at the hospital* (khu vực chung).
- *In the morning* — nhưng *on Monday morning* (có ngày cụ thể → **on**).

### Ôn nhanh

**at** + giờ; **on** + ngày; **in** + tháng/năm/buổi (không có ngày cụ thể)."""

    reading = (
        "My birthday is in May. I was born in 2005. I have class on Monday. "
        "I wake up at 7:00 in the morning. I live in Hanoi. The book is on the table. "
        "I study at school."
    )
    return {
        "lesson_id": "L02_05",
        "lesson_name": "Prepositions of Time & Place (Grammar)",
        "order": 5,
        "estimated_minutes": 42,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Time: in, on, at", "body": p1},
                {"title": "Trang 2 — Place: in, on, at", "body": p2},
                {"title": "Trang 3 — Trường hợp dễ nhầm", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "in / on / at", "vi": "giới từ thời gian & địa điểm"},
            ],
            "examples": [
                {"english": "I live in Vietnam.", "vietnamese": "Tôi sống ở Việt Nam."},
                {"english": "See you on Friday.", "vietnamese": "Hẹn thứ Sáu."},
            ],
        },
        "quizzes": [
            Q("Q_L02_05_01", 2, "multiple_choice", "My birthday is _____ May.", {"A": "in", "B": "on", "C": "at", "D": "by"}, "A", "Tháng → in.", 9),
            Q("Q_L02_05_02", 2, "multiple_choice", "I have a meeting _____ Monday.", {"A": "in", "B": "on", "C": "at", "D": "by"}, "B", "Ngày trong tuần → on.", 9),
            Q("Q_L02_05_03", 2, "fill_in_blank", "The book is _____ the table.", {"A": "on", "B": "in", "C": "at", "D": "by"}, "A", "Trên mặt bàn → on.", 9),
            Q("Q_L02_05_04", 2, "error_identification", "Sửa: “She lives at London.”", {"A": "She", "B": "lives", "C": "at", "D": "London"}, "C", "In London (thành phố).", 11, True),
            Q("Q_L02_05_05", 2, "multiple_choice", "We sleep _____ night.", {"A": "in", "B": "on", "C": "at", "D": "by"}, "C", "At night.", 9),
            Q("Q_L02_05_06", 2, "fill_in_blank", "I am _____ school now.", {"A": "at", "B": "in", "C": "on", "D": "to"}, "A", "At school.", 9),
            Q("Q_L02_05_07", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "He works in a bank.", "B": "He works on a bank.", "C": "He works at a bank in wrong.", "D": "He in works a bank."}, "A", "Works in a bank / at a bank đều có thể; câu A chuẩn.", 11),
            Q("Q_L02_05_08", 1, "true_false", "We usually say “on the morning”.", {"A": "True", "B": "False"}, "B", "In the morning.", 8),
            Q("Q_L02_05_09", 2, "multiple_choice", "“Tôi sống ở Việt Nam.”", {"A": "I live in Vietnam.", "B": "I live on Vietnam.", "C": "I live at Vietnam.", "D": "I live to Vietnam."}, "A", "In + country.", 10),
            Q("Q_L02_05_10", 3, "multiple_choice", "Chọn cặp đúng: ___ 8:00 AM, ___ Tuesday.", {"A": "at, on", "B": "on, at", "C": "in, on", "D": "at, in"}, "A", "At + giờ; on + ngày.", 12),
        ],
    }


def _lesson_06():
    meta = {"skill": "reading", "topic": "city_life_transport", "time_est_minutes": 25, "difficulty": 0.5}
    text = (
        "Sarah lives in New York. It is a big and noisy city. She works in a bank on 5th Avenue. "
        "Every day, her commute is long. She doesn't go to work by car because the traffic is bad. "
        "She walks to the train station at 7:30 in the morning. The train is very fast but crowded. "
        "She arrives at work at 8:15. On weekends, she goes to the park by bicycle and relaxes."
    )
    p1 = """### Pre-reading

**Từ vựng:** *traffic* (giao thông), *noisy* (ồn ào), *fast* (nhanh), *commute* (quãng đường đi làm / di chuyển).

**Chủ đề:** Cuộc sống đi lại ở **thành phố lớn** — xe công cộng, tắc đường, giờ giấc."""

    p2 = """### Reading text

Đọc về **Sarah ở New York** — gạch **because** (lý do), **by + phương tiện**, **in / on / at**."""

    p3 = """### Post-reading

- Lý do: *She doesn't go by car **because** the traffic is bad.*
- Giới từ: *in New York*, *in a bank*, *on 5th Avenue*, *at 7:30*, *on weekends*."""

    return {
        "lesson_id": "L02_06",
        "lesson_name": "City Life (Reading)",
        "order": 6,
        "estimated_minutes": 38,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Pre-reading", "body": p1},
                {"title": "Trang 2 — Bài đọc", "body": p2},
                {"title": "Trang 3 — Post-reading", "body": p3},
            ],
            "reading_passage": text,
            "reading_word_count": wc(text),
            "vocabulary": [
                {"word": "traffic / commute", "vi": "giao thông / đi làm hàng ngày"},
                {"word": "noisy / crowded", "vi": "ồn ào / đông đúc"},
            ],
            "examples": [
                {"english": "The traffic is bad.", "vietnamese": "Giao thông tệ / tắc."},
            ],
        },
        "quizzes": [
            Q("Q_L02_06_01", 1, "multiple_choice", "Where does Sarah live?", {"A": "London", "B": "New York", "C": "Tokyo", "D": "Paris"}, "B", "Đầu đoạn.", 8),
            Q("Q_L02_06_02", 1, "true_false", "The city is quiet.", {"A": "True", "B": "False"}, "B", "It is noisy.", 8),
            Q("Q_L02_06_03", 2, "multiple_choice", "Where does she work?", {"A": "In a bank", "B": "In a hospital", "C": "In a school", "D": "In a park"}, "A", "Works in a bank.", 9),
            Q("Q_L02_06_04", 2, "fill_in_blank", "She doesn't use a car because the _____ is bad.", {"A": "traffic", "B": "train", "C": "park", "D": "bicycle"}, "A", "Because the traffic is bad.", 10),
            Q("Q_L02_06_05", 2, "multiple_choice", "How does she mainly travel to work (after walking to the station)?", {"A": "By car", "B": "By train", "C": "By bus", "D": "By bicycle"}, "B", "Walks to station → train.", 12),
            Q("Q_L02_06_06", 2, "fill_in_blank", "What time does she arrive at work? — _____", {"A": "8:15", "B": "7:30", "C": "5:00", "D": "11:00"}, "A", "Arrives at work at 8:15.", 10),
            Q("Q_L02_06_07", 2, "fill_in_blank", "The train is fast but _____.", {"A": "crowded", "B": "empty", "C": "slow", "D": "quiet"}, "A", "Fast but crowded.", 9),
            Q("Q_L02_06_08", 2, "true_false", "She goes to the park by car on weekends.", {"A": "True", "B": "False"}, "B", "By bicycle.", 9),
            Q("Q_L02_06_09", 2, "error_identification", "Sửa: “She walk to the station.”", {"A": "She", "B": "walk", "C": "to", "D": "station"}, "B", "She walks.", 11, True),
            Q("Q_L02_06_10", 2, "fill_in_blank", "The passage is about Sarah's _____ in the city.", {"A": "commute / city life", "B": "only breakfast", "C": "only the bank name", "D": "holiday"}, "A", "Main idea: đi làm / cuộc sống phố.", 11),
        ],
    }


def _lesson_07():
    meta = {"skill": "vocabulary", "topic": "food_drinks", "time_est_minutes": 20, "difficulty": 0.4}
    p1 = """### Meals of the day

- *Breakfast* — bữa sáng  
- *Lunch* — bữa trưa  
- *Dinner* — bữa tối  
- *Snack* — đồ ăn vặt / bữa phụ  

**Động từ:** *cook*, *eat / have*, *drink*."""

    p2 = """### Common foods

*Rice, bread, meat, chicken, fish, egg, vegetable, fruit, apple, banana*…

**Gợi ý:** *a / an* với đếm được số ít (*an egg*, *a banana*)."""

    p3 = """### Drinks & taste

**Đồ uống:** *water, coffee, tea, milk, juice*.

**Tính từ:** *sweet* (ngọt), *hot* (nóng), *cold* (lạnh).

### Thực hành

Viết **thực đơn** một ngày bằng tiếng Anh (3 bữa + một đồ uống)."""

    reading = (
        "For breakfast, I have bread and an egg. I drink hot coffee. "
        "For lunch, I eat rice and fish. For dinner, I cook chicken with vegetables. "
        "I like fruit: apples and bananas. I drink water every day."
    )
    return {
        "lesson_id": "L02_07",
        "lesson_name": "Food, Drinks & Meals (Vocabulary)",
        "order": 7,
        "estimated_minutes": 32,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Meals", "body": p1},
                {"title": "Trang 2 — Foods", "body": p2},
                {"title": "Trang 3 — Drinks & taste", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "breakfast / lunch / dinner", "vi": "sáng / trưa / tối"},
                {"word": "rice / meat / fruit / vegetable", "vi": "cơm / thịt / trái cây / rau"},
            ],
            "examples": [
                {"english": "I drink a glass of milk.", "vietnamese": "Tôi uống một cốc sữa."},
            ],
        },
        "quizzes": [
            Q("Q_L02_07_01", 1, "multiple_choice", "You eat this in the morning:", {"A": "Breakfast", "B": "Dinner", "C": "Lunch", "D": "Snack"}, "A", "Morning → breakfast.", 8),
            Q("Q_L02_07_02", 1, "multiple_choice", "Which one is a drink?", {"A": "Bread", "B": "Juice", "C": "Meat", "D": "Egg"}, "B", "Juice = đồ uống.", 8),
            Q("Q_L02_07_03", 2, "fill_in_blank", "I like to drink hot _____ in the morning.", {"A": "coffee", "B": "rice", "C": "chicken", "D": "bread"}, "A", "Coffee or tea.", 9),
            Q("Q_L02_07_04", 3, "multiple_choice", "Ghép: 1. Apple — 2. Chicken", {"A": "1→Fruit, 2→Meat", "B": "1→Meat, 2→Fruit", "C": "1→Vegetable, 2→Fish", "D": "1→Drink, 2→Bread"}, "A", "Apple = fruit; chicken = meat.", 12),
            Q("Q_L02_07_05", 2, "error_identification", "Sửa: “I eat water.”", {"A": "I", "B": "eat", "C": "water", "D": "—"}, "B", "Drink water.", 10, True),
            Q("Q_L02_07_06", 1, "multiple_choice", "A banana is a type of _____.", {"A": "Vegetable", "B": "Fruit", "C": "Meat", "D": "Drink"}, "B", "Banana = fruit.", 8),
            Q("Q_L02_07_07", 1, "true_false", "Dinner is the meal at noon.", {"A": "True", "B": "False"}, "B", "Lunch ~ noon; dinner ~ evening.", 8),
            Q("Q_L02_07_08", 2, "multiple_choice", "“Tôi nấu bữa tối.”", {"A": "I cook dinner.", "B": "I make dinner cook.", "C": "I dinner cook.", "D": "I cooking dinner."}, "A", "Cook dinner.", 10),
            Q("Q_L02_07_09", 2, "fill_in_blank", "The opposite of “hot” (drink) is often _____.", {"A": "cold", "B": "sweet", "C": "big", "D": "fast"}, "A", "Hot / cold.", 9),
            Q("Q_L02_07_10", 2, "fill_in_blank", "Cows give us _____ to drink.", {"A": "milk", "B": "juice", "C": "coffee", "D": "rice"}, "A", "Milk.", 9),
        ],
    }


def _lesson_08():
    meta = {"skill": "grammar", "topic": "nouns_quantifiers", "time_est_minutes": 30, "difficulty": 0.55}
    p1 = """### Countable & uncountable nouns

**Countable:** có thể đếm — *apple → apples*, *a banana*, *two eggs*.

**Uncountable:** chất/khái niệm — *water, rice, milk, money* — **không** thêm *s* thông thường; **không** *a/an* đơn lẻ (*a water* sai)."""

    p2 = """### Some

- Khẳng định: *I have some apples.* / *I need some water.*
- Lời mời: *Would you like some tea?*"""

    p3 = """### Any

- Phủ định: *I don't have any eggs.*  
- Nghi vấn: *Do you have any milk?* / *Is there any sugar?*

### Lưu ý

Trong phủ định thường dùng **any**, không dùng **some** (trừ vài trường hợp đặc biệt nâng cao)."""

    reading = (
        "We have some apples in the kitchen. We don't have any oranges. "
        "There is some bread. There isn't any cheese. Would you like some tea? "
        "I don't want any coffee. Rice is important in my country."
    )
    return {
        "lesson_id": "L02_08",
        "lesson_name": "Countable/Uncountable & Some/Any (Grammar)",
        "order": 8,
        "estimated_minutes": 42,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Countable & uncountable", "body": p1},
                {"title": "Trang 2 — Some", "body": p2},
                {"title": "Trang 3 — Any", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "some / any", "vi": "một ít / bất cứ (ngữ cảnh khác nhau)"},
            ],
            "examples": [
                {"english": "I don't have any money.", "vietnamese": "Tôi không có tiền."},
            ],
        },
        "quizzes": [
            Q("Q_L02_08_01", 2, "multiple_choice", "Which noun is uncountable?", {"A": "Egg", "B": "Water", "C": "Banana", "D": "Apple"}, "B", "Water — không đếm kiểu “two waters” trong A1.", 10),
            Q("Q_L02_08_02", 2, "multiple_choice", "“I want _____ apple.”", {"A": "a", "B": "an", "C": "some", "D": "any"}, "B", "An apple (âm /æ/).", 10),
            Q("Q_L02_08_03", 2, "fill_in_blank", "I have _____ bread in the kitchen. (khẳng định)", {"A": "some", "B": "any", "C": "a", "D": "many"}, "A", "Some + uncountable.", 10),
            Q("Q_L02_08_04", 2, "error_identification", "Sửa: “She doesn't have some money.”", {"A": "doesn't", "B": "have", "C": "some", "D": "money"}, "C", "Any money (phủ định).", 11, True),
            Q("Q_L02_08_05", 2, "multiple_choice", "Do we have _____ eggs?", {"A": "some", "B": "any", "C": "a", "D": "much"}, "B", "Câu hỏi → any.", 10),
            Q("Q_L02_08_06", 2, "fill_in_blank", "Would you like _____ coffee? (mời)", {"A": "some", "B": "any", "C": "many", "D": "much"}, "A", "Would you like some…?", 10),
            Q("Q_L02_08_07", 1, "true_false", "“Rices” is correct English.", {"A": "True", "B": "False"}, "B", "Rice không đếm như vậy.", 8),
            Q("Q_L02_08_08", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "I don't have any milk.", "B": "I don't have some milk.", "C": "I any don't have milk.", "D": "Don't I have any milk."}, "A", "Don't have any.", 11),
            Q("Q_L02_08_09", 2, "multiple_choice", "He eats _____ banana every day.", {"A": "a", "B": "some", "C": "any", "D": "much"}, "A", "A banana — đếm được số ít.", 10),
            Q("Q_L02_08_10", 3, "multiple_choice", "Ghép: 1. Affirmative — 2. Negative (thông thường)", {"A": "1→some, 2→any", "B": "1→any, 2→some", "C": "1→any, 2→any", "D": "1→some, 2→some"}, "A", "Some khẳng định; any phủ định.", 13),
        ],
    }


def _lesson_09():
    meta = {"skill": "grammar", "topic": "adverbs_frequency", "time_est_minutes": 25, "difficulty": 0.5}
    p1 = """### Adverbs of frequency (cơ bản)

| Trạng từ | Mức |
|----------|-----|
| **always** | 100% |
| **usually** | ~80% |
| **sometimes** | ~50% |
| **never** | 0% |"""

    p2 = """### Với động từ thường

Đứng **trước** động từ thường:

*I **always** wake up early.*  
*She **never** eats meat.*"""

    p3 = """### Với *to be*

Đứng **sau** *am/is/are*:

*He **is usually** late.*  
*We **are sometimes** tired.*

### Cảnh báo

Không kết hợp *never* với phủ định khác một cách dư thừa (*I never don't…* — sai)."""

    reading = (
        "I always brush my teeth in the morning. Tom is usually on time. "
        "We sometimes watch TV in the evening. She never drinks soda. "
        "They are never late for class."
    )
    return {
        "lesson_id": "L02_09",
        "lesson_name": "Adverbs of Frequency (Vocabulary & Grammar)",
        "order": 9,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Bảng tần suất", "body": p1},
                {"title": "Trang 2 — Với động từ thường", "body": p2},
                {"title": "Trang 3 — Với to be", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "always / usually / sometimes / never", "vi": "luôn / thường / đôi khi / không bao giờ"},
            ],
            "examples": [
                {"english": "I usually go to work by bus.", "vietnamese": "Tôi thường đi làm bằng xe buýt."},
            ],
        },
        "quizzes": [
            Q("Q_L02_09_01", 1, "multiple_choice", "100% frequency means:", {"A": "Always", "B": "Never", "C": "Sometimes", "D": "Usually"}, "A", "Always = 100%.", 8),
            Q("Q_L02_09_02", 2, "multiple_choice", "Choose the correct sentence:", {"A": "I usually play tennis.", "B": "I play usually tennis.", "C": "Usually I play tennis wrong.", "D": "I play tennis usually."}, "A", "Usually trước play.", 10),
            Q("Q_L02_09_03", 2, "fill_in_blank", "She eats meat 0 days a week. She _____ eats meat.", {"A": "never", "B": "always", "C": "usually", "D": "sometimes"}, "A", "Never = 0%.", 9),
            Q("Q_L02_09_04", 2, "error_identification", "Sửa: “He is late always.”", {"A": "He", "B": "is late always", "C": "late", "D": "always"}, "B", "He is always late.", 11, True),
            Q("Q_L02_09_05", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "We sometimes watch TV.", "B": "We watch sometimes TV.", "C": "Sometimes we TV watch.", "D": "Watch we sometimes TV."}, "A", "Sometimes trước watch.", 10),
            Q("Q_L02_09_06", 2, "multiple_choice", "With *to be*, the adverb often comes:", {"A": "before *am/is/are*", "B": "after *am/is/are*", "C": "at the end only", "D": "before the subject"}, "B", "He is usually…", 11),
            Q("Q_L02_09_07", 1, "true_false", "“I never don't eat fish.” is good English.", {"A": "True", "B": "False"}, "B", "Trùng phủ định — sai.", 8),
            Q("Q_L02_09_08", 2, "multiple_choice", "“Tôi luôn đi làm bằng xe buýt.”", {"A": "I always go to work by bus.", "B": "I go always to work by bus.", "C": "Always I go by bus to work wrong.", "D": "I go to always work by bus."}, "A", "Always trước go.", 11),
            Q("Q_L02_09_09", 2, "fill_in_blank", "The opposite of “always” is _____.", {"A": "never", "B": "usually", "C": "sometimes", "D": "often"}, "A", "Always / never.", 9),
            Q("Q_L02_09_10", 2, "fill_in_blank", "I am _____ (about 80%) happy on Fridays.", {"A": "usually", "B": "never", "C": "always", "D": "sometimes"}, "A", "Usually ~ 80%.", 10),
        ],
    }


def _lesson_10():
    meta = {"skill": "reading", "topic": "healthy_lifestyle_review", "time_est_minutes": 30, "difficulty": 0.6}
    text = (
        "David has a very healthy lifestyle. He always wakes up early at 5:30 in the morning. "
        "He drinks some water and exercises in the park. For breakfast, he usually eats an egg and some fruit. "
        "He never eats junk food. David works in an office, but he doesn't go by car. "
        "He always rides his bicycle to work. In the evening, he cooks dinner with his family. "
        "He doesn't drink any coffee at night because he wants to sleep well."
    )
    p1 = """### Pre-reading

**Từ vựng:** *healthy*, *lifestyle*, *exercise*, *junk food*.

**Ôn tập:** hiện tại đơn, trạng từ tần suất, *some/any*, giới từ thời gian/địa điểm."""

    p2 = """### Reading text

Đọc về **David** — gạch *always / usually / never*, *some / any*, *in / at*."""

    p3 = """### Post-reading

- Tần suất: *always wakes*, *usually eats*, *never eats junk food*, *always rides*.  
- Lượng từ: *some water*, *an egg*, *some fruit*, *any coffee*.  
- Giới từ: *in the morning*, *in the park*, *in an office*, *at night*."""

    return {
        "lesson_id": "L02_10",
        "lesson_name": "Healthy Lifestyle (Reading)",
        "order": 10,
        "estimated_minutes": 45,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Pre-reading", "body": p1},
                {"title": "Trang 2 — Bài đọc", "body": p2},
                {"title": "Trang 3 — Post-reading", "body": p3},
            ],
            "reading_passage": text,
            "reading_word_count": wc(text),
            "vocabulary": [
                {"word": "healthy lifestyle / junk food", "vi": "lối sống khỏe / đồ ăn nhanh không tốt"},
                {"word": "exercise", "vi": "tập thể dục"},
            ],
            "examples": [
                {"english": "He doesn't drink any coffee at night.", "vietnamese": "Anh ấy không uống cà phê ban đêm."},
            ],
        },
        "quizzes": [
            Q("Q_L02_10_01", 1, "multiple_choice", "Does David have a healthy lifestyle?", {"A": "Yes, he does.", "B": "No, he doesn't.", "C": "We don't know", "D": "Maybe not"}, "A", "Very healthy lifestyle.", 8),
            Q("Q_L02_10_02", 2, "fill_in_blank", "He wakes up early at _____ in the morning.", {"A": "5:30", "B": "11:00", "C": "8:15", "D": "7:30"}, "A", "5:30.", 9),
            Q("Q_L02_10_03", 1, "true_false", "David eats junk food.", {"A": "True", "B": "False"}, "B", "He never eats junk food.", 8),
            Q("Q_L02_10_04", 2, "multiple_choice", "What does he have for breakfast?", {"A": "Bread only", "B": "An egg and fruit", "C": "Junk food", "D": "Coffee"}, "B", "Usually an egg and some fruit.", 10),
            Q("Q_L02_10_05", 2, "fill_in_blank", "How does he go to work? — _____", {"A": "By bicycle / He rides his bicycle", "B": "By car", "C": "By train", "D": "On foot only"}, "A", "Rides his bicycle.", 11),
            Q("Q_L02_10_06", 2, "multiple_choice", "Does he drink any coffee at night?", {"A": "Yes", "B": "No", "C": "Sometimes", "D": "Always"}, "B", "Doesn't drink any coffee at night.", 10),
            Q("Q_L02_10_07", 2, "fill_in_blank", "He drinks some water and _____ in the park.", {"A": "exercises", "B": "sleeps", "C": "drives", "D": "works"}, "A", "Exercises in the park.", 9),
            Q("Q_L02_10_08", 2, "error_identification", "Sửa: “He don't go by car.”", {"A": "He", "B": "don't", "C": "go", "D": "car"}, "B", "He doesn't.", 10, True),
            Q("Q_L02_10_09", 2, "multiple_choice", "Why doesn't he drink coffee at night?", {"A": "Because he wants to sleep well", "B": "Because he hates water", "C": "Because he walks", "D": "Because he is late"}, "A", "Because… sleep well.", 11),
            Q("Q_L02_10_10", 2, "fill_in_blank", "The text shows how to live a _____ life.", {"A": "healthy", "B": "noisy", "C": "lazy", "D": "slow"}, "A", "Healthy lifestyle.", 9),
        ],
    }
