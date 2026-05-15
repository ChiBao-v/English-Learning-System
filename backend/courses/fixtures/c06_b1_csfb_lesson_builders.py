"""Khóa C06 — English for Customer Service & F&B (B1): 10 bài × 3 trang × 10 quiz."""

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
    meta = {"skill": "speaking", "topic": "welcoming_guests", "time_est_minutes": 20, "difficulty": 0.4}
    p1 = """### Greeting & reservations

*Good morning / Good evening. Welcome to [Restaurant name].*

- *Do you have a reservation?*  
- *Under what name, please?* (lịch sự hơn khi hỏi tên đặt bàn)"""

    p2 = """### Party size & full house

- *How many people are in your party?* / *A table for how many?*  
- *A table for two, please.*

**Hết chỗ:** *I'm sorry, we are fully booked tonight. Would you like to wait at the bar?*"""

    p3 = """### Seating & menus

- *Right this way, please.* / *Follow me, please.*  
- *Here are your menus. Your server will be with you shortly.*"""

    reading = (
        "Good evening. Welcome to Riverside Grill. Do you have a reservation? Under what name, please? "
        "How many people are in your party? Right this way. Here are your menus."
    )
    return {
        "lesson_id": "L06_01",
        "lesson_name": "Welcoming & Seating Guests (Vocabulary/Speaking)",
        "order": 1,
        "estimated_minutes": 32,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Greeting & reservations", "body": p1},
                {"title": "Trang 2 — Party size & fully booked", "body": p2},
                {"title": "Trang 3 — Seating & menus", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "reservation / fully booked / party", "vi": "đặt bàn / kín chỗ / nhóm (khách)"},
            ],
            "examples": [
                {"english": "Right this way, please.", "vietnamese": "Xin mời đi lối này."},
            ],
        },
        "quizzes": [
            Q("Q_L06_01_01", 2, "multiple_choice", "Khách bước vào nhà hàng — lời chào chuyên nghiệp:", {"A": "Welcome to our restaurant.", "B": "What do you want?", "C": "Go away.", "D": "Money first."}, "A", "Welcome…", 9),
            Q("Q_L06_01_02", 2, "multiple_choice", "Hỏi khách đã đặt bàn chưa:", {"A": "Do you want a table?", "B": "Do you have a reservation?", "C": "Table yes?", "D": "Why are you here?"}, "B", "Do you have a reservation?", 9),
            Q("Q_L06_01_03", 2, "fill_in_blank", "How many people are in your _____?", {"A": "party", "B": "birthday", "C": "kitchen", "D": "fare"}, "A", "In your party = your group.", 9),
            Q("Q_L06_01_04", 2, "multiple_choice", "More professional when asking for the booking name:", {"A": "Under what name, please?", "B": "What is your name? (same context as reservation desk)", "C": "Name!", "D": "Who are you?"}, "A", "Under what name — service English.", 11),
            Q("Q_L06_01_05", 3, "multiple_choice", "Ghép: 1. Hết bàn — 2. Dẫn khách", {"A": "1→We are fully booked — 2→Right this way", "B": "1→Right this way — 2→Fully booked", "C": "1→Menus — 2→Bar", "D": "1→Party — 2→Reservation"}, "A", "Fully booked vs escorting.", 12),
            Q("Q_L06_01_06", 1, "true_false", "“Your server will be with you shortly” means the waiter is coming soon.", {"A": "True", "B": "False"}, "A", "Shortly = soon.", 8),
            Q("Q_L06_01_07", 2, "multiple_choice", "“Xin mời đi lối này.”", {"A": "Right this way, please.", "B": "Left this wrong way.", "C": "This way is right always.", "D": "Way right this."}, "A", "Fixed phrase.", 9),
            Q("Q_L06_01_08", 2, "fill_in_blank", "Here are your _____.", {"A": "menus", "B": "gates", "C": "passports", "D": "fares"}, "A", "Here are your menus.", 8),
            Q("Q_L06_01_09", 2, "multiple_choice", "Guest: “We are three.” You respond professionally:", {"A": "No.", "B": "A table for three. Right this way.", "C": "Three is bad.", "D": "Leave."}, "B", "Confirm + seat.", 10),
            Q("Q_L06_01_10", 2, "multiple_choice", "“Fully booked” means:", {"A": "No tables left / fully reserved", "B": "Many books", "C": "Free tables", "D": "Closed forever"}, "A", "Fully booked.", 9),
        ],
    }


def _lesson_02():
    meta = {"skill": "vocabulary", "topic": "taking_orders", "time_est_minutes": 25, "difficulty": 0.45}
    p1 = """### Drinks & ready to order

- *Can I get you something to drink to start off?*  
- *Are you ready to order?*  
- Guest: *We need a few more minutes.*"""

    p2 = """### Recommendations (upselling)

- *I highly recommend the grilled salmon.*  
- *Our chef's special today is …*  
- *Do you prefer meat or seafood?*"""

    p3 = """### Confirming the order

- *Let me repeat your order. That's one steak, medium rare, and two Cokes.*  
- *Would you like anything else?*  
- *I'll have that right out for you.*"""

    reading = (
        "Can I get you something to drink? Are you ready to order? I highly recommend the salmon. "
        "Let me repeat your order: one steak, medium rare. Would you like anything else?"
    )
    return {
        "lesson_id": "L06_02",
        "lesson_name": "Taking Orders & Recommending (Vocabulary)",
        "order": 2,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Ordering flow", "body": p1},
                {"title": "Trang 2 — Recommendations", "body": p2},
                {"title": "Trang 3 — Repeat & confirm", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "medium rare / chef's special / repeat the order", "vi": "chín tái / món đặc biệt / nhắc lại order"},
            ],
            "examples": [
                {"english": "Would you like anything else?", "vietnamese": "Quý khách có dùng thêm gì không?"},
            ],
        },
        "quizzes": [
            Q("Q_L06_02_01", 2, "multiple_choice", "Offer drinks first:", {"A": "Can I get you something to drink?", "B": "Drink water?", "C": "Water only.", "D": "No drinks."}, "A", "Polite offer.", 9),
            Q("Q_L06_02_02", 2, "fill_in_blank", "Are you _____ to order?", {"A": "ready", "B": "readily", "C": "reading", "D": "real"}, "A", "Ready to order.", 8),
            Q("Q_L06_02_03", 2, "multiple_choice", "Guest can't decide yet. You say:", {"A": "Hurry up.", "B": "Would you like some recommendations?", "C": "Choose now or leave.", "D": "Bad customer."}, "B", "Helpful.", 10),
            Q("Q_L06_02_04", 2, "error_identification", "Fix: “I high recommend this dish.”", {"A": "I", "B": "high", "C": "recommend", "D": "dish"}, "B", "Highly recommend.", 10, True),
            Q("Q_L06_02_05", 3, "multiple_choice", "Match: 1. Medium rare — 2. Chef's special", {"A": "1→steak doneness — 2→today's special dish", "B": "1→special — 2→doneness", "C": "1→drink — 2→dessert", "D": "1→vegan — 2→halal"}, "A", "Terms.", 12),
            Q("Q_L06_02_06", 1, "true_false", "You should repeat the order back to avoid mistakes.", {"A": "True", "B": "False"}, "A", "Confirm.", 8),
            Q("Q_L06_02_07", 2, "multiple_choice", "“Quý khách có dùng thêm gì không?”", {"A": "Would you like anything else?", "B": "You else anything like?", "C": "Anything else would?", "D": "Else what?"}, "A", "Anything else.", 9),
            Q("Q_L06_02_08", 2, "fill_in_blank", "Let me _____ your order.", {"A": "repeat", "B": "repetition", "C": "repeating", "D": "repeated"}, "A", "Repeat your order.", 9),
            Q("Q_L06_02_09", 2, "multiple_choice", "Guest orders steak. You should ask:", {"A": "How would you like your steak cooked?", "B": "Do you like cow?", "C": "Steak is meat.", "D": "No questions."}, "A", "Doneness.", 11),
            Q("Q_L06_02_10", 2, "multiple_choice", "“I'll have that right out for you” means:", {"A": "I'll bring it soon", "B": "I must go outside", "C": "No food", "D": "You leave"}, "A", "Serve soon.", 9),
        ],
    }


def _lesson_03():
    meta = {"skill": "vocabulary", "topic": "diets_allergies", "time_est_minutes": 25, "difficulty": 0.5}
    p1 = """### Allergies

*Nuts / peanuts*, *seafood / shellfish*, *dairy*, *gluten*"""

    p2 = """### Dietary preferences

*Vegetarian*, *vegan*, *halal*

*Does this dish contain meat?*"""

    p3 = """### Kitchen communication

- *I will check with the chef to be sure.*  
- *We can remove the peanuts for you.*"""

    reading = "I'm vegan. Does this contain dairy? I will check with the chef. We can remove the nuts from the salad."
    return {
        "lesson_id": "L06_03",
        "lesson_name": "Dietary Requirements & Allergies (Vocabulary/Listening)",
        "order": 3,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Allergies", "body": p1},
                {"title": "Trang 2 — Diets", "body": p2},
                {"title": "Trang 3 — Kitchen", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "vegan / dairy / check with the chef", "vi": "thuần chay / sản phẩm sữa / hỏi bếp"},
            ],
            "examples": [
                {"english": "I will check with the chef.", "vietnamese": "Tôi sẽ kiểm tra với bếp trưởng."},
            ],
        },
        "quizzes": [
            Q("Q_L06_03_01", 2, "multiple_choice", "A vegan does NOT eat:", {"A": "Apple", "B": "Cheese", "C": "Carrot", "D": "Rice"}, "B", "Cheese = animal product.", 10),
            Q("Q_L06_03_02", 2, "multiple_choice", "Milk, butter, cheese are:", {"A": "Dairy", "B": "Gluten", "C": "Nuts", "D": "Shellfish"}, "A", "Dairy.", 9),
            Q("Q_L06_03_03", 2, "fill_in_blank", "I am allergic _____ peanuts.", {"A": "to", "B": "for", "C": "at", "D": "on"}, "A", "Allergic to.", 8),
            Q("Q_L06_03_04", 2, "error_identification", "Fix: “Does this dish contains dairy?”", {"A": "Does", "B": "dish", "C": "contains", "D": "dairy"}, "C", "Does… contain?", 11, True),
            Q("Q_L06_03_05", 3, "multiple_choice", "Match: 1. Seafood — 2. Halal", {"A": "1→shrimp/fish — 2→Islamic dietary rules", "B": "1→halal — 2→seafood", "C": "1→dairy — 2→vegan", "D": "1→gluten — 2→nuts"}, "A", "Categories.", 12),
            Q("Q_L06_03_06", 1, "true_false", "A typical vegetarian eats chicken.", {"A": "True", "B": "False"}, "B", "No meat.", 8),
            Q("Q_L06_03_07", 2, "multiple_choice", "“Tôi sẽ kiểm tra với bếp trưởng.”", {"A": "I will check with the chef.", "B": "I will chef with the check.", "C": "Chef I check.", "D": "Checking chef I."}, "A", "Check with the chef.", 9),
            Q("Q_L06_03_08", 2, "fill_in_blank", "We can _____ the peanuts from the salad.", {"A": "remove", "B": "removal", "C": "removing", "D": "removed"}, "A", "Remove the peanuts.", 9),
            Q("Q_L06_03_09", 2, "multiple_choice", "Guest has a severe allergy and asks about milk in soup. You're not sure. You:", {"A": "Check with the chef", "B": "Guess “maybe no”", "C": "Ignore", "D": "Say vegan"}, "A", "Never guess allergies.", 12),
            Q("Q_L06_03_10", 2, "multiple_choice", "“Dietary requirements” means:", {"A": "Food-related needs/restrictions", "B": "Payment requests", "C": "Table size", "D": "Tip amount"}, "A", "Dietary requirements.", 9),
        ],
    }


def _lesson_04():
    meta = {"skill": "speaking", "topic": "retail_assistance", "time_est_minutes": 25, "difficulty": 0.45}
    p1 = """### Greeting shoppers

- *Good afternoon. Are you looking for anything in particular?*  
- *Let me know if you need any help.*  
- Guest: *I'm just browsing / looking, thanks.*"""

    p2 = """### Sizes, colors, fitting

- *What size are you?*  
- *We have this in blue and red.*  
- *The fitting rooms are right over there.*"""

    p3 = """### Stock

- *Let me check in the back for you.*  
- *I'm afraid we are out of stock in your size.*"""

    reading = "Are you looking for anything in particular? I'm just browsing. The fitting rooms are over there. Let me check in the back."
    return {
        "lesson_id": "L06_04",
        "lesson_name": "Retail & Shop Assistance (Speaking)",
        "order": 4,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Offering help", "body": p1},
                {"title": "Trang 2 — Sizes & fitting", "body": p2},
                {"title": "Trang 3 — Stock", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "browsing / in particular / out of stock", "vi": "chỉ xem / cụ thể / hết size-hàng"},
            ],
            "examples": [
                {"english": "Let me check in the back for you.", "vietnamese": "Để tôi vào kho kiểm tra."},
            ],
        },
        "quizzes": [
            Q("Q_L06_04_01", 2, "multiple_choice", "Polite offer of help:", {"A": "What do you want to buy?", "B": "Are you looking for anything in particular?", "C": "Buy now!", "D": "Money?"}, "B", "In particular.", 9),
            Q("Q_L06_04_02", 2, "multiple_choice", "“I'm just browsing” means:", {"A": "Only looking, not buying yet", "B": "I want to buy everything", "C": "I'm lost", "D": "I'm angry"}, "A", "Browsing.", 9),
            Q("Q_L06_04_03", 2, "fill_in_blank", "The fitting _____ are right over there.", {"A": "rooms", "B": "room's", "C": "roomes", "D": "gates"}, "A", "Fitting rooms.", 8),
            Q("Q_L06_04_04", 2, "error_identification", "Fix: “I'm afraid we are out the stock.”", {"A": "I'm", "B": "afraid", "C": "out the stock", "D": "we"}, "C", "Out of stock.", 11, True),
            Q("Q_L06_04_05", 3, "multiple_choice", "Match: 1. Check the back — 2. Size", {"A": "1→go to storeroom — 2→S/M/L", "B": "1→size — 2→back", "C": "1→menu — 2→party", "D": "1→gate — 2→fare"}, "A", "Back vs size.", 12),
            Q("Q_L06_04_06", 1, "true_false", "“In particular” means “specifically / especially”.", {"A": "True", "B": "False"}, "A", "In particular.", 8),
            Q("Q_L06_04_07", 2, "multiple_choice", "“Báo tôi nếu quý khách cần giúp đỡ.”", {"A": "Let me know if you need any help.", "B": "Let me know you need if help.", "C": "Know let me help.", "D": "Help me let know."}, "A", "Let me know…", 10),
            Q("Q_L06_04_08", 2, "fill_in_blank", "What _____ are you?", {"A": "size", "B": "sigh", "C": "sized", "D": "sizing"}, "A", "What size?", 8),
            Q("Q_L06_04_09", 2, "multiple_choice", "Guest asks for black — not on display. You say:", {"A": "Let me check in the back.", "B": "No, we don't. (end)", "C": "Black is bad.", "D": "Go home."}, "A", "Check stock.", 10),
            Q("Q_L06_04_10", 2, "multiple_choice", "“Out of stock” means:", {"A": "No more available", "B": "Lots in store", "C": "On sale", "D": "New arrival"}, "A", "Out of stock.", 8),
        ],
    }


def _lesson_05():
    meta = {"skill": "vocabulary", "topic": "processing_payments", "time_est_minutes": 20, "difficulty": 0.4}
    p1 = """### Total & methods

- *Your total comes to $45.50.*  
- *How would you like to pay?* / *Cash or card?*"""

    p2 = """### Processing

- *Please insert or tap your card.*  
- *Please enter your PIN.*  
- *Here is your change.*"""

    p3 = """### Wrapping up

- *Would you like your receipt?*  
- *Do you need a bag for this?*  
- *Have a wonderful day. Hope to see you again!*"""

    reading = "Your total comes to fifty dollars. How would you like to pay? Please tap your card. Here is your change. Would you like your receipt?"
    return {
        "lesson_id": "L06_05",
        "lesson_name": "Handling Payments & Cashier (Vocabulary)",
        "order": 5,
        "estimated_minutes": 30,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Total & pay", "body": p1},
                {"title": "Trang 2 — Card & cash", "body": p2},
                {"title": "Trang 3 — Receipt & bag", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "total / PIN / receipt / change", "vi": "tổng / mã PIN / hóa đơn / tiền thối"},
            ],
            "examples": [
                {"english": "Would you like your receipt?", "vietnamese": "Quý khách có lấy hóa đơn không?"},
            ],
        },
        "quizzes": [
            Q("Q_L06_05_01", 2, "multiple_choice", "Professional total announcement:", {"A": "Your total comes to $50.", "B": "Give me $50.", "C": "Pay now or else.", "D": "Money fifty."}, "A", "Your total comes to…", 9),
            Q("Q_L06_05_02", 2, "fill_in_blank", "How would you like to _____?", {"A": "pay", "B": "paid", "C": "paying", "D": "pays"}, "A", "How would you like to pay?", 8),
            Q("Q_L06_05_03", 2, "multiple_choice", "Customer pays cash with extra — you return money and say:", {"A": "Here is your change.", "B": "Here is your money wrong", "C": "Keep everything.", "D": "No change."}, "A", "Here is your change.", 9),
            Q("Q_L06_05_04", 2, "error_identification", "More natural: “Do you want receipt?”", {"A": "Do", "B": "you", "C": "want receipt", "D": "?"}, "C", "…a receipt / your receipt.", 11, True),
            Q("Q_L06_05_05", 3, "multiple_choice", "Match: 1. Tap card — 2. Insert card", {"A": "1→contactless tap — 2→insert chip", "B": "1→insert — 2→tap", "C": "1→PIN — 2→receipt", "D": "1→cash — 2→bag"}, "A", "Tap vs insert.", 11),
            Q("Q_L06_05_06", 1, "true_false", "PIN usually stands for Personal Identification Number.", {"A": "True", "B": "False"}, "A", "PIN.", 8),
            Q("Q_L06_05_07", 2, "multiple_choice", "“Quý khách có cần túi không?”", {"A": "Do you need a bag?", "B": "Do you bag a need?", "C": "Bag need you?", "D": "Need bag why?"}, "A", "Do you need a bag?", 9),
            Q("Q_L06_05_08", 2, "fill_in_blank", "Please enter your _____.", {"A": "PIN", "B": "pen", "C": "pan", "D": "pun"}, "A", "Enter your PIN.", 8),
            Q("Q_L06_05_09", 2, "multiple_choice", "After payment, you often ask:", {"A": "Would you like your receipt?", "B": "Give me a tip now.", "C": "Leave your PIN aloud.", "D": "Show password to everyone."}, "A", "Receipt offer.", 10),
            Q("Q_L06_05_10", 2, "multiple_choice", "“Cash” means:", {"A": "Physical money", "B": "Credit card only", "C": "Bank transfer only", "D": "Cryptocurrency only"}, "A", "Cash.", 8),
        ],
    }


def _lesson_06():
    meta = {"skill": "speaking", "topic": "complaints_solutions", "time_est_minutes": 35, "difficulty": 0.65}
    p1 = """### Acknowledge & apologize

Không đổ lỗi khách hoặc **đổ lỗi bếp trước mặt khách**.

- *I'm so sorry to hear that.*  
- *I apologize for the inconvenience.*"""

    p2 = """### Solutions

- *I'll bring you a new one right away.*  
- *I'll send housekeeping up immediately.*"""

    p3 = """### Compensate

- *Please let me offer you a free dessert.*  
- *I'll deduct this from your bill.*"""

    reading = "I'm sorry the soup is cold. I'll bring a hot one right away. I apologize for the inconvenience."
    return {
        "lesson_id": "L06_06",
        "lesson_name": "Handling Complaints (De-escalation)",
        "order": 6,
        "estimated_minutes": 45,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Apologize", "body": p1},
                {"title": "Trang 2 — Fix it", "body": p2},
                {"title": "Trang 3 — Compensate", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "de-escalation / inconvenience / deduct from the bill", "vi": "xoa dịu / bất tiện / khấu trừ vào hóa đơn"},
            ],
            "examples": [
                {"english": "I will bring you a new one right away.", "vietnamese": "Tôi sẽ mang ra một phần mới ngay."},
            ],
        },
        "quizzes": [
            Q("Q_L06_06_01", 2, "multiple_choice", "Guest says the soup is cold. First line:", {"A": "It's not my fault.", "B": "I apologize for that. Let me get you a hot one.", "C": "Eat it.", "D": "Kitchen problem."}, "B", "Apology + solution.", 11),
            Q("Q_L06_06_02", 2, "multiple_choice", "Shows empathy best:", {"A": "I understand your frustration.", "B": "You are too angry.", "C": "Calm down idiot.", "D": "Not my job."}, "A", "Empathy.", 9),
            Q("Q_L06_06_03", 2, "fill_in_blank", "I apologize for the _____.", {"A": "inconvenience", "B": "inconvenient", "C": "convenience", "D": "convenient"}, "A", "Inconvenience (noun).", 9),
            Q("Q_L06_06_04", 2, "error_identification", "Fix: “I will deduct this to your bill.”", {"A": "I", "B": "deduct", "C": "to", "D": "bill"}, "C", "Deduct **from** your bill.", 11, True),
            Q("Q_L06_06_05", 3, "multiple_choice", "Match: 1. Right away — 2. Compensate", {"A": "1→immediately — 2→make up (discount/dessert)", "B": "1→compensate — 2→delay", "C": "1→never — 2→argue", "D": "1→tip — 2→receipt"}, "A", "Speed vs compensation.", 12),
            Q("Q_L06_06_06", 1, "true_false", "You should blame the head chef in front of the guest.", {"A": "True", "B": "False"}, "B", "Don't throw staff under the bus.", 9),
            Q("Q_L06_06_07", 2, "multiple_choice", "“Tôi sẽ mang ra một phần mới ngay lập tức.”", {"A": "I will bring you a new one right away.", "B": "I will right away new one bring.", "C": "I bring new one away right.", "D": "New one I will maybe."}, "A", "Right away.", 10),
            Q("Q_L06_06_08", 2, "fill_in_blank", "Let me _____ you a free coffee.", {"A": "offer", "B": "offering", "C": "offered", "D": "offers"}, "A", "Let me offer you…", 9),
            Q("Q_L06_06_09", 2, "multiple_choice", "Guest reports bad smell in room — best first step:", {"A": "Apologize and offer room change / fix immediately", "B": "Give spray and leave", "C": "Say it's normal", "D": "Laugh"}, "A", "Service recovery.", 12),
            Q("Q_L06_06_10", 2, "multiple_choice", "“De-escalation” means:", {"A": "Calm tension / lower conflict", "B": "Raise prices", "C": "Ignore guest", "D": "Escalate shouting"}, "A", "De-escalate.", 9),
        ],
    }


def _lesson_07():
    meta = {"skill": "grammar", "topic": "passive_voice_service", "time_est_minutes": 35, "difficulty": 0.6}
    p1 = """### Why passive in service?

Khách quan, lịch sự — tránh công kích cá nhân.

- Blunt: *You didn't clean the room!*  
- Better: *The room has not been cleaned.*"""

    p2 = """### Be + past participle

- *Breakfast is served from 6 AM to 10 AM.*  
- *Your table is being prepared right now.*"""

    p3 = """### Common phrases

- *It is strictly prohibited.*  
- *The tax is included.*  
- *The tickets are sold out.*"""

    reading = "Breakfast is served until 10. Your table is being prepared. Smoking is strictly prohibited. The tax is included."
    return {
        "lesson_id": "L06_07",
        "lesson_name": "The Passive Voice in Politeness (Grammar)",
        "order": 7,
        "estimated_minutes": 45,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Why passive", "body": p1},
                {"title": "Trang 2 — Structures", "body": p2},
                {"title": "Trang 3 — Fixed phrases", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "is served / is included / sold out", "vi": "được phục vụ / đã gồm / bán hết"},
            ],
            "examples": [
                {"english": "Your table is being cleaned.", "vietnamese": "Bàn đang được dọn."},
            ],
        },
        "quizzes": [
            Q("Q_L06_07_01", 2, "multiple_choice", "Why use passive in hospitality?", {"A": "To sound polite and neutral", "B": "Only to make sentences longer", "C": "To confuse guests", "D": "To avoid verbs"}, "A", "Politeness.", 9),
            Q("Q_L06_07_02", 2, "multiple_choice", "Which is passive?", {"A": "Your food is being prepared.", "B": "We are preparing your food.", "C": "Chef cooks", "D": "I cook"}, "A", "Is being prepared.", 10),
            Q("Q_L06_07_03", 2, "fill_in_blank", "Breakfast is _____ at 7 AM.", {"A": "served", "B": "serving", "C": "serve", "D": "serves"}, "A", "Is served.", 9),
            Q("Q_L06_07_04", 2, "error_identification", "Fix: “The tax is include in the price.”", {"A": "The", "B": "tax", "C": "include", "D": "price"}, "C", "Is included.", 11, True),
            Q("Q_L06_07_05", 3, "multiple_choice", "Match: 1. Sold out — 2. Prohibited", {"A": "1→no tickets left — 2→not allowed", "B": "1→allowed — 2→sold", "C": "1→included — 2→tax", "D": "1→menu — 2→party"}, "A", "Meanings.", 11),
            Q("Q_L06_07_06", 1, "true_false", "“The glass was broken” is often more tactful than “You broke the glass”.", {"A": "True", "B": "False"}, "A", "Passive softens.", 9),
            Q("Q_L06_07_07", 2, "multiple_choice", "“Bàn đang được dọn.”", {"A": "Your table is being cleaned.", "B": "Your table is cleaning.", "C": "Your table cleans.", "D": "Table is clean being."}, "A", "Is being + past participle.", 11),
            Q("Q_L06_07_08", 2, "multiple_choice", "Correct order:", {"A": "Smoking is strictly prohibited.", "B": "Smoking prohibited strictly is.", "C": "Prohibited smoking is strictly.", "D": "Is smoking prohibited strictly."}, "A", "Adverb placement.", 10),
            Q("Q_L06_07_09", 2, "multiple_choice", "Instead of “You must pay tax”, softer:", {"A": "The tax is included.", "B": "You pay tax now!", "C": "Tax you!", "D": "No tax info."}, "A", "Included in price.", 10),
            Q("Q_L06_07_10", 2, "multiple_choice", "“It is fully booked” is:", {"A": "Passive-style / common fixed phrase", "B": "Only active", "C": "Future tense", "D": "Question"}, "A", "Fixed expression.", 9),
        ],
    }


def _lesson_08():
    meta = {"skill": "speaking", "topic": "phone_reservations", "time_est_minutes": 30, "difficulty": 0.5}
    p1 = """### Answering & details

*[Restaurant], Peter speaking. How may I assist you?*

- *For what date and time?*  
- *For how many people?*"""

    p2 = """### Spelling & read-back

- *Could you spell your last name, please?*  
- *Let me read that back to you. 0-9-8-…*"""

    p3 = """### Confirm & close

- *So I have a reservation for Mr. Smith, a table for 4 on Friday at 7 PM. Is that correct?*  
- *We hold tables for 15 minutes.*  
- *We look forward to seeing you.*"""

    reading = "Grand Cafe, how may I assist you? For what date and time? Could you spell your last name? Let me read that back to you."
    return {
        "lesson_id": "L06_08",
        "lesson_name": "Telephone Reservations (Speaking/Listening)",
        "order": 8,
        "estimated_minutes": 40,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Opening & details", "body": p1},
                {"title": "Trang 2 — Spell & read back", "body": p2},
                {"title": "Trang 3 — Confirm", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "assist / spell / read back / hold a table", "vi": "hỗ trợ / đánh vần / đọc lại / giữ bàn"},
            ],
            "examples": [
                {"english": "How may I assist you?", "vietnamese": "Tôi có thể giúp gì cho quý khách?"},
            ],
        },
        "quizzes": [
            Q("Q_L06_08_01", 2, "multiple_choice", "Professional phone answer:", {"A": "Hello?", "B": "Grand Cafe, how may I assist you?", "C": "What?", "D": "Speak."}, "B", "Name + offer help.", 9),
            Q("Q_L06_08_02", 2, "multiple_choice", "Hard name — you ask:", {"A": "Could you spell that, please?", "B": "What?", "C": "Write yourself.", "D": "Wrong name."}, "A", "Spell please.", 9),
            Q("Q_L06_08_03", 2, "fill_in_blank", "For what _____ and time?", {"A": "date", "B": "dating", "C": "data", "D": "gate"}, "A", "Date and time.", 8),
            Q("Q_L06_08_04", 2, "error_identification", "More standard: “Let me read that back ___ you.”", {"A": "Let", "B": "read", "C": "for", "D": "you"}, "C", "Read back **to** you.", 11, True),
            Q("Q_L06_08_05", 3, "multiple_choice", "Match: 1. Spell — 2. Hold a table", {"A": "1→spell name — 2→reserve 15 min policy", "B": "1→hold — 2→spell", "C": "1→pay — 2→PIN", "D": "1→menu — 2→chef"}, "A", "Phone skills.", 12),
            Q("Q_L06_08_06", 1, "true_false", "Confirm all details before ending the call.", {"A": "True", "B": "False"}, "A", "Read back.", 8),
            Q("Q_L06_08_07", 2, "multiple_choice", "“Tôi có thể giúp gì cho quý khách?”", {"A": "How may I assist you?", "B": "How you may assist?", "C": "Assist I may how?", "D": "May how assist?"}, "A", "How may I assist you?", 9),
            Q("Q_L06_08_08", 2, "fill_in_blank", "We look _____ to seeing you.", {"A": "forward", "B": "forwards", "C": "toward", "D": "fourth"}, "A", "Look forward to.", 9),
            Q("Q_L06_08_09", 2, "multiple_choice", "Restaurant is full that night. You say:", {"A": "I'm sorry, we are fully booked that night.", "B": "Don't come here.", "C": "Try another planet.", "D": "Hang up."}, "A", "Polite + reason.", 11),
            Q("Q_L06_08_10", 2, "multiple_choice", "“Assist” is closest to:", {"A": "Help", "B": "Ignore", "C": "Fire", "D": "Sell"}, "A", "Assist ≈ help.", 8),
        ],
    }


def _lesson_09():
    meta = {"skill": "vocabulary", "topic": "directions_advice", "time_est_minutes": 25, "difficulty": 0.45}
    p1 = """### Inside the building

*Restroom / toilets*

- *Go straight down the hall — it's on your right.*  
- *Take the elevator to the 3rd floor.*"""

    p2 = """### Transport help

- *Would you like me to call a taxi for you?*  
- *The nearest bus stop is a 5-minute walk from here.*"""

    p3 = """### Local tips

- *If you like history, you should definitely visit the Old Museum.*  
- *Just be careful with pickpockets in that area.*"""

    reading = "The restrooms are down the hall. Would you like me to call a taxi? I highly recommend the old market — be careful with pickpockets."
    return {
        "lesson_id": "L06_09",
        "lesson_name": "Giving Directions & Local Advice (Vocabulary)",
        "order": 9,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Inside directions", "body": p1},
                {"title": "Trang 2 — Transport", "body": p2},
                {"title": "Trang 3 — Recommend & warn", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "restroom / elevator / pickpockets", "vi": "nhà vệ sinh / thang máy / móc túi"},
            ],
            "examples": [
                {"english": "Take the elevator to the third floor.", "vietnamese": "Đi thang máy lên tầng 3."},
            ],
        },
        "quizzes": [
            Q("Q_L06_09_01", 2, "multiple_choice", "Directions to the restroom:", {"A": "It's down the hall on your left.", "B": "It's in the menu.", "C": "It's on the plate.", "D": "No restroom."}, "A", "Down the hall.", 9),
            Q("Q_L06_09_02", 2, "fill_in_blank", "Would you like me to _____ a taxi for you?", {"A": "call", "B": "cold", "C": "called", "D": "calling"}, "A", "Call a taxi.", 8),
            Q("Q_L06_09_03", 2, "multiple_choice", "The machine that moves between floors:", {"A": "Elevator", "B": "Refrigerator", "C": "Microwave", "D": "Dishwasher"}, "A", "Elevator.", 8),
            Q("Q_L06_09_04", 2, "error_identification", "Fix: “Take the elevator at the 3rd floor.”", {"A": "Take", "B": "elevator", "C": "at", "D": "floor"}, "C", "To the 3rd floor.", 11, True),
            Q("Q_L06_09_05", 3, "multiple_choice", "Match: 1. Go straight — 2. Hall", {"A": "1→đi thẳng — 2→corridor", "B": "1→hall — 2→straight", "C": "1→elevator — 2→restroom", "D": "1→tip — 2→tax"}, "A", "Directions.", 11),
            Q("Q_L06_09_06", 1, "true_false", "You may warn guests about pickpockets in busy areas.", {"A": "True", "B": "False"}, "A", "Safety tip.", 9),
            Q("Q_L06_09_07", 2, "multiple_choice", "“Trạm xe buýt cách đây 5 phút đi bộ.”", {"A": "The bus stop is a 5-minute walk from here.", "B": "Bus is five walk minute.", "C": "Walk bus five.", "D": "From here bus no."}, "A", "5-minute walk.", 10),
            Q("Q_L06_09_08", 2, "fill_in_blank", "You should _____ visit that cafe.", {"A": "definitely", "B": "definite", "C": "defiantly", "D": "defiant"}, "A", "Definitely.", 9),
            Q("Q_L06_09_09", 2, "multiple_choice", "Guest asks for local souvenirs. You:", {"A": "I highly recommend the night market.", "B": "I don't care.", "C": "Buy nothing.", "D": "Go home."}, "A", "Recommend.", 10),
            Q("Q_L06_09_10", 2, "multiple_choice", "“Restroom” in US English often means:", {"A": "Polite word for toilet/bathroom", "B": "Bedroom", "C": "Kitchen", "D": "Garage"}, "A", "Restroom.", 8),
        ],
    }


def _lesson_10():
    meta = {"skill": "writing", "topic": "online_reviews", "time_est_minutes": 35, "difficulty": 0.65}
    p1 = """### Positive reviews

- *Thank you for your kind words!*  
- *We are thrilled to hear that you enjoyed the food.*  
- *We look forward to welcoming you back soon.*"""

    p2 = """### Negative reviews

Structure: **Thanks for feedback → apologize → explain/fix → invite offline contact**

- *We sincerely apologize that your experience was not up to our usual standards.*"""

    p3 = """### Take it offline

- *Please contact us directly at [email] so we can make this right.*  
- *We strive to provide excellent service and hope you give us another chance.*"""

    reading = (
        "Dear Anna, thank you for your kind words! We are thrilled you enjoyed the pasta. "
        "We look forward to welcoming you back. — Regarding your wait-time complaint: we sincerely apologize. "
        "Please contact us directly so we can make this right."
    )
    return {
        "lesson_id": "L06_10",
        "lesson_name": "Replying to Online Reviews (Writing)",
        "order": 10,
        "estimated_minutes": 48,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Positive replies", "body": p1},
                {"title": "Trang 2 — Negative replies", "body": p2},
                {"title": "Trang 3 — Offline resolution", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "feedback / strive / up to our standards", "vi": "góp ý / nỗ lực / đạt chuẩn thông thường"},
            ],
            "examples": [
                {"english": "Please contact us directly.", "vietnamese": "Xin vui lòng liên hệ trực tiếp với chúng tôi."},
            ],
        },
        "quizzes": [
            Q("Q_L06_10_01", 2, "multiple_choice", "Reply to a 5-star review:", {"A": "Thank you for your kind words!", "B": "I know.", "C": "Obviously.", "D": "Whatever."}, "A", "Thank + warm tone.", 9),
            Q("Q_L06_10_02", 2, "multiple_choice", "1-star — long wait. Opening line:", {"A": "We sincerely apologize for the delay.", "B": "You are impatient.", "C": "Not our fault.", "D": "Delete review."}, "A", "Apologize first.", 10),
            Q("Q_L06_10_03", 2, "fill_in_blank", "We are _____ to hear that you liked the service.", {"A": "thrilled", "B": "thrill", "C": "thrilling", "D": "thrills"}, "A", "Thrilled to hear…", 9),
            Q("Q_L06_10_04", 2, "error_identification", "Fix: “We apologies for the mistake.”", {"A": "We", "B": "apologies", "C": "for", "D": "mistake"}, "B", "We apologize.", 11, True),
            Q("Q_L06_10_05", 3, "multiple_choice", "Match: 1. Feedback — 2. Strive", {"A": "1→customer comment — 2→try hard to deliver quality", "B": "1→strive — 2→feedback", "C": "1→receipt — 2→PIN", "D": "1→tip — 2→tax"}, "A", "Vocabulary.", 12),
            Q("Q_L06_10_06", 1, "true_false", "You should argue publicly with angry reviewers.", {"A": "True", "B": "False"}, "B", "Stay professional; move offline.", 9),
            Q("Q_L06_10_07", 2, "multiple_choice", "“Xin vui lòng liên hệ trực tiếp với chúng tôi.”", {"A": "Please contact us directly.", "B": "Please contact direct us.", "C": "Contact please directly.", "D": "Us contact please."}, "A", "Contact us directly.", 9),
            Q("Q_L06_10_08", 2, "fill_in_blank", "Your experience was not up to our usual _____.", {"A": "standards", "B": "standard", "C": "standing", "D": "stands"}, "A", "Standards.", 9),
            Q("Q_L06_10_09", 2, "multiple_choice", "Why give private email/phone for bad reviews?", {"A": "Solve the problem privately and protect reputation", "B": "To spam customers", "C": "To ignore them", "D": "To post passwords"}, "A", "Offline resolution.", 11),
            Q("Q_L06_10_10", 2, "multiple_choice", "Professional closing for many replies:", {"A": "We look forward to welcoming you back.", "B": "Bye.", "C": "Go away.", "D": "Never come."}, "A", "Welcoming tone.", 9),
        ],
    }

