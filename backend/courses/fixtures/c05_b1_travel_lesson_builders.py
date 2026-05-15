"""Khóa C05 — English for International Travel (B1): 10 bài × 3 trang × 10 quiz."""

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
    meta = {"skill": "vocabulary", "topic": "airport_procedures", "time_est_minutes": 25, "difficulty": 0.45}
    p1 = """### Check-in terminology

| Từ | Nghĩa |
|----|--------|
| **Terminal** | nhà ga (quốc tế / nội địa) |
| **Boarding pass** | thẻ lên máy bay |
| **Checked baggage** | hành lý ký gửi |
| **Carry-on luggage** | hành lý xách tay |
| **Overweight** | quá cân (hành lý) |
| **Gate** | cửa khởi hành |

**Ngữ cảnh:** *Your flight departs from Gate 12, Terminal 2.*"""

    p2 = """### Checking in & seats

**Nhân viên:** *May I have your passport and booking reference, please?*

**Khách:** *I'd like a window seat / an aisle seat, please.*

**Hành lý:** *Is my luggage checked through to the final destination?*"""

    p3 = """### Security & special gear

Trình tự: *empty your pockets* → *remove your belt* → *electronics in the bin*.

*Nguồn:* *I have sensitive photography equipment. Can I have a manual inspection?*

**Pin:** *Lithium batteries must be in carry-on luggage.*"""

    reading = (
        "Your flight departs from Gate 12, Terminal 2. Please empty your pockets before security. "
        "Put laptops in the bin. Carry-on only for lithium batteries."
    )
    return {
        "lesson_id": "L05_01",
        "lesson_name": "At the Airport - Check-in & Security (Vocabulary)",
        "order": 1,
        "estimated_minutes": 38,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Check-in terminology", "body": p1},
                {"title": "Trang 2 — Dialogue & seats", "body": p2},
                {"title": "Trang 3 — Security & batteries", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "boarding pass / gate / aisle seat", "vi": "thẻ lên máy / cửa / ghế lối đi"},
                {"word": "carry-on / checked baggage", "vi": "xách tay / ký gửi"},
            ],
            "examples": [
                {"english": "I'd like an aisle seat, please.", "vietnamese": "Tôi muốn ghế lối đi."},
            ],
        },
        "quizzes": [
            Q("Q_L05_01_01", 1, "multiple_choice", "Thẻ dùng để lên máy bay gọi là:", {"A": "Ticket", "B": "Boarding pass", "C": "Passport", "D": "Visa"}, "B", "Boarding pass.", 8),
            Q("Q_L05_01_02", 2, "multiple_choice", "Bạn muốn ngồi gần lối đi (dễ đứng dậy), bạn chọn:", {"A": "Window seat", "B": "Aisle seat", "C": "Middle seat", "D": "Exit row only"}, "B", "Aisle seat.", 9),
            Q("Q_L05_01_03", 2, "fill_in_blank", "My suitcase is 25 kg. The limit is 20 kg. It is _____.", {"A": "overweight", "B": "underweight", "C": "free", "D": "gate"}, "A", "Overweight.", 10),
            Q("Q_L05_01_04", 2, "error_identification", "Find the problem: “I have a luggage.”", {"A": "I", "B": "have", "C": "a", "D": "luggage"}, "C", "Luggage — không dùng *a* (uncountable).", 11, True),
            Q("Q_L05_01_05", 3, "multiple_choice", "Ghép hợp lý: 1. Carry-on — 2. Checked", {"A": "1→small backpack — 2→big suitcase", "B": "1→big suitcase — 2→small backpack", "C": "1→gate — 2→terminal", "D": "1→passport — 2→visa"}, "A", "Xách tay nhỏ; ký gửi lớn.", 12),
            Q("Q_L05_01_06", 2, "multiple_choice", "At security, laptops and cameras usually go:", {"A": "In a separate bin", "B": "Inside checked baggage only", "C": "Left at home", "D": "Under the seat only"}, "A", "Electronics in the bin.", 10),
            Q("Q_L05_01_07", 1, "true_false", "Lithium batteries are allowed in checked baggage.", {"A": "True", "B": "False"}, "B", "Usually in carry-on.", 9),
            Q("Q_L05_01_08", 2, "multiple_choice", "“Cửa khởi hành số mấy?” — Choose the best English:", {"A": "Which gate is it? / What is the gate number?", "B": "Where is the terminal food?", "C": "What is overweight?", "D": "When is boarding pass?"}, "A", "Gate number questions.", 11),
            Q("Q_L05_01_09", 2, "multiple_choice", "You carry a mirrorless camera and lenses on the plane. They should go in:", {"A": "Checked baggage only", "B": "Carry-on luggage", "C": "The trash", "D": "Hold luggage of stranger"}, "B", "Valuables/electronics — carry-on.", 12),
            Q("Q_L05_01_10", 2, "fill_in_blank", "Please _____ your pockets and remove your shoes.", {"A": "empty", "B": "fill", "C": "gate", "D": "board"}, "A", "Empty your pockets.", 9),
        ],
    }


def _lesson_02():
    meta = {"skill": "speaking", "topic": "immigration_customs", "time_est_minutes": 30, "difficulty": 0.5}
    p1 = """### Immigration — short, honest answers

- *Purpose of visit:* *I'm here for vacation / business.*  
- *Duration:* *I'm staying for 10 days.* / *I'm going to stay for two weeks.*  
- *Accommodation:* *I'm staying at the Grand Hotel.*"""

    p2 = """### Customs

- *declare*, *prohibited items*, *duty-free*  
- *Do you have anything to declare?* — *Nothing to declare.*  
- **Green channel** — nothing to declare; **red channel** — goods to declare."""

    p3 = """### Grammar: **be going to** (travel plans)

*I am going to visit Kyoto.*  
*We are going to stay in a traditional house.*"""

    reading = (
        "Officer: What's the purpose of your visit? — Traveler: I'm here for vacation. "
        "I'm going to stay for 10 days at a hotel. Do you have anything to declare? — Nothing to declare."
    )
    return {
        "lesson_id": "L05_02",
        "lesson_name": "Immigration & Customs (Speaking/Grammar)",
        "order": 2,
        "estimated_minutes": 40,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Immigration", "body": p1},
                {"title": "Trang 2 — Customs", "body": p2},
                {"title": "Trang 3 — Be going to", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "declare / duty-free / prohibited", "vi": "khai báo / miễn thuế / cấm"},
            ],
            "examples": [
                {"english": "I am going to stay at this hotel for 5 days.", "vietnamese": "Tôi định ở lại khách sạn này 5 ngày."},
            ],
        },
        "quizzes": [
            Q("Q_L05_02_01", 2, "multiple_choice", "Officer: “What's the purpose of your visit?”", {"A": "I'm here for sightseeing.", "B": "I'm from Vietnam.", "C": "I like coffee.", "D": "My bag is blue."}, "A", "Purpose = why you came.", 10),
            Q("Q_L05_02_02", 2, "fill_in_blank", "How long are you _____ to stay? (plan)", {"A": "going", "B": "go", "C": "went", "D": "gone"}, "A", "Be going to stay.", 9),
            Q("Q_L05_02_03", 2, "multiple_choice", "You have nothing to pay tax on. You use:", {"A": "Red channel", "B": "Green channel (nothing to declare)", "C": "Parking lot", "D": "Gate 99"}, "B", "Green channel when nothing to declare.", 10),
            Q("Q_L05_02_04", 2, "multiple_choice", "Better for a **planned** stay length: “I ___ for two weeks.”", {"A": "stay", "B": "am going to stay", "C": "staying", "D": "stayed"}, "B", "Going to for a plan.", 11),
            Q("Q_L05_02_05", 1, "true_false", "“Duty-free” means you don't pay tax on those goods (in that shop/zone).", {"A": "True", "B": "False"}, "A", "Duty-free.", 8),
            Q("Q_L05_02_06", 3, "multiple_choice", "Match: 1. Vacation — 2. Business", {"A": "1→visiting museums — 2→meeting clients", "B": "1→meeting clients — 2→visiting museums", "C": "1→customs — 2→gate", "D": "1→luggage — 2→passport"}, "A", "Typical activities.", 12),
            Q("Q_L05_02_07", 2, "multiple_choice", "“Tôi định ở lại khách sạn này trong 5 ngày.”", {"A": "I am going to stay at this hotel for 5 days.", "B": "I going to stay at this hotel.", "C": "I am stay at this hotel for 5 days.", "D": "I stay going to hotel."}, "A", "Be going to + stay.", 11),
            Q("Q_L05_02_08", 2, "fill_in_blank", "Do you have a _____ ticket? (khứ hồi)", {"A": "return", "B": "one-way", "C": "single", "D": "fare"}, "A", "Return ticket.", 9),
            Q("Q_L05_02_09", 2, "multiple_choice", "If they say “Show me your documents”, you typically show:", {"A": "Only a coffee receipt", "B": "Passport and hotel/flight booking (as required)", "C": "A map only", "D": "Nothing"}, "B", "Travel documents.", 11),
            Q("Q_L05_02_10", 2, "multiple_choice", "“Prohibited” means:", {"A": "Allowed", "B": "Forbidden / not allowed", "C": "Free", "D": "Cheap"}, "B", "Prohibited = banned.", 9),
        ],
    }


def _lesson_03():
    meta = {"skill": "vocabulary", "topic": "hotel_stay", "time_est_minutes": 25, "difficulty": 0.4}
    p1 = """### Check-in & room types

*Reservation*, *single / double / twin room*, *amenities* (WiFi, gym, pool)

**Vấn đề:** *The air conditioning is not working.*"""

    p2 = """### Services

*Wake-up call*, *room service*, *housekeeping*

*Could I have some extra towels, please?*"""

    p3 = """### Check-out & storage

*Check-out time*, *deposit*

*Can I leave my luggage here until 5 PM?*"""

    reading = "I have a reservation under the name Smith. Twin room, please. Could I have extra towels? What is the WiFi password?"
    return {
        "lesson_id": "L05_03",
        "lesson_name": "Hotel & Accommodations (Vocabulary)",
        "order": 3,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Rooms & issues", "body": p1},
                {"title": "Trang 2 — Services", "body": p2},
                {"title": "Trang 3 — Check-out", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "twin room / wake-up call / housekeeping", "vi": "phòng hai giường / báo thức / dọn phòng"},
            ],
            "examples": [
                {"english": "Can I leave my luggage here?", "vietnamese": "Tôi có thể gửi hành lý ở đây không?"},
            ],
        },
        "quizzes": [
            Q("Q_L05_03_01", 2, "multiple_choice", "Two people want **two separate beds:**", {"A": "Double room", "B": "Twin room", "C": "Single room", "D": "Suite only"}, "B", "Twin = two beds.", 9),
            Q("Q_L05_03_02", 2, "fill_in_blank", "I have a _____ under the name “Phat”.", {"A": "reservation", "B": "revolution", "C": "reservoir", "D": "resistant"}, "A", "Reservation / booking.", 9),
            Q("Q_L05_03_03", 2, "multiple_choice", "The AC is broken. You tell reception:", {"A": "The AC is not working.", "B": "The AC is working perfectly.", "C": "I love cold.", "D": "No English."}, "A", "Report the problem clearly.", 9),
            Q("Q_L05_03_04", 2, "error_identification", "Fix: “I want a wake-up calling at 7 AM.”", {"A": "want", "B": "wake-up", "C": "calling", "D": "AM"}, "C", "Wake-up call.", 11, True),
            Q("Q_L05_03_05", 3, "multiple_choice", "Match: 1. Room service — 2. Housekeeping", {"A": "1→bring food — 2→clean the room", "B": "1→clean — 2→food", "C": "1→check-in — 2→check-out", "D": "1→pool — 2→gym"}, "A", "Room service vs cleaning.", 12),
            Q("Q_L05_03_06", 1, "true_false", "You usually pay the full “deposit” when you check out only.", {"A": "True", "B": "False"}, "B", "Often paid earlier (check-in).", 9),
            Q("Q_L05_03_07", 2, "multiple_choice", "“Tôi có thể gửi hành lý ở đây không?”", {"A": "Can I leave my luggage here?", "B": "Can I live my luggage here?", "C": "Can I leaving luggage?", "D": "Luggage can here?"}, "A", "Leave luggage (store).", 10),
            Q("Q_L05_03_08", 2, "fill_in_blank", "What is the _____ password?", {"A": "WiFi", "B": "Gate", "C": "Boarding", "D": "Customs"}, "A", "WiFi password.", 9),
            Q("Q_L05_03_09", 2, "multiple_choice", "Breakfast in your room? Call:", {"A": "Housekeeping only", "B": "Room service", "C": "Police", "D": "Gate 12"}, "B", "Room service.", 9),
            Q("Q_L05_03_10", 2, "multiple_choice", "“Complimentary breakfast” means:", {"A": "Free breakfast (included)", "B": "Very expensive breakfast", "C": "No breakfast", "D": "Breakfast only for staff"}, "A", "Complimentary = free/included.", 10),
        ],
    }


def _lesson_04():
    meta = {"skill": "vocabulary", "topic": "transportation", "time_est_minutes": 25, "difficulty": 0.5}
    p1 = """### Public transport

*Subway / metro / underground*, *fare*, *one-way / round-trip (return) ticket*, *line*, *platform*"""

    p2 = """### Navigation

*GPS*, *compass*, *directions* (*turn left/right*, *go straight*)

*Which line goes to the city center?*"""

    p3 = """### Apps & tickets

*Ride-sharing* (Uber, Grab), *e-ticket*, *QR code*, *charging station*"""

    reading = "Take Line 4 to Central Station. Buy a round-trip ticket. Scan your QR code at the gate. My phone died — I need a charging station."
    return {
        "lesson_id": "L05_04",
        "lesson_name": "Getting Around - Transport (Vocabulary)",
        "order": 4,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Public transport", "body": p1},
                {"title": "Trang 2 — Navigation", "body": p2},
                {"title": "Trang 3 — Apps & tech", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "fare / platform / round-trip", "vi": "giá vé / sân ga / khứ hồi"},
            ],
            "examples": [
                {"english": "Which line goes to the museum?", "vietnamese": "Tuyến nào đi đến bảo tàng?"},
            ],
        },
        "quizzes": [
            Q("Q_L05_04_01", 2, "multiple_choice", "The price you pay for a train ride is often called the:", {"A": "Price (only)", "B": "Fare", "C": "Bill (only food)", "D": "Salary"}, "B", "Fare.", 9),
            Q("Q_L05_04_02", 2, "fill_in_blank", "Take _____ 4 to the Central Station.", {"A": "Line", "B": "Lane", "C": "Gate", "D": "Fare"}, "A", "Line 4.", 9),
            Q("Q_L05_04_03", 2, "multiple_choice", "You go and come back on one purchase:", {"A": "One-way", "B": "Round-trip / return", "C": "Farewell", "D": "Platform"}, "B", "Round-trip / return ticket.", 10),
            Q("Q_L05_04_04", 2, "multiple_choice", "More natural when you are lost in a city:", {"A": "Where is the subway station?", "B": "Where is the nearest subway station?", "C": "Subway where?", "D": "Station?"}, "B", "Nearest sounds natural.", 11),
            Q("Q_L05_04_05", 3, "multiple_choice", "Match: 1. Turn left — 2. Go straight", {"A": "1→rẽ trái — 2→đi thẳng", "B": "1→đi thẳng — 2→rẽ trái", "C": "1→turn right — 2→U-turn", "D": "1→fare — 2→platform"}, "A", "Directions vocabulary.", 12),
            Q("Q_L05_04_06", 1, "true_false", "A platform is where passengers wait for the train.", {"A": "True", "B": "False"}, "A", "Platform.", 8),
            Q("Q_L05_04_07", 2, "multiple_choice", "“Tuyến nào đi đến bảo tàng?”", {"A": "Which line goes to the museum?", "B": "Where museum is line?", "C": "Museum which line goes?", "D": "Line museum which?"}, "A", "Which line…?", 10),
            Q("Q_L05_04_08", 2, "fill_in_blank", "I need to scan my _____ code to enter.", {"A": "QR", "B": "AC", "C": "VIP", "D": "GPS"}, "A", "QR code.", 9),
            Q("Q_L05_04_09", 2, "multiple_choice", "Phone out of battery while using maps — find a:", {"A": "Platform", "B": "Charging station", "C": "Gate only", "D": "Embassy"}, "B", "Charge the phone.", 10),
            Q("Q_L05_04_10", 2, "multiple_choice", "“Miss the train” means:", {"A": "Arrive too late / lose the train", "B": "Remember the train fondly", "C": "Love trains", "D": "Buy a ticket"}, "A", "Miss = don't catch it in time.", 10),
        ],
    }


def _lesson_05():
    meta = {"skill": "vocabulary", "topic": "restaurant_dining", "time_est_minutes": 30, "difficulty": 0.45}
    p1 = """### Booking & ordering

*A table for [number]*, *menu*, *specialty*, *allergy* — *I'm allergic to peanuts.*"""

    p2 = """### At the table

*Napkin*, *cutlery* (fork, knife, spoon, chopsticks), *still / sparkling water*

*Could we have the menu, please?*"""

    p3 = """### Paying

*Bill / check*, *service charge*, *split the bill*

*Do you accept credit cards?*"""

    reading = "A table for four, please. I'm allergic to shellfish. Could I have the bill? Do you accept cards? Can we split the bill?"
    return {
        "lesson_id": "L05_05",
        "lesson_name": "Dining Out & Local Food (Vocabulary)",
        "order": 5,
        "estimated_minutes": 40,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Booking & allergies", "body": p1},
                {"title": "Trang 2 — Etiquette", "body": p2},
                {"title": "Trang 3 — Payment", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "allergy / specialty / split the bill", "vi": "dị ứng / món đặc sản / chia hóa đơn"},
            ],
            "examples": [
                {"english": "Could I have the bill, please?", "vietnamese": "Cho tôi xin hóa đơn."},
            ],
        },
        "quizzes": [
            Q("Q_L05_05_01", 2, "multiple_choice", "You enter with four people:", {"A": "A table for four, please.", "B": "I want four tables.", "C": "Four foods.", "D": "Table four is angry."}, "A", "A table for four.", 9),
            Q("Q_L05_05_02", 2, "fill_in_blank", "I am _____ to seafood.", {"A": "allergic", "B": "allergy", "C": "allergies", "D": "allow"}, "A", "Allergic to.", 9),
            Q("Q_L05_05_03", 2, "multiple_choice", "You want sparkling water:", {"A": "Still water", "B": "Sparkling water", "C": "Tap only", "D": "Soup"}, "B", "Sparkling = có gas.", 9),
            Q("Q_L05_05_04", 2, "multiple_choice", "Politer than “Give me the bill.”:", {"A": "Give me the bill.", "B": "Could I have the bill, please?", "C": "Bill now or else.", "D": "Money paper."}, "B", "Could I have… please?", 10),
            Q("Q_L05_05_05", 3, "multiple_choice", "Match: 1. Fork — 2. Chopsticks", {"A": "1→nĩa — 2→đũa", "B": "1→đũa — 2→nĩa", "C": "1→spoon — 2→knife", "D": "1→napkin — 2→menu"}, "A", "Fork vs chopsticks.", 11),
            Q("Q_L05_05_06", 1, "true_false", "“Specialty” is always a dish you find everywhere with no local link.", {"A": "True", "B": "False"}, "B", "Usually a signature/local dish.", 9),
            Q("Q_L05_05_07", 2, "multiple_choice", "“Bạn có nhận thẻ tín dụng không?”", {"A": "Do you accept credit cards?", "B": "Do you credit accept cards?", "C": "You take money card?", "D": "Cards are illegal."}, "A", "Accept credit cards.", 10),
            Q("Q_L05_05_08", 2, "fill_in_blank", "Can we _____ the bill?", {"A": "split", "B": "spit", "C": "spill", "D": "splash"}, "A", "Split the bill.", 9),
            Q("Q_L05_05_09", 2, "multiple_choice", "You want the best dish here. You ask:", {"A": "What is trash?", "B": "What is the specialty / What do you recommend?", "C": "Give worst food.", "D": "No menu."}, "B", "Recommendation / specialty.", 11),
            Q("Q_L05_05_10", 2, "multiple_choice", "“Keep the change” usually means:", {"A": "The server keeps extra money as a tip", "B": "You want all coins back", "C": "You dislike money", "D": "You cancel the bill"}, "A", "Tip / keep surplus.", 11),
        ],
    }


def _lesson_06():
    meta = {"skill": "reading", "topic": "travel_photography", "time_est_minutes": 30, "difficulty": 0.55}
    text = (
        "Prague is a paradise for photographers. To capture the best images of the Charles Bridge, you should arrive at 'the golden hour' — just before sunset. "
        "The light is soft and orange. However, remember that some museums in the city center have strict rules. "
        "You can take photos, but 'No Flash' is a common rule to protect the old paintings. "
        "If you want to use a professional tripod, you might need a special permit. "
        "Always check the signs at the entrance before you take your Sony a6400 out of the bag."
    )
    p1 = """### Pre-reading — rules

*No flash photography*, *no tripods*, *admission fee*, *guided tour*

Đọc biển báo trước khi chụp — đặc biệt trong bảo tàng."""

    p2 = """### Reading — The Golden Hour in Prague

The text links **golden hour** light, **museum rules**, and **tripod permits**."""

    p3 = """### Describing photos

*vibrant colors*, *breathtaking view*, *hidden gem*"""

    return {
        "lesson_id": "L05_06",
        "lesson_name": "Sightseeing & Photography (Reading)",
        "order": 6,
        "estimated_minutes": 42,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Signs & rules", "body": p1},
                {"title": "Trang 2 — Bài đọc", "body": p2},
                {"title": "Trang 3 — Mô tả ảnh", "body": p3},
            ],
            "reading_passage": text,
            "reading_word_count": wc(text),
            "vocabulary": [
                {"word": "golden hour / no flash", "vi": "giờ vàng chụp ảnh / cấm đèn flash"},
            ],
            "examples": [],
        },
        "quizzes": [
            Q("Q_L05_06_01", 2, "multiple_choice", "“The golden hour” is best for:", {"A": "Soft light for photos", "B": "Sleeping", "C": "Lunch only", "D": "Buying tickets"}, "A", "Just before sunset — soft light.", 10),
            Q("Q_L05_06_02", 1, "true_false", "You can always use a tripod in every Prague museum without rules.", {"A": "True", "B": "False"}, "B", "May need a permit.", 8),
            Q("Q_L05_06_03", 2, "fill_in_blank", "“No Flash” rules often protect old _____.", {"A": "paintings", "B": "bridges", "C": "tickets", "D": "fares"}, "A", "Protect old paintings.", 9),
            Q("Q_L05_06_04", 2, "multiple_choice", "Where should you check rules first?", {"A": "At the entrance (signs)", "B": "Only on social media", "C": "Never", "D": "In the restaurant"}, "A", "Check signs at the entrance.", 10),
            Q("Q_L05_06_05", 2, "fill_in_blank", "The camera model mentioned is Sony _____.", {"A": "a6400", "B": "iPhone", "C": "Gate", "D": "MRT"}, "A", "Sony a6400.", 9),
            Q("Q_L05_06_06", 2, "multiple_choice", "A “hidden gem” is usually:", {"A": "A place many tourists never find / underrated spot", "B": "Always crowded", "C": "A fake place", "D": "A gate number"}, "A", "Hidden gem.", 11),
            Q("Q_L05_06_07", 2, "multiple_choice", "The light at the golden hour is described as:", {"A": "Soft and orange", "B": "Hard and blue", "C": "Dark and purple", "D": "Loud"}, "A", "Soft and orange light.", 10),
            Q("Q_L05_06_08", 1, "true_false", "You might need a special permit to use a professional tripod in some places.", {"A": "True", "B": "False"}, "A", "Text says you might need a permit.", 9),
            Q("Q_L05_06_09", 2, "multiple_choice", "“Cảnh tượng thật tuyệt vời.” — natural English:", {"A": "The view is breathtaking / amazing.", "B": "The view is boring.", "C": "View is terrible amazing.", "D": "I boring view."}, "A", "Breathtaking / amazing.", 11),
            Q("Q_L05_06_10", 2, "fill_in_blank", "The text gives advice for _____ in Prague.", {"A": "photographers", "B": "pilots", "C": "chefs", "D": "bankers"}, "A", "Paradise for photographers.", 10),
        ],
    }


def _lesson_07():
    meta = {"skill": "vocabulary", "topic": "shopping_bargaining", "time_est_minutes": 25, "difficulty": 0.45}
    p1 = """### Prices & sizes

*How much is this?* / *How much does it cost?*

*Fitting room*, *S / M / L / XL*

*Do you have this in a larger size?*"""

    p2 = """### Bargaining

*bargain*, *pricey / expensive*, *a bit out of my budget*

*Could you give me a discount?* / *Is that your best price?*"""

    p3 = """### Refund & exchange

*receipt*, *refund*, *exchange*

*Can I exchange this if it doesn't fit?*"""

    reading = "How much is this shirt? It's a bit out of my budget. Do you have a receipt? I need a refund."
    return {
        "lesson_id": "L05_07",
        "lesson_name": "Shopping & Souvenirs (Vocabulary)",
        "order": 7,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Prices & sizes", "body": p1},
                {"title": "Trang 2 — Bargaining", "body": p2},
                {"title": "Trang 3 — Refund", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "fitting room / receipt / exchange", "vi": "phòng thử / hóa đơn / đổi hàng"},
            ],
            "examples": [
                {"english": "Is that your best price?", "vietnamese": "Đây có phải giá tốt nhất chưa?"},
            ],
        },
        "quizzes": [
            Q("Q_L05_07_01", 2, "multiple_choice", "Where you try on clothes:", {"A": "Living room", "B": "Fitting room", "C": "Kitchen", "D": "Gate"}, "B", "Fitting room.", 8),
            Q("Q_L05_07_02", 2, "fill_in_blank", "Do you have this shirt in _____ (size vừa)?", {"A": "Medium", "B": "Metal", "C": "Middle", "D": "Museum"}, "A", "Medium / M.", 9),
            Q("Q_L05_07_03", 2, "multiple_choice", "Polite when something is too expensive:", {"A": "It's too expensive! (shouting)", "B": "It's a bit out of my budget.", "C": "You are thieves.", "D": "No words."}, "B", "Softener phrase.", 10),
            Q("Q_L05_07_04", 2, "error_identification", "Fix: “I want a refunding.”", {"A": "I", "B": "want", "C": "refunding", "D": "a"}, "C", "A refund (noun).", 10, True),
            Q("Q_L05_07_05", 3, "multiple_choice", "Match: 1. Receipt — 2. Discount", {"A": "1→proof of purchase — 2→lower price", "B": "1→lower price — 2→proof", "C": "1→fitting — 2→refund", "D": "1→fare — 2→gate"}, "A", "Receipt vs discount.", 12),
            Q("Q_L05_07_06", 1, "true_false", "Heavy bargaining is usual in most big supermarkets.", {"A": "True", "B": "False"}, "B", "More common in markets.", 8),
            Q("Q_L05_07_07", 2, "multiple_choice", "“Đây có phải là giá tốt nhất của bạn chưa?”", {"A": "Is that your best price?", "B": "Is your best that price?", "C": "Best price is what?", "D": "Price best your?"}, "A", "Is that your best price?", 10),
            Q("Q_L05_07_08", 2, "fill_in_blank", "I would like to _____ this for a smaller one.", {"A": "exchange", "B": "excuse", "C": "excited", "D": "exhaust"}, "A", "Exchange for another size.", 9),
            Q("Q_L05_07_09", 2, "multiple_choice", "You want souvenirs for friends. You look for a:", {"A": "Souvenir shop", "B": "Pharmacy", "C": "Emergency room", "D": "Embassy"}, "A", "Souvenir shop.", 9),
            Q("Q_L05_07_10", 2, "multiple_choice", "“Buy one get one free” means:", {"A": "Buy one item, get another free", "B": "Buy one, pay double", "C": "No shopping", "D": "Only online"}, "A", "BOGO promotion.", 10),
        ],
    }


def _lesson_08():
    meta = {"skill": "vocabulary", "topic": "emergencies", "time_est_minutes": 25, "difficulty": 0.55}
    p1 = """### Lost items

*Lost and found*, *stolen*, *pickpocket*

*My wallet has been stolen!*"""

    p2 = """### Medical

*pharmacy*, *prescription*, *emergency room*

*I need to see a doctor immediately.*"""

    p3 = """### Police & embassy

*police station*, *report*, *embassy*

*I lost my passport. Where is the Vietnamese Embassy?*"""

    reading = "I left my bag on the train. Go to Lost and Found. My wallet was stolen — report at the police station."
    return {
        "lesson_id": "L05_08",
        "lesson_name": "Emergency Situations (Vocabulary)",
        "order": 8,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Lost & theft", "body": p1},
                {"title": "Trang 2 — Medical", "body": p2},
                {"title": "Trang 3 — Police & embassy", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "stolen / pickpocket / embassy", "vi": "bị trộm / móc túi / đại sứ quán"},
            ],
            "examples": [
                {"english": "I'm lost. Can you help me?", "vietnamese": "Tôi bị lạc. Bạn giúp tôi được không?"},
            ],
        },
        "quizzes": [
            Q("Q_L05_08_01", 2, "multiple_choice", "You forgot your bag on the train. First try:", {"A": "Pharmacy", "B": "Lost and Found", "C": "Restaurant menu", "D": "Duty-free"}, "B", "Lost and Found desk.", 9),
            Q("Q_L05_08_02", 2, "fill_in_blank", "Help! My bag has been _____.", {"A": "stolen", "B": "stole", "C": "steal", "D": "stealing"}, "A", "Has been stolen.", 9),
            Q("Q_L05_08_03", 2, "multiple_choice", "Pickpockets are more common in:", {"A": "Crowded places", "B": "Empty libraries only", "C": "Underwater", "D": "Private homes only"}, "A", "Crowds.", 9),
            Q("Q_L05_08_04", 2, "error_identification", "More natural: “Where is the pharmacy store?”", {"A": "Where", "B": "is", "C": "pharmacy store", "D": "the"}, "C", "Where is the pharmacy? (drop *store*)", 11, True),
            Q("Q_L05_08_05", 3, "multiple_choice", "Match: 1. Wallet — 2. Passport", {"A": "1→money & cards — 2→ID / travel ID", "B": "1→ID — 2→money only", "C": "1→ticket — 2→meal", "D": "1→souvenir — 2→receipt"}, "A", "Typical contents/role.", 12),
            Q("Q_L05_08_06", 1, "true_false", "You usually go to the embassy only because you lost your phone game.", {"A": "True", "B": "False"}, "B", "Embassy for passport/legal help.", 9),
            Q("Q_L05_08_07", 2, "multiple_choice", "“Tôi bị lạc đường. Bạn giúp tôi được không?”", {"A": "I'm lost. Can you help me?", "B": "I lost. Can you help I?", "C": "I am lose. Help?", "D": "Lost I am help?"}, "A", "I'm lost.", 10),
            Q("Q_L05_08_08", 2, "fill_in_blank", "I have a severe headache. I need some _____.", {"A": "medicine", "B": "luggage", "C": "gate", "D": "fare"}, "A", "Medicine / painkillers.", 9),
            Q("Q_L05_08_09", 2, "multiple_choice", "Common emergency numbers in many countries (examples):", {"A": "911 / 112 (region-dependent)", "B": "12345 only for pizza", "C": "000 only for weather", "D": "No emergency numbers"}, "A", "Know local emergency number.", 11),
            Q("Q_L05_08_10", 2, "multiple_choice", "“Immediately” means:", {"A": "Right away", "B": "Later", "C": "Never", "D": "Tomorrow only"}, "A", "Immediately = at once.", 8),
        ],
    }


def _lesson_09():
    meta = {"skill": "speaking", "topic": "socializing_travel", "time_est_minutes": 25, "difficulty": 0.5}
    p1 = """### Breaking the ice

*Is anyone sitting here?*

*Where are you from?* / *How long have you been here?*

*Do you travel alone or with friends?*"""

    p2 = """### Sharing experiences

*What's your favorite place so far?*

*You should try the local coffee — it's amazing!*

*I'm a photographer — I love the architecture here.*"""

    p3 = """### Staying in touch

*Are you on Instagram?*

*Let's exchange contacts.*

*Have a safe trip!*"""

    reading = "Hi, is anyone sitting here? Where are you from? I'm from Vietnam. Let's exchange Instagram. Have a safe trip!"
    return {
        "lesson_id": "L05_09",
        "lesson_name": "Making Friends & Socializing (Speaking)",
        "order": 9,
        "estimated_minutes": 35,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Breaking the ice", "body": p1},
                {"title": "Trang 2 — Sharing", "body": p2},
                {"title": "Trang 3 — Contacts", "body": p3},
            ],
            "reading_passage": reading,
            "reading_word_count": wc(reading),
            "vocabulary": [
                {"word": "so far / exchange contacts", "vi": "cho đến nay / trao đổi liên lạc"},
            ],
            "examples": [
                {"english": "Have a safe trip!", "vietnamese": "Chúc bạn chuyến đi an toàn!"},
            ],
        },
        "quizzes": [
            Q("Q_L05_09_01", 2, "multiple_choice", "At a hostel, a friendly opener:", {"A": "Hi, where are you from?", "B": "Give me your password.", "C": "Money now.", "D": "Go away."}, "A", "Small talk.", 9),
            Q("Q_L05_09_02", 2, "fill_in_blank", "Is anyone _____ here?", {"A": "sitting", "B": "sit", "C": "sat", "D": "seats"}, "A", "Is anyone sitting here?", 9),
            Q("Q_L05_09_03", 2, "multiple_choice", "Recommend a restaurant:", {"A": "Go there. (rude tone)", "B": "You should try that restaurant — the food is great.", "C": "Food bad.", "D": "Don't eat."}, "B", "You should try…", 10),
            Q("Q_L05_09_04", 2, "multiple_choice", "Better question about time since arrival:", {"A": "How long are you here?", "B": "How long have you been here?", "C": "How you long?", "D": "Long how?"}, "B", "Present perfect + been.", 11),
            Q("Q_L05_09_05", 3, "multiple_choice", "Match: 1. Solo traveler — 2. Group traveler", {"A": "1→alone — 2→with friends", "B": "1→with friends — 2→alone", "C": "1→twin room — 2→single", "D": "1→fare — 2→gate"}, "A", "Solo vs group.", 12),
            Q("Q_L05_09_06", 1, "true_false", "“Break the ice” means starting a conversation.", {"A": "True", "B": "False"}, "A", "Idiom.", 8),
            Q("Q_L05_09_07", 2, "multiple_choice", "“Bạn có dùng Instagram không?”", {"A": "Are you on Instagram?", "B": "Are you in Instagram?", "C": "You Instagram are?", "D": "Instagram you have?"}, "A", "On Instagram.", 9),
            Q("Q_L05_09_08", 2, "fill_in_blank", "Let's _____ contacts.", {"A": "exchange", "B": "excuse", "C": "excited", "D": "exhaust"}, "A", "Exchange contacts.", 9),
            Q("Q_L05_09_09", 2, "multiple_choice", "Saying goodbye to a new travel friend:", {"A": "Have a safe trip! / Hope to see you again!", "B": "Never speak.", "C": "Delete me.", "D": "I hate you."}, "A", "Polite farewell.", 10),
            Q("Q_L05_09_10", 2, "multiple_choice", "In “What's your favorite place so far?”, “so far” means:", {"A": "Up to now", "B": "Very far away", "C": "Never", "D": "Tomorrow"}, "A", "So far = until now.", 9),
        ],
    }


def _lesson_10():
    meta = {"skill": "reading", "topic": "travel_reviews", "time_est_minutes": 35, "difficulty": 0.6}
    text = (
        "I recently stayed at a boutique hotel in Singapore. It was a great value for money. The location was perfect, right next to the MRT station. "
        "The staff were very helpful when I lost my camera's lens cap. However, the famous rooftop pool was a bit overrated because it was too crowded. "
        "If you are a photographer, I highly recommend visiting the Gardens by the Bay at night. The light show is breathtaking and perfect for long-exposure shots."
    )
    p1 = """### Review vocabulary

*highly recommend*, *overrated*, *value for money*, *disappointing*"""

    p2 = """### Reading — Singapore stay

Note: *value for money*, *overrated pool*, *Gardens by the Bay*, *breathtaking* light show."""

    p3 = """### Writing a review (structure)

Intro → **The good** → **The bad** → Conclusion (Would you go back?)"""

    return {
        "lesson_id": "L05_10",
        "lesson_name": "Travel Vlogs & Reviews (Reading/Writing)",
        "order": 10,
        "estimated_minutes": 48,
        "metadata": meta,
        "content": {
            "theory": "",
            "theory_pages": [
                {"title": "Trang 1 — Review words", "body": p1},
                {"title": "Trang 2 — Bài đọc", "body": p2},
                {"title": "Trang 3 — Cấu trúc viết review", "body": p3},
            ],
            "reading_passage": text,
            "reading_word_count": wc(text),
            "vocabulary": [
                {"word": "overrated / value for money", "vi": "bị tâng quá / đáng tiền"},
            ],
            "examples": [
                {"english": "I would definitely go back.", "vietnamese": "Tôi chắc chắn sẽ quay lại."},
            ],
        },
        "quizzes": [
            Q("Q_L05_10_01", 2, "multiple_choice", "“Value for money” means:", {"A": "Very expensive", "B": "Good quality for the price", "C": "Free", "D": "No money"}, "B", "Worth what you pay.", 9),
            Q("Q_L05_10_02", 1, "true_false", "The writer loved everything about the rooftop pool.", {"A": "True", "B": "False"}, "B", "Overrated / too crowded.", 8),
            Q("Q_L05_10_03", 2, "fill_in_blank", "I highly _____ this hotel.", {"A": "recommend", "B": "recommendation", "C": "recommended", "D": "recommending"}, "A", "Highly recommend.", 9),
            Q("Q_L05_10_04", 2, "multiple_choice", "Why was the pool “overrated” for the writer?", {"A": "Too crowded", "B": "Too cold", "C": "No water", "D": "Closed forever"}, "A", "Too crowded.", 9),
            Q("Q_L05_10_05", 2, "fill_in_blank", "Photographers should visit Gardens by the Bay at _____.", {"A": "night", "B": "noon", "C": "dawn", "D": "never"}, "A", "At night.", 9),
            Q("Q_L05_10_06", 2, "multiple_choice", "A “lens cap” belongs to a:", {"A": "Camera", "B": "Phone app", "C": "Suitcase", "D": "Boarding pass"}, "A", "Camera lens cap.", 9),
            Q("Q_L05_10_07", 2, "multiple_choice", "Which word in the text describes the light show most positively?", {"A": "Overrated", "B": "Breathtaking", "C": "Crowded", "D": "However"}, "B", "Breathtaking.", 9),
            Q("Q_L05_10_08", 1, "true_false", "The hotel was far from the MRT station.", {"A": "True", "B": "False"}, "B", "Right next to the MRT.", 9),
            Q("Q_L05_10_09", 2, "multiple_choice", "“Tôi chắc chắn sẽ quay lại.”", {"A": "I would definitely go back.", "B": "I go definitely back would.", "C": "Definitely I go.", "D": "I back go definitely."}, "A", "Would definitely go back.", 10),
            Q("Q_L05_10_10", 2, "fill_in_blank", "The text is a _____ of a travel experience.", {"A": "review", "B": "recipe", "C": "ticket", "D": "visa"}, "A", "Hotel / travel review.", 9),
        ],
    }
