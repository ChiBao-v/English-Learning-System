import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import { enhanceLessonMarkdown } from "../utils/lessonMarkdown.js";

const components = {
  h1: ({ children }) => <h1 className="md-heading md-h1">{children}</h1>,
  h2: ({ children }) => <h2 className="md-heading md-h2 lesson-doc-page-title">{children}</h2>,
  h3: ({ children }) => <h3 className="md-heading md-h3">{children}</h3>,
  h4: ({ children }) => <h4 className="md-heading md-h4">{children}</h4>,
  p: ({ children }) => <p className="md-p">{children}</p>,
  hr: () => <hr className="md-hr" />,
  ul: ({ children }) => <ul className="md-ul">{children}</ul>,
  ol: ({ children }) => <ol className="md-ol">{children}</ol>,
  li: ({ children }) => <li className="md-li">{children}</li>,
  strong: ({ children }) => <strong className="md-strong">{children}</strong>,
  em: ({ children }) => <em className="md-em">{children}</em>,
  blockquote: ({ children }) => <blockquote className="md-quote">{children}</blockquote>,
  table: ({ children }) => (
    <div className="md-table-wrap">
      <table className="md-table">{children}</table>
    </div>
  ),
  thead: ({ children }) => <thead className="md-thead">{children}</thead>,
  tbody: ({ children }) => <tbody>{children}</tbody>,
  tr: ({ children }) => <tr className="md-tr">{children}</tr>,
  th: ({ children }) => <th className="md-th">{children}</th>,
  td: ({ children }) => <td className="md-td">{children}</td>,
};

export function LessonMarkdownBody({ content }) {
  const text = enhanceLessonMarkdown(content || "");
  return (
    <div className="lesson-markdown lesson-markdown-prose">
      <ReactMarkdown remarkPlugins={[remarkGfm]} components={components}>
        {text}
      </ReactMarkdown>
    </div>
  );
}
