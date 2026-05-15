import { Navigate } from "react-router-dom";

import { useAuth } from "../context/useAuth.js";

/** Chỉ Admin — CRUD nội dung (khóa học, bài, câu hỏi). */
export function AdminOnlyRoute({ children }) {
  const { user, isAuthenticated, isBootstrapping } = useAuth();

  if (isBootstrapping) {
    return <div className="center-box">Đang tải...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  if (user?.role !== "admin") {
    return <Navigate to="/admin" replace />;
  }

  return children;
}
