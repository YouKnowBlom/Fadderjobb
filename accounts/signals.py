from django.db.models.signals import m2m_changed

from .models import User, BonusPoints


def bonus_points_changed(sender, **kwargs):
    # TODO: fix this
    print("äåndra")


m2m_changed.connect(bonus_points_changed, sender=User.bonus_points.through)
