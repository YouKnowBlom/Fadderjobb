from accounts.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Send activation link to users'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user to send activation email')

    def handle(self, *args, **options):
        username = options['username']

        try:
            # Get the user with the provided username
            user = User.objects.get(username=username)

            user.send_activation_email()

            self.stdout.write(self.style.SUCCESS(f'Activation email sent successfully to {user.username}!'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User with username {username} does not exist!'))