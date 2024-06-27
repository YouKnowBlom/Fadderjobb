from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Creates a new user."

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="The username of the new user.")
        parser.add_argument("password", type=str, help="The password for the new user.")

    def handle(self, *args, **options):
        username = options["username"]
        password = options["password"]

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR('User "%s" already exists.' % username))
            return

        user = User.objects.create_user(username=username, password=password)
        user.save()

        self.stdout.write(self.style.SUCCESS('Successfully created user "%s".' % username))