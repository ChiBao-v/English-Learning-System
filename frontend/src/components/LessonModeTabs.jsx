import { NavLink } from "react-router-dom";

export function LessonModeTabs({ lessonId, quizTabLabel = "Quiz" }) {
  const base = `/lessons/${lessonId}`;
  return (
    <div className="lesson-mode-tabs" role="tablist" aria-label="Chế độ bài học">
      <NavLink to={base} end className={({ isActive }) => `lesson-mode-tab${isActive ? " lesson-mode-tab--active" : ""}`}>
        Tài liệu
      </NavLink>
      <NavLink
        to={`${base}/quiz`}
        className={({ isActive }) => `lesson-mode-tab${isActive ? " lesson-mode-tab--active" : ""}`}
      >
        {quizTabLabel}
      </NavLink>
    </div>
  );
}
