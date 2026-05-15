#!/bin/sh
set -e

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Ensuring default admin account..."
python manage.py ensure_default_admin \
  --email "${DJANGO_SUPERUSER_EMAIL:-admin}" \
  --username "${DJANGO_SUPERUSER_USERNAME:-admin}" \
  --password "${DJANGO_SUPERUSER_PASSWORD:-admin123}"

echo "Seeding demo data if needed..."
python manage.py seed_demo_data \
  --courses "${SEED_COURSES:-24}" \
  --lessons-per-course "${SEED_LESSONS_PER_COURSE:-24}" \
  --questions-per-lesson "${SEED_QUESTIONS_PER_LESSON:-6}" \
  --student-count "${SEED_STUDENT_COUNT:-80}"

echo "Training baseline model (if data allows)..."
python manage.py train_level_model || true

echo "Starting backend server..."
exec "$@"
