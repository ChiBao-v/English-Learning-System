export function lessonStudyPath(lessonId) {
  return `/lessons/${lessonId}`;
}

export function lessonQuizPath(lessonId) {
  return `/lessons/${lessonId}/quiz`;
}

/** Từ danh sách khóa học: khóa Nghe / Đọc (A1…) mở thẳng phần bài tập (quiz). */
export function coursePrimaryLessonPath(lessonId, course) {
  if (lessonId == null || lessonId === undefined) return null;
  if (course?.skill === "listening" || course?.skill === "reading") return lessonQuizPath(lessonId);
  return lessonStudyPath(lessonId);
}
