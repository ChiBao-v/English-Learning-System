import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { Radar } from "react-chartjs-2";

import { useAuth } from "../context/useAuth.js";
import { getRecommendationsApi, getStudentDashboardApi } from "../services/api.js";

const SKILL_VI = {
  listening: "Listening",
  reading: "Reading",
  grammar: "Grammar",
  vocabulary: "Vocabulary",
  writing: "Writing",
  speaking: "Speaking",
};

const SKILL_COLORS = {
  listening:  "#4f46e5",
  reading:    "#0ea5e9",
  grammar:    "#10b981",
  vocabulary: "#f59e0b",
  writing:    "#ec4899",
  speaking:   "#8b5cf6",
};

const SKILL_ICONS = {
  listening: "🎧", reading: "📖", grammar: "✏️",
  vocabulary: "📝", writing: "🖊️", speaking: "🗣️",
};

function formatStudyTime(totalSeconds) {
  if (!totalSeconds) return "0 phút";
  const h = Math.floor(totalSeconds / 3600);
  const m = Math.floor((totalSeconds % 3600) / 60);
  if (h > 0) return `${h}h ${m}m`;
  return `${m} phút`;
}

function SkillBar({ label, pct, color, icon }) {
  const v = Math.min(100, Math.max(0, pct || 0));
  return (
    <div className="skill-row">
      <span className="skill-label">{icon} {label}</span>
      <div className="progress-bar skill-bar-track">
        <div
          className="progress-bar-fill"
          style={{ width: `${v}%`, background: color }}
        />
      </div>
      <span className="skill-pct" style={{ color }}>{v}%</span>
    </div>
  );
}

const skillOrder = ["listening", "reading", "grammar", "vocabulary", "writing", "speaking"];

export function DashboardPage() {
  const { user, authFetch } = useAuth();
  const [dash, setDash] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;
    const run = async () => {
      try {
        const dashData = await authFetch((token) => getStudentDashboardApi(token));
        if (isMounted) setDash(dashData);
      } catch (e) {
        if (isMounted) setError(e.message);
      }
      try {
        const recData = await authFetch((token) => getRecommendationsApi(token));
        if (isMounted) setRecommendations(recData.recommendations || []);
      } catch {
        // Recommendations chưa có model — hiển thị trống, không block dashboard
      }
    };
    run();
    return () => { isMounted = false; };
  }, [authFetch]);

  const kpis = dash?.kpis || {};
  const courseProgress = dash?.course_progress || [];
  const skillPct = dash?.skill_pct || {};

  const displayName =
    [user?.first_name, user?.last_name].filter(Boolean).join(" ").trim() || user?.email || "";

  const radarData = useMemo(
    () => ({
      labels: skillOrder.map((k) => `${SKILL_ICONS[k]} ${SKILL_VI[k]}`),
      datasets: [
        {
          label: "Độ chính xác (%)",
          data: skillOrder.map((k) => skillPct[k] ?? 0),
          backgroundColor: "rgba(79,70,229,0.15)",
          borderColor: "rgba(79,70,229,0.9)",
          borderWidth: 2,
          pointBackgroundColor: skillOrder.map((k) => SKILL_COLORS[k] || "#4f46e5"),
          pointRadius: 4,
          pointHoverRadius: 6,
        },
      ],
    }),
    [skillPct],
  );

  const radarOptions = {
    responsive: true,
    scales: {
      r: {
        beginAtZero: true,
        max: 100,
        ticks: { stepSize: 25, font: { size: 10 } },
        grid: { color: "rgba(0,0,0,.07)" },
        pointLabels: { font: { size: 11, weight: "600" } },
      },
    },
    plugins: { legend: { display: false } },
  };

  return (
    <div className="stack dashboard-doc">
      <header style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", flexWrap: "wrap", gap: 12 }}>
        <div>
          <h1 className="page-title">Dashboard cá nhân</h1>
          <p className="muted">Xin chào{displayName ? `, ${displayName}` : ""} 👋</p>
        </div>
        {dash?.predicted_level && (
          <div style={{ padding: "8px 16px", background: "var(--brand-pale)", border: "1px solid #c7d2fe", borderRadius: "var(--radius)", display: "flex", alignItems: "center", gap: 8 }}>
            <span style={{ fontSize: "0.75rem", fontWeight: 800, color: "var(--text-muted)", textTransform: "uppercase", letterSpacing: ".06em" }}>Trình độ dự đoán</span>
            <span style={{ fontWeight: 900, color: "var(--brand)", fontSize: "1.1rem" }}>{dash.predicted_level}</span>
          </div>
        )}
      </header>

      {error ? <p className="error">{error}</p> : null}

      {/* KPIs */}
      <div className="dashboard-kpi-grid">
        <div className="kpi-card">
          <div className="kpi-icon">📚</div>
          <div className="kpi-label">Khóa học</div>
          <div className="kpi-value">{kpis.enrolled_courses ?? 0}</div>
          <div className="kpi-hint">đang theo học</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-icon">⏱️</div>
          <div className="kpi-label">Thời gian học</div>
          <div className="kpi-value">{formatStudyTime(kpis.total_study_seconds)}</div>
          <div className="kpi-hint">tổng cộng</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-icon">🎯</div>
          <div className="kpi-label">Độ chính xác</div>
          <div className="kpi-value">{kpis.accuracy_pct ?? 0}%</div>
          <div className="kpi-hint">trung bình</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-icon">✅</div>
          <div className="kpi-label">Bài đã hoàn thành</div>
          <div className="kpi-value">{kpis.completed_lessons ?? 0}</div>
          <div className="kpi-hint">bài học</div>
        </div>
      </div>

      <div className="dashboard-two-col">
        {/* Left: tiến độ + kỹ năng */}
        <div className="stack" style={{ gap: 20 }}>
          <section className="card dashboard-panel">
            <h2 className="panel-title">Tiến độ khóa học</h2>
            {courseProgress.length ? (
              <div className="stack gap-sm">
                {courseProgress.map((c) => (
                  <div key={c.course_id} className="course-progress-item">
                    <div className="course-progress-head">
                      <span style={{ fontWeight: 600 }}>{c.title}</span>
                      <span className="muted small">{c.progress_pct}%</span>
                    </div>
                    <div className="progress-bar">
                      <div className="progress-bar-fill" style={{ width: `${Math.min(100, c.progress_pct)}%` }} />
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <p className="muted small">Chưa có khóa học nào. Hãy đăng ký tại mục <Link to="/courses" style={{ color: "var(--brand)" }}>Khóa học</Link>.</p>
            )}
          </section>

          <section className="card dashboard-panel">
            <h2 className="panel-title">Phân tích kỹ năng</h2>
            <div className="chart-wrap radar-wrap">
              <Radar data={radarData} options={radarOptions} />
            </div>
            <div style={{ marginTop: 16 }}>
              {skillOrder.map((key) => (
                <SkillBar
                  key={key}
                  label={SKILL_VI[key] || key}
                  pct={skillPct[key]}
                  color={SKILL_COLORS[key]}
                  icon={SKILL_ICONS[key]}
                />
              ))}
            </div>
            {!Object.keys(skillPct).length ? (
              <p className="muted small" style={{ marginTop: 8 }}>Làm thêm bài tập để có thống kê theo kỹ năng.</p>
            ) : null}
          </section>
        </div>

        {/* Right: gợi ý AI */}
        <section className="card dashboard-panel">
          <h2 className="panel-title">Gợi ý AI</h2>
          <p className="muted small" style={{ marginTop: -8, marginBottom: 16 }}>
            Dựa trên tiến độ và kết quả làm bài gần đây của bạn.
          </p>
          <div className="stack gap-sm rec-list">
            {recommendations.length ? (
              recommendations.map((item, idx) => (
                <div key={item.id || idx} className="rec-card">
                  <div className="rec-rank">#{idx + 1}</div>
                  <div style={{ flex: 1 }}>
                    <div className="rec-title">📖 {item.lesson_title || "Bài học"}</div>
                    <p className="muted small" style={{ margin: "4px 0 10px" }}>{item.reason}</p>
                    <Link className="btn btn-secondary btn-sm" to={`/lessons/${item.lesson}`}>
                      Học ngay →
                    </Link>
                  </div>
                </div>
              ))
            ) : (
              <div style={{ textAlign: "center", padding: "32px 16px" }}>
                <div style={{ fontSize: "2.5rem", marginBottom: 12 }}>🤖</div>
                <p className="muted small" style={{ margin: 0 }}>
                  Chưa có đề xuất. Hãy làm thêm quiz để hệ thống học hành vi của bạn.
                </p>
                <Link to="/courses" className="btn btn-sm" style={{ marginTop: 16, display: "inline-flex" }}>
                  Vào học ngay
                </Link>
              </div>
            )}
          </div>
        </section>
      </div>
    </div>
  );
}
