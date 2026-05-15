from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Ensure a default Data Scientist account exists (staff, not superuser)."

    def add_arguments(self, parser):
        parser.add_argument("--email", default="ds@example.com")
        parser.add_argument("--username", default="datascientist")
        parser.add_argument("--password", default="ds123456")

    def handle(self, *args, **options):
        email = options["email"]
        username = options["username"]
        password = options["password"]

        user = User.objects.filter(email=email).first()
        created = False
        if user is None:
            user = User.objects.filter(username=username).first()
        if user is None:
            user = User(
                email=email,
                username=username,
                role=User.Role.DATA_SCIENTIST,
                is_staff=True,
                is_superuser=False,
            )
            created = True

        user.username = username
        user.email = email
        user.role = User.Role.DATA_SCIENTIST
        user.is_staff = True
        user.set_password(password)
        user.save()

        action = "created" if created else "updated"
        self.stdout.write(self.style.SUCCESS(f"Data Scientist {action}: {email} / {password}"))
