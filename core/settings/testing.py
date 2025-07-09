from .settings import *

SECRET_KEY = "lkanp9cij120indpsn9inpou98jf-20mnoiushj-9wmnp89f=osnm98euijhf0sd"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
