import { useCallback, useEffect, useState } from "react";

import { useAuth } from "../context/useAuth.js";
import {
  getMLFeatureDistributionApi,
  getMLModelStatusApi,
  retrainMLModelApi,
} from "../services/api.js";

function fmtPct(v) {
  if (v === null || v === undefined) return "—";
  return `${(Number(v) * 100).toFixed(2)}%`;
}

function fmtNum(v, digits = 4) {
  if (v === null || v === undefined) return "—";
  return Number(v).toFixed(digits);
}

function fmtDate(iso) {
  if (!iso) return "—";
  const d = new Date(iso);
  return d.toLocaleString();
}

export function MLMonitorPage() {
  const { authFetch } = useAuth();
  const [status, setStatus] = useState(null);
  const [featureDist, setFeatureDist] = useState(null);
  const [error, setError] = useState("");
  const [retraining, setRetraining] = useState(false);
  const [retrainResult, setRetrainResult] = useState(null);

  const load = useCallback(async () => {
    setError("");
    try {
      const [st, fd] = await Promise.all([
        authFetch((t) => getMLModelStatusApi(t)),
        authFetch((t) => getMLFeatureDistributionApi(t)).catch(() => null),
      ]);
      setStatus(st);
      setFeatureDist(fd);
    } catch (e) {
      setError(e.message);
    }
  }, [authFetch]);

  useEffect(() => {
    load();
  }, [load]);

  async function handleRetrain() {
    if (retraining) return;
    if (!window.confirm("Bắt đầu retrain model? Quá trình này có thể mất vài phút.")) return;
    setRetraining(true);
    setRetrainResult(null);
    setError("");
    try {
      const res = await authFetch((t) => retrainMLModelApi(t));
      setRetrainResult(res);
      await load();
    } catch (e) {
      setError(e.message);
    } finally {
      setRetraining(false);
    }
  }

  const active = status?.active;
  const history = status?.history || [];
  const averages = featureDist?.averages || {};
  const levelCounts = featureDist?.predicted_level_counts || [];

  return (
    <div className="ml-monitor-page" style={{ padding: 12 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
        <h2 style={{ margin: 0 }}>🤖 ML Monitor — Level Predictor</h2>
        <button
          type="button"
          onClick={handleRetrain}
          disabled={retraining}
          style={{
            padding: "8px 16px",
            background: retraining ? "#9ca3af" : "#4f46e5",
            color: "#fff",
            border: 0,
            borderRadius: 8,
            cursor: retraining ? "wait" : "pointer",
            fontWeight: 600,
          }}
        >
          {retraining ? "Đang retrain…" : "🔁 Retrain Model"}
        </button>
      </div>

      {error && (
        <div style={{ background: "#fee2e2", color: "#991b1b", padding: 10, borderRadius: 6, marginBottom: 12 }}>
          {error}
        </div>
      )}

      {retrainResult && (
        <div style={{ background: "#dcfce7", color: "#166534", padding: 10, borderRadius: 6, marginBottom: 12 }}>
          ✅ {retrainResult.detail} (version <code>{retrainResult.active_version}</code>)
          {retrainResult.log && (
            <pre style={{ marginTop: 8, fontSize: 12, whiteSpace: "pre-wrap", maxHeight: 200, overflow: "auto" }}>
              {retrainResult.log}
            </pre>
          )}
        </div>
      )}

      <section style={{ background: "#f9fafb", padding: 16, borderRadius: 8, marginBottom: 16 }}>
        <h3 style={{ marginTop: 0 }}>Active Model</h3>
        {active ? (
          <table>
            <tbody>
              <tr><td style={{ paddingRight: 16 }}><strong>Name</strong></td><td><code>{active.name}</code></td></tr>
              <tr><td><strong>Version</strong></td><td><code>{active.version}</code></td></tr>
              <tr><td><strong>Accuracy</strong></td><td>{fmtPct(active.accuracy)}</td></tr>
              <tr><td><strong>F1 (macro)</strong></td><td>{fmtNum(active.f1_macro)}</td></tr>
              <tr><td><strong>Created</strong></td><td>{fmtDate(active.created_at)}</td></tr>
              <tr><td><strong>Path</strong></td><td><code style={{ fontSize: 12 }}>{active.model_path}</code></td></tr>
            </tbody>
          </table>
        ) : (
          <p>Chưa có model active. Bấm "Retrain Model" để train mới.</p>
        )}
      </section>

      <section style={{ marginBottom: 16 }}>
        <h3>Lịch sử Training (10 lần gần nhất)</h3>
        {history.length === 0 ? (
          <p>Chưa có lịch sử.</p>
        ) : (
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ background: "#f3f4f6" }}>
                <th style={{ textAlign: "left", padding: 8 }}>Version</th>
                <th style={{ textAlign: "left", padding: 8 }}>Accuracy</th>
                <th style={{ textAlign: "left", padding: 8 }}>F1 (macro)</th>
                <th style={{ textAlign: "left", padding: 8 }}>Active</th>
                <th style={{ textAlign: "left", padding: 8 }}>Trained at</th>
              </tr>
            </thead>
            <tbody>
              {history.map((m) => (
                <tr key={m.id} style={{ borderBottom: "1px solid #e5e7eb" }}>
                  <td style={{ padding: 8 }}><code>{m.version}</code></td>
                  <td style={{ padding: 8 }}>{fmtPct(m.accuracy)}</td>
                  <td style={{ padding: 8 }}>{fmtNum(m.f1_macro)}</td>
                  <td style={{ padding: 8 }}>{m.is_active ? "✅" : ""}</td>
                  <td style={{ padding: 8 }}>{fmtDate(m.created_at)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>

      <section>
        <h3>Phân phối Feature (UserFeature)</h3>
        {featureDist ? (
          <>
            <p>Số user có feature: <strong>{featureDist.user_feature_count}</strong></p>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
              <div>
                <h4>Trung bình</h4>
                <ul>
                  <li>avg_response_time: {fmtNum(averages.avg_response_time, 2)}s</li>
                  <li>accuracy_rate: {fmtPct(averages.avg_accuracy_rate)}</li>
                  <li>hint_usage: {fmtPct(averages.avg_hint_usage)}</li>
                  <li>consistency: {fmtNum(averages.avg_consistency, 3)}</li>
                </ul>
              </div>
              <div>
                <h4>Phân bố theo level dự đoán</h4>
                <ul>
                  {levelCounts.map((row) => (
                    <li key={row.level}>
                      <strong>{row.level}</strong>: {row.count}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </>
        ) : (
          <p>Chưa có dữ liệu feature.</p>
        )}
      </section>
    </div>
  );
}
