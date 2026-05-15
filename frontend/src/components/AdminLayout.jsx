import { NavLink, Outlet } from "react-router-dom";

import { useAuth } from "../context/useAuth.js";

const DJANGO_ADMIN = import.meta.env.VITE_DJANGO_ADMIN_URL || "http://127.0.0.1:8000/admin/";

const NAV_ITEMS = [
  { to: "/admin", end: true,            icon: "📊", label: "Tổng quan & ML" },
  { to: "/admin/ml",                    icon: "🤖", label: "ML Monitor" },
  { to: "/admin/courses",               icon: "📚", label: "Quản lý khóa học",  adminOnly: true },
  { to: "/admin/lessons",               icon: "📄", label: "Quản lý bài học",   adminOnly: true },
  { to: "/admin/questions",             icon: "❓", label: "Quản lý câu hỏi",   adminOnly: true },
];

export function AdminLayout() {
  const { user } = useAuth();
  const isAdmin = user?.role === "admin";

  return (
    <div className="admin-app-layout">
      <aside className="admin-sidebar">
        <div className="admin-sidebar-title">Bảng điều khiển</div>
        <nav className="admin-sidebar-nav">
          {NAV_ITEMS.filter((item) => !item.adminOnly || isAdmin).map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              className={({ isActive }) => "admin-nav-link" + (isActive ? " active" : "")}
            >
              <span className="admin-nav-icon">{item.icon}</span>
              {item.label}
            </NavLink>
          ))}

          <div style={{ borderTop: "1px solid var(--border)", margin: "12px 0", paddingTop: 12 }}>
            <a
              className="admin-nav-link"
              href={DJANGO_ADMIN}
              target="_blank"
              rel="noreferrer"
              style={{ fontSize: "0.82rem" }}
            >
              <span className="admin-nav-icon">🔧</span>
              Django Admin ↗
            </a>
            <NavLink to="/courses" className="admin-nav-link" style={{ fontSize: "0.82rem" }}>
              <span className="admin-nav-icon">←</span>
              Về khu học tập
            </NavLink>
          </div>

          {!isAdmin && (
            <p className="admin-muted" style={{ fontSize: "0.78rem", padding: "0 8px", marginTop: 8 }}>
              Data Scientist: xem tổng quan và phân phối feature.
            </p>
          )}
        </nav>
      </aside>
      <main className="admin-main">
        <Outlet />
      </main>
    </div>
  );
}
