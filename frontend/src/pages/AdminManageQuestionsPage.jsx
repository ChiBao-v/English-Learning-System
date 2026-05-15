import { useCallback, useEffect, useState } from "react";

import { useAuth } from "../context/useAuth.js";
import {
  createQuestionApi,
  deleteQuestionApi,
  getLessonsApi,
  getQuestionsApi,
  patchQuestionApi,
} from "../services/api.js";

export function AdminManageQuestionsPage() {
  const { authFetch } = useAuth();
  const [lessons, setLessons] = useState([]);
  const [lessonId, setLessonId] = useState("");
  const [questions, setQuestions] = useState([]);
  const [error, setError] = useState("");
  const [form, setForm] = useState({
    content: "",
    question_type: "multiple_choice",
    options: '["A", "B", "C", "D"]',
    answer: "",
    difficulty: 1,
    hint: "",
    skill_type: "reading",
  });
  const [editing, setEditing] = useState(null);

  const loadLessons = useCallback(async () => {
    const l = await authFetch((t) => getLessonsApi(t));
    setLessons(Array.isArray(l) ? l : l.results || []);
  }, [authFetch]);

  useEffect(() => {
    loadLessons().catch((e) => setError(e.message));
  }, [loadLessons]);

  const loadQuestions = async (lid) => {
    if (!lid) {
      setQuestions([]);
      return;
    }
    const data = await authFetch((t) => getQuestionsApi(t));
    const list = Array.isArray(data) ? data : data.results || [];
    const lidNum = Number(lid);
    setQuestions(list.filter((q) => q.lesson === lidNum));
  };

  useEffect(() => {
    if (!lessonId) return;
    loadQuestions(lessonId).catch((e) => setError(e.message));
  }, [lessonId, authFetch]);

  const onSubmit = async (e) => {
    e.preventDefault();
    setError("");
    let optionsParsed;
    try {
      optionsParsed = JSON.parse(form.options || "[]");
    } catch {
      setError("Options phải là JSON hợp lệ (mảng chuỗi).");
      return;
    }
    try {
      const payload = {
        lesson: Number(lessonId),
        content: form.content,
        question_type: form.question_type,
        options: optionsParsed,
        answer: form.answer,
        difficulty: Number(form.difficulty) || 1,
        hint: form.hint,
        skill_type: form.skill_type,
      };
      if (editing) {
        await authFetch((t) => patchQuestionApi(editing.id, payload, t));
        setEditing(null);
      } else {
        await authFetch((t) => createQuestionApi(payload, t));
      }
      setForm({
        content: "",
        question_type: "multiple_choice",
        options: '["A", "B", "C", "D"]',
        answer: "",
        difficulty: 1,
        hint: "",
        skill_type: "reading",
      });
      await loadQuestions(lessonId);
    } catch (err) {
      setError(err.message);
    }
  };

  const onEdit = (q) => {
    setEditing(q);
    setForm({
      content: q.content,
      question_type: q.question_type,
      options: JSON.stringify(q.options || []),
      answer: q.answer,
      difficulty: q.difficulty,
      hint: q.hint || "",
      skill_type: q.skill_type,
    });
  };

  const onDelete = async (id) => {
    if (!window.confirm("Xóa câu hỏi này?")) return;
    setError("");
    try {
      await authFetch((t) => deleteQuestionApi(id, t));
      await loadQuestions(lessonId);
    } catch (err) {
      setError(err.message);
    }
  };

  const cancelEdit = () => {
    setEditing(null);
    setForm({
      content: "",
      question_type: "multiple_choice",
      options: '["A", "B", "C", "D"]',
      answer: "",
      difficulty: 1,
      hint: "",
      skill_type: "reading",
    });
  };

  return (
    <div className="stack admin-manage">
      <h1>Quản lý câu hỏi</h1>
      {error ? <p className="error">{error}</p> : null}

      <div className="card">
        <label className="field">
          <span>Chọn bài học (lesson)</span>
          <select value={lessonId} onChange={(e) => setLessonId(e.target.value)}>
            <option value="">— Chọn bài học —</option>
            {lessons.map((row) => (
              <option key={row.id} value={row.id}>
                #{row.id} — {row.title} (course {row.course})
              </option>
            ))}
          </select>
        </label>
      </div>

      {lessonId ? (
        <form className="card" onSubmit={onSubmit}>
          <h2>{editing ? `Sửa câu #${editing.id}` : "Thêm câu hỏi"}</h2>
          <label className="field">
            <span>Nội dung câu</span>
            <textarea
              value={form.content}
              onChange={(e) => setForm((p) => ({ ...p, content: e.target.value }))}
              rows={3}
              required
            />
          </label>
          <label className="field">
            <span>Loại câu</span>
            <select
              value={form.question_type}
              onChange={(e) => setForm((p) => ({ ...p, question_type: e.target.value }))}
            >
              <option value="multiple_choice">multiple_choice</option>
              <option value="true_false">true_false</option>
              <option value="fill_in_blank">fill_in_blank</option>
            </select>
          </label>
          <label className="field">
            <span>Options (JSON array)</span>
            <textarea
              value={form.options}
              onChange={(e) => setForm((p) => ({ ...p, options: e.target.value }))}
              rows={2}
            />
          </label>
          <label className="field">
            <span>Đáp án đúng</span>
            <input
              value={form.answer}
              onChange={(e) => setForm((p) => ({ ...p, answer: e.target.value }))}
              required
            />
          </label>
          <label className="field">
            <span>Độ khó (1–5)</span>
            <input
              type="number"
              min={1}
              max={5}
              value={form.difficulty}
              onChange={(e) => setForm((p) => ({ ...p, difficulty: e.target.value }))}
            />
          </label>
          <label className="field">
            <span>Skill</span>
            <select
              value={form.skill_type}
              onChange={(e) => setForm((p) => ({ ...p, skill_type: e.target.value }))}
            >
              <option value="listening">listening</option>
              <option value="reading">reading</option>
              <option value="grammar">grammar</option>
              <option value="vocabulary">vocabulary</option>
            </select>
          </label>
          <label className="field">
            <span>Hint</span>
            <input value={form.hint} onChange={(e) => setForm((p) => ({ ...p, hint: e.target.value }))} />
          </label>
          <div className="row">
            <button className="btn" type="submit">
              {editing ? "Cập nhật" : "Tạo mới"}
            </button>
            {editing ? (
              <button type="button" className="btn btn-secondary" onClick={cancelEdit}>
                Hủy sửa
              </button>
            ) : null}
          </div>
        </form>
      ) : null}

      {lessonId ? (
        <div className="card">
          <h2>Câu hỏi của bài ({questions.length})</h2>
          <div className="admin-table-wrap">
            <table className="admin-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Preview</th>
                  <th>Skill</th>
                  <th />
                </tr>
              </thead>
              <tbody>
                {questions.map((q) => (
                  <tr key={q.id}>
                    <td>{q.id}</td>
                    <td className="admin-preview">{q.content?.slice(0, 80)}...</td>
                    <td>{q.skill_type}</td>
                    <td className="admin-actions">
                      <button type="button" className="btn btn-secondary btn-sm" onClick={() => onEdit(q)}>
                        Sửa
                      </button>
                      <button type="button" className="btn btn-secondary btn-sm" onClick={() => onDelete(q.id)}>
                        Xóa
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      ) : null}
    </div>
  );
}
