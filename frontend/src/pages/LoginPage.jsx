import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { useAuth } from "../context/useAuth.js";

export function LoginPage() {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const onSubmit = async (event) => {
    event.preventDefault();
    setError("");
    setIsSubmitting(true);
    try {
      await login(email, password);
      navigate("/courses");
    } catch (submitError) {
      setError(submitError.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="auth-page">
      <form onSubmit={onSubmit} className="auth-card">
        <div className="auth-logo">
          <div className="auth-logo-icon">E</div>
          <span>LearnEnglish</span>
        </div>
        <h1 className="auth-title">Chào mừng trở lại!</h1>
        <p className="auth-sub">Đăng nhập để tiếp tục lộ trình học của bạn.</p>

        <div className="stack" style={{ gap: 14 }}>
          <label className="field">
            <span style={{ fontSize: "0.85rem", fontWeight: 600, color: "var(--text)" }}>
              Email hoặc username
            </span>
            <input
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              type="text"
              placeholder="admin hoặc email@example.com"
              required
              autoComplete="username"
            />
          </label>
          <label className="field">
            <span style={{ fontSize: "0.85rem", fontWeight: 600, color: "var(--text)" }}>
              Mật khẩu
            </span>
            <input
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              type="password"
              placeholder="••••••••"
              minLength={8}
              required
              autoComplete="current-password"
            />
          </label>

          {error ? (
            <div style={{ padding: "10px 14px", background: "#fef2f2", border: "1px solid #fecaca", borderRadius: "var(--radius-sm)", color: "var(--danger)", fontSize: "0.88rem" }}>
              ⚠️ {error}
            </div>
          ) : null}

          <button className="btn btn-block" type="submit" disabled={isSubmitting} style={{ padding: "12px", fontSize: "0.95rem" }}>
            {isSubmitting ? "Đang đăng nhập..." : "Đăng nhập →"}
          </button>
        </div>

        <div style={{ marginTop: 20, textAlign: "center" }}>
          <span className="muted small">Chưa có tài khoản? </span>
          <Link to="/register" style={{ color: "var(--brand)", fontWeight: 600, fontSize: "0.88rem" }}>
            Đăng ký ngay
          </Link>
        </div>
        <div style={{ marginTop: 8, textAlign: "center" }}>
          <Link to="/" style={{ color: "var(--text-muted)", fontSize: "0.85rem" }}>← Về trang chủ</Link>
        </div>
      </form>
    </div>
  );
}
