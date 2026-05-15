/**
 * Chuẩn hóa mô tả khóa học để hiển thị (tránh metadata JSON từ import cũ).
 */
export function formatCourseDescription(raw) {
  if (raw == null || typeof raw !== "string") return "";
  const t = raw.trim();
  if (!t) return "";
  if (t.startsWith("{") && t.includes('"course_id"') && t.includes('"content_mode"')) {
    return "";
  }
  return raw;
}

export function shortCourseDescription(raw, maxLen = 140) {
  const s = formatCourseDescription(raw).replace(/\s+/g, " ").trim();
  if (!s) return "";
  return s.length > maxLen ? `${s.slice(0, maxLen).trim()}…` : s;
}
