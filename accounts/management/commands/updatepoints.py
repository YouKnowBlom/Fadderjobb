from django.core.management.base import BaseCommand

from accounts.models import User
from accounts.utils import update_user_placings

class Command(BaseCommand):
    help = 'Re-calculate points and placings for all users'

    def handle(self, *args, **options):
        for user in User.objects.filter().all():
            user.update_points()
        update_user_placings()