# -*- coding: utf-8 -*-
"""Tạo course_reading_a1.json (4 bài British Council A1). Chạy: python generate_reading_a1_fixture.py"""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).with_name("course_reading_a1.json")

PREP_FOOT = (
    "\n\nĐoạn đọc đầy đủ nằm trong tab **Bài tập** — dùng nút **Hiện đoạn đọc** phía trên câu hỏi."
)


def mc(qid: str, task: str | None, text: str, opts: dict, ans: str, hint: str) -> dict:
    return {
        "quiz_id": qid,
        "difficulty_level": 2,
        "question_type": "multiple_choice",
        "question_text": f"{task}\n{text}" if task else text,
        "options": opts,
        "correct_answer": ans,
        "hint_text": hint,
    }


def tf(qid: str, text: str, correct: str, hint: str) -> dict:
    return {
        "quiz_id": qid,
        "difficulty_level": 2,
        "question_type": "true_false",
        "question_text": text,
        "options": {"A": "True", "B": "False"},
        "correct_answer": correct,
        "hint_text": hint,
    }


def reading_lesson(
    lid: str,
    name: str,
    order: int,
    html: str,
    gd: dict,
    prep_body: str,
    passage: str,
    quizzes: list,
) -> dict:
    prep_full = (prep_body or "").strip() + PREP_FOOT
    return {
        "lesson_id": lid,
        "lesson_name": name,
        "order": order,
        "estimated_minutes": 30,
        "audio_url": "",
        "metadata": {"skill": "reading", "source_html": html, **gd},
        "content": {
            "preparation_pages": [{"title": "Chuẩn bị (Preparation)", "body": prep_full}],
            "reading_passage": passage.strip(),
        },
        "quizzes": quizzes,
    }


PASS_TIMETABLE = r"""## Reading text — A study timetable (summer school)

### Monday to Wednesday

| | Monday | Tuesday | Wednesday |
| --- | --- | --- | --- |
| 9.00 | English level test | Vocabulary | Whole day excursion to London or Oxford |
| 10.00 | English skills: Speaking | English skills: Reading | |
| 11.00 | Preparation for excursion | Preparation for excursion | |
| 12.00 | Lunch | Lunch | |
| 13.00 | Project class | Project class | |
| 15.00 | Art | Basketball | |
| 17.00 | Free time | Free time | |
| 18.00 | Dinner | Dinner | Dinner |
| 19.00 | Swimming | Football tournament | Cinema |
| 21.00 | Free time | Free time | Free time |

*(Wednesday is a full-day excursion — other times are not filled in separately in the original timetable.)*

### Thursday to Sunday

| | Thursday | Friday | Saturday | Sunday |
| --- | --- | --- | --- | --- |
| 9.00 | Grammar | Vocabulary | Grammar | Late breakfast |
| 10.00 | English skills: Speaking | English skills: Listening | Progress test | English skills: Writing |
| 11.00 | Games with English | Drama | Drama | Preparation for excursion |
| 12.00 | Lunch | Lunch | Lunch | Lunch |
| 13.00 | Project class | Project class | Theatre trip | Excursion to local castle or museum |
| 15.00 | Circus skills | Mountain biking | | |
| 17.00 | Free time | Free time | | |
| 18.00 | Dinner | Dinner | Dinner | Dinner |
| 19.00 | Bowling | Talent show | Disco | Free time / packing |
| 21.00 | Free time | Free time | Free time | Free time / packing |

*(Saturday afternoon/evening: theatre trip; Sunday afternoon: local excursion — details follow the merged cells in the original.)*
"""


PASS_MENU = """## Reading text — Tony's Kitchen (restaurant menu)

**Tony's Kitchen** — ★★★★★☆ — 231 reviews  
Chicken, Pizzas, Vegetarian  
**17 Broad Street** — **Opening at 11:30**

### Meat and fish
- Grilled fish of the day — **£8.00**
- Steak with chips or salad — **£12.00**
- Sausage and roast tomato pasta — **£7.00**
- Chicken salad with garlic yoghurt dressing — **£7.00**

### Vegetarian
- Cheese and tomato pizza — **£7.00**
- Mushroom omelette — **£6.00**
- Vegetable chili — **£7.00**
- Soup of the day with brown or white bread — **£4.00**

### Something sweet
- Homemade carrot cake — **£3.50**
- Homemade banana cake — **£3.50**
- Chocolate ice cream with chocolate sauce — **£3.50**
- Fresh fruit salad with grapes, mango, melon and apple, served with cream or ice cream — **£3.50**

### Drinks
- Cup of coffee — **£2.00**
- Cup of tea — **£1.50**
- Glass of wine, white or red — **£3.00**
- Beer — **£3.00**
- Water, still or sparkling — **£1.00**
- Orange juice — **£2.00**
"""


PASS_EXAM = """## Reading text — Exam posters

### Poster 1 — FINAL EXAM INSTRUCTIONS
- Doors close **5 minutes before** the exam begins.
- Show your **student ID card** to examiner when you enter the room.
- **No phones, no books.**

---

### Poster 2 — BEFORE THE EXAM
- Have your **ID card** ready.
- Listen to the instructions.
- **Arrive 10 minutes before** exam.

### Poster 2 — IN THE EXAM
- **Mobile phones** switched off and put away.
- **ID card visible** on the desk.
- **No talking.**
- **No food or drinks** in exam room.

---

### Poster 3
- Follow the examiner's instructions.
- If you have a question, **raise your hand**.
- No **mobile phones, books or bags** in the exam.
- Please use a **blue or black pen**.
"""


PASS_YOGA = """## Reading text — Office yoga poster

### Time to relax!

Come and join our **lunchtime yoga class** with experienced yoga teacher **Divya Bridge**!

- **When?** Every **Tuesday at 1.30 p.m.**
- **Where?** **Meeting Room 7**
- **How much?** **£10 for four 30-minute classes.**
- **What to bring?** Comfortable clothes. Divya will provide the **yoga mats**.
- **How to join?** Write to Sam at **Sam.Holden@example.com**

We can only take a maximum of **20** in the room, so book now!
"""


def main() -> None:
    prep_tt = """**A study timetable** — từ vựng đọc lịch / thời khóa biểu (British Council A1).

- **Days:** Monday, Tuesday, Wednesday … Sunday — **lunch**, **dinner**, **free time**.
- **School activities:** **English level test**, **vocabulary**, **grammar**, **English skills** (Speaking, Reading, Listening, Writing), **project class**, **progress test**.
- **Trips / fun:** **excursion** (đi tham quan), **theatre trip**, **cinema**, **swimming**, **football tournament**, **mountain biking**, **bowling**, **talent show**, **disco**."""
    q_tt = [
        mc("Q_tt_01", None, "Thứ Hai lúc 9.00 có hoạt động gì?", {"A": "Vocabulary", "B": "English level test", "C": "Grammar", "D": "Theatre trip"}, "B", "Bảng Monday."),
        mc("Q_tt_02", None, "Thứ Ba lúc 19.00 học sinh làm gì?", {"A": "Swimming", "B": "Football tournament", "C": "Cinema", "D": "Bowling"}, "B", "Tuesday 19.00: Football tournament."),
        mc("Q_tt_03", None, "Thứ Tư cả ngày là gì?", {"A": "Project class", "B": "Whole day excursion to London or Oxford", "C": "Late breakfast", "D": "Progress test"}, "B", "Reading text Wednesday."),
        mc("Q_tt_04", None, "Thứ Năm lúc 9.00 là tiết gì?", {"A": "Grammar", "B": "Vocabulary", "C": "English skills: Writing", "D": "Games with English"}, "A", "Thursday row 9.00."),
        mc("Q_tt_05", None, "Thứ Sáu lúc 10.00 là gì?", {"A": "English skills: Speaking", "B": "English skills: Listening", "C": "Progress test", "D": "Drama"}, "B", "Friday column."),
        mc("Q_tt_06", None, "Thứ Bảy lúc 10.00 có gì?", {"A": "Grammar", "B": "Progress test", "C": "Games with English", "D": "Mountain biking"}, "B", "Saturday."),
        mc("Q_tt_07", None, "Chủ nhật buổi sáng 9.00 (theo bảng) là gì?", {"A": "Grammar", "B": "Late breakfast", "C": "Project class", "D": "Theatre trip"}, "B", "Sunday 9.00."),
        mc("Q_tt_08", None, "Thứ Hai lúc 19.00 là hoạt động nào?", {"A": "Football tournament", "B": "Swimming", "C": "Talent show", "D": "Cinema"}, "B", "Monday 19.00."),
        mc("Q_tt_09", None, "Thứ Năm lúc 15.00:", {"A": "Art", "B": "Circus skills", "C": "Mountain biking", "D": "Drama"}, "B", "Thursday 15.00."),
        mc("Q_tt_10", None, "Thứ Sáu lúc 19.00:", {"A": "Bowling", "B": "Disco", "C": "Swimming", "D": "Cinema"}, "A", "Friday 19.00."),
        tf("Q_tt_11", "Chủ nhật lúc 11.00 có mục Preparation for excursion.", "A", "Sunday 11.00 row."),
        mc("Q_tt_12", None, "Thứ Hai và thứ Ba lúc 13.00 đều là:", {"A": "Theatre trip", "B": "Project class", "C": "Excursion", "D": "Games with English"}, "B", "13.00 Mon–Tue."),
        mc("Q_tt_13", None, "Thứ Bảy lúc 19.00:", {"A": "Bowling", "B": "Talent show", "C": "Disco", "D": "Football tournament"}, "C", "Saturday 19.00."),
        tf("Q_tt_14", "Thứ Tư học sinh vẫn có bữa tối (dinner) lúc 18.00 như các ngày khác.", "A", "Bảng Wednesday 18.00 Dinner."),
        mc("Q_tt_15", None, "Chủ nhật 13.00 chủ yếu là:", {"A": "Theatre trip", "B": "Excursion to local castle or museum", "C": "Project class", "D": "Circus skills"}, "B", "Sunday 13.00."),
        tf("Q_tt_16", "Thứ Hai 15.00 là Basketball.", "B", "Monday 15.00: Art."),
        mc("Q_tt_17", None, "Thứ Sáu lúc 11.00:", {"A": "Games with English", "B": "Drama", "C": "Preparation for excursion", "D": "Mountain biking"}, "B", "Friday 11.00."),
        mc("Q_tt_18", None, "Thứ Ba lúc 12.00:", {"A": "Dinner", "B": "Lunch", "C": "Free time", "D": "Excursion"}, "B", "12.00 Lunch."),
    ]

    prep_menu = """**A restaurant menu** — từ vựng đọc thực đơn (British Council A1).

- **Menu sections:** meat and fish, **vegetarian**, **something sweet**, **drinks**.
- **Prices:** ký hiệu **£** (pound); so sánh giá rẻ / đắt.
- **Useful words:** **grilled**, **steak**, **chips**, **salad**, **omelette**, **soup of the day**, **homemade**, **still or sparkling** (nước)."""
    q_menu = [
        mc("Q_mn_01", None, "Nhà hàng tên gì?", {"A": "Broad Kitchen", "B": "Tony's Kitchen", "C": "Chicken Pizza", "D": "231 Street"}, "B", "Đầu menu."),
        mc("Q_mn_02", None, "Địa chỉ ghi trên menu?", {"A": "11 Broad Street", "B": "17 Broad Street", "C": "7 Broad Street", "D": "21 Broad Street"}, "B", "17 Broad Street."),
        mc("Q_mn_03", None, "Mấy giờ mở cửa (opening)?", {"A": "9:00", "B": "10:30", "C": "11:30", "D": "12:00"}, "C", "Opening at 11:30."),
        mc("Q_mn_04", None, "Steak with chips or salad giá bao nhiêu?", {"A": "£7.00", "B": "£8.00", "C": "£12.00", "D": "£4.00"}, "C", "Meat and fish."),
        mc("Q_mn_05", None, "Món rẻ nhất trong nhóm Drinks là gì?", {"A": "Orange juice", "B": "Beer", "C": "Water, still or sparkling", "D": "Wine"}, "C", "Water £1.00."),
        mc("Q_mn_06", None, "Cheese and tomato pizza (vegetarian) giá?", {"A": "£6.00", "B": "£7.00", "C": "£8.00", "D": "£12.00"}, "B", "Vegetarian section."),
        mc("Q_mn_07", None, "Mushroom omelette giá?", {"A": "£6.00", "B": "£7.00", "C": "£4.00", "D": "£3.50"}, "A", "Vegetarian."),
        mc("Q_mn_08", None, "Soup of the day with bread giá?", {"A": "£3.50", "B": "£4.00", "C": "£7.00", "D": "£2.00"}, "B", "Vegetarian."),
        tf("Q_mn_09", "Menu ghi 231 reviews.", "A", "Đầu menu."),
        mc("Q_mn_10", None, "Cup of tea giá?", {"A": "£1.00", "B": "£1.50", "C": "£2.00", "D": "£3.00"}, "B", "Drinks."),
        mc("Q_mn_11", None, "Grilled fish of the day giá?", {"A": "£7.00", "B": "£8.00", "C": "£12.00", "D": "£6.00"}, "B", "Meat and fish."),
        mc("Q_mn_12", None, "Chocolate ice cream with chocolate sauce?", {"A": "£3.50", "B": "£4.00", "C": "£2.00", "D": "£1.50"}, "A", "Something sweet."),
        tf("Q_mn_13", "Chicken salad with garlic yoghurt dressing là £7.00.", "A", "Meat and fish list."),
        mc("Q_mn_14", None, "Beer giá?", {"A": "£1.00", "B": "£2.00", "C": "£3.00", "D": "£3.50"}, "C", "Drinks."),
        mc("Q_mn_15", None, "Orange juice?", {"A": "£1.50", "B": "£2.00", "C": "£3.00", "D": "£2.50"}, "B", "Drinks."),
        tf("Q_mn_16", "Vegetarian section có vegetable chili.", "A", "Vegetarian."),
        mc("Q_mn_17", None, "Cup of coffee?", {"A": "£1.50", "B": "£2.00", "C": "£2.50", "D": "£3.00"}, "B", "Drinks £2.00."),
        mc("Q_mn_18", None, "Homemade carrot cake?", {"A": "£3.00", "B": "£3.50", "C": "£4.00", "D": "£7.00"}, "B", "Something sweet."),
    ]

    prep_exam = """**Posters for exam candidates** — từ vựng hướng dẫn phòng thi (British Council A1).

- **ID card / student ID** — giấy tờ danh tính.
- **Arrive** — đến đúng giờ; **doors close** — đóng cửa.
- **Mobile phones** — điện thoại; **raise your hand** — giơ tay hỏi.
- **No food or drinks** — không ăn uống trong phòng thi."""
    q_exam = [
        tf("Q_ex_01", "Poster 1: cửa đóng 5 phút trước khi thi bắt đầu.", "A", "Doors close 5 minutes before…"),
        tf("Q_ex_02", "Poster 2 (Before): cần đến trước giờ thi 10 phút.", "A", "Arrive 10 minutes before exam."),
        mc("Q_ex_03", None, "Poster 3: nếu bạn muốn hỏi thì phải làm sao?", {"A": "Stand up", "B": "Raise your hand", "C": "Shout", "D": "Send email"}, "B", "Raise your hand."),
        tf("Q_ex_04", "Poster 1: được mang sách vào phòng.", "B", "No books."),
        tf("Q_ex_05", "Poster 2 (In the exam): điện thoại phải tắt và cất đi.", "A", "Mobile phones switched off…"),
        mc("Q_ex_06", None, "Poster 3: bút viết nên dùng màu nào?", {"A": "Red or green", "B": "Blue or black", "C": "Any colour", "D": "Pencil only"}, "B", "Blue or black pen."),
        tf("Q_ex_07", "Poster 2: thẻ ID phải để trên bàn (visible).", "A", "ID card visible on the desk."),
        tf("Q_ex_08", "Poster 2: được nói chuyện trong phòng thi.", "B", "No talking."),
        mc("Q_ex_09", None, "Poster 1 khi vào phòng cần làm gì với student ID?", {"A": "Hide it", "B": "Show it to the examiner", "C": "Leave at home", "D": "Throw away"}, "B", "Show your student ID…"),
        tf("Q_ex_10", "Poster 3: được mang túi vào phòng thi.", "B", "No bags."),
        mc("Q_ex_11", None, "Poster 2 trước thi: 'Have your … ready' với gì?", {"A": "Phone", "B": "ID card", "C": "Books", "D": "Food"}, "B", "Have your ID card ready."),
        tf("Q_ex_12", "Poster 2: trong phòng thi không được ăn uống.", "A", "No food or drinks."),
        mc("Q_ex_13", None, "Poster 1 có cho phép điện thoại không?", {"A": "Yes", "B": "No phones", "C": "Silent only", "D": "Only for photos"}, "B", "No phones."),
        tf("Q_ex_14", "Theo Poster 3, phải làm theo hướng dẫn của giám khảo (examiner).", "A", "Follow the examiner's instructions."),
        mc("Q_ex_15", None, "Poster 2 Before: học sinh cần làm gì với instructions?", {"A": "Ignore", "B": "Listen to the instructions", "C": "Read books", "D": "Use phone"}, "B", "Listen to the instructions."),
        tf("Q_ex_16", "Poster 3 cho phép mang sách vào phòng thi.", "B", "No books."),
        mc("Q_ex_17", None, "Poster 1: Doors close khi nào?", {"A": "After exam", "B": "5 minutes before the exam begins", "C": "During lunch", "D": "Never"}, "B", "Poster 1 bullet."),
        tf("Q_ex_18", "Poster 2 In the exam: được ăn trong phòng.", "B", "No food or drinks."),
    ]

    prep_yoga = """**A poster at work** — từ vựng đọc thông báo / lời mời (British Council A1).

- **When / Where / How much** — hỏi thời gian, địa điểm, giá.
- **Yoga** — **mats**, **comfortable clothes**, **lunchtime class**.
- **Book / join** — đăng ký qua **email**; **maximum** — giới hạn chỗ."""
    q_yoga = [
        mc("Q_yg_01", None, "Lớp yoga diễn ra hôm nào?", {"A": "Monday", "B": "Tuesday", "C": "Friday", "D": "Every day"}, "B", "Every Tuesday."),
        mc("Q_yg_02", None, "Mấy giờ bắt đầu?", {"A": "12.30 p.m.", "B": "1.30 p.m.", "C": "3.30 p.m.", "D": "9.00 a.m."}, "B", "1.30 p.m."),
        mc("Q_yg_03", None, "Địa điểm?", {"A": "Room 7", "B": "Meeting Room 7", "C": "Room 70", "D": "Kitchen"}, "B", "Meeting Room 7."),
        mc("Q_yg_04", None, "Giá £10 bao gồm gì?", {"A": "Một buổi 30 phút", "B": "Four 30-minute classes", "C": "Cả năm", "D": "Chỉ thảm yoga"}, "B", "£10 for four 30-minute classes."),
        mc("Q_yg_05", None, "Email liên hệ để đăng ký?", {"A": "Divya@example.com", "B": "Sam.Holden@example.com", "C": "yoga@kitchen.com", "D": "info@broadstreet.com"}, "B", "Write to Sam…"),
        mc("Q_yg_06", None, "Giáo viên yoga tên gì?", {"A": "Sam Holden", "B": "Divya Bridge", "C": "Tony", "D": "Alex"}, "B", "teacher Divya Bridge."),
        tf("Q_yg_07", "Divya sẽ chuẩn bị yoga mats.", "A", "Divya will provide the yoga mats."),
        tf("Q_yg_08", "Học viên nên mang quần áo thoải mái.", "A", "Comfortable clothes."),
        tf("Q_yg_09", "Lớp học diễn ra vào thứ Hai mỗi tuần.", "B", "Tuesday."),
        mc("Q_yg_10", None, "Mỗi buổi học dài bao lâu?", {"A": "20 minutes", "B": "30 minutes", "C": "45 minutes", "D": "60 minutes"}, "B", "30-minute classes."),
        tf("Q_yg_11", "£10 là tiền một buổi duy nhất.", "B", "Four classes."),
        tf("Q_yg_12", "Phòng chỉ chứa tối đa 20 người.", "A", "Maximum of 20."),
        mc("Q_yg_13", None, "Tiêu đề chính của poster?", {"A": "Time to study!", "B": "Time to relax!", "C": "Office rules", "D": "Lunch menu"}, "B", "Heading."),
        tf("Q_yg_14", "Đây là lớp yoga buổi tối (evening).", "B", "Lunchtime."),
        mc("Q_yg_15", None, "Để tham gia cần làm gì?", {"A": "Call Sam", "B": "Write to Sam (email)", "C": "Pay at the door only", "D": "Nothing"}, "B", "How to join."),
        tf("Q_yg_16", "Poster khuyên đăng ký sớm vì chỗ có hạn.", "A", "so book now; maximum 20."),
        mc("Q_yg_17", None, "Ai cung cấp thảm (mats)?", {"A": "Sam", "B": "Participants always", "C": "Divya", "D": "Meeting Room 7"}, "C", "Divya will provide…"),
        tf("Q_yg_18", "Lớp miễn phí £0.", "B", "£10 for four classes."),
    ]

    lessons = [
        reading_lesson(
            "R_a1_study_timetable",
            "A study timetable",
            1,
            "course/reading/A study timetable _ LearnEnglish.html",
            {"gamedata_prep": "http://gamedata.britishcouncil.org/d/Matching_MjI5ODE=.xml", "gamedata_task1": "http://gamedata.britishcouncil.org/d/Matching_MjI5ODI=.xml", "gamedata_task2": "http://gamedata.britishcouncil.org/d/MultipleChoice_MjI5ODM=.xml"},
            prep_tt,
            PASS_TIMETABLE,
            q_tt,
        ),
        reading_lesson(
            "R_a1_restaurant_menu",
            "A restaurant menu",
            2,
            "course/reading/A restaurant menu _ LearnEnglish.html",
            {"gamedata_prep": "http://gamedata.britishcouncil.org/d/Matching_MjI5ODU=.xml", "gamedata_task1": "http://gamedata.britishcouncil.org/d/TrueOrFalse_MjI5ODY=.xml", "gamedata_task2": "http://gamedata.britishcouncil.org/d/MultipleChoice_MjI5ODc=.xml"},
            prep_menu,
            PASS_MENU,
            q_menu,
        ),
        reading_lesson(
            "R_a1_poster_exam",
            "A poster for exam candidates",
            3,
            "course/reading/A poster for exam candidates _ LearnEnglish.html",
            {"gamedata_prep": "http://gamedata.britishcouncil.org/d/Matching_MjI5ODk=.xml", "gamedata_task1": "http://gamedata.britishcouncil.org/d/TrueOrFalse_MjI5OTA=.xml", "gamedata_task2": "http://gamedata.britishcouncil.org/d/MultipleChoice_MjI5OTE=.xml"},
            prep_exam,
            PASS_EXAM,
            q_exam,
        ),
        reading_lesson(
            "R_a1_poster_work",
            "A poster at work",
            4,
            "course/reading/A poster at work _ LearnEnglish.html",
            {"gamedata_prep": "http://gamedata.britishcouncil.org/d/Matching_MjI5OTM=.xml", "gamedata_task1": "http://gamedata.britishcouncil.org/d/TrueOrFalse_MjI5OTQ=.xml", "gamedata_task2": "http://gamedata.britishcouncil.org/d/MultipleChoice_MjI5OTU=.xml"},
            prep_yoga,
            PASS_YOGA,
            q_yoga,
        ),
    ]

    payload = {
        "course_id": "reading_a1",
        "course_name": "Reading — A1",
        "course_description": "Bốn bài đọc A1 (British Council): Study timetable, Restaurant menu, Exam posters, Yoga poster. Tab **Tài liệu**: chuẩn bị dạng text; tab **Bài tập**: đoạn đọc (nút hiện/ẩn) và trắc nghiệm.",
        "course_level": "beginner",
        "course_skill": "reading",
        "course_cefr_level": "A1",
        "lessons": lessons,
    }

    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    nq = sum(len(x["quizzes"]) for x in lessons)
    print("Wrote", OUT, "lessons", len(lessons), "questions", nq)


if __name__ == "__main__":
    main()
