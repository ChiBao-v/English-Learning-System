import { Navigate } from "react-router-dom";

import { useAuth } from "../context/useAuth.js";

const STAFF_ROLES = ["admin", "data_scientist"];

/** Admin hoặc Data Scientist — dashboard vận hành / ML. */
export function StaffRoute({ children }) {
  const { user, isAuthenticated, isBootstrapping } = useAuth();

  if (isBootstrapping) {
    return <div className="center-box">Đang tải...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  if (!STAFF_ROLES.includes(user?.role)) {
    return <Navigate to="/courses" replace />;
  }

  return children;
}
