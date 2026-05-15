/**
 * Tách nhãn dạng "Task 1", "Phần 2", "Part 3" ở đầu stem câu hỏi (MCQ) để hiển thị badge.
 */
export function parseQuestionSection(content) {
  if (content == null || typeof content !== "string") return { sectionLabel: null, stem: "" };
  const raw = content.trim();
  if (!raw) return { sectionLabel: null, stem: "" };

  const lines = raw.split("\n");
  const firstLine = lines[0].replace(/\*\*/g, "").trim();

  const onlyTitle =
    /^(task\s*\d+|phần\s*\d+|part\s*\d+|bài\s*\d+)\s*[:.]?\s*$/i.exec(firstLine);
  if (onlyTitle) {
    const sectionLabel = titleCaseSection(onlyTitle[1].replace(/\s+/g, " "));
    const stem = lines.slice(1).join("\n").trim();
    return { sectionLabel, stem: stem || raw };
  }

  const withRest =
    /^(task\s*\d+|phần\s*\d+|part\s*\d+|bài\s*\d+)\s*[:.]\s*(.+)$/i.exec(firstLine);
  if (withRest) {
    const sectionLabel = titleCaseSection(withRest[1].replace(/\s+/g, " "));
    const stem = [withRest[2], ...lines.slice(1)].join("\n").trim();
    return { sectionLabel, stem: stem || raw };
  }

  return { sectionLabel: null, stem: raw };
}

function titleCaseSection(s) {
  const t = s.trim();
  if (!t) return t;
  return t.charAt(0).toUpperCase() + t.slice(1);
}
