import { useCallback, useEffect, useState } from "react";

import { useAuth } from "../context/useAuth.js";
import {
  createLessonApi,
  deleteLessonApi,
  getCoursesApi,
  getLessonsApi,
  patchLessonApi,
} from "../services/api.js";

export function AdminManageLessonsPage() {
  const { authFetch } = useAuth();
  const [courses, setCourses] = useState([]);
  const [lessons, setLessons] = useState([]);
  const [error, setError] = useState("");
  const [form, setForm] = useState({
    course: "",
    title: "",
    content: "",
    order_num: 1,
    duration: 0,
  });
  const [editing, setEditing] = useState(null);

  const load = useCallback(async () => {
    const [c, l] = await Promise.all([
      authFetch((t) => getCoursesApi(t)),
      authFetch((t) => getLessonsApi(t)),
    ]);
    setCourses(Array.isArray(c) ? c : c.results || []);
    setLessons(Array.isArray(l) ? l : l.results || []);
  }, [authFetch]);

  useEffect(() => {
    load().catch((e) => setError(e.message));
  }, [load]);

  const onSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const payload = {
        course: Number(form.course),
        title: form.title,
        content: form.content,
        order_num: Number(form.order_num),
        duration: Number(form.duration) || 0,
      };
      if (editing) {
        await authFetch((t) => patchLessonApi(editing.id, payload, t));
        setEditing(null);
      } else {
        await authFetch((t) => createLessonApi(payload, t));
      }
      setForm({ course: "", title: "", content: "", order_num: 1, duration: 0 });
      await load();
    } catch (err) {
      setError(err.message);
    }
  };

  const onEdit = (row) => {
    setEditing(row);
    setForm({
      course: String(row.course),
      title: row.title,
      content: row.content || "",
      order_num: row.order_num,
      duration: row.duration,
    });
  };

  const onDelete = async (id) => {
    if (!window.confirm("Xóa bài học này?")) return;
    setError("");
    try {
      await authFetch((t) => deleteLessonApi(id, t));
      await load();
    } catch (err) {
      setError(err.message);
    }
  };

  const cancelEdit = () => {
    setEditing(null);
    setForm({ course: "", title: "", content: "", order_num: 1, duration: 0 });
  };

  return (
    <div className="stack admin-manage">
      <h1>Quản lý bài học</h1>
      {error ? <p className="error">{error}</p> : null}

      <form className="card" onSubmit={onSubmit}>
        <h2>{editing ? `Sửa bài #${editing.id}` : "Thêm bài học"}</h2>
        <label className="field">
          <span>Khóa học (course id)</span>
          <select
            value={form.course}
            onChange={(e) => setForm((p) => ({ ...p, course: e.target.value }))}
            required
          >
            <option value="">— Chọn —</option>
            {courses.map((c) => (
              <option key={c.id} value={c.id}>
                #{c.id} {c.title}
              </option>
            ))}
          </select>
        </label>
        <label className="field">
          <span>Tiêu đề</span>
          <input
            value={form.title}
            onChange={(e) => setForm((p) => ({ ...p, title: e.target.value }))}
            required
          />
        </label>
        <label className="field">
          <span>Nội dung</span>
          <textarea
            value={form.content}
            onChange={(e) => setForm((p) => ({ ...p, content: e.target.value }))}
            rows={4}
          />
        </label>
        <label className="field">
          <span>Thứ tự (order_num)</span>
          <input
            type="number"
            min={1}
            value={form.order_num}
            onChange={(e) => setForm((p) => ({ ...p, order_num: e.target.value }))}
            required
          />
        </label>
        <label className="field">
          <span>Thời lượng (phút)</span>
          <input
            type="number"
            min={0}
            value={form.duration}
            onChange={(e) => setForm((p) => ({ ...p, duration: e.target.value }))}
          />
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

      <div className="card">
        <h2>Danh sách ({lessons.length})</h2>
        <div className="admin-table-wrap">
          <table className="admin-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Course</th>
                <th>Tiêu đề</th>
                <th>Order</th>
                <th />
              </tr>
            </thead>
            <tbody>
              {lessons.map((row) => (
                <tr key={row.id}>
                  <td>{row.id}</td>
                  <td>{row.course}</td>
                  <td>{row.title}</td>
                  <td>{row.order_num}</td>
                  <td className="admin-actions">
                    <button type="button" className="btn btn-secondary btn-sm" onClick={() => onEdit(row)}>
                      Sửa
                    </button>
                    <button type="button" className="btn btn-secondary btn-sm" onClick={() => onDelete(row.id)}>
                      Xóa
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
