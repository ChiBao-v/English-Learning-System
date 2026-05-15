import { useEffect, useMemo, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

import { LessonMarkdownBody } from "../components/LessonMarkdownBody.jsx";
import { LessonModeTabs } from "../components/LessonModeTabs.jsx";
import { LessonProgressHud } from "../components/LessonProgressHud.jsx";
import { LessonSidebar } from "../components/LessonSidebar.jsx";
import { useAuth } from "../context/useAuth.js";
import { completeLessonApi, getLessonDetailApi, submitAnswerApi } from "../services/api.js";
import { stripLeadingOptionLetter } from "../utils/lessonMarkdown.js";
import { parseQuestionSection } from "../utils/questionSection.js";

const LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

export function LessonQuizPage() {
  const { lessonId } = useParams();
  const navigate = useNavigate();
  const { authFetch } = useAuth();
  const [lesson, setLesson] = useState(null);
  const [courseLessons, setCourseLessons] = useState([]);
  const [index, setIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState("");
  const [questionStartedAt, setQuestionStartedAt] = useState(0);
  const [lessonStartedAt, setLessonStartedAt] = useState(0);
  const [answerChangedCount, setAnswerChangedCount] = useState(0);
  const [usedHint, setUsedHint] = useState(false);
  const [score, setScore] = useState(0);
  const [error, setError] = useState("");
  const [isDone, setIsDone] = useState(false);
  const [elapsedSec, setElapsedSec] = useState(0);
  const [showTranscript, setShowTranscript] = useState(false);
  const [showReadingPassage, setShowReadingPassage] = useState(false);

  useEffect(() => {
    let isMounted = true;
    const run = async () => {
      try {
        const data = await authFetch((token) => getLessonDetailApi(lessonId, token));
        if (isMounted) {
          setLesson(data.lesson);
          setCourseLessons(data.course_lessons || []);
          const now = Date.now();
          setQuestionStartedAt(now);
          setLessonStartedAt(now);
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

  useEffect(() => {
    if (!lessonStartedAt || isDone) return undefined;
    const t = window.setInterval(() => {
      setElapsedSec(Math.floor((Date.now() - lessonStartedAt) / 1000));
    }, 1000);
    return () => window.clearInterval(t);
  }, [lessonStartedAt, isDone]);

  const questions = lesson?.questions || [];
  const currentQuestion = questions[index];
  const isListeningCourse = lesson?.course_skill === "listening";
  const isReadingCourse = lesson?.course_skill === "reading";
  const { sectionLabel, stem } = useMemo(
    () => parseQuestionSection(currentQuestion?.content || ""),
    [currentQuestion?.content],
  );
  const isLastQuestion = useMemo(() => index === questions.length - 1, [index, questions.length]);

  const quizProgressPct = questions.length ? Math.round(((index + (isDone ? 1 : 0)) / questions.length) * 100) : 0;
  const runningAccuracyPct = questions.length ? Math.round((score / Math.min(index + 1, questions.length)) * 100) : 0;

  const transcriptMd = (lesson?.transcript || "").trim();
  const hasTranscript = Boolean(transcriptMd);
  const readingPassageMd = (lesson?.reading_passage || "").trim();
  const hasReadingPassage = Boolean(readingPassageMd);

  const courseProgressPct = useMemo(() => {
    if (!courseLessons.length) return 0;
    const done = courseLessons.filter((l) => l.completed).length;
    return Math.round((done / courseLessons.length) * 100);
  }, [courseLessons]);

  const nextLessonPath = useMemo(() => {
    const rows = courseLessons;
    const i = rows.findIndex((r) => r.id === Number(lessonId));
    if (i < 0 || i >= rows.length - 1) return null;
    const nextId = rows[i + 1].id;
    if (lesson?.course_skill === "listening" || lesson?.course_skill === "reading") return `/lessons/${nextId}/quiz`;
    return `/lessons/${nextId}`;
  }, [courseLessons, lessonId, lesson?.course_skill]);

  const onHint = () => {
    setUsedHint(true);
  };

  const onSubmitAnswer = async () => {
    if (!selectedAnswer || !currentQuestion) return;
    const responseTimeSeconds = (Date.now() - questionStartedAt) / 1000;

    try {
      const result = await authFetch((token) =>
        submitAnswerApi(
          {
            question_id: currentQuestion.id,
            user_answer: selectedAnswer,
            response_time_seconds: responseTimeSeconds,
            answer_changed_count: answerChangedCount,
            hint_used: usedHint,
            attempt_num: 1,
          },
          token,
        ),
      );
      const nextScore = result.is_correct ? score + 1 : score;

      if (result.is_correct) {
        setScore((prev) => prev + 1);
      }

      if (isLastQuestion) {
        const finalScore = (nextScore / questions.length) * 100;
        await authFetch((token) =>
          completeLessonApi(
            {
              lesson_id: Number(lessonId),
              score: Number(finalScore.toFixed(2)),
              time_spent: Math.round((Date.now() - lessonStartedAt) / 1000),
            },
            token,
          ),
        );
        setIsDone(true);
        return;
      }

      setIndex((prev) => prev + 1);
      setSelectedAnswer("");
      setAnswerChangedCount(0);
      setUsedHint(false);
      setQuestionStartedAt(Date.now());
    } catch (submitError) {
      setError(submitError.message);
    }
  };

  const quizTabLabel = isListeningCourse || isReadingCourse ? "Bài tập" : "Quiz";
  const isListening =
    isListeningCourse || currentQuestion?.skill_type === "listening";
  const audioSrc = (currentQuestion?.audio_url || lesson?.audio_url || "").trim();
  const imageSrc = (currentQuestion?.image_url || "").trim();
  const options = currentQuestion?.options || [];

  if (error) return <div className="card error">{error}</div>;
  if (!lesson) return <div className="card">Đang tải bài kiểm tra...</div>;

  if (isDone) {
    return (
      <div className="lesson-layout-doc">
        <LessonSidebar courseLessons={courseLessons} lessonId={Number(lessonId)} courseTitle={lesson?.course_title} />
        <div className="lesson-main-doc lesson-main-doc--with-hud">
          <div className="lesson-top-bar">
            <div className="lesson-top-bar-left">
              <LessonModeTabs lessonId={lessonId} quizTabLabel={quizTabLabel} />
            </div>
            <LessonProgressHud
              mode="quiz"
              courseProgressPct={courseProgressPct}
              elapsedSec={elapsedSec}
              quizProgressPct={100}
              scorePct={questions.length ? Math.round((score / questions.length) * 100) : 0}
            />
          </div>
          <div className="card lesson-done-card">
            <h1>Hoàn thành bài kiểm tra</h1>
            <p>
              Điểm: <strong>{score}</strong> / {questions.length}
            </p>
            <div className="row lesson-done-actions">
              {nextLessonPath ? (
                <Link to={nextLessonPath} className="btn btn-continue">
                  Tiếp tục — Bài tiếp theo →
                </Link>
              ) : null}
              <button type="button" className="btn btn-secondary" onClick={() => navigate("/dashboard")}>
                Về Dashboard
              </button>
              <Link to="/courses" className="btn btn-secondary">
                Danh sách khóa học
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="lesson-layout-doc">
      <LessonSidebar courseLessons={courseLessons} lessonId={Number(lessonId)} />

      <div className="lesson-main-doc lesson-main-doc--with-hud">
        <div className="lesson-top-bar">
          <div className="lesson-top-bar-left">
            <LessonModeTabs lessonId={lessonId} quizTabLabel={quizTabLabel} />
          </div>
          <LessonProgressHud
            mode="quiz"
            courseProgressPct={courseProgressPct}
            elapsedSec={elapsedSec}
            quizProgressPct={quizProgressPct}
            scorePct={runningAccuracyPct}
          />
        </div>

        <header className="lesson-main-header lesson-quiz-header lesson-main-header--flush">
          <h1 className="lesson-main-title">{lesson.title}</h1>
          <p className="muted small lesson-quiz-sub">
            {isListeningCourse
              ? `Nghe audio (nếu có) và chọn một đáp án đúng. Có thể gắn nhãn Task / Part cho từng câu.${hasTranscript ? " Dưới audio có nút hiện transcript khi cần đối chiếu lời thoại." : ""}`
              : isReadingCourse
                ? `Đọc đoạn văn và chọn đáp án.${hasReadingPassage ? " Bạn có thể bật nút Hiện đoạn đọc để xem lại bài đọc khi làm bài." : ""}`
                : "Chọn một đáp án cho mỗi câu."}
          </p>
        </header>

        {currentQuestion ? (
          <section className="lesson-quiz-shell">
            <div className="quiz-step-badge">
              Câu hỏi {index + 1} / {questions.length}
            </div>

            {isReadingCourse && hasReadingPassage ? (
              <div className="lesson-quiz-transcript-block lesson-quiz-passage-block">
                <button
                  type="button"
                  className="btn btn-secondary lesson-quiz-transcript-btn"
                  onClick={() => setShowReadingPassage((v) => !v)}
                  aria-expanded={showReadingPassage}
                >
                  {showReadingPassage ? "Ẩn đoạn đọc" : "Hiện đoạn đọc"}
                </button>
                {showReadingPassage ? (
                  <div className="lesson-quiz-transcript-panel lesson-quiz-reading-passage-panel">
                    <LessonMarkdownBody content={readingPassageMd} />
                  </div>
                ) : null}
              </div>
            ) : null}

            {isListening && audioSrc ? (
              <div className="lesson-quiz-audio-wrap">
                <audio className="lesson-quiz-audio" controls preload="metadata" src={audioSrc}>
                  Trình duyệt không hỗ trợ audio.
                </audio>
              </div>
            ) : isListening ? (
              <p className="muted small">Chưa có liên kết audio cho câu này — dùng nội dung đoạn và đáp án.</p>
            ) : null}

            {isListening && hasTranscript ? (
              <div className="lesson-quiz-transcript-block">
                <button
                  type="button"
                  className="btn btn-secondary lesson-quiz-transcript-btn"
                  onClick={() => setShowTranscript((v) => !v)}
                  aria-expanded={showTranscript}
                >
                  {showTranscript ? "Ẩn transcript" : "Hiện transcript"}
                </button>
                {showTranscript ? (
                  <div className="lesson-quiz-transcript-panel">
                    <LessonMarkdownBody content={transcriptMd} />
                  </div>
                ) : null}
              </div>
            ) : null}

            {sectionLabel ? (
              <div className="quiz-task-badge" role="note">
                {sectionLabel}
              </div>
            ) : null}

            <h2 className="question-stem question-stem-lg">{stem}</h2>

            {isListening && imageSrc ? (
              <img className="quiz-question-image" src={imageSrc} alt="" />
            ) : null}

            <div className="quiz-options-tiles" role="radiogroup" aria-label="Lựa chọn đáp án">
              {options.map((option, optIdx) => {
                const letter = LETTERS[optIdx] || "?";
                const labelOnly = stripLeadingOptionLetter(option);
                const selected = selectedAnswer === option;
                return (
                  <button
                    key={option}
                    type="button"
                    className={`quiz-option-tile ${selected ? "quiz-option-tile--selected" : ""}`}
                    onClick={() => {
                      if (selectedAnswer && selectedAnswer !== option) {
                        setAnswerChangedCount((c) => c + 1);
                      }
                      setSelectedAnswer(option);
                    }}
                  >
                    <span className="quiz-option-tile-letter" aria-hidden>
                      {letter}
                    </span>
                    <span className="quiz-option-tile-text">{labelOnly}</span>
                  </button>
                );
              })}
            </div>

            <div className="quiz-actions-row">
              <button type="button" className="btn btn-secondary btn-hint" onClick={onHint}>
                Gợi ý
              </button>
              <button type="button" className="btn btn-continue" disabled={!selectedAnswer} onClick={onSubmitAnswer}>
                {isLastQuestion ? "Nộp bài" : "Tiếp tục"}
              </button>
            </div>
            {usedHint && currentQuestion.hint ? <p className="hint-box hint-box-soft">Gợi ý: {currentQuestion.hint}</p> : null}
          </section>
        ) : (
          <div className="card">Bài học chưa có câu hỏi.</div>
        )}

        <p className="muted small lesson-quiz-foot">
          <Link to={`/lessons/${lessonId}`}>← Quay lại tài liệu</Link>
        </p>
      </div>
    </div>
  );
}
