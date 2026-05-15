import { useCallback, useEffect, useState } from "react";

import { useAuth } from "../context/useAuth.js";
import {
  createCourseApi,
  deleteCourseApi,
  getCoursesApi,
  patchCourseApi,
} from "../services/api.js";

const LEVELS = [
  { value: "beginner", label: "Beginner" },
  { value: "intermediate", label: "Intermediate" },
  { value: "advanced", label: "Advanced" },
];

export function AdminManageCoursesPage() {
  const { authFetch } = useAuth();
  const [courses, setCourses] = useState([]);
  const [error, setError] = useState("");
  const [form, setForm] = useState({
    title: "",
    description: "",
    level: "beginner",
    thumbnail: "",
    is_active: true,
  });
  const [editing, setEditing] = useState(null);

  const load = useCallback(async () => {
    const data = await authFetch((t) => getCoursesApi(t));
    setCourses(Array.isArray(data) ? data : data.results || []);
  }, [authFetch]);

  useEffect(() => {
    load().catch((e) => setError(e.message));
  }, [load]);

  const onSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      if (editing) {
        await authFetch((t) => patchCourseApi(editing.id, form, t));
        setEditing(null);
      } else {
        await authFetch((t) => createCourseApi(form, t));
      }
      setForm({ title: "", description: "", level: "beginner", thumbnail: "", is_active: true });
      await load();
    } catch (err) {
      setError(err.message);
    }
  };

  const onEdit = (c) => {
    setEditing(c);
    setForm({
      title: c.title,
      description: c.description || "",
      level: c.level,
      thumbnail: c.thumbnail || "",
      is_active: c.is_active,
    });
  };

  const onDelete = async (id) => {
    if (!window.confirm("Xóa khóa học này?")) return;
    setError("");
    try {
      await authFetch((t) => deleteCourseApi(id, t));
      await load();
    } catch (err) {
      setError(err.message);
    }
  };

  const cancelEdit = () => {
    setEditing(null);
    setForm({ title: "", description: "", level: "beginner", thumbnail: "", is_active: true });
  };

  return (
    <div className="stack admin-manage">
      <h1>Quản lý khóa học</h1>
      {error ? <p className="error">{error}</p> : null}

      <form className="card" onSubmit={onSubmit}>
        <h2>{editing ? `Sửa khóa #${editing.id}` : "Thêm khóa học"}</h2>
        <label className="field">
          <span>Tiêu đề</span>
          <input
            value={form.title}
            onChange={(e) => setForm((p) => ({ ...p, title: e.target.value }))}
            required
          />
        </label>
        <label className="field">
          <span>Mô tả</span>
          <textarea
            value={form.description}
            onChange={(e) => setForm((p) => ({ ...p, description: e.target.value }))}
            rows={3}
          />
        </label>
        <label className="field">
          <span>Level</span>
          <select value={form.level} onChange={(e) => setForm((p) => ({ ...p, level: e.target.value }))}>
            {LEVELS.map((o) => (
              <option key={o.value} value={o.value}>
                {o.label}
              </option>
            ))}
          </select>
        </label>
        <label className="field">
          <span>Thumbnail URL</span>
          <input
            value={form.thumbnail}
            onChange={(e) => setForm((p) => ({ ...p, thumbnail: e.target.value }))}
            placeholder="https://..."
          />
        </label>
        <label className="field row">
          <input
            type="checkbox"
            checked={form.is_active}
            onChange={(e) => setForm((p) => ({ ...p, is_active: e.target.checked }))}
          />
          <span>Đang hoạt động</span>
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
        <h2>Danh sách ({courses.length})</h2>
        <div className="admin-table-wrap">
          <table className="admin-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Tiêu đề</th>
                <th>Level</th>
                <th>Active</th>
                <th />
              </tr>
            </thead>
            <tbody>
              {courses.map((c) => (
                <tr key={c.id}>
                  <td>{c.id}</td>
                  <td>{c.title}</td>
                  <td>{c.level}</td>
                  <td>{c.is_active ? "Có" : "Không"}</td>
                  <td className="admin-actions">
                    <button type="button" className="btn btn-secondary btn-sm" onClick={() => onEdit(c)}>
                      Sửa
                    </button>
                    <button type="button" className="btn btn-secondary btn-sm" onClick={() => onDelete(c.id)}>
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
