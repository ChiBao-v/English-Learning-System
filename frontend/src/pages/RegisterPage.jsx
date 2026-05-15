import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { useAuth } from "../context/useAuth.js";

export function RegisterPage() {
  const navigate = useNavigate();
  const { register } = useAuth();
  const [form, setForm] = useState({ email: "", username: "", first_name: "", last_name: "", password: "" });
  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const onChange = (e) => setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));

  const onSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setIsSubmitting(true);
    try {
      await register(form);
      navigate("/courses");
    } catch (err) {
      setError(err.message);
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
        <h1 className="auth-title">Tạo tài khoản</h1>
        <p className="auth-sub">Bắt đầu hành trình học tiếng Anh cùng AI.</p>

        <div className="stack" style={{ gap: 12 }}>
          <div style={{ display: "grid", gap: 12, gridTemplateColumns: "1fr 1fr" }}>
            <label className="field">
              <span style={{ fontSize: "0.82rem", fontWeight: 600 }}>Tên</span>
              <input name="first_name" value={form.first_name} onChange={onChange} placeholder="Nguyễn" />
            </label>
            <label className="field">
              <span style={{ fontSize: "0.82rem", fontWeight: 600 }}>Họ</span>
              <input name="last_name" value={form.last_name} onChange={onChange} placeholder="Văn A" />
            </label>
          </div>
          <label className="field">
            <span style={{ fontSize: "0.82rem", fontWeight: 600 }}>Email *</span>
            <input name="email" value={form.email} onChange={onChange} type="email" placeholder="email@example.com" required />
          </label>
          <label className="field">
            <span style={{ fontSize: "0.82rem", fontWeight: 600 }}>Username *</span>
            <input name="username" value={form.username} onChange={onChange} placeholder="username" required />
          </label>
          <label className="field">
            <span style={{ fontSize: "0.82rem", fontWeight: 600 }}>Mật khẩu *</span>
            <input name="password" value={form.password} onChange={onChange} type="password" placeholder="Tối thiểu 8 ký tự" minLength={8} required />
          </label>

          {error ? (
            <div style={{ padding: "10px 14px", background: "#fef2f2", border: "1px solid #fecaca", borderRadius: "var(--radius-sm)", color: "var(--danger)", fontSize: "0.88rem" }}>
              ⚠️ {error}
            </div>
          ) : null}

          <button className="btn btn-block" type="submit" disabled={isSubmitting} style={{ padding: "12px", fontSize: "0.95rem" }}>
            {isSubmitting ? "Đang tạo tài khoản..." : "Tạo tài khoản →"}
          </button>
        </div>

        <div style={{ marginTop: 20, textAlign: "center" }}>
          <span className="muted small">Đã có tài khoản? </span>
          <Link to="/login" style={{ color: "var(--brand)", fontWeight: 600, fontSize: "0.88rem" }}>Đăng nhập</Link>
        </div>
        <div style={{ marginTop: 8, textAlign: "center" }}>
          <Link to="/" style={{ color: "var(--text-muted)", fontSize: "0.85rem" }}>← Về trang chủ</Link>
        </div>
      </form>
    </div>
  );
}
