from accounts.cronjobs import update_points
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Re-calculate points and placings for all users'

    def handle(self, *args, **options):
        update_points(None)