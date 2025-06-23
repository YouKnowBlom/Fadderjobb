from fadderjobb.settings_shared import *

DEBUG = False

SECRET_KEY_PATH = os.path.join(BASE_DIR, "fadderjobb", "secret_key.txt")

load_dotenv(find_dotenv())


def load_secret_key():
    if os.path.isfile(SECRET_KEY_PATH):
        with open(SECRET_KEY_PATH) as file:
            return file.read()
    else:
        from django.utils.crypto import get_random_string

        chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
        secret = get_random_string(50, chars)

        with open(SECRET_KEY_PATH, "w") as file:
            file.write(secret)

        return secret


SECRET_KEY = load_secret_key()


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("DB_NAME", "fadderjobb"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", ""),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
    }
}


# Email
# https://docs.djangoproject.com/en/2.1/topics/email/

EMAIL_BACKEND = "post_office.EmailBackend"

EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")

EMAIL_PORT = os.environ.get("EMAIL_PORT", 587)

EMAIL_HOST_USER = os.getenv("EMAIL_USER")

EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")

EMAIL_USE_TLS = True

# NOTE: For now, it's enough to log directly to console
# as you can view console output through docker compose.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": [
            "console",
        ],
        "level": "INFO",
    },
    "loggers": {
        "django.request": {
            "handlers": [
                "console",
            ],
            "level": "INFO",
            "propagate": True,
        },
        "post_office": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "post_office",
        },
    },
}
