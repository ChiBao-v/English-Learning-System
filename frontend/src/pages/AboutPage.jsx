import { SiteHeader } from "../components/SiteHeader.jsx";

export function AboutPage() {
  return (
    <div className="public-page">
      <SiteHeader />
      <main className="public-main about-main">
        <article className="card about-card">
          <h1>Về chúng tôi</h1>
          <p>
            TOEIC Learning là nền tảng học tiếng Anh hướng TOEIC, kết hợp phân tích hành vi học tập gần real-time và
            gợi ý lộ trình cá nhân hóa nhờ machine learning.
          </p>
          <p className="muted">
            Hệ thống ghi nhận thời gian làm bài, thói quen đổi đáp án, mức dùng gợi ý và tiến độ từng bài để đề xuất
            nội dung phù hợp trình độ của bạn.
          </p>
        </article>
      </main>
    </div>
  );
}
