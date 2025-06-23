from .models import User
from django.db.models import F


def update_user_placings():
    users = User.objects.order_by(F("is_staff"), F("points").desc()).all()

    for i, user in enumerate(users):
        user.placing = i + 1

    User.objects.bulk_update(users, ["placing"], batch_size=20)
