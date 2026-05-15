import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "/api/v1";

const SESSION_STORAGE_KEY = "toeic_session_id";

const client = axios.create({
  baseURL: API_BASE_URL,
  headers: { "Content-Type": "application/json" },
});

function getSessionId() {
  const existing = localStorage.getItem(SESSION_STORAGE_KEY);
  if (existing) return existing;
  const value = `${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
  localStorage.setItem(SESSION_STORAGE_KEY, value);
  return value;
}

export async function apiRequest(path, options = {}, accessToken = null) {
  const headers = {
    "X-Session-ID": getSessionId(),
    ...(options.headers || {}),
  };

  if (accessToken) {
    headers.Authorization = `Bearer ${accessToken}`;
  }

  const method = (options.method || "GET").toUpperCase();
  let data = undefined;
  if (options.body) {
    data = typeof options.body === "string" ? JSON.parse(options.body) : options.body;
  }

  try {
    const response = await client.request({
      url: path,
      method,
      headers,
      data: ["POST", "PUT", "PATCH"].includes(method) ? data : undefined,
    });
    return response.data === "" || response.data == null ? {} : response.data;
  } catch (err) {
    if (axios.isAxiosError(err) && err.response?.data) {
      const b = err.response.data;
      const message = b.detail || b.error || (typeof b === "string" ? b : "Request failed");
      throw new Error(typeof message === "string" ? message : JSON.stringify(message));
    }
    throw err;
  }
}

export async function loginApi(payload) {
  return apiRequest("/auth/login/", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

export async function registerApi(payload) {
  return apiRequest("/auth/register/", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

export async function meApi(accessToken) {
  return apiRequest("/auth/me/", { method: "GET" }, accessToken);
}

export async function refreshTokenApi(refresh) {
  return apiRequest("/auth/refresh/", {
    method: "POST",
    body: JSON.stringify({ refresh }),
  });
}

export async function getPublicCoursesApi() {
  return apiRequest("/public/courses/", { method: "GET" });
}

export async function getCoursesApi(accessToken) {
  return apiRequest("/courses/", { method: "GET" }, accessToken);
}

export async function getStudentDashboardApi(accessToken) {
  return apiRequest("/dashboard/student/", { method: "GET" }, accessToken);
}

export async function getAdminDashboardApi(accessToken) {
  return apiRequest("/dashboard/admin/", { method: "GET" }, accessToken);
}

export async function enrollCourseApi(courseId, accessToken) {
  return apiRequest(
    "/learning/enroll/",
    {
      method: "POST",
      body: JSON.stringify({ course: courseId }),
    },
    accessToken,
  );
}

export async function getLessonsApi(accessToken) {
  return apiRequest("/lessons/", { method: "GET" }, accessToken);
}

export async function getLessonDetailApi(lessonId, accessToken) {
  return apiRequest(`/learning/lessons/${lessonId}/`, { method: "GET" }, accessToken);
}

export async function submitAnswerApi(payload, accessToken) {
  return apiRequest(
    "/learning/submit-answer/",
    {
      method: "POST",
      body: JSON.stringify(payload),
    },
    accessToken,
  );
}

export async function completeLessonApi(payload, accessToken) {
  return apiRequest(
    "/learning/complete-lesson/",
    {
      method: "POST",
      body: JSON.stringify(payload),
    },
    accessToken,
  );
}

export async function getRecommendationsApi(accessToken) {
  return apiRequest("/recommendations/", { method: "GET" }, accessToken);
}

export async function getMLFeatureDistributionApi(accessToken) {
  return apiRequest("/ml/feature-distribution/", { method: "GET" }, accessToken);
}

export async function getMLModelStatusApi(accessToken) {
  return apiRequest("/ml/model-status/", { method: "GET" }, accessToken);
}

export async function retrainMLModelApi(accessToken) {
  return apiRequest("/ml/retrain/", { method: "POST", body: "{}" }, accessToken);
}

export async function createCourseApi(payload, accessToken) {
  return apiRequest("/courses/", { method: "POST", body: JSON.stringify(payload) }, accessToken);
}

export async function patchCourseApi(courseId, payload, accessToken) {
  return apiRequest(`/courses/${courseId}/`, { method: "PATCH", body: JSON.stringify(payload) }, accessToken);
}

export async function deleteCourseApi(courseId, accessToken) {
  return apiRequest(`/courses/${courseId}/`, { method: "DELETE" }, accessToken);
}

export async function createLessonApi(payload, accessToken) {
  return apiRequest("/lessons/", { method: "POST", body: JSON.stringify(payload) }, accessToken);
}

export async function patchLessonApi(lessonId, payload, accessToken) {
  return apiRequest(`/lessons/${lessonId}/`, { method: "PATCH", body: JSON.stringify(payload) }, accessToken);
}

export async function deleteLessonApi(lessonId, accessToken) {
  return apiRequest(`/lessons/${lessonId}/`, { method: "DELETE" }, accessToken);
}

export async function createQuestionApi(payload, accessToken) {
  return apiRequest("/questions/", { method: "POST", body: JSON.stringify(payload) }, accessToken);
}

export async function patchQuestionApi(questionId, payload, accessToken) {
  return apiRequest(`/questions/${questionId}/`, { method: "PATCH", body: JSON.stringify(payload) }, accessToken);
}

export async function deleteQuestionApi(questionId, accessToken) {
  return apiRequest(`/questions/${questionId}/`, { method: "DELETE" }, accessToken);
}

export async function getQuestionsApi(accessToken) {
  return apiRequest("/questions/", { method: "GET" }, accessToken);
}

export async function changePasswordApi(payload, accessToken) {
  return apiRequest("/auth/change-password/", { method: "POST", body: JSON.stringify(payload) }, accessToken);
}

export async function updateProfileApi(payload, accessToken) {
  return apiRequest("/auth/update-profile/", { method: "PATCH", body: JSON.stringify(payload) }, accessToken);
}
