# TOEIC Learning Analytics

Ứng dụng web học TOEIC theo hướng phân tích hành vi học tập real-time và cá nhân hóa lộ trình học.

## Tài liệu quan trọng

- [TIEN_DO_DU_AN.md](TienDo.md): nguồn sự thật về tiến độ thực thi.
- [TaiLieu_LyThuyet_HeThong.md](README.md): tài liệu lý thuyết và thiết kế hệ thống.

## Trạng thái hiện tại

Project đã hoàn thành **P7 — Redis, Docker Compose, README**.

## Stack

- Backend: `Django` + `Django REST Framework` + `SimpleJWT`
- Frontend: `React` + `Vite`
- Database: `PostgreSQL`
- Cache: `Redis`
- ML: `scikit-learn`, `pandas`
- MLOps: `MLflow`
- Container: `Docker`, `Docker Compose`

## Chạy nhanh bằng Docker Compose

Yêu cầu:

- Đã cài Docker Desktop (hoặc Docker Engine + Compose plugin)

### 1) Build và chạy services

```bash
docker compose up -d --build
```

Khi backend khởi động, hệ thống tự động:

- chạy `migrate`
- tạo tài khoản admin mặc định
- seed dữ liệu demo quy mô lớn (khóa học/bài học/câu hỏi + học viên + attempts)
- train model baseline

Services sau khi lên:

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend API: [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)
- Django Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- MLflow: [http://localhost:5000](http://localhost:5000)
- PostgreSQL: `localhost:5432`
- pgAdmin: [http://localhost:5050](http://localhost:5050)
- Redis Commander: [http://localhost:8081](http://localhost:8081)
- Redis: `localhost:6379`

### 2) Tài khoản demo mặc định

- Admin login:
  - email: `admin`
  - password: `admin123`
- Student demo:
  - email dạng `student001@demo.local` ... `student080@demo.local`
  - password: `student123`

### 3) Tùy chọn chạy lại train model

```bash
docker compose exec backend python manage.py train_level_model
```

### 4) (Tuỳ chọn) seed lại dữ liệu demo

```bash
docker compose exec backend python manage.py seed_demo_data --force
```

Lưu ý: model `.joblib` được lưu trong volume `ml_artifacts_data` (mount vào `/app/ml_artifacts`), nên vẫn được giữ lại sau khi rebuild container backend.

### 5) Soạn khóa học bằng file JSON (import nội dung)

- **Mẫu cấu trúc:** `backend/courses/fixtures/course_IMPORT_TEMPLATE.json` (sao chép rồi sửa).
- **Kiểm tra không ghi DB:**

  ```bash
  docker compose exec backend python manage.py import_course_json --path courses/fixtures/my_course.json --dry-run
  ```

- **Import khóa mới** (tránh trùng `course_id` với khóa đã có, hoặc đổi `course_id` trong file):

  ```bash
  docker compose exec backend python manage.py import_course_json --path courses/fixtures/my_course.json
  ```

- **Ghi đè khóa đã tồn tại** (cùng `course_id` trong JSON = `external_id` trong DB; xóa khóa cũ và tiến độ liên quan rồi import lại):

  ```bash
  docker compose exec backend python manage.py import_course_json --path courses/fixtures/my_course.json --replace-if-exists
  ```

Logic import nằm ở `backend/courses/course_json_import.py` (`validate_course_payload`, `import_course_payload`) để sau này có thể gắn upload file từ Admin/API.

## Lệnh hữu ích

- Xem logs tất cả services:
  - `docker compose logs -f`
- Xem logs riêng backend:
  - `docker compose logs -f backend`
- Dừng hệ thống:
  - `docker compose down`
- Dừng và xóa volume:
  - `docker compose down -v`

## Chạy local không Docker (tùy chọn)

- Backend:
  - `cd backend`
  - `python -m venv .venv`
  - `.venv\Scripts\activate` (Windows)
  - `pip install -r requirements.txt`
  - `python manage.py migrate`
  - `python manage.py runserver`
- Frontend:
  - `cd frontend`
  - `npm install`
  - `npm run dev`

## Gợi ý khi mở chat mới

Nói: `Hãy đọc TIEN_DO_DU_AN.md và tiếp tục từ mục Next`.
