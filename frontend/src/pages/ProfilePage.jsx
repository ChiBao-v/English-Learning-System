import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";

import { useAuth } from "../context/useAuth.js";
import { changePasswordApi, updateProfileApi } from "../services/api.js";

const TABS = [
  { id: "profile", label: "👤 Hồ sơ cá nhân" },
  { id: "password", label: "🔐 Đổi mật khẩu" },
  { id: "avatar", label: "🖼️ Ảnh đại diện" },
];

export function ProfilePage() {
  const { user, authFetch, logout, updateUser } = useAuth();
  const [searchParams, setSearchParams] = useSearchParams();
  const activeTab = searchParams.get("tab") || "profile";

  const setTab = (id) => setSearchParams(id === "profile" ? {} : { tab: id });

  return (
    <div className="profile-page">
      <div className="profile-header-card">
        <div className="profile-avatar-lg">
          {([user?.first_name, user?.last_name].filter(Boolean).join("").slice(0, 1) || user?.email?.slice(0, 1) || "?").toUpperCase()}
        </div>
        <div>
          <h1 className="profile-display-name">
            {[user?.first_name, user?.last_name].filter(Boolean).join(" ") || user?.email}
          </h1>
          <p className="profile-email">{user?.email}</p>
          <span className="profile-role-badge">
            {user?.role === "admin" ? "⚙️ Quản trị viên" : user?.role === "data_scientist" ? "🔬 Data Scientist" : "🎓 Học viên"}
          </span>
        </div>
      </div>

      <div className="profile-tabs" role="tablist">
        {TABS.map((t) => (
          <button
            key={t.id}
            type="button"
            role="tab"
            aria-selected={activeTab === t.id}
            className={"profile-tab" + (activeTab === t.id ? " profile-tab--active" : "")}
            onClick={() => setTab(t.id)}
          >
            {t.label}
          </button>
        ))}
      </div>

      <div className="profile-tab-content">
        {activeTab === "profile" && <ProfileInfoTab user={user} authFetch={authFetch} updateUser={updateUser} />}
        {activeTab === "password" && <ChangePasswordTab authFetch={authFetch} logout={logout} />}
        {activeTab === "avatar" && <AvatarTab user={user} />}
      </div>
    </div>
  );
}

function ProfileInfoTab({ user, authFetch, updateUser }) {
  const [form, setForm] = useState({
    first_name: user?.first_name || "",
    last_name: user?.last_name || "",
    username: user?.username || "",
  });
  const [saving, setSaving] = useState(false);
  const [msg, setMsg] = useState(null);
  const [err, setErr] = useState("");

  const onChange = (e) => setForm((f) => ({ ...f, [e.target.name]: e.target.value }));

  const onSubmit = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMsg(null);
    setErr("");
    try {
      const updated = await authFetch((token) => updateProfileApi(form, token));
      updateUser(updated);
      setMsg("Cập nhật thành công!");
    } catch (ex) {
      setErr(ex.message || "Có lỗi xảy ra.");
    } finally {
      setSaving(false);
    }
  };

  return (
    <form className="profile-form card" onSubmit={onSubmit}>
      <h2 className="profile-section-title">Thông tin cá nhân</h2>
      <div className="profile-form-row">
        <div className="field">
          <label htmlFor="first_name">Họ</label>
          <input id="first_name" name="first_name" value={form.first_name} onChange={onChange} placeholder="Nhập họ" />
        </div>
        <div className="field">
          <label htmlFor="last_name">Tên</label>
          <input id="last_name" name="last_name" value={form.last_name} onChange={onChange} placeholder="Nhập tên" />
        </div>
      </div>
      <div className="field">
        <label htmlFor="username">Tên đăng nhập</label>
        <input id="username" name="username" value={form.username} onChange={onChange} placeholder="username" />
      </div>
      <div className="field">
        <label>Email</label>
        <input value={user?.email || ""} disabled className="input-disabled" />
        <span className="field-hint">Email không thể thay đổi.</span>
      </div>
      {msg && <p className="profile-success">{msg}</p>}
      {err && <p className="error">{err}</p>}
      <button type="submit" className="btn" disabled={saving}>
        {saving ? "Đang lưu..." : "Lưu thay đổi"}
      </button>
    </form>
  );
}

function ChangePasswordTab({ authFetch, logout }) {
  const [form, setForm] = useState({ old_password: "", new_password: "", confirm_password: "" });
  const [saving, setSaving] = useState(false);
  const [msg, setMsg] = useState(null);
  const [err, setErr] = useState("");

  const onChange = (e) => setForm((f) => ({ ...f, [e.target.name]: e.target.value }));

  const onSubmit = async (e) => {
    e.preventDefault();
    setErr("");
    setMsg(null);
    if (form.new_password !== form.confirm_password) {
      setErr("Mật khẩu mới và xác nhận không khớp.");
      return;
    }
    if (form.new_password.length < 8) {
      setErr("Mật khẩu mới phải có ít nhất 8 ký tự.");
      return;
    }
    setSaving(true);
    try {
      await authFetch((token) => changePasswordApi({ old_password: form.old_password, new_password: form.new_password }, token));
      setMsg("Đổi mật khẩu thành công. Vui lòng đăng nhập lại.");
      setForm({ old_password: "", new_password: "", confirm_password: "" });
      setTimeout(() => logout(), 2500);
    } catch (ex) {
      setErr(ex.message || "Có lỗi xảy ra.");
    } finally {
      setSaving(false);
    }
  };

  return (
    <form className="profile-form card" onSubmit={onSubmit}>
      <h2 className="profile-section-title">Đổi mật khẩu</h2>
      <p className="muted small">Sau khi đổi thành công, bạn sẽ được đăng xuất và cần đăng nhập lại.</p>
      <div className="field">
        <label htmlFor="old_password">Mật khẩu hiện tại</label>
        <input id="old_password" name="old_password" type="password" value={form.old_password} onChange={onChange} placeholder="Nhập mật khẩu hiện tại" required />
      </div>
      <div className="field">
        <label htmlFor="new_password">Mật khẩu mới</label>
        <input id="new_password" name="new_password" type="password" value={form.new_password} onChange={onChange} placeholder="Ít nhất 8 ký tự" required />
      </div>
      <div className="field">
        <label htmlFor="confirm_password">Xác nhận mật khẩu mới</label>
        <input id="confirm_password" name="confirm_password" type="password" value={form.confirm_password} onChange={onChange} placeholder="Nhập lại mật khẩu mới" required />
      </div>
      {msg && <p className="profile-success">{msg}</p>}
      {err && <p className="error">{err}</p>}
      <button type="submit" className="btn" disabled={saving || !form.old_password || !form.new_password}>
        {saving ? "Đang xử lý..." : "Đổi mật khẩu"}
      </button>
    </form>
  );
}

function AvatarTab({ user }) {
  const initial = ([user?.first_name, user?.last_name].filter(Boolean).join("").slice(0, 1) || user?.email?.slice(0, 1) || "?").toUpperCase();
  const colors = [
    "linear-gradient(135deg,#4f46e5,#7c3aed)",
    "linear-gradient(135deg,#0ea5e9,#06b6d4)",
    "linear-gradient(135deg,#10b981,#059669)",
    "linear-gradient(135deg,#f59e0b,#ef4444)",
    "linear-gradient(135deg,#ec4899,#f43f5e)",
    "linear-gradient(135deg,#8b5cf6,#6366f1)",
  ];
  const [selected, setSelected] = useState(0);

  return (
    <div className="profile-form card">
      <h2 className="profile-section-title">Ảnh đại diện</h2>
      <p className="muted small">Chọn màu nền cho avatar của bạn.</p>

      <div className="avatar-preview-lg" style={{ background: colors[selected] }}>
        {initial}
      </div>

      <div className="avatar-color-grid">
        {colors.map((c, i) => (
          <button
            key={i}
            type="button"
            className={"avatar-color-swatch" + (selected === i ? " avatar-color-swatch--selected" : "")}
            style={{ background: c }}
            onClick={() => setSelected(i)}
            aria-label={`Màu ${i + 1}`}
          />
        ))}
      </div>

      <p className="muted small" style={{ marginTop: 12 }}>
        Tính năng tải ảnh từ máy tính sẽ được bổ sung trong phiên bản tới.
      </p>
    </div>
  );
}
