import { useState } from "react";

import { loginApi, meApi, refreshTokenApi, registerApi } from "../services/api.js";
import { AuthContext } from "./AuthContextObject.js";

const STORAGE_KEY = "toeic_auth";

const EMPTY_AUTH = { accessToken: null, refreshToken: null, user: null };

/** Đọc trường `exp` (giây) từ payload JWT mà không cần thư viện. */
function jwtExp(token) {
  try {
    const payload = JSON.parse(atob(token.split(".")[1]));
    return typeof payload.exp === "number" ? payload.exp : null;
  } catch {
    return null;
  }
}

/** Token coi như hết hạn nếu không đọc được exp hoặc exp đã qua. */
function isJwtExpired(token) {
  const exp = jwtExp(token);
  if (exp == null) return true;
  return Date.now() >= exp * 1000;
}

function readSavedAuth() {
  const saved = localStorage.getItem(STORAGE_KEY);
  if (!saved) return { ...EMPTY_AUTH };

  try {
    const parsed = JSON.parse(saved);
    // Nếu refresh token đã hết hạn thì không còn cách nào lấy access mới
    // → xóa sạch, coi như chưa đăng nhập để app đưa thẳng về /login.
    if (!parsed.refreshToken || isJwtExpired(parsed.refreshToken)) {
      localStorage.removeItem(STORAGE_KEY);
      return { ...EMPTY_AUTH };
    }
    return parsed;
  } catch {
    localStorage.removeItem(STORAGE_KEY);
    return { ...EMPTY_AUTH };
  }
}

export function AuthProvider({ children }) {
  const [authState, setAuthState] = useState(readSavedAuth);
  const { accessToken, refreshToken, user } = authState;

  const persistState = (nextState) => {
    setAuthState(nextState);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(nextState));
  };

  const login = async (email, password) => {
    const tokenData = await loginApi({ email, password });
    const me = await meApi(tokenData.access);
    persistState({
      accessToken: tokenData.access,
      refreshToken: tokenData.refresh,
      user: me,
    });
    return me;
  };

  const register = async ({ email, password, username, first_name, last_name }) => {
    await registerApi({ email, password, username, first_name, last_name });
    return login(email, password);
  };

  const logout = () => {
    setAuthState({ accessToken: null, refreshToken: null, user: null });
    localStorage.removeItem(STORAGE_KEY);
  };

  const authFetch = async (requestFn) => {
    try {
      return await requestFn(accessToken);
    } catch (error) {
      if (!refreshToken) {
        logout();
        throw new Error("Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại.");
      }

      try {
        const refreshed = await refreshTokenApi(refreshToken);
        persistState({
          accessToken: refreshed.access,
          refreshToken,
          user,
        });
        return await requestFn(refreshed.access);
      } catch {
        // Refresh token cũng hết hạn → đăng xuất, ProtectedRoute sẽ đưa về /login
        logout();
        throw new Error("Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại.");
      }
    }
  };

  const updateUser = (updatedUser) => {
    persistState({ accessToken, refreshToken, user: { ...user, ...updatedUser } });
  };

  const value = {
    user,
    accessToken,
    isAuthenticated: Boolean(accessToken && user),
    isBootstrapping: false,
    login,
    register,
    logout,
    authFetch,
    updateUser,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
