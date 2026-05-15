"""Kiểm tra validate và import JSON khóa học."""

import json
from pathlib import Path

import pytest

from courses.course_json_import import (
    CourseJsonImportError,
    import_course_payload,
    validate_course_payload,
)
from courses.models import Course, Lesson, Question

pytestmark = pytest.mark.django_db

FIXTURES = Path(__file__).resolve().parent.parent / "courses" / "fixtures"
TEMPLATE = FIXTURES / "course_IMPORT_TEMPLATE.json"


def test_validate_rejects_empty():
    errors = validate_course_payload({})
    assert any("course_name" in e for e in errors)
    assert any("lessons" in e for e in errors)


def test_validate_accepts_template():
    data = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    assert validate_course_payload(data) == []


def test_import_template_creates_content():
    data = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    data = {**data, "course_id": "C pytest_import_01", "course_name": "Pytest Import Course"}
    course, n_lessons, n_questions = import_course_payload(data)
    assert n_lessons == 1
    assert n_questions == 1
    assert course.external_id == "C pytest_import_01"
    assert Lesson.objects.filter(course=course).count() == 1
    assert Question.objects.filter(lesson__course=course).count() == 1


def test_replace_if_exists_swaps_course():
    data = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    data = {**data, "course_id": "C pytest_replace", "course_name": "First title"}
    import_course_payload(data)
    assert Course.objects.filter(external_id="C pytest_replace").count() == 1

    data2 = {**data, "course_name": "Second title"}
    import_course_payload(data2, replace_if_exists=True)
    assert Course.objects.filter(external_id="C pytest_replace").count() == 1
    c = Course.objects.get(external_id="C pytest_replace")
    assert c.title == "Second title"


def test_replace_without_course_id_errors():
    data = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    data = {**data, "course_id": "", "course_name": "No id"}
    with pytest.raises(CourseJsonImportError, match="replace-if-exists"):
        import_course_payload(data, replace_if_exists=True)
