"""Khóa C03 — Expanding Horizons (Pre-Intermediate A2): 10 bài × 3 trang × 10 quiz."""

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
    meta = {"skill": "vocabulary", "topic": "travel_photo", "time_est_minutes": 25, "difficulty": 0.45}
    p1 = """### At the airport

| Từ | Nghĩa |
|----|--------|
| **Flight** | chuyến bay |
| **Ticket / boarding pass** | vé / thẻ lên máy bay |
| **Luggage** | hành lý |
| **Passport** | hộ chiếu |

**Động từ:** *check in*, *take off*, *land*.

**Ngữ cảnh:** *The flight takes off at 9:00 AM.*"""

    p2 = """### Accommodation & transport

- *Hotel*, *book a room*, *reception*, *tourist*  
- *Rent a car*, *explore*, *arrive*

**Ngữ cảnh:** *We book a room at a hotel near the center.*"""

    p3 = """### Photography (hobbies)

- *Camera*, *lens*, *focus*, *zoom*, *landscape*  
- *Take photos / pictures*, *capture*

**Ngữ cảnh:** *I use a mirrorless camera with a 50mm lens to take photos.*

### Gợi ý

Viết 4–5 câu về một chuyến đi tưởng tượng (sân bay → khách sạn → chụp ảnh)."""

    reading = (
        "Last year I flew to Da Nang. I checked in online and showed my passport at the gate. "
        "The flight took off on time. I took photos of the landscape from the window."
    )
    return {
        "lesson_id": "L03_01",
        "lesson_name": "Travel & Photography (Vocabulary)",
        "order": 1,
        "estimated_minutes": 38,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — At the airport", "body": p1},
                {"title": "Trang 2 — Accommodation & transport", "body": p2},
                {"title": "Trang 3 — Photography", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "passport / boarding pass / luggage", "vi": "hộ chiếu / thẻ lên máy / hành lý"},
                {"word": "take off / land / check in", "vi": "cất cánh / hạ cánh / làm thủ tục"},
                {"word": "landscape / lens / capture", "vi": "phong cảnh / ống kính / bắt khoảnh khắc"},
            ],
            "examples": [
                {"english": "The plane lands at 3 PM.", "vietnamese": "Máy bay hạ cánh lúc 3 giờ chiều."},
            ],
        },
        "quizzes": [
            Q("Q_L03_01_01", 2, "multiple_choice", "You need a _____ to travel to another country.", {"A": "Ticket", "B": "Passport", "C": "Luggage", "D": "Camera"}, "B", "Passport — giấy tờ xuất nhập cảnh.", 10),
            Q("Q_L03_01_02", 2, "multiple_choice", "The plane leaves the ground. It _____.", {"A": "Lands", "B": "Takes off", "C": "Checks in", "D": "Books"}, "B", "Take off = cất cánh.", 10),
            Q("Q_L03_01_03", 2, "fill_in_blank", "I _____ a room at the hotel for two nights.", {"A": "book", "B": "land", "C": "take off", "D": "capture"}, "A", "Book a room.", 9),
            Q("Q_L03_01_04", 3, "multiple_choice", "Ghép đúng: 1. Take — 2. Rent", {"A": "1→photos, 2→a car", "B": "1→a car, 2→photos", "C": "1→luggage, 2→passport", "D": "1→off, 2→in"}, "A", "Take photos; rent a car.", 12),
            Q("Q_L03_01_05", 2, "error_identification", "Sửa: “The flight lands on 9:00 AM.”", {"A": "lands", "B": "on", "C": "9:00", "D": "AM"}, "B", "At + giờ → at 9:00 AM.", 11, True),
            Q("Q_L03_01_06", 2, "multiple_choice", "The glass part of a camera is the _____.", {"A": "Body", "B": "Lens", "C": "Focus", "D": "Zoom"}, "B", "Lens = ống kính.", 10),
            Q("Q_L03_01_07", 1, "true_false", "“Luggage” is a countable noun — we say “luggages”.", {"A": "True", "B": "False"}, "B", "Luggage thường không đếm như vậy (uncountable).", 9),
            Q("Q_L03_01_08", 2, "multiple_choice", "“Máy bay hạ cánh lúc 3 giờ chiều.”", {"A": "The plane lands at 3 PM.", "B": "The plane lands on 3 PM.", "C": "The plane land at 3 PM.", "D": "The plane is land at 3 PM."}, "A", "Lands at 3 PM.", 11),
            Q("Q_L03_01_09", 3, "multiple_choice", "Thứ tự hợp lý:", {"A": "Check in → Take off → Land", "B": "Take off → Land → Check in", "C": "Land → Check in → Take off", "D": "Take off → Check in → Land"}, "A", "Làm thủ tục → cất cánh → hạ cánh.", 13),
            Q("Q_L03_01_10", 2, "fill_in_blank", "He likes to capture beautiful _____ (landscapes).", {"A": "landscapes", "B": "luggage", "C": "passports", "D": "receptions"}, "A", "Beautiful landscapes.", 10),
        ],
    }


def _lesson_02():
    meta = {"skill": "grammar", "topic": "past_simple", "time_est_minutes": 35, "difficulty": 0.5}
    p1 = """### *To be* in the past — **was / were**

- *I / he / she / it + was* — *I was tired yesterday.* (*wasn't*)  
- *You / we / they + were* — *They were at the park.* (*weren't*)

**Dấu hiệu:** *yesterday*, *last night/week*, *… ago* (two days ago)."""

    p2 = """### Regular verbs (-ed)

*Play → played*, *work → worked*, *arrive → arrived*

**Khẳng định:** *S + V-ed* — *We walked to the hotel.*"""

    p3 = """### Irregular verbs & questions/negatives

*Go → went*, *have → had*, *buy → bought*, *take → took*

**Phủ định:** *S + didn't + V (nguyên mẫu)* — không chia V sau *didn't*.

**Nghi vấn:** *Did + S + V?*"""

    reading = (
        "I was busy yesterday. We were at home last night. They went to the park and played football. "
        "She didn't buy anything. Did you work last weekend?"
    )
    return {
        "lesson_id": "L03_02",
        "lesson_name": "Past Simple - Regular & Irregular (Grammar)",
        "order": 2,
        "estimated_minutes": 45,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Was / Were", "body": p1},
                {"title": "Trang 2 — Regular verbs", "body": p2},
                {"title": "Trang 3 — Irregular & did/didn't", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "was / were / didn't / did", "vi": "quá khứ của be; trợ động từ quá khứ"},
            ],
            "examples": [
                {"english": "He wasn't at the hotel.", "vietnamese": "Anh ấy không ở khách sạn."},
            ],
        },
        "quizzes": [
            Q("Q_L03_02_01", 2, "multiple_choice", "I _____ at home last night.", {"A": "was", "B": "were", "C": "am", "D": "be"}, "A", "I was.", 9),
            Q("Q_L03_02_02", 2, "multiple_choice", "They _____ to Paris last summer.", {"A": "go", "B": "goed", "C": "went", "D": "going"}, "C", "Go → went.", 10),
            Q("Q_L03_02_03", 2, "fill_in_blank", "She (buy) _____ a new lens yesterday.", {"A": "buyed", "B": "bought", "C": "buys", "D": "buying"}, "B", "Buy → bought.", 10),
            Q("Q_L03_02_04", 2, "error_identification", "Sửa: “I didn't went to school.”", {"A": "didn't", "B": "went", "C": "to", "D": "school"}, "B", "didn't go.", 11, True),
            Q("Q_L03_02_05", 2, "multiple_choice", "_____ you like the movie?", {"A": "Do", "B": "Did", "C": "Was", "D": "Were"}, "B", "Past → Did.", 10),
            Q("Q_L03_02_06", 2, "fill_in_blank", "We (work) _____ very hard last week.", {"A": "work", "B": "worked", "C": "working", "D": "works"}, "B", "Regular -ed.", 9),
            Q("Q_L03_02_07", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "I didn't have time.", "B": "I didn't had time.", "C": "I not didn't have time.", "D": "Didn't I have time."}, "A", "didn't + have.", 11),
            Q("Q_L03_02_08", 1, "true_false", "The past of “take” is “taked”.", {"A": "True", "B": "False"}, "B", "Take → took.", 8),
            Q("Q_L03_02_09", 2, "multiple_choice", "“Anh ấy không ở khách sạn.” (past)", {"A": "He wasn't at the hotel.", "B": "He isn't at the hotel.", "C": "He not was at the hotel.", "D": "He didn't be at the hotel."}, "A", "wasn't at the hotel.", 11),
            Q("Q_L03_02_10", 3, "multiple_choice", "Ghép quá khứ: 1. Have — 2. See — 3. Buy", {"A": "1→had, 2→saw, 3→bought", "B": "1→saw, 2→bought, 3→had", "C": "1→bought, 2→had, 3→saw", "D": "1→haved, 2→seed, 3→buyed"}, "A", "Have→had, See→saw, Buy→bought.", 14),
        ],
    }


def _lesson_03():
    meta = {"skill": "reading", "topic": "past_events", "time_est_minutes": 30, "difficulty": 0.55}
    text = (
        "Last month, Alex went to Kyoto, Japan. It was a beautiful trip. He flew from New York and arrived in the morning. "
        "He booked a small traditional hotel. On the first day, he didn't rest. He took his mirrorless camera and walked around the city. "
        "He saw many old temples and took hundreds of photos. The weather was perfect. In the evening, he ate delicious sushi. "
        "He didn't buy many souvenirs, but he had great memories."
    )
    p1 = """### Pre-reading

**Từ:** *temple*, *traditional*, *delicious*, *memory*.

**Ngữ pháp:** Động từ quá khứ — *went, flew, arrived, booked, took, saw, ate, was, didn't …*"""

    p2 = """### Reading text

Đọc kỹ đoạn về **chuyến đi Kyoto** — gạch **thời gian** và **hành động**."""

    p3 = """### Post-reading — scanning

- Tìm phủ định: *didn't rest*, *didn't buy many souvenirs* — tương phản nghĩa.  
- *Flew* = quá khứ của *fly*."""

    return {
        "lesson_id": "L03_03",
        "lesson_name": "A Memorable Trip (Reading)",
        "order": 3,
        "estimated_minutes": 40,
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
                {"word": "temple / traditional / souvenir", "vi": "đền chùa / truyền thống / quà lưu niệm"},
            ],
            "examples": [],
        },
        "quizzes": [
            Q("Q_L03_03_01", 1, "multiple_choice", "Where did Alex go?", {"A": "Tokyo", "B": "Kyoto", "C": "New York", "D": "Osaka"}, "B", "Kyoto, Japan.", 9),
            Q("Q_L03_03_02", 1, "true_false", "He arrived in the evening.", {"A": "True", "B": "False"}, "B", "Arrived in the morning.", 8),
            Q("Q_L03_03_03", 2, "fill_in_blank", "He took a mirrorless _____ to take photos.", {"A": "camera", "B": "hotel", "C": "temple", "D": "sushi"}, "A", "Mirrorless camera.", 9),
            Q("Q_L03_03_04", 2, "multiple_choice", "What did he do on the first day?", {"A": "He rested all day", "B": "He walked and took photos", "C": "He flew back", "D": "He slept"}, "B", "Didn't rest — walked and took photos.", 11),
            Q("Q_L03_03_05", 2, "fill_in_blank", "What did he eat in the evening? — _____", {"A": "Delicious sushi", "B": "Pizza", "C": "Breakfast", "D": "Coffee only"}, "A", "Ate delicious sushi.", 10),
            Q("Q_L03_03_06", 2, "multiple_choice", "Did he buy many souvenirs?", {"A": "Yes, he did", "B": "No, he didn't", "C": "The text doesn't say", "D": "He bought hundreds"}, "B", "He didn't buy many souvenirs.", 10),
            Q("Q_L03_03_07", 2, "multiple_choice", "The base form (infinitive) of “flew” is:", {"A": "fly", "B": "flow", "C": "flee", "D": "flight"}, "A", "Fly — flew.", 10),
            Q("Q_L03_03_08", 1, "true_false", "The weather was bad.", {"A": "True", "B": "False"}, "B", "The weather was perfect.", 8),
            Q("Q_L03_03_09", 2, "fill_in_blank", "He saw many old _____.", {"A": "temples", "B": "cameras", "C": "flights", "D": "memories"}, "A", "Old temples.", 9),
            Q("Q_L03_03_10", 2, "fill_in_blank", "The text is about Alex's _____ to Japan.", {"A": "trip", "B": "camera only", "C": "breakfast", "D": "ticket"}, "A", "A memorable trip.", 10),
        ],
    }


def _lesson_04():
    meta = {"skill": "vocabulary", "topic": "technology", "time_est_minutes": 25, "difficulty": 0.5}
    p1 = """### Hardware & wearables

*Laptop*, *smartphone*, *screen*, *battery*  
*Smartwatch*, *fitness band*, *sensor*

**Động từ:** *charge*, *connect*"""

    p2 = """### Software & internet

*Application / app*, *browser*, *cloud*, *network*

**Động từ:** *download*, *install*, *update*, *search*"""

    p3 = """### Data & features

*Feature*, *data*, *speed*, *storage*

**Ngữ cảnh:** *I use my smartwatch to track my health data.*"""

    reading = (
        "My smartphone has a fast processor. I download apps from the store. "
        "I use a browser to search for information. The battery lasts all day. "
        "My smartwatch has a heart-rate sensor."
    )
    return {
        "lesson_id": "L03_04",
        "lesson_name": "Tech & Smart Devices (Vocabulary)",
        "order": 4,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Hardware & wearables", "body": p1},
                {"title": "Trang 2 — Software & internet", "body": p2},
                {"title": "Trang 3 — Data & features", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "smartwatch / sensor / browser", "vi": "đồng hồ thông minh / cảm biến / trình duyệt"},
            ],
            "examples": [
                {"english": "This device has many features.", "vietnamese": "Thiết bị này có nhiều tính năng."},
            ],
        },
        "quizzes": [
            Q("Q_L03_04_01", 1, "multiple_choice", "You wear this on your wrist:", {"A": "Laptop", "B": "Smartwatch", "C": "Screen", "D": "Browser"}, "B", "Smartwatch.", 8),
            Q("Q_L03_04_02", 2, "multiple_choice", "When your battery is low, you need to _____ it.", {"A": "Charge", "B": "Install", "C": "Search", "D": "Delete"}, "A", "Charge the battery.", 9),
            Q("Q_L03_04_03", 2, "fill_in_blank", "I _____ a new app from the store.", {"A": "download", "B": "charge", "C": "sensor", "D": "cloud"}, "A", "Download (or install) an app.", 10),
            Q("Q_L03_04_04", 3, "multiple_choice", "Ghép: 1. Fitness — 2. Cloud", {"A": "1→band, 2→storage", "B": "1→storage, 2→band", "C": "1→browser, 2→battery", "D": "1→lens, 2→zoom"}, "A", "Fitness band; cloud storage.", 12),
            Q("Q_L03_04_05", 2, "error_identification", "Sửa: “I search the informations on the browser.”", {"A": "search", "B": "informations", "C": "on", "D": "browser"}, "B", "Information (uncountable).", 11, True),
            Q("Q_L03_04_06", 2, "multiple_choice", "To open a website, you need a _____.", {"A": "Sensor", "B": "Browser", "C": "Battery", "D": "Lens"}, "B", "Browser.", 9),
            Q("Q_L03_04_07", 1, "true_false", "You install hardware (like a screen) from an app store.", {"A": "True", "B": "False"}, "B", "You install software/apps.", 9),
            Q("Q_L03_04_08", 2, "multiple_choice", "“Thiết bị này có nhiều tính năng.”", {"A": "This device has many features.", "B": "This device has many storages.", "C": "This device have many feature.", "D": "This device many features has."}, "A", "Has many features.", 11),
            Q("Q_L03_04_09", 2, "fill_in_blank", "The opposite of “download” is often _____.", {"A": "upload", "B": "install", "C": "charge", "D": "search"}, "A", "Upload vs download.", 10),
            Q("Q_L03_04_10", 2, "fill_in_blank", "The smartwatch has a _____ to check your heart rate.", {"A": "sensor", "B": "lyrics", "C": "temple", "D": "genre"}, "A", "Heart-rate sensor.", 10),
        ],
    }


def _lesson_05():
    meta = {"skill": "grammar", "topic": "comparisons", "time_est_minutes": 35, "difficulty": 0.6}
    p1 = """### Comparatives (so sánh hơn)

So sánh **hai** đối tượng — thường có **than**.

- Tính từ ngắn: *-er* — *faster*, *cheaper*  
- Tính từ dài: *more + adj* — *more beautiful*, *more expensive*"""

    p2 = """### Superlatives (so sánh nhất)

So sánh **từ ba** trở lên — thường có **the**.

- Ngắn: *the fastest*, *the cheapest*  
- Dài: *the most beautiful*"""

    p3 = """### Đặc biệt & bất quy tắc

- *y → ier / iest*: *easy → easier → the easiest*  
- Gấp đôi phụ âm: *big → bigger → the biggest*  
- Bất quy tắc: *good → better → the best*; *bad → worse → the worst*; *far → further/farther*"""

    reading = "This phone is cheaper than that one. It is the most useful app on my phone. The screen is bigger than before."
    return {
        "lesson_id": "L03_05",
        "lesson_name": "Comparatives & Superlatives (Grammar)",
        "order": 5,
        "estimated_minutes": 45,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Comparatives", "body": p1},
                {"title": "Trang 2 — Superlatives", "body": p2},
                {"title": "Trang 3 — Exceptions & irregulars", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "than / the most / -er / -est", "vi": "so sánh hơn / nhất / tính từ ngắn"},
            ],
            "examples": [
                {"english": "This is the best camera.", "vietnamese": "Đây là chiếc máy ảnh tốt nhất."},
            ],
        },
        "quizzes": [
            Q("Q_L03_05_01", 2, "multiple_choice", "A laptop is _____ than a smartphone (usually).", {"A": "heavy", "B": "heavier", "C": "heaviest", "D": "more heavier"}, "B", "Heavier than.", 10),
            Q("Q_L03_05_02", 2, "multiple_choice", "This is _____ app on my phone.", {"A": "the usefulest", "B": "the most useful", "C": "more useful", "D": "usefullest"}, "B", "The most useful.", 10),
            Q("Q_L03_05_03", 2, "fill_in_blank", "My internet is (fast) _____ than yours.", {"A": "faster", "B": "more fast", "C": "fastest", "D": "more faster"}, "A", "Faster than.", 9),
            Q("Q_L03_05_04", 2, "error_identification", "Sửa: “He is the better student in the class.”", {"A": "He", "B": "better", "C": "student", "D": "class"}, "B", "The best student (superlative trong nhóm).", 12, True),
            Q("Q_L03_05_05", 2, "multiple_choice", "Today the weather is _____ than yesterday.", {"A": "badder", "B": "worse", "C": "worst", "D": "more bad"}, "B", "Worse than (bad → worse).", 10),
            Q("Q_L03_05_06", 2, "fill_in_blank", "A smartwatch is (expensive) _____ than a fitness band.", {"A": "more expensive", "B": "expensiver", "C": "most expensive", "D": "expensiver than"}, "A", "More expensive than.", 10),
            Q("Q_L03_05_07", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "This is the biggest screen.", "B": "This is the biggester screen.", "C": "This the is biggest screen.", "D": "This is biggest the screen."}, "A", "The biggest screen.", 10),
            Q("Q_L03_05_08", 1, "true_false", "The comparative of “easy” is “easyer”.", {"A": "True", "B": "False"}, "B", "Easier.", 8),
            Q("Q_L03_05_09", 2, "multiple_choice", "“Đây là chiếc máy ảnh tốt nhất.”", {"A": "This is the best camera.", "B": "This is the better camera.", "C": "This is best the camera.", "D": "This is the goodest camera."}, "A", "The best camera.", 10),
            Q("Q_L03_05_10", 3, "multiple_choice", "Ghép dạng so sánh hơn: 1. Big — 2. Good — 3. Expensive", {"A": "1→bigger, 2→better, 3→more expensive", "B": "1→more big, 2→gooder, 3→expensiver", "C": "1→bigger, 2→more good, 3→expensiver", "D": "1→biggest, 2→better, 3→more expensive"}, "A", "Bigger, better, more expensive.", 14),
        ],
    }


def _lesson_06():
    meta = {"skill": "reading", "topic": "tech_comparisons", "time_est_minutes": 30, "difficulty": 0.65}
    text = (
        "Many people want to track their health. Should you buy a smartwatch or a fitness band? "
        "A fitness band is smaller and cheaper than a smartwatch. It is the best choice for a tight budget. "
        "It has a great battery. However, a smartwatch has a bigger screen and more features. "
        "It can run apps and connect to Wi-Fi. The sensors on a premium smartwatch are often more accurate than a cheap band. "
        "If you only want to count your steps, the band is better. If you want a mini computer on your wrist, the smartwatch is the winner."
    )
    p1 = """### Pre-reading

**Từ:** *compare*, *accurate*, *budget*, *step*.

**Mục tiêu:** So sánh **smartwatch** và **fitness band** — tìm *cheaper*, *smaller*, *more features*…"""

    p2 = """### Reading text

Đọc ý **ưu / nhược** của từng thiết bị và **kết luận** (*If you only… / If you want…*)."""

    p3 = """### Post-reading — argument

- Band: *smaller*, *cheaper*, *battery* tốt.  
- Smartwatch: *bigger screen*, *more features*, *more accurate* (premium).  
- Kết luận theo nhu cầu: đếm bước chân vs “mini computer”."""

    return {
        "lesson_id": "L03_06",
        "lesson_name": "Choosing the Right Device (Reading)",
        "order": 6,
        "estimated_minutes": 42,
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
                {"word": "fitness band / premium / accurate", "vi": "vòng tay thể thao / cao cấp / chính xác"},
            ],
            "examples": [],
        },
        "quizzes": [
            Q("Q_L03_06_01", 1, "multiple_choice", "Which device is cheaper?", {"A": "Fitness band", "B": "Smartwatch", "C": "Laptop", "D": "Camera"}, "A", "Smaller and cheaper than a smartwatch.", 8),
            Q("Q_L03_06_02", 1, "true_false", "A fitness band has a bigger screen than a smartwatch.", {"A": "True", "B": "False"}, "B", "Smartwatch has a bigger screen.", 8),
            Q("Q_L03_06_03", 2, "fill_in_blank", "The fitness band is the best choice for a tight _____.", {"A": "budget", "B": "screen", "C": "sensor", "D": "winner"}, "A", "Tight budget.", 9),
            Q("Q_L03_06_04", 2, "multiple_choice", "Which usually has more accurate sensors (according to the text)?", {"A": "The cheap band", "B": "The premium smartwatch", "C": "A laptop", "D": "A browser"}, "B", "Premium smartwatch sensors more accurate than a cheap band.", 12),
            Q("Q_L03_06_05", 2, "fill_in_blank", "A smartwatch can connect to _____.", {"A": "Wi-Fi", "B": "only paper", "C": "luggage", "D": "passport"}, "A", "Connect to Wi-Fi.", 9),
            Q("Q_L03_06_06", 2, "multiple_choice", "If you only want to count steps, which is better?", {"A": "Fitness band", "B": "Smartwatch", "C": "Piano", "D": "Temple"}, "A", "The band is better for counting steps.", 11),
            Q("Q_L03_06_07", 2, "fill_in_blank", "Find a superlative in the text: “It is the _____ choice…”", {"A": "best", "B": "better", "C": "good", "D": "goodest"}, "A", "The best choice.", 10),
            Q("Q_L03_06_08", 1, "true_false", "A smartwatch is described as a kind of mini computer on your wrist.", {"A": "True", "B": "False"}, "A", "“Mini computer on your wrist”.", 9),
            Q("Q_L03_06_09", 2, "fill_in_blank", "A fitness band is _____ than a smartwatch.", {"A": "smaller", "B": "bigger", "C": "slower", "D": "worse"}, "A", "Smaller and cheaper.", 10),
            Q("Q_L03_06_10", 2, "fill_in_blank", "The text mainly _____ two types of wearables.", {"A": "compares", "B": "composes", "C": "lands", "D": "coughs"}, "A", "Compares smartwatch and fitness band.", 10),
        ],
    }


def _lesson_07():
    meta = {"skill": "vocabulary", "topic": "music", "time_est_minutes": 25, "difficulty": 0.55}
    p1 = """### Instruments & gear

*Acoustic guitar*, *piano*, *keyboard*, *drums*  
*Amplifier / amp*, *microphone*

**Động từ:** *tune*, *plug in*"""

    p2 = """### Musical elements

*Melody*, *rhythm*, *chord*, *lyrics*, *genre*

**Ngữ cảnh:** *He plays a complex chord on his guitar.*"""

    p3 = """### Actions

*Practice*, *perform*, *record*, *compose*  
*Producer*, *DAW* (digital audio workstation)"""

    reading = (
        "She plays the acoustic guitar every weekend. The lyrics of this song are beautiful. "
        "He uses an amplifier for his electric guitar. They practice before the concert."
    )
    return {
        "lesson_id": "L03_07",
        "lesson_name": "Music & Instruments (Vocabulary)",
        "order": 7,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Instruments & gear", "body": p1},
                {"title": "Trang 2 — Elements", "body": p2},
                {"title": "Trang 3 — Actions & roles", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "chord / lyrics / rhythm", "vi": "hợp âm / lời bài hát / nhịp"},
            ],
            "examples": [
                {"english": "He is practicing a new chord.", "vietnamese": "Anh ấy đang luyện một hợp âm mới."},
            ],
        },
        "quizzes": [
            Q("Q_L03_07_01", 1, "multiple_choice", "An instrument with six strings is usually a:", {"A": "Guitar", "B": "Drum", "C": "Piano", "D": "Mic"}, "A", "Guitar — typically six strings.", 8),
            Q("Q_L03_07_02", 1, "multiple_choice", "The words of a song are called:", {"A": "Melody", "B": "Lyrics", "C": "Chords", "D": "Rhythm"}, "B", "Lyrics.", 8),
            Q("Q_L03_07_03", 2, "fill_in_blank", "I need an _____ to make my electric guitar louder.", {"A": "amplifier", "B": "browser", "C": "passport", "D": "sensor"}, "A", "Amplifier / amp.", 9),
            Q("Q_L03_07_04", 3, "multiple_choice", "Ghép: 1. Play — 2. Write", {"A": "1→chords, 2→lyrics", "B": "1→lyrics, 2→chords", "C": "1→rhythm, 2→genre", "D": "1→drums, 2→piano"}, "A", "Play chords; write lyrics.", 12),
            Q("Q_L03_07_05", 2, "error_identification", "Sửa: “He compose a new song yesterday.”", {"A": "He", "B": "compose", "C": "song", "D": "yesterday"}, "B", "Composed (past).", 11, True),
            Q("Q_L03_07_06", 2, "multiple_choice", "To save your voice or music to a computer, you often _____ it.", {"A": "Practice", "B": "Record", "C": "Tune", "D": "Land"}, "B", "Record.", 10),
            Q("Q_L03_07_07", 2, "true_false", "“Rhythm” is the same as pitch (how high or low a note is).", {"A": "True", "B": "False"}, "B", "Rhythm = beat/timing; pitch is high/low.", 10),
            Q("Q_L03_07_08", 2, "multiple_choice", "“Anh ấy đang luyện tập hợp âm mới.”", {"A": "He is practicing a new chord.", "B": "He practice a new chord.", "C": "He is practice a new chord.", "D": "He practicing a new chord."}, "A", "Is practicing.", 11),
            Q("Q_L03_07_09", 3, "multiple_choice", "Logical order for making a song (general):", {"A": "Compose → Record → Perform", "B": "Perform → Compose → Record", "C": "Record → Perform → Compose", "D": "Compose → Perform → Record only wrong"}, "A", "Often compose → record → perform (contextual).", 13),
            Q("Q_L03_07_10", 2, "fill_in_blank", "Ableton Live is popular software used by a music _____.", {"A": "producer", "B": "browser", "C": "tourist", "D": "luggage"}, "A", "Music producer.", 10),
        ],
    }


def _lesson_08():
    meta = {"skill": "grammar", "topic": "past_continuous", "time_est_minutes": 35, "difficulty": 0.65}
    p1 = """### Past continuous

**was / were + V-ing** — hành động **đang diễn ra** tại một thời điểm trong quá khứ.

*At 8 PM last night, I was playing the guitar.*"""

    p2 = """### When — hành động cắt ngang

Hành động **dài** (past continuous) + **when** + hành động **ngắn** (past simple).

*I was practicing when the phone rang.*"""

    p3 = """### While — song song

Hai hành động **dài** cùng lúc:

*While I was playing the guitar, he was singing.*"""

    reading = (
        "At 9 PM yesterday, I was watching TV. When the lights went out, I was reading a book. "
        "While my brother was cooking, I was setting the table."
    )
    return {
        "lesson_id": "L03_08",
        "lesson_name": "Past Continuous vs Past Simple (Grammar)",
        "order": 8,
        "estimated_minutes": 45,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Past continuous", "body": p1},
                {"title": "Trang 2 — When", "body": p2},
                {"title": "Trang 3 — While", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "was/were + -ing", "vi": "quá khứ tiếp diễn"},
            ],
            "examples": [
                {"english": "I was sleeping when she called.", "vietnamese": "Tôi đang ngủ thì cô ấy gọi."},
            ],
        },
        "quizzes": [
            Q("Q_L03_08_01", 2, "multiple_choice", "At 10 PM yesterday, I _____ TV.", {"A": "watched", "B": "was watching", "C": "watch", "D": "am watching"}, "B", "At a moment in the past → was watching.", 11),
            Q("Q_L03_08_02", 2, "multiple_choice", "I was walking home _____ it started to rain.", {"A": "while", "B": "when", "C": "what", "D": "during"}, "B", "When + past simple (short action).", 10),
            Q("Q_L03_08_03", 2, "fill_in_blank", "_____ I was working, she was reading a book.", {"A": "While", "B": "When", "C": "Then", "D": "Last"}, "A", "While + parallel actions.", 10),
            Q("Q_L03_08_04", 2, "error_identification", "Sửa: “When he arrived, I am sleeping.”", {"A": "When", "B": "arrived", "C": "am sleeping", "D": "I"}, "C", "I was sleeping.", 11, True),
            Q("Q_L03_08_05", 2, "multiple_choice", "The phone _____ while I was taking a shower.", {"A": "rang", "B": "was ringing", "C": "ringed", "D": "rung"}, "A", "Short interrupt → rang (past simple).", 12),
            Q("Q_L03_08_06", 2, "fill_in_blank", "They (play) _____ games at 3 PM yesterday.", {"A": "were playing", "B": "played", "C": "playing", "D": "are playing"}, "A", "At 3 PM yesterday → were playing.", 10),
            Q("Q_L03_08_07", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "I was studying when you arrived.", "B": "I studying was when you arrived.", "C": "When you arrived I studying.", "D": "I was study when you arrived."}, "A", "Was studying when…", 11),
            Q("Q_L03_08_08", 1, "true_false", "“We were play football” is correct.", {"A": "True", "B": "False"}, "B", "We were playing.", 8),
            Q("Q_L03_08_09", 2, "multiple_choice", "“Tôi đang ngủ thì cô ấy gọi.”", {"A": "I was sleeping when she called.", "B": "I slept when she called.", "C": "I am sleeping when she called.", "D": "I sleeping when she called."}, "A", "Was sleeping when… called.", 11),
            Q("Q_L03_08_10", 3, "multiple_choice", "Ghép: 1. Long background action — 2. Short interrupting action", {"A": "1→Past Continuous, 2→Past Simple", "B": "1→Past Simple, 2→Past Continuous", "C": "1→Present, 2→Future", "D": "1→Future, 2→Past"}, "A", "Long: was/were -ing; short: V2.", 13),
        ],
    }


def _lesson_09():
    meta = {"skill": "vocabulary", "topic": "health_lifestyle", "time_est_minutes": 25, "difficulty": 0.5}
    p1 = """### Symptoms

*Headache*, *stomachache*, *fever*, *cough*, *cold*

**Cấu trúc:** *I have a + noun* — *I have a fever.*

*Feel sick*, *hurt*"""

    p2 = """### Treatment

*Medicine / pill*, *rest*, *see a doctor*, *hospital*

**Động từ:** *take medicine*, *recover*"""

    p3 = """### Healthy lifestyle

*Workout / exercise*, *diet*, *nutrition*, *stay hydrated*  
*Mental health*, *reduce stress*"""

    reading = (
        "I have a headache today. I need to rest and drink water. If I feel worse, I will see a doctor. "
        "Exercise and a good diet help my mental health."
    )
    return {
        "lesson_id": "L03_09",
        "lesson_name": "Health, Fitness & Lifestyle (Vocabulary)",
        "order": 9,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Symptoms", "body": p1},
                {"title": "Trang 2 — Treatment", "body": p2},
                {"title": "Trang 3 — Lifestyle", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "take medicine / stay hydrated", "vi": "uống thuốc / giữ đủ nước"},
            ],
            "examples": [
                {"english": "I feel sick. I need to see a doctor.", "vietnamese": "Tôi cảm thấy ốm. Tôi cần đi khám bác sĩ."},
            ],
        },
        "quizzes": [
            Q("Q_L03_09_01", 1, "multiple_choice", "If your head hurts, you have a _____.", {"A": "Fever", "B": "Headache", "C": "Cough", "D": "Diet"}, "B", "Headache.", 8),
            Q("Q_L03_09_02", 2, "multiple_choice", "When you are sick, you should _____ medicine.", {"A": "eat", "B": "drink", "C": "take", "D": "make"}, "C", "Take medicine.", 9),
            Q("Q_L03_09_03", 2, "fill_in_blank", "You should drink water to stay _____.", {"A": "hydrated", "B": "stress", "C": "cold", "D": "lyrics"}, "A", "Stay hydrated.", 9),
            Q("Q_L03_09_04", 3, "multiple_choice", "Ghép: 1. Physical — 2. Mental", {"A": "1→workout, 2→health (mental health)", "B": "1→mental, 2→physical", "C": "1→fever, 2→cough", "D": "1→doctor, 2→hospital"}, "A", "Physical workout; mental health.", 12),
            Q("Q_L03_09_05", 2, "error_identification", "Sửa: “I have cough.”", {"A": "I", "B": "have", "C": "cough", "D": "—"}, "C", "Have a cough.", 10, True),
            Q("Q_L03_09_06", 2, "multiple_choice", "Eating fruit and vegetables is part of a good _____.", {"A": "Diet", "B": "Medicine", "C": "Fever", "D": "Cough"}, "A", "A good diet.", 9),
            Q("Q_L03_09_07", 1, "true_false", "“Rest” means you keep working without stopping.", {"A": "True", "B": "False"}, "B", "Rest = nghỉ.", 8),
            Q("Q_L03_09_08", 2, "multiple_choice", "“Tôi cảm thấy ốm. Tôi cần đi khám bác sĩ.”", {"A": "I feel sick. I need to see a doctor.", "B": "I feel sick. I need see doctor.", "C": "I am feel sick. I need to see a doctor.", "D": "I feel sickly. I need see a doctor."}, "A", "Feel sick; see a doctor.", 11),
            Q("Q_L03_09_09", 3, "multiple_choice", "Logical order:", {"A": "Feel sick → Take medicine → Recover", "B": "Recover → Feel sick → Take medicine", "C": "Take medicine → Feel sick → Recover", "D": "Feel sick → Recover → Take medicine"}, "A", "Often feel sick → treatment → recover.", 13),
            Q("Q_L03_09_10", 2, "fill_in_blank", "Listening to music can reduce _____.", {"A": "stress", "B": "water", "C": "guitar", "D": "browser"}, "A", "Reduce stress.", 9),
        ],
    }


def _lesson_10():
    meta = {"skill": "reading", "topic": "music_past_narrative", "time_est_minutes": 35, "difficulty": 0.7}
    text = (
        "Yesterday was the most productive day for Ben. He is a music producer. In the afternoon, he was sitting in his studio while it was raining outside. "
        "The sound of the rain was louder than usual, but it inspired him. He was practicing a new chord on his acoustic guitar when his friend, Sarah, called. "
        "She is a better singer than him. They decided to record a song. While Ben was playing the guitar and recording on his laptop, Sarah was singing. "
        "The session was amazing. It was faster and easier than their last song."
    )
    p1 = """### Pre-reading

**Từ:** *session*, *background*, *focus*, *inspire*.

**Ngữ pháp:** Quá khứ đơn + quá khứ tiếp diễn + so sánh — trong **một** câu chuyện thu âm."""

    p2 = """### Reading text

The **Rainy Session** — theo dõi *while*, *when*, *than*, *better*, *most productive*."""

    p3 = """### Post-reading

- *While* … *was raining* / *While Ben was playing… Sarah was singing*  
- *When* … *was practicing… when Sarah called*  
- So sánh: *the most productive*, *louder than*, *a better singer*, *faster and easier than*"""

    return {
        "lesson_id": "L03_10",
        "lesson_name": "The Rainy Session (Reading)",
        "order": 10,
        "estimated_minutes": 48,
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
                {"word": "session / producer / inspired", "vi": "buổi thu / nhà sản xuất / truyền cảm hứng"},
            ],
            "examples": [],
        },
        "quizzes": [
            Q("Q_L03_10_01", 1, "multiple_choice", "What was the weather like yesterday?", {"A": "Sunny", "B": "Raining", "C": "Hot", "D": "Snowing"}, "B", "It was raining.", 8),
            Q("Q_L03_10_02", 1, "true_false", "Ben was playing the piano when Sarah called.", {"A": "True", "B": "False"}, "B", "Acoustic guitar.", 8),
            Q("Q_L03_10_03", 2, "fill_in_blank", "Sarah is a _____ singer than Ben.", {"A": "better", "B": "good", "C": "best", "D": "more good"}, "A", "A better singer than him.", 9),
            Q("Q_L03_10_04", 2, "multiple_choice", "What was Ben doing when Sarah called?", {"A": "Practicing a chord on his guitar", "B": "Sleeping", "C": "Driving", "D": "Cooking"}, "A", "Was practicing… when… called.", 11),
            Q("Q_L03_10_05", 2, "fill_in_blank", "Where was Ben sitting? — In his _____.", {"A": "studio", "B": "bank", "C": "airport", "D": "hospital"}, "A", "Sitting in his studio.", 9),
            Q("Q_L03_10_06", 2, "multiple_choice", "“While Ben was playing, Sarah was singing” describes:", {"A": "Two parallel long actions", "B": "Only one verb", "C": "Future plans", "D": "Present habits"}, "A", "Parallel past continuous.", 12),
            Q("Q_L03_10_07", 2, "fill_in_blank", "A superlative in the first sentence: “Yesterday was the _____ productive day…”", {"A": "most", "B": "more", "C": "much", "D": "many"}, "A", "The most productive.", 10),
            Q("Q_L03_10_08", 2, "true_false", "Recording this song was harder than their last song.", {"A": "True", "B": "False"}, "B", "Faster and easier than their last song.", 9),
            Q("Q_L03_10_09", 2, "fill_in_blank", "Ben was recording on his _____.", {"A": "laptop", "B": "drums", "C": "passport", "D": "luggage"}, "A", "Recording on his laptop.", 9),
            Q("Q_L03_10_10", 2, "fill_in_blank", "The text is about a successful music recording _____.", {"A": "session", "B": "fever", "C": "flight", "D": "browser"}, "A", "Recording session.", 9),
        ],
    }
