from uwsgidecorators import cron

from .models import User
from .utils import update_user_placings


@cron(0, 0, -1, -1, -1)
def update_points(num):
    for user in User.objects.filter().all():
        user.update_points()
    update_user_placings()

@cron(5, -1, -1, -1, -1)
def send_activation_emails(num):
    for user in User.objects.filter(is_activated=False).all():
        user.send_activation_email()
