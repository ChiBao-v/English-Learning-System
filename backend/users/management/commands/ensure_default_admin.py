from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Ensure a default admin account exists."

    def add_arguments(self, parser):
        parser.add_argument("--email", default="admin@example.com")
        parser.add_argument("--username", default="admin")
        parser.add_argument("--password", default="admin123")

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
                role=User.Role.ADMIN,
                is_staff=True,
                is_superuser=True,
            )
            created = True

        user.username = username
        user.email = email
        user.role = User.Role.ADMIN
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        action = "created" if created else "updated"
        self.stdout.write(self.style.SUCCESS(f"Default admin {action}: {email}/{password}"))
