"""
Kiểm tra và tự động retrain model nếu chưa train hoặc đã quá 7 ngày.

    python manage.py auto_retrain              # retrain nếu cần
    python manage.py auto_retrain --force      # luôn retrain
    python manage.py auto_retrain --days 14    # ngưỡng 14 ngày

Để chạy định kỳ hàng tuần, xem retrain_cron.bat (Windows) hoặc thêm vào crontab:
    0 2 * * 1  cd /path/to/backend && python manage.py auto_retrain
"""

from __future__ import annotations

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import timezone

from ml.models import MLModel


class Command(BaseCommand):
    help = "Auto-retrain level prediction model nếu chưa có hoặc đã quá --days ngày."

    def add_arguments(self, parser):
        parser.add_argument("--days", type=int, default=7, help="Số ngày trước khi retrain (mặc định 7)")
        parser.add_argument("--force", action="store_true", help="Luôn retrain không kiểm tra thời gian")

    def handle(self, *args, **options):
        days = options["days"]
        force = options["force"]

        active = MLModel.objects.filter(name="level_predictor", is_active=True).order_by("-created_at").first()

        if force:
            self.stdout.write("--force: bắt đầu retrain...")
        elif active is None:
            self.stdout.write("Chưa có model nào. Bắt đầu train lần đầu...")
        else:
            age = timezone.now() - active.created_at
            if age.days < days:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Model hiện tại (version={active.version}) mới {age.days} ngày — chưa cần retrain (ngưỡng {days} ngày)."
                    )
                )
                return
            self.stdout.write(f"Model đã {age.days} ngày (> {days}). Bắt đầu retrain...")

        try:
            call_command("train_level_model")
            self.stdout.write(self.style.SUCCESS("Retrain hoàn thành."))
        except Exception as exc:
            self.stdout.write(self.style.ERROR(f"Retrain thất bại: {exc}"))
            raise
