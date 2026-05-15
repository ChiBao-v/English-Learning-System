export const DOC_PAGE_BREAK = "<<<DOC_PAGE_BREAK>>>";
export const DOC_PAGE_END_THEORY = "<<<DOC_PAGE_END_THEORY>>>";

/**
 * Tách nội dung bài học: phần lý thuyết nhiều trang + phần đoạn đọc / từ / ví dụ.
 */
export function splitLessonDocument(raw) {
  const text = raw || "";
  if (!text.includes(DOC_PAGE_END_THEORY)) {
    return { mode: "single", full: text };
  }
  const parts = text.split(DOC_PAGE_END_THEORY);
  const theoryPart = (parts[0] || "").trim();
  const supplemental = (parts.slice(1).join(DOC_PAGE_END_THEORY) || "").trim();
  const pageChunks = theoryPart
    .split(DOC_PAGE_BREAK)
    .map((s) => s.trim())
    .filter(Boolean);
  return { mode: "paged", pages: pageChunks, supplemental };
}
