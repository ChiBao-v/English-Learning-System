import { Link } from "react-router-dom";

export function LessonSidebar({ courseLessons, lessonId, courseTitle }) {
  const total = courseLessons.length;
  const done = courseLessons.filter((r) => r.completed).length;
  const progressPct = total > 0 ? Math.round((done / total) * 100) : 0;
  const continueId = courseLessons.find((row) => !row.completed)?.id ?? null;

  return (
    <aside className="lesson-sidebar">
      {courseTitle && (
        <div className="sidebar-course-header">
          <div className="sidebar-course-title">{courseTitle}</div>
          <div className="sidebar-course-progress-row">
            <span className="sidebar-course-progress-label">{done}/{total} bài</span>
            <span className="sidebar-course-progress-pct">{progressPct}%</span>
          </div>
          <div className="progress-bar sidebar-progress-bar">
            <div className="progress-bar-fill" style={{ width: `${progressPct}%` }} />
          </div>
        </div>
      )}

      <div className="sidebar-section-title">DANH SÁCH BÀI HỌC</div>
      <ul className="lesson-nav-list">
        {courseLessons.map((row, idx) => {
          const num = idx + 1;
          const active = row.id === Number(lessonId);
          const isDone = row.completed;
          const isNext = !isDone && row.id === continueId;

          const cls = ["lesson-nav-item"];
          if (active) cls.push("lesson-nav-item--active");
          if (isDone) cls.push("lesson-nav-item--done");
          else if (isNext) cls.push("lesson-nav-item--next");

          const icon = isDone ? "✓" : active ? "▶" : isNext ? "→" : "○";

          return (
            <li key={row.id}>
              {active ? (
                <span
                  className={cls.join(" ")}
                  title={isDone ? "Đã hoàn thành" : isNext ? "Bài đang học dở" : "Bài hiện tại"}
                >
                  <span className="lesson-nav-icon" aria-hidden>{icon}</span>
                  <span className="lesson-nav-num">{num}.</span>
                  <span className="lesson-nav-title">{row.title}</span>
                </span>
              ) : (
                <Link
                  className={cls.join(" ")}
                  to={`/lessons/${row.id}`}
                  title={isDone ? "Đã hoàn thành" : isNext ? "Tiếp tục học bài này" : ""}
                >
                  <span className="lesson-nav-icon" aria-hidden>{icon}</span>
                  <span className="lesson-nav-num">{num}.</span>
                  <span className="lesson-nav-title">{row.title}</span>
                </Link>
              )}
            </li>
          );
        })}
      </ul>

      {total > 0 && (
        <div className="sidebar-footer">
          <Link to="/courses" className="sidebar-back-link">← Quay lại khóa học</Link>
        </div>
      )}
    </aside>
  );
}
