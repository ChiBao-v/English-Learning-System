/**
 * Chuẩn hoá nội dung thô (từ API) thành markdown dễ đọc hơn.
 */
export function enhanceLessonMarkdown(raw) {
  if (!raw || typeof raw !== "string") return "";
  let s = raw.trim();

  // Đưa các nhãn mục thành tiêu đề cấp 3
  s = s.replace(/^Từ vựng:\s*$/m, "### Từ vựng");
  s = s.replace(/^Ví dụ:\s*$/m, "### Ví dụ");
  s = s.replace(/^Đoạn đọc\s*$/m, "### Đoạn đọc");
  s = s.replace(/^---\s*\nĐoạn đọc\s*$/m, "---\n\n### Đoạn đọc");

  return s;
}

/** Bỏ tiền tố "A. " trên text đáp án để hiển thị gọn trong ô chọn */
export function stripLeadingOptionLetter(text) {
  if (!text) return "";
  return String(text).replace(/^[A-H]\.\s*/i, "").trim();
}
