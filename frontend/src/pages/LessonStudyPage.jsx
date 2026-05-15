import { useEffect, useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";

import { LessonDocPages } from "../components/LessonDocPages.jsx";
import { LessonMarkdownBody } from "../components/LessonMarkdownBody.jsx";
import { LessonModeTabs } from "../components/LessonModeTabs.jsx";
import { LessonProgressHud } from "../components/LessonProgressHud.jsx";
import { LessonSidebar } from "../components/LessonSidebar.jsx";
import { useAuth } from "../context/useAuth.js";
import { getLessonDetailApi } from "../services/api.js";
import { splitLessonDocument } from "../utils/splitLessonDoc.js";

export function LessonStudyPage() {
  const { lessonId } = useParams();
  const { authFetch } = useAuth();
  const [lesson, setLesson] = useState(null);
  const [courseLessons, setCourseLessons] = useState([]);
  const [error, setError] = useState("");
  const [elapsedSec, setElapsedSec] = useState(0);

  useEffect(() => {
    const t0 = Date.now();
    const id = window.setInterval(() => {
      setElapsedSec(Math.floor((Date.now() - t0) / 1000));
    }, 1000);
    return () => window.clearInterval(id);
  }, [lessonId]);

  useEffect(() => {
    let isMounted = true;
    const run = async () => {
      try {
        const data = await authFetch((token) => getLessonDetailApi(lessonId, token));
        if (isMounted) {
          setLesson(data.lesson);
          setCourseLessons(data.course_lessons || []);
        }
      } catch (loadError) {
        if (isMounted) setError(loadError.message);
      }
    };
    run();
    return () => {
      isMounted = false;
    };
  }, [authFetch, lessonId]);

  const courseProgressPct = useMemo(() => {
    if (!courseLessons.length) return 0;
    const done = courseLessons.filter((l) => l.completed).length;
    return Math.round((done / courseLessons.length) * 100);
  }, [courseLessons]);

  const docParts = useMemo(() => splitLessonDocument(lesson?.content || ""), [lesson?.content]);
  const isListeningCourse = lesson?.course_skill === "listening";
  const isReadingCourse = lesson?.course_skill === "reading";
  const hasTranscript = Boolean((lesson?.transcript || "").trim());
  const hasReadingPassage = Boolean((lesson?.reading_passage || "").trim());
  const hasStudyContent = Boolean(lesson?.content && String(lesson.content).trim());

  if (error) return <div className="card error">{error}</div>;
  if (!lesson) return <div className="card">Đang tải bài học...</div>;

  return (
    <div className="lesson-layout-doc">
      <LessonSidebar courseLessons={courseLessons} lessonId={Number(lessonId)} courseTitle={lesson?.course_title} />

      <div className="lesson-main-doc lesson-main-doc--with-hud">
        <div className="lesson-top-bar">
          <div className="lesson-top-bar-left">
            <LessonModeTabs lessonId={lessonId} quizTabLabel={isListeningCourse || isReadingCourse ? "Bài tập" : "Quiz"} />
          </div>
          <LessonProgressHud
            mode="study"
            courseProgressPct={courseProgressPct}
            elapsedSec={elapsedSec}
            quizProgressPct={0}
            scorePct={null}
          />
        </div>

        <header className="lesson-main-header lesson-main-header--flush">
          <h1 className="lesson-main-title">{lesson.title}</h1>
        </header>

        {hasStudyContent ? (
          <article className="lesson-content-shell">
            {docParts.mode === "paged" ? (
              <>
                <LessonDocPages pages={docParts.pages} />
                {docParts.supplemental ? (
                  <div className="lesson-supplemental">
                    <LessonMarkdownBody content={docParts.supplemental} />
                  </div>
                ) : null}
              </>
            ) : (
              <LessonMarkdownBody content={lesson.content} />
            )}
            {isListeningCourse && hasTranscript ? (
              <p className="muted small lesson-transcript-hint">
                Lời thoại đầy đủ (transcript) nằm ở tab <strong>Bài tập</strong>, dưới trình phát audio — dùng nút hiện/ẩn khi cần.
              </p>
            ) : null}
            {isReadingCourse && hasReadingPassage ? (
              <p className="muted small lesson-transcript-hint">
                Bài đọc đầy đủ nằm ở tab <strong>Bài tập</strong> — bật nút Hiện đoạn đọc phía trên câu hỏi khi cần.
              </p>
            ) : null}
          </article>
        ) : isListeningCourse ? (
          <div className="card lesson-listening-placeholder">
            <p className="lesson-listening-placeholder-lead">
              Bài <strong>Nghe</strong> có thể không có tài liệu lý thuyết trên trang này.
            </p>
            <p className="muted">
              Phần <strong>Task / Part</strong> được chuyển thành câu trắc nghiệm trong tab <strong>Bài tập</strong> (kèm audio khi có).
              {hasTranscript ? " Transcript có trong tab đó, dưới audio." : ""}
            </p>
            <Link to={`/lessons/${lessonId}/quiz`} className="btn btn-continue lesson-listening-cta">
              Vào bài tập →
            </Link>
          </div>
        ) : (
          <p className="muted">Chưa có nội dung lý thuyết.</p>
        )}

        <div className="lesson-study-actions lesson-study-actions--inline">
          <Link to="/courses" className="btn btn-secondary">
            ← Khóa học
          </Link>
        </div>

        <div className="lesson-continue-bar">
          <div className="lesson-continue-inner">
            <p className="lesson-continue-text">
              {isListeningCourse && !hasStudyContent ? (
                <>
                  <strong>Tiếp tục:</strong> làm các câu trắc nghiệm theo từng phần (Task / Part) trong mục bài tập.
                </>
              ) : isReadingCourse ? (
                <>
                  <strong>Tiếp tục:</strong> đọc đoạn văn và làm câu hỏi trắc nghiệm trong tab bài tập.
                </>
              ) : (
                <>
                  <strong>Tiếp tục:</strong> làm bài kiểm tra để ghi nhận tiến độ và điểm số.
                </>
              )}
            </p>
            <Link to={`/lessons/${lessonId}/quiz`} className="btn btn-continue">
              {isListeningCourse && !hasStudyContent
                ? "Vào bài tập →"
                : isReadingCourse
                  ? "Tiếp tục → Làm bài tập"
                  : "Tiếp tục → Làm bài Quiz"}
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
