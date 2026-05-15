# -*- coding: utf-8 -*-
"""Tạo course_listening_a1.json: 4 bài A1; preparation (text tĩnh) → tab Tài liệu; transcript → field riêng (quiz). Chạy: python generate_listening_a1_fixture.py"""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).with_name("course_listening_a1.json")
BASE = "https://learnenglish.britishcouncil.org/sites/podcasts/files"

def mc(qid: str, task: str | None, text: str, opts: dict, ans: str, hint: str) -> dict:
    q: dict = {
        "quiz_id": qid,
        "difficulty_level": 2,
        "question_type": "multiple_choice",
        "question_text": f"{task}\n{text}" if task else text,
        "options": opts,
        "correct_answer": ans,
        "hint_text": hint,
    }
    return q


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


def lesson(
    lid: str,
    name: str,
    order: int,
    audio: str,
    html: str,
    gd: dict,
    prep_study_md: str,
    transcript_md: str,
    quizzes: list,
) -> dict:
    core = (prep_study_md or "").strip()
    foot = (
        "Bản ghi lời thoại đầy đủ (*transcript*) nằm trong tab **Bài tập** — dùng nút **Hiện transcript** dưới trình phát audio."
    )
    prep_body = "\n\n".join(p for p in (core, foot) if p)
    content: dict = {
        "preparation_pages": [{"title": "Chuẩn bị (Preparation)", "body": prep_body}],
        "transcript": (transcript_md or "").strip(),
    }
    return {
        "lesson_id": lid,
        "lesson_name": name,
        "order": order,
        "estimated_minutes": 30,
        "audio_url": f"{BASE}/{audio}",
        "metadata": {"skill": "listening", "source_html": html, **gd},
        "content": content,
        "quizzes": quizzes,
    }


def main() -> None:
    boss_transcript = """## Transcript

**Susanne**: Hi, Mario. Can you help me prepare some things for the next month?

**Mario**: OK, sure. What can I help you with?

**Susanne**: I need to visit the customer in Germany. It's important.

**Mario**: What can I do to help?

**Susanne**: Can you send an email to the customer? Ask them when I can visit them next week. Please do this first. It's a priority and very urgent.

**Mario**: Right. I'll do it today.

**Susanne**: Thanks. This next task is also important. Can you invite everyone to the next team meeting?

**Mario**: Yes, I will.

**Susanne**: But first you need to book a meeting room. After that, please send everyone an email about it.

**Mario**: Yes, of course.

**Susanne**: And finally, can you write a short report about our new project? I have to give a presentation to our managers next month. Please do it when you have time – sometime in the next two or three weeks. It's not too urgent.

**Mario**: Sure, no problem. I can do it this week.

**Susanne**: There's no hurry. Take your time.
"""
    boss_prep_study = """**A request from your boss** — từ vựng về mức độ **gấp / ưu tiên** (British Council A1).

Cùng một dạng ý có thể nói theo hai hướng: việc cần ưu tiên ngay, hoặc việc **không** cần vội.

- **Gấp / ưu tiên:** *This is a priority.* — *It's important.* — *Do this first.*
- **Không gấp / không vội:** *There's no hurry.* — *Take your time.* — *Do it when you have time.*"""

    # Load existing quiz Q_rb_* from current file or redefine
    with OUT.open(encoding="utf-8") as f:
        existing = json.load(f)
    boss_quizzes = existing["lessons"][0]["quizzes"]

    boss = lesson(
        "L_a1_request_from_your_boss",
        "A request from your boss",
        1,
        "LE_listening_A1_A_request_from_your_boss.mp3",
        "course/listening/A request from your boss _ LearnEnglish.html",
        {
            "gamedata_task1": "http://gamedata.britishcouncil.org/d/Matching_MjI4NDU=.xml",
            "gamedata_task2": "http://gamedata.britishcouncil.org/d/ReorderingVertical_MjI4NDY=.xml",
        },
        boss_prep_study,
        boss_transcript,
        boss_quizzes,
    )

    # --- Voicemail ---
    vm_transcript = """## Transcript

**John**: Hi, this is John. Thanks for calling. I'm not here at the moment, so please leave a message and I'll call you back.

**Marina**: Hi, John, this is Marina Silva calling from Old Time Toys. Your colleague Alex gave me your phone number. She said you can help me.

I need some information on your new products. Could you please call me when you are back in the office? My phone number is 0-2-0-8, 6-5-5-7-6-2-1.

Also, can you please email me your new brochure and information about your prices? My email address is Marina, that's M-A-R-I-N-A, dot Silva, S-I-L-V-A, at O-L-D-T-I-M-E hyphen toys dot com.

Thanks a lot. I look forward to hearing from you.
"""
    vm_prep_study = """**A voicemail message** — từ vựng trong phần chuẩn bị (British Council A1).

- **colleague** — người cùng làm việc với mình (*someone you work with*).
- **brochure** — cuốn sách nhỏ / tập tài liệu có thông tin về sản phẩm (*a small book with information about a product*).
- **products** — những thứ một công ty làm ra và bán (*things a company makes and sells*).
- **office** — văn phòng.
- **price / prices** — giá.

**Cụm thường gặp trong tin nhắn thoại:** *leave a message* — *call you back* — *Could you please call me when you are back in the office?* — *I look forward to hearing from you.*"""

    vm_quizzes = [
        mc(
            "Q_vm_01", "Task 1",
            "Theo bài *Preparation* (matching từ vựng), *colleague* có nghĩa gần nhất là?",
            {"A": "Một cuốn sách nhỏ có thông tin sản phẩm (brochure)", "B": "Người cùng làm việc với mình", "C": "Giá (price)", "D": "Văn phòng (office)"},
            "B",
            "Gamedata: 'someone you work with — a colleague'.",
        ),
        mc(
            "Q_vm_02", "Task 1",
            "*Brochure* trong bài có nghĩa là gì?",
            {"A": "Giá cả", "B": "Sản phẩm", "C": "Ấn phẩm/tập tài liệu giới thiệu sản phẩm", "D": "Đồng nghiệp"},
            "C",
            "‘a small book with information about a product’.",
        ),
        mc(
            "Q_vm_03", None,
            "Marina làm việc cho công ty nào?",
            {"A": "Old Time Toys", "B": "New Time Toys", "C": "Alex Toys", "D": "British Council"},
            "A",
            "‘calling from Old Time Toys’.",
        ),
        mc(
            "Q_vm_04", None,
            "Ai đã cho Marina số điện thoại của John?",
            {"A": "John", "B": "Alex", "C": "Marina", "D": "Boss"},
            "B",
            "‘Your colleague Alex gave me your phone number’.",
        ),
        mc(
            "Q_vm_05", None,
            "Marina muốn John làm gì khi trở lại văn phòng?",
            {"A": "Gửi fax ngay", "B": "Gọi lại cho cô ấy", "C": "Đến cửa hàng", "D": "Xóa tin nhắn"},
            "B",
            "‘Could you please call me when you are back in the office?’",
        ),
        mc(
            "Q_vm_06", None,
            "Số điện thoại Marina để lại là gì (viết liền như trong bài nghe)?",
            {"A": "0208 6656721", "B": "0208 6557621", "C": "0208 6576621", "D": "0802 6557621"},
            "B",
            "0-2-0-8, 6-5-5-7-6-2-1.",
        ),
        mc(
            "Q_vm_07", None,
            "Địa chỉ email của Marina (đúng theo transcript) gần nhất với:",
            {"A": "marina.silva@oldtime_toys.com", "B": "marina.silva@oldtime-toys.com", "C": "marina@oldtoys.com", "D": "silva.marina@oldtime.com"},
            "B",
            "OLDTIME hyphen toys dot com → oldtime-toys; dấu chấm giữa marina và silva.",
        ),
        tf(
            "Q_vm_08",
            "Theo nội dung audio, John làm việc tại Old Time Toys.",
            "B",
            "Marina gọi từ Old Time Toys; John chỉ nhắn hộp thư thoại cá nhân.",
        ),
        tf(
            "Q_vm_09",
            "Marina muốn thông tin về sản phẩm mới, brochure và giá.",
            "A",
            "Cô nói rõ ‘information on your new products’, brochure và prices.",
        ),
        mc(
            "Q_vm_10", "Task 2",
            "Trong đúng trình tự lời nhắn, việc *đầu tiên* Marina làm là gì?",
            {"A": "Đọc địa chỉ email", "B": "Giới thiệu bản thân", "C": "Nêu số điện thoại", "D": "Cảm ơn John"},
            "B",
            "Gamedata Task 2: ‘Marina introduces herself’ đứng đầu.",
        ),
        mc(
            "Q_vm_11", "Task 2",
            "Ngay sau khi giới thiệu, Marina nói về điều gì?",
            {"A": "Brochure và giá", "B": "Cô ấy biết số John như thế nào", "C": "Số điện thoại", "D": "Giờ làm việc"},
            "B",
            "‘how she got John's phone number’ (Alex).",
        ),
        mc(
            "Q_vm_12", "Task 2",
            "Trước khi xin brochure và giá, Marina đã nói rõ nhu cầu nào?",
            {"A": "Muốn mời John đi cà phê", "B": "Cần thông tin về sản phẩm mới và nhờ gọi lại", "C": "Muốn đổi tên công ty", "D": "Hỏi John có ở văn phòng không"},
            "B",
            "Nêu nhu cầu → nhờ gọi lại; sau đó mới email/brochure.",
        ),
        mc(
            "Q_vm_13", None,
            "John nói gì về tình trạng hiện tại của anh ấy?",
            {"A": "Anh ấy đang họp", "B": "Anh ấy không có ở đây lúc này", "C": "Anh ấy nghỉ phép dài", "D": "Anh ấy từ chối mọi cuộc gọi"},
            "B",
            "‘I'm not here at the moment’.",
        ),
        mc(
            "Q_vm_14", None,
            "Marina đánh chữ cái họ mình thế nào?",
            {"A": "S-I-L-V-A", "B": "S-I-L-V-A-H", "C": "S-Y-L-V-A", "D": "S-I-L-B-A"},
            "A",
            "‘S-I-L-V-A’.",
        ),
        tf(
            "Q_vm_15",
            "Alex được nói là người sẽ trực tiếp cung cấp thông tin sản phẩm cho Marina.",
            "B",
            "Alex cho số John; ‘She said you can help me’ nói về John.",
        ),
        mc(
            "Q_vm_16", "Task 1",
            "Từ *products* trong phần chuẩn bị có nghĩa gần nhất với:",
            {"A": "Giá", "B": "Tài liệu quảng cáo", "C": "Hàng hóa / sản phẩm công ty làm ra và bán", "D": "Đồng nghiệp"},
            "C",
            "Gamedata: ‘things a company makes and sells’.",
        ),
        tf(
            "Q_vm_17",
            "Marina lần đầu gọi cho John để bán hàng trực tiếp trong cuộc gọi.",
            "B",
            "Cô để lại voicemail và nhờ gọi lại / gửi email.",
        ),
        mc(
            "Q_vm_18", None,
            "Marina kết thúc lời nhắn bằng thái độ nào?",
            {"A": "Tức giận", "B": "Hối hận", "C": "Lịch sự, mong nhận phản hồi", "D": "Yêu cầu gặp mặt ngay"},
            "C",
            "‘Thanks a lot. I look forward to hearing from you.’",
        ),
        tf(
            "Q_vm_19",
            "Trong transcript, email dùng dấu *gạch ngang* (hyphen) trong phần ‘oldtime-toys’.",
            "A",
            "‘O-L-D-T-I-M-E hyphen toys’.",
        ),
        mc(
            "Q_vm_20", None,
            "Marina nhắc tới *brochure* vì cô muốn nhận thêm thông tin dạng nào từ John?",
            {"A": "Hóa đơn thanh toán", "B": "Tài liệu giới thiệu sản phẩm", "C": "Hợp đồng luật sư", "D": "Lịch nghỉ phép"},
            "B",
            "‘email me your new brochure’.",
        ),
    ]

    vm = lesson(
        "L_a1_voicemail_message",
        "A voicemail message",
        2,
        "LE_listening_A1_A_voicemail_message.mp3",
        "course/listening/A voicemail message _ LearnEnglish.html",
        {
            "gamedata_prep": "http://gamedata.britishcouncil.org/d/Matching_MjI4MDk=.xml",
            "gamedata_task1": "http://gamedata.britishcouncil.org/d/MultipleChoice_MjI4MTA=.xml",
            "gamedata_task2": "http://gamedata.britishcouncil.org/d/ReorderingVertical_MjI4MTE=.xml",
        },
        vm_prep_study,
        vm_transcript,
        vm_quizzes,
    )

    # --- Booking ---
    book_transcript = """## Transcript

**Staff**: Hello, Gino's.

**Jamie**: Hi. Can I book a table for tomorrow night, please?

**Staff**: How many people is it for?

**Jamie**: Four.

**Staff**: And what time would you like?

**Jamie**: About eight, eight thirty maybe?

**Staff**: Let's see ... We're pretty busy tomorrow, so I can do half past seven or nine.

**Jamie**: Oh. OK, then. Half seven, please.

**Staff**: What name is it?

**Jamie**: Jamie.

**Staff**: J-A- ...?

**Jamie**: M-I-E

**Staff**: OK, so that's a table for four at half past seven tomorrow evening.

**Jamie**: Great. Thanks! Bye.

**Staff**: Bye.

---

**Staff**: Hello, Gino's.

**Jamie**: Hi, I called earlier to book a table for four and I was wondering if I can make it for six instead?

**Staff**: Ah, what name was it?

**Jamie**: It's Jamie.

**Staff**: Table for four at half past seven. So you want to change it to 6 o'clock?

**Jamie**: No, sorry. Can I make it for six people?

**Staff**: Oh, I see. Sorry! That shouldn't be a problem. I can move you to a bigger table but it will be nearer the kitchen. Is that OK?

**Jamie**: No problem. Is it possible to change the time as well? Make it a little bit later?

**Staff**: Ah ... yeah, we can. Is eight OK for you?

**Jamie**: Perfect, thanks!

**Staff**: Lovely. See you tomorrow, then.

**Jamie**: Thanks! Bye!

**Staff**: Thanks. Ciao!
"""
    book_prep_study = """**Booking a table** — cụm giao tiếp đặt bàn nhà hàng (British Council A1). Bài có **hai lượt** gọi điện (đặt lần đầu rồi gọi lại để đổi số người / giờ).

- **Bắt đầu / yêu cầu:** *Can I book a table for tomorrow night, please?* — *I called earlier to book a table for four…* — *Can I make it for six instead?* — *Can I make it for six people?* — *Is it possible to change the time as well?*
- **Nhân viên hỏi thông tin:** *How many people is it for?* — *And what time would you like?* — *What name is it?* — *What name was it?*
- **Thời gian & xếp chỗ:** *tomorrow night* — *about eight, eight thirty maybe* — *half past seven* / *half seven* — *nine* — *eight o'clock* — *six o'clock* — *We're pretty busy…* — *a bigger table* — *nearer the kitchen* — *See you tomorrow.*"""

    book_quizzes = [
        mc("Q_bt_01", None, "Nhà hàng tên gì?", {"A": "Jamie's", "B": "Gino's", "C": "Mario's", "D": "Kitchen's"}, "B", "‘Hello, Gino's.’"),
        mc(
            "Q_bt_02", None,
            "Lần đầu Jamie muốn đặt bàn cho *tối nào*?",
            {"A": "Tối nay", "B": "Sáng mai", "C": "Tối mai", "D": "Trưa ngày kia"},
            "C",
            "‘tomorrow night’ (khớp gamedata MC).",
        ),
        mc(
            "Q_bt_03", None,
            "Jamie muốn bàn mấy người trong lần đặt đầu tiên?",
            {"A": "3 người", "B": "4 người", "C": "5 người", "D": "6 người"},
            "B",
            "Jamie: ‘Four.’",
        ),
        mc(
            "Q_bt_04", None,
            "Khi Jamie nói ‘about eight, eight thirty maybe’, ý là khoảng thời gian nào?",
            {"A": "Đúng 8 giờ", "B": "Đúng 8 giờ 30", "C": "Khoảng giữa 8 giờ và 8 giờ 30", "D": "9 giờ tối"},
            "C",
            "British Council gapfill / MC.",
        ),
        mc(
            "Q_bt_05", None,
            "Vì nhà hàng bận, thời gian nhân viên đề xuất cho lần đặt *đầu* là gì?",
            {"A": "7:30 hoặc 9:00", "B": "6:00 hoặc 8:00", "C": "Chỉ 8:30", "D": "Chỉ 9:30"},
            "A",
            "half past seven or nine.",
        ),
        mc(
            "Q_bt_06", None,
            "Jamie chọn mấy giờ cho lần đặt đầu tiên?",
            {"A": "half past seven (7:30)", "B": "9:00", "C": "8:00", "D": "6:00"},
            "A",
            "‘Half seven, please.’",
        ),
        mc(
            "Q_bt_07", None,
            "Họ đánh vần tên Jamie phần cuối như thế nào?",
            {"A": "J-A-M-I-E", "B": "M-I-E", "C": "J-M-E", "D": "J-A-Y"},
            "B",
            "Sau J-A-… Jamie nói M-I-E.",
        ),
        mc(
            "Q_bt_08", None,
            "Trong cuộc gọi thứ hai, Jamie thực sự muốn thay đổi điều gì?",
            {"A": "Đổi từ 4 người sang 6 người", "B": "Đổi từ 7:30 sang 6 giờ", "C": "Hủy đặt bàn", "D": "Đổi tên nhà hàng"},
            "A",
            "‘six people’ không phải 6 giờ.",
        ),
        mc(
            "Q_bt_09", None,
            "Bàn lớn hơn sẽ ở đâu?",
            {"A": "Gần cửa ra vào", "B": "Gần bếp hơn", "C": "Trong góc yên tĩnh", "D": "Ngoài hiên"},
            "B",
            "nearer the kitchen.",
        ),
        mc(
            "Q_bt_10", None,
            "Giờ ăn mới cuối cùng Jamie đồng ý là mấy giờ?",
            {"A": "6:00", "B": "7:30", "C": "8:00", "D": "9:00"},
            "C",
            "‘Is eight OK for you?’ — Perfect.",
        ),
        mc(
            "Q_bt_11", "Task 1",
            "Theo *MultipleChoice* gốc: lần đặt *đầu tiên* được xác nhận lúc mấy giờ?",
            {"A": "7.30", "B": "8.30", "C": "9.00", "D": "6.00"},
            "A",
            "half past seven = 7.30.",
        ),
        mc(
            "Q_bt_12", "Task 1",
            "Chữ khi đánh vần tên (đúng theo bài) là:",
            {"A": "Jamei", "B": "Jamie", "C": "Janie", "D": "Jimmy"},
            "B",
            "Gamedata MultipleChoice.",
        ),
        mc(
            "Q_bt_13", "Task 2",
            "Bước *đầu tiên* trong trình tự lịch sự đặt bàn (Task 2) thường là:",
            {"A": "Hỏi có thể đổi giờ không", "B": "Hỏi đặt bàn cho tối mai", "C": "Hỏi bàn cho mấy người", "D": "Xác nhận 8 giờ"},
            "B",
            "‘Can I book a table for tomorrow night?’ đứng đầu gamedata.",
        ),
        tf(
            "Q_bt_14",
            "Nhân viên hiểu nhầm Jamie muốn đổi giờ sang 6 giờ (thay vì 6 người).",
            "A",
            "‘So you want to change it to 6 o'clock?’ — Jamie nói không.",
        ),
        tf(
            "Q_bt_15",
            "Jamie chấp nhận ngồi bàn gần bếp.",
            "A",
            "‘No problem.’",
        ),
        mc(
            "Q_bt_16", "Task 1 (grouping / thời gian)",
            "7.30 trong tiếng Anh Anh thường đọc là:",
            {"A": "Eight thirty", "B": "Half past seven / seven thirty", "C": "Nine o'clock", "D": "Half eight only (không có seven)"},
            "B",
            "Gamedata Grouping: Seven thirty; Half past eight; …",
        ),
        tf(
            "Q_bt_17",
            "Trong lần đầu, nhà hàng có thể cho bàn lúc 8:30.",
            "B",
            "Chỉ 7:30 hoặc 9:00 vì busy.",
        ),
        mc(
            "Q_bt_18", None,
            "Jamie gọi lại nhà hàng vì:",
            {"A": "Muốn hủy", "B": "Muốn tăng số người và có thể đổi giờ", "C": "Than phiền món ăn", "D": "Xin việc"},
            "B",
            "four → six people; later time.",
        ),
        tf(
            "Q_bt_19",
            "Staff nói họ có thể sắp bàn lớn hơn cho nhóm 6 người.",
            "A",
            "‘move you to a bigger table’.",
        ),
        mc(
            "Q_bt_20", None,
            "Lần đặt cuối: số khách và giờ (gần nhất) là?",
            {"A": "4 người, 7:30", "B": "6 người, 8:00", "C": "6 người, 7:30", "D": "4 người, 9:00"},
            "B",
            "six people; eight o'clock.",
        ),
    ]

    book = lesson(
        "L_a1_booking_table",
        "Booking a table",
        3,
        "LE_listening_A1_Booking_a_table.mp3",
        "course/listening/Booking a table _ LearnEnglish.html",
        {
            "gamedata_prep": "http://gamedata.britishcouncil.org/d/Grouping_MjI4NTA=.xml",
            "gamedata_task1": "http://gamedata.britishcouncil.org/d/MultipleChoice_MjI4NTE=.xml",
            "gamedata_task2": "http://gamedata.britishcouncil.org/d/ReorderingVertical_MjI4NTI=.xml",
        },
        book_prep_study,
        book_transcript,
        book_quizzes,
    )

    # --- Business cards ---
    card_transcript = """## Transcript (A–D)

### A

**A**: Hello, Doctor Miller. It's nice to meet you.

**B**: Please call me Peter.

**A**: OK. Are you a medical doctor? It must be helpful when you sell medical equipment.

**B**: Actually, no. My doctorate was in electronic engineering, but it's still helpful for me when I sell our equipment.

### B

Good morning, everyone. I'm happy to be here today to tell you about our new project. My name is Alessandro Rossi. I'm the project leader on the Starlight programming project.

### C

Pleased to meet you. Here's my card. My real name is Megumi Tanaka, but people who are not from my country think it's difficult to say my name, so I use another name, Meg, when I'm working internationally.

### D

Hello, everyone. My name's Andres Mulligan. I'm very happy to be joining this team for the next few months and learning more about research and development.

## Danh thiếp (đọc thêm)

1. **Dr Peter Miller** — DX Medical Equipment Ltd — Sales Director  
2. **Alessandro Rossi** — *Space10 Designs* — Lead Programmer  
3. **Megumi Tanaka** — Global Engineering Consults — Product Manager  
4. **Andres Mulligan Jr** — MaXtin Ltd — Intern, R&D team
"""
    card_prep_study = """**Business cards** — từ vựng giới thiệu và danh thiếp (British Council A1).

- **Chào & trao đổi lần đầu:** *It's nice to meet you.* — *Pleased to meet you.* — *Here's my card.*
- **Cách xưng hô:** *Please call me Peter.*
- **Trình độ / lĩnh vực:** *medical doctor* — *doctorate* — *electronic engineering* — *medical equipment* — *sell our equipment*
- **Chức danh & công việc:** *project leader* — *lead programmer* — *product manager* — *sales director* — *intern* — *R&D team* — *research and development*
- **Giới thiệu ngắn:** *I'm happy to be here today to tell you about our new project.* — *I'm the project leader on the … project.* — *My real name is … but … I use another name, Meg, when I'm working internationally.* — *I'm very happy to be joining this team for the next few months.*

Chi tiết lời thoại đầy đủ và mẫu *Danh thiếp* xem trong **transcript** (tab **Bài tập**)."""

    bc_quizzes = [
        tf("Q_bc_01", "Peter Miller không phải là bác sĩ y khoa (medical doctor).", "A", "‘Actually, no.’"),
        tf("Q_bc_02", "Peter bán thiết bị dùng trong bệnh viện / cho bác sĩ (medical equipment).", "A", "Cuộc đối thoại A."),
        tf("Q_bc_03", "Starlight là tên công ty của Alessandro.", "B", "Starlight là *programming project*."),
        tf("Q_bc_04", "Alessandro là *manager* of the company.", "B", "Anh là *project leader*."),
        tf("Q_bc_05", "Megumi *nghĩ* tên thật của cô *khó đọc* (theo nguyên văn: she thinks...).", "B", "Người *ngoài nước* thấy khó phát âm."),
        tf("Q_bc_06", "Andres không phải thành viên vĩnh viễn lâu dài trong team (intern, vài tháng).", "A", "‘joining … for the next few months’."),
        mc("Q_bc_07", None, "Peter muốn người khác gọi mình là gì?", {"A": "Doctor Miller", "B": "Peter", "C": "Engineer Peter", "D": "Mr Equipment"}, "B", "‘Please call me Peter.’"),
        mc("Q_bc_08", None, "Bằng tiến sĩ (doctorate) của Peter về lĩnh vực nào?", {"A": "Medicine", "B": "Electronic engineering", "C": "Sales only", "D": "Cooking"}, "B", "Transcript đoạn A."),
        mc("Q_bc_09", None, "Công ty trên danh thiếp của Peter là:", {"A": "Starlight Designs", "B": "DX Medical Equipment Ltd", "C": "MaXtin Ltd", "D": "Old Time Toys"}, "B", "Reading text."),
        mc("Q_bc_10", None, "Alessandro Rossi làm việc cho công ty nào (trên thẻ)?", {"A": "Global Engineering", "B": "Space10 Designs", "C": "DX Medical", "D": "MaXtin"}, "B", "Card 2."),
        mc("Q_bc_11", None, "Chức danh của Megumi Tanaka trên thẻ:", {"A": "Intern", "B": "Product Manager", "C": "Sales Director", "D": "Project leader"}, "B", "Card 3."),
        mc("Q_bc_12", None, "Khi làm việc quốc tế, Megumi thường dùng tên gọi nào?", {"A": "Tanaka", "B": "Meg", "C": "Marina", "D": "Alex"}, "B", "‘I use another name, Meg’."),
        mc("Q_bc_13", "Task 2", "Ghép câu: *I'm the project leader.* — ai nói?", {"A": "Peter Miller", "B": "Alessandro Rossi", "C": "Megumi Tanaka", "D": "Andres Mulligan"}, "B", "Gamedata matching."),
        mc("Q_bc_14", "Task 2", "*I use another name when I'm* working internationally.* — ai?", {"A": "Peter", "B": "Alessandro", "C": "Megumi Tanaka", "D": "Jamie"}, "C", "Gamedata."),
        mc("Q_bc_15", "Task 2", "*I'm happy to be joining this team for the next few months.* — ai?", {"A": "Peter", "B": "Alessandro", "C": "Megumi", "D": "Andres Mulligan Jr"}, "D", "Gamedata."),
        mc("Q_bc_16", None, "Andres Mulligan Jr trên danh thiếp có chức danh gì?", {"A": "Sales Director", "B": "Intern, R&D team", "C": "Project leader", "D": "Lead Programmer"}, "B", "Card 4."),
        mc("Q_bc_17", None, "Công ty của Andres là:", {"A": "Space10 Designs", "B": "MaXtin Ltd", "C": "DX Medical", "D": "Gino's"}, "B", "Card 4."),
        tf("Q_bc_18", "Peter nói bằng tiến sĩ về điện tử vẫn giúp ích khi bán thiết bị.", "A", "‘still helpful when I sell our equipment’."),
        mc("Q_bc_19", None, "Trong đoạn B, Alessandro giới thiệu điều gì?", {"A": "Dự án lập trình mới", "B": "Menu nhà hàng", "C": "Luật giao thông", "D": "Cách đặt bàn"}, "A", "‘new project … Starlight programming project’."),
        mc("Q_bc_20", None, "Mục đích Andres tham gia team là gì (theo audio)?", {"A": "Bán medical equipment", "B": "Học hỏi thêm về R&D", "C": "Làm hộp thư thoại", "D": "Đặt bàn ăn"}, "B", "‘learning more about research and development’."),
    ]

    bc = lesson(
        "L_a1_business_cards",
        "Business cards",
        4,
        "LE_listening_A1_Business_cards.mp3",
        "course/listening/Business cards _ LearnEnglish.html",
        {
            "gamedata_prep": "http://gamedata.britishcouncil.org/d/Matching_MjI4MzY=.xml",
            "gamedata_task1": "http://gamedata.britishcouncil.org/d/TrueOrFalse_MjI4Mzg=.xml",
            "gamedata_task2": "http://gamedata.britishcouncil.org/d/Matching_MjI4Mzc=.xml",
        },
        card_prep_study,
        card_transcript,
        bc_quizzes,
    )

    payload = {
        "course_id": "listening_a1",
        "course_name": "Listening — A1",
        "course_description": "Bốn bài A1 (British Council): Request from your boss, Voicemail, Booking a table, Business cards. Tab **Tài liệu**: từ vựng/cụm chuẩn bị dạng text; tab **Bài tập**: audio, quiz (~20 câu/bài) và transcript (nút hiện/ẩn).",
        "course_level": "beginner",
        "course_skill": "listening",
        "course_cefr_level": "A1",
        "lessons": [boss, vm, book, bc],
    }

    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote", OUT, "lessons", len(payload["lessons"]), "questions", sum(len(x["quizzes"]) for x in payload["lessons"]))


if __name__ == "__main__":
    main()
