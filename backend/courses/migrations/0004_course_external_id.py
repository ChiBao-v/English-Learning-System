from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_question_image_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="external_id",
            field=models.CharField(
                blank=True,
                default="",
                db_index=True,
                max_length=32,
                help_text="Mã khóa trong file JSON (vd: C01); dùng để hiển thị tên chuẩn.",
            ),
        ),
    ]
