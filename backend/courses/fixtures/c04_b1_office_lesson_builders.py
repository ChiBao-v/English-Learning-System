"""Khóa C04 — Practical Office Communication (B1): 10 bài × 3 trang × 10 quiz."""

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
    meta = {"skill": "vocabulary", "topic": "small_talk", "time_est_minutes": 20, "difficulty": 0.4}
    p1 = """### Formal vs informal greetings

**Formal** (sếp, khách, đối tác lần đầu):

- *Good morning / Good afternoon.*  
- *How do you do?* (rất trang trọng, lần đầu gặp)  
- *It's a pleasure to meet you.*

**Informal** (đồng nghiệp thân):

- *Morning!* / *How's it going?* / *What's up?*

> Trong môi trường chuyên nghiệp, chào **quá thân mật** với lãnh đạo/đối tác có thể được đánh giá là **không phù hợp** (fail ngữ cảnh)."""

    p2 = """### Safe small talk (văn phòng)

- **Thời tiết:** *Terrible weather today, isn't it?*  
- **Cuối tuần:** *How was your weekend?* / *Did you do anything fun?*  
- **Công việc (nhẹ):** *Are you busy today?* / *How is the new project going?*

Tránh: lương, chính trị, chủ đề nhạy cảm cá nhân (trừ khi đã rất thân)."""

    p3 = """### Ending a chat politely

Không **im lặng bỏ đi**. Dùng:

- *Well, I should get back to work.*  
- *It was great talking to you, but I have a meeting in 5 minutes.*

### Thực hành

Viết **2 lời thoại ngắn**: một formal (chào đối tác), một informal (chào bạn cùng phòng)."""

    reading = (
        "Good morning, Mr. Lee. It's a pleasure to meet you. — Good morning. Terrible weather today, isn't it? "
        "Well, I should get back to work. Nice talking to you."
    )
    return {
        "lesson_id": "L04_01",
        "lesson_name": "Office Small Talk & Greetings (Vocabulary)",
        "order": 1,
        "estimated_minutes": 32,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Formal vs informal", "body": p1},
                {"title": "Trang 2 — Safe small talk", "body": p2},
                {"title": "Trang 3 — Kết thúc hội thoại", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "How do you do? / pleasure to meet you", "vi": "chào trang trọng lần đầu"},
                {"word": "get back to work", "vi": "quay lại làm việc"},
            ],
            "examples": [
                {"english": "How was your weekend?", "vietnamese": "Cuối tuần của bạn thế nào?"},
            ],
        },
        "quizzes": [
            Q("Q_L04_01_01", 2, "multiple_choice", "Câu nào phù hợp nhất để chào đối tác lần đầu gặp mặt?", {"A": "What's up?", "B": "It's a pleasure to meet you.", "C": "How's it going?", "D": "See ya."}, "B", "Formal + first meeting.", 11),
            Q("Q_L04_01_02", 2, "multiple_choice", "Chủ đề small talk tương đối an toàn ở văn phòng:", {"A": "The weather", "B": "Salary", "C": "Politics", "D": "Gossip about colleagues"}, "A", "Weather is a classic safe topic.", 10),
            Q("Q_L04_01_03", 2, "fill_in_blank", "Well, I should get back to _____.", {"A": "work", "B": "weekend", "C": "politics", "D": "salary"}, "A", "Get back to work.", 9),
            Q("Q_L04_01_04", 2, "error_identification", "Sửa: “How was your weekends?”", {"A": "How", "B": "was", "C": "weekends", "D": "your"}, "C", "Your weekend (singular).", 11, True),
            Q("Q_L04_01_05", 3, "multiple_choice", "Ghép: 1. Formal — 2. Informal", {"A": "1→Good morning, sir. — 2→Morning!", "B": "1→Morning! — 2→Good morning, sir.", "C": "1→What's up? — 2→How do you do?", "D": "1→Salary — 2→Weather"}, "A", "Formal vs informal pairing.", 13),
            Q("Q_L04_01_06", 2, "multiple_choice", "Cách kết thúc cuộc trò chuyện lịch sự:", {"A": "I want to go.", "B": "I have a meeting in 5 minutes.", "C": "Stop talking.", "D": "Bye. (only)"}, "B", "Polite + reason.", 10),
            Q("Q_L04_01_07", 1, "true_false", "You should greet your boss with “What's up?” in most offices.", {"A": "True", "B": "False"}, "B", "Too informal for many contexts.", 9),
            Q("Q_L04_01_08", 2, "multiple_choice", "“Cuối tuần của bạn thế nào?”", {"A": "How was your weekend?", "B": "How is your weekend?", "C": "What was weekend?", "D": "How your weekend was?"}, "A", "How was your weekend?", 10),
            Q("Q_L04_01_09", 2, "multiple_choice", "If someone asks “How's it going?”, a natural reply is:", {"A": "I am going to work.", "B": "Great, thanks. And you?", "C": "It is going.", "D": "By train."}, "B", "Short positive + return question.", 11),
            Q("Q_L04_01_10", 2, "fill_in_blank", "Terrible weather today, _____ it?", {"A": "isn't", "B": "doesn't", "C": "wasn't", "D": "aren't"}, "A", "Question tag with *is*.", 10),
        ],
    }


def _lesson_02():
    meta = {"skill": "writing", "topic": "email_basics", "time_est_minutes": 30, "difficulty": 0.5}
    p1 = """### Openings & closings

**Mở:** *Dear Mr. Smith,* (formal) / *Hi Team,* (nội bộ).

**Đóng:** *Sincerely,* (rất formal) / *Best regards,* / *Kind regards,* (rất phổ biến).

Luôn **viết hoa** chữ cái đầu: *Dear*, *Best regards* — không viết *hi boss*."""

    p2 = """### Stating the purpose

Đi **thẳng vào việc** — không vòng vo.

**I am writing to + verb…**

- *I am writing to inform you about the meeting.*"""

    p3 = """### Attachments & calls to action

- *Please find attached the report.* / *I have attached the document.*  
- *Please let me know if you have any questions.*  
- *I look forward to hearing from you.*"""

    reading = (
        "Dear Sales team,\n\nI am writing to inform you about the new schedule. "
        "Please find attached the report.\n\nPlease let me know if you have any questions.\n\nBest regards,\nAnna"
    )
    return {
        "lesson_id": "L04_02",
        "lesson_name": "Writing Professional Emails (Writing/Vocab)",
        "order": 2,
        "estimated_minutes": 40,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Openings & closings", "body": p1},
                {"title": "Trang 2 — Purpose", "body": p2},
                {"title": "Trang 3 — Attachments & CTA", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "Best regards / Kind regards", "vi": "kết thư trang trọng thân mật vừa phải"},
                {"word": "Please find attached", "vi": "xin xem file đính kèm"},
            ],
            "examples": [
                {"english": "I look forward to hearing from you.", "vietnamese": "Tôi mong nhận được phản hồi từ bạn."},
            ],
        },
        "quizzes": [
            Q("Q_L04_02_01", 2, "multiple_choice", "Cách kết email phổ biến và an toàn trong kinh doanh:", {"A": "Love,", "B": "Bye,", "C": "Best regards,", "D": "Cheers mate,"}, "C", "Best regards / Kind regards.", 10),
            Q("Q_L04_02_02", 2, "fill_in_blank", "I am _____ to inform you about the new schedule.", {"A": "writing", "B": "write", "C": "written", "D": "wrote"}, "A", "I am writing to…", 9),
            Q("Q_L04_02_03", 2, "error_identification", "Sửa: “Please find attach the file.”", {"A": "Please", "B": "find", "C": "attach", "D": "file"}, "C", "Attached (adjective/participle).", 11, True),
            Q("Q_L04_02_04", 2, "multiple_choice", "Khi đính kèm báo cáo, cách viết tốt nhất:", {"A": "Please find attached the report.", "B": "The report is in the email body only wrong", "C": "Attached I am report", "D": "Report attached please find maybe"}, "A", "Please find attached…", 11),
            Q("Q_L04_02_05", 3, "multiple_choice", "Ghép: 1. Opening — 2. Closing", {"A": "1→Dear Mr. John, — 2→Sincerely,", "B": "1→Sincerely, — 2→Dear Mr. John,", "C": "1→Bye — 2→Hi", "D": "1→Love — 2→Boss"}, "A", "Dear… at start; Sincerely at end.", 12),
            Q("Q_L04_02_06", 1, "true_false", "You should write “HI BOSS” at the start of a professional email.", {"A": "True", "B": "False"}, "B", "Use Dear… / Hi + name (proper case).", 8),
            Q("Q_L04_02_07", 2, "multiple_choice", "“Tôi mong nhận được phản hồi từ bạn.”", {"A": "I look forward to hearing from you.", "B": "I look forward to hear you.", "C": "I forward look to hearing you.", "D": "I am forward to hear you."}, "A", "to + V-ing after look forward to.", 11),
            Q("Q_L04_02_08", 2, "multiple_choice", "After sending a complex document, a polite follow-up line is:", {"A": "Please let me know if you have any questions.", "B": "Don't ask me questions.", "C": "No questions allowed.", "D": "I hate questions."}, "A", "Professional CTA.", 11),
            Q("Q_L04_02_09", 2, "fill_in_blank", "Dear _____ team, (Kính gửi nhóm Bán hàng)", {"A": "Sales", "B": "sales", "C": "sale's", "D": "Sells"}, "A", "Dear Sales team,", 9),
            Q("Q_L04_02_10", 2, "multiple_choice", "Viết hoa đúng chuẩn:", {"A": "Best Regards,", "B": "Best regards,", "C": "best regards,", "D": "BEST REGARDS,"}, "B", "Best regards, (only B capitalized in closing line).", 10),
        ],
    }


def _lesson_03():
    meta = {"skill": "vocabulary", "topic": "telephone", "time_est_minutes": 25, "difficulty": 0.5}
    p1 = """### Answering & asking for someone

**Người nhận:** *Hello, [Company name], [Your name] speaking. How can I help you?*

**Người gọi:** *Hi, this is [name] from [company]. Could I speak to Mr. Davis, please?*"""

    p2 = """### When someone is unavailable

- *I'm afraid he is in a meeting.*  
- *She is not at her desk right now.*

**Đề xuất:** *Can I take a message?* / *Would you like to leave a message?*"""

    p3 = """### Leaving a message

- *Yes, please tell him that Anna called.*  
- *Could you ask him to call me back at [number]?*"""

    reading = (
        "Hello, Bright Tech, Linh speaking. How can I help you? — Hi, this is Tom from Delta Ltd. "
        "Could I speak to Ms. Park, please? — I'm afraid she is in a meeting. Can I take a message?"
    )
    return {
        "lesson_id": "L04_03",
        "lesson_name": "Phone Calls & Taking Messages (Listening/Vocab)",
        "order": 3,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Answering & asking", "body": p1},
                {"title": "Trang 2 — Unavailable", "body": p2},
                {"title": "Trang 3 — Messages", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "speaking (on the phone)", "vi": "đang nghe máy (đầu dây bên này là…)"},
                {"word": "take a message", "vi": "nhận lời nhắn"},
            ],
            "examples": [
                {"english": "Can I take a message?", "vietnamese": "Tôi có thể nhận lời nhắn không?"},
            ],
        },
        "quizzes": [
            Q("Q_L04_03_01", 2, "multiple_choice", "Bốc máy công ty, bạn nói:", {"A": "Who are you?", "B": "ABC Company, John speaking.", "C": "What do you want?", "D": "Speak now."}, "B", "Company + name + speaking.", 10),
            Q("Q_L04_03_02", 2, "fill_in_blank", "Could I _____ to Ms. Sarah, please?", {"A": "speak", "B": "speaking", "C": "spoke", "D": "talking"}, "A", "Could I speak to…?", 9),
            Q("Q_L04_03_03", 2, "multiple_choice", "Cách lịch sự khi sếp đang bận:", {"A": "He is busy. Bye.", "B": "I'm afraid he is in a meeting.", "C": "Hang up.", "D": "Not here. Whatever."}, "B", "I'm afraid… + reason.", 10),
            Q("Q_L04_03_04", 2, "error_identification", "Sửa: “Can I leave a messages?”", {"A": "Can", "B": "leave", "C": "messages", "D": "a"}, "C", "A message.", 10, True),
            Q("Q_L04_03_05", 1, "true_false", "On the phone, “This is Anna” often replaces “I am Anna.”", {"A": "True", "B": "False"}, "A", "Standard phone introduction.", 8),
            Q("Q_L04_03_06", 3, "multiple_choice", "Ghép: 1. Caller — 2. Receiver", {"A": "1→Could you ask him to call me back? — 2→Can I take a message?", "B": "1→Can I take a message? — 2→Could you ask him to call me back?", "C": "1→Speaking — 2→Speaking", "D": "1→Bye — 2→Hello"}, "A", "Caller asks callback; receiver offers message.", 13),
            Q("Q_L04_03_07", 2, "multiple_choice", "“Tôi có thể nhận lời nhắn không?”", {"A": "Can I take a message?", "B": "Can I make a message?", "C": "Can I leave a message to you wrong", "D": "I take message?"}, "A", "Can I take a message?", 10),
            Q("Q_L04_03_08", 2, "fill_in_blank", "Please _____ her that David called.", {"A": "tell", "B": "say", "C": "speak", "D": "talk"}, "A", "Tell her that…", 9),
            Q("Q_L04_03_09", 2, "multiple_choice", "A client reads a phone number very fast. You say:", {"A": "What?", "B": "Could you repeat that, please?", "C": "Wrong number.", "D": "Stop."}, "B", "Polite clarification.", 10),
            Q("Q_L04_03_10", 2, "multiple_choice", "“Unavailable” on the phone usually means:", {"A": "Free and waiting", "B": "Not free / not able to take the call", "C": "Happy", "D": "Speaking"}, "B", "Not available.", 10),
        ],
    }


def _lesson_04():
    meta = {"skill": "speaking", "topic": "meetings_opinions", "time_est_minutes": 30, "difficulty": 0.55}
    p1 = """### Giving opinions

Đừng chỉ lặp *I think…* — đa dạng hóa:

- *In my opinion, …*  
- *From my point of view, …*  
- *I strongly believe that …*"""

    p2 = """### Agreeing

- *I completely agree.*  
- *That's a valid point.*  
- *I feel exactly the same way.*"""

    p3 = """### Disagreeing politely

Tránh *You are wrong* trong họp.

**Khen trước, phản biện sau:** *I see your point, but …*

- *I'm afraid I have to disagree.*  
- *That's a good idea, but how about …?*"""

    reading = (
        "In my opinion, we should delay the launch. That's a valid point about the budget. "
        "I see your point, but the risks are high. I'm afraid I have to disagree with the timeline."
    )
    return {
        "lesson_id": "L04_04",
        "lesson_name": "Meetings - Giving Opinions (Speaking/Grammar)",
        "order": 4,
        "estimated_minutes": 40,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Opinions", "body": p1},
                {"title": "Trang 2 — Agreeing", "body": p2},
                {"title": "Trang 3 — Disagreeing politely", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "valid point / disagree politely", "vi": "ý hợp lý / phản đối lịch sự"},
            ],
            "examples": [
                {"english": "I'm afraid I have to disagree.", "vietnamese": "Tôi e là tôi phải không đồng ý."},
            ],
        },
        "quizzes": [
            Q("Q_L04_04_01", 2, "multiple_choice", "Mở đầu để đưa ý kiến cá nhân:", {"A": "In my opinion,", "B": "I am opinion,", "C": "In my opinions,", "D": "My opinion is are"}, "A", "In my opinion, …", 9),
            Q("Q_L04_04_02", 2, "fill_in_blank", "I completely _____. (đồng ý)", {"A": "agree", "B": "agrees", "C": "agreeing", "D": "to agree"}, "A", "I completely agree.", 9),
            Q("Q_L04_04_03", 2, "multiple_choice", "Cách phản biện lịch sự:", {"A": "You are wrong.", "B": "I see your point, but…", "C": "That's stupid.", "D": "Shut up."}, "B", "Acknowledge + but…", 10),
            Q("Q_L04_04_04", 2, "error_identification", "Sửa: “From my point of views…”", {"A": "From", "B": "my", "C": "views", "D": "point"}, "C", "Point of view (singular).", 11, True),
            Q("Q_L04_04_05", 3, "multiple_choice", "Ghép: 1. Agree — 2. Disagree", {"A": "1→That's a valid point — 2→I'm afraid I have to disagree", "B": "1→I'm afraid I have to disagree — 2→That's a valid point", "C": "1→You are wrong — 2→I agree", "D": "1→Stupid — 2→Valid"}, "A", "Valid point = agree tone; disagree phrase for opposition.", 13),
            Q("Q_L04_04_06", 2, "fill_in_blank", "I strongly _____ that we should launch the product now.", {"A": "believe", "B": "believes", "C": "believing", "D": "belief"}, "A", "I strongly believe that…", 9),
            Q("Q_L04_04_07", 1, "true_false", "Using only “I think…” repeatedly is the best style in every meeting.", {"A": "True", "B": "False"}, "B", "Vary your language.", 8),
            Q("Q_L04_04_08", 2, "multiple_choice", "“Tôi e là tôi phải không đồng ý.”", {"A": "I'm afraid I have to disagree.", "B": "I'm afraid to disagree have.", "C": "I afraid disagree.", "D": "I'm disagree afraid."}, "A", "Fixed phrase.", 10),
            Q("Q_L04_04_09", 2, "multiple_choice", "Your boss suggests a risky idea. You respond professionally:", {"A": "It's stupid.", "B": "That's an interesting idea, but what about the risks?", "C": "No.", "D": "Wrong."}, "B", "Polite + constructive.", 12),
            Q("Q_L04_04_10", 2, "multiple_choice", "“Valid point” means:", {"A": "A reasonable / good argument", "B": "A useless idea", "C": "Invalid", "D": "Off topic"}, "A", "Valid = well-reasoned.", 9),
        ],
    }


def _lesson_05():
    meta = {"skill": "grammar", "topic": "modals_requests", "time_est_minutes": 35, "difficulty": 0.6}
    p1 = """### Polite requests (modals)

Tránh mệnh lệnh: *Send me the file!*

- *Could you + verb… please?* — *Could you send me the report, please?*  
- *Would you mind + V-ing?* — *Would you mind sending me the report?*"""

    p2 = """### Asking permission

- *Do you mind if I leave early today?*

**Đồng ý:** *No, not at all.* / *Go ahead.*"""

    p3 = """### Professional apologies

- *I apologize for the delay.*  
- *I'm sorry for the inconvenience — I will fix it right away.*"""

    reading = (
        "Could you review this draft, please? Would you mind checking the numbers? "
        "Do you mind if I leave at 4 PM? I apologize for the late reply."
    )
    return {
        "lesson_id": "L04_05",
        "lesson_name": "Making Requests & Apologizing (Modals)",
        "order": 5,
        "estimated_minutes": 45,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Polite requests", "body": p1},
                {"title": "Trang 2 — Permission", "body": p2},
                {"title": "Trang 3 — Apologies", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "Would you mind + -ing", "vi": "phiền bạn làm…"},
                {"word": "apologize for", "vi": "xin lỗi về…"},
            ],
            "examples": [
                {"english": "I apologize for the delay.", "vietnamese": "Tôi xin lỗi vì sự chậm trễ."},
            ],
        },
        "quizzes": [
            Q("Q_L04_05_01", 2, "multiple_choice", "Cách yêu cầu gửi file lịch sự nhất:", {"A": "Send me the file.", "B": "Could you send me the file, please?", "C": "File now.", "D": "Give file."}, "B", "Could you… please?", 10),
            Q("Q_L04_05_02", 2, "fill_in_blank", "Would you mind _____ (help) me with this project?", {"A": "helping", "B": "help", "C": "to help", "D": "helped"}, "A", "Would you mind + V-ing.", 10),
            Q("Q_L04_05_03", 2, "error_identification", "Sửa: “I apologize of the mistake.”", {"A": "I", "B": "apologize", "C": "of", "D": "mistake"}, "C", "Apologize for.", 11, True),
            Q("Q_L04_05_04", 2, "multiple_choice", "“Do you mind if I open the window?” — To agree, you say:", {"A": "Yes, I mind.", "B": "No, not at all.", "C": "Yes, please mind.", "D": "I mind yes."}, "B", "No, not at all = not bothered.", 11),
            Q("Q_L04_05_05", 2, "multiple_choice", "“Tôi xin lỗi vì sự chậm trễ.”", {"A": "I apologize for the delay.", "B": "I apologize the delay.", "C": "I apologize of the delay.", "D": "I sorry for delay."}, "A", "Apologize for the delay.", 10),
            Q("Q_L04_05_06", 1, "true_false", "After “Would you mind”, the verb is usually in -ing form.", {"A": "True", "B": "False"}, "A", "Would you mind closing…?", 8),
            Q("Q_L04_05_07", 2, "fill_in_blank", "I am sorry for the _____ (inconvenience).", {"A": "inconvenience", "B": "inconvenient", "C": "convenient", "D": "convenience"}, "A", "Noun after *the*.", 9),
            Q("Q_L04_05_08", 2, "multiple_choice", "A customer complains about a system error. You should say:", {"A": "It's not my fault.", "B": "I apologize for the inconvenience. We are fixing it.", "C": "Not my problem.", "D": "So what?"}, "B", "Professional apology + action.", 12),
            Q("Q_L04_05_09", 2, "multiple_choice", "“Apologize” is closest to:", {"A": "Request", "B": "Say sorry formally", "C": "Order", "D": "Cancel"}, "B", "Apologize ≈ say sorry (formal register).", 9),
            Q("Q_L04_05_10", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "Would you mind closing the door?", "B": "Would you mind close the door?", "C": "Would you mind to closing the door?", "D": "You mind would closing door?"}, "A", "Would you mind + V-ing + object.", 11),
        ],
    }


def _lesson_06():
    meta = {"skill": "vocabulary", "topic": "company_structure", "time_est_minutes": 25, "difficulty": 0.55}
    p1 = """### Core departments

- **HR** — Human Resources (nhân sự)  
- **IT** — Information Technology  
- **Sales & Marketing**  
- **Accounting / Finance**  
- **R&D** — Research and Development"""

    p2 = """### Titles & roles

*CEO*, *manager*, *supervisor*, *employee / staff*, *colleague / coworker*"""

    p3 = """### Responsibilities

- *I am responsible for + V-ing / noun* — *I am responsible for training new staff.*  
- *I am in charge of …* — *I am in charge of the marketing budget.*"""

    reading = (
        "Our HR department hires new employees. IT fixes computers. "
        "I am responsible for monthly reports. My manager is in charge of the whole team."
    )
    return {
        "lesson_id": "L04_06",
        "lesson_name": "Departments & Responsibilities (Vocabulary)",
        "order": 6,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Departments", "body": p1},
                {"title": "Trang 2 — Titles", "body": p2},
                {"title": "Trang 3 — Responsibilities", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "HR / IT / R&D", "vi": "các phòng ban phổ biến"},
                {"word": "responsible for / in charge of", "vi": "chịu trách nhiệm / phụ trách"},
            ],
            "examples": [
                {"english": "I am in charge of the IT department.", "vietnamese": "Tôi phụ trách phòng IT."},
            ],
        },
        "quizzes": [
            Q("Q_L04_06_01", 1, "multiple_choice", "Phòng lo tuyển dụng nhân sự:", {"A": "HR", "B": "R&D", "C": "IT", "D": "Sales"}, "A", "Human Resources.", 8),
            Q("Q_L04_06_02", 2, "fill_in_blank", "I am responsible _____ creating monthly reports.", {"A": "for", "B": "of", "C": "to", "D": "in"}, "A", "Responsible for.", 9),
            Q("Q_L04_06_03", 2, "error_identification", "Sửa: “I am in charge for the project.”", {"A": "in charge", "B": "for", "C": "the", "D": "project"}, "B", "In charge of.", 11, True),
            Q("Q_L04_06_04", 2, "multiple_choice", "Người quản lý trực tiếp thường gọi là:", {"A": "Colleague only", "B": "Supervisor / Manager", "C": "CEO always", "D": "HR only"}, "B", "Supervisor / manager.", 10),
            Q("Q_L04_06_05", 3, "multiple_choice", "Ghép: 1. Accounting — 2. R&D", {"A": "1→money & taxes — 2→new product ideas", "B": "1→new product ideas — 2→money & taxes", "C": "1→IT support — 2→HR", "D": "1→marketing — 2→sales only"}, "A", "Accounting ~ money; R&D ~ research.", 12),
            Q("Q_L04_06_06", 2, "fill_in_blank", "A person you work with is your _____.", {"A": "colleague", "B": "CEO", "C": "passport", "D": "browser"}, "A", "Colleague / coworker.", 9),
            Q("Q_L04_06_07", 1, "true_false", "CEO stands for Chief Employee Officer.", {"A": "True", "B": "False"}, "B", "Chief Executive Officer.", 8),
            Q("Q_L04_06_08", 2, "multiple_choice", "“Tôi phụ trách phòng IT.”", {"A": "I am in charge of the IT department.", "B": "I am in charge for the IT department.", "C": "I am charge of IT.", "D": "I in charge the IT."}, "A", "In charge of.", 10),
            Q("Q_L04_06_09", 2, "multiple_choice", "If your computer breaks, you usually contact:", {"A": "HR", "B": "IT", "C": "Accounting", "D": "Sales"}, "B", "IT support.", 9),
            Q("Q_L04_06_10", 2, "multiple_choice", "After “responsible for”, we often use:", {"A": "to + verb", "B": "V-ing or a noun", "C": "bare infinitive only", "D": "past tense"}, "B", "Responsible for + -ing / noun.", 11),
        ],
    }


def _lesson_07():
    meta = {"skill": "grammar", "topic": "perfect_tense_reporting", "time_est_minutes": 35, "difficulty": 0.65}
    p1 = """### Present perfect (reporting)

*Have/has + past participle* — kết quả / kinh nghiệm liên quan **hiện tại**, báo cáo tiến độ.

*I have finished the report.*"""

    p2 = """### Just / already / yet

- *I have just sent the email.*  
- *We have already booked the flight.*  
- *I haven't received the data yet.* (yet ở cuối câu phủ định/câu hỏi)"""

    p3 = """### vs Past simple

Có **mốc thời gian cụ thể** trong quá khứ (*yesterday*, *last week*) → **past simple**.

✓ *I sent the report yesterday.*  
✗ *I have sent the report yesterday.*"""

    reading = (
        "I have finished the slides. I have just emailed the client. We met the client last week. "
        "I haven't received their feedback yet."
    )
    return {
        "lesson_id": "L04_07",
        "lesson_name": "Reporting Progress (Present Perfect vs Past Simple)",
        "order": 7,
        "estimated_minutes": 45,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Present perfect", "body": p1},
                {"title": "Trang 2 — Just, already, yet", "body": p2},
                {"title": "Trang 3 — vs Past simple", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "already / yet / just", "vi": "đã / chưa / vừa mới (với present perfect)"},
            ],
            "examples": [
                {"english": "I have just called the client.", "vietnamese": "Tôi vừa mới gọi cho khách hàng."},
            ],
        },
        "quizzes": [
            Q("Q_L04_07_01", 2, "multiple_choice", "Boss: “Have you finished the task?” You answer:", {"A": "Yes, I finish.", "B": "Yes, I have already finished it.", "C": "Yes, I finished already have.", "D": "Yes, I finishing."}, "B", "Yes, I have (already)…", 11),
            Q("Q_L04_07_02", 2, "fill_in_blank", "I haven't completed the presentation _____.", {"A": "yet", "B": "already", "C": "just", "D": "ever"}, "A", "Yet in negative.", 9),
            Q("Q_L04_07_03", 2, "error_identification", "Which part is wrong: “We have met the client last week.”", {"A": "We", "B": "have met", "C": "the client", "D": "last week"}, "B", "We met the client last week (past simple).", 12, True),
            Q("Q_L04_07_04", 2, "multiple_choice", "I _____ just updated the software.", {"A": "has", "B": "have", "C": "did", "D": "was"}, "B", "I have just…", 9),
            Q("Q_L04_07_05", 2, "multiple_choice", "“Tôi vừa mới gọi cho khách hàng.”", {"A": "I have just called the client.", "B": "I just have called the client.", "C": "I have called just the client.", "D": "I called just have the client."}, "A", "Have just + past participle.", 11),
            Q("Q_L04_07_06", 1, "true_false", "We often use “yet” at the end of a negative sentence to mean “not until now”.", {"A": "True", "B": "False"}, "A", "Haven't… yet.", 8),
            Q("Q_L04_07_07", 2, "multiple_choice", "You submitted the report at 8 AM; now it is 10 AM. You say:", {"A": "I sent it at 8 AM.", "B": "I have sent it at 8 AM.", "C": "I have sent it since 8 AM wrong", "D": "I send it at 8 AM."}, "A", "Specific past time → past simple.", 12),
            Q("Q_L04_07_08", 3, "multiple_choice", "Ghép: 1. Already — 2. Yet", {"A": "1→emphasizes completed before now — 2→negative/question “still not”", "B": "1→negative — 2→positive", "C": "1→past simple only — 2→future", "D": "same meaning"}, "A", "Already / yet usage.", 13),
            Q("Q_L04_07_09", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "I have already sent the email.", "B": "I already have sent the email.", "C": "I sent have already the email.", "D": "I have sent already the email."}, "A", "Standard word order.", 11),
            Q("Q_L04_07_10", 2, "fill_in_blank", "The IT team _____ (fix) the bug. It is working now.", {"A": "has fixed", "B": "fixed", "C": "fixes", "D": "fixing"}, "A", "Result matters now → has fixed.", 10),
        ],
    }


def _lesson_08():
    meta = {"skill": "vocabulary", "topic": "scheduling", "time_est_minutes": 25, "difficulty": 0.55}
    p1 = """### Proposing a time

- *Are you available on Tuesday at 3 PM?*  
- *Can we set up a meeting for next week?*"""

    p2 = """### Postpone / cancel / move

- *Can we postpone the meeting to Friday?* / *push it back*  
- *Can we bring it forward to Monday?* (sớm hơn)  
- *I'm afraid I have to cancel our appointment.*"""

    p3 = """### Confirming

- *Tuesday at 3 PM works for me.*  
- *I will send you a calendar invite.*"""

    reading = (
        "Are you available on Monday at 10? Can we set up a call? "
        "If not, we can push the meeting back to Wednesday. Tuesday works for me."
    )
    return {
        "lesson_id": "L04_08",
        "lesson_name": "Scheduling & Appointments (Vocabulary)",
        "order": 8,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Proposing time", "body": p1},
                {"title": "Trang 2 — Postpone & cancel", "body": p2},
                {"title": "Trang 3 — Confirming", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "available / postpone / cancel", "vi": "rảnh / hoãn / hủy"},
                {"word": "works for me", "vi": "thời gian đó phù hợp với tôi"},
            ],
            "examples": [
                {"english": "Can we postpone the meeting to Friday?", "vietnamese": "Chúng ta có thể hoãn họp sang thứ Sáu không?"},
            ],
        },
        "quizzes": [
            Q("Q_L04_08_01", 2, "multiple_choice", "To ask if someone is free, you often use:", {"A": "empty", "B": "available", "C": "busy only", "D": "full"}, "B", "Are you available…?", 9),
            Q("Q_L04_08_02", 2, "fill_in_blank", "Can we set _____ a meeting for tomorrow?", {"A": "up", "B": "on", "C": "in", "D": "at"}, "A", "Set up a meeting.", 9),
            Q("Q_L04_08_03", 2, "error_identification", "Sửa: “Tuesday works to me.”", {"A": "Tuesday", "B": "works", "C": "to", "D": "me"}, "C", "Works for me.", 10, True),
            Q("Q_L04_08_04", 2, "multiple_choice", "A synonym for “postpone” in scheduling:", {"A": "Bring forward", "B": "Push back", "C": "Confirm", "D": "Attend"}, "B", "Push back ≈ postpone.", 10),
            Q("Q_L04_08_05", 2, "multiple_choice", "“Chúng ta có thể dời buổi họp sang thứ Sáu không?”", {"A": "Can we postpone the meeting to Friday?", "B": "Can we forward the meeting to Friday?", "C": "Can we the meeting postpone Friday?", "D": "Postpone we can Friday?"}, "A", "Postpone to Friday.", 11),
            Q("Q_L04_08_06", 1, "true_false", "“Bring forward” means to schedule earlier.", {"A": "True", "B": "False"}, "A", "Earlier than planned.", 8),
            Q("Q_L04_08_07", 2, "fill_in_blank", "I will send you a calendar _____. (common in Outlook/Google)", {"A": "invite", "B": "invitation", "C": "inviting", "D": "invited"}, "A", "Often “calendar invite” in workplace English.", 10),
            Q("Q_L04_08_08", 2, "multiple_choice", "Reply to “Are you available on Monday?”", {"A": "I am unavailable on Tuesday.", "B": "Yes, Monday works for me.", "C": "Monday is bad always", "D": "No Monday."}, "B", "Direct confirmation.", 10),
            Q("Q_L04_08_09", 3, "multiple_choice", "Ghép: 1. Cancel — 2. Propose a slot", {"A": "1→I have to cancel — 2→Are you available?", "B": "1→Are you available? — 2→I have to cancel", "C": "1→Works for me — 2→Cancel", "D": "1→Postpone — 2→Postpone"}, "A", "Cancel vs proposing time.", 12),
            Q("Q_L04_08_10", 2, "multiple_choice", "“That time works for me” means:", {"A": "That time suits me / is OK", "B": "I must work overtime", "C": "I cancel", "D": "I am busy"}, "A", "Works for me = OK.", 9),
        ],
    }


def _lesson_09():
    meta = {"skill": "speaking", "topic": "presentations", "time_est_minutes": 30, "difficulty": 0.6}
    p1 = """### Opening a presentation

- *Good morning everyone. Thank you for coming.*  
- *Today, I am going to talk about …*  
- *My presentation is divided into three parts. First, … Second, … Finally, …*"""

    p2 = """### Signposting (moving between points)

- *Let's move on to the next point.*  
- *Turning our attention to the budget …*  
- *As you can see on this slide …*"""

    p3 = """### Q&A

- *That brings me to the end of my presentation.*  
- *I would be happy to answer any questions.*  
- *That's a good question. Let me check and get back to you later.*"""

    reading = (
        "Good morning everyone. Today I am going to talk about sales. First, I will outline the goals. "
        "Let's move on to the next point. As you can see on this slide, revenue grew. "
        "That brings me to the end of my presentation. I would be happy to answer any questions."
    )
    return {
        "lesson_id": "L04_09",
        "lesson_name": "Presentations - Signposting (Speaking)",
        "order": 9,
        "estimated_minutes": 40,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Introduction", "body": p1},
                {"title": "Trang 2 — Signposting", "body": p2},
                {"title": "Trang 3 — Q&A", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "signposting / move on", "vi": "chỉ dẫn người nghe / chuyển sang ý tiếp"},
            ],
            "examples": [
                {"english": "Let's move on to the budget.", "vietnamese": "Hãy chuyển sang phần ngân sách."},
            ],
        },
        "quizzes": [
            Q("Q_L04_09_01", 2, "multiple_choice", "To start a presentation professionally:", {"A": "Listen to me.", "B": "Today, I am going to talk about…", "C": "Be quiet.", "D": "Look."}, "B", "Standard opening.", 9),
            Q("Q_L04_09_02", 2, "fill_in_blank", "My presentation is divided _____ three parts.", {"A": "into", "B": "in", "C": "to", "D": "on"}, "A", "Divided into.", 9),
            Q("Q_L04_09_03", 2, "error_identification", "Sửa: “Let's move in to the next slide.”", {"A": "Let's", "B": "move", "C": "in", "D": "slide"}, "C", "Move on to.", 11, True),
            Q("Q_L04_09_04", 2, "multiple_choice", "To direct attention to the slide:", {"A": "Look at me.", "B": "As you can see on this slide…", "C": "Don't read.", "D": "Ignore the slide."}, "B", "Professional signposting.", 10),
            Q("Q_L04_09_05", 2, "multiple_choice", "“Hãy chuyển sang phần ngân sách.”", {"A": "Let's move on to the budget.", "B": "Let's move in to the budget.", "C": "Move budget let's.", "D": "We budget move."}, "A", "Move on to.", 10),
            Q("Q_L04_09_06", 1, "true_false", "In Q&A, saying only “I don't know” is the most professional option.", {"A": "True", "B": "False"}, "B", "Offer to follow up.", 8),
            Q("Q_L04_09_07", 2, "fill_in_blank", "That brings me to the _____ of my presentation.", {"A": "end", "B": "start", "C": "middle", "D": "slide"}, "A", "End of presentation.", 9),
            Q("Q_L04_09_08", 2, "multiple_choice", "Sắp xếp đúng:", {"A": "I would be happy to answer any questions.", "B": "I would happy be to answer any questions.", "C": "I happy would answer any questions.", "D": "Would I be happy answer any questions."}, "A", "Would be happy to + verb.", 11),
            Q("Q_L04_09_09", 2, "multiple_choice", "Signposting helps the audience:", {"A": "Follow the structure of your talk", "B": "Sleep better", "C": "Skip slides", "D": "Ignore you"}, "A", "Clear structure.", 9),
            Q("Q_L04_09_10", 2, "multiple_choice", "“Signposting” in presentations means:", {"A": "Using language to guide listeners through sections", "B": "Only making pretty slides", "C": "Speaking very fast", "D": "Reading every word"}, "A", "Discourse markers / signposts.", 10),
        ],
    }


def _lesson_10():
    meta = {"skill": "reading", "topic": "modern_workplace", "time_est_minutes": 35, "difficulty": 0.65}
    text = (
        "In recent years, the traditional office has changed. Many companies now use a hybrid model. "
        "Employees work from home for three days and go to the office for two days a week. "
        "This model gives staff flexible hours and improves their work-life balance. However, remote work has challenges. "
        "Communication can be difficult. Colleagues can't just walk to another desk to ask a quick question. "
        "Instead, they have to schedule video calls on Zoom or send messages on Slack. "
        "To succeed in a remote team, clear and professional written communication is essential."
    )
    p1 = """### Pre-reading

*Remote work / telecommuting*, *hybrid model*, *flexible hours*, *work-life balance*."""

    p2 = """### Reading

Đọc về **hybrid & remote** — lợi ích và **thách thức giao tiếp**."""

    p3 = """### Post-reading — link to this course

Lợi ích: linh hoạt, cân bằng. Thách thức: không gặp trực tiếp → cần **email, tin nhắn, họp video** rõ ràng — ôn lại các bài trước (email, small talk, lịch hẹn)."""

    return {
        "lesson_id": "L04_10",
        "lesson_name": "Remote Work Culture (Reading)",
        "order": 10,
        "estimated_minutes": 48,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Vocabulary", "body": p1},
                {"title": "Trang 2 — Bài đọc", "body": p2},
                {"title": "Trang 3 — Phân tích", "body": p3},
            ],
            "reading_passage": text,
            "reading_word_count": wc(text),
            "vocabulary": [
                {"word": "hybrid model / remote work", "vi": "làm việc kết hợp / từ xa"},
                {"word": "work-life balance", "vi": "cân bằng công việc và cuộc sống"},
            ],
            "examples": [],
        },
        "quizzes": [
            Q("Q_L04_10_01", 1, "multiple_choice", "What is a “hybrid model” in the text?", {"A": "100% at home", "B": "Working both at home and in the office", "C": "Only in the office", "D": "No work"}, "B", "Home + office mix.", 9),
            Q("Q_L04_10_02", 1, "true_false", "Remote work has no challenges.", {"A": "True", "B": "False"}, "B", "However, remote work has challenges.", 8),
            Q("Q_L04_10_03", 2, "fill_in_blank", "The hybrid model improves an employee's work-life _____.", {"A": "balance", "B": "busy", "C": "budget", "D": "browser"}, "A", "Work-life balance.", 9),
            Q("Q_L04_10_04", 2, "multiple_choice", "Why is communication difficult in remote work (according to the text)?", {"A": "You can't just walk to someone's desk.", "B": "The internet is always bad.", "C": "There is no email.", "D": "Everyone is offline."}, "A", "Can't walk to another desk.", 11),
            Q("Q_L04_10_05", 2, "fill_in_blank", "Tools mentioned for communication include Zoom and _____.", {"A": "Slack", "B": "Facebook only", "C": "paper", "D": "fax"}, "A", "Zoom or Slack.", 10),
            Q("Q_L04_10_06", 2, "multiple_choice", "What is “essential” for remote teams?", {"A": "Speaking loud", "B": "Clear written communication", "C": "Ignoring messages", "D": "No meetings"}, "B", "Clear and professional written communication.", 11),
            Q("Q_L04_10_07", 2, "multiple_choice", "A synonym for “staff” in the passage:", {"A": "Managers only", "B": "Employees", "C": "Customers", "D": "IT tools"}, "B", "Staff ≈ employees.", 9),
            Q("Q_L04_10_08", 1, "true_false", "Flexible hours mean you must work exactly 9–5 with no variation.", {"A": "True", "B": "False"}, "B", "Flexible implies variation.", 9),
            Q("Q_L04_10_09", 2, "multiple_choice", "“Làm việc từ xa có những thử thách.”", {"A": "Remote work has challenges.", "B": "Remote work has no challenge.", "C": "Remote work is challenge.", "D": "Challenges has remote work."}, "A", "Has challenges.", 10),
            Q("Q_L04_10_10", 2, "fill_in_blank", "The text discusses pros and cons of the modern _____.", {"A": "workplace", "B": "airport", "C": "guitar", "D": "hospital"}, "A", "Modern workplace / remote patterns.", 10),
        ],
    }
