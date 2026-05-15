import { Link } from "react-router-dom";

const FEATURES = [
  { icon: "🤖", title: "AI gợi ý cá nhân hóa", desc: "Hệ thống machine learning phân tích hành vi học tập và gợi ý bài học phù hợp trình độ của từng người." },
  { icon: "📊", title: "Phân tích tiến độ chi tiết", desc: "Dashboard theo dõi tiến độ theo kỹ năng, điểm số, thời gian học và xu hướng cải thiện theo thời gian." },
  { icon: "🎯", title: "Lộ trình có hệ thống", desc: "Nội dung được sắp xếp theo chuẩn CEFR từ A1 đến C2, đảm bảo học đúng trình tự và hiệu quả." },
  { icon: "🔬", title: "MLflow & Data Science", desc: "Mô hình ML được train và theo dõi qua MLflow, liên tục cải thiện dựa trên dữ liệu thực từ hàng trăm người học." },
];

const TEAM = [
  { name: "Nhóm phát triển", role: "IUH K18 — HK2 N4", desc: "Xây dựng hệ thống trong khuôn khổ đồ án môn Công nghệ mới." },
  { name: "Công nghệ sử dụng", role: "Tech Stack", desc: "Django REST Framework · React 19 · MLflow · scikit-learn · Chart.js · JWT Authentication" },
];

export function AboutInAppPage() {
  return (
    <div className="stack about-inapp-page">
      <div className="about-hero-banner">
        <div className="about-hero-content">
          <div className="about-hero-badge">🎓 Về hệ thống</div>
          <h1 className="about-hero-title">TOEIC Learning Platform</h1>
          <p className="about-hero-sub">
            Nền tảng học tiếng Anh thông minh kết hợp Machine Learning để cá nhân hóa lộ trình học cho từng người dùng.
          </p>
          <div className="row" style={{ marginTop: 8 }}>
            <Link to="/courses" className="btn">Khóa học của tôi</Link>
            <Link to="/dashboard" className="btn btn-secondary" style={{ color: "#fff", borderColor: "rgba(255,255,255,.5)", background: "rgba(255,255,255,.15)" }}>Xem Dashboard</Link>
          </div>
        </div>
      </div>

      <div>
        <h2 className="about-section-title">Tính năng nổi bật</h2>
        <div className="about-features-grid">
          {FEATURES.map((f) => (
            <div key={f.title} className="about-feature-card card">
              <div className="about-feature-icon">{f.icon}</div>
              <h3 className="about-feature-title">{f.title}</h3>
              <p className="muted small" style={{ margin: 0 }}>{f.desc}</p>
            </div>
          ))}
        </div>
      </div>

      <div>
        <h2 className="about-section-title">Thông tin dự án</h2>
        <div className="about-team-grid">
          {TEAM.map((t) => (
            <div key={t.name} className="about-team-card card">
              <div className="about-team-name">{t.name}</div>
              <div className="about-team-role">{t.role}</div>
              <p className="muted small" style={{ margin: "8px 0 0" }}>{t.desc}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="card about-stats-card">
        <h2 className="about-section-title" style={{ margin: "0 0 16px" }}>Thống kê hệ thống</h2>
        <div className="about-stats-row">
          <div className="about-stat"><span className="about-stat-num">6+</span><span className="about-stat-label">Kỹ năng TOEIC</span></div>
          <div className="about-stat"><span className="about-stat-num">A1→C2</span><span className="about-stat-label">Cấp độ CEFR</span></div>
          <div className="about-stat"><span className="about-stat-num">ML</span><span className="about-stat-label">AI gợi ý</span></div>
          <div className="about-stat"><span className="about-stat-num">500+</span><span className="about-stat-label">Dữ liệu học tập</span></div>
        </div>
      </div>
    </div>
  );
}
