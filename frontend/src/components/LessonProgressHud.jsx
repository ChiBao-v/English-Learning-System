function formatClock(totalSeconds) {
  const m = Math.floor(totalSeconds / 60);
  const s = totalSeconds % 60;
  return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

/**
 * Thanh tiến độ góc phải: % khóa, thời gian, điểm/độ chính xác (tùy chế độ).
 */
export function LessonProgressHud({ mode, courseProgressPct, elapsedSec, quizProgressPct, scorePct }) {
  const pctLabel = mode === "study" ? "Tiến độ khóa" : "Tiến độ quiz";
  const pctValue = mode === "study" ? courseProgressPct ?? 0 : quizProgressPct ?? 0;
  const scoreLabel = mode === "study" ? "Quiz" : "Đúng (ước lượng)";
  const scoreValue = mode === "study" ? "—" : scorePct != null ? `${scorePct}%` : "—";

  return (
    <aside className="lesson-progress-hud" aria-label="Tiến độ học">
      <div className="lesson-progress-hud-row">
        <span className="lesson-progress-hud-label">{pctLabel}</span>
        <span className="lesson-progress-hud-value">{pctValue}%</span>
      </div>
      <div className="lesson-progress-hud-row">
        <span className="lesson-progress-hud-label">Thời gian</span>
        <span className="lesson-progress-hud-value lesson-progress-hud-mono">{formatClock(elapsedSec)}</span>
      </div>
      <div className="lesson-progress-hud-row">
        <span className="lesson-progress-hud-label">{scoreLabel}</span>
        <span className="lesson-progress-hud-value">{scoreValue}</span>
      </div>
      <div className="lesson-progress-hud-bar" aria-hidden>
        <div className="lesson-progress-hud-bar-fill" style={{ width: `${Math.min(100, Math.max(0, pctValue))}%` }} />
      </div>
    </aside>
  );
}
