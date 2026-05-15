import { Link } from "react-router-dom";

const ROADMAP = [
  {
    level: "A1–A2",
    cefr: "Sơ cấp",
    color: "linear-gradient(135deg,#10b981,#059669)",
    skills: ["Từ vựng cơ bản 500–1000 từ", "Ngữ pháp nền tảng", "Nghe câu đơn giản", "Đọc đoạn văn ngắn"],
    goal: "Giao tiếp cơ bản, giới thiệu bản thân",
  },
  {
    level: "B1–B2",
    cefr: "Trung cấp",
    color: "linear-gradient(135deg,#0ea5e9,#4f46e5)",
    skills: ["Từ vựng học thuật 3000+ từ", "Ngữ pháp nâng cao", "Nghe podcast, tin tức", "Đọc báo tiếng Anh"],
    goal: "TOEIC 550–750, giao tiếp lưu loát",
  },
  {
    level: "C1–C2",
    cefr: "Cao cấp",
    color: "linear-gradient(135deg,#f59e0b,#ef4444)",
    skills: ["Từ vựng học thuật & chuyên ngành", "Viết luận, báo cáo", "Nghe hội thảo, bài giảng", "Đọc tài liệu học thuật"],
    goal: "TOEIC 800+, làm việc trong môi trường quốc tế",
  },
];

const TOEIC_TIPS = [
  { icon: "🎧", title: "Listening", desc: "Luyện nghe hàng ngày 20–30 phút, tập trung vào Part 3 và Part 4." },
  { icon: "📖", title: "Reading", desc: "Đọc đoạn văn dài, chú ý từ vựng ngữ cảnh và cấu trúc câu phức." },
  { icon: "📝", title: "Ngữ pháp", desc: "Nắm vững 12 thì, câu bị động, mệnh đề quan hệ." },
  { icon: "📚", title: "Từ vựng", desc: "Học 10–20 từ mới mỗi ngày theo chủ đề: Văn phòng, Tài chính, Du lịch." },
];

export function RoadmapPage() {
  return (
    <div className="stack roadmap-page">
      <div>
        <h1 className="page-title">Lộ trình học tiếng Anh</h1>
        <p className="muted">Lộ trình học được thiết kế phù hợp với từng cấp độ, giúp bạn tiến bộ có hệ thống.</p>
      </div>

      <div className="roadmap-levels">
        {ROADMAP.map((r, i) => (
          <div key={r.level} className="roadmap-level-card">
            <div className="roadmap-level-banner" style={{ background: r.color }}>
              <div className="roadmap-level-step">Giai đoạn {i + 1}</div>
              <div className="roadmap-level-name">{r.level}</div>
              <div className="roadmap-level-cefr">{r.cefr}</div>
            </div>
            <div className="roadmap-level-body">
              <ul className="roadmap-skill-list">
                {r.skills.map((s) => (
                  <li key={s}><span className="roadmap-check">✓</span> {s}</li>
                ))}
              </ul>
              <div className="roadmap-goal">
                <strong>Mục tiêu:</strong> {r.goal}
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="roadmap-tips-section">
        <h2 className="roadmap-section-title">Tips học hiệu quả</h2>
        <div className="roadmap-tips-grid">
          {TOEIC_TIPS.map((t) => (
            <div key={t.title} className="roadmap-tip-card card">
              <div className="roadmap-tip-icon">{t.icon}</div>
              <div className="roadmap-tip-title">{t.title}</div>
              <p className="roadmap-tip-desc muted small">{t.desc}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="roadmap-cta card">
        <h2>Sẵn sàng bắt đầu?</h2>
        <p className="muted">Hệ thống AI sẽ gợi ý khóa học phù hợp nhất dựa trên trình độ và tiến độ của bạn.</p>
        <div className="row">
          <Link to="/courses" className="btn">Xem khóa học</Link>
          <Link to="/dashboard" className="btn btn-secondary">Xem Dashboard</Link>
        </div>
      </div>
    </div>
  );
}
