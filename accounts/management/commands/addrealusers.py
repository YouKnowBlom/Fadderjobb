import csv
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    help = (
        "Inserts users from a headerless CSV file of shape: name, username, phone_number, email"
    )

    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **options):
        file_name = options.get("file_name")
        if not file_name:
            raise CommandError("File name is required")

        with open(file_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            users = [User(
                name=row[0],
                username=row[1].lower(),
                phone_number=row[2],
                email=row[3],
            ) for row in reader]
            User.objects.bulk_create(users, ignore_conflicts=True)
