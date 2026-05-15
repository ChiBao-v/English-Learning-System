import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { SiteHeader } from "../components/SiteHeader.jsx";
import { useAuth } from "../context/useAuth.js";
import { getPublicCoursesApi } from "../services/api.js";
import { shortCourseDescription } from "../utils/courseDisplay.js";

const LEVEL_VI = { beginner: "Cơ bản", intermediate: "Trung cấp", advanced: "Nâng cao" };

const SKILL_COLORS = {
  listening: "linear-gradient(135deg,#4f46e5 0%,#7c3aed 100%)",
  reading:   "linear-gradient(135deg,#0ea5e9 0%,#06b6d4 100%)",
  writing:   "linear-gradient(135deg,#10b981 0%,#059669 100%)",
  speaking:  "linear-gradient(135deg,#f59e0b 0%,#ef4444 100%)",
  general:   "linear-gradient(135deg,#64748b 0%,#475569 100%)",
};

const FEATURES = [
  { icon: "🎯", title: "AI cá nhân hóa", desc: "Hệ thống phân tích hành vi học tập và gợi ý bài phù hợp với bạn." },
  { icon: "📊", title: "Theo dõi tiến độ", desc: "Dashboard hiển thị độ chính xác, thời gian học và biểu đồ kỹ năng." },
  { icon: "🎧", title: "6 kỹ năng", desc: "Listening, Reading, Writing, Speaking, Grammar và Vocabulary." },
  { icon: "⚡", title: "Học ngay lập tức", desc: "Không cần cài đặt — đăng ký và bắt đầu học trong 30 giây." },
];

export function HomePage() {
  const { isAuthenticated } = useAuth();
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;
    (async () => {
      try {
        const data = await getPublicCoursesApi();
        if (mounted) setCourses(Array.isArray(data) ? data : data.results || []);
      } catch (_) {
        /* silent */
      } finally {
        if (mounted) setLoading(false);
      }
    })();
    return () => { mounted = false; };
  }, []);

  const featured = courses.filter(c => c.lesson_count > 0).slice(0, 6);
  const ctaTo = isAuthenticated ? "/courses" : "/login";

  return (
    <div className="public-page">
      <SiteHeader />

      <main className="public-main">
        {/* HERO */}
        <section className="hero-section">
          <div className="hero-badge">🚀 Học tiếng Anh theo AI</div>
          <h1 className="hero-title">Nâng trình tiếng Anh<br />thông minh hơn</h1>
          <p className="hero-sub">
            Hệ thống phân tích hành vi học tập, gợi ý bài cá nhân hóa và theo dõi 6 kỹ năng theo thời gian thực.
          </p>
          <div className="hero-cta-row">
            <Link to={ctaTo} className="btn hero-cta">
              {isAuthenticated ? "Vào học ngay →" : "Bắt đầu miễn phí →"}
            </Link>
            {!isAuthenticated && (
              <Link to="/login" className="btn btn-secondary" style={{ padding: "13px 24px" }}>
                Đăng nhập
              </Link>
            )}
          </div>
          <div className="hero-stats">
            <div className="hero-stat"><div className="hero-stat-num">6</div><div className="hero-stat-label">Kỹ năng</div></div>
            <div className="hero-stat"><div className="hero-stat-num">24+</div><div className="hero-stat-label">Bài học</div></div>
            <div className="hero-stat"><div className="hero-stat-num">400+</div><div className="hero-stat-label">Câu hỏi</div></div>
            <div className="hero-stat"><div className="hero-stat-num">AI</div><div className="hero-stat-label">Gợi ý</div></div>
          </div>
        </section>

        {/* FEATURES */}
        <section id="tinh-nang" style={{ marginBottom: 72, scrollMarginTop: 80 }}>
          <div className="section-header">
            <h2 className="section-title">Tính năng nổi bật</h2>
            <p className="section-sub">Tất cả những gì bạn cần để học tiếng Anh hiệu quả, được hỗ trợ bởi AI và phân tích dữ liệu.</p>
          </div>
          <div style={{ display: "grid", gap: 16, gridTemplateColumns: "repeat(auto-fill,minmax(220px,1fr))" }}>
            {FEATURES.map((f) => (
              <div key={f.title} className="card" style={{ padding: 20 }}>
                <div style={{ fontSize: "1.8rem", marginBottom: 10 }}>{f.icon}</div>
                <div style={{ fontWeight: 700, marginBottom: 6 }}>{f.title}</div>
                <p className="muted small" style={{ margin: 0, lineHeight: 1.6 }}>{f.desc}</p>
              </div>
            ))}
          </div>

          <div style={{ display: "grid", gap: 16, gridTemplateColumns: "repeat(auto-fill,minmax(260px,1fr))", marginTop: 24 }}>
            {[
              { icon: "🧠", title: "Mô hình ML dự đoán trình độ", desc: "RandomForest phân loại CEFR (A1–C2) dựa trên hành vi học và độ chính xác bài làm." },
              { icon: "📈", title: "MLflow tracking", desc: "Mỗi lần retrain đều ghi log experiment, accuracy, f1-score để so sánh phiên bản." },
              { icon: "🗺️", title: "Lộ trình thông minh", desc: "Hệ thống đề xuất bài tiếp theo theo điểm yếu kỹ năng của bạn." },
              { icon: "🔁", title: "Học lại theo Spaced Repetition", desc: "Câu sai được lặp lại có chu kỳ để ghi nhớ dài hạn hiệu quả hơn." },
              { icon: "🏆", title: "Bảng xếp hạng & thành tích", desc: "Thi đua điểm số, streak ngày học liên tiếp và huy hiệu khi đạt mốc." },
              { icon: "🌙", title: "Học mọi lúc, mọi thiết bị", desc: "Responsive cho mobile, tablet, desktop. Tiến độ đồng bộ tự động." },
            ].map((f) => (
              <div key={f.title} className="card" style={{ padding: 20 }}>
                <div style={{ fontSize: "1.8rem", marginBottom: 10 }}>{f.icon}</div>
                <div style={{ fontWeight: 700, marginBottom: 6 }}>{f.title}</div>
                <p className="muted small" style={{ margin: 0, lineHeight: 1.6 }}>{f.desc}</p>
              </div>
            ))}
          </div>
        </section>

        {/* COURSES */}
        <section id="khoa-hoc-noi-bat" className="featured-section">
          <div className="section-header">
            <h2 className="section-title">Khóa học nổi bật</h2>
            <p className="section-sub">Nội dung từ British Council, được chuẩn hóa cho hệ thống học thông minh.</p>
          </div>
          {loading ? (
            <p className="muted">Đang tải khóa học...</p>
          ) : (
            <div className="featured-grid">
              {featured.map((course) => {
                const blurb = shortCourseDescription(course.description, 100);
                const bg = course.thumbnail
                  ? { backgroundImage: `url(${course.thumbnail})` }
                  : { background: SKILL_COLORS[course.skill] || SKILL_COLORS.general };
                return (
                  <article key={course.id} className="course-card">
                    <div className="course-card-image" style={bg}>
                      {course.cefr_level && (
                        <span className="course-card-skill-badge">{course.cefr_level}</span>
                      )}
                    </div>
                    <div className="course-card-body">
                      <h3 className="course-card-title">{course.title}</h3>
                      <p className="course-card-tier">{course.level_label || LEVEL_VI[course.level] || course.level}</p>
                      {blurb ? <p className="course-card-blurb">{blurb}</p> : null}
                      <p className="course-card-meta">{course.lesson_count ?? 0} bài học</p>
                      <Link to={ctaTo} className="btn btn-secondary btn-block btn-sm" style={{ marginTop: "auto" }}>
                        Xem chi tiết
                      </Link>
                    </div>
                  </article>
                );
              })}
            </div>
          )}
          <div style={{ textAlign: "center", marginTop: 28 }}>
            <Link to={ctaTo} className="btn btn-secondary">
              Xem tất cả khóa học →
            </Link>
          </div>
        </section>

        {/* CONTACT */}
        <section id="lien-he" className="featured-section" style={{ scrollMarginTop: 80 }}>
          <div className="section-header">
            <h2 className="section-title">Liên hệ với chúng tôi</h2>
            <p className="section-sub">Có câu hỏi, góp ý hay muốn hợp tác? Đội ngũ LearnEnglish luôn sẵn sàng hỗ trợ bạn.</p>
          </div>

          <div style={{ display: "grid", gap: 20, gridTemplateColumns: "1.2fr 1fr", alignItems: "start" }}>
            <div className="card" style={{ padding: 28 }}>
              <h3 style={{ marginTop: 0, marginBottom: 16 }}>Gửi tin nhắn cho chúng tôi</h3>
              <form onSubmit={(e) => { e.preventDefault(); alert("Cảm ơn bạn! Chúng tôi sẽ phản hồi qua email trong vòng 24 giờ."); }}>
                <div className="form-group" style={{ marginBottom: 14 }}>
                  <label style={{ display: "block", marginBottom: 6, fontWeight: 500 }}>Họ và tên</label>
                  <input type="text" required placeholder="Nguyễn Văn A" style={{ width: "100%", padding: 10, border: "1px solid #dee2e6", borderRadius: 6 }} />
                </div>
                <div className="form-group" style={{ marginBottom: 14 }}>
                  <label style={{ display: "block", marginBottom: 6, fontWeight: 500 }}>Email</label>
                  <input type="email" required placeholder="ban@example.com" style={{ width: "100%", padding: 10, border: "1px solid #dee2e6", borderRadius: 6 }} />
                </div>
                <div className="form-group" style={{ marginBottom: 14 }}>
                  <label style={{ display: "block", marginBottom: 6, fontWeight: 500 }}>Chủ đề</label>
                  <select style={{ width: "100%", padding: 10, border: "1px solid #dee2e6", borderRadius: 6 }}>
                    <option>Hỏi về khóa học</option>
                    <option>Báo lỗi kỹ thuật</option>
                    <option>Đề xuất tính năng</option>
                    <option>Hợp tác kinh doanh</option>
                    <option>Khác</option>
                  </select>
                </div>
                <div className="form-group" style={{ marginBottom: 16 }}>
                  <label style={{ display: "block", marginBottom: 6, fontWeight: 500 }}>Nội dung</label>
                  <textarea required rows={5} placeholder="Hãy chia sẻ thắc mắc của bạn..." style={{ width: "100%", padding: 10, border: "1px solid #dee2e6", borderRadius: 6, fontFamily: "inherit" }} />
                </div>
                <button type="submit" className="btn">Gửi tin nhắn</button>
              </form>
            </div>

            <div className="stack" style={{ gap: 14 }}>
              <div className="card" style={{ padding: 20 }}>
                <div style={{ fontSize: "1.6rem", marginBottom: 8 }}>📧</div>
                <div style={{ fontWeight: 700, marginBottom: 4 }}>Email</div>
                <p className="muted small" style={{ margin: 0 }}>support@learnenglish.vn<br />partners@learnenglish.vn</p>
              </div>
              <div className="card" style={{ padding: 20 }}>
                <div style={{ fontSize: "1.6rem", marginBottom: 8 }}>📞</div>
                <div style={{ fontWeight: 700, marginBottom: 4 }}>Hotline</div>
                <p className="muted small" style={{ margin: 0 }}>(+84) 28 1234 5678<br />T2–T7: 8:00 — 18:00</p>
              </div>
              <div className="card" style={{ padding: 20 }}>
                <div style={{ fontSize: "1.6rem", marginBottom: 8 }}>📍</div>
                <div style={{ fontWeight: 700, marginBottom: 4 }}>Văn phòng</div>
                <p className="muted small" style={{ margin: 0 }}>12 Nguyễn Văn Bảo, Phường 4,<br />Q. Gò Vấp, TP. Hồ Chí Minh</p>
              </div>
              <div className="card" style={{ padding: 20 }}>
                <div style={{ fontSize: "1.6rem", marginBottom: 8 }}>💬</div>
                <div style={{ fontWeight: 700, marginBottom: 4 }}>Mạng xã hội</div>
                <p className="muted small" style={{ margin: 0 }}>Facebook · YouTube · TikTok<br />@learnenglish.vn</p>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="public-footer">
        <p className="muted small">© {new Date().getFullYear()} LearnEnglish Analytics — Học tiếng Anh thông minh cùng AI</p>
      </footer>
    </div>
  );
}
