import { useEffect, useMemo, useState } from "react";
import { Bar } from "react-chartjs-2";

import { useAuth } from "../context/useAuth.js";
import { getAdminDashboardApi, getMLFeatureDistributionApi } from "../services/api.js";

const KPI_DEFS = [
  { key: "total_users",   icon: "👥", label: "Người dùng",  accent: "#4f46e5", sub: "đã đăng ký" },
  { key: "total_courses", icon: "📚", label: "Khóa học",    accent: "#0ea5e9", sub: "đang hoạt động" },
  { key: "total_lessons", icon: "📄", label: "Bài học",     accent: "#10b981", sub: "tổng cộng" },
  { key: "active_today",  icon: "⚡", label: "Hoạt động hôm nay", accent: "#f59e0b", sub: "người dùng" },
];

export function AdminDashboardPage() {
  const { authFetch } = useAuth();
  const [data, setData] = useState(null);
  const [featureDist, setFeatureDist] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    let mounted = true;
    (async () => {
      try {
        const [res, fd] = await Promise.all([
          authFetch((t) => getAdminDashboardApi(t)),
          authFetch((t) => getMLFeatureDistributionApi(t)).catch(() => null),
        ]);
        if (mounted) { setData(res); setFeatureDist(fd); }
      } catch (e) {
        if (mounted) setError(e.message);
      }
    })();
    return () => { mounted = false; };
  }, [authFetch]);

  const chart = data?.activity_last_7_days || [];
  const days = useMemo(() => {
    const labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
    return chart.length ? chart : labels.map((_, i) => ({ day: null, count: 0 }));
  }, [chart]);

  const barChartData = useMemo(() => ({
    labels: days.map((row, idx) => row.day ? String(row.day).slice(5) : `D${idx + 1}`),
    datasets: [{
      label: "Sự kiện BehaviorLog",
      data: days.map((row) => row.count ?? 0),
      backgroundColor: days.map((_, i) => `hsla(${240 - i * 8},70%,55%,0.75)`),
      borderRadius: 8,
      borderSkipped: false,
    }],
  }), [days]);

  const barOptions = {
    responsive: true,
    plugins: {
      legend: { display: false },
      tooltip: { callbacks: { label: (ctx) => ` ${ctx.raw} sự kiện` } },
    },
    scales: {
      y: { beginAtZero: true, ticks: { precision: 0 }, grid: { color: "rgba(0,0,0,.05)" } },
      x: { grid: { display: false } },
    },
  };

  if (error) return <div className="admin-shell"><p className="error">{error}</p></div>;
  if (!data) return <div className="admin-shell"><p className="muted">Đang tải bảng điều khiển...</p></div>;

  const o = data.overview || {};
  const ml = data.ml_model;

  return (
    <div className="admin-shell">
      <header className="admin-header-block">
        <h1>System Overview</h1>
        <p className="muted">Tổng quan hệ thống — hoạt động 7 ngày gần nhất</p>
      </header>

      {/* KPIs */}
      <div className="admin-kpi-grid">
        {KPI_DEFS.map(({ key, icon, label, accent, sub }) => (
          <div key={key} className="stat-card">
            <div className="stat-card-accent" style={{ background: accent }} />
            <div className="stat-icon">{icon}</div>
            <div className="stat-label">{label}</div>
            <div className="stat-value" style={{ color: accent }}>{o[key] ?? "—"}</div>
            <div className="stat-sub">{sub}</div>
          </div>
        ))}
      </div>

      {/* Activity chart */}
      <div className="card admin-chart-card" style={{ marginBottom: 20 }}>
        <h2 className="chart-section-title">Hoạt động người dùng — 7 ngày qua</h2>
        <div className="chart-wrap">
          <Bar data={barChartData} options={barOptions} />
        </div>
      </div>

      <div className="admin-two-col">
        {/* ML Model */}
        <div className="card admin-card">
          <h2>ML Model Status</h2>
          {ml ? (
            <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              <div style={{ padding: "12px 16px", background: ml.is_active ? "#ecfdf5" : "#fef2f2", border: `1px solid ${ml.is_active ? "#a7f3d0" : "#fecaca"}`, borderRadius: "var(--radius)", display: "flex", alignItems: "center", gap: 10 }}>
                <span style={{ fontSize: "1.5rem" }}>{ml.is_active ? "✅" : "⚠️"}</span>
                <div>
                  <div style={{ fontWeight: 700 }}>{ml.name}</div>
                  <div className="muted small">v{ml.version} · {ml.is_active ? "Active" : "Inactive"}</div>
                </div>
              </div>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
                <div style={{ padding: "12px", background: "var(--bg-muted)", borderRadius: "var(--radius-sm)", textAlign: "center" }}>
                  <div style={{ fontWeight: 900, fontSize: "1.3rem", color: "var(--brand)" }}>{ml.accuracy_pct != null ? `${ml.accuracy_pct}%` : "—"}</div>
                  <div className="muted small">Accuracy</div>
                </div>
                <div style={{ padding: "12px", background: "var(--bg-muted)", borderRadius: "var(--radius-sm)", textAlign: "center" }}>
                  <div style={{ fontWeight: 700, fontSize: "0.85rem", color: "var(--text)" }}>{ml.last_trained || "—"}</div>
                  <div className="muted small">Last trained</div>
                </div>
              </div>
            </div>
          ) : (
            <div style={{ textAlign: "center", padding: "24px 0" }}>
              <div style={{ fontSize: "2rem", marginBottom: 8 }}>🤖</div>
              <p className="muted small">Chưa có model active trong registry.</p>
            </div>
          )}
          <p className="muted small" style={{ marginTop: 12 }}>
            Train lại: <code style={{ background: "var(--bg-muted)", padding: "2px 6px", borderRadius: 4 }}>python manage.py train_level_model</code>
          </p>
        </div>

        {/* Feature Distribution */}
        <div className="card admin-card">
          <h2>Feature Distribution</h2>
          {featureDist && featureDist.user_feature_count > 0 ? (
            <>
              <div style={{ padding: "10px 14px", background: "var(--brand-pale)", borderRadius: "var(--radius-sm)", marginBottom: 14, display: "flex", alignItems: "center", gap: 8 }}>
                <span style={{ fontSize: "1.2rem" }}>👤</span>
                <span style={{ fontWeight: 700, color: "var(--brand)" }}>{featureDist.user_feature_count}</span>
                <span className="muted small">users có vector feature</span>
              </div>
              <div className="muted small" style={{ marginBottom: 8, fontWeight: 700 }}>Phân bố level dự đoán:</div>
              <ul className="admin-list" style={{ paddingLeft: 0, listStyle: "none", display: "flex", flexDirection: "column", gap: 6 }}>
                {(featureDist.predicted_level_counts || []).map((row) => (
                  <li key={row.level} style={{ display: "flex", alignItems: "center", gap: 8 }}>
                    <span style={{ padding: "3px 10px", background: "var(--bg-muted)", borderRadius: "999px", fontSize: "0.8rem", fontWeight: 700 }}>{row.level}</span>
                    <span style={{ fontWeight: 600 }}>{row.count} users</span>
                  </li>
                ))}
              </ul>
            </>
          ) : (
            <div style={{ textAlign: "center", padding: "24px 0" }}>
              <div style={{ fontSize: "2rem", marginBottom: 8 }}>📊</div>
              <p className="muted small">Chưa có bản ghi UserFeature. Học viên cần làm bài để sinh feature.</p>
            </div>
          )}
        </div>

        {/* Recent activity */}
        <div className="card admin-card" style={{ gridColumn: "1 / -1" }}>
          <h2>Recent Activity</h2>
          <ul className="admin-recent">
            {(data.recent_logs || []).map((log, i) => (
              <li key={`${log.timestamp}-${i}`} style={{ display: "flex", alignItems: "flex-start", gap: 12 }}>
                <div style={{ width: 32, height: 32, borderRadius: "50%", background: "var(--brand-pale)", color: "var(--brand)", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 800, fontSize: "0.85rem", flexShrink: 0 }}>
                  {(log.user_email || "?").slice(0, 1).toUpperCase()}
                </div>
                <div>
                  <span className="admin-recent-user">{log.user_email}</span>
                  <span className="muted"> — {log.summary}</span>
                  <div className="muted small">{log.timestamp}</div>
                </div>
              </li>
            ))}
            {!data.recent_logs?.length && (
              <li className="muted small" style={{ padding: "16px 0", textAlign: "center" }}>Chưa có log nào.</li>
            )}
          </ul>
        </div>
      </div>
    </div>
  );
}
