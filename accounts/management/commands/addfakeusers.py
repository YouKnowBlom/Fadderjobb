from django.core.management.base import BaseCommand, CommandError

# from django.utils import timezone
# import datetime
from django.contrib.auth import get_user_model
from faker import Faker

# YEAR = timezone.now().year


User = get_user_model()


class Command(BaseCommand):
    help = (
        "Inserts some default user data to the database. Useful for local environments."
    )

    def handle(self, *args, **options):
        fake = Faker("sv-SE")
        fake.seed_instance(69)

        for i in range(80):
            fn = fake.first_name()
            ln = fake.last_name()
            username = (fn[:3] + ln[:2] + str(fake.random_int(max=999))).lower()
            user, created = User.objects.get_or_create(username=username)
            user.name = f"{fn} {ln}"
            user.email = f"{username}@student.liu.se"
            user.save()
