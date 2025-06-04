from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Creates a superuser from environment variables or with defaults'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = os.environ.get("DJANGO_ADMIN_USERNAME", "admin")
        email = os.environ.get("DJANGO_ADMIN_EMAIL", "admin@example.com")
        password = os.environ.get("DJANGO_ADMIN_PASSWORD", None)

        if password == None:
            self.stdout.write(self.style.WARNING(f"You need to define DJANGO_ADMIN_PASSWORD in environment variables"))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"User '{username}' already exists."))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully."))
