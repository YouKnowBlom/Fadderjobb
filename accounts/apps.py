from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "accounts"

    def ready(self):
        from . import signals

        try:
            import uwsgidecorators
            from . import cronjobs
        except ImportError:
            pass
