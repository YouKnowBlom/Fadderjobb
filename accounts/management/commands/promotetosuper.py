from django.core.management.base import BaseCommand, CommandError
from accounts.models import User


class Command(BaseCommand):
    help = "Promotes an existing user to superuser."

    def add_arguments(self, parser):
        parser.add_argument("username", nargs="+", type=str)

    def handle(self, *args, **options):
        for username in options["username"]:
            user = User.objects.get(username=username)

            user.is_staff = True
            user.is_superuser = True
            user.save()

            self.stdout.write(
                self.style.SUCCESS('Successfully promoted user "%s" to superuser' % username)
            )
