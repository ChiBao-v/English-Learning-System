import { useEffect, useRef, useState } from "react";
import { Link, NavLink } from "react-router-dom";

import { useAuth } from "../context/useAuth.js";

const navLinkClass = ({ isActive }) => "nav-link" + (isActive ? " active" : "");

/**
 * Header dùng chung cho TOÀN BỘ trang (public lẫn trong app) để taskbar đồng
 * bộ. Khi đã đăng nhập → hiển thị nav học tập + dropdown người dùng (giống
 * trang /courses). Khi chưa đăng nhập → nav giới thiệu + nút Đăng nhập/Đăng ký.
 */
export function SiteHeader() {
  const { isAuthenticated, user, logout } = useAuth();
  const [dropOpen, setDropOpen] = useState(false);
  const dropRef = useRef(null);

  const displayName =
    [user?.first_name, user?.last_name].filter(Boolean).join(" ").trim() || user?.email || "Học viên";
  const initial = (displayName.slice(0, 1) || "?").toUpperCase();

  useEffect(() => {
    function onClickOutside(e) {
      if (dropRef.current && !dropRef.current.contains(e.target)) setDropOpen(false);
    }
    document.addEventListener("mousedown", onClickOutside);
    return () => document.removeEventListener("mousedown", onClickOutside);
  }, []);

  return (
    <header className="header app-header-doc">
      <Link to={isAuthenticated ? "/courses" : "/"} className="brand">
        <div className="public-logo" style={{ width: 28, height: 28, fontSize: "0.8rem" }}>E</div>
        <span className="brand-mark">Learn</span>English
      </Link>

      <nav className="nav">
        {isAuthenticated ? (
          <>
            <NavLink to="/courses" className={navLinkClass}>📚 Khóa học</NavLink>
            <NavLink to="/dashboard" className={navLinkClass}>📊 Dashboard</NavLink>
            <NavLink to="/roadmap" className={navLinkClass}>🗺️ Lộ trình</NavLink>
            <NavLink to="/about" className={navLinkClass}>ℹ️ Về chúng tôi</NavLink>
            {user?.role === "admin" || user?.role === "data_scientist" ? (
              <NavLink to="/admin" className={navLinkClass}>
                ⚙️ {user?.role === "data_scientist" ? "ML & Vận hành" : "Quản trị"}
              </NavLink>
            ) : null}
          </>
        ) : (
          <>
            <a href="/#khoa-hoc-noi-bat" className="nav-link">📚 Khóa học</a>
            <a href="/#lo-trinh" className="nav-link">🗺️ Lộ trình</a>
            <NavLink to="/about" className={navLinkClass}>ℹ️ Về chúng tôi</NavLink>
            <a href="/#tinh-nang" className="nav-link">✨ Tính năng</a>
            <a href="/#lien-he" className="nav-link">📞 Liên hệ</a>
          </>
        )}
      </nav>

      {isAuthenticated ? (
        <div className="user-box user-box-doc" ref={dropRef}>
          <button
            type="button"
            className="user-avatar-btn"
            onClick={() => setDropOpen((v) => !v)}
            aria-expanded={dropOpen}
            aria-haspopup="true"
          >
            <span className="user-avatar" aria-hidden>{initial}</span>
            <span className="user-name">{displayName}</span>
            <span className="user-chevron" aria-hidden>{dropOpen ? "▲" : "▼"}</span>
          </button>

          {dropOpen && (
            <div className="user-dropdown" role="menu">
              <div className="user-dropdown-header">
                <div className="user-dropdown-avatar">{initial}</div>
                <div>
                  <div className="user-dropdown-name">{displayName}</div>
                  <div className="user-dropdown-email">{user?.email}</div>
                  {user?.role && (
                    <span className="user-dropdown-role">
                      {user.role === "admin" ? "Quản trị viên" : user.role === "data_scientist" ? "Data Scientist" : "Học viên"}
                    </span>
                  )}
                </div>
              </div>
              <div className="user-dropdown-divider" />
              <Link
                to="/profile"
                className="user-dropdown-item"
                role="menuitem"
                onClick={() => setDropOpen(false)}
              >
                👤 Hồ sơ cá nhân
              </Link>
              <Link
                to="/profile?tab=password"
                className="user-dropdown-item"
                role="menuitem"
                onClick={() => setDropOpen(false)}
              >
                🔐 Đổi mật khẩu
              </Link>
              <Link
                to="/profile?tab=avatar"
                className="user-dropdown-item"
                role="menuitem"
                onClick={() => setDropOpen(false)}
              >
                🖼️ Thay đổi ảnh đại diện
              </Link>
              <Link
                to="/dashboard"
                className="user-dropdown-item"
                role="menuitem"
                onClick={() => setDropOpen(false)}
              >
                📊 Tiến độ học tập
              </Link>
              <div className="user-dropdown-divider" />
              <button
                type="button"
                className="user-dropdown-item user-dropdown-item--danger"
                role="menuitem"
                onClick={() => { setDropOpen(false); logout(); }}
              >
                🚪 Đăng xuất
              </button>
            </div>
          )}
        </div>
      ) : (
        <div className="user-box">
          <Link to="/login" className="btn btn-ghost btn-sm">Đăng nhập</Link>
          <Link to="/register" className="btn btn-sm">Đăng ký miễn phí</Link>
        </div>
      )}
    </header>
  );
}
