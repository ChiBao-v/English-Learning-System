import { Navigate, Route, Routes } from "react-router-dom";

import { AdminLayout } from "./components/AdminLayout.jsx";
import { AdminOnlyRoute } from "./components/AdminOnlyRoute.jsx";
import { AppLayout } from "./components/AppLayout.jsx";
import { ProtectedRoute } from "./components/ProtectedRoute.jsx";
import { StaffRoute } from "./components/StaffRoute.jsx";
import { useAuth } from "./context/useAuth.js";
import { AboutPage } from "./pages/AboutPage.jsx";
import { AdminDashboardPage } from "./pages/AdminDashboardPage.jsx";
import { AdminManageCoursesPage } from "./pages/AdminManageCoursesPage.jsx";
import { AdminManageLessonsPage } from "./pages/AdminManageLessonsPage.jsx";
import { AdminManageQuestionsPage } from "./pages/AdminManageQuestionsPage.jsx";
import { CoursesPage } from "./pages/CoursesPage.jsx";
import { DashboardPage } from "./pages/DashboardPage.jsx";
import { HomePage } from "./pages/HomePage.jsx";
import { LessonQuizPage } from "./pages/LessonQuizPage.jsx";
import { LessonStudyPage } from "./pages/LessonStudyPage.jsx";
import { LoginPage } from "./pages/LoginPage.jsx";
import { MLMonitorPage } from "./pages/MLMonitorPage.jsx";
import { AboutInAppPage } from "./pages/AboutInAppPage.jsx";
import { ProfilePage } from "./pages/ProfilePage.jsx";
import { RegisterPage } from "./pages/RegisterPage.jsx";
import { RoadmapPage } from "./pages/RoadmapPage.jsx";

function App() {
  const { isAuthenticated } = useAuth();

  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/about" element={<AboutPage />} />
      <Route path="/login" element={isAuthenticated ? <Navigate to="/courses" replace /> : <LoginPage />} />
      <Route path="/register" element={isAuthenticated ? <Navigate to="/courses" replace /> : <RegisterPage />} />
      <Route
        element={
          <ProtectedRoute>
            <AppLayout />
          </ProtectedRoute>
        }
      >
        <Route path="courses" element={<CoursesPage />} />
        <Route path="lessons/:lessonId" element={<LessonStudyPage />} />
        <Route path="lessons/:lessonId/quiz" element={<LessonQuizPage />} />
        <Route path="dashboard" element={<DashboardPage />} />
        <Route path="profile" element={<ProfilePage />} />
        <Route path="roadmap" element={<RoadmapPage />} />
        <Route path="about" element={<AboutInAppPage />} />
        <Route
          path="admin"
          element={
            <StaffRoute>
              <AdminLayout />
            </StaffRoute>
          }
        >
          <Route index element={<AdminDashboardPage />} />
          <Route path="ml" element={<MLMonitorPage />} />
          <Route
            path="courses"
            element={
              <AdminOnlyRoute>
                <AdminManageCoursesPage />
              </AdminOnlyRoute>
            }
          />
          <Route
            path="lessons"
            element={
              <AdminOnlyRoute>
                <AdminManageLessonsPage />
              </AdminOnlyRoute>
            }
          />
          <Route
            path="questions"
            element={
              <AdminOnlyRoute>
                <AdminManageQuestionsPage />
              </AdminOnlyRoute>
            }
          />
        </Route>
      </Route>
      <Route path="*" element={<Navigate to={isAuthenticated ? "/courses" : "/"} replace />} />
    </Routes>
  );
}

export default App;
