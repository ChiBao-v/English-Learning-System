import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";

import { useAuth } from "../context/useAuth.js";
import { enrollCourseApi, getCoursesApi, getLessonsApi, getStudentDashboardApi } from "../services/api.js";
import { formatCourseDescription } from "../utils/courseDisplay.js";
import { coursePrimaryLessonPath } from "../utils/lessonPaths.js";

const LEVEL_VI = {
  beginner: "Cơ bản",
  intermediate: "Trung cấp",
  advanced: "Nâng cao",
};

const CEFR_RANK = { A1: 1, A2: 2, B1: 3, B2: 4, C1: 5, C2: 6 };

function cefrRank(cefr) {
  const k = (cefr || "").toString().trim().toUpperCase();
  return CEFR_RANK[k] ?? 100;
}

const SKILL_ORDER = ["listening", "reading", "writing", "speaking", "grammar", "vocabulary", "general"];

const SKILL_LABELS_VI = {
  listening: "Kỹ năng Nghe",
  reading: "Kỹ năng Đọc",
  writing: "Kỹ năng Viết",
  speaking: "Kỹ năng Nói",
  grammar: "Ngữ pháp",
  vocabulary: "Từ vựng",
  general: "Khóa tổng hợp",
};

const SKILL_ICONS = {
  listening: "🎧",
  reading: "📖",
  writing: "✍️",
  speaking: "🗣️",
  grammar: "📝",
  vocabulary: "📚",
  general: "🌐",
};

const SKILL_COLORS = {
  listening: "linear-gradient(135deg,#4f46e5 0%,#7c3aed 100%)",
  reading:   "linear-gradient(135deg,#0ea5e9 0%,#06b6d4 100%)",
  writing:   "linear-gradient(135deg,#10b981 0%,#059669 100%)",
  speaking:  "linear-gradient(135deg,#f59e0b 0%,#ef4444 100%)",
  grammar:   "linear-gradient(135deg,#8b5cf6 0%,#6366f1 100%)",
  vocabulary:"linear-gradient(135deg,#ec4899 0%,#f43f5e 100%)",
  general:   "linear-gradient(135deg,#64748b 0%,#475569 100%)",
};

export function CoursesPage() {
  const { authFetch } = useAuth();
  const [courses, setCourses] = useState([]);
  const [lessonByCourse, setLessonByCourse] = useState({});
  const [enrolledIds, setEnrolledIds] = useState(() => new Set());
  const [resumeLessonByCourse, setResumeLessonByCourse] = useState({});
  const [courseProgressRows, setCourseProgressRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [activeSkill, setActiveSkill] = useState("all");

  useEffect(() => {
    let isMounted = true;
    const run = async () => {
      try {
        setError("");
        const [coursesData, lessonsData, dash] = await Promise.all([
          authFetch((token) => getCoursesApi(token)),
          authFetch((token) => getLessonsApi(token)),
          authFetch((token) => getStudentDashboardApi(token)),
        ]);
        if (isMounted) {
          setCourses(coursesData);
          const firstLessonByCourse = lessonsData.reduce((acc, lesson) => {
            if (!acc[lesson.course]) acc[lesson.course] = lesson.id;
            return acc;
          }, {});
          setLessonByCourse(firstLessonByCourse);
          const ids = new Set((dash.course_progress || []).map((c) => c.course_id));
          setEnrolledIds(ids);
          setResumeLessonByCourse(dash.resume_lesson_by_course || {});
          setCourseProgressRows(dash.course_progress || []);
        }
      } catch (loadError) {
        if (isMounted) setError(loadError.message);
      } finally {
        if (isMounted) setLoading(false);
      }
    };
    run();
    return () => { isMounted = false; };
  }, [authFetch]);

  const onEnroll = async (courseId) => {
    try {
      await authFetch((token) => enrollCourseApi(courseId, token));
      setCourses((prev) => prev.map((item) => (item.id === courseId ? { ...item, enrolled: true } : item)));
      setEnrolledIds((prev) => new Set([...prev, courseId]));
    } catch (enrollError) {
      setError(enrollError.message);
    }
  };

  const courseGroups = useMemo(() => {
    const sorted = [...courses].sort((a, b) => {
      const d = cefrRank(a.cefr_level) - cefrRank(b.cefr_level);
      if (d !== 0) return d;
      return (a.title || "").localeCompare(b.title || "");
    });
    const by = new Map();
    for (const c of sorted) {
      const sk = c.skill || "general";
      if (!by.has(sk)) by.set(sk, []);
      by.get(sk).push(c);
    }
    const seen = new Set();
    const out = [];
    for (const sk of SKILL_ORDER) {
      if (by.has(sk)) {
        out.push({ skill: sk, label: SKILL_LABELS_VI[sk] || sk, courses: by.get(sk) });
        seen.add(sk);
      }
    }
    for (const sk of [...by.keys()].sort()) {
      if (!seen.has(sk)) {
        out.push({ skill: sk, label: SKILL_LABELS_VI[sk] || sk, courses: by.get(sk) });
      }
    }
    return out;
  }, [courses]);

  const visibleGroups = useMemo(
    () => activeSkill === "all" ? courseGroups : courseGroups.filter((g) => g.skill === activeSkill),
    [courseGroups, activeSkill],
  );

  if (loading) return <div className="card">Đang tải khóa học...</div>;

  return (
    <div className="stack page-courses">
      <div className="courses-page-hero">
        <div>
          <h1 className="page-title">Khóa học tiếng Anh</h1>
          <p className="muted">Chọn kỹ năng và khóa học phù hợp để bắt đầu lộ trình học của bạn.</p>
        </div>
        <div className="courses-stats-row">
          <div className="courses-stat"><span className="courses-stat-num">{courses.length}</span><span className="courses-stat-label">Khóa học</span></div>
          <div className="courses-stat"><span className="courses-stat-num">{enrolledIds.size}</span><span className="courses-stat-label">Đã đăng ký</span></div>
          <div className="courses-stat"><span className="courses-stat-num">{courseProgressRows.filter(r => r.progress_pct === 100).length}</span><span className="courses-stat-label">Hoàn thành</span></div>
        </div>
      </div>

      {error ? <p className="error">{error}</p> : null}

      <div className="skill-filter-tabs" role="tablist" aria-label="Lọc theo kỹ năng">
        <button
          type="button"
          role="tab"
          aria-selected={activeSkill === "all"}
          className={"skill-filter-tab" + (activeSkill === "all" ? " skill-filter-tab--active" : "")}
          onClick={() => setActiveSkill("all")}
        >
          🌐 Tất cả
        </button>
        {courseGroups.map((g) => (
          <button
            key={g.skill}
            type="button"
            role="tab"
            aria-selected={activeSkill === g.skill}
            className={"skill-filter-tab" + (activeSkill === g.skill ? " skill-filter-tab--active" : "")}
            style={activeSkill === g.skill ? { background: SKILL_COLORS[g.skill] || SKILL_COLORS.general, borderColor: "transparent", color: "#fff" } : {}}
            onClick={() => setActiveSkill(g.skill)}
          >
            {SKILL_ICONS[g.skill] || "📌"} {g.label}
          </button>
        ))}
      </div>

      <div className="courses-by-skill">
        {visibleGroups.map((group) => (
          <section key={group.skill} className="courses-skill-section" aria-label={group.label}>
            <header className="courses-skill-head">
              <h2 className="courses-skill-title">
                {SKILL_ICONS[group.skill] || "📌"} {group.label}
              </h2>
            </header>

            <div className="featured-grid">
              {group.courses.map((course) => {
                const enrolled = course.enrolled || enrolledIds.has(course.id);
                const firstLesson = lessonByCourse[course.id];
                const progressRow = courseProgressRows.find((c) => c.course_id === course.id);
                const progressPct = progressRow?.progress_pct ?? 0;
                const resumeId = resumeLessonByCourse[course.id];
                const showContinue =
                  enrolled && resumeId && progressPct > 0 && progressPct < 100 &&
                  firstLesson && resumeId !== firstLesson;
                const targetLessonId =
                  progressPct > 0 && progressPct < 100 && resumeId ? resumeId : firstLesson;
                const primaryPath = coursePrimaryLessonPath(targetLessonId, course);
                const firstPath = coursePrimaryLessonPath(firstLesson, course);
                const resumePath = coursePrimaryLessonPath(resumeId, course);
                const isSkillQuizCourse = course.skill === "listening" || course.skill === "reading";
                const firstBtnLabel = isSkillQuizCourse ? "Bài tập đầu tiên" : "Học bài đầu tiên";
                const continueLabel = isSkillQuizCourse ? "Tiếp tục bài tập" : "Tiếp tục học";
                const bg = course.thumbnail
                  ? { backgroundImage: `url(${course.thumbnail})` }
                  : { background: SKILL_COLORS[course.skill] || SKILL_COLORS.general };
                const blurb = formatCourseDescription(course.description);

                return (
                  <article key={course.id} className="course-card">
                    <div className="course-card-image" style={bg}>
                      {course.cefr_level && (
                        <span className="course-card-skill-badge">{course.cefr_level}</span>
                      )}
                      {enrolled && progressPct > 0 && (
                        <span className="course-card-progress-badge">{progressPct}%</span>
                      )}
                    </div>
                    <div className="course-card-body">
                      <h3 className="course-card-title">{course.title}</h3>
                      <p className="course-card-tier">
                        {[course.cefr_level, course.level_label || LEVEL_VI[course.level] || course.level]
                          .filter(Boolean)
                          .join(" · ")}
                      </p>
                      {blurb ? <p className="course-card-blurb">{blurb}</p> : null}
                      <p className="course-card-meta">{course.lesson_count ?? 0} bài học</p>

                      <div className="course-actions">
                        {!enrolled ? (
                          <button type="button" className="btn btn-block btn-sm" onClick={() => onEnroll(course.id)}>
                            Đăng ký khóa học
                          </button>
                        ) : firstLesson ? (
                          showContinue ? (
                            <div className="course-lesson-buttons">
                              <Link className="btn btn-secondary btn-block btn-sm" to={firstPath || "#"}>
                                {firstBtnLabel}
                              </Link>
                              <Link className="btn btn-block btn-sm" to={resumePath || "#"}>
                                {continueLabel}
                              </Link>
                            </div>
                          ) : (
                            <Link className="btn btn-block btn-sm" to={primaryPath || "#"}>
                              {progressPct > 0 && progressPct < 100 ? continueLabel : firstBtnLabel}
                            </Link>
                          )
                        ) : (
                          <span className="muted small">Chưa có bài học</span>
                        )}
                        {!enrolled && firstLesson ? (
                          <span className="muted small" style={{ textAlign: "center" }}>
                            Đăng ký để mở bài học
                          </span>
                        ) : null}
                      </div>
                    </div>
                  </article>
                );
              })}
            </div>
          </section>
        ))}
      </div>
    </div>
  );
}
