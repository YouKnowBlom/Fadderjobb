from fadderjobb.settings_shared import *

DEBUG = False

SECRET_KEY_PATH = os.path.join(BASE_DIR, "fadderjobb", "secret_key.txt")

CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")


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
