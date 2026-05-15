import { useState } from "react";

import { LessonMarkdownBody } from "./LessonMarkdownBody.jsx";

export function LessonDocPages({ pages }) {
  const [idx, setIdx] = useState(0);
  if (!pages?.length) return null;
  const safe = Math.min(idx, pages.length - 1);
  const current = pages[safe];

  return (
    <div className="lesson-doc-pages">
      <div className="lesson-doc-tabs" role="tablist" aria-label="Trang tài liệu">
        {pages.map((_, i) => (
          <button
            key={i}
            type="button"
            role="tab"
            aria-selected={i === safe}
            className={`lesson-doc-tab${i === safe ? " lesson-doc-tab--active" : ""}`}
            onClick={() => setIdx(i)}
          >
            Trang {i + 1}
          </button>
        ))}
      </div>
      <div className="lesson-doc-panel" role="tabpanel">
        <LessonMarkdownBody content={current} />
      </div>
      {pages.length > 1 ? (
        <div className="lesson-doc-nav">
          <button type="button" className="btn btn-secondary btn-sm" disabled={safe <= 0} onClick={() => setIdx((j) => j - 1)}>
            ← Trang trước
          </button>
          <span className="muted small">
            {safe + 1} / {pages.length}
          </span>
          <button
            type="button"
            className="btn btn-secondary btn-sm"
            disabled={safe >= pages.length - 1}
            onClick={() => setIdx((j) => j + 1)}
          >
            Trang sau →
          </button>
        </div>
      ) : null}
    </div>
  );
}
