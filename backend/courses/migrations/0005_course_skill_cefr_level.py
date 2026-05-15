# Generated manually for skill + CEFR band

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_course_external_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="skill",
            field=models.CharField(
                choices=[
                    ("general", "General"),
                    ("listening", "Listening"),
                    ("reading", "Reading"),
                    ("writing", "Writing"),
                    ("speaking", "Speaking"),
                ],
                default="general",
                help_text="Kỹ năng chính của khóa (listening, reading, …).",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="cefr_level",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Band CEFR hiển thị: A1, A2, B1, B2, …",
                max_length=8,
            ),
        ),
    ]
