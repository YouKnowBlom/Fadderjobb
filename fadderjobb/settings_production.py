from fadderjobb.settings_shared import *

DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "NAME": os.environ.get("DB_NAME", "fadderjobb"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", ""),
        "USER": credentials["database"]["user"],
        "PASSWORD": credentials["database"]["password"],
    }
}


# Email
# https://docs.djangoproject.com/en/2.1/topics/email/

EMAIL_BACKEND = "post_office.EmailBackend"

EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")

EMAIL_PORT = os.environ.get("EMAIL_PORT", 587)

EMAIL_HOST_USER = credentials["email"]["user"]

EMAIL_HOST_PASSWORD = credentials["email"]["password"]

EMAIL_USE_TLS = True
